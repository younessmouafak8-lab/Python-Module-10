def spell_combiner(spell1: callable, spell2: callable) -> callable:

    def combined(target):
        return (spell1(target), spell2(target))

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def mega_fireball(target):
        result = base_spell(target)
        return result * multiplier

    return mega_fireball


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(trick):
        if condition(trick):
            return spell(trick)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def cast_all_spells(trick):
        results = [spell(trick) for spell in spells]
        return results
    return cast_all_spells


def fire_ball(target):
    return f"Fireball hits {target}"


def heal(target):
    return f"Heals {target}"


def mana_generator(target):
    return 10


def main():
    print("\nTesting spell combiner...")
    combined = spell_combiner(fire_ball, heal)
    fire, healing = combined("Dragon")
    print(f"Combined spell result: {fire}, {healing}\n")

    print("Testing power amplifier...")
    mana = 10
    mana_amplifier = power_amplifier(mana_generator, 3)
    amplified_mana = mana_amplifier("dargon")
    print(f"Original: {mana}, Amplified: {amplified_mana}")


main()
