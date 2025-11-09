Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# UPPER function

Converts a string to uppercase. UPPER supports UTF-8 multibyte characters, up to a
maximum of four bytes per character.

## Syntax

```
UPPER(*string*)
```

## Arguments

_string_

The input parameter is a `VARCHAR` string or any other data type, such as `CHAR`, that can be implicitly converted to `VARCHAR`.

## Return type

The UPPER function returns a character string that is the same data type as the
input string. For example, the function will return a `VARCHAR` string if the input is a `VARCHAR` string.

## Examples

The following example uses data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To convert the CATNAME field to uppercase, use the following.

```
`SELECT catname, UPPER(catname)
FROM category
ORDER BY 1,2;`

`+-----------+-----------+
| catname | upper |
+-----------+-----------+
| Classical | CLASSICAL |
| Jazz | JAZZ |
| MLB | MLB |
| MLS | MLS |
| Musicals | MUSICALS |
| NBA | NBA |
| NFL | NFL |
| NHL | NHL |
| Opera | OPERA |
| Plays | PLAYS |
| Pop | POP |
+-----------+-----------+`
```
