from entity.item import Item
from entity.acount import Account
from entity.person import Person
from renting.rentingSystem import RentingSystem
from repository.cardPayement import CardPayment
from typeEnum.Typecompte import TypeCompte
from typeEnum.devise import Devise
from typeEnum.typeItem import TypeItem


class Main:  
    @staticmethod
    def run():
        user = Person(name="Ben")

        user.acounts.append(Account(
           typeCompte=TypeCompte.CREDITCARD,
           money=100,
           devise=Devise.DOLLAR
        ))

        user.acounts.append(Account(
            typeCompte=TypeCompte.CASH,
            money=50,
            devise=Devise.AR
        ))

        user.acounts.append(Account(
           typeCompte=TypeCompte.CHEQUE,
           money=20,
           devise=Devise.EURO
         ))


        car = Item(
          name="Toyota",
          price=10,
          devise=Devise.DOLLAR,
          quantity=5,
          typeItem=TypeItem.CAR
       )

        renting = RentingSystem()
        payment = CardPayment()

        renting.rent(user, car, 1, payment)


if __name__ == "__main__":
    Main.run()