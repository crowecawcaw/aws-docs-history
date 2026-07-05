Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SOUNDEX function

The SOUNDEX function returns the American Soundex value consisting of the first letter of the input string followed by a 3–digit encoding of the sounds that represent the English pronunciation of the string that you specify.

For example, `Smith` and `Smyth` have the same Soundex value.

## Syntax

```
SOUNDEX(*string*)
```

## Arguments

_string_

You specify a `CHAR` or `VARCHAR` string that you want to convert to an American Soundex code value.

## Return type

VARCHAR(4)

## Usage notes

The SOUNDEX function converts only English alphabetical lowercase and uppercase ASCII
characters, including a–z and A–Z. SOUNDEX ignores other characters.
SOUNDEX returns a single Soundex value for a string of multiple words separated by
spaces.

```
`SELECT SOUNDEX('AWS Amazon');`

`+---------+
| soundex |
+---------+
| A252 |
+---------+`
```

SOUNDEX returns an empty string if the input string doesn't contain any English
letters.

```
`SELECT SOUNDEX('+-*/%');`

`+---------+
| soundex |
+---------+
| |
+---------+`
```

## Examples

To return the Soundex value for `Amazon`, use the following example.

```
`SELECT SOUNDEX('Amazon');`

`+---------+
| soundex |
+---------+
| A525 |
+---------+`
```

To return the Soundex value for `smith` and `smyth`, use the following example. Note that the Soundex values are the same.

```
`SELECT SOUNDEX('smith'), SOUNDEX('smyth');`

`+-------+-------+
| smith | smyth |
+-------+-------+
| S530 | S530 |
+-------+-------+`
```
