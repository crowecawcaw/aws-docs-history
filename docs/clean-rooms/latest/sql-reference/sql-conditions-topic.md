# AWS Clean Rooms SQL conditions

Conditions are statements of one or more expressions and logical operators that evaluate to
true, false, or unknown. Conditions are also sometimes referred to as predicates.

###### Note

All string comparisons and LIKE pattern matches are case-sensitive. For example,
'A' and 'a' do not match. However, you can do a case-insensitive pattern match by
using the ILIKE predicate.

The following SQL conditions are supported in AWS Clean Rooms.

###### Topics

- [Comparison conditions](comparison-condition.md "comparison-condition.md")
- [Logical conditions](logical-conditions.md "logical-conditions.md")
- [Pattern-matching conditions](sql-contitions-pattern-matching.md "sql-contitions-pattern-matching.md")
- [BETWEEN range condition](r_range_condition.md "r_range_condition.md")
- [Null condition](r_null_condition.md "r_null_condition.md")
- [EXISTS condition](r_exists_condition.md "r_exists_condition.md")
- [IN condition](r_in_condition.md "r_in_condition.md")
- [Syntax](#r_conditions-synopsis "#r_conditions-synopsis")

## Syntax

````
comparison_condition
| logical_condition
| range_condition
| pattern_matching_condition
| null_condition
| EXISTS_condition
| IN_condition ```
````
