Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# BPCHARCMP function

Compares the value of two strings and returns an integer. If the strings are
identical, the function returns `0`. If the first string is greater alphabetically, the function returns `1`. If the
second string is greater, the function returns `-1`.

For multibyte characters, the comparison is based on the byte encoding.

Synonym of [BTTEXT_PATTERN_CMP function](r_BTTEXT_PATTERN_CMP.md "r_BTTEXT_PATTERN_CMP.md").

## Syntax

```
BPCHARCMP(*string1*, *string2*)
```

## Arguments

_string1_

A `CHAR` string or a `VARCHAR` string.

_string2_

A `CHAR` string or a `VARCHAR` string.

## Return type

INTEGER

## Examples

The following examples use the USERS table from the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To determine whether a user's first name is alphabetically
greater than the user's last name for the first ten entries in the USERS table, use the following example. For entries where the string for FIRSTNAME is later
alphabetically than the string for LASTNAME, the function returns `1`. If the LASTNAME is
alphabetically later than FIRSTNAME, the function returns `-1`.

````
`SELECT userid, firstname, lastname, BPCHARCMP(firstname, lastname)
FROM users
ORDER BY 1, 2, 3, 4
LIMIT 10;`

`+--------+-----------+-----------+-----------+
| userid | firstname | lastname | bpcharcmp | +--------+-----------+-----------+-----------+
| 1 | Rafael | Taylor | -1 |
| 2 | Vladimir | Humphrey | 1 |
| 3 | Lars | Ratliff | -1 |
| 4 | Barry | Roy | -1 |
| 5 | Reagan | Hodge | 1 |
| 6 | Victor | Hernandez | 1 |
| 7 | Tamekah | Juarez | 1 |
| 8 | Colton | Roy | -1 |
| 9 | Mufutau | Watkins | -1 |
| 10 | Naida | Calderon | 1 | +--------+-----------+-----------+-----------+` ``` To return all entries in the USERS table where the function returns `0`, use the following example. The function returns `0` when FIRSTNAME is identical to LASTNAME. ``` `SELECT userid, firstname, lastname, BPCHARCMP(firstname, lastname) FROM users WHERE BPCHARCMP(firstname, lastname)=0 ORDER BY 1, 2, 3, 4;` `+--------+-----------+----------+-----------+
| userid | firstname | lastname | bpcharcmp | +--------+-----------+----------+-----------+
| 62 | Chase | Chase | 0 |
| 4008 | Whitney | Whitney | 0 |
| 12516 | Graham | Graham | 0 |
| 13570 | Harper | Harper | 0 |
| 16712 | Cooper | Cooper | 0 |
| 18359 | Chase | Chase | 0 |
| 27530 | Bradley | Bradley | 0 |
| 31204 | Harding | Harding | 0 | +--------+-----------+----------+-----------+` ```
````
