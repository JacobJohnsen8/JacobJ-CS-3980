# JacobJ-CS-3980
Coding Projects for my Topics in Computer Science course at the University of Iowa

---

# Python Referesher Assignment

## Images:
### Echo.py
<img width="670" height="459" alt="image" src="https://github.com/user-attachments/assets/b3ed7c0f-7500-4339-aaac-3875912da9c4" />
### Fib.py
<img width="769" height="397" alt="image" src="https://github.com/user-attachments/assets/4e8bd109-1b78-45ba-bcb1-bfd7b861d8a4" />
<img width="773" height="367" alt="image" src="https://github.com/user-attachments/assets/8466fe99-33c6-4192-b1a3-2886572170b4" />
<img width="768" height="254" alt="image" src="https://github.com/user-attachments/assets/7cde9c02-39d7-482f-83a5-16a81faf4702" />
### Fib times graph
<img width="596" height="469" alt="image" src="https://github.com/user-attachments/assets/7488ff68-071d-47c8-bcb3-9f6b4dc6375c" />


# RAW CODE:
## Echo.py

def echo(text: str, repetitions: int = 3) -> str:
    "immitate a real world echo."
    print(text[-(repetitions):])
    print(text[-(repetitions- 1):])
    print(text[-(repetitions- 2):])
    print(".")

if __name__ == "__main__":
    text = input("Yell something into the mountians!: ")
    print(echo(text))

# Fib.py
from __future__ import annotations
from functools import lru_cache, wraps
from time import perf_counter
from typing import Callable, Dict, Any

TIMES: Dict[int, float] = {}


def timer(func: Callable[..., int]) -> Callable[..., int]:
    """Decorator that times a function call and prints: Finished in Xs: f(n) -> result
    Also stores timings in TIMES[n].
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> int:
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start

        # fib's first positional arg is n
        n = int(args[0]) if args else int(kwargs.get("n"))
        TIMES[n] = elapsed

        print(f"Finished in {elapsed:.7f}s: f({n}) -> {result}")
        return result

    return wrapper


@lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    """Return the nth Fibonacci number (recursive)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def make_plot(max_n: int = 100, filename: str = "fib_times.png") -> None:
    """Create a time vs n plot from the collected TIMES dict."""
    import matplotlib.pyplot as plt

    xs = list(range(max_n + 1))
    ys = [TIMES.get(i, 0.0) for i in xs]

    plt.figure()
    plt.plot(xs, ys)
    plt.title("Fibonacci Execution Time (with lru_cache)")
    plt.xlabel("n")
    plt.ylabel("time (seconds)")
    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close()


if __name__ == "__main__":
    # Run the required test
    fib(100)

    # Make the required plot image for your repo / README
    make_plot(100, "fib_times.png")
