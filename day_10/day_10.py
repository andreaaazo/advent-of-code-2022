import os


BASE_DIR = os.path.dirname(__file__)

def response_part_1():
    with open(f'{BASE_DIR}/input.txt', "r") as inp:
        signals = [line.split(" ") for line in inp.read().splitlines()]
        inp.close()

    X = 1
    cycles_counter = 0
    cycles_value  = 0

    for signal in signals:
        if len(signal) == 1:  # is noop
            cycles_counter += 1
            if cycles_counter in [20, 60, 100, 140, 180, 220]:
                cycles_value += cycles_counter * X
        else:  # is addx
            cycles_counter += 1
            if cycles_counter in [20, 60, 100, 140, 180, 220]:
                cycles_value += cycles_counter * X

            cycles_counter += 1
            if cycles_counter in [20, 60, 100, 140, 180, 220]:
                cycles_value += cycles_counter * X

            X += int(signal[1])

    return cycles_value


if __name__ == "__main__":
    print(response_part_1())
    print(f'{BASE_DIR}/input.txt')
