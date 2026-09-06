

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Conditions
<a name="r_conditions"></a>

**Topics**
+ [Syntax](#r_conditions-synopsis)
+ [Comparison condition](r_comparison_condition.md)
+ [Logical conditions](r_logical_condition.md)
+ [Pattern-matching conditions](pattern-matching-conditions.md)
+ [BETWEEN range condition](r_range_condition.md)
+ [Null condition](r_null_condition.md)
+ [EXISTS condition](r_exists_condition.md)
+ [IN condition](r_in_condition.md)

 A condition is a statement of one or more expressions and logical operators that evaluates to true, false, or unknown. Conditions are also sometimes referred to as predicates.

**Note**  
All string comparisons and LIKE pattern matches are case-sensitive. For example, 'A' and 'a' do not match. However, you can do a case-insensitive pattern match by using the ILIKE predicate.

## Syntax
<a name="r_conditions-synopsis"></a>

```
comparison_condition
| logical_condition
| range_condition
| pattern_matching_condition
| null_condition
| EXISTS_condition
| IN_condition
```