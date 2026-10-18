from src.database.repository import(
    get_dataset,
    get_enabled_quality_rules
)

def main():
    dataset = get_dataset(1)
    rules = get_enabled_quality_rules(1)

    print('Dataset:')
    print(dataset)

    print('\nEnabled quality rules:')
    for rule in rules:
        print(rule)
    print(f'\nTotal enabled rules: {len(rules)}')

if __name__=="__main__":
    main()
