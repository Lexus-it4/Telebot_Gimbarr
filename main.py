from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from selenium import webdriver
from db import Database
import functions as fc
from time import sleep
import markups as nav
from text import *
import datetime
import logging
import time


driver = webdriver.Chrome()

TOKEN = "5618985345:AAHN7eCg2qFwFmwTa3ezj_0s5OPdF_OuawE"
YOOTOKEN = "381764678:TEST:46092"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')


def days_to_seconds(days):
    """Перевод дней в секунды для подписки"""
    return days * 24 * 60 * 60


def time_sub_day(get_time):
    """Высчитать оставшееся врямя подписки"""
    time_now = int(time.time())
    middle_time = int(get_time) - time_now

    if middle_time <= 0:
        return False
    else:
        dt = str(datetime.timedelta(seconds=middle_time))
        dt = dt.replace("days", "дней")
        dt = dt.replace("day", "день")
        return dt


def is_number(_str):
    """Проверка на число"""
    try:
        int(_str)
        return True
    except ValueError:
        return False


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Старт бота, проверка регистрации в БД"""
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваш ник!")
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегестрированны", reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    """Функционал кнопок"""
    if message.chat.type == 'private':
        if message.text == "Профиль":
            user_nickname = "<b>Ваш ник:</b> " + db.get_nickname(message.from_user.id)
            user_sub = time_sub_day(db.get_time_sub(message.from_user.id))
            if not user_sub:
                user_sub = "Нет"
            user_sub = "\n<b>Подписка:</b> " + user_sub
            await bot.send_message(message.from_user.id,
                                   user_nickname + "\n<b>Пользователь:</b> " + message.from_user.full_name +
                                   user_sub + sub_text_memory, parse_mode='html')

        elif message.text == "Подписка":
            await bot.send_message(message.from_user.id, sub_text, reply_markup=nav.sub_inline_markup)

        elif message.text == "Функции":
            await bot.send_message(message.from_user.id, "<b>Вы перешли в меню функций бота</b>",
                                   parse_mode='html', reply_markup=nav.functions_button)
            await bot.send_message(message.from_user.id, StartText)

        elif message.text == "Назад":
            await bot.send_message(message.from_user.id, "<b>Вы вернулись в основное меню бота</b>",
                                   parse_mode='html', reply_markup=nav.mainMenu)

        elif message.text == "Официальный сайт":
            await bot.send_message(message.from_user.id,
                                   '<a href="https://gimbarrofficial.com/">Официальный сайт Gimbarr Official</a>',
                                   parse_mode="HTML",
                                   reply_markup=nav.go_site)

        elif message.text == "Основная информация":
            await bot.send_message(message.from_user.id, "<b>Вы перешли в раздел основной информации</b>",
                                   parse_mode='html', reply_markup=nav.mainInfo)

        elif message.text == "Поддержать":
            await bot.send_message(message.from_user.id, support_channel_text, reply_markup=nav.support)

        elif message.text == "Назадㅤ":
            await bot.send_message(message.from_user.id, "<b>Вы вернулись в меню функций бота</b>",
                                   parse_mode='html', reply_markup=nav.functions_button)

        elif message.text == 'Категории элементов':
            await bot.send_photo(message.chat.id, r'https://i.ytimg.com/vi/dCvindw-Hkg/maxresdefault.jpg',
                                 caption='Любая дисциплина имеет деление.\nСуществующие категории в Джимбарре:',
                                 reply_markup=nav.categories)

        elif message.text == 'Для новичков':
            if db.get_sub_status(message.from_user.id):
                await bot.send_photo(message.chat.id,
                                     r'https://sun9-81.userapi.com/impf/f5CimqduPQ'
                                     r'peByipP2o36Qf7ZSaw_JQqxy_vGg/WoGQOK7AetI.jpg'
                                     r'?size=586x293&quality=96&sign=25e3cecf01e3f5159e2261586a263080&type=album',
                                     green_text, reply_markup=nav.green_vip)

            else:
                await bot.send_photo(message.chat.id,
                                     r'https://sun9-81.userapi.com/impf/f5CimqduPQ'
                                     r'peByipP2o36Qf7ZSaw_JQqxy_vGg/WoGQOK7AetI.jpg'
                                     r'?size=586x293&quality=96&sign=25e3cecf01e3f5159e2261586a263080&type=album',
                                     green_text, reply_markup=nav.green)

        elif message.text == "Показать элемент":
            if db.get_sub_status(message.from_user.id):
                await bot.send_message(message.from_user.id, "Введите название элемента:",
                                       reply_markup=types.ReplyKeyboardRemove())
                db.set_pars(message.from_user.id, "process")
            else:
                await bot.send_message(message.from_user.id, "\U000026A0Данная функция доступна при подписке\U000026A0"
                                                             "\nЖелаете приобрести?",
                                       reply_markup=nav.sub_inline_markup)

        elif message.text == 'История дисциплины':
            await bot.send_photo(message.chat.id, r'https://cdn.fishki.net/upload/post/201505/04/1521947'
                                                  r'/068a9802968466165f53798588ef5ca0.jpg',
                                 caption=history_text, reply_markup=nav.history_markup)

        elif message.text == 'Музыка':
            await bot.send_message(message.from_user.id, "<b>Вы перешли в раздел музыки</b>",
                                   parse_mode='html', reply_markup=nav.music_markup)

        elif message.text == 'ㅤНазад':
            await bot.send_message(message.from_user.id, "<b>Вы вернулись в раздел основной информации</b>",
                                   parse_mode='html', reply_markup=nav.mainInfo)

        elif message.text == "Поиск (Шазам)":
            await bot.send_message(message.chat.id, music_pars_text, reply_markup=nav.go_music)

        elif message.text == "Музыка с отчётов":
            await bot.send_message(message.chat.id, music_playlist_text, reply_markup=nav.go_music_list)

        else:
            if db.get_signup(message.from_user.id) == "setnickname":
                if len(message.text) > 15:
                    await bot.send_message(message.from_user.id, "Никнейм не должен превышать 15 символов")
                elif "@" in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрещённый символ")
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, "done")
                    await bot.send_message(message.chat.id, "Регистрация прошла успешно!", reply_markup=nav.mainMenu)
            else:
                if db.get_pars(message.from_user.id) == "process":
                    video = "https://www.youtube.com/results?search_query=" + message.text + " gimbarr"
                    driver.get(video)
                    sleep(2)
                    videos = driver.find_elements("id", "video-title")
                    number_of_videos = 0
                    await bot.send_photo(message.chat.id,
                                         r'https://vsrap.ru/wp-content/uploads/2019/11/artificialintelligence.jpg',
                                         caption="Вот, что мне удалось найти:")
                    for i in range(len(videos)):
                        if not (("минут" or "минута" or "часа" or "часов") in videos[i].get_attribute('aria-label')):
                            await bot.send_message(message.chat.id, "Видео №" + str(number_of_videos + 1) + ":\n"
                                                   + videos[i].get_attribute('href'), reply_markup=nav.functions_button)
                            number_of_videos += 1
                            if number_of_videos == 3:
                                break
                    if number_of_videos == 0:
                        await bot.send_message(message.from_user.id, zero_pars)
                    db.set_pars(message.from_user.id, "nopars")
                elif fc.recognize_question(message.text, db.get_questions()) > 0:
                    answer_id = fc.recognize_question(message.text, db.get_questions())
                    await bot.send_message(message.from_user.id, db.get_answer(answer_id))
                else:
                    await bot.send_message(message.chat.id, '<b>Я тебя не понимаю.</b>', parse_mode='html')


@dp.callback_query_handler(text="subweek")
async def subday(call: types.CallbackQuery):
    """Обработчик для подписки на неделю"""
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки",
                           description=sub_text, payload="week_sub", provider_token=YOOTOKEN,
                           currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб", "amount": 10000}])


@dp.callback_query_handler(text="submonth")
async def submonth(call: types.CallbackQuery):
    """Обработчик для подписки на месяц"""
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки",
                           description=sub_text, payload="month_sub", provider_token=YOOTOKEN,
                           currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб", "amount": 25000}])


@dp.callback_query_handler(text="subyear")
async def subyear(call: types.CallbackQuery):
    """Обработчик для подписки на год"""
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки",
                           description=sub_text, payload="year_sub", provider_token=YOOTOKEN,
                           currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб", "amount": 49900}])


@dp.callback_query_handler(text="support_channel")
async def support(call: types.CallbackQuery):
    """Обработчик для доната"""
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки",
                           description=support_channel_text, payload="support_channel", provider_token=YOOTOKEN,
                           currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб", "amount": 10000}])


# Подтверждение наличия товара
@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    """Обработчик подтверждающий наличие товара"""
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


# Обработчик после оплаты
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    """Обработчик, выдающий подписку"""

    if message.successful_payment.invoice_payload == "week_sub":
        if db.get_time_sub(message.from_user.id) >= int(time.time()):
            time_sub = db.get_time_sub(message.from_user.id) + days_to_seconds(7)
        else:
            time_sub = int(time.time()) + days_to_seconds(7)
        db.set_time_sub(message.from_user.id, time_sub)
        await bot.send_message(message.from_user.id, "Вам выдана подписка на неделю!!!")

    elif message.successful_payment.invoice_payload == "month_sub":
        if db.get_time_sub(message.from_user.id) >= int(time.time()):
            time_sub = db.get_time_sub(message.from_user.id) + days_to_seconds(30)
        else:
            time_sub = int(time.time()) + days_to_seconds(30)
        db.set_time_sub(message.from_user.id, time_sub)
        await bot.send_message(message.from_user.id, "Вам выдана подписка на месяц!!!")

    elif message.successful_payment.invoice_payload == "year_sub":
        if db.get_time_sub(message.from_user.id) >= int(time.time()):
            time_sub = db.get_time_sub(message.from_user.id) + days_to_seconds(365)
        else:
            time_sub = int(time.time()) + days_to_seconds(365)
        db.set_time_sub(message.from_user.id, time_sub)
        await bot.send_message(message.from_user.id, "Вам выдана подписка на год!!!")

    elif message.successful_payment.invoice_payload == "support_channel":
        await bot.send_message(message.from_user.id, "Благодарим вас за поддержку!!!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
