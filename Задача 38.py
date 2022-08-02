text = 'Привет абвдр друг, рада приабв приветствовать тебя в нашей программе'
def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_words(text)
print(text)