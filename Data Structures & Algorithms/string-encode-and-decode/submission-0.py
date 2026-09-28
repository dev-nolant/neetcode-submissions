class Solution:

    def encode(self, strs: List[str]) -> str:

        # list_string = list(":".join(strs)) # delim :
        # hex_values = [ord(i) for i in list_string]
        # encoded_string = [i * j for i, j in zip(hex_values, cycle(key))]
        # return ":".join(map(str, encoded_string))

        encoded_string = ""

        for i in strs:
            encoded_string += str(len(i)) + "#" + i # 11#Hello World

        return encoded_string

    def decode(self, s: str) -> List[str]:
        # split_list = s.split(":")
        # hex_values = [int(i) // j for i, j in zip(split_list, cycle(key))]

        # decoded_string_list = [chr(i) for i in hex_values]

        # return "".join(decoded_string_list).split(":")

        decoded_list = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            decoded_list.append(s[start:end])

            i = end
        return decoded_list
