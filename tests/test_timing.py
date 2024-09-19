import time
from pprint import pprint

from easy_kit.timing import TimingTestCase, timing, _TIMING


class TestTiming(TimingTestCase):
    def test_timing(self):
        with timing('test1'):
            time.sleep(.3)

        for i in range(10):
            with timing('test2'):
                time.sleep(.02)

    def test_lots_of_events(self):
        x = 3
        y = 1

        for _ in range(1_000_000):
            with timing('xxx'):
                x += 2

            if _ % 3 == 0:
                with timing('yyy'):
                    y += 4


    def test_structure(self):
        with timing('aaa.test1'):
            time.sleep(.3)
        with timing('aaa.test2'):
            time.sleep(.02)
        with timing('xxx.yyy'):
            time.sleep(.01)
        with timing('xxx.test2'):
            time.sleep(.01)
        pprint(_TIMING.tree_structure())
