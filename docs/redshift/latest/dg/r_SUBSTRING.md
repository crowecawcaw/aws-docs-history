Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SUBSTRING function

Returns the subset of a string based on the specified start position.

If the input is a character string, the start position and number of characters extracted are based on
characters, not bytes, so that multi-byte characters are counted as single characters.
If the input is a binary expression, the start position and extracted substring are based on bytes.
You can't specify a negative length, but you can specify a negative starting
position.

## Syntax

```
SUBSTRING(*character\_string* FROM *start\_position* [ FOR *number\_characters* ] )
```

```
SUBSTRING(*character\_string*, *start\_position*, *number\_characters* )
```

```
SUBSTRING(*binary\_expression*, *start\_byte*, *number\_bytes* )
```

```
SUBSTRING(*binary\_expression*, *start\_byte* )
```

## Arguments

_character_string_

The string to be searched. Non-character data types are treated like a
string.

_start_position_

The position within the string to begin the extraction, starting at 1.
The _start_position_ is based on the number of
characters, not bytes, so that multi-byte characters are counted as single
characters. This number can be negative.

_number_characters_

The number of characters to extract (the length of the substring). The
_number_characters_ is based on the number of
characters, not bytes, so that multi-byte characters are counted as single
characters. This number cannot be negative.

_binary_expression_

The binary_expression of data type VARBYTE to be searched.

_start_byte_

The position within the binary expression to begin the extraction, starting at 1.
This number can be negative.

_number_bytes_

The number of bytes to extract, that is, the length of the substring.
This number can't be negative.

## Return type

VARCHAR or VARBYTE depending on the input.

## Usage Notes

Following are some examples of how you can use _start_position_ and _number_characters_ to extract substrings from various positions in a string.

The following example returns a four-character string beginning with the sixth
character.

```
select substring('caterpillar',6,4);
substring
-----------
pill
(1 row)
```

If the _start_position_ +
_number_characters_ exceeds the length of the
_string_, SUBSTRING returns a substring starting from the
_start_position_ until the end of the string. For example:

```
select substring('caterpillar',6,8);
substring
-----------
pillar
(1 row)
```

If the `start_position` is negative or 0, the SUBSTRING function
returns a substring beginning at the first character of string with a length of
`start_position` + `number_characters` -1. For
example:

```
select substring('caterpillar',-2,6);
substring
-----------
cat
(1 row)
```

If `start_position` + `number_characters` -1 is less than or
equal to zero, SUBSTRING returns an empty string. For example:

```
select substring('caterpillar',-5,4);
substring
-----------

(1 row)
```

## Examples

The following example returns the month from the LISTTIME string in the LISTING
table:

```
select listid, listtime,
substring(listtime, 6, 2) as month
from listing
order by 1, 2, 3
limit 10;

 listid |      listtime       | month
--------+---------------------+-------
      1 | 2008-01-24 06:43:29 | 01
      2 | 2008-03-05 12:25:29 | 03
      3 | 2008-11-01 07:35:33 | 11
      4 | 2008-05-24 01:18:37 | 05
      5 | 2008-05-17 02:29:11 | 05
      6 | 2008-08-15 02:08:13 | 08
      7 | 2008-11-15 09:38:15 | 11
      8 | 2008-11-09 05:07:30 | 11
      9 | 2008-09-09 08:03:36 | 09
     10 | 2008-06-17 09:44:54 | 06
(10 rows)
```

The following example is the same as above, but uses the FROM...FOR option:

```
select listid, listtime,
substring(listtime from 6 for 2) as month
from listing
order by 1, 2, 3
limit 10;

 listid |      listtime       | month
--------+---------------------+-------
      1 | 2008-01-24 06:43:29 | 01
      2 | 2008-03-05 12:25:29 | 03
      3 | 2008-11-01 07:35:33 | 11
      4 | 2008-05-24 01:18:37 | 05
      5 | 2008-05-17 02:29:11 | 05
      6 | 2008-08-15 02:08:13 | 08
      7 | 2008-11-15 09:38:15 | 11
      8 | 2008-11-09 05:07:30 | 11
      9 | 2008-09-09 08:03:36 | 09
     10 | 2008-06-17 09:44:54 | 06
(10 rows)
```

You can't use SUBSTRING to predictably extract the prefix of a string that might
contain multi-byte characters because you need to specify the length of a multi-byte
string based on the number of bytes, not the number of characters. To extract the
beginning segment of a string based on the length in bytes, you can CAST the string
as VARCHAR(_byte_length_) to truncate the string,
where _byte_length_ is the required length. The
following example extracts the first 5 bytes from the string `'Fourscore and
 seven'`.

```
select cast('Fourscore and seven' as varchar(5));

varchar
-------
Fours
```

The following example shows a negative start position of a binary value `abc`.
Because the start position is -3, the substring is extracted from the beginning of the binary value.
The result is automatically shown as the hexadecimal representation of the binary substring.

```
select substring('abc'::varbyte, -3);

 substring
-----------
 616263
```

The following example shows a 1 for the start position of a binary value `abc`.
Because because there is no length specified, the string is extracted from the start position to the end of the string.
The result is automatically shown as the hexadecimal representation of the binary substring.

```
select substring('abc'::varbyte, 1);

 substring
-----------
 616263
```

The following example shows a 3 for the start position of a binary value `abc`.
Because because there is no length specified, the string is extracted from the start position to the end of the string.
The result is automatically shown as the hexadecimal representation of the binary substring.

```
select substring('abc'::varbyte, 3);

 substring
-----------
 63
```

The following example shows a 2 for the start position of a binary value `abc`.
The string is extracted from the start position to position 10, but the end of the string is at position 3.
The result is automatically shown as the hexadecimal representation of the binary substring.

```
select substring('abc'::varbyte, 2, 10);

 substring
-----------
 6263
```

The following example shows a 2 for the start position of a binary value `abc`.
The string is extracted from the start position for 1 byte.
The result is automatically shown as the hexadecimal representation of the binary substring.

```
select substring('abc'::varbyte, 2, 1);

 substring
-----------
 62
```

The following example returns the first name `Ana` which appears after the last space in the input string `Silva, Ana`.

```
`select reverse(substring(reverse('Silva, Ana'), 1, position(' ' IN reverse('Silva, Ana'))))`
`reverse
-----------
 Ana`
```
