import os

BASE_DIR = os.path.dirname(__file__)


class SignalReceiver:
    def response_part_1(self) -> int:
        """Response to part 1"""

        return self.check_marker(4)  # 1042

    def response_part_2(self) -> int:
        """Response to part 2"""

        return self.check_marker(14)  # 2980

    def check_marker(self, len_of_string: int) -> int:
        """Get index of last character inside a unique string of lenght n"""

        with open(os.path.join(BASE_DIR, "day_6_input.txt"), "r") as input:
            signal = list(input.read())

        counter = len_of_string

        for character in range(len(signal)):
            packet = signal[character : character + len_of_string]

            # Check if packet has different character
            if len(packet) == len(list(set(packet))):
                break
            else:
                counter += 1

        return counter


if __name__ == "__main__":
    print(SignalReceiver().response_part_1())
    print(SignalReceiver().response_part_2())
