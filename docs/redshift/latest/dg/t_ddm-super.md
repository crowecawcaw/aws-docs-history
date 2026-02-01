Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using dynamic data masking with SUPER data type paths

Amazon Redshift supports attaching dynamic data masking policies to paths of SUPER type columns.
For more information about the SUPER data type, see
[Semi-structured data in Amazon Redshift](super-overview.md "super-overview.md").

When attaching masking policies to paths of SUPER type columns, consider the following.

- When attaching a masking policy to a path on a column, that column must
  be defined as the SUPER data type. You can only apply masking
  policies to _scalar_ values on the SUPER path. You can't
  apply masking policies to complex structures or arrays.
- You can apply different masking policies to multiple scalar values on
  a single SUPER column, as long as the SUPER paths don't conflict.
  For example, the SUPER paths `a.b` and `a.b.c`
  conflict because they are on the same path, with `a.b`
  being the parent of `a.b.c`. The SUPER paths
  `a.b.c` and `a.b.d` don’t conflict.
- Amazon Redshift can’t check that the paths that a masking policy attaches
  to exist in the data and are of the expected type until the policy
  is applied at user query runtime. For example, when you attach a masking
  policy that masks TEXT values to a SUPER path that contains an INT value,
  Amazon Redshift will attempt to cast the type of the value at the path.

In such situations, the behavior of Amazon Redshift at runtime depends on
your configuration settings for querying SUPER objects.
By default, Amazon Redshift is in lax mode, and will resolve missing paths and invalid
casts as `NULL` for the given SUPER path.
For more information about SUPER-related
configuration settings, see [SUPER configurations](super-configurations.md "super-configurations.md").

- SUPER is a schemaless type, which means that Amazon Redshift can’t confirm the existence of
  the value at a given SUPER path. If you attach a masking policy to a SUPER path
  that doesn’t exist and Amazon Redshift is in lax mode, Amazon Redshift will resolve the path
  to a `NULL` value. We recommend that you consider the expected format of SUPER
  objects and the likelihood of them having unexpected attributes when
  attaching masking policies to paths of SUPER columns. If you think there
  might be an unexpected schema in your SUPER column, consider attaching
  your masking policies directly to the SUPER column. You can use SUPER type information
  functions to check attributes and types, and using `OBJECT_TRANSFORM` to
  mask the values. For more information about SUPER type information functions,
  see [SUPER type information functions](c_Type_Info_Functions.md "c_Type_Info_Functions.md").

## Examples

###### Attaching masking policies to SUPER paths

The following example attaches multiple masking policies
onto multiple SUPER type paths in one column.

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
                "company": "Company Inc."
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
                "company": "Organization Org."
            }
        ')
    )
;
GRANT ALL ON ALL TABLES IN SCHEMA "public" TO PUBLIC;

-- Create the masking policies.

-- This policy converts the given name to all uppercase letters.
CREATE MASKING POLICY mask_first_name
WITH(first_name TEXT)
USING ( UPPER(first_name) );

-- This policy replaces the given name with the fixed string 'XXXX'.
CREATE MASKING POLICY mask_last_name
WITH(last_name TEXT)
USING ( 'XXXX'::TEXT );

-- This policy rounds down the given age to the nearest 10.
CREATE MASKING POLICY mask_age
WITH(age INT)
USING ( (FLOOR(age::FLOAT / 10) * 10)::INT );

-- This policy converts the first five digits of the given SSN to 'XXX-XX'.
CREATE MASKING POLICY mask_ssn
WITH(ssn TEXT)
USING ( 'XXX-XX-'::TEXT || SUBSTRING(ssn::TEXT FROM 8 FOR 4) );

-- Attach the masking policies to the employees table.
ATTACH MASKING POLICY mask_first_name
ON employees(col_person.name.first)
TO PUBLIC;

ATTACH MASKING POLICY mask_last_name
ON employees(col_person.name.last)
TO PUBLIC;

ATTACH MASKING POLICY mask_age
ON employees(col_person.age)
TO PUBLIC;

ATTACH MASKING POLICY mask_ssn
ON employees(col_person.ssn)
TO PUBLIC;

-- Verify that your masking policies are attached.
SELECT
    policy_name,
    TABLE_NAME,
    priority,
    input_columns,
    output_columns
FROM
    svv_attached_masking_policy;

 `policy_name | table_name | priority | input_columns | output_columns
-----------------+------------+----------+-----------------------------------+-----------------------------------
 mask_age | employees | 0 | ["col_person.\"age\""] | ["col_person.\"age\""]
 mask_first_name | employees | 0 | ["col_person.\"name\".\"first\""] | ["col_person.\"name\".\"first\""]
 mask_last_name | employees | 0 | ["col_person.\"name\".\"last\""] | ["col_person.\"name\".\"last\""]
 mask_ssn | employees | 0 | ["col_person.\"ssn\""] | ["col_person.\"ssn\""]
(4 rows)`

-- Observe the masking policies taking effect.
SELECT col_person FROM employees ORDER BY col_person.age;

-- This result is formatted for ease of reading.
 `col_person
--------------------------------
{
 "name": {
 "first": "JOHN",
 "last": "XXXX"
 },
 "age": 20,
 "ssn": "XXX-XX-3333",
 "company": "Company Inc."
}
{
 "name": {
 "first": "JANE",
 "last": "XXXX"
 },
 "age": 30,
 "ssn": "XXX-XX-7777",
 "company": "Organization Org."
}`
```

Following are some examples of invalid masking policy attachments to SUPER paths.

```
-- This attachment fails because there is already a policy
-- with equal priority attached to employees.name.last, which is
-- on the same SUPER path as employees.name.
ATTACH MASKING POLICY mask_ssn
ON employees(col_person.name)
TO PUBLIC;
`ERROR: DDM policy "mask_last_name" is already attached on relation "employees" column "col_person."name"."last"" with same priority`

-- Create a masking policy that masks DATETIME objects.
CREATE MASKING POLICY mask_date
WITH(INPUT DATETIME)
USING ( INPUT );

-- This attachment fails because SUPER type columns can't contain DATETIME objects.
ATTACH MASKING POLICY mask_date
ON employees(col_person.company)
TO PUBLIC;
`ERROR: cannot attach masking policy for output of type "timestamp without time zone" to column "col_person."company"" of type "super`
```

Following is an example of attaching a masking policy to a
SUPER path that doesn’t exist. By default, Amazon Redshift will resolve the path to `NULL`.

```
ATTACH MASKING POLICY mask_first_name
ON employees(col_person.not_exists)
TO PUBLIC;

SELECT col_person FROM employees LIMIT 1;

-- This result is formatted for ease of reading.
 `col_person
-----------------------------------
{
 "name": {
 "first": "JOHN",
 "last": "XXXX"
 },
 "age": 20,
 "ssn": "XXX-XX-3333",
 "company": "Company Inc.",
 "not_exists": null
}`
```
