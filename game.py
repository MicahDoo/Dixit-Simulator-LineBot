from random import shuffle
from random import randint

import data

#TODO:
#For each room, there is:
#deck[]: cards currently not on anybody's hand
#hands[][]: cards in each player's hand
#player_ids[]: ids of players, has to be in the same order as hands

class Game():
    def __init__(self):
        self.player_count = 0

    def start_game(self):
        print("Start game")
        self.deck = list(range(len(data.img_urls)))
        shuffle(self.deck)
        self.hands = [[-1]*5 for _ in range(self.player_count)]
        self.display = [-1]*self.player_count
        self.guesses = [-1]*self.player_count
        self.scores = [0]*self.player_count
        for i in range(0, len(self.hands)):
            for j in range(0, len(self.hands[0])):
                print("~", self.deck[0])
                self.hands[i][j] = self.deck[0]
                self.deck.pop(0)
        self.game_started = True
        self.guesses_recorded = False
        self.story = -1
        self.answer = -1
        self.collected = False
        self.tally_text = ""
        self.ranking_text = ""

    def shuffle_deck(self):
        shuffle(self.deck)

    def log_story(self, player_id, number):
        self.display[player_id] = number
        self.story = self.hands[player_id][number]

    def log_distraction(self, player_id, number):
        self.display[player_id] = number

    def log_guess(self, player_id, number):
        self.guesses[player_id] = number

    def start_round(self):
        self.display = [-1]*self.player_count
        self.guesses = [-1]*self.player_count
        self.story = -1
        self.answer = -1
        self.storyteller = (self.storyteller+1)%self.player_count
        self.collected = False
        self.guesses_recorded = False
        self.tally_text = ""
        self.ranking_text = ""

    def tally(self):
        if self.tally_text != "":
            return self.tally_text
        hit_count = 0
        miss_count = 0
        hit_text = "Hit: "
        miss_text = "Miss: "
        for i in range(self.player_count):
            if i != self.storyteller:
                if self.display[self.guesses[i]] == self.story:
                    hit_count += 1
                    hit_text += "player" + str(i) + " "
                else:
                    miss_count += 1
                    miss_text += "player" + str(i) + " "
        this_round_text = ""
        if hit_count == 0 or miss_count == self.player_count-1:
            for i in range(self.player_count):
                if i != self.storyteller:
                    this_round_text += "player" + str(i) + ": +2"
                    self.scores[i] += 2
                else:
                    this_round_text += "player" + str(i) + ": +4" #####
                    print("score goes from", self.scores[i])
                    self.scores[i] += 4
                    print("to", self.scores[i])
                if i != self.player_count - 1:
                    this_round_text +="\n"
        else:
            for i in range(self.player_count):
                if i != self.storyteller:
                    if self.display[self.guesses[i]] == self.story:
                        this_round_text += "player" + str(i) + ": +3"
                        self.scores[i] += 3
                    elif self.guesses[i] == i:
                        this_round_text += "player" + str(i) + ": +1"
                        self.scores[i] += 1
                else:
                    this_round_text += "player" + str(i) + ": +3"
                    self.scores[i] += 3
                if i != self.player_count - 1:
                    this_round_text +="\n"
        self.tally_text = "This round: \n" + hit_text + "\n" + miss_text + "\n" + this_round_text
        return self.tally_text

    def show_ranking(self):
        if self.ranking_text != "":
            return self.ranking_text
        text = "Leaderboard:\n"
        for i in range(self.player_count):
            text += "player" + str(i) + ": " + str(self.scores[i])
            if i != self.player_count - 1:
                text +="\n"
        self.ranking_text = text
        return text
        

    def replace_card(self, hand, card_order):
        card_num = hand[card_order]
        hand.pop(card_order)
        hand.insert(0, self.deck[0])
        self.deck.pop(0)
        self.deck.insert(card_num, randint(0, len(self.deck)-1))

    def replace_all_cards(self):
        for i in range(len(self.display)):
            num = self.hands[i][self.display[i]]
            self.replace_card(self.hands[i], self.display[i])
            self.display[i] = num
        shuffle(self.display)
        for i in range(len(self.display)):
            if(self.display[i] == self.story):
                self.answer = i
                break

    def game_is_ready(self):
        self.create_complete = False
        return True

    def get_hand(self, player_id):
        return self.hands[player_id]

    def set_password(self, password):
        self.password = password
        self.password_protected = True

    def get_password(self):
        return self.password

    def add_new_player(self, user_id):
        self.player_count += 1
        print("player_count = ", self.player_count)
        self.users[self.player_count-1] = user_id
        return self.player_count - 1

    def is_password(self, attempt):
        return attempt == self.password

    def is_game_alive(self):
        return self.game_started

    def complete_room_creation(self):
        self.create_complete = True

    def room_joinable(self):
        return self.create_complete

    create_complete = False
    player_count = int()
    collected = False
    guesses_recorded = False
    deck = list()
    hands = list() # Do I organize them in (x) user_id or just (v) player_number?
    guesses = list()
    display = list()
    password_protected = False
    password = ""
    users = {}
    game_started = False
    storyteller = 0
    story = -1
    answer = -1
    scores = list()
    tally_text = ""
    ranking_text = ""

def create_game():
    new_game = Game()
    return new_game
