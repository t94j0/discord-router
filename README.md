# Discord Router

A simple router decorator for [discord.py](https://github.com/Rapptz/discord.py) chat bots.

## Installation

`pip3 install discordrouter`

## Usage

```py
from discordrouter import Router, message

class ChatBot(discord.Client):
  router = Router('!test')

  async def on_ready(self):
    print(f'Logged in as {self.user.name}')
  
  async on_message(self, message):
    await self.router(message)

  @message(router, "new <name>")
  async _test1(self, items, message):
    name = items['name']
    await message.channel.send('{name}')
```
