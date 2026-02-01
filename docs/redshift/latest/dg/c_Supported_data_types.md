Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data types

###### Topics

- [Multibyte
  characters](#c_Supported_data_types-multi-byte-characters "#c_Supported_data_types-multi-byte-characters")
- [Numeric types](r_Numeric_types201.md "r_Numeric_types201.md")
- [Character types](r_Character_types.md "r_Character_types.md")
- [Datetime types](r_Datetime_types.md "r_Datetime_types.md")
- [Boolean type](r_Boolean_type.md "r_Boolean_type.md")
- [HLLSKETCH type](r_HLLSKTECH_type.md "r_HLLSKTECH_type.md")
- [SUPER type](r_SUPER_type.md "r_SUPER_type.md")
- [VARBYTE type](r_VARBYTE_type.md "r_VARBYTE_type.md")
- [Type compatibility and conversion](#r_Type_conversion "#r_Type_conversion")
  Each value that Amazon Redshift stores or retrieves has a data type with a fixed set of
  associated properties. Data types are declared when tables are created. A data type
  constrains the set of values that a column or argument can contain.

The following table lists the data types that you can use in Amazon Redshift tables.

| Data type              | Aliases                           | Description                                                                                                                     |
| ---------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| SMALLINT               | INT2                              | Signed two-byte integer                                                                                                         |
| INTEGER                | INT, INT4                         | Signed four-byte integer                                                                                                        |
| BIGINT                 | INT8                              | Signed eight-byte integer                                                                                                       |
| DECIMAL                | NUMERIC                           | Exact numeric of selectable precision                                                                                           |
| REAL                   | FLOAT4                            | Single precision floating-point number                                                                                          |
| DOUBLE PRECISION       | FLOAT8, FLOAT                     | Double precision floating-point number                                                                                          |
| CHAR                   | CHARACTER, NCHAR, BPCHAR          | Fixed-length character string                                                                                                   |
| VARCHAR                | CHARACTER VARYING, NVARCHAR, TEXT | Variable-length character string with a user-defined<br>limit                                                                   |
| DATE                   |                                   | Calendar date (year, month, day)                                                                                                |
| TIME                   | TIME WITHOUT TIME ZONE            | Time of day                                                                                                                     |
| TIMETZ                 | TIME WITH TIME ZONE               | Time of day with time zone                                                                                                      |
| TIMESTAMP              | TIMESTAMP WITHOUT TIME ZONE       | Date and time (without time zone)                                                                                               |
| TIMESTAMPTZ            | TIMESTAMP WITH TIME ZONE          | Date and time (with time zone)                                                                                                  |
| INTERVAL YEAR TO MONTH |                                   | Time duration in year to month order                                                                                            |
| INTERVAL DAY TO SECOND |                                   | Time duration in day to second order                                                                                            |
| BOOLEAN                | BOOL                              | Logical Boolean (true/false)                                                                                                    |
| HLLSKETCH              |                                   | Type used with HyperLogLog sketches.                                                                                            |
| SUPER                  |                                   | A superset data type that encompasses all scalar types<br>of Amazon Redshift including complex types such as ARRAY and STRUCTS. |
| VARBYTE                | VARBINARY, BINARY VARYING         | Variable-length binary value                                                                                                    |
| GEOMETRY               |                                   | Spatial data                                                                                                                    |
| GEOGRAPHY              |                                   | Spatial data                                                                                                                    |

###### Note

For information about unsupported data types, such as "char" (notice that char
is enclosed in quotation marks), see [Unsupported PostgreSQL data
types](c_unsupported-postgresql-datatypes.md "c_unsupported-postgresql-datatypes.md").

## Multibyte

characters

The VARCHAR data type supports UTF-8 multibyte characters up to a maximum of
four bytes. Five-byte or longer characters are not supported. To calculate the
size of a VARCHAR column that contains multibyte characters, multiply the number
of characters by the number of bytes per character. For example, if a string has
four Chinese characters, and each character is three bytes long, then you will
need a VARCHAR(12) column to store the string.

The VARCHAR data type doesn't support the following invalid UTF-8
codepoints:

`0xD800 – 0xDFFF` (Byte sequences: `ED A0 80`
– `ED BF BF`)

The CHAR data type doesn't support multibyte characters.

## Type compatibility and conversion

Following, you can find a discussion about how type conversion rules and data
type compatibility work in Amazon Redshift.

### Compatibility

Data type matching and matching of literal values and constants to data
types occurs during various database operations, including the following:

- Data manipulation language (DML) operations on tables
- UNION, INTERSECT, and EXCEPT queries
- CASE expressions
- Evaluation of predicates, such as LIKE and IN
- Evaluation of SQL functions that do comparisons or extractions of data
- Comparisons with mathematical operators

The results of these operations depend on type conversion rules and data
type compatibility. _Compatibility_ implies that a
one-to-one matching of a certain value and a certain data type is not always
required. Because some data types are _compatible_, an
implicit conversion, or _coercion_, is possible (for more
information, see [Implicit conversion types](#implicit-conversion-types "#implicit-conversion-types")). When data types are
incompatible, you can sometimes convert a value from one data type to another
by using an explicit conversion function.

### General compatibility and conversion rules

Note the following compatibility and conversion rules:

- In general, data types that fall into the same type category (such as
  different numeric data types) are compatible and can be implicitly
  converted.

For example, with implicit conversion you can insert a decimal value
into an integer column. The decimal is rounded to produce a whole number.
Or you can extract a numeric value, such as `2008`, from a
date and insert that value into an integer column.

- Numeric data types enforce overflow conditions that occur when you
  attempt to insert out-of-range values. For example, a decimal value with
  a precision of 5 does not fit into a decimal column that was defined with
  a precision of 4. An integer or the whole part of a decimal is never
  truncated; however, the fractional part of a decimal can be rounded up or
  down, as appropriate. However, results of explicit casts of values
  selected from tables are not rounded.
- Different types of character strings are compatible; VARCHAR column
  strings containing single-byte data and CHAR column strings are
  comparable and implicitly convertible. VARCHAR strings that contain
  multibyte data are not comparable. Also, you can convert a character
  string to a date, time, timestamp, or numeric value if the string is an
  appropriate literal value; any leading or trailing spaces are ignored.
  Conversely, you can convert a date, time, timestamp, or numeric value to
  a fixed-length or variable-length character string.

###### Note

A character string that you want to cast to a numeric type must
contain a character representation of a number. For example, you can
cast the strings `'1.0'` or `'5.9'` to decimal
values, but you cannot cast the string `'ABC'` to any
numeric type.

- If you compare DECIMAL values with character strings, Amazon Redshift attempts to
  convert the character string to a DECIMAL value. When comparing all other
  numeric values with character strings, the numeric values are converted
  to character strings. To enforce the opposite conversion (for example,
  converting character strings to integers, or converting DECIMAL values to
  character strings), use an explicit function, such as [CAST](r_CAST_function.md "r_CAST_function.md").
- To convert 64-bit DECIMAL or NUMERIC values to a higher precision, you
  must use an explicit conversion function such as the CAST or CONVERT
  functions.
- When converting DATE or TIMESTAMP to TIMESTAMPTZ, or converting TIME
  to TIMETZ, the time zone is set to the current session time zone. The
  session time zone is UTC by default. For more information about setting
  the session time zone, see [timezone](r_timezone_config.md "r_timezone_config.md").
- Similarly, TIMESTAMPTZ is converted to DATE, TIME, or TIMESTAMP based
  on the current session time zone. The session time zone is UTC by
  default. After the conversion, time zone information is dropped.
- Character strings that represent a timestamp with time zone specified
  are converted to TIMESTAMPTZ using the current session time zone, which
  is UTC by default. Likewise, character strings that represent a time with
  time zone specified are converted to TIMETZ using the current session
  time zone, which is UTC by default.

### Implicit conversion types

There are two types of implicit conversions:

- Implicit conversions in assignments, such as setting values in INSERT
  or UPDATE commands.
- Implicit conversions in expressions, such as performing comparisons in
  the WHERE clause.

The table following lists the data types that can be converted implicitly in
assignments or expressions. You can also use an explicit conversion function to
perform these conversions.

| From type                 | To type       |
| ------------------------- | ------------- |
| BIGINT (INT8)             | BOOLEAN       |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| DOUBLE PRECISION (FLOAT8) |
| INTEGER (INT, INT4)       |
| REAL (FLOAT4)             |
| SMALLINT (INT2)           |
| VARCHAR                   |
| CHAR                      | VARCHAR       |
| DATE                      | CHAR          |
| VARCHAR                   |
| TIMESTAMP                 |
| TIMESTAMPTZ               |
| DECIMAL (NUMERIC)         | BIGINT (INT8) |
| CHAR                      |
| DOUBLE PRECISION (FLOAT8) |
| INTEGER (INT, INT4)       |
| REAL (FLOAT4)             |
| SMALLINT (INT2)           |
| VARCHAR                   |
| DOUBLE PRECISION (FLOAT8) | BIGINT (INT8) |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| INTEGER (INT, INT4)       |
| REAL (FLOAT4)             |
| SMALLINT (INT2)           |
| VARCHAR                   |
| INTEGER (INT, INT4)       | BIGINT (INT8) |
| BOOLEAN                   |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| DOUBLE PRECISION (FLOAT8) |
| REAL (FLOAT4)             |
| SMALLINT (INT2)           |
| VARCHAR                   |
| REAL (FLOAT4)             | BIGINT (INT8) |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| INTEGER (INT, INT4)       |
| SMALLINT (INT2)           |
| VARCHAR                   |
| SMALLINT (INT2)           | BIGINT (INT8) |
| BOOLEAN                   |
| CHAR                      |
| DECIMAL (NUMERIC)         |
| DOUBLE PRECISION (FLOAT8) |
| INTEGER (INT, INT4)       |
| REAL (FLOAT4)             |
| VARCHAR                   |
| TIMESTAMP                 | CHAR          |
| DATE                      |
| VARCHAR                   |
| TIMESTAMPTZ               |
| TIME                      |
| TIMESTAMPTZ               | CHAR          |
| DATE                      |
| VARCHAR                   |
| TIMESTAMP                 |
| TIMETZ                    |
| TIME                      | VARCHAR       |
| TIMETZ                    |
| INTERVAL DAY TO SECOND    |
| TIMETZ                    | VARCHAR       |
| TIME                      |
| GEOMETRY                  | GEOGRAPHY     |
| GEOGRAPHY                 | GEOMETRY      |

###### Note

Implicit conversions between TIMESTAMPTZ, TIMESTAMP, DATE, TIME, TIMETZ,
or character strings use the current session time zone. For information
about setting the current time zone, see [timezone](r_timezone_config.md "r_timezone_config.md").

The GEOMETRY and GEOGRAPHY data types can't be implicitly converted
to any other data type, except each other. For more information, see [CAST function](r_CAST_function.md "r_CAST_function.md").

The VARBYTE data type can't be implicitly converted to any other
data type. For more information, see [CAST function](r_CAST_function.md "r_CAST_function.md").

### Using dynamic typing for the SUPER

data type

Amazon Redshift uses dynamic typing to process schemaless SUPER data without the
need to declare the data types before you use them in your query. Dynamic
typing uses the results of navigating into SUPER data columns without having to
explicitly cast them into Amazon Redshift types. For more information about using
dynamic typing for SUPER data type, see [Dynamic typing](query-super.md#dynamic-typing-lax-processing "query-super.md#dynamic-typing-lax-processing").

You can cast SUPER values to and from other data types with some exceptions.
For more information, see [Limitations](limitations-super.md "limitations-super.md").
