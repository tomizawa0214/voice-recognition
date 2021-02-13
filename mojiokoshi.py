import pandas as pd #エクセルのブックを操作するライブラリの読み込み
import speech_recognition as sr
import datetime as dt
import threading


r = sr.Recognizer() #言葉を認識するオブジェクト
mic = sr.Microphone() #マイクオブジェクト
# result_list = [] #エクセルに出力するデータを格納するリスト
# endFlag = False #記録終了フラグ
# lock = threading.RLock() #ロックオブジェクトの生成

while True:
    print("記録を開始します。何か喋ってください。")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    print ("認識中…")

    try:
        print(r.recognize_google(audio, language='ja-JP'))

        # "ストップ" と言ったら音声認識を止める
        if r.recognize_google(audio, language='ja-JP') == "ストップ" :
            print("end")
            break

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))