import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    await asyncio.sleep(1)

async def main2():
    print('Hello!!! ...')
    await asyncio.sleep(3)
    print('... !!!!World!')
    await asyncio.sleep(3)

# Python 3.7+
while True:
    asyncio.run(main())
    asyncio.run(main2())