from dataclasses import dataclass
from typeEnum.devise import Devise
from typeEnum.typeItem import TypeItem


@dataclass
class Item:
    name: str
    price: float
    devise: Devise
    quantity: int
    typeItem: TypeItem
