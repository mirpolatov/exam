from aiogram import Bot, Dispatcher, types, executor

BOT_TOKEN = ("6094306251:AAGe4_OC7E-ZC7dcMthDdfg7GkehD7UpxkQ")
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start_handler(msg: types.Message):
    await msg.answer('HEllo')


@dp.message_handler()
async def share(msg: types.Message):
    v = msg.text
    vol = 'AOUIEaioue'
    c = 0
    for i in v:
        if i in vol:
            c += 1
    if c >= 5:
        await msg.delete()
        await msg.answer('HAbar o''chirildi')
    else:
        await msg.answer('UNLI hariflar 5 tadan kam')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
