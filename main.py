from aiogram import Bot, Dispatcher, executor, types
import kb
from aiogram.dispatcher.filters import Text
import days
import random as rd
from questions import que
from dare import dare

TOKEN_API = "5477294427:AAGa5aVGifbbU7pds4Uri-pJPrODnSe98NU"
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)
day_of_week = ''
timetable = {}
question = ''
dar = ''
num1 = ''
num2 = ''


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    name = dict(msg['from'])
    username = dict(msg['from'])
    await msg.answer("Привіт! Вибери один одне з запропонованих варіантів нижче", reply_markup=kb.chosen)
    await msg.delete()
    with open("logs.txt", mode='a') as file:
        file.write(f"\nName = {name['first_name']}, Username = {username['username']};")


@dp.message_handler(Text(equals='Розклад'))
async def table(msg: types.Message):
    await msg.answer("Вибери по якому тижнню", reply_markup=kb.week)
    un_table()


@dp.message_handler(Text(equals='Правда чи Дія'))
async def table(msg: types.Message):
    await msg.answer("Привіт! Вітаю в грі 'Правда чи Дія'! Виберай:", reply_markup=kb.game)
    game()


def un_table():
    @dp.message_handler(Text(equals='1 тиждень'))
    async def week1(msg: types.Message):
        global timetable
        timetable = days.week_1
        await msg.answer("Розклад по першому тижню, вибери день", reply_markup=kb.day)

    @dp.message_handler(Text(equals='2 тиждень'))
    async def week2(msg: types.Message):
        global timetable
        timetable = days.week_2
        await msg.answer("Розклад по другому тижню, вибери день", reply_markup=kb.day)
        day()

    def day():
        @dp.message_handler(Text(equals='Понеділок'))
        async def mon(msg: types.Message):
            global day_of_week
            day_of_week = msg
            await msg.answer(f"{timetable[day_of_week['text']]}", reply_markup=kb.chosen)

        @dp.message_handler(Text(equals='Вівторок'))
        async def tus(msg: types.Message):
            global day_of_week
            day_of_week = msg
            await msg.answer(f"{timetable[day_of_week['text']]}", reply_markup=kb.chosen)

        @dp.message_handler(Text(equals='Середа'))
        async def wen(msg: types.Message):
            global day_of_week
            day_of_week = msg
            await msg.answer(f"{timetable[day_of_week['text']]}", reply_markup=kb.chosen)

        @dp.message_handler(Text(equals='Четверг'))
        async def thur(msg: types.Message):
            global day_of_week
            day_of_week = msg
            await msg.answer(f"{timetable[day_of_week['text']]}", reply_markup=kb.chosen)

        @dp.message_handler(Text(equals="П'ятниця"))
        async def fri(msg: types.Message):
            global day_of_week
            day_of_week = msg
            await msg.answer(f"{timetable[day_of_week['text']]}", reply_markup=kb.chosen)


def game():
    def rand():
        global question, dar, num1, num2
        num1 = str(rd.randint(1, 250))
        question = que[num1]
        num2 = str(rd.randint(1, 79))
        dar = dare[num2]

    @dp.message_handler(Text(equals="Правда?"))
    async def ques(msg: types.Message):
        rand()
        await msg.answer(f'{question}', reply_markup=kb.game)
        with open("logs.txt", mode='a') as file:
            file.write(f"Name = {msg['from']['first_name']} Choice = {msg['text']} Number = {num1};\n")

    @dp.message_handler(Text(equals="Дія?"))
    async def ques(msg: types.Message):
        rand()
        await msg.answer(f'{dar}', reply_markup=kb.game)
        with open("logs.txt", mode='a') as file:
            file.write(f"Name = {msg['from']['first_name']} Choice = {msg['text']} Number = {num2};\n")

    @dp.message_handler(Text(equals='Меню'))
    async def ques(msg: types.Message):
        await msg.answer("Повертаю тебе в меню!", reply_markup=kb.chosen)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
