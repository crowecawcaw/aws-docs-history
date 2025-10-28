# Using bar charts

Amazon Quick Suite supports the following types of bar charts, with either horizontal or
vertical orientation:

- **Single-measure** – A
  _single-measure bar chart_ shows values for a single
  measure for a dimension.
- **Multi-measure** – A
  _multi-measure bar chart_ shows values for multiple
  measure for a dimension.
- **Clustered** – A _clustered bar
  chart_ shows values for a single measure for a dimension, grouped
  by another dimension.
- **Stacked** – A _stacked bar
  chart_ is similar to a clustered bar chart in that it displays a
  measure for two dimensions. However, instead of clustering bars for each child
  dimension by the parent dimension, it displays one bar per parent dimension. It
  uses color blocks within the bars to show the relative values of each item in
  the child dimension. The color blocks reflect the value of each item in the
  child dimension relative to the total for the measure. A stacked bar chart uses
  a scale based on the maximum value for the selected measure.
- **Stacked 100 percent** – A
  _stacked 100 percent bar chart_ is similar to a stacked
  bar chart. However, in a stacked 100 percent bar chart, the color blocks reflect
  the percentage of each item in the child dimension, out of 100 percent.
  Bar charts show up to 10,000 data points on the axis for visuals that don't use
  group or color. For visuals that do use group or color, they show up to 50 data points
  on the axis and up to 50 data points for group or color. For more information about how
  Amazon Quick Suite handles data that falls outside display limits, see [Display limits](working-with-visual-types.md#display-limits "working-with-visual-types.md#display-limits").

## Creating single-measure bar charts

Use the following procedure to create a single-measure bar chart.

###### To create a single-measure bar chart

1. On the analysis page, choose **Visualize** on the toolbar
   at left.
2. On the application bar at upper left, choose **Add**, and
   then choose **Add visual**.
3. On the **Visual types** pane, choose the
   **Horizontal bar chart** or **Vertical bar
   chart** icon.
4. From the **Fields list** pane, drag a dimension to the
   **X-axis** or **Y-axis** field
   well.
5. From the **Fields list** pane, drag a measure to the
   **Value** field well.

## Creating multi-measure bar charts

Use the following procedure to create a multi-measure bar chart.

###### To create a multi-measure bar chart

1. On the analysis page, choose **Visualize** on the toolbar
   at left.
2. On the application bar at upper-left, choose **Add**, and
   then choose **Add visual**.
3. On the **Visual types** pane, choose the
   **Horizontal bar chart** or **Vertical bar
   chart** icon.
4. From the **Fields list** pane, drag a dimension to the
   **X-axis** or **Y-axis** field
   well.
5. From the **Fields list** pane, drag two or more measures
   to the **Value** field well.

## Creating clustered bar charts

Use the following procedure to create a clustered bar chart.

###### To create a clustered bar chart

1. On the analysis page, choose **Visualize** on the toolbar
   at left.
2. On the application bar at upper left, choose **Add**, and
   then choose **Add visual**.
3. On the **Visual types** pane, choose the
   **Horizontal bar chart** or **Vertical bar
   chart** icon.
4. From the **Fields list** pane, drag a dimension to the
   **X-axis** or **Y-axis** field
   well.
5. From the **Fields list** pane, drag a measure to the
   **Value** field well.
6. From the **Fields list** pane, drag a dimension to the
   **Group/Color** field well.

## Creating stacked bar charts

Use the following procedure to create a stacked bar chart.

###### To create a stacked bar chart

1. On the analysis page, choose **Visualize** on the toolbar
   at left.
2. On the application bar at upper-left, choose **Add**, and
   then choose **Add visual**.
3. On the **Visual types** pane, choose the
   **Horizontal stacked bar chart** or **Vertical
   stacked bar chart** icon.
4. From the **Fields list** pane, drag a dimension to the
   **X-axis** or **Y-axis** field
   well.
5. From the **Fields list** pane, drag a dimension to the
   **Group/Color** field well.
6. From the **Fields list** pane, drag a measure to the
   **Value** field well.
7. (Optional) Add data labels and show totals:
   1. On the menu in the upper-right corner of the visual, choose the
      **Format visual** icon.
   2. In the **Visual** pane, choose **Data
      labels**.
   3. Toggle the switch to display data labels.

   Labels for each measure value appear in the chart and the option
   to show totals appears in the pane. 4. Check **Show totals**.

   Totals appear for each bar in the chart.

## Creating stacked 100 percent bar

charts

Use the following procedure to create a stacked 100 percent bar chart.

###### To create a stacked 100 percent bar chart

1. On the analysis page, choose **Visualize** on the toolbar
   at left.
2. On the application bar at upper-left, choose **Add**, and
   then choose **Add visual**.
3. On the **Visual types** pane, choose the
   **Horizontal stacked 100% bar chart** or
   **Vertical stacked 100% bar chart** icon.
4. From the **Fields list** pane, drag a dimension to the
   **X-axis** or **Y-axis** field
   well.
5. From the **Fields list** pane, drag two or more measures
   to the **Value** field well.

## Bar chart features

To understand the features supported by bar charts, use the following
table.

| Feature                                                                    | Supported?           | Comments                                                                                                                                                                           | For more information                                                                                                                                                                    |
| -------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Changing the legend display                                                | Yes, with exceptions | Multi-measure and clustered bar charts display a legend, while single-measure horizontal bar charts don't.                                                                         | [Legends on visual types in Quick Suite](customizing-visual-legend.md "customizing-visual-legend.md")                                                                                   |
| Changing the title display                                                 | Yes                  |                                                                                                                                                                                    | [Titles and subtitles on visual types in Quick Suite](customizing-a-visual-title.md "customizing-a-visual-title.md")                                                                    |
| Changing the axis range                                                    | Yes                  |                                                                                                                                                                                    | [Range and scale on visual types in Quick Suite](changing-visual-scale-axis-range.md "changing-visual-scale-axis-range.md")                                                             |
| Showing or hiding axis lines, grid lines, axis labels, and axis sort icons | Yes                  |                                                                                                                                                                                    | [Axes and grid lines on visual types in Quick Suite](showing-hiding-axis-grid-tick.md "showing-hiding-axis-grid-tick.md")                                                               |
| Changing the visual colors                                                 | Yes                  |                                                                                                                                                                                    | [Colors in visual types in Quick Suite](changing-visual-colors.md "changing-visual-colors.md")                                                                                          |
| Focusing on or excluding elements                                          | Yes, with exceptions | You can focus on or exclude any bar on the chart, except when you are using a date field as the dimension for the axis. In that case, you can only focus on a bar, not exclude it. | [Focusing on visual elements](focusing-on-visual-elements.md "focusing-on-visual-elements.md") [Excluding visual elements](excluding-visual-elements.md "excluding-visual-elements.md") |
| Sorting                                                                    | Yes                  | You can sort on the fields you choose for the axis and the values.                                                                                                                 | [Sorting visual data in Amazon Quick Suite](sorting-visual-data.md "sorting-visual-data.md")                                                                                            |
| Performing field aggregation                                               | Yes                  | You must apply aggregation to the field or fields you choose for the value, and can't apply aggregation to the fields you choose for the axis or group/ color.                     | [Changing field aggregation](changing-field-aggregation.md "changing-field-aggregation.md")                                                                                             |
| Adding drill-downs                                                         | Yes                  | You can add drill-down levels to the axis and **Group/Color** field wells.                                                                                                         | [Adding drill-downs to visual data in Quick Sight](adding-drill-downs.md "adding-drill-downs.md")                                                                                       |
| Showing data labels                                                        | Yes                  |                                                                                                                                                                                    | [Data labels on visual types in Quick Suite](customizing-visual-data-labels.md "customizing-visual-data-labels.md")                                                                     |
| Showing stacked bar chart totals                                           | Yes                  | Showing totals in a stacked bar chart is only available when you choose to show data labels.                                                                                       | [Stacked bar charts](#create-bar-chart-stacked "#create-bar-chart-stacked")                                                                                                             |
