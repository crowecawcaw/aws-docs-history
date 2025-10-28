# varpIf

Based on a conditional statement, the `varpIf` function calculates the
variance of the set of numbers in the specified measure, grouped by the chosen dimension
or dimensions, based on a biased population.

## Syntax

```
varpIf(*measure, conditions*)
```

## Arguments

_measure_

The argument must be a measure. Null values are omitted from the
results. Literal values don't work. The argument must be a field.

_condition_

One or more conditions in a single statement.
