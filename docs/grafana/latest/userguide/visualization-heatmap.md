# Heatmap

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The heatmap panel visualization allows you to view histograms over time. For more
information about histograms, see [Introduction to histograms
and heatmaps](getting-started-grafanaui.md#introduction-to-histograms-and-heatmaps "getting-started-grafanaui.md#introduction-to-histograms-and-heatmaps").

## Axes options

Use these settings to adjust how axes are displayed in your visualization.

### Y Axis

- Unit – The display unit for the
  y-axis value
- Scale – The scale to use for the
  y-axis value
  - linear – Linear scale
  - log (base 2) – Logarithmic
    scale with base 2
  - log (base 10) – Logarithmic
    scale with base 10
  - log (base 32) – Logarithmic
    scale with base 32
  - log (base 1024) –
    Logarithmic scale with base 1024

- Y-Min – The minimum y value
  (default is auto)
- Y-Max – The maximum y value
  (default is auto)
- Decimals – Number of decimals to
  render y-axis values with (default is auto)

### Buckets

###### Note

If the data format is **Time series buckets**, this
section is not be available.

- Y Axis Buckets – The number of
  buckets that the y-axis will be split into.
- Size – The size of each y-axis
  bucket (visible only if **Scale** is
  _linear_). This option has priority over
  **Y Axis Buckets**.
- Split Factor – (Only visible if
  **Scale** is _log (base 2)_ or
  greater). By default, Amazon Managed Grafana splits y values by log base. With this
  option, you can split each default bucket into the specified number of
  buckets.
- X Axis Buckets – The number of
  buckets that the x-axis will be split into.
- Size – The size of each x-axis
  bucket. Number or time interval (10s, 5m, 1h, etc). Supported intervals:
  ms, s, m, h, d, w, M, y. This option has priority over **X Axis Buckets**.

#### Bucket bound

When Data format is Time series buckets, the data source returns series
with names representing bucket bound. But depending on the data source, a
bound can be upper or lower. You can use this option to adjust a bound type.
If **Auto** is set, a bound option is chosen based on
panels’ data source type.

#### Bucket size

The Bucket count and size options are used by Amazon Managed Grafana to calculate how
big each cell in the heatmap is. You can define the bucket size either by
count (the first input box) or by specifying a size interval. For the
y-axis, the size interval is just a value. For the X-bucket, you can specify
a time interval in the **Size** input. For example, you can
set the time range to `1h`. This will make the cells 1h wide on
the x-axis.

#### Data format

Choose an option in the **Format** list.

- Time series – Amazon Managed Grafana does
  the bucketing by going through all time series values. The bucket
  sizes and intervals are set in the **Buckets**
  options.
- Time series buckets – Each
  time series already represents a y-axis bucket. The time series name
  (alias) must be a numeric value representing the upper or lower
  interval for the bucket. The Grafana workspace does no bucketing, so
  the bucket size options are hidden.

## Display options

Use these settings to refine your visualization.

### Colors

The color spectrum controls the mapping between value count (in each bucket)
and the color assigned to each bucket. The color on the far-left side of the
spectrum represents the minimum count, and the color on the far-right side
represents the maximum count. Some color schemes are automatically inverted when
using the light theme.

You can also change the color mode to **Opacity**. In this
case, the color will not change, but the amount of opacity will change with the
bucket count.

- **Mode**
  - Opacity – Bucket value
    represented by cell opacity. An opaque cell means the maximum
    value.
    - Color – Cell base
      color.
    - Scale – Scale for
      mapping bucket values to the opacity.
      - linear –
        Linear scale. Bucket value maps linearly to the
        opacity.
      - sqrt – Power
        scale. Cell opacity calculated as `value ^
k`, where `k` is a configured
        **Exponent** value.
        If the exponent is less than `1`, you
        will get a logarithmic scale. If the exponent is
        greater than `1`, you will get an
        exponential scale. In the case of `1`,
        the scale will be the same as linear.

    - Exponent – value of
      the exponent, greater than `0`.

  - spectrum – Bucket value
    represented by cell color.
    - Scheme – If the
      mode is **spectrum**,
      select a color scheme.

### Color scale

By default, Amazon Managed Grafana calculates cell colors based on minimum and maximum
buckets values. With **Min** and **Max**, you
can overwrite those values. Think of a bucket value as a z-axis and Min and Max
as Z-Min and Z-Max respectively.

- Min – Minimum value used for cell
  color calculation. If the bucket value is less than Min, it is mapped to
  the minimum color. The default is `series min value`.
- Max – Maximum value used for cell
  color calculation. If the bucket value is greater than Max, it is mapped
  to the maximum color. The default is `series max value`.

### Legend

Choose whether to display the heatmap legend on the visualization or not.

### Buckets

- Hide zero – Do not draw cells that
  have zero values.
- Space – Set the space between cells
  in pixels. Default is 1 pixel.
- Round – Set the cell roundness in
  pixels. Default is 0.

### Tooltip

- Show tooltip – Show the heatmap
  tooltip.
- Histogram – Show the y-axis
  histogram on the tooltip. The histogram represents distribution of the
  bucket values for the specific timestamp.
- Decimals – Set the number of
  decimals to render bucket value with (default is auto).
