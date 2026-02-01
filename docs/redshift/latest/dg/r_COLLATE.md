Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# COLLATE function

The COLLATE function overrides the collation of a string column or expression.

For information on how to create tables using database collation, see [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md").

For information on how to create databases using database collation, see [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md").

## Syntax

```
COLLATE( `string`, *'case\_sensitive'* | *'cs'* | *'case\_insensitive'* | *'ci'*);
```

## Arguments

_string_

A string column or expression that you want to override.

_'case_sensitive'_ | _'cs'_ | _'case_insensitive'_ | _'ci'_

A string constant of a collation name. Amazon Redshift only
supports the following values for this parameter:

- _case_sensitive_
- _cs_
- _case_insensitive_
- _ci_

_case_sensitive_ and _cs_ are interchangeable and yield the same results.
Similarly, _case_insensitive_ and _ci_ are interchangeable and yield the same results.

## Return type

The COLLATE function returns `VARCHAR`, `CHAR`, or
`SUPER` depending on the first input expression type. This function
only changes the collation of the first input argument and won't change its
output value.

## Examples

To create table T and define col1 in table T as `case_sensitive`, use the following example.

```
`CREATE TABLE T ( col1 Varchar(20) COLLATE case_sensitive );

INSERT INTO T VALUES ('john'),('JOHN');`
```

When you run the first query, Amazon Redshift only returns `john`. After the COLLATE function runs on
col1, the collation becomes `case_insensitive`. The second query returns both `john` and `JOHN`.

```
`SELECT * FROM T WHERE col1 = 'john';`

`+------+
| col1 |
+------+
| john |
+------+`

`SELECT * FROM T WHERE COLLATE(col1, 'case_insensitive') = 'john';`

`+------+
| col1 |
+------+
| john |
| JOHN |
+------+`
```

To create table A and define col1 in table A as `case_insensitive`, use the following example.

```
`CREATE TABLE A ( col1 Varchar(20) COLLATE case_insensitive );

INSERT INTO A VALUES ('john'),('JOHN');`
```

When you run the first query, Amazon Redshift returns both `john` and `JOHN`. After the COLLATE function runs on
col1, the collation becomes `case_sensitive`. The second query returns only `john`.

```
`SELECT * FROM A WHERE col1 = 'john';`

`+------+
| col1 |
+------+
| john |
| JOHN |
+------+`

`SELECT * FROM A WHERE COLLATE(col1, 'case_sensitive') = 'john';`

`+------+
| col1 |
+------+
| john |
+------+`
```
