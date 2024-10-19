from pathlib import Path
from typing import Any

from pydantic import Field

from easy_kit.my_model import MyModel
from easy_kit.timing import TimingTestCase, timing


class Item(MyModel):
    attributes: dict[str, Any] = Field(default_factory=dict)


class Region(MyModel):
    name: str
    items: list[Item]


class State(MyModel):
    id: str
    regions: list[Region] = Field(default_factory=list)


state = State(id='toto', regions=[
    Region(
        name=f'region_{i}',
        items=[Item(attributes={'i': i, 'j': j}) for j in range(10)]
    )
    for i in range(100)
])


class TestModel(TimingTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.temp_path = Path.cwd() / 'toto.csv'

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.temp_path.unlink(missing_ok=True)

    def test_json(self):
        root = Path.cwd()
        path = root / 'toto.json'
        for i in range(100):
            with timing('json.save'):
                state.save(path)
            with timing('json.load'):
                xxx = State.load(path)
            with timing('json.load[no_validation]'):
                xxx = State.load(path, validate=False)

    # def test_bson(self):
    #     root = Path.cwd()
    #     path = root / 'toto.bson'
    #     for i in range(100):
    #         with timing('bson.save'):
    #             state.save(path)
    #         with timing('bson.load'):
    #             xxx = State.load(path)
    #         with timing('bson.load[no_validation]'):
    #             xxx = State.load(path, validate=False)
