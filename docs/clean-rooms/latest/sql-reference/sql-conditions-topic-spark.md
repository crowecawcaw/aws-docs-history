# AWS Clean Rooms Spark SQL conditions

Conditions are statements of one or more expressions and logical operators that evaluate to
true, false, or unknown. Conditions are also sometimes referred to as predicates.

**Syntax**

```
comparison_condition
| logical_condition
| range_condition
| pattern_matching_condition
| null_condition
| EXISTS_condition
| IN_condition
```

###### Note

All string comparisons and LIKE pattern matches are case-sensitive. For example,
'A' and 'a' do not match. However, you can do a case-insensitive pattern match by
using the ILIKE predicate.

The following SQL conditions are supported in AWS Clean Rooms Spark SQL.

###### Topics

- [Comparison operators](comparison-operators.md "comparison-operators.md")
- [Logical conditions](logical-conditions-spark.md "logical-conditions-spark.md")
- [Pattern-matching conditions](sql-contitions-pattern-matching-spark.md "sql-contitions-pattern-matching-spark.md")
- [BETWEEN range condition](range_condition-spark.md "range_condition-spark.md")
- [Null condition](null_condition-spark.md "null_condition-spark.md")
- [EXISTS condition](exists_condition.md "exists_condition.md")
- [IN condition](in_condition-spark.md "in_condition-spark.md")
