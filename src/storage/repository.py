from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List, Optional
from src.storage.models import Base, Player, Map, Leaderboard, RoomInfo
from src.storage.database import SessionLocal

# Base is a type, python does not see that.
T = TypeVar("T", bound=Base)  # type: ignore


class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def get(self, id: any) -> Optional[T]:
        return self.session.query(self.model).get(id)

    def get_all(self) -> List[T]:
        return self.session.query(self.model).all()

    def create(self, **kwargs) -> T:
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def update(self, id: any, **kwargs) -> Optional[T]:
        instance = self.get(id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            self.session.commit()
            self.session.refresh(instance)
        return instance

    def delete(self, id: any) -> bool:
        instance = self.get(id)
        if instance:
            self.session.delete(instance)
            self.session.commit()
            return True
        return False


# Specific Repositories
class PlayerRepository(BaseRepository[Player]):
    def __init__(self, session: Session):
        super().__init__(session, Player)


class MapRepository(BaseRepository[Map]):
    def __init__(self, session: Session):
        super().__init__(session, Map)


class LeaderboardRepository(BaseRepository[Leaderboard]):
    def __init__(self, session: Session):
        super().__init__(session, Leaderboard)

    def get_latest_for_map(self, map_id: str) -> Optional[Leaderboard]:
        return (
            self.session.query(Leaderboard)
            .filter_by(map_id=map_id)
            .order_by(Leaderboard.fetched_at.desc())
            .first()
        )


class RoomInfoRepository(BaseRepository[RoomInfo]):
    def __init__(self, session: Session):
        super().__init__(session, RoomInfo)


# Example of how to use the repositories
if __name__ == "__main__":
    db_session = SessionLocal()

    player_repo = PlayerRepository(db_session)

    # Example: Create a player
    # new_player = player_repo.create(id='test_player_id', name='Test Player')
    # print(f"Created Player: {new_player.id} - {new_player.name}")

    # Example: Get a player
    # a_player = player_repo.get('test_player_id')
    # if a_player:
    #     print(f"Found Player: {a_player.name}")

    db_session.close()
