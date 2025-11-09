# String Operators

You can use string operators for streaming SQL, including concatenation and string pattern
comparison, to combine and compare strings.

| Operator   | Unary/Binary | Description               | Notes                                                                   |
| ---------- | ------------ | ------------------------- | ----------------------------------------------------------------------- | ------------- | ---------------------------- |
|            |              |                           | B                                                                       | Concatenation | Also applies to binary types |
| LIKE       | B            | String pattern comparison | <string> LIKE <like pattern> [ESCAPE <escape character>]                |
| SIMILAR TO | B            | String pattern comparison | <string> SIMILAR TO <similar to pattern> [ESCAPE <escape<br>character>] |

## Concatenation

This operator is used to concatenate one or more strings as shown in the following
table.

| Operation | Result |
| --------- | ------ | -------- | --------- | --------------- | ---------------------- | ------ | ------------------------ |
| 'SQL'     |        | 'stream' | SQLstream |
| 'SQL'     |        | ''       |           | 'stream'        | SQLstream              |
| 'SQL'     |        | 'stream' |           | ' Incorporated' | SQLstream Incorporated |
| <col1>    |        | <col2>   |           | <col3>          |                        | <col4> | <col1><col2><col3><col4> |

## LIKE patterns

LIKE compares a string to a string pattern. In the pattern, the characters \_ (underscore)
and % (percent) have special meaning.

| Character in pattern  | Effect                                            |
| --------------------- | ------------------------------------------------- |
| \_                    | Matches any single character                      |
| %                     | Matches any substring, including the empty string |
| <any other character> | Matches only the exact same character             |

If either operand is NULL, the result of the LIKE operation is UNKNOWN.

To explicitly match a special character in the character string, you must specify an
escape character using the ESCAPE clause. The escape character must then precede the special
character in the pattern. The following table lists examples.

| Operation                     | Result |
| ----------------------------- | ------ |
| 'a' LIKE 'a'                  | TRUE   |
| 'a' LIKE 'A'                  | FALSE  |
| 'a' LIKE 'b'                  | FALSE  |
| 'ab' LIKE 'a\_'               | TRUE   |
| 'ab' LIKE 'a%'                | TRUE   |
| 'ab' LIKE 'a\\\_' ESCAPE '\'  | FALSE  |
| 'ab' LIKE 'a\%' ESCAPE '\'    | FALSE  |
| 'a\_' LIKE 'a\\\_' ESCAPE '\' | TRUE   |
| 'a%' LIKE 'a\%' ESCAPE '\'    | TRUE   |
| 'a' LIKE 'a\_'                | FALSE  |
| 'a' LIKE 'a%'                 | TRUE   |
| 'abcd' LIKE 'a\_'             | FALSE  |
| 'abcd' LIKE 'a%'              | TRUE   |
| '' LIKE ''                    | TRUE   |
| '1a' LIKE '\_a'               | TRUE   |
| '123aXYZ' LIKE '%a%'          | TRUE   |
| '123aXYZ' LIKE '\_%\_a%\_'    | TRUE   |

## SIMILAR TO patterns

SIMILAR TO compares a string to a pattern. It is much like the LIKE operator, but more
powerful, as the patterns are regular expressions.

In the following SIMILAR TO table, _seq_ means any sequence of
characters  explicitly specified, such as '13aq'. Non-alphanumeric characters intended for
matching must be preceded by an escape character explicitly declared in the SIMILAR TO
statement, such as '13aq\!' SIMILAR TO '13aq\!24br\!% ESCAPE '\'  (This statement is
TRUE).

When a range is indicated, as when a dash is used in a pattern, the current collating
sequence is used. Typical ranges are 0-9 and a-z. [PostgreSQL](https://www.postgresql.org/docs/7.3/static/functions-matching.html "https://www.postgresql.org/docs/7.3/static/functions-matching.html")
provides a typical discussion of pattern-matching, including ranges.

When a line requires multiple comparisons, the innermost pattern that can be matched will
be matched first, then the "next-innermost," etc.

Expressions and matching operations that are enclosed within parentheses are evaluated
before surrounding operations are applied, again by innermost-first precedence.

| Delimiter           | Character in pattern            | Effect                                                                                                                                                                                                       | Rule ID |
| ------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| parentheses (  )    | (  seq  )                       | Groups the \*seq<br>• (used for defining precedence of pattern<br>expressions)                                                                                                                               | 1       |
| brackets [  ]       | [  seq  ]                       | Matches any single character in the seq                                                                                                                                                                      | 2       |
| caret or circumflex | [^seq]                          | Matches any single character not in the seq                                                                                                                                                                  | 3       |
|                     | [ seq ^ seq]                    | Matches any single character in seq and not in seq                                                                                                                                                           | 4       |
| dash                | <character1>-<character2>       | Specifies a range of characters between character1 and character2<br>(using some known sequence like 1-9 or a-z)                                                                                             | 5       |
| bar                 | [ seq  seq]                     | Matches either seq or seq                                                                                                                                                                                    | 6       |
| asterisk            | seq\*                           | Matches zero or more repetitions of seq                                                                                                                                                                      | 7       |
| plus                | seq+                            | Matches one or more repetitions of seq                                                                                                                                                                       | 8       |
| braces              | seq{<number>}                   | Matches exactly number repetitions of seq                                                                                                                                                                    | 9       |
|                     | seq{<low number>,<high number>} | Matches low number or more repetitions of seq, to a maximum of high<br>number                                                                                                                                | 10      |
| question-mark       | seq?                            | Matches zero or one instances of seq                                                                                                                                                                         | 11      |
| underscore          | \_                              | Matches any single character                                                                                                                                                                                 | 12      |
| percent             | %                               | Matches any substring, including the empty string                                                                                                                                                            | 13      |
| character           | <any other character>           | Matches only the exact same character                                                                                                                                                                        | 14      |
| NULL                | NULL                            | If either operand is NULL, the result of the SIMILAR TO operation is<br>UNKNOWN.                                                                                                                             | 15      |
| Non-alphanumeric    | Special characters              | To explicitly match a special character in the character string,<br>that special character must be preceded by an escape character defined<br>using<br>an ESCAPE clause specified at the end of the pattern. | 16      |

The following table lists examples.

| Operation                                     | Result  | Rule    |
| --------------------------------------------- | ------- | ------- |
| 'a' SIMILAR TO 'a'                            | TRUE    | 14      |
| 'a' SIMILAR TO 'A'                            | FALSE   | 14      |
| 'a' SIMILAR TO 'b'                            | FALSE   | 14      |
| 'ab' SIMILAR TO 'a\_'                         | TRUE    | 12      |
| 'ab' SIMILAR TO 'a%'                          | TRUE    | 13      |
| 'a' SIMILAR TO 'a\_'                          | FALSE   | 12 & 14 |
| 'a' SIMILAR TO 'a%'                           | TRUE    | 13      |
| 'abcd' SIMILAR TO 'a\_'                       | FALSE   | 12      |
| 'abcd' SIMILAR TO 'a%'                        | TRUE    | 13      |
| '' SIMILAR TO ''                              | TRUE    | 14      |
| '1a' SIMILAR TO '\_a'                         | TRUE    | 12      |
| '123aXYZ' SIMILAR TO ''                       | TRUE    | 14      |
| '123aXYZ' SIMILAR TO '\_%\_a%\_'              | TRUE    | 13 & 12 |
| 'xy' SIMILAR TO '(xy)'                        | TRUE    | 1       |
| 'abd' SIMILAR TO '[ab][bcde]d'                | TRUE    | 2       |
| 'bdd' SIMILAR TO '[ab][bcde]d'                | TRUE    | 2       |
| 'abd' SIMILAR TO '[ab]d'                      | FALSE   | 2       |
| 'cd' SIMILAR TO '[a-e]d'                      | TRUE    | 2       |
| 'cd' SIMILAR TO '[a-e^c]d'                    | FALSE   | 4       |
| 'cd' SIMILAR TO '[^(a-e)]d'                   | INVALID |
| 'yd' SIMILAR TO '[^(a-e)]d'                   | INVALID |
| 'amy' SIMILAR TO 'amyfred'                    | TRUE    | 6       |
| 'fred' SIMILAR TO 'amyfred'                   | TRUE    | 6       |
| 'mike' SIMILAR TO 'amyfred'                   | FALSE   | 6       |
| 'acd' SIMILAR TO 'ab\*c+d'                    | TRUE    | 7 & 8   |
| 'accccd' SIMILAR TO 'ab\*c+d'                 | TRUE    | 7 & 8   |
| 'abd' SIMILAR TO 'ab\*c+d'                    | FALSE   | 7 & 8   |
| 'aabc' SIMILAR TO 'ab\*c+d'                   | FALSE   |         |
| 'abb' SIMILAR TO 'a(b{3})'                    | FALSE   | 9       |
| 'abbb' SIMILAR TO 'a(b{3})'                   | TRUE    | 9       |
| 'abbbbb' SIMILAR TO 'a(b{3})'                 | FALSE   | 9       |
| 'abbbbb' SIMILAR TO 'ab{3,6}'                 | TRUE    | 10      |
| 'abbbbbbbb' SIMILAR TO 'ab{3,6}'              | FALSE   | 10      |
| '' SIMILAR TO 'ab?'                           | FALSE   | 11      |
| '' SIMILAR TO '(ab)?'                         | TRUE    | 11      |
| 'a' SIMILAR TO 'ab?'                          | TRUE    | 11      |
| 'a' SIMILAR TO '(ab)?'                        | FALSE   | 11      |
| 'a' SIMILAR TO 'a(b?)'                        | TRUE    | 11      |
| 'ab' SIMILAR TO 'ab?'                         | TRUE    | 11      |
| 'ab' SIMILAR TO 'a(b?)'                       | TRUE    | 11      |
| 'abb' SIMILAR TO 'ab?'                        | FALSE   | 11      |
| 'ab' SIMILAR TO 'a\\\_' ESCAPE '\'            | FALSE   | 16      |
| 'ab' SIMILAR TO 'a\%' ESCAPE '\'              | FALSE   | 16      |
| 'a\_' SIMILAR TO 'a\\\_' ESCAPE '\'           | TRUE    | 16      |
| 'a%' SIMILAR TO 'a\%' ESCAPE '\'              | TRUE    | 16      |
| 'a(b{3})' SIMILAR TO 'a(b{3})'                | FALSE   | 16      |
| 'a(b{3})' SIMILAR TO 'a\(b\{3\}\)' ESCAPE '\' | TRUE    | 16      |
