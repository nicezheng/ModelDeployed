import os


def clear():
    return None, None


# example database
def get_image_examples():
    image_examples = []
    path = os.path.join(os.path.dirname(__file__), "images")
    examples_num = 0
    for file in os.listdir(path):
        if file.endswith(".jpg") or file.endswith(".png"):
            image_examples.append([os.path.join(path, file), examples_num])
            examples_num += 1
    return image_examples


if __name__ == '__main__':
    image_examples = get_image_examples()
    print(image_examples)
