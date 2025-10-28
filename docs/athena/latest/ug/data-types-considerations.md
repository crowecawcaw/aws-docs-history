# Considerations for data types

## Size limits

For data types that do not specify a size limit, keep in mind that there is a
practical limit of 32MB for all of the data in a single row. For more information,
see [Row or column size limitation](other-notable-limitations.md#sql-limitations-rowsize "other-notable-limitations.md#sql-limitations-rowsize") in [Considerations and limitations for SQL queries
in Amazon Athena](other-notable-limitations.md "other-notable-limitations.md").

## CHAR and VARCHAR

A `CHAR(`n`)` value always has a count of
`n` characters. For example, if you
cast 'abc' to `CHAR(7)`, 4 trailing spaces are added.

Comparisons of `CHAR` values include leading and trailing spaces.

If a length is specified for `CHAR` or `VARCHAR`, strings
are truncated at the specified length when read. If the underlying data string is
longer, the underlying data string remains unchanged.

To escape a single quote in a `CHAR` or `VARCHAR`, use an
additional single quote.

To cast a non-string data type to a string in a DML query, cast to the
`VARCHAR` data type.

To use the `substr` function to return a substring of specified length
from a `CHAR` data type, you must first cast the `CHAR` value
as a `VARCHAR`. In the following example, `col1` uses the
`CHAR` data type.

```
substr(CAST(col1 AS VARCHAR), 1, 4)
```

## DECIMAL

To specify decimal values as literals in `SELECT` queries, such as when
selecting rows with a specific decimal value, you can specify the
`DECIMAL` type and list the decimal value as a literal in single
quotes in your query, as in the following examples.

```
SELECT * FROM my_table
WHERE decimal_value = DECIMAL '0.12'
```

```
SELECT DECIMAL '44.6' + DECIMAL '77.2'
```
