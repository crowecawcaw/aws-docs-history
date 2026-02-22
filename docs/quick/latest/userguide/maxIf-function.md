# maxIf

Based on a conditional statement, the `maxIf` function returns the maximum
value of the specified measure, grouped by the chosen dimension or dimensions. For
example, `maxIf(ProdRev,CalendarDay >= ${BasePeriodStartDate} AND CalendarDay <=
 ${BasePeriodEndDate} AND SourcingType <> 'Indirect')` returns the maximum
sales goals grouped by the (optional) chosen dimension, if the condition evaluates to
true.

## Syntax

```
maxIf(*measure, condition*)
```

## Arguments

_measure_

The argument must be a measure. Null values are omitted from the
results. Literal values don't work. The argument must be a field.

_condition_

One or more conditions in a single statement.
