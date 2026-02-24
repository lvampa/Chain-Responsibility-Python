from middleware import Middleware

class MiddleMiddleware(Middleware):
    def handle(self, request: int) -> str | None:
        if 1 < request < 20:
            return "Middle"

        return self._pass(request)
