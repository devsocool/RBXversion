# AI Generated Example

import asyncio
from roblox_version import Version

async def main():
    versions = await Version().get()
    print(versions)

asyncio.run(main())
