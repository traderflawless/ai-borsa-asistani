import asyncio
import os
import bot

# Telegram tokenini environment içine yazıyoruz
os.environ["TOKEN"] = "8023463275:AAEvNrbcVzz1sG1sacHKYp4YWLQLI1iVNJw"

async def main():
    await bot.main()

if __name__ == "__main__":
    asyncio.run(main())
