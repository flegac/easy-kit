from typing import Type, Any


class Context:
    def __init__(self, *initial_state: Any):
        self.data: dict[Type, Any] = {}
        for _ in initial_state:
            self.register(_)

    def register[T](self, data: T, ctype: Type[T] = None):
        found_type = type(data)

        if ctype is not None:
            if not issubclass(found_type, ctype):
                raise ValueError(f'incompatible type [{ctype}] for data of type [{found_type}]')

        if ctype is not None:
            assert issubclass(found_type, ctype)
        else:
            ctype = found_type
        self.data[ctype] = data
        return self

    def find[T](self, ctype: Type[T]) -> T:
        return self.data[ctype]
