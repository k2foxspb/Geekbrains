tutors = ['Иван', 'Анастасия', 'Пётр', 'Сергей', 'Дмитрий', 'Борис', 'Антон']
klasses = ['9A', '7B', '9Б', '9В', '8Б',  ]


def gen_klass(t,k):
    i = 0
    while i < len(t) and i < len(k):
        yield t[i], k[i]
        i += 1
    while i < len(t):
        yield t[i], 'класс не указан'
        i += 1


for i in gen_klass(tutors,klasses):
    print(i)