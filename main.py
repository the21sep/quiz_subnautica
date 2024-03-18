print('Добро пожаловать на викторину по игре subnautica!')
print('Ответь на следущие вопросы:')
questions= [
'1. Какой самый быстрый транспорт в игре?',
'2. Какой самый большой транспорт в игре?',
'3. Название левиофана который обитает рядом с кораблём?',
'4. Какой самый большой левиофан в игре?',
'5. Какой самый маленький левиофан в игре?',
'6. Что требуется чтобы закончить игру?',
'7. Название космического корабля на котором упал главный герой игры?'
]
variants = [
    ['катер','мотылёк','орнитоптор','батискаф'],
    ['субмарина','подводная лодка','циклоп','краб'],
    ['акула','мегалодон','жнец','червь'],
    ['королевский пенгвин','спинозавр','ихтиозавр','морской император'],
    ['гуппи','рифоспин','пискун','иглобрюх'],
    ['а) съесть всех левиофанов','б) отремонтировать корабль и взорвать планету','в) Выключить пушку ПВО и улететь с планеты','г) Включить пушку ПВО и подать сигнал бедствия'],
    ['Аврора', 'Чёрная жемчужина', 'Посейдон', 'Заря']
]
answers = [
'Мотылёк',
'Циклоп',
'Жнец',
'Морской император',
'Рифоспин',
'в',
'Аврора'
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

if score>5:
    print("Это отличный результат! Ты профессионал в сабнатике.")
elif score>3:
    print("Неплохой результат! Ты многое знаешь но не всё о этой игре.")
else:
    print("Видимо ты новичёк, тебе ещё многое предстоит узнать об этой игре!.")