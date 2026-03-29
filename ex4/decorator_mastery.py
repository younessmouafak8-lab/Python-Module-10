from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def casting() -> str | None:
        start = time.time()
        print(f"Casting {func.__name__}...")
        result = func()
        end = time.time()
        print(f"Spell completed in {(end - start):.6f} seconds")
        return result

    return casting


def power_validator(min_power: int) -> callable:
    def validate(func: callable) -> callable:
        @wraps(func)
        def validate_inner(self, spell_name, power, *args,
                           **kwargs) -> str | None:
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return validate_inner
    return validate


def retry_spell(max_attempts: int) -> callable:
    def retry(func: callable) -> callable:
        def inner(*args, **kwargs) -> str | None:
            for i in range(1, max_attempts + 1):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    print(f"Spell failed, retrying... ({i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return inner
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3 or \
                not all([c.isalpha() or c.isspace() for c in name]):
            return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def fireball() -> str:
    return "Fireball cast!"


def main() -> None:
    print("\nTesting spell timer...")
    func = spell_timer(fireball)
    print(f"Result: {func()}")

    print("\nTesting MageGuild...")
    mage_guild = MageGuild()
    print(mage_guild.validate_mage_name("Magic"))
    print(mage_guild.validate_mage_name("Magic1"))
    print(mage_guild.cast_spell("Lightning", 15))
    print(mage_guild.cast_spell("Lightning", 5))


main()
