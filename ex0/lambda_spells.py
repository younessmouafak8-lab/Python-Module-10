def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    res = list(filter(lambda x: x['power'] >= min_power, mages))
    return res


def spell_transformer(spells: list[str]) -> list[str]:
    res = list(map(lambda x: f"* {x} *", spells))
    return res


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])
    min_power = min(mages, key=lambda x: x['power'])
    total_mages = len(mages)
    power_sum = sum(map(lambda x: x['power'], mages))
    avg_power = 0 if total_mages == 0 else power_sum / total_mages
    return {'max_power': max_power['power'],
            'min_power': min_power['power'],
            'avg_power': round(avg_power, 2)}


def main():
    fire_staff = {'name': "Fire Staff", 'power': 92, 'type': "Fire"}
    crystal_orb = {'name': "Crystal Orb", 'power': 85, 'type': "Crystal"}
    print("\nTesting artifact sorter...")
    artifacts = artifact_sorter([crystal_orb, fire_staff])
    for i, artifact in enumerate(artifacts):
        if i == 0:
            print(f"{artifact['name']} ({artifact['power']}) ", end="")
        else:
            print(f"comes before {artifact['name']} ({artifact['power']})",
                  end="")
    print("\n\nTesting spell transformer...")
    spells = ["fireball", "heal", "sheild"]
    transformed_spells = spell_transformer(spells)
    for spell in transformed_spells:
        print(f"{spell} ", end="",)
    print()


main()
