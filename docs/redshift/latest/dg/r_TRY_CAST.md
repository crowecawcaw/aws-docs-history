Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TRY_CAST function

Compared to the CAST function, TRY_CAST
first attempts to cast the expression to the specified type.
If casting fails because of conversion errors, the operation
returns null. If a conversion isn’t explicitly permitted,
the operation returns an error. You can find the list of
possible conversions in the usage notes below. For example,
attempting to convert a boolean to a timestamp isn't permitted.

## Syntax

```
TRY_CAST(expression AS type)
```

## Arguments

_expression_

An expression that evaluates to one
or more values, such as a column name or a literal.
Converting null values returns nulls. The expression
cannot contain blank or empty strings.

_type_

One of the supported data types. For a full list of data types, see
[Data types](c_Supported_data_types.md "c_Supported_data_types.md").
For the list of supported source data type and target data type pairs,
see the usage notes below.

## Return type

TRY_CAST returns a value of the data type specified by the
_type_ argument. If the conversion fails,
the operation returns null.

## Usage notes

Following is the list of source data type
and target data type pairs that Amazon Redshift supports for
TRY_CAST.

_BOOL_

SMALLINT, INT, BIGINT, SUPER

_SMALLINT_

BOOL, INT, BIGINT, DECIMAL, REAL, FLOAT, BPCHAR, TEXT, VARCHAR, SUPER

_INT_

BOOL, SMALLINT, BIGINT, DECIMAL, REAL, FLOAT, BPCHAR, TEXT, VARCHAR, SUPER

_BIGINT_

BOOL, SMALLINT, INT, DECIMAL, REAL, FLOAT, BPCHAR, TEXT, VARCHAR, SUPER

_DECIMAL_

SMALLINT, INT, BIGINT, REAL, FLOAT, BPCHAR, TEXT, VARCHAR, SUPER

_REAL_

SMALLINT, INT, BIGINT, DECIMAL, FLOAT, BPCHAR, TEXT, VARCHAR, SUPER

_FLOAT_

SMALLINT, INT, BIGINT, DECIMAL, REAL, BPCHAR, TEXT, VARCHAR, SUPER

_BPCHAR_

SMALLINT, INT, BIGINT, DECIMAL, REAL, FLOAT, TEXT, VARCHAR, TIMESTAMP, TIMESTAMPTZ, DATE, TIME, TIMETZ, SUPER

_TEXT_

SMALLINT, INT, BIGINT, DECIMAL, REAL, FLOAT, BPCHAR, VARCHAR, TIMESTAMP, TIMESTAMPTZ, DATE, TIME, TIMETZ, SUPER

_VARCHAR_

SMALLINT, INT, BIGINT, DECIMAL, REAL, FLOAT, BPCHAR, TEXT, TIMESTAMP, TIMESTAMPTZ, DATE, TIME, TIMETZ, SUPER

_TIMESTAMP_

BPCHAR, TEXT, VARCHAR, TIMESTAMPTZ, DATE, TIME

_TIMESTAMPTZ_

BPCHAR, TEXT, VARCHAR, TIMESTAMP, DATE, TIME, TIMETZ

_DATE_

BPCHAR, TEXT, VARCHAR, TIMESTAMP, TIMESTAMPTZ

_TIME_

BPCHAR, TEXT, VARCHAR

_TIMETZ_

BPCHAR, TEXT, VARCHAR

_SUPER_

SUPER can be converted into any other data type, with the exception of DATE, TIME, TIMETZ, TIMESTAMP, and TIMESTAMPTZ.

## Examples

The following example casts a STRING into an INTEGER.

```
SELECT TRY_CAST('123' AS INT);

`int
----
123`
```

The following example returns null.
Converting a STRING to an INTEGER is permitted so TRY_CAST doesn't
return an error, but 'foo' isn't an integer so the function
returns null.

```
SELECT TRY_CAST('foo' AS INT)
```

The following example returns an error, because converting
a BOOLEAN to a TIMESTAMP isn't permitted.

```
SELECT TRY_CAST(true as timestamp);
```

Because TRY_CAST returns null instead of immediately
returning an error if conversion fails, you can use
TRY_CAST to filter out invalid data. Consider the following
example, where an invalid row is filtered out because of a
conversion failure in the age column for Akua Mansa.

```
CREATE TABLE IF NOT EXISTS student_data(
name VARCHAR(100) NOT NULL,
age VARCHAR(3) NOT NULL,
enrollment_date DATE NOT NULL);

INSERT INTO student_data (name, age, enrollment_date)
VALUES
('Alejandro Rosalez', '10', '01/01/2000'),
('Akua Mansa', 'Ten', '01/01/2000');

SELECT * FROM student_data WHERE TRY_CAST(age AS INT) IS NOT NULL;

--Akua is not returned.
 name              | age | enrollment_date
-------------------+-----+-----------------
 Alejandro Rosalez | 10  | 01/01/2000
```
