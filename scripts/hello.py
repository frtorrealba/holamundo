"""Utility functions used by the sample app.

This module demonstrates a small, well-documented function suitable
for generating docs from docstrings. Use Google or reST style docstrings.
"""

from typing import Optional


def greet(name: Optional[str] = None) -> str:
    """Return a friendly greeting.

    Args:
        name: Person or thing to greet. Defaults to "Mundo".

    Returns:
        A greeting string, e.g. "¡Hola, Mundo!".
    """

    if not name:
        name = "Mundo"
    return f"¡Chao,nos vimos {name}!"


if __name__ == "__main__":
    # Simple CLI demo: prints greeting for an optional first CLI arg
    import sys

    arg = sys.argv[1] if len(sys.argv) > 1 else None
    print(greet(arg))
