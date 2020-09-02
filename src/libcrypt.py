class LibCrypt(object):
    def __init__(self, codes):
        self._encryption_codes = {_: str(num) for _, num in codes.items()}

    @property
    def _decryption_codes(self):
        return {num: vowel for vowel, num in self._encryption_codes.items()}

    @staticmethod
    def _contains_digit(content):
        return any(map(str.isdigit, content))

    def _encode(self, content):
        # TODO:
        # Sting to Number mapping
        pass

    def _decode(self, content):
        # TODO:
        # Number to String Mapping
        pass

    def transform(self, content):
        if self._contains_digit(content):
            return self._decode(content)

        return self._encode(content)


def main():
    codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

    content = 'th3s 3s 1 m2ss1g2.'
    print(LibCrypt(codes=codes).transform(content))

    content = 'another message here!'
    print(LibCrypt(codes=codes).transform(content))


if __name__ == '__main__':
    main()
