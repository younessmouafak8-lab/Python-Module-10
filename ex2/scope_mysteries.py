def mage_counter() -> callable:
    counter = 0

    def count():
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> callable:

    def accumulate_power(power):
        nonlocal initial_power
        initial_power += power
        return initial_power
    return accumulate_power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchante(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchante


def memory_vault() -> dict[str, callable]:
    dic = {}

    def store(key, value):
        dic[key] = value

    def recall(key):
        return dic.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main():
    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))


main()
