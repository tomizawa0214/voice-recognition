import speech_recognition as sr
from datetime import datetime
import os


#文字起こしファイルのファイル名を日付のtxtファイルとする
filename = datetime.now().strftime('%Y%m%d_%H%M')
txt = filename + ".txt"

with open(txt, 'w') as f: #txtファイルの新規作成 
    f.write(filename + "\n") #最初の一行目にはfilenameを記載する

r = sr.Recognizer() #言葉を認識するオブジェクト
mic = sr.Microphone() #マイクオブジェクト

while True:
    print("記録を開始するよ！何か喋ってね！")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    print ("考え中…")

    try:
        print(r.recognize_google(audio, language='ja-JP'))

        # "ストップ" と言ったら音声認識を止める
        if r.recognize_google(audio, language='ja-JP') == "ストップ" :
            print("end")
            break
        with open(txt,'a') as f: #ファイルの末尾に追記していく
            f.write("\n" + r.recognize_google(audio, language='ja-JP'))

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("すみません、ちょっと何言ってるかわかりません。")
    except sr.RequestError as e:
        print("すみません、ちょっと何言ってるかわかりません。; {0}".format(e))