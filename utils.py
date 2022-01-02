import os
import data

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, ImageCarouselTemplate, ImageCarouselColumn, TemplateSendMessage, MessageAction

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text1, text2 = None, text3 = None, text4 = None, text5 = None):
    line_bot_api = LineBotApi(channel_access_token)
    if text5 != None:
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=text1), TextSendMessage(text=text2), TextSendMessage(text=text3), TextSendMessage(text=text4), TextSendMessage(text=text5)])
    elif text4 != None:
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=text1), TextSendMessage(text=text2), TextSendMessage(text=text3), TextSendMessage(text=text4)])
    elif text3 != None:
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=text1), TextSendMessage(text=text2), TextSendMessage(text=text3)])
    elif text2 != None:
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=text1), TextSendMessage(text=text2)])
    else:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=text1))
    return "OK"

def show_hand(reply_token, hand, text, n = 5):
    line_bot_api = LineBotApi(channel_access_token)
    cards = " "
    for card in hand:
        cards = cards + " " + str(card)
    hand_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ImageCarouselTemplate(
            columns=[
                # ImageCarouselColumn(
                #     image_url=data.img_urls[hand[0]],
                #     action=MessageAction(
                #         text='1',
                #     )
                # ),
                # ImageCarouselColumn(
                #     image_url=data.img_urls[hand[1]],
                #     action=MessageAction(
                #         text='2',
                #     )
                # ),
                # ImageCarouselColumn(
                #     image_url=data.img_urls[hand[2]],
                #     action=MessageAction(
                #         text='3',
                #     )
                # ),
                # ImageCarouselColumn(
                #     image_url=data.img_urls[hand[3]],
                #     action=MessageAction(
                #         text='4',
                #     )
                # ),
                # ImageCarouselColumn(
                #     image_url=data.img_urls[hand[4]],
                #     action=MessageAction(
                #         text='5',
                #     )
                # )
            ]
        )
    )
    for i in range(n):
        print(i)
        hand_template.template.columns.append(
            ImageCarouselColumn(
                image_url=data.img_urls[hand[i]],
                action=MessageAction(
                    text=str(i+1)
                )
            )
        )
    line_bot_api.reply_message(reply_token, [TextSendMessage(text=text + cards), hand_template])

def send_text_and_image(reply_token, text, image_number, text1=None):
    line_bot_api = LineBotApi(channel_access_token)
    image_url = data.img_urls[image_number]
    if text1 != None:
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=text), ImageSendMessage(original_content_url = image_url, preview_image_url = image_url), TextSendMessage(text=text1)])
    else:
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=text), ImageSendMessage(original_content_url = image_url, preview_image_url = image_url)])

def show_selection(reply_token):
    # TODO: Show what cards the players play so you can choose what to select
    pass

def show_scores(reply_token):
    pass


# def push_text_message(reply_token, text):
#     line_bot_api = LineBotApi(channel_access_token)
#     line_bot_api.push_message(reply_token, TextSendMessage(text=text))

#     return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
