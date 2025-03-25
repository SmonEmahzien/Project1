import sys

class Vcipher:
    def _init_(self):
        self.passkey = None

    def passkey(self,key):
        self.passkey = key.upper()
    def vEncrypt(self,text):
        if not self.passkey:
            return "error"
        return self._vigenere_cipher(text, self.passkey, encrypt=True)
    def vDecrypt(self,text):
        if not self.passkey:
            return"error"
        return self._vigenere_cipher(text, self.passkey, encrypt=False)

    def _vigenere_cipher(self, text, key, encrypt=True):
        result = []
        text = text.upper()
        key = key.upper()
        key_length = len(key)
        key_indices = [ord(char) - ord('A') for char in key]
        for i, char in enumerate(text):
            if char.isalpha():
                text_index = ord(char) - ord('A')
                key_index = key_indices[i % key_length]
                if encrypt:
                    result.append(chr((text_index + key_index) % 26 + ord('A')))
                else:
                    result.append(chr((text_index - key_index) % 26 + ord('A')))
        return "RESULT " + "".join(result)

    def main(self):
        ciph = Vcipher()

        while True:
            # Read input from stdin
            line = input().strip().upper()

            if line == "QUIT":
                break

            command, *args = line.split(" ", 1)
            if command == "PASS":
                ciph.passkey(args[0])
                print(" Passkey set")
            elif command == "ENCRYPT":
                print(ciph.vEncrypt(args[0]))
            elif command == "DECRYPT":
                print(ciph.vDecrypt(args[0]))
            else:
                print("error")

    if __name__ == "__main__":
        main()





