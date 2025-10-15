import speech_recognition as sr

# Inicializa el reconocedor
r = sr.Recognizer()

# Usa el micrófono como fuente de entrada
with sr.Microphone() as source:
    print("Di algo...")
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio, language="es-ES")
    print("Has dicho:", texto)
except sr.UnknownValueError:
    print("No entendí lo que dijiste.")
except sr.RequestError:
    print("Error al conectar con el servicio de reconocimiento.")
