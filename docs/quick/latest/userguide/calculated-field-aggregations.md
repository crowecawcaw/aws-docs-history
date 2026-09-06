

# Aggregate functions
<a name="calculated-field-aggregations"></a>

Aggregate functions are only available during analysis and visualization. Each of these functions returns values grouped by the chosen dimension or dimensions. For each aggregation, there is also a conditional aggregation. These perform the same type of aggregation, based on a condition.

When a calculated field formula contains an aggregation, it becomes a custom aggregation. To make sure that your data is accurately displayed, Amazon Quick applies the following rules:
+ Custom aggregations can't contain nested aggregate functions. For example, this formula doesn't work: `sum(avg(x)/avg(y))`. However, nesting nonaggregated functions inside or outside aggregate functions does work. For example, `ceil(avg(x))` works. So does `avg(ceil(x))`.
+ Custom aggregations can't contain both aggregated and nonaggregated fields, in any combination. For example, this formula doesn't work: `Sum(sales)+quantity`.
+ Filter groups can't contain both aggregated and nonaggregated fields.
+ Custom aggregations can't be converted to a dimension. They also can't be dropped into the field well as a dimension.
+ In a pivot table, custom aggregations can't be added to table calculations.
+ Scatter plots with custom aggregations need at least one dimension under **Group/Color** in the field wells.

For more information about supported functions and operators, see [Calculated field function and operator reference for Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/calculated-field-reference.html). 

The aggregate functions for calculated fields in Quick include the following.

**Topics**
+ [avg](avg-function.md)
+ [avgIf](avgIf-function.md)
+ [count](count-function.md)
+ [countIf](countIf-function.md)
+ [distinct\_count](distinct_count-function.md)
+ [distinct\_countIf](distinct_countIf-function.md)
+ [max](max-function.md)
+ [maxIf](maxIf-function.md)
+ [median](median-function.md)
+ [medianIf](medianIf-function.md)
+ [min](min-function.md)
+ [minIf](minIf-function.md)
+ [percentile](percentile-function.md)
+ [percentileCont](percentileCont-function.md)
+ [percentileDisc (percentile)](percentileDisc-function.md)
+ [periodToDateAvg](periodToDateAvg-function.md)
+ [periodToDateCount](periodToDateCount-function.md)
+ [periodToDateMax](periodToDateMax-function.md)
+ [periodToDateMedian](periodToDateMedian-function.md)
+ [periodToDateMin](periodToDateMin-function.md)
+ [periodToDatePercentile](periodToDatePercentile-function.md)
+ [periodToDatePercentileCont](periodToDatePercentileCont-function.md)
+ [periodToDateStDev](periodToDateStDev-function.md)
+ [periodToDateStDevP](periodToDateStDevP-function.md)
+ [periodToDateSum](periodToDateSum-function.md)
+ [periodToDateVar](periodToDateVar-function.md)
+ [periodToDateVarP](periodToDateVarP-function.md)
+ [stdev](stdev-function.md)
+ [stdevp](stdevp-function.md)
+ [stdevIf](stdevIf-function.md)
+ [stdevpIf](stdevpIf-function.md)
+ [sum](sum-function.md)
+ [sumIf](sumIf-function.md)
+ [var](var-function.md)
+ [varIf](varIf-function.md)
+ [varp](varp-function.md)
+ [varpIf](varpIf-function.md)