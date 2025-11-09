# Scatter panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The scatter panel shows an X/Y scatter plot for table data with a simpler interface
than other graphing panels. Unlike the graph panel, the scatter panel does not require
the data to be in a time series. The scatter panel requires a table formatted dataset
with two or more numeric columns of data.

One of these can be assigned to the X axis. One or more can be
assigned to a series of Y axis values and the resulting data plotted as a
series of dots. Each series can optionally also show a regression line using
one of a number of statistical best fits.

**Creating a scatter panel**

The following procedure describes how to create a scatter plot using the scatter
panel. For this example, we will assume that there is data, as in the following table
called `HEIGHT` with three columns of numerical values, `Age`,
`Boys`, and `Girls`, showing the average height of boys and
girls by age.

| Age | Boy's Height | Girl's Height |
| --- | ------------ | ------------- |
| 5   | 109.7        | 109.5         |
| 6   | 115.6        | 115.4         |
| 7   | 121.1        | 120.8         |
| 8   | 126.3        | 126           |
| 9   | 131.3        | 131.3         |
| 10  | 136.2        | 137.1         |
| 11  | 141.2        | 143.2         |
| 12  | 147          | 148.7         |
| 13  | 153.6        | 152.6         |
| 14  | 159.9        | 155.1         |
| 15  | 164.4        | 156.7         |
| 16  | 167.3        | 157.6         |
| 17  | 169          | 158           |
| 18  | 170          | 158.3         |
| 19  | 170.8        | 158.6         |

###### To create a scatter plot with the scatter panel

1. In your Grafana dashboard, choose **Add Panel**.
2. For the Query, write a query that will return the data needed. In this case,
   you would use a query such as `SELECT * FROM HEIGHT`.
3. Select the **Scatter** visualization.
   This will create a scatter plot, using the first column as the X axis, and the other
   numeric columns as Y axes.

**Configuration options**

The scatter panel provides the following four custom configuration options.

- **X Axis** – You can choose which field to use as the
  X axis, as well as extents and title and display information for the
  axis.
- **Y Axis** – You can choose which fields to display on
  the Y axis, including display options for each field, and extents and title
  information for the axis. You can also choose to display a regression line for
  each field. See the following information for more details on regression line
  configuration.
- **Legend** – You can turn a legend for the panel on or
  off, as well as choose the size of the text in the legend.
- **Display** – You can set other options for the chart,
  including grid color and border style.
  **Regression line configuration**

Each Y axis dataset can display a line, in addition to the individual dots. There are
five options for the line type.

- **None** – Do not display a regression line.
- **Simple** – Display a regression line that connects
  the dataset points.
- **Linear** – Display a straight line, using the
  least-squares, best-fit method.
- **Exponential** – Display an exponential best-fit
  regression line.
- **Power** – Display a power best-fit regression
  line.
