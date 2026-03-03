#include "chacha20.h"
#include <cstring>

// rotate left
static inline uint32_t rotl(uint32_t x, int n) {
    return (x << n) | (x >> (32 - n));
}

// quarter round as defined in RFC 8439
#define QR(a,b,c,d)     \
    a += b, d ^= a, d = rotl(d,16), \
    c += d, b ^= c, b = rotl(b,12), \
    a += b, d ^= a, d = rotl(d,8),  \
    c += d, b ^= c, b = rotl(b,7)

// core ChaCha20 block function: input state -> 64 bytes of keystream
static void chacha20_block(uint32_t output[16], const uint32_t input[16]) {
    int i;
    uint32_t x[16];
    memcpy(x, input, sizeof(x));
    for (i = 0; i < 10; ++i) {
        // column rounds
        QR(x[0], x[4], x[8], x[12]);
        QR(x[1], x[5], x[9], x[13]);
        QR(x[2], x[6], x[10], x[14]);
        QR(x[3], x[7], x[11], x[15]);
        // diagonal rounds
        QR(x[0], x[5], x[10], x[15]);
        QR(x[1], x[6], x[11], x[12]);
        QR(x[2], x[7], x[8], x[13]);
        QR(x[3], x[4], x[9], x[14]);
    }
    for (i = 0; i < 16; ++i) {
        output[i] = x[i] + input[i];
    }
}

void chacha20_encrypt(const uint8_t key[32], const uint8_t nonce[12],
                      uint32_t counter,
                      const uint8_t* in, uint8_t* out, size_t len) {
    // 16-word (512-bit) state
    uint32_t state[16];
    static const char* constants = "expand 32-byte k"; // little-endian

    // set up state
    state[0]  = ((uint32_t)constants[0]) | ((uint32_t)constants[1] << 8) |
                ((uint32_t)constants[2] << 16) | ((uint32_t)constants[3] << 24);
    state[1]  = ((uint32_t)constants[4]) | ((uint32_t)constants[5] << 8) |
                ((uint32_t)constants[6] << 16) | ((uint32_t)constants[7] << 24);
    state[2]  = ((uint32_t)constants[8]) | ((uint32_t)constants[9] << 8) |
                ((uint32_t)constants[10] << 16) | ((uint32_t)constants[11] << 24);
    state[3]  = ((uint32_t)constants[12]) | ((uint32_t)constants[13] << 8) |
                ((uint32_t)constants[14] << 16) | ((uint32_t)constants[15] << 24);
    // key
    for (int i = 0; i < 8; ++i) {
        state[4 + i] = ((uint32_t)key[4*i])       |
                       ((uint32_t)key[4*i + 1] << 8) |
                       ((uint32_t)key[4*i + 2] << 16) |
                       ((uint32_t)key[4*i + 3] << 24);
    }
    // counter
    state[12] = counter;
    // nonce
    for (int i = 0; i < 3; ++i) {
        state[13 + i] = ((uint32_t)nonce[4*i])       |
                        ((uint32_t)nonce[4*i + 1] << 8) |
                        ((uint32_t)nonce[4*i + 2] << 16) |
                        ((uint32_t)nonce[4*i + 3] << 24);
    }

    uint8_t block[64];
    size_t offset = 0;
    while (len > 0) {
        uint32_t output_state[16];
        chacha20_block(output_state, state);
        // serialize keystream
        for (int i = 0; i < 16; ++i) {
            block[4*i]     = output_state[i] & 0xff;
            block[4*i + 1] = (output_state[i] >> 8) & 0xff;
            block[4*i + 2] = (output_state[i] >> 16) & 0xff;
            block[4*i + 3] = (output_state[i] >> 24) & 0xff;
        }
        size_t chunk = len < 64 ? len : 64;
        for (size_t i = 0; i < chunk; ++i) {
            out[offset + i] = in[offset + i] ^ block[i];
        }
        len -= chunk;
        offset += chunk;
        // increment counter
        state[12]++;
    }
}
