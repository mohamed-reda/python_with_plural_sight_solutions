core = [
    6,
    6,
    7,
    6,
    11,
    12,
    6,
    8,
    3,
    5,
    5,
]

advanced = [

    9,
    9,
    5,
    13,
    4,
    5,
]

for_analysis = [
    5,
    5,
    5,
    6,
    7,
    4,
    5,
    5,
    6,
    6,
    4,

]

Interpreting = [

    4,
    4,
    5,
]

Web_Scraping = [
    4,
    6,
    9,
    5,
    5,
    5,

]


def sum_of_list(l):
    counter = 0
    for i in l:
        counter += i
    return counter


count = sum(core) + sum(advanced) + sum(for_analysis) + sum(Interpreting) + sum(Web_Scraping)
print(sum(core))
print(sum(advanced))
print(count)
