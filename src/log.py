def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


def log_call(method):
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except:
            print(f"Failed calling {method.__name__},on {self} returning None")
            return None
        return method(*args, **kwargs)

    return wrapper


@repeat(3)
@log_call
def hello_world():
    print("Hello world!")


hello_world()
