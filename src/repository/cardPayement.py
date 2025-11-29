import logging
from repository import PayementMethod
from utils.converter import convertToAr, CONVERSION

class CardPayment(PayementMethod):
    FEES = 0.03  

    def pay(self, user, amountAr: float):

        acc = next((a for a in user.accounts if a.typeCompte == a.typeCompte.CREDITCARD), None)
        if not acc:
            raise ValueError("User has no CARD account.")

        total = amountAr * (1 + self.FEES)

        if convertToAr(acc.money, acc.devise) < total:
            raise ValueError("Insufficient card balance.")

        user.payAr(total)
        logging.info(f"{user.name} paid {total} Ar with CARD (3% fees).")
        return total
