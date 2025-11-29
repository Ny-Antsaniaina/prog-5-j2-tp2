
from typeEnum.devise import Devise


CONVERSION = {
    Devise.AR: 1,
    Devise.DOLLAR: 5000,
    Devise.EURO: 6000
}

def convertToAr(amount: float, devise: Devise) -> float:
    return amount * CONVERSION[devise]
