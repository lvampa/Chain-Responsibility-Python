from middleware import Middleware


class LastMiddleware(Middleware):
    def handle(self, request: int) -> str | None:
        if request > 1:
            return "Last"

        return self._pass(request)
