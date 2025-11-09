# Configure a TestData data source for

testing

Grafana ships with a TestData data source, which creates simulated time series
data for any panel. You can use it to build your own fake and random time series
data and render it in any panel, which helps you verify dashboard functionality and
safely and easily share the data.

**Configure the data source**

###### To access the data source configuration for TestData

1. Choose the **Configuration** (gear) icon.
2. Choose **Data Sources**.
3. choose **TestData**.
   The data source doesn’t provide any settings beyond the most basic options common
   to all data sources:

| Name      | Description                                                     |
| --------- | --------------------------------------------------------------- |
| `Name`    | The name of the data source in panels, queries, and<br>Explore. |
| `Default` | Whether this datasource will be pre-selected for new<br>panels. |

**Create mock data**

Added the TestData data source, your Grafana instance’s users can use it as a data
source in any metric panel, and it will provide mock data that you can use, based on
the TestData scenario you choose.

**Choose a scenario**

Instead of providing a query editor, the TestData data source helps you select a
**Scenario** that generates simulated data for
panels.

You can assign an **Alias** to each scenario, and
many have their own options that appear when selected.

**Available scenarios:**

- **Annotations**
- **Conditional Error**
- **CSV Content**
- **CSV File**
- **CSV Metric Values**
- **Datapoints Outside Range**
- **Exponential heatmap bucket data**
- **Grafana API**
- **Grafana Live**
- **Linear heatmap bucket data**
- **Load Apache Arrow Data**
- **Logs**
- **No Data Points**
- **Node Graph**
- **Predictable CSV Wave**
- **Predictable Pulse**
- **Random Walk**
- **Random Walk (with error)**
- **Random Walk Table**
- **Raw Frames**
- **Simulation**
- **Slow Query**
- **Streaming Client**
- **Table Static**
- **USA generated data**
  **Import a pre-configured dashboard**

TestData also provides an example dashboard.

###### To import the example dashboard

1. Navigate to the data source’s configuration page.
2. Select the **Dashboards** tab.
3. Select **Import** for the **Simple Streaming
   Example** dashboard.
   **To customize an imported dashboard:**

To customize the imported dashboard, we recommend that you save it under a
different name. If you don’t, upgrading Grafana can overwrite the customized
dashboard with the new version.

**Use test data to report issues**

If you report an issue to GrafanaLabs on GitHub involving the use or rendering of
time series data, we strongly recommend that you use this data source to replicate
the issue. That makes it much easier for the developers to replicate and solve your
issue.
