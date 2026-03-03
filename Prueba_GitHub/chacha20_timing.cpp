#include <iostream>
#include <chrono>
#include <cstring>
#include <iomanip>
#include <random>

#include "chacha20.h"  // implementación incluida en este proyecto

// Función para convertir bytes a hexadecimal
std::string bytesToHex(const unsigned char* data, size_t len, size_t maxChars = 50) {
    std::string hex;
    for (size_t i = 0; i < len && i < maxChars; ++i) {
        hex += std::string("0123456789abcdef")[data[i] >> 4];
        hex += std::string("0123456789abcdef")[data[i] & 0x0f];
    }
    if (len > maxChars) hex += "...";
    return hex;
}

int main() {
    // Tamaño de clave y nonce para ChaCha20
    const int KEY_SIZE = 32;      // 256 bits
    const int NONCE_SIZE = 12;    // 96 bits

    // Generar clave y nonce aleatorios usando el generador de C++
    std::random_device rd;
    unsigned char key[KEY_SIZE];
    unsigned char nonce[NONCE_SIZE];
    for (int i = 0; i < KEY_SIZE; ++i) key[i] = static_cast<unsigned char>(rd());
    for (int i = 0; i < NONCE_SIZE; ++i) nonce[i] = static_cast<unsigned char>(rd());

    // Texto plano
    const char* plaintext = "Este es un mensaje de prueba para medir el tiempo de ejeccion con ChaCha20";
    size_t plaintext_len = std::strlen(plaintext);

    // Buffers para cifrado y descifrado (igual tamaño que el texto plano)
    unsigned char* ciphertext = new unsigned char[plaintext_len];
    unsigned char* decrypted = new unsigned char[plaintext_len];

    std::cout << std::string(70, '=') << std::endl;
    std::cout << "MEDICIÓN DE TIEMPO: CIFRADO Y DESCIFRADO CON CHACHA20POLY1305" << std::endl;
    std::cout << std::string(70, '=') << std::endl;

    std::cout << "\nTexto original: " << plaintext << std::endl;
    std::cout << "Longitud del texto: " << plaintext_len << " bytes" << std::endl;
    std::cout << "\nClave: " << KEY_SIZE << " bytes" << std::endl;
    std::cout << "Nonce: " << NONCE_SIZE << " bytes" << std::endl;
    std::cout << "\n" << std::string(70, '=') << std::endl;

    // ============== CIFRADO (Packaging) ==============
    std::cout << "\n[1] CIFRADO (Packaging):" << std::endl;
    std::cout << std::string(70, '-') << std::endl;

    // medir tiempo de cifrado usando implementación propia
    auto start = std::chrono::high_resolution_clock::now();
    chacha20_encrypt(key, nonce, 1, (const unsigned char*)plaintext, ciphertext, plaintext_len);
    auto end = std::chrono::high_resolution_clock::now();
    double encryption_time = std::chrono::duration<double, std::milli>(end - start).count();

    std::cout << "Texto cifrado: " << bytesToHex(ciphertext, plaintext_len) << std::endl;
    std::cout << "Longitud del texto cifrado: " << plaintext_len << " bytes" << std::endl;
    std::cout << std::fixed << std::setprecision(6);
    std::cout << "Tiempo de cifrado: " << encryption_time << " ms" << std::endl;
    std::cout << "Tiempo de cifrado: " << (encryption_time * 1000) << " μs" << std::endl;

    // ============== DESCIFRADO (Unpackaging) ==============
    std::cout << "\n[2] DESCIFRADO (Unpackaging):" << std::endl;
    std::cout << std::string(70, '-') << std::endl;

    // medir tiempo de descifrado (idéntico a cifrado)
    start = std::chrono::high_resolution_clock::now();
    chacha20_encrypt(key, nonce, 1, ciphertext, decrypted, plaintext_len);
    end = std::chrono::high_resolution_clock::now();
    double decryption_time = std::chrono::duration<double, std::milli>(end - start).count();

    std::cout << "Texto descifrado: ";
    for (size_t i = 0; i < plaintext_len; ++i) {
        std::cout << (char)decrypted[i];
    }
    std::cout << std::endl;
    std::cout << "Longitud del texto descifrado: " << plaintext_len << " bytes" << std::endl;
    std::cout << "Tiempo de descifrado: " << decryption_time << " ms" << std::endl;
    std::cout << "Tiempo de descifrado: " << (decryption_time * 1000) << " μs" << std::endl;

    // ============== RESUMEN ==============
    std::cout << "\n" << std::string(70, '=') << std::endl;
    std::cout << "RESUMEN:" << std::endl;
    std::cout << std::string(70, '=') << std::endl;
    std::cout << "Tiempo total (cifrado + descifrado): " 
              << (encryption_time + decryption_time) << " ms" << std::endl;
    std::cout << "Tiempo total: " 
              << ((encryption_time + decryption_time) * 1000) << " μs" << std::endl;

    // Verificación
    bool match = std::memcmp(decrypted, plaintext, plaintext_len) == 0;
    std::cout << "\nVerificación - ¿Descifrado correcto?: " 
              << (match ? "true" : "false") << std::endl;
    std::cout << std::string(70, '=') << std::endl;

    // liberar buffers
    delete [] ciphertext;
    delete [] decrypted;

    return 0;
}
