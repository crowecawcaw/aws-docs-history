# Type compatibility and conversion

The following topics describe how type conversion rules and data type compatibility work
in AWS Clean Rooms SQL.

###### Topics

- [Compatibility](#r_Type_conversion-compatibility "#r_Type_conversion-compatibility")
- [General
  compatibility and conversion rules](#r_Type_conversion-general-compatibility-and-conversion-rules "#r_Type_conversion-general-compatibility-and-conversion-rules")
- [Implicit conversion types](#implicit-conversion-types "#implicit-conversion-types")

## Compatibility

Data type matching and matching of literal values and constants to data types occurs
during various database operations, including the following:

- Data manipulation language (DML) operations on tables
- UNION, INTERSECT, and EXCEPT queries
- CASE expressions
- Evaluation of predicates, such as LIKE and IN
- Evaluation of SQL functions that do comparisons or extractions of data
- Comparisons with mathematical operators

The results of these operations depend on type conversion rules and data type
compatibility. _Compatibility_ implies that a one-to-one matching of
a certain value and a certain data type is not always required. Because some data types
are _compatible_, an implicit conversion, or
_coercion_, is possible. For more information, see [Implicit conversion types](#implicit-conversion-types "#implicit-conversion-types"). When
data types are incompatible, you can sometimes convert a value from one data type to
another by using an explicit conversion function.

## General

compatibility and conversion rules

Note the following compatibility and conversion rules:

- In general, data types that fall into the same type category (such as different
  numeric data types) are compatible and can be implicitly converted.

For example, with implicit conversion you can insert a decimal value into an
integer column. The decimal is rounded to produce a whole number. Or you can
extract a numeric value, such as `2008`, from a date and insert that
value into an integer column.

- Numeric data types enforce overflow conditions that occur when you attempt to
  insert out-of-range values. For example, a decimal value with a precision of 5
  does not fit into a decimal column that was defined with a precision of 4. An
  integer or the whole part of a decimal is never truncated. However, the fractional
  part of a decimal can be rounded up or down, as appropriate. However, results of
  explicit casts of values selected from tables are not rounded.
- Different types of character strings are compatible. VARCHAR column strings
  containing single-byte data and CHAR column strings are comparable and implicitly
  convertible. VARCHAR strings that contain multibyte data are not comparable. Also,
  you can convert a character string to a date, time, timestamp, or numeric value if
  the string is an appropriate literal value. Any leading or trailing spaces are
  ignored. Conversely, you can convert a date, time, timestamp, or numeric value to
  a fixed-length or variable-length character string.

###### Note

A character string that you want to cast to a numeric type must contain a
character representation of a number. For example, you can cast the strings
`'1.0'` or `'5.9'` to decimal values, but you can't
cast the string `'ABC'` to any numeric type.

- If you compare DECIMAL values with character strings, AWS Clean Rooms attempts to convert
  the character string to a DECIMAL value. When comparing all other numeric values
  with character strings, the numeric values are converted to character strings. To
  enforce the opposite conversion (for example, converting character strings to
  integers, or converting DECIMAL values to character strings), use an explicit
  function, such as [CAST function](r_CAST_function.md "r_CAST_function.md").
- To convert 64-bit DECIMAL or NUMERIC values to a higher precision, you must use
  an explicit conversion function such as the CAST or CONVERT functions.
- When converting DATE or TIMESTAMP to TIMESTAMPTZ, or converting TIME to TIMETZ,
  the time zone is set to the current session time zone. The session time zone is
  UTC by default.
- Similarly, TIMESTAMPTZ is converted to DATE, TIME, or TIMESTAMP based on the
  current session time zone. The session time zone is UTC by default. After the
  conversion, time zone information is dropped.
- Character strings that represent a timestamp with time zone specified are
  converted to TIMESTAMPTZ using the current session time zone, which is UTC by
  default. Likewise, character strings that represent a time with time zone
  specified are converted to TIMETZ using the current session time zone, which is
  UTC by default.

## Implicit conversion types

There are two types of implicit conversions:

- Implicit conversions in assignments, such as setting values in INSERT or UPDATE
  commands
- Implicit conversions in expressions, such as performing comparisons in the
  WHERE clause

The following table lists the data types that can be converted implicitly in
assignments or expressions. You can also use an explicit conversion function to perform
these conversions.

| From type                 | To type        |
| ------------------------- | -------------- |
| BIGINT                    | BOOLEAN        |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| DOUBLE PRECISION (FLOAT8) |
| INTEGER                   |
| REAL (FLOAT4)             |
| SMALLINT or SHORT         |
| VARCHAR                   |
| CHAR                      | VARCHAR        |
| DATE                      | CHAR           |
| VARCHAR                   |
| TIMESTAMP                 |
| TIMESTAMPTZ               |
| DECIMAL (NUMERIC)         | BIGINT or LONG |
| CHAR                      |
| DOUBLE PRECISION (FLOAT8) |
| INTEGER INT)              |
| REAL (FLOAT4)             |
| SMALLINT or SHORT         |
| VARCHAR                   |
| DOUBLE PRECISION (FLOAT8) | BIGINT or LONG |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| INTEGER (INT)             |
| REAL (FLOAT4)             |
| SMALLINT or SHORT         |
| VARCHAR                   |
| INTEGER (INT)             | BIGINT or LONG |
| BOOLEAN                   |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| DOUBLE PRECISION (FLOAT8) |
| REAL (FLOAT4)             |
| SMALLINT or SHORT         |
| VARCHAR                   |
| REAL (FLOAT4)             | BIGINT or LONG |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| INTEGER (INT)             |
| SMALLINT or SHORT         |
| VARCHAR                   |
| SMALLINT                  | BIGINT or LONG |
| BOOLEAN                   |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| DOUBLE PRECISION (FLOAT8) |
| INTEGER (INT)             |
| REAL (FLOAT4)             |
| VARCHAR                   |
| TIMESTAMP                 | CHAR           |
| DATE                      |
| VARCHAR                   |
| TIMESTAMPTZ               |
| TIME                      |
| TIMESTAMPTZ               | CHAR           |
| DATE                      |
| VARCHAR                   |
| TIMESTAMP                 |
| TIMETZ                    |
| TIME                      | VARCHAR        |
| TIMETZ                    |
| TIMETZ                    | VARCHAR        |
| TIME                      |

###### Note

Implicit conversions between TIMESTAMPTZ, TIMESTAMP, DATE, TIME, TIMETZ, or
character strings use the current session time zone.

The VARBYTE data type can't be implicitly converted to any other data type.
For more information, see [CAST function](r_CAST_function.md "r_CAST_function.md").
