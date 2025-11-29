import logging

from repository.PayementMethod import PaymentMethod
from utils.converter import convertToAr
class BankTransferPayment(PaymentMethod):
    FEES = 0.01

    def pay(self, user, amountAr):
        acc = next((a for a in user.accounts if a.typeCompte == a.typeCompte.BANKTRANSFER), None)
        if not acc:
            raise ValueError("User has no BANK TRANSFER account.")

        total = amountAr * (1 + self.FEES)

        if convertToAr(acc.money, acc.devise) < total:
            raise ValueError("Insufficient bank balance.")
        user.payAr(total, acc)
        logging.info(f"{user.name} paid {total} Ar via BANK TRANSFER (1% fees).")
        return total
    