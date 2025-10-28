# Graph panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

A graph panel can render as a line, a path of dots, or a series of bars. This type of
graph is versatile enough to display almost any time-series data.

## Data and field options

When using graph visualizations, you can apply the following options:

- [Transformations](panel-transformations.md "panel-transformations.md")
- Alerts. This is the only type of visualization that allows you to set
  alerts. For more information, see [Grafana alerting](alerts-overview.md "alerts-overview.md").
- [Thresholds](thresholds.md "thresholds.md")

## Display options

To refine your visualization, use the following settings:

- Bars – Display values as a bar chart.
- Lines – Display values as a line graph.
- Line width – Specify the width of the
  line for a series. The default is 1.
- Staircase – Draw adjacent points as
  staircase.
- Area fill – Specify the amount of color
  fill for a series. The default is 1; 0 is none.
- Fill gradient – Specify the degree of
  gradient on the area fill. The default is 0, which is no gradient; 10 is a
  steep gradient.
- Points – Display points for values.
- Point radius – Control how large the
  points are.
- Alert thresholds – Display alert
  thresholds and Regions on the panel.

### Stacking and null value

- Stack – Each series is stacked on
  top of another.
- Percent – Each series is drawn as a
  percentage of the total of all series. This option is available when
  **Stack** is selected.
- Null value – Specify how null
  values are displayed. _This is an important setting._
  See the note below.
  - connected – If there is a
    gap in the series, meaning one or more null values, the line
    will skip the gap and connect to the next non-null value.
  - null If there is a gap in the
    series, meaning a null value, the line in the graph will be
    broken and show the gap. This is the default setting.
  - null as zero – If there is
    a gap in the series, meaning a null value, it will be displayed
    as a zero value in the graph panel.

###### Important

If you are monitoring a server’s CPU load and the load reaches 100
percent, the server will lock up, and the agent sending statistics will not
be able to collect the load statistic. This leads to a gap in the metrics,
and using the default _null_ setting means that Amazon Managed Grafana
will show the gaps and indicate that something is wrong. If this is set to
_connected_, it will be easy to miss this signal.

### Hover tooltip

Use these settings to change the appearance of the tooltip that appears when
you pause over the graph visualization.

- Mode – Determines how many series
  the hover tooltip shows.
  - All series – The hover
    tooltip shows all series in the graph. In the series list in the
    tooltip, the Grafana workspace highlights the series that you
    are pausing on in bold.
  - Single – The hover tooltip
    shows only a single series, the one that you are pausing on in
    the graph.

- Sort order – Sorts the order of
  series in the hover tooltip if you have selected **All
  series** mode. When you pause on a graph, Amazon Managed Grafana
  displays the values associated with the lines. Generally, users are most
  interested in the highest or lowest values. Sorting these values can
  make it much easier to find the data that you want.
  - None – The order of the
    series in the tooltip is determined by the sort order in your
    query. For example, you can sort the series alphabetically by
    series name.
  - Increasing – The series in
    the hover tooltip are sorted by value and in increasing order,
    with the lowest value at the top of the list.
  - Decreasing – The series in
    the hover tooltip are sorted by value and in decreasing order,
    with the highest value at the top of the list.

## Series overrides

Series overrides allow a series in a graph panel to be rendered differently from
the others. You can customize display options on a per-series basis or by using
regex rules. For example, one series can have a thicker line width to make it stand
out or be moved to the right Y-axis.

You can add multiple series overrides.

###### To add a series override

1. Choose **Add series override**.
2. In **Alias or regex**, type or select a series. Choose
   the field to see a list of available series.

For example, `/Network.*/` would match two series named
`Network out` and `Network in`. 3. Choose **+** and then select a style to apply to the
series. You can add multiple styles to each entry.

- Bars – Show series as a bar graph.
- Lines – Show series as a line graph.
- Line fill – Show a line graph with area
  fill.
- Fill gradient – Specify the area fill
  gradient amount.
- Line width – Set line width.
- Null point mode – Use this option to
  ignore null values or replace them with zero. This is important if you want
  to ignore gaps in your data.
- Fill below to – Fill the area between
  two series.
- Staircase line – Show series as a
  staircase line.
- Dashes – Show a line with dashes.
- Hidden Series – Hide the series.
- Dash Length – Set the length of dashes
  in the line.
- Dash Space – Set the length of the
  spaces between the dashes in the line.
- Points – Show series as separate
  points.
- Point Radius – Set the radius for point
  rendering.
- Stack – Set the stack group for the
  series.
- Color – Set the series color.
- Y-axis – Set the series y-axis.
- Z-index – Set the series z-index
  (rendering order). This option is important when you are overlaying
  different styles, such as bar charts and area charts.
- Transform – Transform value to negative
  to render below the y-axis.
- Legend – Control whether a series is
  shown in the legend.
- Hide in tooltip – Control whether a
  series is shown in a graph tooltip.

## Axes

Use these options to control the display of axes in the visualization.

### Left Y/Right Y

Options are identical for both y-axes.

- Show – Choose to show or hide the
  axis.
- Unit – Choose the display unit for
  the y value.
- Scale – Choose the scale to use for
  the y value: **linear**, or
  **logarithmic**. The default is
  **linear**.
- Y-Min – The minimum y value. The
  default is **auto**.
- Y-Max – The maximum Y value. The
  default is **auto**.
- Decimals – Define how many decimals
  are displayed for the y value. The default is **auto**.
- Label – Specify the y axis label.
  The default is “",

### Y-Axes

- Align – Align left and right y-axes
  by value. The default is unchecked/false.
- Level – Enter the value to use for
  alignment of left and right y-axes, starting from Y=0. The default is 0.
  This option is available when **Align** is selected.

### X-Axis

- Show – Choose to show or hide the
  axis.
- Mode – The display mode completely
  changes the visualization of the graph panel. It’s like three panels in
  one. The main mode is the time series mode with time on the x-axis. The
  other two modes are a basic bar chart mode with series on the x-axis
  instead of time and a histogram mode.
  - Time (default) – The x-axis
    represents time and the data is grouped by time (for example, by
    hour, or by minute).
  - Series – The data is
    grouped by series, and not by time. The y-axis still represents
    the value.
    - Value – This is the
      aggregation type to use for the values. The default is
      **total** (summing the values
      together).

  - Histogram – This option
    converts the graph into a histogram. A histogram is a kind of
    bar chart that groups numbers into ranges, often called buckets
    or bins. Taller bars show that more data falls in that range.

  For more information about histograms, see [Introduction to histograms
  and heatmaps](getting-started-grafanaui.md#introduction-to-histograms-and-heatmaps "getting-started-grafanaui.md#introduction-to-histograms-and-heatmaps").

      - Buckets – Sets the
       number of buckets to group the values by. If left empty,
       Amazon Managed Grafana tries to calculate a suitable number of
       buckets.
      - X-Min – Filters out
       values from the histogram that are less than this
       minimum limit.
      - X-Max – Filters out
       values that are greater than this maximum limit.

## Legend

Use these settings to refine how the legend appears in your visualization.

### Options

- Show – Clear to hide the legend.
  The default is selected (true).
- As Table – Select to display the
  legend in the table. The default is checked (true).
- To the right – Select to display
  the legend to the right.
- Width – Enter the minimum width for
  the legend in pixels. This option is available when **To the
  right** is selected.

### Values

Additional values can be shown alongside the legend names.

- Min – The minimum value returned
  from the metric query.
- Max – The maximum value returned
  from the metric query.
- Avg – The average value returned
  from the metric query.
- Current – The last value returned
  from the metric query.
- Total – The sum of all values
  returned from the metric query.
- Decimals – How many decimals are
  displayed for legend values and graph hover tooltips.

Amazon Managed Grafana calculates the legend values on the client side. These legend
values depend on the type of aggregation or point consolidation that your metric
query is using. All the above legend values cannot be correct at the same time.

For example, if you plot a rate such requests/second, which is probably using
average as an aggregator, the Total in the legend will not represent the total
number of requests. It is just the sum of all data points received by Amazon Managed Grafana.

### Hide series

Hide series when all values of a series from a metric query are of a specific
value.

- With only nulls – Value=null
  (default unchecked)
- With only zeroes – Value=zero
  (default unchecked)

### Time regions

You can highlight specific time regions on the graph to make it easier to see,
for example, weekends, business hours, and off-work hours. All configured time
regions refer to UTC time.
