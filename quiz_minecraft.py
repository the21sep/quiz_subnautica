print('Добро пожаловать на викторину по игре Minecraft!')
print('Ответь на следущие вопросы:')
questions= [
'1. самый частый моб ночью?',
'2. Какой самый сильный моб в игре?',
'3. Какой самый бесячий моб при добыче алмазов?',
'4. Какой самый большой моб в аду?',
'5. Название основных мобов в эндер мире?',
'6. Что требуется чтобы закончить игру?',
'7. Как зовут главного героя мужского пола?',
'7.Как зовут главного героя женского пола?'
]
variants = [
    ['скелет','зомби','крипер','корова'],
    ['акула','эндер дракон','визер','гаст'],
    ['крипер','скелет','эндермен','слизень'],
    ['королевский пиглин','императорский гаст','королевский магма-куб','гаст'],
    ['скелет','зомби','эндермен','пилогриф'],
    ['а) уничтожить эндер мир','б) убить всех эндерменов','в) убить визера','г) убить эндер дракона'],
    ['Геннадий', 'Карл', 'Тима', 'Стив'],
    ['Алекс','Даша','Аликс','Таля']
]
answers = [
'Зомби',
'Визер',
'Крипер',
'Гаст',
'Эндермен',
'г',
'Стив',
'Алекс'
]
score = 0
print(questions[0])
print(variants[0])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[0].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")
print(questions[1])
print(variants[1])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[1].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[2])
print(variants[2])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[2].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[3])
print(variants[3])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[3].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[4])
print(variants[4])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[4].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[5])
print(variants[5])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[5].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно.")

print(questions[6])
print(variants[6])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[6].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно")

print(questions[7])
print(variants[7])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[7].lower():
    print("Правильно!")
    score = score + 1
else:
    print("Неправильно")

if score>5:
    print("Это отличный результат! Ты про в майнкрафте.")
elif score>3:
    print("Неплохой результат! Ты многое знаешь но не всё о этой игре.")
else:
    print("Видимо ты новичёк, тебе ещё многое предстоит узнать об этой игре!.")