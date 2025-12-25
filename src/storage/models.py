from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    Float,
    DateTime,
    ForeignKey,
    BigInteger,
)
from sqlalchemy.orm import Mapped, relationship, declarative_base
from sqlalchemy.sql import func

# Make two way type defenitions work
from __future__ import annotations

import datetime

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    id = Column(String, primary_key=True)
    account_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    blacklisted = Column(Boolean, nullable=False)
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())

    scores: Mapped[list[LeaderboardEntry]] = relationship(
        "LeaderboardEntry", back_populates="player"
    )


class Map(Base):
    __tablename__ = "maps"
    id = Column(String, primary_key=True)
    map_uid = Column(String, nullable=False)
    name = Column(String, nullable=False)
    campaign_id = Column(String, nullable=False)
    # The channel in which to send leaderboard updates of the map
    # if null, it means the map is untracked.
    channel_id = Column(Integer, nullable=True)


class LeaderboardEntry(Base):
    __tablename__ = "leaderboard_entries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    map_id = Column(Integer, ForeignKey("maps.id"), nullable=False)
    player_id = Column(String, ForeignKey("players.id"), nullable=False)
    score = Column(Integer, nullable=False)  # Time in milliseconds
    club_position = Column(Integer, nullable=False)
    global_position = Column(Integer)
    fetched_at = Column(DateTime, nullable=False)

    map: Mapped[Map] = relationship("Map")
    player: Mapped[Player] = relationship("Player", back_populates="scores")


class RoomInfo(Base):
    __tablename__ = "room_info"
    id = Column(String, primary_key=True)  # room_id
    name = Column(String)
    active_players = Column(Integer, default=0)
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())
