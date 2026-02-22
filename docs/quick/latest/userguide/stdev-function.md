# stdev

The `stdev` function calculates the standard deviation of the set of
numbers in the specified measure, grouped by the chosen dimension or dimensions, based
on a sample.

## Syntax

```
stdev(*measure*, [*group-by level*])
```

## Arguments

_measure_

The argument must be a measure. Null values are omitted from the
results. Literal values don't work. The argument must be a field.

_group-by level_

(Optional) Specifies the level to group the aggregation by. The level
added can be any dimension or dimensions independent of the dimensions
added to the visual.

The argument must be a dimension field. The group-by level must be
enclosed in square brackets `[ ]`. For more information, see
[Level-aware calculation - aggregate (LAC-A)
functions](../../../quicksight/latest/user/level-aware-calculations-aggregate.md "../../../quicksight/latest/user/level-aware-calculations-aggregate.md").

## Examples

The following example returns the standard deviation of test scores for a class,
using a sample of the test scores recorded.

```
stdev({Score})
```

You can also specify at what level to group the computation using one or more
dimensions in the view or in your dataset. This is called a LAC-A function. For more
information about LAC-A functions, see [Level-aware calculation - aggregate (LAC-A)
functions](../../../quicksight/latest/user/level-aware-calculations-aggregate.md "../../../quicksight/latest/user/level-aware-calculations-aggregate.md"). The following example calculates the standard deviation of
test scores at the subject level, but not across other dimensions (Class) in the
visual.

```
stdev({Score}, [Subject])
```
