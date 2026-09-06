

# Configure thresholds
<a name="v10-panels-configure-thresholds"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 10.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

In dashboards, a threshold is a value or limit you set for a metric that's reflected visually when it's met or exceeded. Thresholds are one way you can conditionally style and color your visualizations based on query results.

You can use thresholds to:
+ Color grid lines or grid ares areas in a time-series visualization.
+ Color the background or value text in a stat visualization.
+ Define regions and region colors in a state timeline.
+ Color lines in a time-series visualization.
+ Color the gauge and threshold markers in a gauge.
+ Color markers in a geomap.
+ Color cell text or background in a table.

**Supported visualizations**
+ Bar chart
+ Bar gauge
+ Candlestick
+ Canvas
+ Gauge
+ Geomap
+ Histogram
+ Stat
+ State timeline
+ Status history
+ Table
+ Time series
+ Trend

## Default thresholds
<a name="v10-panels-thresholds-default"></a>

On visualizations that support thresholds, Grafana has the following default threshold settings:
+ 80 = red
+ Base = green
+ Mode = Absolute
+ Show thresholds = Off (for some visualizations)

  For more information, see [Show thresholds](#v10-panels-thresholds-show).

## Thresholds options
<a name="v10-panels-thresholds-options"></a>

You can set the following options to further define how thresholds look.

### Thresholds value
<a name="v10-panels-thresholds-value"></a>

This number is the value that triggers the threshold. You can also set the color associated with the threshold in this field.

The **Base** value represents minus infinity. By default, it's set to the color green, which is generally the "good" color.

### Thresholds mode
<a name="v10-panels-thresholds-mode"></a>

There are two threshold modes:
+ **Absolute** thresholds are defined by a number. For example, 80 on a scale of 1 to 150.
+ **Percentage** thresholds are defined relative to minimum or maximum. For example, 80 percent.

### Show thresholds
<a name="v10-panels-thresholds-show"></a>

**Note**  
This option is only supported for the bar chart, candlestick, time series, and trend visualizations.

Set if and how thresholds are shown on the visualization with the following options.
+ **Off** – The thresholds are not shown.
+ **As lines** – The thresholds are shown as horizontal lines on the visualization.
+ **As lines (dashed)** – The thresholds are shown as dashed horizontal lines.
+ **As filled regions** – The thresholds are shown as horizontal regions.
+ **As filled regions and lines** – The thresholds are shown as horizontal regions separated by lines.
+ **As filled regions and lines (dashed)** – The thresholds are shown as horizontal regions separated by dashed lines.

## Adding a threshold
<a name="v10-panels-thresholds-add"></a>

You can add as many thresholds to a visualization as you want. Grafana automatically sorts thresholds values from highest to lowest.

**To add a threshold**

1. Navigate to the panel you want to update.

1. Hover over any part of the panel to display the menu at the top right corner.

1. From the menu, select **Edit**.

1. Scroll to the **Thresholds** section, or enter `Thresholds` in the search bar at the top of the panel edit pane.

1. Choose **\+ Add threshold**.

1. Enter a new threshold value, or use the up and down arrows at the right side of the field to increase or decrease the value incrementally.

1. Click the colored circle to the left of the threshold value to open the color picker, where you can update the threshold color.

1. Under **Thresholds mode**, select either **Absolute** or **Percentage**.

1. Under **Show thresholds**, set how the threshold is displayed, or turn it off.

To delete a threshold, navigate to the panel that contains the threshold and choose the trash icon next to the threshold you want to remove.