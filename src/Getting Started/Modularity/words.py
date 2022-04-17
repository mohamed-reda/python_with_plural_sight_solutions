from urllib.request import urlopen

story = urlopen("http://sixty-north.com/c/t.txt")
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()
print(str(story_words))
print(' '.join(story_words))

print(f'2 ** 3 = {2 ** 3} = 8')
print(f'{64 ** (1 / 4)}')
# __Feature__ is called dunder Feature
# so dunder is = double underscore
