from typing import Any


def mage_counter() -> callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> callable:

    def accumulate_power(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return accumulate_power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchante(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchante


def memory_vault() -> dict[str, callable]:
    dic: dict[str, Any] = {}

    def store(key: str, value: int) -> None:
        dic[key] = value

    def recall(key: str) -> Any:
        return dic.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))


try:
    main()
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
