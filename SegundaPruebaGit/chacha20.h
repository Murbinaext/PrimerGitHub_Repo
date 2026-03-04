#ifndef CHACHA20_H
#define CHACHA20_H

#include <cstddef>
#include <cstdint>

/**
 * Encrypt/decrypt data using ChaCha20 stream cipher.
 *
 * 
 * @param key     32-byte key
 * @param nonce   12-byte nonce
 * @param counter initial block counter (usually 1)
 * @param in      input buffer (plaintext or ciphertext)
 * @param out     output buffer (must be at least `len` bytes)
 * @param len     number of bytes to process
 *
 * ChaCha20 is symmetrical so the same function is used for encrypting
 * and decrypting.
 */
void chacha20_encrypt(const uint8_t key[32], const uint8_t nonce[12],
                      uint32_t counter,
                      const uint8_t* in, uint8_t* out, size_t len);

#endif // CHACHA20_H
