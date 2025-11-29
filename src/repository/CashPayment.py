import logging

from repository.PayementMethod import PaymentMethod
from utils.converter import convertToAr

class CashPayment(PaymentMethod):

    def pay(self, user, amountAr):
        acc = next((a for a in user.accounts if a.typeCompte == a.typeCompte.CASH), None)
        if not acc:
            raise ValueError("User has no CASH account.")

        if convertToAr(acc.money, acc.devise) < amountAr:
            raise ValueError("Insufficient cash balance.")

        user.payAr(amountAr)
        logging.info(f"{user.name} paid {amountAr} Ar in CASH.")
        return amountAr