from pymavlink import mavutil
import time

# --------------------------------------------------------
# Conexión al autopiloto (ajusta según tu caso)
# --------------------------------------------------------
connection = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)  # USB
# connection = mavutil.mavlink_connection('udpin:localhost:14551')   # UDP, si usas SITL

print("Esperando heartbeat...")
connection.wait_heartbeat()
print(f"¡Conectado! (Sistema: {connection.target_system}, Componente: {connection.target_component})")

# --------------------------------------------------------
# Enviar comando para cambiar frecuencia de BATTERY_STATUS
# --------------------------------------------------------
interval_us = 50000  # intervalo en microsegundos -> 500000 us = 2 Hz

message = connection.mav.command_long_encode(
    connection.target_system,
    connection.target_component,
    mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
    0,
    mavutil.mavlink.MAVLINK_MSG_ID_HEARTBEAT,
    interval_us,
    0, 0, 0, 0, 0
)

connection.mav.send(message)

# Esperar ACK
response = connection.recv_match(type='COMMAND_ACK', blocking=True)
if response and response.command == mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL and response.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    print(f"Comando aceptado, interval = {interval_us / 1e6} s")
else:
    print("Comando falló")

# --------------------------------------------------------
# Observar mensajes en tiempo real
# --------------------------------------------------------
print("\nObservando mensajes HEARTBEAT...")
last_time = None

try:
    while True:
        msg = connection.recv_match(type='HEARTBEAT', blocking=True, timeout=5)
        if msg is None:
            print("No se recibió mensaje durante 5 segundos")
            continue
        
        now = time.time()
        if last_time is not None:
            dt = now - last_time
            freq = 1 / dt
            print(f"Mensaje recibido. Intervalo = {dt:.3f} s, Frecuencia ≈ {freq:.2f} Hz")
        else:
            print("Primer mensaje recibido")
        
        last_time = now

except KeyboardInterrupt:
    print("\nObservación detenida por usuario")