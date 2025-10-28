# minIf

Based on a conditional statement, the `minIf` function returns the minimum
value of the specified measure, grouped by the chosen dimension or dimensions. For
example, `minIf(ProdRev,CalendarDay >= ${BasePeriodStartDate} AND CalendarDay <=
 ${BasePeriodEndDate} AND SourcingType <> 'Indirect')` returns the minimum
rate of returns grouped by the (optional) chosen dimension, if the condition evaluates
to true.

## Syntax

```
minIf(*measure, condition*)
```

## Arguments

_measure_

The argument must be a measure. Null values are omitted from the
results. Literal values don't work. The argument must be a field.

_condition_

One or more conditions in a single statement.
