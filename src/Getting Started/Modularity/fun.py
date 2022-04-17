from urllib.request import urlopen
import sys


def fetch_words(url):
    """this is Docstring"""

    # story = urlopen("http://sixty-north.com/c/t.txt")
    """to send the url with the script, use this command:"""
    #  python fun.py http://sixty-north.com/c/t.txt
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()

    return story_words


# if __name__ == '__main__':
# print(fetch_words())

# string = 'hello'
# string = 20
# print(type(string))
# print(help(fetch_words()))
help(fetch_words)
# from fun import fetch_words

print(__name__)
""" if __name__ = __main__, so you are running the function from here, 
not from any import"""
"""the module is only executed once with first import"""


def print_items(word_list):
    for word in word_list:
        print(word)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    print('this')
    main(sys.argv[1])
