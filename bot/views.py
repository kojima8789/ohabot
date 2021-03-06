from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    LocationMessage
)
from . import scrape as sc
from . import weathermap as we
from . import news as ne
import urllib3.request
import os

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseForbidden()
    return HttpResponse('OK', status=200)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    msg = we.get_weather_from_api()
    news = ne.get_yahoo_news()

    if '天気' in text:
        line_bot_api.reply_message(
        event.reply_token,
        [
        TextSendMessage(text='位置情報を教えてください。'),
        TextSendMessage(text='line://nv/location')
        ]
        )
    elif '東京' in text:

        line_bot_api.reply_message(
        event.reply_token,

        TextSendMessage(text=msg)

        )
    elif 'ニュース' in text:
        line_bot_api.reply_message(
            event.reply_token,

            TextSendMessage(text=news)

        )

    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    text = event.message.address

    result = sc.get_weather_from_location(text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result)
    )


# オウム返し
# @handler.add(MessageEvent, message=TextMessage)
# def handle_text_message(event):
#     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
        port = int(os.getenv("PORT", 5000))
        app.run(host="0.0.0.0", port=port)

