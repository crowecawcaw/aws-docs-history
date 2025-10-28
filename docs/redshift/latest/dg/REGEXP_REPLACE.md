Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# REGEXP_REPLACE function

Searches a string for a regular expression pattern and replaces every occurrence of
the pattern with the specified string. REGEXP_REPLACE is similar to the [REPLACE function](r_REPLACE.md "r_REPLACE.md"), but lets you search a string for a
regular expression pattern. For more information about regular expressions, see [POSIX operators](pattern-matching-conditions-posix.md "pattern-matching-conditions-posix.md") and
[Regular expression](https://en.wikipedia.org/wiki/Regular_expression "https://en.wikipedia.org/wiki/Regular_expression") in Wikipedia.

REGEXP_REPLACE is similar to the [TRANSLATE function](r_TRANSLATE.md "r_TRANSLATE.md") and the [REPLACE function](r_REPLACE.md "r_REPLACE.md"), except that TRANSLATE makes multiple single-character
substitutions and REPLACE substitutes one entire string with another string, while
REGEXP_REPLACE lets you search a string for a regular expression pattern.

## Syntax

```
REGEXP_REPLACE( *source\_string*, *pattern* [, *replace\_string* [ , *position* [, *parameters* ] ] ] )
```

## Arguments

_source_string_

A `CHAR` or `VARCHAR` string expression, such as a column name, to be searched.

_pattern_

A UTF-8 string literal that represents a regular expression pattern. For more information, see
[POSIX operators](pattern-matching-conditions-posix.md "pattern-matching-conditions-posix.md").

_replace_string_

(Optional) A `CHAR` or `VARCHAR` string expression, such as a column name, that will replace each
occurrence of pattern. The default is an empty string ( "" ).

_position_

(Optional) A positive integer that indicates the position within
_source_string_ to begin searching. The position is
based on the number of characters, not bytes, so that multibyte characters
are counted as single characters. The default is `1`. If
_position_ is less than `1`, the search begins at the
first character of _source_string_. If
_position_ is greater than the number of characters in
_source_string_, the result is
_source_string_.

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

VARCHAR

If either _pattern_ or _replace_string_ is
`NULL`, the function returns `NULL`.

## Examples

To replace all occurrences of the string `FOX` within the value
`quick brown fox` using case-insensitive matching, use the following example.

````
`SELECT REGEXP_REPLACE('the fox', 'FOX', 'quick brown fox', 1, 'i');`

`+---------------------+
| regexp_replace | +---------------------+
| the quick brown fox | +---------------------+` ``` The following example uses a pattern written in the PCRE dialect to locate words containing at least one number and one lowercase letter. It uses the `?=` operator, which has a specific look-ahead connotation in PCRE. To replace each occurrence of such a word with the value `[hidden]`, use the following example. ``` `SELECT REGEXP_REPLACE('passwd7 plain A1234 a1234', '(?=[^ ]*[a-z])(?=[^ ]*[0-9])[^ ]+', '[hidden]', 1, 'p');` `+-------------------------------+
| regexp_replace | +-------------------------------+
| [hidden] plain A1234 [hidden] | +-------------------------------+` ``` The following example uses a pattern written in the PCRE dialect to locate words containing at least one number and one lowercase letter. It uses the `?=` operator, which has a specific look-ahead connotation in PCRE. To replace each occurrence of such a word with the value `[hidden]`, but differs from the previous example in that it uses case-insensitive matching, use the following example. ``` `SELECT REGEXP_REPLACE('passwd7 plain A1234 a1234', '(?=[^ ]*[a-z])(?=[^ ]*[0-9])[^ ]+', '[hidden]', 1, 'ip');` `+----------------------------------+
| regexp_replace | +----------------------------------+
| [hidden] plain [hidden] [hidden] | +----------------------------------+` ``` The following examples use data from the USERS table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md"). To delete the `@` and domain name from email addresses, use the following example. ``` `SELECT email, REGEXP_REPLACE(email, '@.*\\.(org|gov|com|edu|ca)$') FROM users ORDER BY userid LIMIT 4;` `+-----------------------------------------------+-----------------------+
| email | regexp_replace | +-----------------------------------------------+-----------------------+
| Etiam.laoreet.libero@sodalesMaurisblandit.edu | Etiam.laoreet.libero |
| Suspendisse.tristique@nonnisiAenean.edu | Suspendisse.tristique |
| amet.faucibus.ut@condimentumegetvolutpat.ca | amet.faucibus.ut |
| sed@lacusUtnec.ca | sed | +-----------------------------------------------+-----------------------+` ``` To replace the domain names of email addresses with `internal.company.com`, use the following example. ``` `SELECT email, REGEXP_REPLACE(email, '@.*\\.[[:alpha:]]{2,3}','@internal.company.com') FROM users ORDER BY userid LIMIT 4;` `+-----------------------------------------------+--------------------------------------------+
| email | regexp_replace | +-----------------------------------------------+--------------------------------------------+
| Etiam.laoreet.libero@sodalesMaurisblandit.edu | Etiam.laoreet.libero@internal.company.com |
| Suspendisse.tristique@nonnisiAenean.edu | Suspendisse.tristique@internal.company.com |
| amet.faucibus.ut@condimentumegetvolutpat.ca | amet.faucibus.ut@internal.company.com |
| sed@lacusUtnec.ca | sed@internal.company.com | +-----------------------------------------------+--------------------------------------------+` ```
````
