# Functions by category

In this section, you can find a list of the functions available in Amazon Quick Suite,
sorted by category.

###### Topics

- [Aggregate functions](#aggregate-functions "#aggregate-functions")
- [Conditional functions](#conditional-functions "#conditional-functions")
- [Date functions](#date-functions "#date-functions")
- [Numeric functions](#numeric-functions "#numeric-functions")
- [Mathematical functions](#mathematical-functions "#mathematical-functions")
- [String functions](#string-functions "#string-functions")
- [Table calculations](#table-calculations "#table-calculations")

## Aggregate functions

The aggregate functions for calculated fields in Amazon Quick Suite include the
following. These are only available during analysis and visualization. Each of these
functions returns values grouped by the chosen dimension or dimensions. For each
aggregation, there is also a conditional aggregation. These perform the same type of
aggregation, based on a condition.

- [avg](../../../quicksight/latest/user/avg-function.md "../../../quicksight/latest/user/avg-function.md") averages the set of numbers in the
  specified measure, grouped by the chosen dimension or dimensions.
- [avgIf](../../../quicksight/latest/user/avgIf-function.md "../../../quicksight/latest/user/avgIf-function.md") calculates the average
  based on a conditional statement.
- [count](../../../quicksight/latest/user/count-function.md "../../../quicksight/latest/user/count-function.md") calculates the number
  of values in a dimension or measure, grouped by the chosen dimension or
  dimensions.
- [countIf](../../../quicksight/latest/user/countIf-function.md "../../../quicksight/latest/user/countIf-function.md") calculates the count
  based on a conditional statement.
- [distinct_count](../../../quicksight/latest/user/distinct_count-function.md "../../../quicksight/latest/user/distinct_count-function.md") calculates
  the number of distinct values in a dimension or measure, grouped by the
  chosen dimension or dimensions.
- [distinct_countIf](../../../quicksight/latest/user/distinct_countIf-function.md "../../../quicksight/latest/user/distinct_countIf-function.md") calculates
  the distinct count based on a conditional statement.
- [max](../../../quicksight/latest/user/max-function.md "../../../quicksight/latest/user/max-function.md") returns the maximum value of the
  specified measure, grouped by the chosen dimension or dimensions.
- [maxIf](../../../quicksight/latest/user/maxIf-function.md "../../../quicksight/latest/user/maxIf-function.md") calculates the maximum
  based on a conditional statement.
- [median](../../../quicksight/latest/user/median-function.md "../../../quicksight/latest/user/median-function.md") returns the median
  value of the specified measure, grouped by the chosen dimension or
  dimensions.
- [medianIf](../../../quicksight/latest/user/medianIf-function.md "../../../quicksight/latest/user/medianIf-function.md") calculates the
  median based on a conditional statement.
- [min](../../../quicksight/latest/user/min-function.md "../../../quicksight/latest/user/min-function.md") returns the minimum value of the
  specified measure, grouped by the chosen dimension or dimensions.
- [minIf](../../../quicksight/latest/user/minIf-function.md "../../../quicksight/latest/user/minIf-function.md") calculates the minimum
  based on a conditional statement.
- [percentile](../../../quicksight/latest/user/percentile-function.md "../../../quicksight/latest/user/percentile-function.md") (alias of
  `percentileDisc`) computes the *n*th
  percentile of the specified measure, grouped by the chosen dimension or
  dimensions.
- [percentileCont](../../../quicksight/latest/user/percentileCont-function.md "../../../quicksight/latest/user/percentileCont-function.md") calculates
  the *n*th percentile based on a continuous distribution
  of the numbers of the specified measure, grouped by the chosen dimension or
  dimensions.
- [percentileDisc (percentile)](../../../quicksight/latest/user/percentileDisc-function.md "../../../quicksight/latest/user/percentileDisc-function.md")
  calculates the *n*th percentile based on the actual
  numbers of the specified measure, grouped by the chosen dimension or
  dimensions.
- [periodToDateAvg](../../../quicksight/latest/user/periodToDateAvg-function.md "../../../quicksight/latest/user/periodToDateAvg-function.md") averages the
  set of numbers in the specified measure for a given time granularity (for
  instance, a quarter) up to a point in time.
- [periodToDateCount](../../../quicksight/latest/user/periodToDateCount-function.md "../../../quicksight/latest/user/periodToDateCount-function.md") calculates
  the number of values in a dimension or measure for a given time granularity
  (for instance, Quarter) up to a point in time including duplicates.
- [periodToDateMax](../../../quicksight/latest/user/periodToDateMax-function.md "../../../quicksight/latest/user/periodToDateMax-function.md") returns the
  maximum value of the specified measure for a given time granularity (for
  instance, a quarter) up to a point in time.
- [periodToDateMedian](../../../quicksight/latest/user/periodToDateMedian-function.md "../../../quicksight/latest/user/periodToDateMedian-function.md") returns
  the median value of the specified measure for a given time granularity (for
  instance, a quarter) up to a point in time.
- [periodToDateMin](../../../quicksight/latest/user/periodToDateMin-function.md "../../../quicksight/latest/user/periodToDateMin-function.md") returns the
  minimum value of the specified measure or date for a given time granularity
  (for instance, a quarter) up to a point in time.
- [periodToDatePercentile](../../../quicksight/latest/user/periodToDatePercentile-function.md "../../../quicksight/latest/user/periodToDatePercentile-function.md")
  calculates the percentile based on the actual numbers in measure for a given
  time granularity (for instance, a quarter) up to a point in time.
- [periodToDatePercentileCont](../../../quicksight/latest/user/periodToDatePercentileCont-function.md "../../../quicksight/latest/user/periodToDatePercentileCont-function.md")
  calculates percentile based on a continuous distribution of the numbers in
  the measure for a given time granularity (for instance, a quarter) up to a
  point in time.
- [periodToDateStDev](../../../quicksight/latest/user/periodToDateStDev-function.md "../../../quicksight/latest/user/periodToDateStDev-function.md") calculates
  the standard deviation of the set of numbers in the specified measure for a
  given time granularity (for instance, a quarter) up to a point in time based
  on a sample.
- [periodToDateStDevP](../../../quicksight/latest/user/periodToDateStDevP-function.md "../../../quicksight/latest/user/periodToDateStDevP-function.md")
  calculates the population standard deviation of the set of numbers in the
  specified measure for a given time granularity (for instance, a quarter) up
  to a point in time based on a sample.
- [periodToDateSum](../../../quicksight/latest/user/periodToDateSum-function.md "../../../quicksight/latest/user/periodToDateSum-function.md") adds the set
  of numbers in the specified measure for a given time granularity (for
  instance, a quarter) up to a point in time.
- [periodToDateVar](../../../quicksight/latest/user/periodToDateVar-function.md "../../../quicksight/latest/user/periodToDateVar-function.md") calculates
  the sample variance of the set of numbers in the specified measure for a
  given time granularity (for instance, a quarter) up to a point in
  time.
- [periodToDateVarP](../../../quicksight/latest/user/periodToDateVarP-function.md "../../../quicksight/latest/user/periodToDateVarP-function.md") calculates
  the population variance of the set of numbers in the specified measure for a
  given time granularity (for instance, a quarter) up to a point in
  time.
- [stdev](../../../quicksight/latest/user/stdev-function.md "../../../quicksight/latest/user/stdev-function.md")) calculates the
  standard deviation of the set of numbers in the specified measure, grouped
  by the chosen dimension or dimensions, based on a sample.
- [stdevIf](../../../quicksight/latest/user/stdevIf-function.md "../../../quicksight/latest/user/stdevIf-function.md") calculates the
  sample standard deviation based on a conditional statement.
- [stdevp](../../../quicksight/latest/user/stdevp-function.md "../../../quicksight/latest/user/stdevp-function.md") calculates the
  standard deviation of the set of numbers in the specified measure, grouped
  by the chosen dimension or dimensions, based on a biased population.
- [stdevpIf](../../../quicksight/latest/user/stdevpIf-function.md "../../../quicksight/latest/user/stdevpIf-function.md") calculates the
  population deviation based on a conditional statement.
- [var](../../../quicksight/latest/user/var-function.md "../../../quicksight/latest/user/var-function.md")) calculates the variance of the set of
  numbers in the specified measure, grouped by the chosen dimension or
  dimensions, based on a sample.
- [varIf](../../../quicksight/latest/user/varIf-function.md "../../../quicksight/latest/user/varIf-function.md") calculates the sample
  variance based on a conditional statement.
- [varp](../../../quicksight/latest/user/varp-function.md "../../../quicksight/latest/user/varp-function.md")) calculates the
  variance of the set of numbers in the specified measure, grouped by the
  chosen dimension or dimensions, based on a biased population.
- [varpIf](../../../quicksight/latest/user/varpIf-function.md "../../../quicksight/latest/user/varpIf-function.md") calculates the
  population variance based on a conditional statement.
- [sum](../../../quicksight/latest/user/sum-function.md "../../../quicksight/latest/user/sum-function.md")) adds the set of numbers in the
  specified measure, grouped by the chosen dimension or dimensions.
- [sumIf](../../../quicksight/latest/user/sumIf-function.md "../../../quicksight/latest/user/sumIf-function.md")) calculates the sum
  based on a conditional statement.

## Conditional functions

The conditional functions for calculated fields in Amazon Quick Suite include the
following:

- [Coalesce](../../../quicksight/latest/user/coalesce-function.md "../../../quicksight/latest/user/coalesce-function.md") returns the value
  of the first argument that is not null.
- [Ifelse](../../../quicksight/latest/user/ifelse-function.md "../../../quicksight/latest/user/ifelse-function.md") evaluates a set of
  _if_, _then_ expression pairings,
  and returns the value of the _then_ argument for the
  first _if_ argument that evaluates to true.
- [in](../../../quicksight/latest/user/in-function.md "../../../quicksight/latest/user/in-function.md") evaluates an expression to see if it is
  in a given list of values.
- [isNotNull](../../../quicksight/latest/user/isNotNull-function.md "../../../quicksight/latest/user/isNotNull-function.md") evaluates an
  expression to see if it is not null.
- [isNull](../../../quicksight/latest/user/isNull-function.md "../../../quicksight/latest/user/isNull-function.md") evaluates an
  expression to see if it is null. If the expression is null,
  `isNull` returns true, and otherwise it returns false.
- [notIn](../../../quicksight/latest/user/notIn-function.md "../../../quicksight/latest/user/notIn-function.md") evaluates an
  expression to see if it is not in a given list of values.
- [nullIf](../../../quicksight/latest/user/nullIf-function.md "../../../quicksight/latest/user/nullIf-function.md") compares two
  expressions. If they are equal, the function returns null. If they are not
  equal, the function returns the first expression.
- [switch](../../../quicksight/latest/user/switch-function.md "../../../quicksight/latest/user/switch-function.md") returns an expression
  that matches the first label equal to the condition expression.

## Date functions

The date functions for calculated fields in Amazon Quick Suite include the
following:

- [addDateTime](../../../quicksight/latest/user/addDateTime-function.md "../../../quicksight/latest/user/addDateTime-function.md") adds or
  subtracts a unit of time to the date or time provided.
- [addWorkDays](../../../quicksight/latest/user/addWorkDays-function.md "../../../quicksight/latest/user/addWorkDays-function.md") adds or
  subtracts the given number of work days to the date or time provided.
- [dateDiff](../../../quicksight/latest/user/dateDiff-function.md "../../../quicksight/latest/user/dateDiff-function.md") returns the
  difference in days between two date fields.
- [epochDate](../../../quicksight/latest/user/epochDate-function.md "../../../quicksight/latest/user/epochDate-function.md") converts an epoch
  date into a standard date.
- [Extract](../../../quicksight/latest/user/extract-function.md "../../../quicksight/latest/user/extract-function.md") returns a specified
  portion of a date value.
- [formatDate](../../../quicksight/latest/user/formatDate-function.md "../../../quicksight/latest/user/formatDate-function.md") formats a date
  using a pattern you specify.
- [isWorkDay](../../../quicksight/latest/user/isWorkDay-function.md "../../../quicksight/latest/user/isWorkDay-function.md") returns TRUE if a
  given date-time value is a work or business day.
- [netWorkDays](../../../quicksight/latest/user/netWorkDays-function.md "../../../quicksight/latest/user/netWorkDays-function.md") returns the
  number of working days between the provided two date values.
- [Now](../../../quicksight/latest/user/now-function.md "../../../quicksight/latest/user/now-function.md") returns the current date and time, using
  either settings for a database, or UTC for file and Salesforce.
- [truncDate](../../../quicksight/latest/user/truncDate-function.md "../../../quicksight/latest/user/truncDate-function.md") returns a date
  value that represents a specified portion of a date.

## Numeric functions

The numeric functions for calculated fields in Amazon Quick Suite include the
following:

- [Ceil](../../../quicksight/latest/user/ceil-function.md "../../../quicksight/latest/user/ceil-function.md") rounds a decimal value
  to the next highest integer.
- [decimalToInt](../../../quicksight/latest/user/decimalToInt-function.md "../../../quicksight/latest/user/decimalToInt-function.md") converts a
  decimal value to an integer.
- [Floor](../../../quicksight/latest/user/floor-function.md "../../../quicksight/latest/user/floor-function.md") decrements a decimal
  value to the next lowest integer.
- [intToDecimal](../../../quicksight/latest/user/intToDecimal-function.md "../../../quicksight/latest/user/intToDecimal-function.md") converts an
  integer value to a decimal.
- [Round](../../../quicksight/latest/user/round-function.md "../../../quicksight/latest/user/round-function.md") rounds a decimal value
  to the closest integer or, if scale is specified, to the closest decimal
  place.

## Mathematical functions

The mathematical functions for calculated fields in Amazon Quick Suite include the
following:

- `Mod(`number`,
`divisor`)` – Finds the
  remainder after dividing a number by a divisor.
- `Log(`expression`)` – Returns the base 10 logarithm of a given expression.
- `Ln(`expression`)` – Returns the natural logarithm of a given expression.
- `Abs(`expression`)` – Returns the absolute value of a given expression.
- `Sqrt(`expression`)` – Returns the square root of a given expression.
- `Exp(`expression`)` – Returns the base of natural log _e_ raised to the power of a given expression.

## String functions

The string (text) functions for calculated fields in Amazon Quick Suite include the
following:

- [Concat](../../../quicksight/latest/user/concat-function.md "../../../quicksight/latest/user/concat-function.md") concatenates two or
  more strings.
- [contains](../../../quicksight/latest/user/contains-function.md "../../../quicksight/latest/user/contains-function.md") checks if an
  expression contains a substring.
- [endsWith](../../../quicksight/latest/user/endsWith-function.md "../../../quicksight/latest/user/endsWith-function.md") checks if the
  expression ends with the substring specified.
- [Left](../../../quicksight/latest/user/left-function.md "../../../quicksight/latest/user/left-function.md") returns the specified
  number of leftmost characters from a string.
- [Locate](../../../quicksight/latest/user/locate-function.md "../../../quicksight/latest/user/locate-function.md") locates a substring
  within another string, and returns the number of characters before the
  substring.
- [Ltrim](../../../quicksight/latest/user/ltrim-function.md "../../../quicksight/latest/user/ltrim-function.md") removes preceding
  blank space from a string.
- [parseDate](../../../quicksight/latest/user/parseDate-function.md "../../../quicksight/latest/user/parseDate-function.md") parses a string to
  determine if it contains a date value, and returns the date if found.
- [parseDecimal](../../../quicksight/latest/user/parseDecimal-function.md "../../../quicksight/latest/user/parseDecimal-function.md") parses a string
  to determine if it contains a decimal value.
- [parseInt](../../../quicksight/latest/user/parseInt-function.md "../../../quicksight/latest/user/parseInt-function.md") parses a string to
  determine if it contains an integer value.
- [parseJson](../../../quicksight/latest/user/parseJson-function.md "../../../quicksight/latest/user/parseJson-function.md") parses values from
  a native JSON or from a JSON object in a text field.
- [Replace](../../../quicksight/latest/user/replace-function.md "../../../quicksight/latest/user/replace-function.md") replaces part of a
  string with a new string.
- [Right](../../../quicksight/latest/user/right-function.md "../../../quicksight/latest/user/right-function.md") returns the specified
  number of rightmost characters from a string.
- [Rtrim](../../../quicksight/latest/user/rtrim-function.md "../../../quicksight/latest/user/rtrim-function.md") removes following
  blank space from a string.
- [Split](../../../quicksight/latest/user/split-function.md "../../../quicksight/latest/user/split-function.md") splits a string into
  an array of substrings, based on a delimiter that you choose, and returns
  the item specified by the position.
- [startsWith](../../../quicksight/latest/user/startsWith-function.md "../../../quicksight/latest/user/startsWith-function.md") checks if the
  expression starts with the substring specified.
- [Strlen](../../../quicksight/latest/user/strlen-function.md "../../../quicksight/latest/user/strlen-function.md") returns the number of
  characters in a string.
- [Substring](../../../quicksight/latest/user/substring-function.md "../../../quicksight/latest/user/substring-function.md") returns the
  specified number of characters in a string, starting at the specified
  location.
- [toLower](../../../quicksight/latest/user/toLower-function.md "../../../quicksight/latest/user/toLower-function.md") formats a string in
  all lowercase.
- [toString](../../../quicksight/latest/user/toString-function.md "../../../quicksight/latest/user/toString-function.md") formats the input
  expression as a string.
- [toUpper](../../../quicksight/latest/user/toUpper-function.md "../../../quicksight/latest/user/toUpper-function.md") formats a string in
  all uppercase.
- [trim](../../../quicksight/latest/user/trim-function.md "../../../quicksight/latest/user/trim-function.md") removes both preceding
  and following blank space from a string.

## Table calculations

Table calculations form a group of functions that provide context in an analysis.
They provide support for enriched aggregated analysis. By using these calculations,
you can address common business scenarios such as calculating percentage of total,
running sum, difference, common baseline, and rank.

When you are analyzing data in a specific visual, you can apply table calculations
to the current set of data to discover how dimensions influence measures or each
other. Visualized data is your result set based on your current dataset, with all
the filters, field selections, and customizations applied. To see exactly what this
result set is, you can export your visual to a file. A table calculation function
performs operations on the data to reveal relationships between fields.

**Lookup-based functions**

- [difference](../../../quicksight/latest/user/difference-function.md "../../../quicksight/latest/user/difference-function.md") calculates the
  difference between a measure based on one set of partitions and
  sorts, and a measure based on another.
- [lag](../../../quicksight/latest/user/lag-function.md "../../../quicksight/latest/user/lag-function.md") calculates the lag (previous) value for
  a measure.
- [lead](../../../quicksight/latest/user/lead-function.md "../../../quicksight/latest/user/lead-function.md") calculates the lead
  (following) value for a measure.
- [percentDifference](../../../quicksight/latest/user/percentDifference-function.md "../../../quicksight/latest/user/percentDifference-function.md") calculates
  the percentage difference between the current value and a comparison
  value.

**Over functions**

- [avgOver](../../../quicksight/latest/user/avgOver-function.md "../../../quicksight/latest/user/avgOver-function.md") calculates the
  average of a measure over one or more dimensions.
- [countOver](../../../quicksight/latest/user/countOver-function.md "../../../quicksight/latest/user/countOver-function.md") calculates the
  count of a field over one or more dimensions.
- [distinctCountOver](../../../quicksight/latest/user/distinctCountOver-function.md "../../../quicksight/latest/user/distinctCountOver-function.md") calculates
  the distinct count of the operand partitioned by the specified attributes at
  a specified level.
- [maxOver](../../../quicksight/latest/user/maxOver-function.md "../../../quicksight/latest/user/maxOver-function.md") calculates the
  maximum of a measure over one or more dimensions.
- [minOver](../../../quicksight/latest/user/minOver-function.md "../../../quicksight/latest/user/minOver-function.md") the minimum of a
  measure over one or more dimensions.
- [percentileOver](../../../quicksight/latest/user/percentileOver-function.md "../../../quicksight/latest/user/percentileOver-function.md") (alias of
  `percentileDiscOver`) calculates the *n*th
  percentile of a measure partitioned by a list of dimensions.
- [percentileContOver](../../../quicksight/latest/user/percentileContOver-function.md "../../../quicksight/latest/user/percentileContOver-function.md")
  calculates the *n*th percentile based on a continuous
  distribution of the numbers of a measure partitioned by a list of
  dimensions.
- [percentileDiscOver](../../../quicksight/latest/user/percentileDiscOver-function.md "../../../quicksight/latest/user/percentileDiscOver-function.md")
  calculates the *n*th percentile based on the actual
  numbers of a measure partitioned by a list of dimensions.
- [percentOfTotal](../../../quicksight/latest/user/percentOfTotal-function.md "../../../quicksight/latest/user/percentOfTotal-function.md") calculates
  the percentage that a measure contributes to the total.
- [periodOverPeriodDifference](../../../quicksight/latest/user/periodOverPeriodDifference-function.md "../../../quicksight/latest/user/periodOverPeriodDifference-function.md")
  calculates the difference of a measure over two different time periods as
  specified by period granularity and offset.
- [periodOverPeriodLastValue](../../../quicksight/latest/user/periodOverPeriodLastValue-function.md "../../../quicksight/latest/user/periodOverPeriodLastValue-function.md")
  calculates the last (previous) value of a measure from a previous time
  period as specified by period granularity and offset.
- [periodOverPeriodPercentDifference](../../../quicksight/latest/user/periodOverPeriodPercentDifference-function.md "../../../quicksight/latest/user/periodOverPeriodPercentDifference-function.md") calculates the
  percent difference of a measure over two different time periods as specified
  by period granularity and offset.
- [periodToDateAvgOverTime](../../../quicksight/latest/user/periodToDateAvgOverTime-function.md "../../../quicksight/latest/user/periodToDateAvgOverTime-function.md")
  calculates the average of a measure for a given time granularity (for
  instance, a quarter) up to a point in time.
- [periodToDateCountOverTime](../../../quicksight/latest/user/periodToDateCountOverTime-function.md "../../../quicksight/latest/user/periodToDateCountOverTime-function.md")
  calculates the count of a dimension or measure for a given time granularity
  (for instance, a quarter) up to a point in time.
- [periodToDateMaxOverTime](../../../quicksight/latest/user/periodToDateMaxOverTime-function.md "../../../quicksight/latest/user/periodToDateMaxOverTime-function.md")
  calculates the maximum of a measure or date for a given time granularity
  (for instance, a quarter) up to a point in time.
- [periodToDateMinOverTime](../../../quicksight/latest/user/periodToDateMinOverTime-function.md "../../../quicksight/latest/user/periodToDateMinOverTime-function.md")
  calculates the minimum of a measure or date for a given time granularity
  (for instance, a quarter) up to a point in time.
- [periodToDateSumOverTime](../../../quicksight/latest/user/periodToDateSumOverTime-function.md "../../../quicksight/latest/user/periodToDateSumOverTime-function.md")
  calculates the sum of a measure for a given time granularity (for instance,
  a quarter) up to a point in time.
- [sumOver](../../../quicksight/latest/user/sumOver-function.md "../../../quicksight/latest/user/sumOver-function.md") calculates the sum
  of a measure over one or more dimensions.
- [stdevOver](../../../quicksight/latest/user/stdevOver-function.md "../../../quicksight/latest/user/stdevOver-function.md") calculates the
  standard deviation of the specified measure, partitioned by the chosen
  attribute or attributes, based on a sample.
- [stdevpOver](../../../quicksight/latest/user/stdevpOver-function.md "../../../quicksight/latest/user/stdevpOver-function.md") calculates the
  standard deviation of the specified measure, partitioned by the chosen
  attribute or attributes, based on a biased population.
- [varOver](../../../quicksight/latest/user/varOver-function.md "../../../quicksight/latest/user/varOver-function.md") calculates the
  variance of the specified measure, partitioned by the chosen attribute or
  attributes, based on a sample.
- [varpOver](../../../quicksight/latest/user/varpOver-function.md "../../../quicksight/latest/user/varpOver-function.md") calculates the
  variance of the specified measure, partitioned by the chosen attribute or
  attributes, based on a biased population.

**Ranking functions**

- [rank](../../../quicksight/latest/user/rank-function.md "../../../quicksight/latest/user/rank-function.md") calculates the rank of
  a measure or a dimension.
- [denseRank](../../../quicksight/latest/user/denseRank-function.md "../../../quicksight/latest/user/denseRank-function.md") calculates the
  rank of a measure or a dimension, ignoring duplicates.
- [percentileRank](../../../quicksight/latest/user/percentileRank-function.md "../../../quicksight/latest/user/percentileRank-function.md") calculates
  the rank of a measure or a dimension, based on percentile.

**Running functions**

- [runningAvg](../../../quicksight/latest/user/runningAvg-function.md "../../../quicksight/latest/user/runningAvg-function.md") calculates a
  running average for a measure.
- [runningCount](../../../quicksight/latest/user/runningCount-function.md "../../../quicksight/latest/user/runningCount-function.md") calculates a
  running count for a measure.
- [runningMax](../../../quicksight/latest/user/runningMax-function.md "../../../quicksight/latest/user/runningMax-function.md") calculates a
  running maximum for a measure.
- [runningMin](../../../quicksight/latest/user/runningMin-function.md "../../../quicksight/latest/user/runningMin-function.md") calculates a
  running minimum for a measure.
- [runningSum](../../../quicksight/latest/user/runningSum-function.md "../../../quicksight/latest/user/runningSum-function.md") calculates a
  running sum for a measure.

**Window functions**

- [firstValue](../../../quicksight/latest/user/firstValue-function.md "../../../quicksight/latest/user/firstValue-function.md") calculates the
  first value of the aggregated measure or dimension partitioned and sorted by
  specified attributes.
- [lastValue](../../../quicksight/latest/user/lastValue-function.md "../../../quicksight/latest/user/lastValue-function.md") calculates the
  last value of the aggregated measure or dimension partitioned and sorted by
  specified attributes.
- [windowAvg](../../../quicksight/latest/user/windowAvg-function.md "../../../quicksight/latest/user/windowAvg-function.md") calculates the
  average of the aggregated measure in a custom window that is partitioned and
  sorted by specified attributes.
- [windowCount](../../../quicksight/latest/user/windowCount-function.md "../../../quicksight/latest/user/windowCount-function.md") calculates the
  count of the aggregated measure in a custom window that is partitioned and
  sorted by specified attributes.
- [windowMax](../../../quicksight/latest/user/windowMax-function.md "../../../quicksight/latest/user/windowMax-function.md") calculates the
  maximum of the aggregated measure in a custom window that is partitioned and
  sorted by specified attributes.
- [windowMin](../../../quicksight/latest/user/windowMin-function.md "../../../quicksight/latest/user/windowMin-function.md") calculates the
  minimum of the aggregated measure in a custom window that is partitioned and
  sorted by specified attributes.
- [windowSum](../../../quicksight/latest/user/windowSum-function.md "../../../quicksight/latest/user/windowSum-function.md") calculates the sum
  of the aggregated measure in a custom window that is partitioned and sorted
  by specified attributes.
