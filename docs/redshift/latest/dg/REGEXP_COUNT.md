Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# REGEXP_COUNT function

Searches a string for a regular expression pattern and returns an integer that
indicates the number of times the specified pattern occurs in the string. If no match is found,
then the function returns `0`. For more information about regular expressions, see [POSIX operators](pattern-matching-conditions-posix.md "pattern-matching-conditions-posix.md") and
[Regular expression](https://en.wikipedia.org/wiki/Regular_expression "https://en.wikipedia.org/wiki/Regular_expression") in Wikipedia.

## Syntax

```
REGEXP_COUNT( *source\_string*, *pattern* [, *position* [, *parameters* ] ] )
```

## Arguments

_source_string_

A `CHAR` or `VARCHAR` string.

_pattern_

A UTF-8 string literal that represents a regular expression pattern. For more information, see
[POSIX operators](pattern-matching-conditions-posix.md "pattern-matching-conditions-posix.md").

_position_

(Optional) A positive `INTEGER` that indicates the position within
_source_string_ to begin searching. The position is
based on the number of characters, not bytes, so that multibyte characters
are counted as single characters. The default is `1`. If
_position_ is less than `1`, the search begins at the
first character of _source_string_. If
_position_ is greater than the number of characters in
_source_string_, the result is `0`.

_parameters_

(Optional) One or more string literals that indicate how the function matches the
pattern. The possible values are the following:

- c – Perform case-sensitive matching. The default is to use
  case-sensitive matching.
- i – Perform case-insensitive matching.
- p – Interpret the pattern with Perl Compatible Regular Expression (PCRE) dialect.
  For more information about PCRE, see
  [Perl Compatible Regular Expressions](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions "https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions") in Wikipedia.

## Return type

INTEGER

## Examples

To count the number of times a three-letter sequence
occurs, use the following example.

```
`SELECT REGEXP_COUNT('abcdefghijklmnopqrstuvwxyz', '[a-z]{3}');`

`+--------------+
| regexp_count |
+--------------+
| 8 |
+--------------+`
```

To count the occurrences of the string `FOX` using case-insensitive matching, use the following example.

```
`SELECT REGEXP_COUNT('the fox', 'FOX', 1, 'i');`

`+--------------+
| regexp_count |
+--------------+
| 1 |
+--------------+`
```

To use a pattern written in the PCRE dialect to locate words
containing at least one number and one lowercase letter, use the following example. The example uses the
`?=` operator, which has a specific look-ahead connotation in PCRE. This example counts the
number of occurrences of such words, with case-sensitive matching.

```
`SELECT REGEXP_COUNT('passwd7 plain A1234 a1234', '(?=[^ ]*[a-z])(?=[^ ]*[0-9])[^ ]+', 1, 'p');`

`+--------------+
| regexp_count |
+--------------+
| 2 |
+--------------+`
```

To use a pattern written in the PCRE dialect to locate words
containing at least one number and one lowercase letter, use the following example. It uses the
`?=` operator, which has a specific connotation in PCRE. This example counts the
number of occurrences of such words, but differs from the previous example in that it uses case-insensitive matching.

```
`SELECT REGEXP_COUNT('passwd7 plain A1234 a1234', '(?=[^ ]*[a-z])(?=[^ ]*[0-9])[^ ]+', 1, 'ip');`

`+--------------+
| regexp_count |
+--------------+
| 3 |
+--------------+`
```

The following example uses data from the USERS table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To count the number of times the top-level domain name is
either `org` or `edu`, use the following example.

```
`SELECT email, REGEXP_COUNT(email,'@[^.]*\.(org|edu)') FROM users
ORDER BY userid LIMIT 4;`

`+-----------------------------------------------+--------------+
| email | regexp_count |
+-----------------------------------------------+--------------+
| Etiam.laoreet.libero@sodalesMaurisblandit.edu | 1 |
| Suspendisse.tristique@nonnisiAenean.edu | 1 |
| amet.faucibus.ut@condimentumegetvolutpat.ca | 0 |
| sed@lacusUtnec.ca | 0 |
+-----------------------------------------------+--------------+`
```
