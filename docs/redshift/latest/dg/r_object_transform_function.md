Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# OBJECT_TRANSFORM function

Transforms a SUPER object.

## Syntax

```
OBJECT_TRANSFORM(
  *input*
  [KEEP *path1*, ...]
  [SET
    *path1*, *value1*,
    ...,  ...
  ]
)
```

## Arguments

_input_

An expression that resolves to a SUPER type object.

_KEEP_

All _path_ values specified in this clause
are kept and carried over to the output object.

This clause is optional.

_path1_, _path2_, ...

Constant string literals, in the format of double-quoted path
components delimited by periods. For example, `'"a"."b"."c"'`
is a valid path value. This applies to the path parameter in
both the KEEP and SET clauses.

_SET_

_path_ and _value_ pairs
to modify an exiting path or add a new path, and set the value
of that path in the output object.

This clause is optional.

_value1_, _value2_, ...

Expressions that resolve to SUPER type values. Note that numeric,
text, and Boolean types are resolvable to SUPER.

## Return type

`SUPER`

## Usage notes

OBJECT_TRANSFORM returns a SUPER type object containing the path values
from _input_ that were specified in KEEP and the
_path_ and _value_ pairs
that were specified in SET.

If both KEEP and SET are empty, OBJECT_TRANSFORM returns
_input_.

If _input_ isn’t a SUPER type _object_, OBJECT_TRANSFORM
returns _input_, regardless of any KEEP or SET values.

## Example

The following example transforms a SUPER object into another SUPER object.

```
CREATE TABLE employees (
    col_person SUPER
);

INSERT INTO employees
VALUES
    (
        json_parse('
            {
                "name": {
                    "first": "John",
                    "last": "Doe"
                },
                "age": 25,
                "ssn": "111-22-3333",
                "company": "Company Inc.",
                "country": "U.S."
            }
        ')
    ),
    (
        json_parse('
            {
                "name": {
                    "first": "Jane",
                    "last": "Appleseed"
                },
                "age": 34,
                "ssn": "444-55-7777",
                "company": "Organization Org.",
                "country": "Ukraine"
            }
        ')
    )
;

SELECT
    OBJECT_TRANSFORM(
        col_person
        KEEP
            '"name"."first"',
            '"age"',
            '"company"',
            '"country"'
        SET
            '"name"."first"', UPPER(col_person.name.first::TEXT),
            '"age"', col_person.age + 5,
            '"company"', 'Amazon'
    ) AS col_person_transformed
FROM employees;

--This result is formatted for ease of reading.
 `col_person_transformed
-------------------------------------------------------------
{
 "name": {
 "first": "JOHN"
 },
 "age": 30,
 "company": "Amazon",
 "country": "U.S."
}
{
 "name": {
 "first": "JANE"
 },
 "age": 39,
 "company": "Amazon",
 "country": "Ukraine"
}`
```
