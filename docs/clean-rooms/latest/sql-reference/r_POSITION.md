# POSITION function

Returns the location of the specified substring within a string.

See [CHARINDEX function](r_CHARINDEX.md "r_CHARINDEX.md") and [STRPOS function](r_STRPOS.md "r_STRPOS.md") for similar functions.

## Syntax

```
POSITION(*substring* IN *string* )
```

## Arguments

_substring_

The substring to search for within the _string_.

_string_

The string or column to be searched.

## Return type

The POSITION function returns an integer corresponding to the position of the
substring (one-based, not zero-based). The position is based on the number of
characters, not bytes, so that multi-byte characters are counted as single
characters.

## Usage notes

POSITION returns 0 if the substring is not found within the string:

```
select position('dog' in 'fish');

position
----------
 0
(1 row)

```

## Examples

The following example shows the position of the string `fish` within the
word `dogfish`:

```
select position('fish' in 'dogfish');

position
----------
 4
(1 row)

```

The following example returns the number of sales transactions with a COMMISSION over
999.00 from the SALES table:

```
select distinct position('.' in commission), count (position('.' in commission))
from sales where position('.' in commission) > 4 group by position('.' in commission)
order by 1,2;

position | count
---------+-------
       5 |    629
(1 row)

```
