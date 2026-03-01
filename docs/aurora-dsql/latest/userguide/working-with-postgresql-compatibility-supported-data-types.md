# Supported data types in Aurora DSQL

Aurora DSQL supports a subset of the common PostgreSQL types.

###### Topics

- [Numeric data types](#numeric-data-types "#numeric-data-types")
- [Character data types](#character-data-types "#character-data-types")
- [Date and time data types](#date-time-data-types "#date-time-data-types")
- [Miscellaneous data types](#miscellaneous-data-types "#miscellaneous-data-types")
- [Query runtime data types](#working-with-postgresql-compatibility-query-runtime "#working-with-postgresql-compatibility-query-runtime")

## Numeric data types

Aurora DSQL supports the following PostgreSQL numeric data types.

| Name                            | Aliases                                                     | Range and precision                                                                                                                     | Storage size                                                     | Index support |
| ------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------- |
| `smallint`                      | `int2`                                                      | -32768 to +32767                                                                                                                        | 2 bytes                                                          | Yes           |
| `integer`                       | `int`, `int4`                                               | -2147483648 to +2147483647                                                                                                              | 4 bytes                                                          | Yes           |
| `bigint`                        | `int8`                                                      | -9223372036854775808 to +9223372036854775807                                                                                            | 8 bytes                                                          | Yes           |
| `real`                          | `float4`                                                    | 6 decimal digits precision                                                                                                              | 4 bytes                                                          | Yes           |
| `double precision`              | `float8`                                                    | 15 decimal digits precision                                                                                                             | 8 bytes                                                          | Yes           |
| `numeric` [ `(``p`,<br>`s``)` ] | `decimal` [ `(``p`,<br>`s``)` ]<br>`dec`[<br>`(``p`,`s``)`] | Exact numeric of selectable precision. The maximum precision is 38 and the<br>maximum scale is 37.1 The default is `numeric<br>(18,6)`. | 8 bytes + 2 bytes per precision digit. Maximum size is 27 bytes. | Yes           |

1 – If you don't explicitly specify a size when you run
`CREATE TABLE` or `ALTER TABLE ADD COLUMN`, Aurora DSQL enforces the
defaults. Aurora DSQL applies limits when you run `INSERT` or `UPDATE`
statements.

## Character data types

Aurora DSQL supports the following PostgreSQL character data types.

| Name                                 | Aliases                    | Description                                                                                                                                                   | Aurora DSQL limit | Storage size               | Index support |
| ------------------------------------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------------------------- | ------------- |
| `character` [<br>`(``n``)` ]         | `char` [ `(``n``)`<br>]    | Fixed-length character string                                                                                                                                 | 4096 bytes1       | Variable up to 4100 bytes  | Yes           |
| `character varying` [<br>`(``n``)` ] | `varchar` [<br>`(``n``)` ] | Variable-length character string                                                                                                                              | 65535 bytes1      | Variable up to 65539 bytes | Yes           |
| `bpchar` [<br>`(``n``)` ]            |                            | If fixed length, this is an alias for `char`. If variable length,<br>this is an alias for `varchar`, where trailing spaces are<br>semantically insignificant. | 4096 bytes1       | Variable up to 4100 bytes  | Yes           |
| `text`                               |                            | Variable-length character string                                                                                                                              | 1 MiB1            | Variable up to 1 MiB       | Yes           |

1 – If you don't explicitly specify a size when you run
`CREATE TABLE` or `ALTER TABLE ADD COLUMN`, then Aurora DSQL enforces
the defaults. Aurora DSQL applies limits when you run `INSERT` or
`UPDATE` statements.

## Date and time data types

Aurora DSQL supports the following PostgreSQL date and time data types.

| Name                                                    | Aliases       | Description                        | Range                              | Resolution    | Storage size | Index support |
| ------------------------------------------------------- | ------------- | ---------------------------------- | ---------------------------------- | ------------- | ------------ | ------------- |
| `date`                                                  |               | Calendar date (year, month, day)   | 4713 BC – 5874897 AD               | 1 day         | 4 bytes      | Yes           |
| `time` [ `(``p``)`<br>] [ `without time zone` ]         | `timestamp`   | Time of day, with no time zone     | 0 – 1                              | 1 microsecond | 8 bytes      | Yes           |
| `time` [ `(``p``)`<br>] `with time zone`                | `timetz`      | time of day, including time zone   | 00:00:00+1559 – 24:00:00 –1559     | 1 microsecond | 12 bytes     | No            |
| `timestamp` [<br>`(``p``)` ] [ `without<br>time zone` ] |               | Date and time, with no time zone   | 4713 BC – 294276 AD                | 1 microsecond | 8 bytes      | Yes           |
| `timestamp` [<br>`(``p``)` ] `with time<br>zone`        | `timestamptz` | Date and time, including time zone | 4713 BC – 294276 AD                | 1 microsecond | 8 bytes      | Yes           |
| `interval` [ `fields` ] [<br>`(``p``)` ]                |               | Time span                          | -178000000 years – 178000000 years | 1 microsecond | 16 bytes     | No            |

## Miscellaneous data types

Aurora DSQL supports the following miscellaneous PostgreSQL data types.

| Name      | Aliases | Description                   | Aurora DSQL limit | Storage size               | Index support |
| --------- | ------- | ----------------------------- | ----------------- | -------------------------- | ------------- |
| `boolean` | `bool`  | Logical Boolean (true/false)  |                   | 1 byte                     | Yes           |
| `bytea`   |         | Binary data ("byte array")    | 1 MiB1            | Variable up to 1 MiB limit | No            |
| `UUID`    |         | Universally unique identifier |                   | 16 bytes                   | Yes           |

1 – If you don't explicitly specify a size when you run
`CREATE TABLE` or `ALTER TABLE ADD COLUMN`, then Aurora DSQL enforces
the defaults. Aurora DSQL applies limits when you run `INSERT` or
`UPDATE` statements.

## Query runtime data types

Query runtime data types are internal data types used at query execution time. These
types are distinct from the PostgreSQL-compatible types like `varchar` and
`integer` that you define in your schema. Instead, these types are runtime
representations that Aurora DSQL uses when processing a query.

The following data types are supported only during query runtime:

**Array type**

Aurora DSQL supports arrays of the supported data types. For example, you can have an
array of integers. The function `string_to_array` splits a string into a
PostgreSQL-style array with the comma delimiter (`,`) as shown in the following example.
You can use arrays in expressions, function outputs, or temporary computations during query
execution.

```
SELECT string_to_array('1,2', ',');
```

The function returns a response similar to the following:

```
 string_to_array
-----------------
 {1,2}
(1 row)
```

\***\*inet type\*\***

The data type represents IPv4, IPv6 host addresses, and their subnets. This type
is useful when parsing logs, filtering on IP subnets, or doing network calculations
within a query. For more information, see [inet in the PostgreSQL documentation](https://www.PostgreSQL.org/docs/16/datatype-net-types.html#DATATYPE-INET "https://www.PostgreSQL.org/docs/16/datatype-net-types.html#DATATYPE-INET").

**JSON runtime functions**

Aurora DSQL supports JSON and JSONB as runtime data types for query processing. Store JSON data as `text` columns and cast to JSON during query execution to use PostgreSQL JSON functions and operators.

Aurora DSQL supports most PostgreSQL JSON functions from [section 9.1.6 JSON Functions and Operators](https://www.postgresql.org/docs/current/functions-json.html "https://www.postgresql.org/docs/current/functions-json.html") with identical behavior.

Functions that return JSON or JSONB types may require additional casting to `text` for proper display.

```
SELECT json_build_array(1, 2, 'foo', 4, 5)::text;
```

The function returns a response similar to the following:

```
     json_build_array
 ---------------------
   [1, 2, "foo", 4, 5]
 (1 row)
```
