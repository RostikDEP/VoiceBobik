import speech_recognition as sr
import pyttsx3
import serial
import webbrowser
from fuzzywuzzy import fuzz
from config import * 
import random
import quotes
import time

try:
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = 'COM3'
	ser.open()
except:
	print("Open port ERROR")


class Communicator:
	def __init__(self):
		#-------------------init speaker------------------------------
		self.tts = pyttsx3.init()
		voices = self.tts.getProperty('voices')

		for voice in voices:
			if voice.name == "Anatol":
				self.tts.setProperty('voice', voice.id)
		#-------------------init listener-----------------------------
		self.recognizer = sr.Recognizer()
		self.listening = True


	def speek(self, text):
		self.tts.say(text)
		self.tts.runAndWait()


	def listen(self):
		while self.listening:
			with sr.Microphone() as source:
			    print("Слухаю...")
			    audio = self.recognizer.listen(source)

			try:
				text = self.recognizer.recognize_google(audio, language="uk-UK")
				print(f"Ви сказали: {text}")
				CommandsHandler().process(text)
			except:
				print("Не розбірливо...")



class CommandsHandler:
	def __init__(self):
		self.serialX = SerialX("COM3")

	def process(self, cmd):
		print("LOL")
		cmd = cmd.lower()
		print("process")
		if fuzz.ratio(NAME, cmd) > 80:
			cmd = cmd.replace(NAME, "")

			answer_id = random.randint(0, len(quotes.answers))
			answer = quotes.answers["welcome"][answer_id] 
			communicator.speek(answer)


			if "увімкни світло" in cmd:
				self.serialX.light_turn_on(True)
			if "вимкни світло" in cmd:
				self.serialX.light_turn_on(False)
			# if "youtube" in cmd:
			# 	Communicator().speek("Радий виконати ваш наказ")
			# 	webbrowser.open("youtube.com")
			# 	Communicator().speek("Відкриваю ютуб")
			kon = True
			while kon:
				with sr.Microphone() as source:
				    print("Слухаю...")
				    audio = communicator.recognizer.listen(source)
				    text = communicator.recognizer.recognize_google(audio, language="uk-UK")
				    print(F"SAID: {text}")

				    if "двигун" in text.lower():
				    	self.serialX.light_turn_on(True)


				    kon = False



class SerialX:
	def __init__(self, port):
		self.port = port


	def light_turn_on(self, on):
		if on == True:
			print("Debug")
			Communicator().speek("Запускаю двигун")
			self.write("Enable")
			time.sleep(1)
			self.write("Disable")
			# print("Enable light")
		else:
			print("Debug")
			Communicator().speek("Вимикаю світло.")
			self.write("Disable")
			print("Disable light")


	def write(self, data):
		print("Writing")


		ser.write(data.encode('utf-8') )
		print("SUCCES")



if __name__ == '__main__':
	communicator = Communicator()
	communicator.listen()
