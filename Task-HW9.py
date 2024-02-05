"""
1. Даний текстовий файл. Необхідно створити новий файл,
 який потрібно переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.
"""
with open('input.txt', 'w') as file:
    file.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep")
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        words = line.split()
        filtered_words = [word for word in words if len(word) >= 7]
        output_file.write(' '.join(filtered_words) + '\n')

"""
Даний текстовий файл. Підрахувати кількість слів у ньому.
"""

with open('input.txt', 'r') as input_file:
    text = input_file.read()
    word_count = len(text.split())
    print(f"The number of words in the text: {word_count}")

"""
 Створіть програму, яка перевіряє текст на неприпустимі слова.

Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.

За підсумками роботи програми необхідно показати статистику дій.
"""
import re
def censor_text(text, forbidden_word):
    pattern = r'\b' + re.escape(forbidden_word) + r'\b'
    censored_text, count = re.subn(pattern, '*' * len(forbidden_word), text, flags=re.IGNORECASE)
    print(f"Inadmissible word: {forbidden_word}.")
    print(f"Result:\n{censored_text}")
    return censored_text, count

forbidden_word = 'die'
with open('input.txt', 'r') as input_file:
    original_text = input_file.read()
    censored_text, replacements = censor_text(original_text, forbidden_word)

    print(f"Statistics: {replacements} word substitution for {forbidden_word}.")


