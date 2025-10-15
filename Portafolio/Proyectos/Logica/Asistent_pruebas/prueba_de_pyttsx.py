import pyttsx3

engine = pyttsx3.init('sapi5')  # o simplemente: pyttsx3.init()
engine.say("Hola, estoy hablando con sapi5 en Windows")
engine.runAndWait()
