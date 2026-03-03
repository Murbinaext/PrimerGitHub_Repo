"""
Script para medir el tiempo de ejecución de cifrado y descifrado con ChaCha20Poly1305
"""

import time
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os

# Generar una clave de 32 bytes para ChaCha20Poly1305
key = os.urandom(32)
# Generar un nonce de 12 bytes para ChaCha20Poly1305
nonce = os.urandom(12)

# Texto plano a cifrar
plaintext = b"Este es un mensaje de prueba para medir el tiempo de ejeccion con ChaCha20"

print("=" * 70)
print("MEDICIÓN DE TIEMPO: CIFRADO Y DESCIFRADO CON CHACHA20POLY1305")
print("=" * 70)
print(f"\nTexto original: {plaintext.decode()}")
print(f"Longitud del texto: {len(plaintext)} bytes")
print(f"\nClave: {len(key)} bytes")
print(f"Nonce: {len(nonce)} bytes")
print("\n" + "=" * 70)

# Crear el cipher
cipher = ChaCha20Poly1305(key)

# ============== CIFRADO (Packaging) ==============
print("\n[1] CIFRADO (Packaging):")
print("-" * 70)

# Medir tiempo de cifrado
start_time = time.time()
ciphertext = cipher.encrypt(nonce, plaintext, None)
end_time = time.time()

encryption_time = end_time - start_time

print(f"Texto cifrado: {ciphertext.hex()[:50]}...")
print(f"Longitud del texto cifrado: {len(ciphertext)} bytes")
print(f"Tiempo de cifrado: {encryption_time * 1000:.6f} ms")
print(f"Tiempo de cifrado: {encryption_time * 1000000:.2f} μs")

# ============== DESCIFRADO (Unpackaging) ==============
print("\n[2] DESCIFRADO (Unpackaging):")
print("-" * 70)

# Medir tiempo de descifrado
start_time = time.time()
decrypted_text = cipher.decrypt(nonce, ciphertext, None)
end_time = time.time()

decryption_time = end_time - start_time

print(f"Texto descifrado: {decrypted_text.decode()}")
print(f"Longitud del texto descifrado: {len(decrypted_text)} bytes")
print(f"Tiempo de descifrado: {decryption_time * 1000:.6f} ms")
print(f"Tiempo de descifrado: {decryption_time * 1000000:.2f} μs")

# ============== RESUMEN ==============
print("\n" + "=" * 70)
print("RESUMEN:")
print("=" * 70)
print(f"Tiempo total (cifrado + descifrado): {(encryption_time + decryption_time) * 1000:.6f} ms")
print(f"Tiempo total: {(encryption_time + decryption_time) * 1000000:.2f} μs")
print(f"\nVerificación - ¿Descifrado correcto?: {plaintext == decrypted_text}")
print("=" * 70)
