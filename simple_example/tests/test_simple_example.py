"""Basic tests for the chain-of-responsibility example."""

from first_middleware import FirstMiddleware
from last_middleware import LastMiddleware
from middle_middleware import MiddleMiddleware


def build_chain():
    """Build the same chain as main.py: first -> middle -> last."""
    first = FirstMiddleware()
    middle = MiddleMiddleware()
    last = LastMiddleware()
    first.set_successor(middle).set_successor(last)
    return first


class TestFirstMiddleware:
    """Tests for FirstMiddleware: handles request == 1."""

    def test_handles_one(self):
        chain = build_chain()
        assert chain.handle(1) == "First"

    def test_passes_other_values(self):
        chain = build_chain()
        assert chain.handle(5) == "Middle"
        assert chain.handle(100) == "Last"


class TestMiddleMiddleware:
    """Tests for MiddleMiddleware: handles 1 < request < 20."""

    def test_handles_range(self):
        chain = build_chain()
        assert chain.handle(2) == "Middle"
        assert chain.handle(10) == "Middle"
        assert chain.handle(19) == "Middle"

    def test_does_not_handle_one(self):
        chain = build_chain()
        assert chain.handle(1) == "First"

    def test_passes_large_values(self):
        chain = build_chain()
        assert chain.handle(20) == "Last"
        assert chain.handle(100) == "Last"


class TestLastMiddleware:
    """Tests for LastMiddleware: handles request > 1."""

    def test_handles_large_values(self):
        chain = build_chain()
        assert chain.handle(20) == "Last"
        assert chain.handle(100) == "Last"

    def test_does_not_handle_one(self):
        chain = build_chain()
        assert chain.handle(1) == "First"


class TestFullChain:
    """Tests for the full chain matching main.py behavior."""

    def test_main_example_outputs(self):
        """Values used in main.py produce expected results."""
        chain = build_chain()
        assert chain.handle(1) == "First"
        assert chain.handle(5) == "Middle"
        assert chain.handle(15) == "Middle"
        assert chain.handle(100) == "Last"

    def test_unhandled_request_returns_none(self):
        """Request that no handler accepts (e.g. 0) returns None."""
        chain = build_chain()
        assert chain.handle(0) is None
