from speech_recognition import Recognizer, AudioFile

recognizer = Recognizer()

with AudioFile('thefile') as audio_file:
  audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)
print(text)