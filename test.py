import asyncio

# 假設my_async_function包含複雜的非阻塞操作，例如網絡通信
async def fetch_data(url, n=1):
    print(f"start {url}")
    await asyncio.sleep(n)  # 模擬網絡請求的耗時
    print(f"over {url} ")

# 使用異步函式
async def main():
    print("Start main")

    # 使用 asyncio.gather() 同時處理多個非阻塞任務
    tasks = [
        fetch_data("A",10),
        fetch_data("B",2),
        fetch_data("C"),
    ]
    await asyncio.gather(*tasks)

    print("over main")

# 建立事件循環並執行主函式
asyncio.run(main())