# REPLACE function

Replaces all occurrences of a set of characters within an existing string with other
specified characters.

REPLACE is similar to the [TRANSLATE function](r_TRANSLATE.md "r_TRANSLATE.md") and
the [REGEXP_REPLACE function](r_REGEXP_REPLACE.md "r_REGEXP_REPLACE.md"), except that TRANSLATE
makes multiple single-character substitutions and REGEXP_REPLACE lets you search a string
for a regular expression pattern, while REPLACE substitutes one entire string with another
string.

## Syntax

```
REPLACE(*string*1, *old\_chars*, *new\_chars*)
```

## Arguments

_string_

CHAR or VARCHAR string to be searched search

_old_chars_

CHAR or VARCHAR string to replace.

_new_chars_

New CHAR or VARCHAR string replacing the _old_string_.

## Return type

VARCHAR

If either _old_chars_ or _new_chars_ is NULL,
the return is NULL.

## Examples

The following example converts the string `Shows` to `Theatre`
in the CATGROUP field:

```
select catid, catgroup,
replace(catgroup, 'Shows', 'Theatre')
from category
order by 1,2,3;

 catid | catgroup | replace
-------+----------+----------
     1 | Sports   | Sports
     2 | Sports   | Sports
     3 | Sports   | Sports
     4 | Sports   | Sports
     5 | Sports   | Sports
     6 | Shows    | Theatre
     7 | Shows    | Theatre
     8 | Shows    | Theatre
     9 | Concerts | Concerts
    10 | Concerts | Concerts
    11 | Concerts | Concerts
(11 rows)
```
