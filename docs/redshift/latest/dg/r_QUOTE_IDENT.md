Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# QUOTE_IDENT function

The QUOTE_IDENT function returns the specified string as a string with a leading double quotation mark and a trailing double quotation mark.
The function output can be used as an identifier in a SQL statement. The function appropriately doubles any
embedded double quotation marks.

QUOTE_IDENT adds double quotation marks only where necessary to create a valid identifier,
when the string contains non-identifier characters or would otherwise be folded to
lowercase. To always return a single-quoted string, use [QUOTE_LITERAL](r_QUOTE_LITERAL.md "r_QUOTE_LITERAL.md").

## Syntax

```
QUOTE_IDENT(*string*)
```

## Argument

_string_

A `CHAR` or `VARCHAR` string.

## Return type

The QUOTE_IDENT function returns the same type of string as the input _string_.

## Examples

To return the string `"CAT"` with doubled quotation
marks, use the following example.

````
`SELECT QUOTE_IDENT('"CAT"');`

`+-------------+
| quote_ident | +-------------+
| """CAT""" | +-------------+` ``` The following example uses data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md"). To return the CATNAME column surrounded by quotation marks, use the following example. ``` `SELECT catid, QUOTE_IDENT(catname) FROM category ORDER BY 1,2;` `+-------+-------------+
| catid | quote_ident | +-------+-------------+
| 1 | "MLB" |
| 2 | "NHL" |
| 3 | "NFL" |
| 4 | "NBA" |
| 5 | "MLS" |
| 6 | "Musicals" |
| 7 | "Plays" |
| 8 | "Opera" |
| 9 | "Pop" |
| 10 | "Jazz" |
| 11 | "Classical" | +-------+-------------+` ```
````
