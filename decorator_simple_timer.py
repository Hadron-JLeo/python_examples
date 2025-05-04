import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} dauerte {end - start:.4f} Sekunden")
        return result
    return wrapper

@timing
def slow_add(x, y):
    time.sleep(1)
    return x + y

slow_add(3, 4)
