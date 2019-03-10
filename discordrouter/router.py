from functools import wraps
from chatbottokenizer import Tokenizer


def message(router: 'Router', template: str):
    def decorator(func):
        router.add(template, func)

        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            await func(self, *args, **kwargs)

        return wrapper

    return decorator


def guide(router: 'Router'):
    def decorator(func):
        router.set_guide(func)

        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            await func(self, *args, **kwargs)

        return wrapper

    return decorator


class Router:
    commands = []
    guide = None

    def __init__(self, name: str):
        self.name = name

    def add(self, template, func):
        self.commands.append((template, func))

    def set_guide(self, func):
        self.guide = func

    async def __call__(self, _self, message: 'discord.Message'):
        tokens = Tokenizer(self.name, message.content)

        if not tokens.to_bot():
            return

        for (tmpl, func) in self.commands:
            if tokens.match(tmpl):
                await func(
                    _self,
                    items=tokens.items(),
                    message=message,
                    send=message.channel.send)
                return
        if self.guide != None:
            await self.guide(_self, message=message, send=message.channel.send)
