from core.bot import app

import sys
import asyncio
import threading

if __name__ == '__main__':

    if sys.argv[0]:
        try:
            print("Run build telegram bot")
            asyncio.run(app())
        except Exception as e:
            print(e)
