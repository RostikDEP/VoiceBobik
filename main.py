import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
from transliterate import translit
from converter_c import *
import pyperclip
import keyboard

tts = pyttsx3.init()
voices = tts.getProperty('voices')

for voice in voices:
	if voice.name == "Anatol":
		tts.setProperty('voice', voice.id)


def paste(text: str):     
	buffer = pyperclip.paste()
	pyperclip.copy(text)
	keyboard.press_and_release('ctrl + v')
	pyperclip.copy(buffer)


z= 0
while z < 5:
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Привіт начальнику! Я Бобік")
	    audio = r.listen(source)

	z +=1
	try:
		text = r.recognize_google(audio, language="uk-UK")
		print(text)
		if "YouTube" in text:
			tts.say("Бобік радий виконати ваш наказ.")
			tts.runAndWait()	
			webbrowser.open("YouTube.com")
			tts.say("Відкриваю Ютуб.")
			tts.runAndWait()	

		if "яка твоя мрія" in text.lower():
			tts.say("Засунути Якіну в жопу бутилку від пива та йобнуть йому палкою поголові")
			tts.runAndWait()	

		if "не любиш" in text.lower():
			tts.say("Бо він кончиний мудак з їбалом чупакабри. Таких уйобків Як якін требе ловити і проводити над ними досліди")
			tts.runAndWait()	

		if "зі мною" in text.lower():
			tts.say("Ростіка потрібно любити та поважати. Він на цьому світі тільки один такий. Хороший та унікальний. Його потрібно берегти. Він - скарб усього людства")
			tts.runAndWait()	

		if "дякую" in text.lower():
			tts.say("Без питаннь Бро")
			tts.runAndWait()	


		if "друкуй" in text.lower():

			tts.say("Виконую.")
			tts.runAndWait()

			text = text.lower()
			text = text.replace("бобік", "")
			
			pyperclip.copy(text.replace("друкуй", ""))
			keyboard.press_and_release('ctrl + v')

	except sr.UnknownValueError:  
		print("Error")

