STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guesses = set()

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            return ValueError("Man,no guess")        
        
        if char not in self.guesses and char in self.word:
            self.guesses.add(char)

            if all( c in self.guesses for c in self.word):
                return STATUS_WIN

        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE


    def get_masked_word(self):      
        
        return ''.join(c if c in self.guesses else '_' for c in self.word)

      
    def get_status(self):
        return self.status

obj1 = Hangman("mtu")
print(obj1.guess(''))
print(obj1.guess('t'))
print(obj1.guess('u'))
print(obj1.get_masked_word())
print(obj1.get_status())