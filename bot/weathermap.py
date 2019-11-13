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
        weather = ("+ 都市=", data["name"])
                  ("| 天気=", data["weather"][0]["description"])
                  ("| 最低気温=", k2c(data["main"]["temp_min"]))
        # print("| 最高気温=", k2c(data["main"]["temp_max"]))
        # print("| 湿度=", data["main"]["humidity"])
        # print("| 気圧=", data["wind"]["deg"])
        # print("| 風速度=", data["wind"]["speed"])
        # print("")

        return weather

