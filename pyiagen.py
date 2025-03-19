import os
import wave
import json
import pyaudio
import wave
import openai
import requests
import uuid
import pathlib
import os
import webbrowser
import uuid
import speech_recognition as sr
from openai import OpenAI
from bs4 import BeautifulSoup
#DEL FOR SHARING
openia_secret_key = 'OPEN_AI_SECRET_KEY-CHATGPT'
html_rx = 'false'

def startApp():
	print('Welcome, to PY-IA Generative API')
	print('--------------------------------')
	print('Speek and get IA LLMs results from IA Generative APIs')
	print('Please, speak to start your works')
	print('--------------------------------')
	print('Recording Init - Wait, please')
	rvx = getCommand()
	print('Recording Done - All right, now your speak will converted to text')
	print('Convert Voice to Text Init - Wait, please')
	rvtx = getCommandToTextSR(rvx)
	print('Convert Voice to Text Done - All Right, now your works will sended to IA API')
	print('Generate Content with API Init - Wait, please')
	rvyix = getCommandToIA(rvtx)
	html_rx = writeFile(rvyix)
	print('Generate Content with API Done - All Right, the works is done, please read bellow your works and input A(Open on the Directory) or B(Open on the Web Browser) to open your works file..')
	getChoice('0x00')
	getChoice('0x001')

def getChoice(ix):
	if(ix == '0x00'):
		rcx = input("(A-Open Directory | B-Open on the Web Browser):")
		try:
			if(rcx == 'a'):
				# Get the current working directory
				current_directory = pathlib.Path().resolve()
				# Open the current directory
				os.startfile(current_directory)
			if(rcx == 'b'):
				# Get the current directory
				current_directory = os.getcwd()
				# Define the HTML file name
				html_file = str(html_rx )
				# Create the full path to the HTML file
				file_path = os.path.join(current_directory, html_file)
				# Open the HTML file in the default web browser
				webbrowser.open(f"file://{file_path}")
			if(rcx != 'a' and rcx != 'b'):
				getChoice('0x00')
		except:
			getChoice('0x00')
	if(ix == '0x001'):
		rcx_x = input('(A):Continue | (B):Quit:')
		if(rcx_x == 'a'):
			startApp()
		if(rcx_x == 'b'):
			print('Bye, thanks by PY-IA Generative API')
			print('--------------------------------')
			print('App is Done...')
		if(rcx_x != 'a' and rcx_x != 'b'):
			getChoice('0x001')

def writeFile(rvftx):
	# Generate a random UUID
	guid = uuid.uuid4()
	rx_fx = str(guid) + '.html'
	rx_fx = rx_fx.replace('-','_')
	# Write the HTML content to a file
	with open(rx_fx, "w") as file:
		print(str(rvftx))
		file.write(str(rvftx))
	print("File Saved...")
	return rx_fx

def getCommandToIA(rvtx):
	print(rvtx)
	# Replace 'your-api-key' with your actual OpenAI API key
	client = OpenAI(
	api_key=openia_secret_key)
	completion = client.chat.completions.create(model="gpt-4o-mini",store=True,messages=[{"role": "user", "content": str(rvtx)}])
	result = completion.choices[0].message.content
	print('------------------------------')
	print('Your Works ir Done -  See your result:')
	print('------------------------------')
	print(result)
	return result

def getCommandToTextSR(rvx):
	rx = 'false'
	# Initialize the recognizer
	recognizer = sr.Recognizer()
	# Load the audio file
	with sr.AudioFile('output.wav') as source:
		print("Processing audio file...")
		audio_data = recognizer.record(source)
	# Recognize speech
	try:
		rx = recognizer.recognize_google(audio_data)
		print("Text from audio:", rx)
	except sr.UnknownValueError:
		print("Sorry, speech could not be recognized.")
	except sr.RequestError:
		print("Couldn't request results. Check your internet connection.")
	return str(rx)

def getCommand():
	# Parameters for recording
	FORMAT = pyaudio.paInt16  # 16-bit resolution
	CHANNELS = 1  # Mono channel
	RATE = 44100  # 44.1kHz sampling rate
	CHUNK = 1024  # 1024 samples per frame
	RECORD_SECONDS = 5  # Duration of recording
	OUTPUT_FILENAME = "output.wav"  # Output file name

	# Initialize PyAudio
	audio = pyaudio.PyAudio()

	# Open stream
	stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
	print("Recording...")
	frames = []
	# Record data
	for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	print("Recording finished.")
	# Stop and close the stream
	stream.stop_stream()
	stream.close()
	audio.terminate()
	# Save the recorded data as a WAV file
	with wave.open(OUTPUT_FILENAME, 'wb') as wf:
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(audio.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
	print(f"Await, the voice command is done... Congratulations, success...")
	return OUTPUT_FILENAME

startApp()