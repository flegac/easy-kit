from pathlib import Path

from easy_kit.helper import Helper
from easy_kit.timing import TimingTestCase


class TestHelper(TimingTestCase):
    def test_available_filename(self):
        path = Path(__file__)
        expected = path.with_stem(f'{path.stem}-{1}')
        actual = Helper.available_filename(path)
        print(f'base_file: {path}')
        print(f'actual: {actual}')
        print(f'expected: {expected}')
        self.assertEqual(expected, actual)
