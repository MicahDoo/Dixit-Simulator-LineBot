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

    # img_urls += ['', '', '', '', '', '', '', '', '']
    global img_urls
    img_urls = ['https://i.imgur.com/NiAtMOX.jpg', 'https://i.imgur.com/hOCXaPW.jpg', 'https://i.imgur.com/pefZDtk.jpg', 'https://i.imgur.com/7uQUsaN.jpg', 'https://i.imgur.com/LHuK64T.jpg', 'https://i.imgur.com/oknK6UU.jpg', 'https://i.imgur.com/SzvJK2d.jpg', 'https://i.imgur.com/vwyafa2.jpg', 'https://i.imgur.com/5pEkAjR.jpg']
    img_urls += ['https://i.imgur.com/ziLZMgz.jpg', 'https://i.imgur.com/cBIVaub.jpg', 'https://i.imgur.com/VLRwtEc.jpg', 'https://i.imgur.com/D1lG334.jpg', 'https://i.imgur.com/ZGsLHuh.jpg', 'https://i.imgur.com/7jLXNRa.jpg', 'https://i.imgur.com/lpg9RMP.jpg', 'https://i.imgur.com/rScCgZy.jpg', 'https://i.imgur.com/3x6ctJ4.jpg']
    img_urls += ['https://i.imgur.com/KWd5gjM.jpg', 'https://i.imgur.com/jQBBuAr.jpg', 'https://i.imgur.com/owZiPdS.jpg', 'https://i.imgur.com/j9e7H6F.jpg', 'https://i.imgur.com/zEfnIYt.jpg', 'https://i.imgur.com/s1nIFFu.jpg', 'https://i.imgur.com/k5iVZYE.jpg', 'https://i.imgur.com/ptTOxTP.jpg', 'https://i.imgur.com/ouQSrdD.jpg']
    img_urls += ['https://i.imgur.com/H55tWhA.jpg', 'https://i.imgur.com/iAZkPFV.jpg', 'https://i.imgur.com/OPxNNr7.jpg', 'https://i.imgur.com/hloh2MD.jpg', 'https://i.imgur.com/Yh4yrcj.jpg', 'https://i.imgur.com/qrSCTO7.jpg', 'https://i.imgur.com/vIWQLQE.jpg', 'https://i.imgur.com/8DDWYNj.jpg', 'https://i.imgur.com/pNKPJq7.jpg']
    img_urls += ['https://i.imgur.com/nhaADgj.jpg', 'https://i.imgur.com/GOAkCES.jpg', 'https://i.imgur.com/X6DKyxp.jpg', 'https://i.imgur.com/bczxeSe.jpg', 'https://i.imgur.com/BoCdtA8.jpg', 'https://i.imgur.com/fUDNQfM.jpg', 'https://i.imgur.com/E9EIHJg.jpg', 'https://i.imgur.com/GxYoTEJ.jpg', 'https://i.imgur.com/QLySAxJ.jpg']


    global storyteller_messages
    storyteller_messages = ['Enchant them with your tale.']
    storyteller_messages += ['Give them the bare minimum. Spare the fuzzy details.']
    storyteller_messages += ['Vague or clear? I\'ll have both.']
    storyteller_messages += ['Imagination is key.']
    storyteller_messages += ['Kill them with vagueness, revive them with clarity.']
    storyteller_messages += ['Victory lies in subtlety.']
    storyteller_messages += ['What you say might not be what they hear.']
    storyteller_messages += ['Give them something to scratch their heads about.']
    storyteller_messages += ['Amuse and bemuse.']

    global listener_messages   
    listener_messages = ['Behold, bewitch and bewilder.']
    listener_messages += ['The power is on you to confuse.']
    listener_messages += ['I\'ve heard.. I\'ve seen that story before...']
    listener_messages += ['They have the words and pictures... but you have the frames.']
    listener_messages += ['What you hear might not be what you see.']
    listener_messages += ['Befuzzle them, as they will rightly you.']

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
                            "text": "Pick an image. \nConfuse the other players.",
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
                "separator": False
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

    global game_ended
    game_ended = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "😢 Game ended... 😢",
                    "weight": "bold",
                    "size": "xxl",
                    "margin": "xl",
                    "align": "center"
                },
                {
                    "type": "text",
                    "text": "It seems like the game was stopped short.\nHope to see you again.",
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
    if room_id in games:
        for player in games[room_id].users.values():
            print("Taking user " + player + " out of the game...")
            user_FSMs[player].leave_game()

    games.pop(room_id)
    heappush(unused_room_numbers, room_id)
