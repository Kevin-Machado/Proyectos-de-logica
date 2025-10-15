import speechre_cognition 
import pyttsx3
import spacy
import os
import subprocess

# Cargar modelo de NLP en español
nlp = spacy.load("es_core_news_sm")

# Motor de texto a voz
engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language="es-ES")
            print(f"Escuchado: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            hablar("No entendí lo que dijiste")
        except sr.RequestError:
            hablar("Error con el servicio de reconocimiento")
    return ""

def procesar_comando(texto):
    doc = nlp(texto)
    verbos = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    
    print(f"Verbos detectados: {verbos}")
    
    for verbo in verbos:
        if verbo == "abrir":
            if "navegador" in texto:
                hablar("Abriendo navegador")
                subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            elif "bloc" in texto:
                hablar("Abriendo bloc de notas")
                subprocess.Popen("notepad.exe")
        elif verbo == "cerrar":
            if "explorador" in texto:
                hablar("Cerrando explorador")
                os.system("taskkill /f /im explorer.exe")
        elif verbo == "reiniciar":
            hablar("Reiniciando sistema")
            os.system("shutdown /r /t 0")

# Programa principal
if __name__ == "__main__":
    hablar("Asistente iniciado. Te escucho.")
    comando = escuchar()
    if comando:
        procesar_comando(comando)
