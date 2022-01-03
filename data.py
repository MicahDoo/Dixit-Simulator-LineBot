# from queue import PriorityQueue
from heapq import heapify, heappush, heappop
from linebot.models import CarouselTemplate

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
    img_urls += ['https://i.imgur.com/KVtJNwh.jpg', 'https://i.imgur.com/IEAEYct.jpg', 'https://i.imgur.com/ukEN5QE.jpg', 'https://i.imgur.com/vFarBiM.jpg', 'https://i.imgur.com/3hV1TnW.jpg', 'https://i.imgur.com/mQU5EOs.jpg', 'https://i.imgur.com/w8It5aZ.jpg', 'https://i.imgur.com/lKhYFrb.jpg', 'https://i.imgur.com/Pk36ixw.jpg']
    img_urls += ['https://i.imgur.com/KuE5Qbf.jpg', 'https://i.imgur.com/U4gpBKh.jpg', 'https://i.imgur.com/n3w333y.jpg', 'https://i.imgur.com/ccfLedo.jpg', 'https://i.imgur.com/3SfnxbY.jpg', 'https://i.imgur.com/hvpX9Zq.jpg', 'https://i.imgur.com/laWkwvX.jpg', 'https://i.imgur.com/0AsS5Mb.jpg', 'https://i.imgur.com/qvtb9ze.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/KVtJNwh.jpg', 'https://i.imgur.com/IEAEYct.jpg', 'https://i.imgur.com/ukEN5QE.jpg', 'https://i.imgur.com/vFarBiM.jpg', 'https://i.imgur.com/3hV1TnW.jpg', 'https://i.imgur.com/mQU5EOs.jpg', 'https://i.imgur.com/w8It5aZ.jpg', 'https://i.imgur.com/lKhYFrb.jpg', 'https://i.imgur.com/Pk36ixw.jpg']
    img_urls += ['https://i.imgur.com/KuE5Qbf.jpg', 'https://i.imgur.com/U4gpBKh.jpg', 'https://i.imgur.com/n3w333y.jpg', 'https://i.imgur.com/ccfLedo.jpg', 'https://i.imgur.com/3SfnxbY.jpg', 'https://i.imgur.com/hvpX9Zq.jpg', 'https://i.imgur.com/laWkwvX.jpg', 'https://i.imgur.com/0AsS5Mb.jpg', 'https://i.imgur.com/qvtb9ze.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/KVtJNwh.jpg', 'https://i.imgur.com/IEAEYct.jpg', 'https://i.imgur.com/ukEN5QE.jpg', 'https://i.imgur.com/vFarBiM.jpg', 'https://i.imgur.com/3hV1TnW.jpg', 'https://i.imgur.com/mQU5EOs.jpg', 'https://i.imgur.com/w8It5aZ.jpg', 'https://i.imgur.com/lKhYFrb.jpg', 'https://i.imgur.com/Pk36ixw.jpg']
    img_urls += ['https://i.imgur.com/KuE5Qbf.jpg', 'https://i.imgur.com/U4gpBKh.jpg', 'https://i.imgur.com/n3w333y.jpg', 'https://i.imgur.com/ccfLedo.jpg', 'https://i.imgur.com/3SfnxbY.jpg', 'https://i.imgur.com/hvpX9Zq.jpg', 'https://i.imgur.com/laWkwvX.jpg', 'https://i.imgur.com/0AsS5Mb.jpg', 'https://i.imgur.com/qvtb9ze.jpg']
    img_urls += ['https://i.imgur.com/VdJI90y.jpeg', 'https://i.imgur.com/QlFu6Ff.jpg', 'https://i.imgur.com/NljlPbD.jpg', 'https://i.imgur.com/sNpg7YI.jpg', 'https://i.imgur.com/VEwp7KE.jpg', 'https://i.imgur.com/PI9HnKD.jpg', 'https://i.imgur.com/rjcFxHb.jpg', 'https://i.imgur.com/wxD0mIw.jpg', 'https://i.imgur.com/OMlktVf.jpg']
    img_urls += ['https://i.imgur.com/KVtJNwh.jpg', 'https://i.imgur.com/IEAEYct.jpg', 'https://i.imgur.com/ukEN5QE.jpg', 'https://i.imgur.com/vFarBiM.jpg', 'https://i.imgur.com/3hV1TnW.jpg', 'https://i.imgur.com/mQU5EOs.jpg', 'https://i.imgur.com/w8It5aZ.jpg', 'https://i.imgur.com/lKhYFrb.jpg', 'https://i.imgur.com/Pk36ixw.jpg']
    img_urls += ['https://i.imgur.com/KuE5Qbf.jpg', 'https://i.imgur.com/U4gpBKh.jpg', 'https://i.imgur.com/n3w333y.jpg', 'https://i.imgur.com/ccfLedo.jpg', 'https://i.imgur.com/3SfnxbY.jpg', 'https://i.imgur.com/hvpX9Zq.jpg', 'https://i.imgur.com/laWkwvX.jpg', 'https://i.imgur.com/0AsS5Mb.jpg', 'https://i.imgur.com/qvtb9ze.jpg']

    global flex_carousel
    flex_carousel = {
        "type": "carousel",
        "contents": [
            
        ]
        }
    
    global image_bubble
    image_bubble = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip2.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "2:3",
                "gravity": "top"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "1",
                    "color": "#ffffff",
                    "align": "center",
                    "size": "xs",
                    "offsetTop": "3px"
                }
                ],
                "position": "absolute",
                "cornerRadius": "20px",
                "offsetTop": "18px",
                "backgroundColor": "#6f4137",
                "offsetStart": "18px",
                "height": "25px",
                "width": "25px"
            }
            ],
            "paddingAll": "0px"
        },
        "action": {
            "type": "message",
            "label": "action",
            "text": "1"
        }
        }
       



def clear_game(room_id):
    for player in games[room_id].users.values():
        print("Taking user " + player + " out of the game...")
        user_FSMs[player].leave_game()

    games.pop(room_id)
    heappush(unused_room_numbers, room_id)
