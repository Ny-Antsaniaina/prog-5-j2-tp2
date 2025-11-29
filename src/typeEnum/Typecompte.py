from enum import Enum


class TypeCompte(Enum):
    CREDITCARD = "CreditCard"
    BANKTRANSFER = "BankTransfer"
    CASH = "Cash"
    CHEQUE = "Cheque"
    