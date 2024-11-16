from setuptools import setup, find_packages

setup(
    name="roblox_version",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "asyncio",
        "httpx"
    ],
)
