# medianIf

Based on a conditional statement, the `medianIf` aggregation returns the
median value of the specified measure, grouped by the chosen dimension or dimensions.
For example, `medianIf(Revenue,SaleDate >= ${BasePeriodStartDate} AND SaleDate
 <= ${BasePeriodEndDate})` returns the median revenue grouped by the
(optional) chosen dimension, if the condition evaluates to true.

## Syntax

```
medianIf(`measure`, `condition`)
```

## Arguments

_measure_

The argument must be a measure. Null values are omitted from the
results. Literal values don't work. The argument must be a field.

_condition_

One or more conditions in a single statement.
