

# distinct\_countIf
<a name="distinct_countIf-function"></a>

Based on a conditional statement, the `distinct_countIf` function calculates the number of distinct values in a dimension or measure, grouped by the chosen dimension or dimensions. For example, `distinct_countIf(product type)` returns the total number of unique product types grouped by the (optional) chosen dimension, without any duplicates. The `distinct_countIf(ProdRev,CalendarDay >= ${BasePeriodStartDate} AND CalendarDay <= ${BasePeriodEndDate} AND SourcingType <> 'Indirect')` function returns the total number of dates when products were shipped grouped by the (optional) chosen dimension, for example region, if the condition evaluates to true.

## Syntax
<a name="distinct_countIf-function-syntax"></a>

```
distinct_countIf(dimension or measure, condition)
```

## Arguments
<a name="distinct_countIf-function-arguments"></a>

 *dimension or measure*   
The argument must be a measure or a dimension. Null values are omitted from the results. Literal values don't work. The argument must be a field.

 *condition*   
One or more conditions in a single statement.