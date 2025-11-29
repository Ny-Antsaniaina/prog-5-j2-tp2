
import logging
from repository.PayementMethod import PaymentMethod
from utils.converter import convertToAr


class ChequePayment(PaymentMethod):
    def pay(self, user, amountAr):
        acc = next((a for a in user.accounts if a.typeCompte == a.typeCompte.CHEQUE), None)
        if not acc:
            raise ValueError("User has no CHEQUE account.")

        if convertToAr(acc.money, acc.devise) < amountAr:
            raise ValueError("Insufficient cheque balance.")
        user.payAr(amountAr, acc)
        logging.info(f"{user.name} paid {amountAr} Ar by CHEQUE.")
        return amountAr