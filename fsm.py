import data
from transitions.extensions import GraphMachine

from heapq import heappop, heappush, heapify
from game import create_game

from random import randint

from utils import send_text_message, start_show_hand_listener, start_show_hand_storyteller, show_hand_listener, show_hand_storyteller, send_text_and_image, show_display, send_text_and_question, show_game_over

class UserMachine(GraphMachine):
    my_room_number = -1
    my_player_id = 0
    my_game = None
    in_game = False
    disconnected = False

    wait_flag = False

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def leave_game(self):
        self.in_game = False
        self.my_room_number = -1
        self.my_player_id = 0
        self.my_game = False
        self.disconnected = True

    def is_going_to_room_created(self, event):
        text = event.message.text

        return text.lower().find("create") != -1 or text.lower().find("game") != -1 or text.lower().find("room") != -1

    def on_enter_room_created(self, event):
        print("I'm entering room_created")

        reply_token = event.reply_token
        # send_text_message(reply_token, "Your user ID is" + str(event.source.user_id))
        new_room_number = heappop(data.unused_room_numbers)
        data.games[new_room_number] = create_game()
        self.my_room_number = new_room_number
        self.my_game = data.games[new_room_number]
        self.my_player_id = self.my_game.add_new_player(event.source.user_id)
        self.in_game = True
        send_text_and_question(reply_token, "Initializing room...", "Room created!\nYour room number is " + str(new_room_number), "Your player ID: " + str(self.my_player_id), "Would you like to set a password?")

        # n = 10000000
        # while(self.flag == 0):
        #     n -= 1
        #     if(n == 0):
        #         print("a")
        #         n = 10000000

    # def on_exit_room_created(self, event):
    #      print("Leaving room init")
        #  self.flag = 1
        #  send_text_message(event.reply_token, "Exiting initializing room...")

    def is_joining_game(self, event):
        text = event.message.text
        words = text.split(" ")
        if len(words) == 2 and words[0].lower() == "join" and words[1].isnumeric():
            room_number = int(words[1])
            if data.games[room_number] != None:
                print("Game exists")
                self.my_room_number = room_number
                self.my_game = data.games[room_number]
                if self.my_game.room_joinable() and not self.my_game.password_protected:
                    return True
                else:
                     return False
            else:
                return False
        else:
            return False

    def is_joining_password_protected_game(self, event):
        text = event.message.text
        words = text.split(" ")
        if len(words) == 2 and words[0].lower() == "join" and words[1].isnumeric():
            room_number = int(words[1])
            if data.games[room_number] != None:
                self.my_room_number = room_number
                self.my_game = data.games[room_number]
                if self.my_game.room_joinable() and self.my_game.password_protected:
                    return True
                else:
                     return False
            else:
                return False
        else:
            return False

    def on_enter_in_room(self, event):
        reply_token = event.reply_token
        self.my_player_id = self.my_game.add_new_player(event.source.user_id)
        self.in_game = True
        send_text_message(reply_token, "Successfully joined room number " + str(self.my_room_number), "Your player ID: " + str(self.my_player_id), "Waiting for the game to start...")

    def on_enter_enter_password(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Please put in the password for room number " + str(self.my_room_number) + ":")

    def is_correct_password(self, event):
        text = event.message.text
        if not self.my_game.is_password(text):
            reply_token = event.reply_token
            send_text_message(reply_token, "The password is incorrect")
            return False
        return True

    def is_not_setting_password(self, event):
        text = event.message.text
        
        if text.lower().find("n") != -1:
            reply_token = event.reply_token
            send_text_message(reply_token, "Room successfully created!", "Wait till all of your friends have joined.\n(Type \"Join " + str(self.my_room_number) + "\")", "Type \"start game\" to start the game")
        ## I reply here because the actions vary depending on where you are from

        return text.lower().find("n") != -1

    def on_enter_waiting_for_players(self, event):
        print("I'm entering waiting_for_players")
        self.my_game.complete_room_creation()

    def game_ready_to_start(self, event):
        text = event.message.text
        return text.lower().find("start") != -1 and self.my_game.game_is_ready()

    def on_enter_hosting_game(self, event):
        print("I'm entering game_started")
        
        self.my_game.start_game()
        hand = self.my_game.get_hand(self.my_player_id)

        reply_token = event.reply_token
        start_show_hand_listener(reply_token, hand, 'Your role:')

    def plays_a_card(self, event):
        text = event.message.text
        if text.isnumeric() and 0 < int(text) <= 5:
            send_text_and_image(event.reply_token, "You played card " + text + " to confuse the opponent: ", self.my_game.hands[self.my_player_id][int(text)-1], "Continue after everyone plays a card and the storyteller collects the cards.")
            self.my_game.log_distraction(self.my_player_id, int(text)-1)
        return text.isnumeric() and 0 < int(text) <= 5

    def guesses_a_card(self,event):
        text = event.message.text
        if text.isnumeric() and 0 < int(text) <= self.my_game.player_count:
            send_text_and_image(event.reply_token, "Your guess:", self.my_game.display[int(text)-1], "Continue after the storyteller confirms everyone makes a guess.")
            self.my_game.log_guess(self.my_player_id, int(text)-1)
        return text.isnumeric() and 0 < int(text) <= self.my_game.player_count

    def plays_a_card_as_story(self, event):
        text = event.message.text
        if text.isnumeric() and 0 < int(text) <= 5:
            send_text_and_image(event.reply_token, "You chose image " + text + " for your story:", self.my_game.hands[self.my_player_id][int(text)-1], "Now, make up a sentence related to this picture and say it out loud.\nType \"Next\" when everyone's played a card.")
            self.my_game.log_story(self.my_player_id, int(text)-1)
        return text.isnumeric() and 0 < int(text) <= 5

    def on_enter_story_told(self, event):
        pass

    def everyone_played_a_card(self, event):
        text = event.message.text
        if text.lower().find("next") != -1 and self.my_game.display.count(-1) == 0:
            return True
        else:
             return False

    def on_enter_all_cards_played(self, event):
        self.my_game.collected = True
        self.my_game.replace_all_cards()
        show_display(event.reply_token, self.my_game.display, "Can your audience see through your story?", self.my_game.player_count, "Continue when all players have placed their bets.")

    def storyteller_collected_the_cards(self, event):
        return self.my_game.collected

    def on_enter_cards_displayed(self, event):
        show_display(event.reply_token, self.my_game.display, "Can you spot the story from these cards?", self.my_game.player_count)

    def end_of_the_game(self, event):
        print("max(self.my_game.scores) ==", max(self.my_game.scores))
        return max(self.my_game.scores) >= 30

    def everyone_made_a_guess(self, event):
        return self.my_game.guesses.count(-1) == 1

    def storyteller_recorded_the_guesses(self, event):
        if self.my_game.guesses_recorded:
            print("storyteller_recorded_the_guesses passed")
        return self.my_game.guesses_recorded

    def on_enter_storyteller_results_shown(self, event):
        self.my_game.guesses_recorded = True
        tally_text = self.my_game.tally()
        leaderboard_text = self.my_game.show_ranking()
        print("tally_text = ", tally_text)
        print("leaderboard_text = ", leaderboard_text)
        send_text_and_image(event.reply_token, "Answer:", self.my_game.story, tally_text, leaderboard_text)

    def on_enter_scores_tallied(self, event):
        tally_text = self.my_game.tally()
        leaderboard_text = self.my_game.show_ranking()
        print("tally_text = ", tally_text)
        print("leaderboard_text = ", leaderboard_text)
        send_text_and_image(event.reply_token, "Answer:", self.my_game.story, tally_text, leaderboard_text)

    def on_enter_final_results_shown(self, event):
        show_game_over(event.reply_token)

    def not_another_game(self, event):
        text = event.message.text
        if text.lower().find("quit") != -1 or text.lower().find("exit") != -1 or text.lower().find("no") != -1 or text.lower().find("leave") != -1 or text.lower().find("bye") != -1:
            data.clear_game(self.my_room_number)
            return True

    def host_wants_another_game(self, event):
        text = event.message.text
        if self.my_player_id == 0 and text.lower().find("continue") != -1 or text.lower().find("another") != -1 or text.lower().find("yes") != -1 or text.lower().find("resume") != -1 or text.lower().find("again") != -1 or text.lower().find("好") != -1 or text.lower().find("繼續") != -1 or text.lower().find("再") != -1:
            return True

    def wants_another_game(self, event):
        text = event.message.text
        if self.my_player_id != 0 and text.lower().find("continue") != -1 or text.lower().find("another") != -1 or text.lower().find("yes") != -1 or text.lower().find("resume") != -1 or text.lower().find("again") != -1 or text.lower().find("好") != -1 or text.lower().find("繼續") != -1 or text.lower().find("再") != -1:
            return True

    def storyteller_next_round(self, event):
        return self.my_player_id == (self.my_game.storyteller+1)%self.my_game.player_count

    def on_enter_storyteller_card_dealt(self, event):
        self.my_game.start_round()
        hand = self.my_game.get_hand(self.my_player_id)

        reply_token = event.reply_token
        show_hand_storyteller(reply_token, hand, 'Your role:', )

    def not_storyteller_next_round(self, event):
        return self.my_player_id != (self.my_game.storyteller+1)%self.my_game.player_count

    def on_enter_card_dealt(self, event):
        hand = self.my_game.get_hand(self.my_player_id)
        show_hand_listener(event.reply_token, hand, "Your role:")

    def anything(self, event):
        return True

    def is_setting_password(self, event):
        text = event.message.text

        return text.lower().find("n") == -1 and text.lower().find("y") != -1

    def on_enter_create_password(self, event):

        reply_token = event.reply_token
        send_text_message(reply_token, "Please enter your password:")

    def password_valid(self, event):
        print("Checking if password is valid")
        text = event.message.text

        if text != "":
            print("It is valid!")
            reply_token = event.reply_token
            self.my_game.set_password(text)
            send_text_message(reply_token, "Room successfully created!", "Tell your friends to join by texting the room number " + str(self.my_room_number) + " and the password " + self.my_game.get_password(), "Type \"start game\" to start the game")

        return text != ""

    def game_started(self, event):
        print("Checking if game started")
        return self.my_game.is_game_alive()

    def on_enter_in_game(self, event):
        print("In game")
        start_show_hand_listener(event.reply_token, self.my_game.hands[self.my_player_id], "Your role:")


    def game_finished(self, event):
        print("Checking if game ended")
        text = event.message.text
        if text.lower().find("quit") != -1: # only room owner or if you haven't joined any game yet can quit
            if not self.in_game:
                send_text_message(event.reply_token, "Game ended.")
                return True
            if self.my_player_id == 0:
                # self.in_game = False
                data.clear_game(self.my_room_number)
                send_text_message(event.reply_token, "Game ended.")
                return True
        elif not self.in_game and self.disconnected:
            self.disconnected = False
            send_text_message(event.reply_token, "Game ended.")
            return True
        return False

