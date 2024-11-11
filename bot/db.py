import os

from dotenv import load_dotenv
from sqlalchemy import Column, Text, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import StaticPool

load_dotenv()

engine = create_engine(
    os.getenv('BOT_DATABASE_URL'),
    echo=True,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

Base = declarative_base()


class UserSettings(Base):
    __tablename__ = 'user_settings'
    id = Column(Integer, primary_key=True)
    text = Column(Text, default='NOT FOR DISTRIBUTION')
    chat_id = Column(Integer, unique=True, nullable=False)
    transparency = Column(Integer, default=64)
    front_size = Column(Integer, default=20)
    front = Column(Text)
    position_x = Column(Integer, default=10)
    position_y = Column(Integer, default=10)


Base.metadata.create_all(engine)
Session = scoped_session(sessionmaker(bind=engine))
session = Session()
