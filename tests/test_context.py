from dataclasses import dataclass

from easy_kit.context import Context
from easy_kit.timing import TimingTestCase


@dataclass
class MyData:
    x: float = 0
    y: float = 1


@dataclass
class SubclassData(MyData):
    z: float = 2


class TestContext(TimingTestCase):
    def test_simple(self):
        ctx = Context()
        xxx = MyData()
        ctx.register(xxx)
        self.assertEqual(xxx, ctx.find(MyData))

    def test_subclass(self):
        ctx = Context()
        xxx = SubclassData()
        ctx.register(xxx)
        self.assertEqual(xxx, ctx.find(SubclassData))

        with self.assertRaises(KeyError):
            ctx.find(MyData)

        ctx.register(xxx, ctype=MyData)
        self.assertEqual(xxx, ctx.find(MyData))

    def test_wrong_subclass(self):
        ctx = Context()
        with self.assertRaises(ValueError):
            ctx.register('wrong class', ctype=MyData)
        with self.assertRaises(KeyError):
            ctx.find(MyData)
