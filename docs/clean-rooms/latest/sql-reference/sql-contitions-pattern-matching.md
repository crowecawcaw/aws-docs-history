# Pattern-matching conditions

A pattern-matching operator searches a string for a pattern specified in the conditional
expression and returns true or false depending on whether it finds a match. AWS Clean Rooms uses the
following methods for pattern matching:

- LIKE expressions

The LIKE operator compares a string expression, such as a column name, with a pattern that
uses the wildcard characters `%` (percent) and `_` (underscore). LIKE
pattern matching always covers the entire string. LIKE performs a case-sensitive match.

- SIMILAR TO regular expressions

The SIMILAR TO operator matches a string expression with a SQL standard regular expression
pattern, which can include a set of pattern-matching metacharacters that includes the two
supported by the LIKE operator. SIMILAR TO matches the entire string and performs a
case-sensitive match.

###### Topics

- [LIKE](r_patternmatching_condition_like.md "r_patternmatching_condition_like.md")
- [SIMILAR TO](r_pattern-matching-conditions-similar-to.md "r_pattern-matching-conditions-similar-to.md")
