from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

chosen = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
q1 = KeyboardButton("Розклад")
q2 = KeyboardButton("Контакти Викладачів")
q3 = KeyboardButton("Правда чи Дія")

chosen.row(q1, q2).add(q3)

day = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
mon = KeyboardButton("Понеділок")
tue = KeyboardButton("Вівторок")
wen = KeyboardButton("Середа")
thu = KeyboardButton("Четверг")
fri = KeyboardButton("П'ятниця")

day.row(mon, tue).row(wen, thu).add(fri)

week = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
w1 = KeyboardButton("1 тиждень")
w2 = KeyboardButton("2 тиждень")

week.row(w1, w2)

game = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

ch1 = KeyboardButton("Правда?")
ch2 = KeyboardButton("Дія?")
ch3 = KeyboardButton("Меню")

game.row(ch1, ch2).add(ch3)

