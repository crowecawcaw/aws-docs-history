

# String Operators
<a name="sql-reference-string-operators"></a>

You can use string operators for streaming SQL, including concatenation and string pattern comparison, to combine and compare strings.


| Operator | Unary/Binary | Description | Notes | 
| --- | --- | --- | --- | 
| \|\| | B | Concatenation | Also applies to binary types | 
| LIKE | B | String pattern comparison | <string> LIKE <like pattern> [ESCAPE <escape character>] | 
| SIMILAR TO | B | String pattern comparison | <string> SIMILAR TO <similar to pattern> [ESCAPE <escape character>] | 

## Concatenation
<a name="CONCAT"></a>

This operator is used to concatenate one or more strings as shown in the following table.


| Operation | Result | 
| --- | --- | 
| 'SQL'\|\|'stream' | SQLstream | 
| 'SQL'\|\|''\|\|'stream' | SQLstream | 
| 'SQL'\|\|'stream'\|\|' Incorporated' | SQLstream Incorporated | 
| <col1>\|\|<col2>\|\|<col3>\|\|<col4> | <col1><col2><col3><col4> | 

## LIKE patterns
<a name="w2aac10c19c21b9"></a>

LIKE compares a string to a string pattern. In the pattern, the characters \_ (underscore) and % (percent) have special meaning.


| Character in pattern | Effect | 
| --- | --- | 
| \_ | Matches any single character | 
| % | Matches any substring, including the empty string | 
| <any other character> | Matches only the exact same character | 

If either operand is NULL, the result of the LIKE operation is UNKNOWN.

To explicitly match a special character in the character string, you must specify an escape character using the ESCAPE clause. The escape character must then precede the special character in the pattern. The following table lists examples.


| Operation | Result | 
| --- | --- | 
| 'a' LIKE 'a' | TRUE | 
| 'a' LIKE 'A' | FALSE | 
| 'a' LIKE 'b' | FALSE | 
| 'ab' LIKE 'a\_' | TRUE | 
| 'ab' LIKE 'a%' | TRUE | 
| 'ab' LIKE 'a\\\_' ESCAPE '\\' | FALSE | 
| 'ab' LIKE 'a\\%' ESCAPE '\\' | FALSE | 
| 'a\_' LIKE 'a\\\_' ESCAPE '\\' | TRUE | 
| 'a%' LIKE 'a\\%' ESCAPE '\\' | TRUE | 
| 'a' LIKE 'a\_' | FALSE | 
| 'a' LIKE 'a%' | TRUE | 
| 'abcd' LIKE 'a\_' | FALSE | 
| 'abcd' LIKE 'a%' | TRUE | 
| '' LIKE '' | TRUE | 
| '1a' LIKE '\_a' | TRUE | 
| '123aXYZ' LIKE '%a%' | TRUE | 
| '123aXYZ' LIKE '\_%\_a%\_' | TRUE | 

## SIMILAR TO patterns
<a name="SIMILARPATTERNS"></a>

SIMILAR TO compares a string to a pattern. It is much like the LIKE operator, but more powerful, as the patterns are regular expressions.

In the following SIMILAR TO table, *seq* means any sequence of characters  explicitly specified, such as '13aq'. Non-alphanumeric characters intended for matching must be preceded by an escape character explicitly declared in the SIMILAR TO statement, such as '13aq\\\!' SIMILAR TO '13aq\\\!24br\\\!% ESCAPE '\\'  (This statement is TRUE).

When a range is indicated, as when a dash is used in a pattern, the current collating sequence is used. Typical ranges are 0-9 and a-z. [PostgreSQL](https://www.postgresql.org/docs/7.3/static/functions-matching.html) provides a typical discussion of pattern-matching, including ranges.

When a line requires multiple comparisons, the innermost pattern that can be matched will be matched first, then the "next-innermost," etc.

Expressions and matching operations that are enclosed within parentheses are evaluated before surrounding operations are applied, again by innermost-first precedence.


| Delimiter | Character in pattern | Effect | Rule ID | 
| --- | --- | --- | --- | 
| parentheses (  ) |   (  seq  ) |  Groups the *seq* (used for defining precedence of pattern expressions) | 1 | 
|  brackets [  ] |  [  seq  ] | Matches any single character in the seq | 2 | 
|  caret or circumflex |  [^seq] |  Matches any single character not in the seq | 3 | 
|   |   [ seq ^ seq] | Matches any single character in seq and not in seq | 4 | 
| dash |  <character1>-<character2> | Specifies a range of characters between character1 and character2<br />(using some known sequence like 1-9 or a-z) | 5 | 
|  bar |   [ seq  seq] | Matches either seq or seq | 6 | 
|  asterisk |   seq\* | Matches zero or more repetitions of seq | 7 | 
|  plus |  seq\+ | Matches one or more repetitions of seq | 8 | 
|  braces |   seq{<number>} | Matches exactly number repetitions of seq  | 9 | 
|  |   seq{<low number>,<high number>} | Matches low number or more repetitions of seq, to a maximum of high number | 10 | 
|  question-mark |   seq? | Matches zero or one instances of seq | 11 | 
|  underscore |  \_ |  Matches any single character | 12 | 
|  percent |  % |  Matches any substring, including the empty string | 13 | 
|  character |  <any other character> |  Matches only the exact same character | 14 | 
|   NULL |   NULL |   If either operand is NULL, the result of the SIMILAR TO operation is UNKNOWN. | 15 | 
|   Non-alphanumeric |  Special characters |  To explicitly match a special character in the character string,<br />that special character must be preceded by an escape character defined using<br />an ESCAPE clause specified at the end of the pattern. | 16 | 

The following table lists examples.


<table>
<thead>
  <tr><th>Operation</th><th>Result</th><th>Rule</th></tr>
</thead>
<tbody>
  <tr><td>'a' SIMILAR TO 'a'</td><td>TRUE</td><td>14</td></tr>
  <tr><td>'a' SIMILAR TO 'A'</td><td>FALSE</td><td>14</td></tr>
  <tr><td>'a' SIMILAR TO 'b'</td><td>FALSE</td><td>14</td></tr>
  <tr><td>'ab' SIMILAR TO 'a_'</td><td>TRUE</td><td>12</td></tr>
  <tr><td>'ab' SIMILAR TO 'a%'</td><td>TRUE</td><td>13</td></tr>
  <tr><td>'a' SIMILAR TO 'a_'</td><td>FALSE</td><td>12 &amp; 14</td></tr>
  <tr><td>'a' SIMILAR TO 'a%'</td><td>TRUE</td><td>13</td></tr>
  <tr><td>'abcd' SIMILAR TO 'a_'</td><td>FALSE</td><td>12</td></tr>
  <tr><td>'abcd' SIMILAR TO 'a%'</td><td>TRUE</td><td>13</td></tr>
  <tr><td>'' SIMILAR TO ''</td><td>TRUE</td><td>14</td></tr>
  <tr><td>'1a' SIMILAR TO '_a'</td><td>TRUE</td><td>12</td></tr>
  <tr><td>'123aXYZ' SIMILAR TO ''</td><td>TRUE</td><td>14</td></tr>
  <tr><td>'123aXYZ' SIMILAR TO '_%_a%_'</td><td>TRUE</td><td>13 &amp; 12</td></tr>
  <tr><td>'xy' SIMILAR TO '(xy)'</td><td>TRUE</td><td>1</td></tr>
  <tr><td>'abd' SIMILAR TO '[ab][bcde]d'</td><td>TRUE</td><td>2</td></tr>
  <tr><td>'bdd' SIMILAR TO '[ab][bcde]d'</td><td>TRUE</td><td>2</td></tr>
  <tr><td>'abd' SIMILAR TO '[ab]d'</td><td>FALSE</td><td>2</td></tr>
  <tr><td>'cd' SIMILAR TO '[a-e]d'</td><td>TRUE</td><td>2</td></tr>
  <tr><td>'cd' SIMILAR TO '[a-e^c]d'</td><td>FALSE</td><td>4</td></tr>
  <tr><td>'cd' SIMILAR TO '[^(a-e)]d'</td><td colspan="2">INVALID</td></tr>
  <tr><td>'yd' SIMILAR TO '[^(a-e)]d'</td><td colspan="2">INVALID</td></tr>
  <tr><td>'amy' SIMILAR TO 'amyfred'</td><td>TRUE</td><td>6</td></tr>
  <tr><td>'fred' SIMILAR TO 'amyfred'</td><td>TRUE</td><td>6</td></tr>
  <tr><td>'mike' SIMILAR TO 'amyfred'</td><td>FALSE</td><td>6</td></tr>
  <tr><td>'acd' SIMILAR TO 'ab*c+d'</td><td>TRUE</td><td>7 &amp; 8</td></tr>
  <tr><td>'accccd' SIMILAR TO 'ab*c+d'</td><td>TRUE</td><td>7 &amp; 8</td></tr>
  <tr><td>'abd' SIMILAR TO 'ab*c+d'</td><td>FALSE</td><td>7 &amp; 8</td></tr>
  <tr><td>'aabc' SIMILAR TO 'ab*c+d'</td><td>FALSE</td><td> </td></tr>
  <tr><td>'abb' SIMILAR TO 'a(b{3})'</td><td>FALSE</td><td>9</td></tr>
  <tr><td>'abbb' SIMILAR TO 'a(b{3})'</td><td>TRUE</td><td>9</td></tr>
  <tr><td>'abbbbb' SIMILAR TO 'a(b{3})'</td><td>FALSE</td><td>9</td></tr>
  <tr><td>'abbbbb' SIMILAR TO 'ab{3,6}'</td><td>TRUE</td><td>10</td></tr>
  <tr><td>'abbbbbbbb' SIMILAR TO 'ab{3,6}'</td><td>FALSE</td><td>10</td></tr>
  <tr><td>'' SIMILAR TO 'ab?'</td><td>FALSE</td><td>11</td></tr>
  <tr><td>'' SIMILAR TO '(ab)?'</td><td>TRUE</td><td>11</td></tr>
  <tr><td>'a' SIMILAR TO 'ab?'</td><td>TRUE</td><td>11</td></tr>
  <tr><td>'a' SIMILAR TO '(ab)?'</td><td>FALSE</td><td>11</td></tr>
  <tr><td>'a' SIMILAR TO 'a(b?)'</td><td>TRUE</td><td>11</td></tr>
  <tr><td>'ab' SIMILAR TO 'ab?'</td><td>TRUE</td><td>11</td></tr>
  <tr><td>'ab' SIMILAR TO 'a(b?)'</td><td>TRUE</td><td>11</td></tr>
  <tr><td>'abb' SIMILAR TO 'ab?'</td><td>FALSE</td><td>11</td></tr>
  <tr><td>'ab' SIMILAR TO 'a\_' ESCAPE '\'</td><td>FALSE</td><td>16</td></tr>
  <tr><td>'ab' SIMILAR TO 'a\%' ESCAPE '\'</td><td>FALSE</td><td>16</td></tr>
  <tr><td>'a_' SIMILAR TO 'a\_' ESCAPE '\'</td><td>TRUE</td><td>16</td></tr>
  <tr><td>'a%' SIMILAR TO 'a\%' ESCAPE '\'</td><td>TRUE</td><td>16</td></tr>
  <tr><td>'a(b{3})' SIMILAR TO 'a(b{3})'</td><td>FALSE</td><td>16</td></tr>
  <tr><td>'a(b{3})' SIMILAR TO 'a\(b\{3\}\)' ESCAPE '\'</td><td>TRUE</td><td>16</td></tr>
</tbody>
</table>
