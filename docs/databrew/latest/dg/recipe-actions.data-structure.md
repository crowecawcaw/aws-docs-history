# Data structure recipe steps

Use these recipe steps to tabulate and summarize data from different perspectives, or to
perform advanced functions.

###### Topics

- [NEST_TO_ARRAY](recipe-actions.NEST_TO_ARRAY.md "recipe-actions.NEST_TO_ARRAY.md")
- [NEST_TO_MAP](recipe-actions.NEST_TO_MAP.md "recipe-actions.NEST_TO_MAP.md")
- [NEST_TO_STRUCT](recipe-actions.NEST_TO_STRUCT.md "recipe-actions.NEST_TO_STRUCT.md")
- [UNNEST_ARRAY](recipe-actions.UNNEST_ARRAY.md "recipe-actions.UNNEST_ARRAY.md")
- [UNNEST_MAP](recipe-actions.UNNEST_MAP.md "recipe-actions.UNNEST_MAP.md")
- [UNNEST_STRUCT](recipe-actions.UNNEST_STRUCT.md "recipe-actions.UNNEST_STRUCT.md")
- [UNNEST_STRUCT_N](recipe-actions.UNNEST_STRUCT_N.md "recipe-actions.UNNEST_STRUCT_N.md")
- [GROUP_BY](recipe-actions.GROUP_BY.md "recipe-actions.GROUP_BY.md")
- [JOIN](recipe-actions.JOIN.md "recipe-actions.JOIN.md")
- [PIVOT](recipe-actions.PIVOT.md "recipe-actions.PIVOT.md")
- [SCALE](#recipe-actions.SCALE "#recipe-actions.SCALE")
- [TRANSPOSE](recipe-actions.TRANSPOSE.md "recipe-actions.TRANSPOSE.md")
- [UNION](recipe-actions.UNION.md "recipe-actions.UNION.md")
- [UNPIVOT](recipe-actions.UNPIVOT.md "recipe-actions.UNPIVOT.md")

## SCALE

Scales or normalizes the range of data in a numeric column.

###### Parameters

- `sourceColumn` — The name of an existing column.
- `strategy` — The operation to be applied to the column values:
  - `MIN_MAX` — Rescales the values into a range of
    [0,1].
  - `SCALE_BETWEEN` — Rescales the values into a range
    of two specified values.
  - `MEAN_NORMALIZATION` — Rescales the data to have a
    mean (μ) of 0 and standard deviation (σ) of 1 within a range of [-1,
    1].
  - `Z_SCORE` — Linearly scales data values to have a mean
    (μ) of 0 and standard deviation (σ) of 1. Best for handling
    outliers.

- `targetColumn` — The name of a column to contain the
  results.

###### Example

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
