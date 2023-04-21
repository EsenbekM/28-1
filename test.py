from time import sleep
import asyncio


async def download_photo(photo_count, limit):
    while photo_count < limit:
        await asyncio.sleep(1)
        photo_count += 1
        print(f"Photo {photo_count}")


async def download_video(video_count, limit):
    while video_count < limit:
        await asyncio.sleep(5)
        video_count += 1
        print(f"video {video_count}")


async def main():
    photo_count = 0
    video_count = 0
    task_list = [download_photo(photo_count, 30), download_video(video_count, 10)]
    await asyncio.gather(*task_list)


asyncio.run(main())
