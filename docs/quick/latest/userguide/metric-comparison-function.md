# Metric comparison

computation

The metric comparison computation compares values in different measures. For
example, you can create a computation to compare two values, such as actual
sales compared to sales goals.

To use this function, you need at least one dimension in the
**Time** field well and at least two measures in the
**Values** field well.

## Parameters

_name_

A unique descriptive name that you assign or change. A name is
assigned if you don't create your own. You can edit this
later.

_Date_

The date dimension that you want to rank.

_Value_

The aggregated measure that the computation is based
on.

_Target value_

The field that you want to compare to the value.

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

- `timeField` – From the **Time**
  field well.
  - `**name**`
    – The formatted display name of the field.
  - `**timeGranularity**` – The time
    field granularity (**DAY**,
    **YEAR**, and so on).

- `fromMetricField` – From the
  **Values** field well.
  - `**name**`
    – The formatted display name of the field.
  - `**aggregationFunction**` – The
    aggregation used for the metric (**SUM**,
    **AVG**, and so on).

- `fromMetricValue` – The value in the metric
  dimension.
  - `**value**`
    – The raw value.
  - `**formattedValue**` – The value
    formatted by the metric field.
  - `**formattedAbsoluteValue**` –
    The absolute value formatted by the metric field.

- `toMetricField` – From the
  **Values** field well.
  - `**name**`
    – The formatted display name of the field.
  - `**aggregationFunction**` – The
    aggregation used for the metric (**SUM**,
    **AVG**, and so on).

- `toMetricValue` – The current value in the
  metric dimension.
  - `**value**`
    – The raw value.
  - `**formattedValue**` – The value
    formatted by the metric field.
  - `**formattedAbsoluteValue**` –
    The absolute value formatted by the metric field.

- `timeValue` – The value in the datetime
  dimension.
  - `**value**`
    – The raw value.
  - `**formattedValue**` – The value
    formatted by the datetime field.

- `percentDifference` – The percent difference
  between the current and previous values of the metric field.
  - `**value**`
    – The raw value of the calculation of the percent
    difference.
  - `**formattedValue**` – The formatted
    value of the percent difference (for example, -42%).
  - `**formattedAbsoluteValue**` –
    The formatted absolute value of the percent difference (for
    example, 42%).

- `absoluteDifference` – The absolute difference
  between the current and previous values of the metric field.
  - `**value**`
    – The raw value of the calculation of the absolute
    difference.
  - `**formattedValue**` – The absolute
    difference formatted by the settings in the metric field's
    format preferences.
  - `**formattedAbsoluteValue**` –
    The absolute value of the difference formatted by the metric
    field.
