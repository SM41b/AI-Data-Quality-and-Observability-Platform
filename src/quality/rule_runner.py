from src.quality.quality_engine import(
    check_not_null,
    check_unique,
    check_numeric
)
RULE_FUNCTIONS = {
     "not_null": check_not_null,
     "unique": check_unique,
     "numeric": check_numeric
}

def run_quality_rules(df, rules):
    '''Execute configured quality rules against a DataFrame'''

    results = []

    for rule in rules:
        rule_type = rule["rule_type"]
        column = rule['column_name']

        if rule_type not in RULE_FUNCTIONS:
            raise ValueError(
                f'Unsupported rule type: {rule_type}'
            )
        if column not in df.columns:
            raise ValueError(
                f'Column {column} does not exist in dataset.'
            )
        check_function = RULE_FUNCTIONS[rule_type]
        result = check_function(df, column)

        result['rule_id'] = rule['id']
        result['severity'] = rule['severity']

        results.append(result)

    return results
