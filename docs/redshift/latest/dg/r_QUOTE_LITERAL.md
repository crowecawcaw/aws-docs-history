Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# QUOTE_LITERAL function

The QUOTE_LITERAL function returns the specified string as a single quoted string so that it
can be used as a string literal in a SQL statement. If the input parameter is a number,
QUOTE_LITERAL treats it as a string. Appropriately doubles any embedded single quotation marks
and backslashes.

## Syntax

```
QUOTE_LITERAL(*string*)
```

## Argument

_string_

A `CHAR` or `VARCHAR` string.

## Return type

The QUOTE_LITERAL function returns a `CHAR` or `VARCHAR` string that is the same data type as the
input _string_.

## Examples

To return the string `''CAT''` with SINGLE quotation
marks, use the following example.

```
`SELECT QUOTE_LITERAL('''CAT''');`

`+---------------+
| quote_literal |
+---------------+
| '''CAT''' |
+---------------+`
```

The following examples use data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To return the CATNAME column surrounded by single quotation
marks, use the following example.

```
`SELECT catid, QUOTE_LITERAL(catname)
FROM category
ORDER BY 1,2;`

`+-------+---------------+
| catid | quote_literal |
+-------+---------------+
| 1 | 'MLB' |
| 2 | 'NHL' |
| 3 | 'NFL' |
| 4 | 'NBA' |
| 5 | 'MLS' |
| 6 | 'Musicals' |
| 7 | 'Plays' |
| 8 | 'Opera' |
| 9 | 'Pop' |
| 10 | 'Jazz' |
| 11 | 'Classical' |
+-------+---------------+`
```

To return the CATID column surrounded by single quotation
marks, use the following example.

```
`SELECT QUOTE_LITERAL(catid), catname
FROM category
ORDER BY 1,2;`

`+---------------+-----------+
| quote_literal | catname |
+---------------+-----------+
| '1' | MLB |
| '10' | Jazz |
| '11' | Classical |
| '2' | NHL |
| '3' | NFL |
| '4' | NBA |
| '5' | MLS |
| '6' | Musicals |
| '7' | Plays |
| '8' | Opera |
| '9' | Pop |
+---------------+-----------+`
```
