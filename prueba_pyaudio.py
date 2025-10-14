import pyaudio

p = pyaudio.PyAudio()

# Ver los dispositivos de audio disponibles
print("Dispositivos disponibles:")
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))
