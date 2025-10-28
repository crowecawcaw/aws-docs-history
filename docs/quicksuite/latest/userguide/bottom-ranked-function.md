# Bottom ranked computation

The bottom ranked computation calculates the requested number of categories by
value that rank in the bottom of the autonarrative's dataset. For example, you
can create a computation to find the bottom three states by sales
revenue.

To use this function, you need at least one dimension in the
**Categories** field well.

## Parameters

_name_

A unique descriptive name that you assign or change. A name is
assigned if you don't create your own. You can edit this
later.

_Category_

The category dimension that you want to rank.

_Value_

The aggregated measure that the computation is based
on.

_Number of results_

The number of ranked results that you want to display.

## Computation

outputs

Each function generates a set of output parameters. You can add these
outputs to the autonarrative to customize what it displays. You can also add
your own custom text.

To locate the output parameters, open the
**Computations** tab on the right, and locate the
computation that you want to use. The names of the computations come from
the name you provide when you create the insight. Choose the output
parameter by clicking on it only once. If you click twice, you add the same
output twice. Items displayed in **bold** can
be used in the narrative.

###### Note

These are the same output parameters as the ones that are returned by
the top ranked computation.

- `categoryField` – From the
  **Categories** field well.
  - `**name**`
    – The formatted display name of the field.

- `metricField` – From the
  **Values** field well.
  - `**name**`
    – The formatted display name of the field.
  - `**aggregationFunction**` – The
    aggregation used for the metric (**SUM**,
    **AVG**, and so on).

- `**itemsCount**` –
  The number of items included in this computation.
- `**items**`: Bottom ranked
  items.
  - `categoryField` – The category
    field.
    - `**value**` – The value
      (contents) of the category field.
    - `**formattedValue**` – The
      formatted value (contents) of the category field. If
      the field is null, this displays
      '`NULL`'. If the field is empty, it
      displays '`(empty)`'.

  - `metricValue` – The metric field.
    - `**value**` – The raw
      value.
    - `**formattedValue**` – The
      value formatted by the metric field.
    - `**formattedAbsoluteValue**` –
      The absolute value formatted by the metric
      field.

## Example

The following screenshot shows the default configuration for the
bottom-ranked computation.

![Default configuration for the bottom-ranked computation.](../images/bottom-ranked-computation.png)
