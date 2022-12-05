from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# TODO конпки основного меню
btnProfile = KeyboardButton('Профиль')
btnSub = KeyboardButton('Подписка')
btnList = KeyboardButton('Функции')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile, btnSub, btnList)

# TODO конпки для оплаты подписки
sub_inline_markup = InlineKeyboardMarkup(row_width=1)
btnSubWeek = InlineKeyboardButton(text="Неделя - 100 рублей", callback_data="subweek")
btnSubMonth = InlineKeyboardButton(text="Месяц - 250 рублей", callback_data="submonth")
btnSubMonthYear = InlineKeyboardButton(text="Год - 499 рублей", callback_data="subyear")
sub_inline_markup.add(btnSubWeek, btnSubMonth, btnSubMonthYear)

# TODO конпки меню функций
functions_button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
official_site = KeyboardButton('Официальный сайт')
main_info = KeyboardButton('Основная информация')
show_element_vip = KeyboardButton('Показать элемент')
show_element = KeyboardButton('Показать элемент')
back_main = KeyboardButton('Назад')
help_us = KeyboardButton('Поддержать', callback_data="support_channel")
functions_button.add(official_site, main_info, show_element, back_main, help_us)

# TODO конпка для перехода на официальный сайт
go_site = InlineKeyboardMarkup(row_width=1)
site = InlineKeyboardButton("Перейти на официальный сайт", url="https://gimbarrofficial.com/")
go_site.add(site)

# TODO конпки меню основной информации
kategorii = KeyboardButton('Категории элементов')
for_green = KeyboardButton('Для новичков')
history = KeyboardButton('История дисциплины')
music = KeyboardButton('Музыка')
back = KeyboardButton('Назадㅤ')
mainInfo = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
mainInfo.add(kategorii, for_green, history, music, back)

# TODO конпка для поддержки канала
support = InlineKeyboardMarkup(row_width=1)
btnsupport = InlineKeyboardButton(text="Пожертвовать - 100 рублей", callback_data="support_channel")
support.add(btnsupport)

# TODO конпки ссылок на категории элементов
categories = InlineKeyboardMarkup(row_width=1)
cat_yoyo = InlineKeyboardButton("Категория yoyos", url="https://www.youtube.com/watch?v=Qh_bCvH4IOc&t=29s")
cat_figure = InlineKeyboardButton("Категория figuras", url="https://www.youtube.com/watch?v=psQlw5wzLi4&t=3s")
cat_giro = InlineKeyboardButton("Категори giros", url="https://www.youtube.com/watch?v=WiRw4q09vL4")
categories.add(cat_yoyo, cat_figure, cat_giro)

# TODO конпки ссылки для новичков
green = InlineKeyboardMarkup(row_width=1)
green_vip = InlineKeyboardMarkup(row_width=1)
green_50 = InlineKeyboardButton("Топ 50 элементов для новичка",
                                url="https://yandex.ru/video/touch/preview/7662644382562477463")
green_begin = InlineKeyboardButton("С чего начать Gimbarr",
                                   url="https://yandex.ru/video/touch/preview/13188479677315431601")
green_chat = InlineKeyboardButton("Доступно при подписке", callback_data="subweek")
green_chat_vip = InlineKeyboardButton("Беседа для обучения", url="https://vk.me/join/AJQ1dzY4IyJjTFSz5msCllng")
green.add(green_50, green_begin, green_chat)
green_vip.add(green_50, green_begin, green_chat_vip)

# TODO конпки в раздел история дисциплины
history_markup = InlineKeyboardMarkup(row_width=1)
history_first_video = InlineKeyboardButton("Самое первое Джимбарр видео", url="https://youtu.be/MPiTzbwJAWg")
history_sport = InlineKeyboardButton("Как появился Gimbarr", url="https://youtu.be/kkaYYTa3DRc")
history_wiki = InlineKeyboardButton("Wikipedia", url="https://ru.wikipedia.org/wiki/%D0%94%D0%B6%D0%B8%D0%BC%D0%B1%D0"
                                                     "%B0%D1%80%D1%80")
history_markup.add(history_first_video, history_sport, history_wiki)

# TODO конпки меню музыка
music_report = KeyboardButton('Музыка с отчётов')
music_shazam = KeyboardButton('Поиск (Шазам)')
back_main_info = KeyboardButton('ㅤНазад')
music_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
music_markup.add(music_report, music_shazam, back_main_info)

# TODO конпка для перехода к Шазаму музыки
go_music = InlineKeyboardMarkup(row_width=1)
music_list = InlineKeyboardButton("Распознать трек", url="https://t.me/YaMelodyBot")
go_music.add(music_list)

# TODO конпка для перехода плэйлисту
go_music_list = InlineKeyboardMarkup(row_width=1)
music_playlist = InlineKeyboardButton("Музыка с отчётов",
                                      url="https://music.yandex.ru/users/alex181103@mail.ru/playlists/1000")
go_music_list.add(music_playlist)

