# from queue import PriorityQueue
from heapq import heapify, heappush, heappop

def init():
    # For each user
    global user_FSMs 
    user_FSMs = {} #[key:user_id, value: TocMachine() object for user}

    global unused_room_numbers
    unused_room_numbers = list(range(1, 100+1))

    heapify(unused_room_numbers)

    global games
    games = {} #[key:room_id, value: Game() object, which includes an fsm and more]

    global img_urls
    img_urls = ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']




def clear_game(room_id):
    for player in games[room_id].users.values():
        print("Taking user " + player + " out of the game...")
        user_FSMs[player].leave_game()

    games.pop(room_id)
    heappush(unused_room_numbers, room_id)
