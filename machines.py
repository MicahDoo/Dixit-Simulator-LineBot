from fsm import UserMachine
from fsm import GameMachine

def create_user_fsm():
    machine = UserMachine(
        states=['user', 'room_created', 'create_password', 'enter_password', 'waiting_for_players', 'in_room', 'hosting_game', 
        'in_game', 'card_played', 'cards_displayed', 'guess_made', 'scores_tallied', 'card_dealt', 'story_told', 
        'all_cards_played', 'storyteller_results_shown', 'storyteller_card_dealt', 'final_results_shown'],
        transitions=[
            {'trigger': 'advance', 'source': ['room_created', 'waiting_for_players', 'in_room', 'hosting_game', 
        'in_game', 'card_played', 'cards_displayed', 'guess_made', 'scores_tallied', 'card_dealt', 'story_told', 
        'all_cards_played', 'storyteller_results_shown', 'storyteller_card_dealt', 'final_results_shown'], 'dest': 'user', 'conditions': 'game_finished'},
            {'trigger': 'advance', 'source': 'user', 'dest': 'room_created', 'conditions': 'is_going_to_room_created'},
            {'trigger': 'advance', 'source': 'room_created', 'dest': 'waiting_for_players', 'conditions': 'is_not_setting_password'},
            {'trigger': 'advance', 'source': 'room_created', 'dest': 'create_password', 'conditions': 'is_setting_password'},
            {'trigger': 'advance', 'source': 'create_password', 'dest': 'waiting_for_players', 'conditions': 'password_valid'},
            {'trigger': 'advance', 'source': 'user', 'dest': 'in_room', 'conditions': 'is_joining_game'},
            {'trigger': 'advance', 'source': 'user', 'dest': 'enter_password', 'conditions': 'is_joining_password_protected_game'},
            {'trigger': 'advance', 'source': 'enter_password', 'dest': 'in_room', 'conditions': 'is_correct_password'},
            {'trigger': 'advance', 'source': 'waiting_for_players', 'dest': 'hosting_game', 'conditions': 'game_ready_to_start'},
            {'trigger': 'advance', 'source': 'in_room', 'dest': 'in_game', 'conditions': 'game_started'},
            {'trigger': 'advance', 'source': 'in_game', 'dest': 'card_played', 'conditions': 'plays_a_card'},
            {'trigger': 'advance', 'source': 'card_played', 'dest': 'cards_displayed', 'conditions': 'storyteller_collected_the_cards'},
            {'trigger': 'advance', 'source': 'card_played', 'dest': 'card_played', 'conditions': 'plays_a_card'},
            {'trigger': 'advance', 'source': 'cards_displayed', 'dest': 'guess_made', 'conditions': 'guesses_a_card'},
            {'trigger': 'advance', 'source': 'guess_made', 'dest': 'scores_tallied', 'conditions': 'storyteller_recorded_the_guesses'},
            {'trigger': 'advance', 'source': 'guess_made', 'dest': 'guess_made', 'conditions': 'guesses_a_card'},
            {'trigger': 'advance', 'source': 'scores_tallied', 'dest': 'final_results_shown', 'conditions': 'end_of_the_game'},
            {'trigger': 'advance', 'source': 'scores_tallied', 'dest': 'card_dealt', 'conditions': 'not_storyteller_next_round'},
            {'trigger': 'advance', 'source': 'scores_tallied', 'dest': 'storyteller_card_dealt', 'conditions': 'storyteller_next_round'},
            {'trigger': 'advance', 'source': 'hosting_game', 'dest': 'story_told', 'conditions': 'plays_a_card_as_story'},
            {'trigger': 'advance', 'source': 'story_told', 'dest': 'story_told', 'conditions': 'plays_a_card_as_story'},
            {'trigger': 'advance', 'source': 'story_told', 'dest': 'all_cards_played', 'conditions': 'everyone_played_a_card'},
            {'trigger': 'advance', 'source': 'all_cards_played', 'dest': 'storyteller_results_shown', 'conditions': 'everyone_made_a_guess'},
            {'trigger': 'advance', 'source': 'storyteller_results_shown', 'dest': 'final_results_shown', 'conditions': 'end_of_the_game'},
            ###
            # {'trigger': 'advance', 'source': 'storyteller_results_shown', 'dest': 'storyteller_card_dealt', 'conditions': 'anything'},
            {'trigger': 'advance', 'source': 'storyteller_results_shown', 'dest': 'card_dealt', 'conditions': 'anything'},
            ###
            {'trigger': 'advance', 'source': 'card_dealt', 'dest': 'card_played', 'conditions': 'plays_a_card'},
            {'trigger': 'advance', 'source': 'storyteller_card_dealt', 'dest': 'story_told', 'conditions': 'plays_a_card_as_story'},
            

            {"trigger": "go_back", "source": ['room_created', 'waiting_for_players', 'in_room', 'hosting_game', 
        'in_game', 'card_played', 'cards_displayed', 'guess_made', 'scores_tallied', 'card_dealt', 'story_told', 
        'all_cards_played', 'storyteller_results_shown', 'storyteller_card_dealt', 'final_results_shown'], "dest": "user"},
        ],
        initial='user',
        auto_transitions=False,
        show_conditions=True,
    )
    return machine