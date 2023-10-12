class VendingMachine:
    def __init__(self):
        self.beverages = []
        self.cards = []

    def addBeverage(self, name, price):
        beverage = {
            "name": name,
            "price": price
        }
        self.beverages.append(beverage)

    def getPrice(self, name):
        for beverage in self.beverages:
            if beverage["name"] == name:
                return beverage["price"]
        return -1.0

    def rechargeCard(self, card_id, credit):
        for card in self.cards:
            if card["id"] == card_id:
                card["credit"] += credit
                return
        new_card = {
            "id": card_id,
            "credit": credit
        }
        self.cards.append(new_card)

    def getCredit(self, card_id):
        for card in self.cards:
            if card["id"] == card_id:
                return card["credit"]
        return -1.0

vm = VendingMachine()

vm.addBeverage("Coca Cola", 3200)
vm.addBeverage("Suv", 1000)
vm.addBeverage("Pepsi", 2500)

print(vm.getPrice("Coca Cola")) 
# print(vm.getPrice("Sprite"))    


vm.rechargeCard(12, 12800)
vm.rechargeCard(21, 5600)
vm.rechargeCard(99, 15800)

print(vm.getCredit(12))  
# print(vm.getCredit(50)) 