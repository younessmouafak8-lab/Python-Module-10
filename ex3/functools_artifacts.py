from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int | None:
    result = None

    ops = {
            "add":      add,
            "multiply": mul,
            "max":      max,
            "min":      min,
        }
    if operation in ops:
        result = reduce(ops[operation], spells)
    return result


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    lightning = partial(base_enchantment, 50, "lightning")

    return {'fire_enchant': fire,
            'ice_enchant': ice,
            'lightning_enchant': lightning}


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch
    def dispatcher_function(value: Any) -> None:
        ...

    @dispatcher_function.register
    def _(value: int) -> str:
        return f'deal {value} damage'

    @dispatcher_function.register
    def _(value: str) -> str:
        return value

    @dispatcher_function.register
    def _(value: list) -> list:
        results = [dispatcher_function(spell) for spell in value]
        return results

    return dispatcher_function


def main() -> None:

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer([25, 25, 25, 25], 'add')}")
    print(f"Product: {spell_reducer([80, 30, 100], 'multiply')}")
    print(f"Max: {spell_reducer([25, -1, 40], 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


main()
