from pymavlink import mavutil
import math

# 1. Conexión (Asegúrate de poner tu puerto correcto, el que te funcionó antes)
puerto = '/dev/ttyACM0' 
the_connection = mavutil.mavlink_connection(puerto, baud=115200)

# 2. Esperamos el heartbeat para asegurar que hay comunicación
print("Esperando heartbeat...")
the_connection.wait_heartbeat()
print("---Conectado a la controladora---")

print("\nLeyendo la inclinación de la placa (Presiona Ctrl+C para parar)...")

try:
    # Hacemos un bucle para leer 20 mensajes seguidos
    for i in range(500):
        # recv_match busca en el flujo de datos y "atrapa" solo el mensaje que le pedimos
        # blocking=True hace que el código espere hasta que llegue ese mensaje concreto
        msg = the_connection.recv_match(type='ATTITUDE', blocking=True)
        
        # Ardupilot envía estos datos en radianes. 
        # Los convertimos a grados (°) para que los entiendas mejor a simple vista.
        secuencia = msg.get_header().seq    # Lectura del numero de secuencia del mensaje attitude
        roll = math.degrees(msg.roll)
        pitch = math.degrees(msg.pitch)
        yaw = math.degrees(msg.yaw)
        
        # Imprimimos los datos formateados con 2 decimales
        print(f"Nº Secuencia: {secuencia} | Roll (Balanceo): {roll:>7.2f}° | Pitch (Cabeceo): {pitch:>7.2f}° | Yaw (Guiñada): {yaw:>7.2f}°")
        
except KeyboardInterrupt:
    # Esto captura si pulsas Ctrl+C en la terminal para salir limpiamente
    print("\nLectura detenida por el usuario.")