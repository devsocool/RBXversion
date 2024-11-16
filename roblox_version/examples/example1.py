# AI Generated Example

import asyncio
from roblox_version import Version

async def main():
    versions = await Version().get()
    if versions:
        print("Roblox Versions:")
        print(f"Windows: {versions['Windows']}")
        print(f"Mac: {versions['Mac']}")
    else:
        print("Failed to fetch versions.")

if __name__ == "__main__":
    asyncio.run(main())
