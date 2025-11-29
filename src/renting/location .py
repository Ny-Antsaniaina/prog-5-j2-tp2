from dataclasses import dataclass
from datetime import datetime
from entity import Item
from entity.baseEntity import BaseEntity

@dataclass
class LocationRecord:
    user: BaseEntity
    item: Item
    quantity: int
    totalPrice: float
    date: datetime
