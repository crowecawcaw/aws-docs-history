Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# POSIX operators

A POSIX regular expression is a sequence of characters that specifies a match
pattern. A string matches a regular expression if it is a member of the regular
set described by the regular expression.

POSIX regular expressions provide a more powerful means for pattern matching
than the [LIKE](r_patternmatching_condition_like.md "r_patternmatching_condition_like.md") and [SIMILAR TO](pattern-matching-conditions-similar-to.md "pattern-matching-conditions-similar-to.md") operators. POSIX
regular expression patterns can match any portion of a string, unlike the SIMILAR
TO operator, which returns true only if its pattern matches the entire
string.

###### Note

Regular expression matching using POSIX operators is computationally
expensive. We recommend using LIKE whenever possible, especially when
processing a very large number of rows. For example, the following queries are
functionally identical, but the query that uses LIKE runs several times faster
than the query that uses a regular expression:

```
select count(*) from event where eventname ~ '.*(Ring|Die).*';
select count(*) from event where eventname LIKE '%Ring%' OR eventname LIKE '%Die%';
```

## Syntax

```
*expression* [ ! ] ~ *pattern*
```

## Arguments

_expression_

A valid UTF-8 character expression, such as a column name.

!

Negation operator. Does not match the regular expression.

~

Perform a case-sensitive match for any substring of
_expression_.

###### Note

A `~~` is a synonym for [LIKE](r_patternmatching_condition_like.md "r_patternmatching_condition_like.md").

_pattern_

A string literal that represents a regular expression pattern.

If _pattern_ does not contain wildcard characters, then
the pattern only represents the string itself.

To search for strings that include metacharacters, such as ‘`. * | ?` ‘, and so on, escape the character using two backslashes ('`\\` '). Unlike `SIMILAR TO` and `LIKE`, POSIX
regular expression syntax does not support a user-defined escape character.

Either of the character expressions can be CHAR or VARCHAR data types. If
they differ, Amazon Redshift converts _pattern_ to the data type of
_expression_.

All of the character expressions can be CHAR or VARCHAR data types. If the
expressions differ in data type, Amazon Redshift converts them to the data type of
_expression_.

POSIX pattern matching supports the following metacharacters:

| POSIX   | Description                                                                                                                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------- |
| .       | Matches any single character.                                                                                                                                                                                       |
| `*`     | Matches zero or more occurrences.                                                                                                                                                                                   |
| `+`     | Matches one or more occurrences.                                                                                                                                                                                    |
| `?`     | Matches zero or one occurrence.                                                                                                                                                                                     |
| `       | `                                                                                                                                                                                                                   | Specifies alternative matches; for example,<br>``E | H``means`E` or<br>`H`. |
| `^`     | Matches the beginning-of-line character.                                                                                                                                                                            |
| `$`     | Matches the end-of-line character.                                                                                                                                                                                  |
| `$`     | Matches the end of the string.                                                                                                                                                                                      |
| [ ]     | Brackets specify a matching list, that should<br>match one expression in the list. A caret (`^`) precedes<br>a nonmatching list, which matches any character except for the<br>expressions represented in the list. |
| `( )`   | Parentheses group items into a single logical<br>item.                                                                                                                                                              |
| `{m}`   | Repeat the previous item exactly<br>\*m<br>• times.                                                                                                                                                                 |
| `{m,}`  | Repeat the previous item _m_<br>or more times.                                                                                                                                                                      |
| `{m,n}` | Repeat the previous item at least<br>*m<br>• and not more than *n\*<br>times.                                                                                                                                       |
| `[: :]` | Matches any character within a POSIX character<br>class. In the following character classes, Amazon Redshift supports only<br>ASCII characters: `[:alnum:]`, `[:alpha:]`,<br>`[:lower:]`, `[:upper:]`               |

Amazon Redshift supports the following POSIX character classes.

| Character Class | Description                                  |
| --------------- | -------------------------------------------- |
| `[[:alnum:]]`   | All ASCII alphanumeric characters            |
| `[[:alpha:]]`   | All ASCII alphabetic characters              |
| `[[:blank:]]`   | All blank space characters                   |
| `[[:cntrl:]]`   | All control characters (nonprinting)         |
| `[[:digit:]]`   | All numeric digits                           |
| `[[:lower:]]`   | All lowercase ASCII alphabetic<br>characters |
| `[[:punct:]]`   | All punctuation characters                   |
| `[[:space:]]`   | All space characters (nonprinting)           |
| `[[:upper:]]`   | All uppercase ASCII alphabetic<br>characters |
| `[[:xdigit:]]`  | All valid hexadecimal characters             |

Amazon Redshift supports the following Perl-influenced operators in regular
expressions. Escape the operator using two backslashes (‘`\\`’).  

| Operator | Description                 | Equivalent character class expression |
| -------- | --------------------------- | ------------------------------------- |
| `\\d`    | A digit character           | `[[:digit:]]`                         |
| `\\D`    | A nondigit character        | `[^[:digit:]]`                        |
| `\\w`    | A word character            | `[[:word:]]`                          |
| `\\W`    | A nonword character         | `[^[:word:]]`                         |
| `\\s`    | A white space character     | `[[:space:]]`                         |
| `\\S`    | A non–white space character | `[^[:space:]]`                        |
| `\\b`    | A boundary word             |                                       |

## Examples

The following table shows examples of pattern matching using POSIX
operators:

| Expression                                                 | Returns |
| ---------------------------------------------------------- | ------- | ---- |
| `'abc' ~ 'abc'`                                            | True    |
| `'abc' ~ 'a'`                                              | True    |
| `'abc' ~ 'A'`                                              | False   |
| `'abc' ~ '.\*(b                                            | d).\*'` | True |
| `'abc' ~ '(b                                               | c).\*'` | True |
| `'AbcAbcdefgefg12efgefg12' ~<br>'((Ab)?c)+d((efg)+(12))+'` | True    |
| `'aaaaaab11111xy' ~<br>'a{6}.[1]{5}(x                      | y){2}'` | True |
| `'$0.87' ~ '\\$[0-9]+(\\.[0-9][0-9])?'`                    | True    |
| `'ab c' ~ '[[:space:]]'`                                   | True    |
| `'ab c' ~ '\\s'`                                           | True    |
| `' ' ~ '\\S'`                                              | False   |

The following example finds cities whose names contain `E` or
`H`:

```
SELECT DISTINCT city FROM users
WHERE city ~ '.*E.*|.*H.*' ORDER BY city LIMIT 5;

      city
-----------------
 Agoura Hills
 Auburn Hills
 Benton Harbor
 Beverly Hills
 Chicago Heights
```

The following example finds cities whose names don't contain `E`
or `H`:

```
`SELECT DISTINCT city FROM users WHERE city !~ '.*E.*|.*H.*' ORDER BY city LIMIT 5;`
`city
-----------------
 Aberdeen
 Abilene
 Ada
 Agat
 Agawam`
```

The following example uses the escape string ('`\\`') to search
for strings that include a period.

```
SELECT venuename FROM venue
WHERE venuename ~ '.*\\..*'
ORDER BY venueid;

          venuename
------------------------------
 St. Pete Times Forum
 Jobing.com Arena
 Hubert H. Humphrey Metrodome
 U.S. Cellular Field
 Superpages.com Center
 E.J. Nutter Center
 Bernard B. Jacobs Theatre
 St. James Theatre
```
