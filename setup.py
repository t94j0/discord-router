import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discordrouter",
    version="0.0.4",
    author="Max Harley",
    author_email="maxh@maxh.io",
    description="Decorator for discord.py chat bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/t94j0/discord-router",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
