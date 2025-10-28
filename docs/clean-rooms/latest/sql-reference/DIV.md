# DIV function

The DIV operator returns the integral part of the division of dividend by divisor.

## Syntax

```
dividend div divisor

```

## Arguments

_dividend_

An expression that evaluates to a numeric or interval.

_divisor_

A matching interval type if `dividend` is an interval, a numeric
otherwise.

## Return type

`BIGINT`

## Examples

The following example selects two columns from the squirrels table: the
`id` column, which contains the unique identifier for each squirrel, and a
`calculated` column, `age div 2`, which represents the integer
division of the age column by 2. The `age div 2` calculation performs integer
division on the `age` column, effectively rounding down the age to the
nearest even integer. For example, if the `age` column contains values like
3, 5, 7, and 10, the `age div 2` column would contain the values 1, 2, 3, and
5, respectively.

```
SELECT id, age div 2 FROM squirrels
```

This query can be useful in scenarios where you need to group or analyze data based
on age ranges, and you want to simplify the age values by rounding them down to the
nearest even integer. The resulting output would provide the `id` and the age
divided by 2 for each squirrel in the `squirrels` table.
