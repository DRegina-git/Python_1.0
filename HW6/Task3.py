# Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, 
# начинающиеся с соответствующей буквы.

def employee_names(*names):
    vocab_names = {}
    for i in sorted(names):
        first_letter = i[0]
        if first_letter not in vocab_names:
            vocab_names[first_letter] = [i]
        vocab_names[first_letter] += [i]
        
    return vocab_names

print(employee_names('Иван', 'Мария', 'Петр', 'Илья', 'Марина', 'Петр', 'Алина', 'Бибочка'))