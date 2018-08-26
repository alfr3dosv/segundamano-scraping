from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import config

engine = create_engine(config.url)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()