from middleware import Middleware

class FirstMiddleware(Middleware):
    def handle(self, request: int) -> str | None:
        if request == 1:
            return "First"

        return self._pass(request)
