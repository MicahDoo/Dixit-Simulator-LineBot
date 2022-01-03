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

    global storyteller_messages
    storyteller_messages = ['Enchant them with your tale.']
    storyteller_messages += ['Give them the bare minimum. Spare the fuzzy details.']
    storyteller_messages += ['Vague or clear? I\'ll have both.']
    storyteller_messages += ['Imagination is key.']
    storyteller_messages += ['Kill them with vagueness, revive them with clarity.']
    storyteller_messages += ['Victory lies in subtlety.']
    storyteller_messages += ['What you say might not be what they hear.']
    storyteller_messages += ['Give them something to scratch their heads about.']

    global listener_messages   
    listener_messages = ['Listen and bemuse.']
    listener_messages = ['The power is on your to confuse.']
    listener_messages = ['I\'ve heared.. I\'ve seen that story before...']
    listener_messages = ['They have the words... but you have the pictures.']
    listener_messages = ['What you hear might not be what you see.']
    listener_messages = ['Befuzzle them, as they will rightly do you.']

    global storyteller_template
    storyteller_template = {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/yrEeehO.jpg",
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
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Give them the bare minimum. Spare the fuzzy details.",
                            "size": "md",
                            "color": "#ffffff",
                            "weight": "bold",
                            "wrap": True
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Pick a card. \nTell a story about it.",
                            "color": "#ebebeb",
                            "size": "sm",
                            "flex": 0,
                            "wrap": True
                        }
                        ],
                        "spacing": "lg"
                    }
                    ],
                    "position": "absolute",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#725b0777",
                    "paddingAll": "20px",
                    "paddingTop": "18px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "THE STORYTELLER",
                        "color": "#ffffff",
                        "align": "center",
                        "size": "xs",
                        "offsetTop": "6px"
                    }
                    ],
                    "position": "absolute",
                    "cornerRadius": "20px",
                    "height": "30px",
                    "offsetTop": "10px",
                    "offsetStart": "10px",
                    "backgroundColor": "#56344477",
                    "offsetEnd": "10px"
                }
                ],
                "paddingAll": "0px"
            },
            "styles": {
                "header": {
                "backgroundColor": "#D1D9D9"
                },
                "hero": {
                "separator": False
                }
            }
            }
        ]
        }

    global listener_template
    listener_template = {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/GEDlJoI.jpg",
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
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "They have the words... but you have the pictures.",
                            "size": "md",
                            "color": "#ffffff",
                            "weight": "bold",
                            "wrap": True
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Pick an image. \nConfuse the other audience.",
                            "color": "#ebebeb",
                            "size": "sm",
                            "flex": 0,
                            "wrap": True
                        }
                        ],
                        "spacing": "lg"
                    }
                    ],
                    "position": "absolute",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#33341177",
                    "paddingAll": "20px",
                    "paddingTop": "18px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "THE LISTENER",
                        "color": "#ffffff",
                        "align": "center",
                        "size": "xs",
                        "offsetTop": "6px"
                    }
                    ],
                    "position": "absolute",
                    "cornerRadius": "20px",
                    "height": "30px",
                    "offsetTop": "10px",
                    "offsetStart": "10px",
                    "backgroundColor": "#13220077",
                    "offsetEnd": "10px"
                }
                ],
                "paddingAll": "0px"
            },
            "styles": {
                "header": {
                "backgroundColor": "#D1D9D9"
                },
                "hero": {
                "separator": false
                }
            }
            }
        ]
        }

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

    global game_over
    game_over = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "🎊 Game over! 🎊",
                    "weight": "bold",
                    "size": "xxl",
                    "margin": "xl",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "Did you get your fair share of fun?\nLet's play again?",
                    "size": "md",
                    "wrap": True,
                    "margin": "lg",
                    "align": "center"
                }
            ],
            "background_color": "#BFACAA"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "background_color": "#BFACAA",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    # "height": "md",
                    "action": {
                        "type": "message",
                        "label": "Yes, please",
                        "text": "Play again"
                    },
                    "color": "#654321"
                },
                {
                    "type": "button",
                    "style": "primary",
                    # "height": "md",
                    "action": {
                        "type": "message",
                        "label": "Nope, too much fun",
                        "text": "Quit"
                    },
                    "color": "#3B5249"
                }
            ],
            "spacing": "lg"
        },
        "styles": {
            "footer": {
                "separator": False
            }
        }
        }

    global game_start
    game_start = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "🎊 Game started! 🎊",
                    "weight": "bold",
                    "size": "xxl",
                    "margin": "xl",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "First to get 30 points wins!\nDo your best!",
                    "size": "md",
                    "wrap": True,
                    "margin": "lg",
                    "align": "center"
                }
            ],
            "background_color": "#BFACAA"
        },
        }
       



def clear_game(room_id):
    for player in games[room_id].users.values():
        print("Taking user " + player + " out of the game...")
        user_FSMs[player].leave_game()

    games.pop(room_id)
    heappush(unused_room_numbers, room_id)
