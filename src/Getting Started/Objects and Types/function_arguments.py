def adds(message=[]):
    print(message)
    message.append("list")

    print(message)


def add(message=None):
    if message is None:
        message = []
    message.append("list")

    print(message)


lunch = ["Hi"]
adds(lunch)
adds(lunch)
adds()
adds()  # this prints ['list', 'list']

# add()
# add()
