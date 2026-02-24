from first_middleware import FirstMiddleware
from middle_middleware import MiddleMiddleware
from last_middleware import LastMiddleware

def main(request: int) -> str | None:
    first = FirstMiddleware()
    middle = MiddleMiddleware()
    last = LastMiddleware()
    first.set_successor(middle).set_successor(last)

    return first.handle(request)

print(main(1))
print(main(5))
print(main(15))
print(main(100))
