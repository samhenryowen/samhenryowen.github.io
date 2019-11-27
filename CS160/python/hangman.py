class Game():

    def __init__(self, word, guesses):
        self.letter_count = 0
        self.guess_limit = guesses
        self.player_guesses = 0
        self.word = self.parse_word(word)
        self.display_word = list('_') * self.letter_count

        self.run_game()

    ''' main game function
        takes player guesses and works with display class show game board '''
    def run_game(self):
        still_playing = True

        while still_playing:
            Display(self)  # show game board

            print("\n\nEnter your guess: ", end='')
            player_guess = input(str)
            correct_guess = False

            for i in range(self.letter_count):  # check guess against each letter
                if self.word[i] == player_guess:
                    self.display_word[i] = self.word[i]
                    correct_guess = True
                else:
                    continue

            if correct_guess == False:  # subtract a remaining guess if wrong
                self.player_guesses = self.player_guesses + 1
                print("\nIncorrect guess. Remaining chances:", self.guess_limit - self.player_guesses)

            if self.display_word == self.word:  # if these are equal then the word has been guessed (win)
                still_playing = False
                Display(self)
                print("\nCongrats, you successfully guessed the word. \nThanks for playing!")

            if self.player_guesses == self.guess_limit and self.word != self.display_word:  # ran out of guesses (lose)
                still_playing = False
                Display(self)
                print("\nYou have failed to guess the word:", self.get_word_string(), "\nThanks for playing!")

    ''' parse_word takes the word,
        converts to lowercase,
        calculates the length,
        returns the word as a list '''
    def parse_word(self, word):
        return_word = list()
        for i in word:
            i = i.lower()
            return_word.append(i)
        self.letter_count = len(word)
        return return_word

    ''' returns the word as a string '''
    def get_word_string(self):
        return ''.join(self.word)


''' Display class
    Could be expanded upon to display the actual hangman, etc '''
class Display():

    def __init__(self, game):
        self.game = game
        self.display_word(self.game.display_word)

    def display_word(self, word):
        print("Guess the word...")
        for i in word:
            print(i, end=' ')


game1 = Game('Samuel', 5)