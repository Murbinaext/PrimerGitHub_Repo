from pymavlink import mavutil
import ardupilotmega  # tu dialecto personalizado

# Conexión
puerto = '/dev/ttyACM0'
master = mavutil.mavlink_connection(
    puerto,
    baud=115200,
    dialect="ardupilotmega"
)

print("Esperando heartbeat...")
master.wait_heartbeat()
print("Conectado")

print("Esperando MI_MENSAJE_PRUEBA...")

while True:

    msg = master.recv_match(blocking=True)
    if msg:
        print(msg.get_type())



    # msg = master.recv_match(
    #     type='MI_MENSAJE_PRUEBA',
    #     blocking=True
    # )

    # if msg:
    #     print("Mensaje recibido:")
    #     print(msg.to_dict())