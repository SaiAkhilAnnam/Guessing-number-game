import random
class Guess:
    def __init__(self, number, mn = 0, mx = 100):
        self.number = number
        self.mn = mn
        self.mx = mx
        self.guesses = 0 
        
    def get_number(self):
        num = input(f"Enter the gussed number between{self.mn} and {self.mx}")
        if self.valied_number(num):
            return int(num)
        else:
            print("print a valied number")
            return self.get_number()
    
    def valied_number(self, num):
        try:
            number = int(num)
        except:
            return False
        
        return self.mn <= number <= self.mx
    
    def play(self):
        while True:
            self.guesses += 1
            guess = self.get_number()

            if guess < self.number:
                print("Your guess is below")
            elif guess > self.number:
                print("Your guess is above")
            else:
                print('''Wow!!!\nYou won''')
                break
if __name__ == "__main__":
    n = int(input("Enter the minimum number"))
    N = int(input("Enter the maximum number"))
    r = random.randint(n, N)
    game = Guess(r, n, N)
    game.play()
