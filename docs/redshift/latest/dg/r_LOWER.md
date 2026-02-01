Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LOWER function

Converts a string to lowercase. LOWER supports UTF-8 multibyte characters, up to a
maximum of four bytes per character.

## Syntax

```
LOWER(*string*)
```

## Argument

_string_

A `VARCHAR` string or any expression that evaluates to the `VARCHAR` type.

## Return type

string

The LOWER function returns a string that is the same data type as the input string. For example, if the input is a `CHAR` string, the function will return a `CHAR` string.

## Examples

The following example uses data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To convert the `VARCHAR` strings in the CATNAME column to lowercase, use the following example.

```
`SELECT catname, LOWER(catname) FROM category ORDER BY 1,2;`

`+-----------+-----------+
| catname | lower |
+-----------+-----------+
| Classical | classical |
| Jazz | jazz |
| MLB | mlb |
| MLS | mls |
| Musicals | musicals |
| NBA | nba |
| NFL | nfl |
| NHL | nhl |
| Opera | opera |
| Plays | plays |
| Pop | pop |
+-----------+-----------+`
```
