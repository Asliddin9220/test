class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self):
        self.beverages = []
        self.cards = []
        self.columns = []

    def addBeverage(self, name, price):
        beverage = Beverage(name, price)
        self.beverages.append(beverage)

    def getPrice(self, name):
        for beverage in self.beverages:
            if beverage.name == name:
                return beverage.price
        return -1.0

    def rechargeCard(self, card_id, credit):
        for card in self.cards:
            if card.card_id == card_id:
                card.credit += credit
                return
        new_card = Card(card_id, credit)
        self.cards.append(new_card)

    def getCredit(self, card_id):
        for card in self.cards:
            if card.card_id == card_id:
                return card.credit
        return -1.0

    def refillColumn(self, column_number, name, quantity):
        column = Column(column_number, name, quantity)
        self.columns.append(column)

    def availableCans(self, name):
        count = 0
        for column in self.columns:
            if column.name == name:
                count += column.quantity
        return count


class Card:
    def __init__(self, card_id, credit):
       self.card_id = card_id
       self.credit = credit


class Column:
    def __init__(self, number, name ,quantity):
       self.number = number
       self.name = name
       self.quantity = quantity




vending_machine = VendingMachine()


vending_machine.addBeverage("Coca Cola", 3200)
vending_machine.addBeverage("Suv", 1000)
vending_machine.addBeverage("Pepsi", 2500)


print(vending_machine.getPrice("Coca Cola")) 


vending_machine.rechargeCard(12, 12000)


print(vending_machine.getCredit(12)) 

vending_machine.refillColumn(1, "Coca Cola", 1)
vending_machine.refillColumn(2, "Suv", 10)
vending_machine.refillColumn(3, "Pepsi", 15)
vending_machine.refillColumn(4, "Suv", 20)


print(vending_machine.availableCans("Suv")) 