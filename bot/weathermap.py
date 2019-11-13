import requests
import json

def get_weather_from_api():
    # APIキーの指定
    apikey = "a9a2238e4624c8c1203e49d4e0e3643f"

    # 天気を調べたい都市の一覧
    cities = ["Tokyo,JP", "London,US", "New York,US"]
    # APIのひな型
    api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

    # 温度変換(ケルビン→摂氏)
    k2c = lambda k: k - 273.15

    # 各都市の温度を取得する
    for name in cities:
        # APIのURLを得る
        url = api.format(city=name, key=apikey)
        # 実際にAPIにリクエストを送信して結果を取得する
        r = requests.get(url)
        # 結果はJSON形式なのでデコードする
        data = json.loads(r.text)

        # 結果を出力
        msg += "都市:" + data["name"] + "\n"
        msg += " 天気:" + data["weather"][0]["description"] + "\n"
        msg += " 最低気温=" + str(k2c(data["main"]["temp_min"])) + "\n"
        msg += " 最高気温=" + str(k2c(data["main"]["temp_max"])) + "\n"
        msg += " 湿度=" + str(data["main"]["humidity"]) + "\n"
        msg += " 気圧=" + str(data["main"]["pressure"]) + "\n"
        msg += " 風向き=" + str(data["wind"]["deg"]) + "\n"
        msg += " 風速度=" + str(data["wind"]["speed"]) + "\n\n"


