# REGEXP_REPLACE function

Searches a string for a regular expression pattern and replaces every occurrence of the
pattern with the specified string. REGEXP_REPLACE is similar to the [REPLACE function](REPLACE.md "REPLACE.md"), but lets you search a string for a regular expression
pattern.

REGEXP_REPLACE is similar to the [TRANSLATE function](TRANSLATE.md "TRANSLATE.md")
and the [REPLACE function](REPLACE.md "REPLACE.md"), except that TRANSLATE makes
multiple single-character substitutions and REPLACE substitutes one entire string with
another string, while REGEXP_REPLACE lets you search a string for a regular expression
pattern.

## Syntax

```
REGEXP_REPLACE ( *source\_string*, *pattern* [, *replace\_string* [ , *position* [, *parameters* ] ] ] )
```

## Arguments

_source_string_

A string expression, such as a column name, to be searched.

_pattern_

A string literal that represents a regular expression pattern.

_replace_string_

A string expression, such as a column name, that will replace each
occurrence of pattern. The default is an empty string ( "" ).

_position_

A positive integer that indicates the position within
_source_string_ to begin searching. The position is based
on the number of characters, not bytes, so that multibyte characters are
counted as single characters. The default is 1. If
_position_ is less than 1, the search begins at the first
character of _source_string_. If
_position_ is greater than the number of characters in
_source_string_, the result is
_source_string_.

_parameters_

One or more string literals that indicate how the function matches the
pattern. The possible values are the following:

- c – Perform case-sensitive matching. The default is to use
  case-sensitive matching.
- i – Perform case-insensitive matching.
- p – Interpret the pattern with Perl Compatible Regular
  Expression (PCRE) dialect.

## Return type

VARCHAR

If either _pattern_ or _replace_string_ is
NULL, the return is NULL.

## Example

The following example deletes the `@` and domain name from email
addresses.

```
SELECT email, regexp_replace(email, '@.*\\.(org|gov|com|edu|ca)$')
FROM users
ORDER BY userid LIMIT 4;

              email                            | regexp_replace
-----------------------------------------------+----------------
 Etiam.laoreet.libero@sodalesMaurisblandit.edu | Etiam.laoreet.libero
 Suspendisse.tristique@nonnisiAenean.edu       | Suspendisse.tristique
 amet.faucibus.ut@condimentumegetvolutpat.ca   | amet.faucibus.ut
 sed@lacusUtnec.ca                             | sed
```

The following example replaces the domain names of email addresses with this value:
`internal.company.com`.

```
SELECT email, regexp_replace(email, '@.*\\.[[:alpha:]]{2,3}',
'@internal.company.com') FROM users
ORDER BY userid LIMIT 4;

                     email                     |               regexp_replace
-----------------------------------------------+--------------------------------------------
 Etiam.laoreet.libero@sodalesMaurisblandit.edu | Etiam.laoreet.libero@internal.company.com
 Suspendisse.tristique@nonnisiAenean.edu       | Suspendisse.tristique@internal.company.com
 amet.faucibus.ut@condimentumegetvolutpat.ca   | amet.faucibus.ut@internal.company.com
 sed@lacusUtnec.ca                             | sed@internal.company.com
```

The following example replaces all occurrences of the string `FOX` within
the value `quick brown fox`, using case-insensitive matching.

```
SELECT regexp_replace('the fox', 'FOX', 'quick brown fox', 1, 'i');

   regexp_replace
---------------------
 the quick brown fox
```

The following example uses a pattern written in the PCRE dialect to locate words
containing at least one number and one lowercase letter. It uses the `?=`
operator, which has a specific look-ahead connotation in PCRE. This example replaces
each occurrence of such a word with the value `[hidden]`.

```
SELECT regexp_replace('passwd7 plain A1234 a1234', '(?=[^ ]*[a-z])(?=[^ ]*[0-9])[^ ]+', '[hidden]', 1, 'p');

        regexp_replace
-------------------------------
 [hidden] plain A1234 [hidden]
```

The following example uses a pattern written in the PCRE dialect to locate words
containing at least one number and one lowercase letter. It uses the `?=`
operator, which has a specific look-ahead connotation in PCRE. This example replaces
each occurrence of such a word with the value `[hidden]`, but differs from
the previous example in that it uses case-insensitive matching.

```
SELECT regexp_replace('passwd7 plain A1234 a1234', '(?=[^ ]*[a-z])(?=[^ ]*[0-9])[^ ]+', '[hidden]', 1, 'ip');

          regexp_replace
----------------------------------
 [hidden] plain [hidden] [hidden]
```
