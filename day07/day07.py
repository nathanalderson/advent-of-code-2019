def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]


def get_pixel(x, y, image, width):
    pos = (y * width) + x
    stack = [layer[pos] for layer in image]
    color = next(x for x in stack if x != 2)
    return "█" if color == 1 else " "


def image_str(image, height, width):
    for y in range(height):
        for x in range(width):
            yield get_pixel(x, y, image, width)
        yield "\n"


def main():
    with open("input") as f:
        data = f.read().strip()
    image = [int(d) for d in data]
    width = 25
    height = 6
    layer_size = width * height
    layers = list(chunks(image, layer_size))
    fewest_zeros = min(layers, key=lambda l: l.count(0))
    print(fewest_zeros.count(1) * fewest_zeros.count(2))
    print()
    print("".join(image_str(layers, height, width)))


if __name__ == "__main__":
    main()
