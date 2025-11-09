Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SIMILAR TO

The SIMILAR TO operator matches a string expression, such as a column name,
with a SQL standard regular expression pattern. A SQL regular expression pattern
can include a set of pattern-matching metacharacters, including the two supported
by the [LIKE](r_patternmatching_condition_like.md "r_patternmatching_condition_like.md") operator.

The SIMILAR TO operator returns true only if its pattern matches the entire
string, unlike POSIX regular expression behavior, where the pattern can match any
portion of the string.

SIMILAR TO performs a case-sensitive match.

###### Note

Regular expression matching using SIMILAR TO is computationally expensive.
We recommend using LIKE whenever possible, especially when processing a very
large number of rows. For example, the following queries are functionally
identical, but the query that uses LIKE runs several times faster than the
query that uses a regular expression:

```
select count(*) from event where eventname SIMILAR TO '%(Ring|Die)%';
select count(*) from event where eventname LIKE '%Ring%' OR eventname LIKE '%Die%';
```

## Syntax

```
*expression* [ NOT ] SIMILAR TO *pattern* [ ESCAPE '*escape\_char*' ]
```

## Arguments

_expression_

A valid UTF-8 character expression, such as a column name.

SIMILAR TO

SIMILAR TO performs a case-sensitive pattern match for the entire
string in _expression_.

_pattern_

A valid UTF-8 character expression representing a SQL standard
regular expression pattern.

_escape_char_

A character expression that will escape metacharacters in the
pattern. The default is two backslashes ('\\').

If _pattern_ does not contain metacharacters, then the
pattern only represents the string itself.

Either of the character expressions can be CHAR or VARCHAR data types. If
they differ, Amazon Redshift converts _pattern_ to the data type of
_expression_.

SIMILAR TO supports the following pattern-matching metacharacters:

| Operator | Description                                                                                |
| -------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| `%`      | Matches any sequence of zero or more<br>characters.                                        |
| `_`      | Matches any single character.                                                              |
| `        | `                                                                                          | Denotes alternation (either of two<br>alternatives). |
| `*`      | Repeat the previous item zero or more<br>times.                                            |
| `+`      | Repeat the previous item one or more<br>times.                                             |
| `?`      | Repeat the previous item zero or one<br>time.                                              |
| `{m}`    | Repeat the previous item exactly<br>\*m<br>• times.                                        |
| `{m,}`   | Repeat the previous item _m_<br>or more times.                                             |
| `{m,n}`  | Repeat the previous item at least<br>*m<br>• and not more than *n\*<br>times.              |
| `()`     | Parentheses group items into a single logical<br>item.                                     |
| `[...]`  | A bracket expression specifies a character<br>class, just as in POSIX regular expressions. |

## Examples

The following table shows examples of pattern matching using SIMILAR
TO:

| Expression                                                          | Returns |
| ------------------------------------------------------------------- | ------- | ----- |
| `'abc' SIMILAR TO 'abc'`                                            | True    |
| `'abc' SIMILAR TO '_b_'`                                            | True    |
| `'abc' SIMILAR TO '_A_'`                                            | False   |
| `'abc' SIMILAR TO '%(b                                              | d)%'`   | True  |
| `'abc' SIMILAR TO '(b                                               | c)%'`   | False |
| `'AbcAbcdefgefg12efgefg12' SIMILAR TO<br>'((Ab)?c)+d((efg)+(12))+'` | True    |
| `'aaaaaab11111xy' SIMILAR TO 'a{6}\_<br>[0-9]{5}(x                  | y){2}'` | True  |
| `'$0.87' SIMILAR TO '$[0-9]+(.[0-9][0-9])?'`                        | True    |

The following example finds cities whose names contain "E" or "H":

```
SELECT DISTINCT city FROM users
WHERE city SIMILAR TO '%E%|%H%' ORDER BY city LIMIT 5;

      city
-----------------
 Agoura Hills
 Auburn Hills
 Benton Harbor
 Beverly Hills
 Chicago Heights
```

The following example uses the default escape string ('`\\`') to
search for strings that include "`_`":

```
SELECT tablename, "column" FROM pg_table_def
WHERE "column" SIMILAR TO '%start\\_%'
ORDER BY tablename, "column" LIMIT 5;

        tablename         |       column
--------------------------+---------------------
 stcs_abort_idle          | idle_start_time
 stcs_abort_idle          | txn_start_time
 stcs_analyze_compression | start_time
 stcs_auto_worker_levels  | start_level
 stcs_auto_worker_levels  | start_wlm_occupancy
```

The following example specifies '`^`' as the escape string, then
uses the escape string to search for strings that include "`_`":

```
SELECT tablename, "column" FROM pg_table_def
WHERE "column" SIMILAR TO '%start^_%' ESCAPE '^'
ORDER BY tablename, "column" LIMIT 5;

        tablename         |       column
--------------------------+---------------------
 stcs_abort_idle          | idle_start_time
 stcs_abort_idle          | txn_start_time
 stcs_analyze_compression | start_time
 stcs_auto_worker_levels  | start_level
 stcs_auto_worker_levels  | start_wlm_occupancy
```
