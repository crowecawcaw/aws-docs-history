Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# BTRIM function

The BTRIM function trims a string by removing leading and trailing blanks or by
removing leading and trailing characters that match an optional specified string.

## Syntax

```
BTRIM(*string* [, *trim\_chars* ] )
```

## Arguments

_string_

The input VARCHAR string to be trimmed.

_trim_chars_

The VARCHAR string containing the characters to be matched.

## Return type

The BTRIM function returns a VARCHAR string.

## Examples

The following example trims leading and trailing blanks from the string `'
 abc '`:

```
`select ' abc ' as untrim, btrim(' abc ') as trim;`
`untrim | trim
----------+------
 abc | abc`
```

The following example removes the leading and trailing `'xyz'` strings
from the string `'xyzaxyzbxyzcxyz'`.
The leading and trailing occurrences of `'xyz'` are removed,
but occurrences that are internal within the string are not removed.

```
`select 'xyzaxyzbxyzcxyz' as untrim,
btrim('xyzaxyzbxyzcxyz', 'xyz') as trim;`
`untrim | trim
-----------------+-----------
 xyzaxyzbxyzcxyz | axyzbxyzc`
```

The following example removes the leading and trailing parts
from the string `'setuphistorycassettes'` that match any of the characters in the _trim_chars_ list `'tes'`.
Any `t`, `e`, or `s` that occur before another character that is not in the _trim_chars_ list at the beginning or ending of the input string are removed.

```
`SELECT btrim('setuphistorycassettes', 'tes');`
`btrim
-----------------
 uphistoryca`
```
