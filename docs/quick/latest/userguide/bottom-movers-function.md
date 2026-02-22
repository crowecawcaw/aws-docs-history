# Bottom movers computation

The bottom movers computation counts the requested number of categories by
date that rank in the bottom of the autonarrative's dataset. For example, you
can create a computation to find the bottom three products sold, by sales
revenue.

To use this function, at least one dimension in the **Time**
field well and at least one dimension in the **Categories**
field well.

## Parameters

_name_

A unique descriptive name that you assign or change. A name is
assigned if you don't create your own. You can edit this
later.

_Date_

The date dimension that you want to rank.

_Category_

The category dimension that you want to rank.

_Value_

The aggregated measure that the computation is based
on.

_Number of movers_

The number of ranked results that you want to display.

_Order by_

The order that you want to use, percent difference or absolute
difference.

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
the top movers computation.

- `timeField` – From the **Time**
  field well.
  - `**name**`
    – The formatted display name of the field.
  - `**timeGranularity**` – The time
    field granularity (**DAY**,
    **YEAR**, and so on).

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

- `startTimeValue` – The value in the date
  dimension.
  - `**value**`
    – The raw value.
  - `**formattedValue**` – The value
    formatted by the datetime field.

- `endTimeValue` – The value in the date
  dimension.
  - `**value**`
    – The raw value.
  - `**formattedValue**` – The absolute
    value formatted by the datetime field.

- `**itemsCount**` –
  The number of items included in this computation.
- `**items**`: Bottom moving
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

  - `currentMetricValue` – The current value
    for the metric field.
    - `**value**` – The raw
      value.
    - `**formattedValue**` – The
      value formatted by the metric field
    - `**formattedAbsoluteValue**` –
      The absolute value formatted by the metric
      field.

  - `previousMetricValue` – The previous
    value for the metric field.
    - `**value**` – The raw
      value.
    - `**formattedValue**` – The
      value formatted by the metric field
    - `**formattedAbsoluteValue**` –
      The absolute value formatted by the metric
      field.

  - `percentDifference` – The percent
    difference between the current and previous values of the
    metric field.
    - `**value**` – The raw value of
      the calculation of the percent difference.
    - `**formattedValue**` – The
      formatted value of the percent difference (for
      example, -42%).
    - `**formattedAbsoluteValue**` –
      The formatted absolute value of the percent
      difference (for example, 42%).

  - `absoluteDifference` – The absolute
    difference between the current and previous values of the
    metric field.
    - `**value**` – The raw value of
      the calculation of the absolute difference.
    - `**formattedValue**` – The
      absolute difference formatted by the settings in the
      metric field's format preferences.
    - `**formattedAbsoluteValue**` –
      The absolute value of the difference formatted by
      the metric field.
