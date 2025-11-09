# Data types

Each value that AWS Clean Rooms Spark SQL stores or retrieves has a data type with a fixed set of
associated properties. Data types are declared when tables are created. A data type constrains
the set of values that a column or argument can contain.

The following table lists the data types that you can use in AWS Clean Rooms Spark SQL.

| Data type name | Data type                                                    | Aliases                  | Description                                                  |
| -------------- | ------------------------------------------------------------ | ------------------------ | ------------------------------------------------------------ |
| ARRAY          | [Nested type](s_Nested-data-type.md "s_Nested-data-type.md") | Not applicable           | Array nested data type                                       |
| BIGINT         | [Numeric types](Numeric_types.md "Numeric_types.md")         | Not applicable           | Signed eight-byte integer                                    |
| BINARY         | [Binary type](binary-data-type.md "binary-data-type.md")     | Not applicable           | Byte sequence values                                         |
| BOOLEAN        | [Boolean type](s_Boolean_type.md "s_Boolean_type.md")        | BOOL                     | Logical Boolean (true/false)                                 |
| BYTE           | [Numeric types](Numeric_types.md "Numeric_types.md")         | Not applicable           | 1-byte signed integer numbers, from -128 to 127              |
| CHAR           | [Character types](Character_types.md "Character_types.md")   | CHARACTER                | Fixed-length character string                                |
| DATE           | [Datetime types](Datetime_types.md "Datetime_types.md")      | Not applicable           | Calendar date (year, month, day)                             |
| DECIMAL        | [Numeric types](Numeric_types.md "Numeric_types.md")         | NUMERIC                  | Exact numeric of selectable precision                        |
| FLOAT          | [Numeric types](Numeric_types.md "Numeric_types.md")         | FLOAT8, DOUBLE PRECISION | Double precision floating-point number                       |
| INTEGER        | [Numeric types](Numeric_types.md "Numeric_types.md")         | INT                      | Signed four-byte integer                                     |
| INTERVAL       | [Datetime types](Datetime_types.md "Datetime_types.md")      | Not applicable           | Time duration in day to time order or year to month<br>order |
| LONG           | [Numeric types](Numeric_types.md "Numeric_types.md")         | Not applicable           | 8-byte signed integer numbers                                |
| MAP            | [Nested type](s_Nested-data-type.md "s_Nested-data-type.md") | Not applicable           | Map nested data type                                         |
| REAL           | [Numeric types](Numeric_types.md "Numeric_types.md")         | FLOAT4                   | Single precision floating-point number                       |
| SHORT          | [Numeric types](Numeric_types.md "Numeric_types.md")         | Not applicable           | 2-byte signed integer numbers.                               |
| SMALLINT       | [Numeric types](Numeric_types.md "Numeric_types.md")         | Not applicable           | Signed two-byte integer                                      |
| STRUCT         | [Nested type](s_Nested-data-type.md "s_Nested-data-type.md") | Not applicable           | Struct nested data type                                      |
| TIMESTAMP_LTZ  | [Datetime types](Datetime_types.md "Datetime_types.md")      | Not applicable           | Time of day with local time zone                             |
| TIMESTAMP_NTZ  | [Datetime types](Datetime_types.md "Datetime_types.md")      | Not applicable           | Time of day without time zone                                |
| TINYINT        | [Numeric types](Numeric_types.md "Numeric_types.md")         | Not applicable           | 1-byte signed integer numbers, from -128 to 127              |
| VARCHAR        | [Character types](Character_types.md "Character_types.md")   | CHARACTER VARYING        | Variable-length character string with a user-defined limit   |

###### Note

The ARRAY, STRUCT, and MAP nested data types are currently only enabled for the custom
analysis rule. For more information, see [Nested type](s_Nested-data-type.md "s_Nested-data-type.md").

## Multibyte

characters

The VARCHAR data type supports UTF-8 multibyte characters up to a maximum of four bytes.
Five-byte or longer characters are not supported. To calculate the size of a VARCHAR column
that contains multibyte characters, multiply the number of characters by the number of
bytes per character. For example, if a string has four Chinese characters, and each
character is three bytes long, then you will need a VARCHAR(12) column to store the
string.

The VARCHAR data type doesn't support the following invalid UTF-8 codepoints:

`0xD800 – 0xDFFF` (Byte sequences: `ED A0 80` –
`ED BF BF`)

The CHAR data type doesn't support multibyte characters.
