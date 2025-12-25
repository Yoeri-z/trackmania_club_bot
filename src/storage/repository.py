from sqlalchemy import func, and_
from sqlalchemy.orm import Session, aliased
from typing import Type, TypeVar, Generic, List, Optional
from src.storage.models import Base, Player, Map, LeaderboardEntry, RoomInfo
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

    def upsert(self, unique_filters: dict, **kwargs) -> T:
        instance = self.session.query(self.model).filter_by(**unique_filters).first()
        if instance:
            instance = self.update(instance.id, **kwargs)
        else:
            instance = self.create(**kwargs)

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

    def get_tracked(self) -> list[Map]:
        return self.session.query(Map).filter(Map.channel_id.isnot(None)).all()


class LeaderboardRepository(BaseRepository[LeaderboardEntry]):
    def __init__(self, session: Session):
        super().__init__(session, LeaderboardEntry)

    def get_latest_for_map(self, map_id: str) -> list[LeaderboardEntry]:
        subq = (
            self.session.query(
                LeaderboardEntry.player_id,
                func.max(LeaderboardEntry.fetched_at).label("latest"),
            )
            .filter(LeaderboardEntry.map_id == map_id)
            .group_by(LeaderboardEntry.player_id)
            .subquery()
        )

        return (
            self.session.query(LeaderboardEntry)
            .join(
                subq,
                and_(
                    LeaderboardEntry.player_id == subq.c.player_id,
                    LeaderboardEntry.fetched_at == subq.c.latest,
                ),
            )
            .order_by(LeaderboardEntry.fetched_at.desc())
            .limit(100)
            .all()
        )

    def compare(
        self, new_entry: LeaderboardEntry
    ) -> tuple[LeaderboardEntry, LeaderboardEntry | None] | None:
        # TODO: Check if there is an old entry
        old_entry = (
            self.session.query(LeaderboardEntry)
            .filter(LeaderboardEntry.player_id == new_entry.player_id)
            .first()
        )

        if not old_entry or new_entry.score >= old_entry.score:
            return None
        else:
            return new_entry, old_entry


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
