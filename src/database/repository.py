from src.database.connection import get_connection

def get_dataset(dataset_id: int) ->dict|None:
    '''Fetch one dataset by its ID. '''
    query = '''
        SELECT id, name, source_type, source_location
        FROM datasets
        WHERE id = %s;
    '''

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (dataset_id,))
            row = cursor.fetchone()
    if row is None:
        return None

    return {
        'id':row[0],
        'name':row[1],
        'source_type':row[2],
        'source_location':row[3],
    }

def get_enabled_quality_rules(dataset_id:int)->list[dict]:
    '''Fetch all enabled quality rules from a dataset.'''

    query = '''
        SELECT
            id,
            dataset_id,
            column_name,
            rule_type,
            parameters,
            severity,
            enabled
            FROM quality_rules
            WHERE dataset_id = %s
                AND enabled = TRUE
            ORDER BY id;
    '''
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query,(dataset_id,))
            rows = cursor.fetchall()

    return [
        {
            'id': row[0],
            'dataset_id': row[1],
            'column_name': row[2],
            'rule_type': row[3],
            'parameters': row[4],
            'severity': row[5],
            'enabled': row[6]
        }
        for row in rows
    ]