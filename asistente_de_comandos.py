import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

def escuchar_comando():
    with sr.Microphone() as source:
        print("🎤 Escuchando comando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            comando = recognizer.recognize_google(audio)
            print(f"✅ Comando reconocido: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("❌ No entendí el comando.")
            return ""
        except sr.RequestError:
            print("⚠️ Error con el servicio de reconocimiento.")
            return ""

def ejecutar_comando(comando):
    if 'escanear la red' in comando:
        subprocess.run(['nmap', '-sn', '192.168.1.0/24'])
    elif 'escanear puertos' in comando:
        subprocess.run(['nmap', '-p-', '192.168.1.10'])
    elif 'escanear agresivo' in comando:
        subprocess.run(['nmap', '-A', '192.168.1.10'])
    elif 'detectar sistema operativo' in comando:
        subprocess.run(['nmap', '-O', '192.168.1.10'])
    elif 'enumerar smb' in comando:
        subprocess.run(['enum4linux', '192.168.1.10'])
    elif 'consulta dns' in comando:
        subprocess.run(['nslookup', 'example.com'])
    elif 'buscar vulnerabilidades' in comando:
        subprocess.run(['nmap', '--script', 'vuln', '192.168.1.10'])
    elif 'sqlmap' in comando:
        subprocess.run(['sqlmap', '-u', 'http://192.168.1.10/vulnerable.php?id=1', '--batch'])
    elif 'fuerza bruta' in comando:
        subprocess.run(['hydra', '-l', 'admin', '-P', '/usr/share/wordlists/rockyou.txt', 'ssh://192.168.1.10'])
    elif 'sniffer' in comando:
        subprocess.run(['tcpdump', '-i', 'eth0'])
    elif 'wireshark' in comando:
        subprocess.run(['wireshark'])
    elif 'metasploit' in comando:
        subprocess.run(['msfconsole'])
    elif 'gobuster' in comando:
        subprocess.run(['gobuster', 'dir', '-u', 'http://192.168.1.10', '-w', '/usr/share/wordlists/dirb/common.txt'])
    elif 'searchsploit' in comando:
        subprocess.run(['searchsploit', 'apache struts'])
    elif 'salir' in comando:
        print("👋 Cerrando el asistente.")
        exit()
    else:
        print("⚠️ Comando no reconocido. Intenta otra vez.")

def asistente_pentesting():
    print("🛡️ Asistente de Pentesting por Voz 🛡️\nDi un comando cuando estés listo.")
    while True:
        comando = escuchar_comando()
        if comando:
            ejecutar_comando(comando)

if __name__ == "__main__":
    asistente_pentesting()
