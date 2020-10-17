
# TODO - try to find a regexp able to check the overall validity (instead of incremental checks)

# Regexp able to extract named match groups from a FIQL constraint instance.
REGEXP_CONSTRAINT = r'(?P<loperand>[\w-]+)(?P<operator>=.{0,}=)(?P<roperand>[\*\"\w-]+)'

# FIQL logical operators.
LOGICAL_OPERATOR = [
    (';', 'Logical AND'),
    (',', 'Logical OR')
]

# FIQL constraint operators.
CONSTRAINT_OPERATOR = [
    '==',
    '=lt=',
    '=gt=',
    '=lte=',
    '=gte=',
    '=!~='
]

# Translation table of FIQL logical operators and SQL ones.
SQL_LOGICAL_OPERATOR = {
    ',': 'OR',
    ';': 'AND'
}

# Translation table of FIQL logical operators and JSON ones.
JSON_LOGICAL_OPERATOR = {
    ',': 'or',
    ';': 'and'
}

# Translation table of FIQL constraint operators and SQL ones.
SQL_CONSTRAINT_OPERATOR = {
    '==': '=',
    '=lt=': '<',
    '=gt=': '>',
    '=lte=': '<=',
    '=gte=': '>=',
    '=!~=': '~'
}

## Translation table of FIQL constraint operators and JSON ones.
JSON_CONSTRAINT_OPERATOR = {
    '==': 'eq',
    '=lt=': '<',
    '=gt=': '>',
    '=lte=': '<=',
    '=gte=': '>=',
    '=!~=': '~'
}
