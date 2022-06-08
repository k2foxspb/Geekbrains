

def num_translate(num):
    nums = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if num in nums:
        return nums[num]
    else:
        return 'none'


fun=num_translate(input('введите число\n'))
print(fun)