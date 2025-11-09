Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CHR function

The CHR function returns the character that matches the ASCII code point value
specified by the input parameter.

## Syntax

```
CHR(*number*)
```

## Argument

_number_

The input parameter is an `INTEGER` that represents an ASCII code point value.

## Return type

CHAR

The CHR function returns a `CHAR` string if an ASCII character matches the input
value. If the input number has no ASCII match, the function returns `NULL`.

## Examples

To return the character that corresponds with ASCII code point 0, use the following example. Note that the CHR function returns `NULL` for the input `0`.

```
`SELECT CHR(0);`

`+-----+
| chr |
+-----+
| |
+-----+`
```

To return the character that corresponds with ASCII code point 65, use the following example.

```
`SELECT CHR(65);`

`+-----+
| chr |
+-----+
| A |
+-----+`
```

To return distinct event names that begin with a capital A (ASCII code point 65), use the following example. The following example uses the EVENT table from the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

```
`SELECT DISTINCT eventname FROM event
WHERE SUBSTRING(eventname, 1, 1)=CHR(65) LIMIT 5;`

`+-----------------------+
| eventname |
+-----------------------+
| A Catered Affair |
| As You Like It |
| A Man For All Seasons |
| Alan Jackson |
| Armando Manzanero |
+-----------------------+`
```
