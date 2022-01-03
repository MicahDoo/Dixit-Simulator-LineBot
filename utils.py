import os
import data

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
    hand_json = data.flex_carousel
    hand_template = FlexSendMessage("Show hand", hand_json)
    # hand_template = TemplateSendMessage(
    #     alt_text='Buttons Template',
    #     template=ImageCarouselTemplate(
    #         columns=[
    #         ]
    #     )
    # )
    for i in range(n):
        image_json = data.image_bubble
        image_flex = FlexContainer(image_json)
        print(image_flex)
        image = BubbleContainer(image_flex)
        print(image)
        image.action = MessageAction(text=str(i+1))
        image.body.contents[0].url = data.img_urls[hand[i]]
        image.body.contents[1].contents[0].text = str(i+1)
        hand_template.template.columns.append(
            image
            # ImageCarouselColumn(
            #     image_url=data.img_urls[hand[i]],
            #     action=MessageAction(
            #         text=str(i+1)
            #     )
            # )
        )
    send_message(reply_token, TextSendMessage(text=text), hand_template)

def show_display(reply_token, display, text, n, text1 = None):
    line_bot_api = LineBotApi(channel_access_token)
    cards = " "
    for card in display:
        cards = cards + " " + str(card)
    print(cards)
    hand_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ImageCarouselTemplate(
            columns=[
            ]
        )
    )
    for i in range(n):
        hand_template.template.columns.append(
            ImageCarouselColumn(
                image_url=data.img_urls[display[i]],
                action=MessageAction(
                    text=str(i+1)
                )
            )
        )
    if text1 != None:
        line_bot_api.reply_message(reply_token, [TextSendMessage(text=text), hand_template, TextSendMessage(
        text=text1, quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label="Continue", text="Next"))]))])
    else:
        send_message(reply_token, TextSendMessage(text=text), hand_template)

def send_text_and_image(reply_token, text, image_number, text1=None):
    image_url = data.img_urls[image_number]
    if text1 != None:
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
