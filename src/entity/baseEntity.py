from dataclasses import dataclass

from attr import field
from entity import acount
from utils.converter import CONVERSION, convertToAr

@dataclass
class BaseEntity:
    name: str
    acounts : list[acount.Account] = field(default_factory=list)

    def getMoneyInAr(self) -> float:
        return sum(convertToAr(acc.money, acc.devise) for acc in self.accounts)

    def payAr(self, amountAr: float , account: acount) -> None:
        acount.money -= amountAr / CONVERSION[acount.devise]
