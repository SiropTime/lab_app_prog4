from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from internal.utils import TOKEN, logger

bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    print("""
          Maltsev Timofey. IDB-21-10. Lab 4
          """)
    logger.info("Setting up everything...")

    from internal.telegram import dp  # Importing dispatcher with handlers
    executor.start_polling(dp, skip_updates=True)
