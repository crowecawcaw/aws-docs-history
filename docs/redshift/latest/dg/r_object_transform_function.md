

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# OBJECT\_TRANSFORM function
<a name="r_object_transform_function"></a>

Transforms a SUPER object.

## Syntax
<a name="r_object_transform_function-synopsis"></a>

```
OBJECT_TRANSFORM(
  input
  [KEEP path1, ...]
  [SET
    path1, value1,
    ...,  ...
  ]
)
```

## Arguments
<a name="r_object_transform_function-arguments"></a>

*input*  
An expression that resolves to a SUPER type object.

*KEEP*  
All *path* values specified in this clause are kept and carried over to the output object.  
This clause is optional.

*path1*, *path2*, ...  
Constant string literals, in the format of double-quoted path components delimited by periods. For example, `'"a"."b"."c"'` is a valid path value. This applies to the path parameter in both the KEEP and SET clauses.

*SET*  
*path* and *value* pairs to modify an exiting path or add a new path, and set the value of that path in the output object.  
This clause is optional.

*value1*, *value2*, ...  
Expressions that resolve to SUPER type values. Note that numeric, text, and Boolean types are resolvable to SUPER.

## Return type
<a name="r_object_transform_function-returns"></a>

`SUPER`

## Usage notes
<a name="r_object_transform_function-usage-notes"></a>

OBJECT\_TRANSFORM returns a SUPER type object containing the path values from *input* that were specified in KEEP and the *path* and *value* pairs that were specified in SET. 

If both KEEP and SET are empty, OBJECT\_TRANSFORM returns *input*.

If *input* isn’t a SUPER type *object*, OBJECT\_TRANSFORM returns *input*, regardless of any KEEP or SET values.

## Example
<a name="r_object_transform_function-example"></a>

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
                  col_person_transformed
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
}
```