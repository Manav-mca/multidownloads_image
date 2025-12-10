import asyncio
import requests


async def function1():
    url = "https://wallpaperaccess.com/full/7493519.jpg"
    response = requests.get(url)
    open("instagram.ico", "wb").write(response.content)
    print("func1")

async def function2():
    url = "https://th.bing.com/th/id/OIP.4ByRfg5HIhmKjulLUHL49wHaEK?w=312&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1"
    response = requests.get(url)
    open("instagram2.ico", "wb").write(response.content)
    print("func2")

async def function3():
    url = "https://th.bing.com/th/id/OIP.82JnmhXiohFy98IRKa-GTAHaEK?w=312&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1"
    response = requests.get(url)
    open("instagram3.ico", "wb").write(response.content)
    print("func3")

async def main():
    
    await function1()
    await function2()
    await function3()

asyncio.run(main())
