import os
import data
import copy

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, BubbleContainer, TextSendMessage, FlexContainer, FlexSendMessage, ImageSendMessage, ImageCarouselTemplate, ImageCarouselColumn, TemplateSendMessage, MessageAction, QuickReplyButton, QuickReply, ConfirmTemplate, MessageTemplateAction

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text1, text2 = None, text3 = None, text4 = None, text5 = None):
    if text5 != None:
        send_message(reply_token, TextSendMessage(text=text1), TextSendMessage(text=text2), TextSendMessage(text=text3), TextSendMessage(text=text4), TextSendMessage(text=text5))
    elif text4 != None:
        send_message(reply_token, TextSendMessage(text=text1), TextSendMessage(text=text2), TextSendMessage(text=text3), TextSendMessage(text=text4))
    elif text3 != None:
        send_message(reply_token, TextSendMessage(text=text1), TextSendMessage(text=text2), TextSendMessage(text=text3))
    elif text2 != None:
        send_message(reply_token, TextSendMessage(text=text1), TextSendMessage(text=text2))
    else:
        send_message(reply_token, TextSendMessage(text=text1))
    return "OK"

def send_message(reply_token, msg1, msg2 = None, msg3 = None, msg4 = None, msg5 = None):
    line_bot_api = LineBotApi(channel_access_token)
    if msg5 != None:
        line_bot_api.reply_message(reply_token, [msg1, msg2, msg3, msg4, msg5])
    elif msg4 != None:
        line_bot_api.reply_message(reply_token, [msg1, msg2, msg3, msg4])
    elif msg3 != None:
        line_bot_api.reply_message(reply_token, [msg1, msg2, msg3])
    elif msg2 != None:
        line_bot_api.reply_message(reply_token, [msg1, msg2])
    else:
        line_bot_api.reply_message(reply_token, msg1)
    return "OK"

def show_hand(reply_token, hand, text, n = 5):
    cards = " "
    for card in hand:
        cards = cards + " " + str(card)
    print(cards)
    hand_json = copy.deepcopy(data.flex_carousel)
    for i in range(n):
        image_json = copy.deepcopy(data.image_bubble)  ###NOTE: IMPORTANT: hard copy
        image_json['action']['text'] = str(i+1)
        image_json['body']['contents'][0]['url'] = data.img_urls[hand[i]]
        image_json['body']['contents'][1]['contents'][0]['text'] = str(i+1)
        hand_json['contents'].append(image_json)
    hand_template = FlexSendMessage("Show hand", hand_json)
    send_message(reply_token, TextSendMessage(text=text), hand_template)

def show_display(reply_token, display, text, n, text1 = None):
    line_bot_api = LineBotApi(channel_access_token)
    cards = " "
    for card in display:
        cards = cards + " " + str(card)
    print(cards)
    display_json = copy.deepcopy(data.flex_carousel)
    for i in range(n):
        image_json = copy.deepcopy(data.image_bubble)  ###NOTE: IMPORTANT: hard copy
        image_json['action']['text'] = str(i+1)
        image_json['body']['contents'][0]['url'] = data.img_urls[display[i]]
        image_json['body']['contents'][1]['contents'][0]['text'] = str(i+1)
        display_json['contents'].append(image_json)
    display_template = FlexSendMessage("Show display", display_json)
    if text1 != None:
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=text), display_template, TextSendMessage(
        text=text1, quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label="Continue", text="Next"))]))])
    else:
        send_message(reply_token, TextSendMessage(text=text), display_template)

def show_game_over(reply_token):
    message_json = data.game_over
    message = FlexSendMessage("Game over", message_json)
    send_message(reply_token, message)


def send_text_and_image(reply_token, text, image_number, text1 = None, text2 = None):
    print("Send text and image")
    image_url = data.img_urls[image_number]
    if text2 != None:
        print(text2, text1, text)
        send_message(reply_token, TextSendMessage(text=text), ImageSendMessage(original_content_url = image_url, preview_image_url = image_url), TextSendMessage(text=text1), TextSendMessage(
        text=text2, quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label="Continue", text="Next"))])))
    elif text1 != None:
        send_message(reply_token, TextSendMessage(text=text), ImageSendMessage(original_content_url = image_url, preview_image_url = image_url), TextSendMessage(
        text=text1, quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label="Continue", text="Next"))])))
    else:
        send_message(reply_token, TextSendMessage(text=text), ImageSendMessage(original_content_url = image_url, preview_image_url = image_url))

def send_text_and_question(reply_token, text1, text2 = None, text3 = None, text4 = None, text5 = None):
    question_template = TemplateSendMessage(alt_text='template', template=ConfirmTemplate(title='ConfirmTemplate', text=text1, actions=[MessageTemplateAction(label='Yes', text='Yes'), MessageTemplateAction(label='No', text='No')]))
    if text5 != None:
        question_template.template.text = text5
        send_message(reply_token, TextSendMessage(text=text1), TextSendMessage(text=text2), TextSendMessage(text=text3), TextSendMessage(text=text4), question_template)
    elif text4 != None:
        question_template.template.text = text4
        send_message(reply_token, TextSendMessage(text=text1), TextSendMessage(text=text2), TextSendMessage(text=text3), question_template)
    elif text3 != None:
        question_template.template.text = text3
        send_message(reply_token, TextSendMessage(text=text1), TextSendMessage(text=text2), question_template)
    elif text2 != None:
        question_template.template.text = text2
        send_message(reply_token, TextSendMessage(text=text1), question_template)
    else:
        send_message(reply_token, question_template)
    return "OK"


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
