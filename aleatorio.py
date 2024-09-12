import threading
import requests
import random
import time
import string

# Configuración
target_url = "http://127.0.0.1:8000"  # Asegúrate de que este puerto esté abierto o cámbialo según sea necesario
num_threads = 50
attack_duration = 30  # El ataque dura solo 30 segundos

# Palabras para generar la clave aleatoria
palabras = ["python", "seguridad", "red", "wireshark", "captura", "paquete", "Guatemala", "Honduras", "oculto", "clave"]

# Función para generar el mensaje secreto con clave aleatoria
def generar_mensaje_secreto():
    palabra_clave = random.choice(palabras)
    numero_aleatorio = random.randint(1000, 9999)
    mensaje_base = "MENSAJE_SECRETO_ENCONTRADO_Felicidades_La_informacion_confidencial_es_"
    return f"{mensaje_base}_{palabra_clave.upper()}_{numero_aleatorio}"

# Generar el mensaje secreto al inicio del programa
mensaje_secreto = generar_mensaje_secreto()

def create_payload():
    return {'message': mensaje_secreto}

def send_requests():
    end_time = time.time() + attack_duration
    while time.time() < end_time:
        try:
            if random.random() < 0.1:  # 10% de probabilidad de enviar el mensaje oculto
                payload = create_payload()
                requests.post(target_url, data=payload, timeout=1)
            else:
                requests.get(f"{target_url}/{random.randint(1, 1000)}", timeout=1)
        except:
            pass

def start_attack():
    thread_list = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests)
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    print(f"Iniciando simulación de ataque DDoS con mensaje oculto en {target_url}")
    print(f"Duración: {attack_duration} segundos")
    print("ADVERTENCIA: Este script es solo para fines educativos en un entorno controlado.")
    # print(f"Mensaje secreto generado: {mensaje_secreto}")
    start_attack()
    print("Simulación completada. Analiza la captura en Wireshark para encontrar el mensaje oculto.")