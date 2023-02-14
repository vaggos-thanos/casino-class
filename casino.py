class Casino:
    def __init__(self, cid, moneyIn, moneyOut):
        self.cid = cid
        while moneyIn < 0:
            moneyIn = int(input("Please enter a positive number: "))
        self.moneyIn = moneyIn
        while moneyOut < 0:
            moneyOut = int(input("Please enter a positive number: "))
        self.moneyOut = moneyOut

    def win_loose(self):
        if self.moneyIn < self.moneyOut:
            return "Win"
        elif self.moneyIn > self.moneyOut:
            return "Loose"
        else:
            return "Draw"
    
    @staticmethod
    def quest():
        cid = str(input("Enter Customer ID: "))
        return cid in [i.cid for i in players]


players = []
for i in range(10):
    cid = str(input("Enter Customer ID: "))
    moneyIn = int(input("Enter money in: "))
    moneyOut = int(input("Enter money out: "))
    players.append(Casino( cid, moneyIn, moneyOut ))

for i in players:
    print(i.cid, i.win_loose())

print(Casino.quest())