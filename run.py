import asyncio
import os
import bot

# Telegram tokenini environment içine yazıyoruz
os.environ["TOKEN"] = "BURAYA_TOKENI_YAZ"

async def main():
    await bot.main()

if __name__ == "__main__":
    asyncio.run(main())
