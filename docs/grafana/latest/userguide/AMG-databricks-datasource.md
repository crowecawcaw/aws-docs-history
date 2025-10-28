# Connect to a Databricks data

source

The Databricks data source enables you to query and visualize Databricks data
within Amazon Managed Grafana. It includes a SQL editor to format and color code your
queries.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Adding a Databricks data

source

Follow these steps to add a Databricks data source in the Grafana
console.

###### To add a Databricks data source

1. Open the side menu by choosing the Grafana icon in the top
   header.
2. In the side menu, under the **Dashboards** link,
   select **Data Sources**.

###### Note

If you don't see the **Data Sources** link, you
do not have the `Admin` role for Grafana. 3. Choose the **+ Add data source** button in the top
header. 4. Select **Databricks** from the
**Type** dropdown list.

###### Note

If you don't see the Databricks option, and need it, you must
upgrade to Grafana Enterprise. 5. Choose the options to connect to and edit your data.

## Notes when using the Databricks data

source

**Time series**

Time series visualizations are selectable when you add a `datetime`
field to your query. This field will be used as the timestamp for the series. If
the field does not include a specific time zone, Grafana will assume that the
time is UTC.

**Multi-line time series**

To create a multi-line time series visualization, the query must include at
least three fields in the following order.

1. A `datetime` field with an alias of
   `time`.
2. A value to `GROUP BY`.
3. One or more metric values to visualize.

The following is an example of a query that will return multi-line time series
options.

```
SELECT log_time AS time, machine_group, avg(disk_free) AS avg_disk_free
FROM mgbench.logs1
GROUP BY machine_group, log_time
ORDER BY log_time
```
