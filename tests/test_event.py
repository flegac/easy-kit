from unittest import TestCase

from easy_kit.event import Event


class TestEvent(TestCase):
    def test_event(self):
        # allow to register new observers (if not enabled, the lib is disabled and has no performance impact)
        Event.enable()

        # create an event queue
        toto = Event(name='Toto')

        @toto.observe
        def send_hello(data: str):
            return f'hello {data}'

        @toto.connect
        def handler(data: str):
            print(f'echo: {data}')

        toto.emit('coucou')
        send_hello('toto')
