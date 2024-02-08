import random 


class Card:
    values = [1,2,3,4,5,6,7,8,9,10]

class Player(Card):
    def take(self):
        pass
    
class Player1(Player):
    def take1(self):
        return random.choice(self.values)
    
class Player2(Player):
    def take2(self):
        return random.choice(self.values)

p1 = Player1()
result1 = p1.take1()

p2 = Player2()
result2 = p2.take2()

print("Player1 take card (take/no)")
answer1 = input()
if answer1 == "take":
    print(f"Your card number: {result1}")
else:
    result1 = 0
    

print("Player2 take card (take/no)")
answer2 = input()
if answer2 == "take":
    print(f"Your card number:{result2}")
else:
    result2 = 0
    print("game over")
    
    
if result1 > result2:
    print("Player1 won, congratulations!")
elif result1 == result2:
    print("it is a draw")
else:
    print("Player2 won, congratulations!")






