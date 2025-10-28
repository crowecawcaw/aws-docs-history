# Pattern-matching conditions

A pattern-matching operator searches a string for a pattern specified in the conditional
expression and returns true or false depending on whether it finds a match. AWS Clean Rooms Spark SQL uses
the following methods for pattern matching:

- LIKE expressions

The LIKE operator compares a string expression, such as a column name, with a pattern that
uses the wildcard characters `%` (percent) and `_` (underscore). LIKE
pattern matching always covers the entire string. LIKE performs a case-sensitive match.

###### Topics

- [LIKE](patternmatching_condition_like.md "patternmatching_condition_like.md")
- [RLIKE](RLIKE.md "RLIKE.md")
