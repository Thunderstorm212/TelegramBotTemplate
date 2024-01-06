import logging
from aiogram import Bot, Dispatcher
from core.handlers import router
import conf


async def app():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(conf.BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    try:
        dp.include_router(router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as ex:
        print(ex)

