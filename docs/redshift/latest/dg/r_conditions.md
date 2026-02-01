Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Conditions

###### Topics

- [Syntax](#r_conditions-synopsis "#r_conditions-synopsis")
- [Comparison condition](r_comparison_condition.md "r_comparison_condition.md")
- [Logical conditions](r_logical_condition.md "r_logical_condition.md")
- [Pattern-matching conditions](pattern-matching-conditions.md "pattern-matching-conditions.md")
- [BETWEEN range condition](r_range_condition.md "r_range_condition.md")
- [Null condition](r_null_condition.md "r_null_condition.md")
- [EXISTS condition](r_exists_condition.md "r_exists_condition.md")
- [IN condition](r_in_condition.md "r_in_condition.md")
  A condition is a statement of one or more expressions and logical operators that
  evaluates to true, false, or unknown. Conditions are also sometimes referred to as
  predicates.

###### Note

All string comparisons and LIKE pattern matches are case-sensitive. For example,
'A' and 'a' do not match. However, you can do a case-insensitive pattern match by
using the ILIKE predicate.

## Syntax

```
comparison_condition
| logical_condition
| range_condition
| pattern_matching_condition
| null_condition
| EXISTS_condition
| IN_condition
```
