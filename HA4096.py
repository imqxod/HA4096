class HA4096:
    def __init__(self):
        self.initial_state = [
            0x6A09E667F3BCC908, 0xBB67AE8584CAA73B, 0x3C6EF372FE94F82B, 0xA54FF53A5F1D36F1,
            0x510E527FADE682D1, 0x9B05688C2B3E6C1F, 0x1F83D9ABFB41BD6B, 0x5BE0CD19137E2179
        ]
        self.prime_constants = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        self.rounds = 1000

    def _pad_message(self, msg):
        original_len = len(msg) * 8
        msg += b'\x80'
        while (len(msg) * 8) % 1024 != 896:
            msg += b'\x00'
        msg += original_len.to_bytes(16, byteorder='big')
        return msg

    def _mod_exp(self, base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result

    def _rotate_left(self, value, bits, size=64):
        return ((value << bits) | (value >> (size - bits))) & ((1 << size) - 1)

    def _improved_mix(self, a, b, c, d, round_key):
        mix1 = (a ^ self._rotate_left(b, 13) + c) & 0xFFFFFFFFFFFFFFFF
        mix2 = (self._mod_exp(mix1, round_key, 0xFFFFFFFFFFFFFFFF) ^ d) & 0xFFFFFFFFFFFFFFFF
        return mix2

    def _compress_chunk(self, chunk, state):
        words = [int.from_bytes(chunk[i:i+8], 'big') for i in range(0, 128, 8)]
        for i in range(16, 80):
            s0 = self._rotate_left(words[i-15], 1) ^ self._rotate_left(words[i-15], 8) ^ (words[i-15] >> 7)
            s1 = self._rotate_left(words[i-2], 19) ^ self._rotate_left(words[i-2], 61) ^ (words[i-2] >> 6)
            words.append((words[i-16] + s0 + words[i-7] + s1) & 0xFFFFFFFFFFFFFFFF)

        a, b, c, d, e, f, g, h = state

        for r in range(self.rounds):
            for i in range(80):
                s1 = self._rotate_left(e, 14) ^ self._rotate_left(e, 18) ^ self._rotate_left(e, 41)
                ch = (e & f) ^ (~e & g)
                temp1 = (h + s1 + ch + words[i] + self.prime_constants[i % 16]) & 0xFFFFFFFFFFFFFFFF
                s0 = self._rotate_left(a, 28) ^ self._rotate_left(a, 34) ^ self._rotate_left(a, 39)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (s0 + maj) & 0xFFFFFFFFFFFFFFFF
                temp1 = self._improved_mix(temp1, b, c, d, self.prime_constants[r % 16])

                h = g
                g = f
                f = e
                e = (d + temp1) & 0xFFFFFFFFFFFFFFFF
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xFFFFFFFFFFFFFFFF

        return [(state[i] + v) & 0xFFFFFFFFFFFFFFFF for i, v in enumerate([a, b, c, d, e, f, g, h])]

    def encrypt(self, text):
        padded_message = self._pad_message(text.encode())
        state = self.initial_state[:]
        for i in range(0, len(padded_message), 128):
            chunk = padded_message[i:i+128]
            state = self._compress_chunk(chunk, state)
        return ''.join(f'{x:016x}' for x in state)