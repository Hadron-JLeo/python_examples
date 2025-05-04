class Sample:
    def __init__(self):
        return 42

## Attempting to instantiate Sample will result in an error
a = Sample()  # Raises TypeError: __init__() should return None
