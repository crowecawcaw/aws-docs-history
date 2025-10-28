# runningCount

The `runningCount` function calculates a running count for a measure or
dimension, based on the specified dimensions and sort orders.

## Syntax

The brackets are required. To see which arguments are optional, see the following
descriptions.

```
runningCount
(
  `measure_or_dimension`
  ,`[ sortorder_field ASC_or_DESC, ... ]`
  ,`[ partition_field, ... ]`
**)**
```

## Arguments

_measure or dimension_

An aggregated measure or dimension that you want to see the running
count for.

_sort order field_

One or more measures and dimensions that you want to sort the data by,
separated by commas. You can specify either ascending
(`ASC`) or descending
(`DESC`) sort order.

Each field in the list is enclosed in {} (curly braces), if it is more
than one word. The entire list is enclosed in [ ] (square
brackets).

_partition field_

(Optional) One or more dimensions that you want to partition by,
separated by commas.

Each field in the list is enclosed in {} (curly braces), if it is more
than one word. The entire list is enclosed in [ ] (square
brackets).

## Example

The following example calculates a running count of `sum(Sales)`,
sorted by `Sales`, partitioned by `City` and
`State`.

```
runningCount
(
  sum(Sales),
  [Sales ASC],
  [City, State]
)
```

The following example calculates a running count of `Billed Amount`,
sorted by month (`[truncDate("MM",Date) ASC]`). The fields in the table
calculation are in the field wells of the visual.

```
runningCount
(
  sum({Billed Amount}),
  [truncDate("MM",Date) ASC]
)
```
