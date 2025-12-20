from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
import datetime

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())

    scores = relationship("LeaderboardEntry", back_populates="player")

class Map(Base):
    __tablename__ = 'maps'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    campaign_id = Column(String, nullable=False)

    leaderboards = relationship("Leaderboard", back_populates="map")

class Leaderboard(Base):
    __tablename__ = 'leaderboards'
    id = Column(Integer, primary_key=True, autoincrement=True)
    map_id = Column(String, ForeignKey('maps.id'), nullable=False)
    fetched_at = Column(DateTime, server_default=func.now())

    map = relationship("Map", back_populates="leaderboards")
    entries = relationship("LeaderboardEntry", back_populates="leaderboard", cascade="all, delete-orphan")

class LeaderboardEntry(Base):
    __tablename__ = 'leaderboard_entries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    leaderboard_id = Column(Integer, ForeignKey('leaderboards.id'), nullable=False)
    player_id = Column(String, ForeignKey('players.id'), nullable=False)
    score = Column(BigInteger, nullable=False)  # Time in milliseconds
    club_position = Column(Integer)
    global_position = Column(Integer)

    leaderboard = relationship("Leaderboard", back_populates="entries")
    player = relationship("Player", back_populates="scores")


class RoomInfo(Base):
    __tablename__ = 'room_info'
    id = Column(String, primary_key=True) # room_id
    name = Column(String)
    active_players = Column(Integer, default=0)
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())

