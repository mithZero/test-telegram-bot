from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = InlineKeyboardBuilder()
main.add(
	InlineKeyboardButton(text="Адрес", url="https://yandex.ru/maps/10747/podolsk/house/ulitsa_lenina_1/Z04YcwViQUYBQFtvfX93cnllYQ==/?ll=37.522836%2C55.363565&z=16.58"),	
	InlineKeyboardButton(text="Оплатить 2р", url="https://ya.ru"),
	InlineKeyboardButton(text="Картика", callback_data="image"),
)
main.adjust(2, 1, 1)

main.row(
	InlineKeyboardButton(text="Google Sheets", callback_data="google"))

