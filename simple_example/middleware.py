from __future__ import annotations

from abc import ABC, abstractmethod


class Middleware(ABC):
    _successor: Middleware | None = None

    @abstractmethod
    def handle(self, request: int) -> str | None:
        pass

    def set_successor(self, successor: Middleware) -> Middleware:
        self._successor = successor
        return successor

    def _pass(self, request: int) -> str | None:
        if self._successor:
            return self._successor.handle(request)

        return None
