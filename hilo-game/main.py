import random
def main():
    # create a game instance
    game = Director()

    # create a card
    card = Card()

    # start the game
    game.start_game(card)

class Director:
    # class that hold the game
    # if the score is 0 the game will end 
    # OR if the player decides to quit
    
    def __init__(self):
        # start 
        # default score is 300
        self.is_playing = True
        self.score = 300
        
    def start_game(self, card):
        while self.is_playing:
            print()
            card.display_card()
            self.get_input()
            card.display_next_card()
            self.update_score(card)
            self.display_score()
            card.update_card()
            self.play_again()
            
    
    def get_input(self):
        self.input = input('Higher or Lower? [h/l]: ').lower()

    def display_score(self):
        print(f'your score is: {self.score}')

    def update_score(self, card):

        if self.input == 'h':
            if card.current_card < card.next_card:
                self.score += 100
            else:
                self.score -= 75

        if self.input == 'l':
            if card.current_card > card.next_card:
                self.score += 100
            else:
                self.score -= 75
        
    def play_again(self):
        if self.score > 0:
            repeat = input('Play again? [y/n] ').lower()
            if repeat == 'y':
                return
        print('Game Over!')
        self.is_playing = False

class Card:

    def __init__(self):
        self.current_card = random.randint(1, 14)
        self.next_card = random.randint(1, 14)

    def display_card(self):
        print(f'The card is: {self.current_card}')
    
    def display_next_card(self):
        print(f'Next card is: {self.next_card}')


    def update_card(self):
        self.current_card = self.next_card
        self.next_card = random.randint(1, 14)



main()