from sqlalchemy import Boolean, Column, BigInteger, ForeignKey, String, DateTime, Table, Text
# from sqlalchemy.orm import relationship
from src.db.base_class import Base
from datetime import datetime

class Post(Base):
  id = Column(BigInteger, primary_key=True, index=True)
  title = Column(String, index=True)
  content = Column(Text)
  created_at = Column(DateTime, default=datetime.now)
  published_at = Column(DateTime, nullable=True)
  published = Column(Boolean, default=False)
  author_id = Column(BigInteger, ForeignKey('author.id'))

    # Relaciones