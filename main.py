import random


LETTER_SCORES ={
    "А": 1, "Б": 3, "В": 1, "Г": 3, "Д": 2, "Е": 1, "Ё": 1, "Ж": 5, "З": 5, "И": 1,
    "Й": 4, "К": 2, "Л": 2, "М": 2, "Н": 1, "О": 1, "П": 2, "Р": 1, "С": 1, "Т": 1,
    "У": 2, "Ф": 10, "Х": 5, "Ц": 5, "Ч": 5, "Ш": 8, "Щ": 10, "Ъ": 10, "Ы": 4, "Ь": 3,
    "Э": 8, "Ю": 8, "Я": 3
}


def get_random_letter():
    keys = LETTER_SCORES.keys()
    converted_dictionary = list(keys)
    random_letter = random.choice(converted_dictionary)
    return random_letter


def get_word_with_letter(random_letter):
    word = input(f"введите слово на букву '{random_letter}':")
    while word[0].upper() != random_letter:
        print(f"Слово должно начинаться на '{random_letter}'. Попробуйте снова")
        word = input(f"введите слово на букву '{random_letter}':")
    return word


def calculate_score(word):
    all_scores = []
    for letter in word:
        big_letter = letter.upper()
        score = LETTER_SCORES.get(big_letter)
        all_scores.append(score)
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    random_letter = get_random_letter()
    print(f"Начальная буква:{random_letter}")
    print("Игрок 1")
    word1 = get_word_with_letter(random_letter)
    print("Игрок 2")
    word2 = get_word_with_letter(random_letter)
    sum_scores1 = calculate_score(word1)
    sum_scores2 = calculate_score(word2)
    print(f"Игрок 1 ввел слово '{word1}' и набрал {sum_scores1} очков.")
    print(f"Игрок 2 ввел слово '{word2}' и набрал {sum_scores2} очков.")
    if sum_scores1 > sum_scores2:
        print("Игрок 1 победил!")
    elif sum_scores1 == sum_scores2:
        print("Выиграла ничья!")
    else:
        print("Игрок 2 победил!")


if __name__ == '__main__':
    main()
