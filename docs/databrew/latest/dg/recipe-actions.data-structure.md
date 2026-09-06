

# Data structure recipe steps
<a name="recipe-actions.data-structure"></a>

Use these recipe steps to tabulate and summarize data from different perspectives, or to perform advanced functions.

**Topics**
+ [NEST\_TO\_ARRAY](recipe-actions.NEST_TO_ARRAY.md)
+ [NEST\_TO\_MAP](recipe-actions.NEST_TO_MAP.md)
+ [NEST\_TO\_STRUCT](recipe-actions.NEST_TO_STRUCT.md)
+ [UNNEST\_ARRAY](recipe-actions.UNNEST_ARRAY.md)
+ [UNNEST\_MAP](recipe-actions.UNNEST_MAP.md)
+ [UNNEST\_STRUCT](recipe-actions.UNNEST_STRUCT.md)
+ [UNNEST\_STRUCT\_N](recipe-actions.UNNEST_STRUCT_N.md)
+ [GROUP\_BY](recipe-actions.GROUP_BY.md)
+ [JOIN](recipe-actions.JOIN.md)
+ [PIVOT](recipe-actions.PIVOT.md)
+ [SCALE](#recipe-actions.SCALE)
+ [TRANSPOSE](recipe-actions.TRANSPOSE.md)
+ [UNION](recipe-actions.UNION.md)
+ [UNPIVOT](recipe-actions.UNPIVOT.md)

## SCALE
<a name="recipe-actions.SCALE"></a>

Scales or normalizes the range of data in a numeric column.

**Parameters**
+ `sourceColumn` — The name of an existing column.
+ `strategy` — The operation to be applied to the column values:
  + `MIN_MAX` — Rescales the values into a range of [0,1].
  + `SCALE_BETWEEN` — Rescales the values into a range of two specified values.
  +  `MEAN_NORMALIZATION` — Rescales the data to have a mean (μ) of 0 and standard deviation (σ) of 1 within a range of [-1, 1].
  +  `Z_SCORE` — Linearly scales data values to have a mean (μ) of 0 and standard deviation (σ) of 1. Best for handling outliers.
+ `targetColumn` — The name of a column to contain the results.

**Example**  
  

```
{
    "Action": {
        "Operation": "NORMALIZATION",
        "Parameters": {
            "sourceColumn": "all_votes",
            "strategy": "MIN_MAX",
            "targetColumn": "all_votes_normalized"
        }
    }
}
```