"""Entry point for the sample project.

This simple runner imports the example `greet` function from
`scripts/hello.py` and prints a greeting. It's intentionally tiny
so contributors can experiment with documenting functions and
rendering docs in `docs/`.
"""

from .hello import greet


def main():
	print(greet("Mundo"))


if __name__ == "__main__":
	main()
