from TikTokApi import TikTokApi
import asyncio
import os
from datetime import datetime

ms_token = os.environ.get("ms_token", None)  # get your own ms_token from your cookies on tiktok.com


async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        async for video in api.hashtag(name='Dota2').videos(count=300):
            print(video)
            ts = int(video.as_dict["createTime"])
            print(print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')))

if __name__ == "__main__":
    asyncio.run(trending_videos())
