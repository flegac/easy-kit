from typing import Type

from easy_kit.context import Context


class ContextService:
    def __init__(self, ctx: Context):
        self.ctx = ctx

    def find[T](self, ctype: Type[T]):
        return self.ctx.find(ctype)
