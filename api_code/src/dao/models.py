from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Investor(Base):
    __tablename__ = "investors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    country = Column(String)
    date_added = Column(Date)
    last_updated = Column(Date)

    commitments = relationship("Commitment", back_populates="investor", lazy="joined")

class Commitment(Base):
    __tablename__ = "commitments"

    id = Column(Integer, primary_key=True, index=True)
    investor_id = Column(Integer, ForeignKey("investors.id"))
    asset_class = Column(String)
    amount = Column(Float)
    currency = Column(String)

    investor = relationship("Investor", back_populates="commitments")
