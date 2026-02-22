# Aggregate functions

Aggregate functions are only available during analysis and visualization. Each of these
functions returns values grouped by the chosen dimension or dimensions. For each
aggregation, there is also a conditional aggregation. These perform the same type of
aggregation, based on a condition.

When a calculated field formula contains an aggregation, it becomes a custom aggregation.
To make sure that your data is accurately displayed, Amazon Quick applies the following
rules:

- Custom aggregations can't contain nested aggregate functions. For example, this
  formula doesn't work: `sum(avg(x)/avg(y))`. However, nesting
  nonaggregated functions inside or outside aggregate functions does work. For
  example, `ceil(avg(x))` works. So does `avg(ceil(x))`.
- Custom aggregations can't contain both aggregated and nonaggregated fields, in any
  combination. For example, this formula doesn't work:
  `Sum(sales)+quantity`.
- Filter groups can't contain both aggregated and nonaggregated fields.
- Custom aggregations can't be converted to a dimension. They also can't be dropped
  into the field well as a dimension.
- In a pivot table, custom aggregations can't be added to table calculations.
- Scatter plots with custom aggregations need at least one dimension under
  **Group/Color** in the field wells.
  For more information about supported functions and operators, see [Calculated field function and operator reference for Amazon Quick](../../../quicksight/latest/user/calculated-field-reference.md "../../../quicksight/latest/user/calculated-field-reference.md").

The aggregate functions for calculated fields in Quick include the
following.

###### Topics

- [avg](avg-function.md "avg-function.md")
- [avgIf](avgIf-function.md "avgIf-function.md")
- [count](count-function.md "count-function.md")
- [countIf](countIf-function.md "countIf-function.md")
- [distinct_count](distinct_count-function.md "distinct_count-function.md")
- [distinct_countIf](distinct_countIf-function.md "distinct_countIf-function.md")
- [max](max-function.md "max-function.md")
- [maxIf](maxIf-function.md "maxIf-function.md")
- [median](median-function.md "median-function.md")
- [medianIf](medianIf-function.md "medianIf-function.md")
- [min](min-function.md "min-function.md")
- [minIf](minIf-function.md "minIf-function.md")
- [percentile](percentile-function.md "percentile-function.md")
- [percentileCont](percentileCont-function.md "percentileCont-function.md")
- [percentileDisc
  (percentile)](percentileDisc-function.md "percentileDisc-function.md")
- [periodToDateAvg](periodToDateAvg-function.md "periodToDateAvg-function.md")
- [periodToDateCount](periodToDateCount-function.md "periodToDateCount-function.md")
- [periodToDateMax](periodToDateMax-function.md "periodToDateMax-function.md")
- [periodToDateMedian](periodToDateMedian-function.md "periodToDateMedian-function.md")
- [periodToDateMin](periodToDateMin-function.md "periodToDateMin-function.md")
- [periodToDatePercentile](periodToDatePercentile-function.md "periodToDatePercentile-function.md")
- [periodToDatePercentileCont](periodToDatePercentileCont-function.md "periodToDatePercentileCont-function.md")
- [periodToDateStDev](periodToDateStDev-function.md "periodToDateStDev-function.md")
- [periodToDateStDevP](periodToDateStDevP-function.md "periodToDateStDevP-function.md")
- [periodToDateSum](periodToDateSum-function.md "periodToDateSum-function.md")
- [periodToDateVar](periodToDateVar-function.md "periodToDateVar-function.md")
- [periodToDateVarP](periodToDateVarP-function.md "periodToDateVarP-function.md")
- [stdev](stdev-function.md "stdev-function.md")
- [stdevp](stdevp-function.md "stdevp-function.md")
- [stdevIf](stdevIf-function.md "stdevIf-function.md")
- [stdevpIf](stdevpIf-function.md "stdevpIf-function.md")
- [sum](sum-function.md "sum-function.md")
- [sumIf](sumIf-function.md "sumIf-function.md")
- [var](var-function.md "var-function.md")
- [varIf](varIf-function.md "varIf-function.md")
- [varp](varp-function.md "varp-function.md")
- [varpIf](varpIf-function.md "varpIf-function.md")
