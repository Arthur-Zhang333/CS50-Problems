from cs50 import get_string

def main():
    p = get_string("Text: ")
    word = count_word(p)
    letter = count_letter(p)
    sentence = count_sentence(p)
    L = 100 * (letter / word)
    S = 100 * (sentence / word)
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = int(index)

    if grade < 1:
        print("Before Grade 1")

    elif grade >= 16:
        print("Grade 16+")

    else:
        print(f"Grade {grade}")


def count_letter(x):
    letter = 0
    for i in range(len(x)):
        if x[i].isalpha():
            letter += 1
    return letter

def count_word(y):
    word = 0
    for i in y:
        if i == ' ':
            word += 1
    return word + 1

def count_sentence(z):
    sentence = 0
    for i in range(len(z)):
        if z[i] == '.' or z[i] == '!' or z[i] =='?':
            sentence += 1
    return sentence

main()
