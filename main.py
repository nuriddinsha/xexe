from aiogram import Bot, Dispatcher, types
API_TOKEN = '6378852189:AAFrexfXF0w154Q1gCGnVUjiOzgF9btHiFg'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    name = message.from_user.first_name
    surname = message.from_user.last_name
    await message.answer(f"Здраствуйте {name} "
                         f"{surname}", reply_markup=keyboard)


@dp.message_handler(content_types=['contact'])
async def send_contact(message: types.Message):
    name = message.from_user.first_name
    phone_number = message.from_user.phone_number
    txt = f"{phone_number},{name}"
    await bot.send_message(message.chat.id, text = txt)



if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)