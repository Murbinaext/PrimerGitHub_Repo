from pymavlink import mavutil
import time

# 1. Conexión a la placa por USB
puerto = '/dev/ttyACM0' 
the_connection = mavutil.mavlink_connection(puerto, baud=115200)

print("Esperando heartbeat...")
the_connection.wait_heartbeat()
print(f"¡Conectado! (Sistema: {the_connection.target_system}, Componente: {the_connection.target_component})")

## -------------------------------------------------------------------------------
# 2. Definimos el nombre del parámetro que queremos leer (debe enviarse en bytes)
nombre_parametro = b'HEARTBEAT'
## -------------------------------------------------------------------------------


print(f"\nPidiendo el parámetro {nombre_parametro.decode()}...")

# 3. Enviamos el mensaje MAVLink pidiendo que nos lea ese parámetro
# param_request_read_send necesita: (ID_sistema_destino, ID_componente_destino, ID_del_parametro, Indice_del_parametro)
# Usamos índice -1 porque le estamos dando el nombre exacto.
the_connection.mav.param_request_read_send(
    the_connection.target_system, 
    the_connection.target_component,
    nombre_parametro,
    -1
)

# 4. Esperamos la respuesta de la placa
# Le decimos que bloquee la ejecución hasta recibir un mensaje de tipo 'PARAM_VALUE'
mensaje = the_connection.recv_match(type='HEARTBEAT', blocking=True, timeout=5)

if mensaje:
    print("\nRespuesta recibida")
    print(f"Parámetro: {mensaje.param_id}")
    print(f"Valor:     {mensaje.param_value}")
    print(f"Tipo:      {mensaje.param_type}")
else:
    print("\nNo se recibió respuesta del parámetro a tiempo.")