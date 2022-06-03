
from random import choice



def get_jokes(*args):
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', ' позавчера', 'ночью']
    adjectives = ['весёлый', 'яркий', 'зелёный', 'утопичный', 'мягкий']


    return choice(nouns), choice(adverbs), choice(adjectives)


print(*get_jokes())