from pymavlink import mavutil
import time

# --------------------------------------------------------
# Configuración de conexión
# --------------------------------------------------------
# USB real:
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# SITL por UDP:
# master = mavutil.mavlink_connection('udpin:localhost:14551')

# Esperar el primer heartbeat
print("Esperando heartbeat...")
master.wait_heartbeat()
print(f"¡Conectado! (Sistema: {master.target_system}, Componente: {master.target_component})")

# --------------------------------------------------------
# Enviar heartbeat de prueba (opcional)
# --------------------------------------------------------
# master.mav.heartbeat_send(
#    type=mavutil.mavlink.MAV_TYPE_QUADROTOR,
#    autopilot=mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA,
#    base_mode=0,
#    custom_mode=0,
#    system_status=mavutil.mavlink.MAV_STATE_ACTIVE
# )
# print("Heartbeat enviado")

# --------------------------------------------------------
# Medición de ancho de banda
# --------------------------------------------------------
print("\nMidiendo ancho de banda de mensajes MAVLink...")
interval = 1.0  # segundos
bytes_recibidos = 0
start_time = time.time()
ultimo_print = start_time

try:
    while True:
        msg = master.recv_match(blocking=True, timeout=1)
        if msg:
            # Tamaño aproximado del mensaje en bytes
            bytes_recibidos += len(msg.get_msgbuf())

        ahora = time.time()
        if ahora - ultimo_print >= interval:
            bw = bytes_recibidos / (ahora - ultimo_print)  # bytes/segundo
            print(f"Ancho de banda ≈ {bw:.2f} bytes/s")
            bytes_recibidos = 0
            ultimo_print = ahora

except KeyboardInterrupt:
    print("\nMedición detenida por usuario")