import logging
from datetime import datetime
from entity import item
from entity.baseEntity import BaseEntity
from repository import PaymentMethod
from utils.converter import convertToAr
from renting import LocationRevord

class RentingSystem:
    def __init__(self):
        self.locations: list[LocationRevord] = []

    def rent(self, user: BaseEntity, item: item, quantity: int, payment: PaymentMethod):

        if item.quantity < quantity:
            raise ValueError("Not enough quantity available.")

        priceAr = convertToAr(item.price, item.devise) * quantity

        if user.getMoneyInAr() < priceAr:
            raise ValueError("User does not have enough money for this rental.")

        totalPaid = PaymentMethod.pay(user, priceAr)
        

        item.quantity -= quantity

        record = LocationRevord(
            user=user,
            item=item,
            quantity=quantity,
            totalPrice=priceAr,
            date=datetime.now()
        )
        self.locations.append(record)

        logging.info(f"{user.name} rented {quantity} x {item.name} for {totalPaid} Ar.")
        return record
