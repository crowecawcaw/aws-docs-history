# Connect to a Honeycomb data

source

The Honeycomb data source allows you to query and visualize Honeycomb metrics and
link to Honeycomb traces from within Amazon Managed Grafana.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Known limitations

- This data source does not support ad-hoc queries.
- Because of API limitations, the variable editor can only return the
  first 1000 unique values for a selected column.
- Because of API limitations, the data source can query only the last 7
  days of data.

## Adding the data

source

1. Open the Grafana console in the Amazon Managed Grafana workspace and make sure you
   are logged in.
2. In the side menu under **Configuration** (the gear
   icon), choose **Data Sources**.
3. Choose **Add data source**.
4. Select **Honeycomb** from the list of data sources.

###### Note

If you don't see the **Data Sources** link in your side
menu, it means that your current user does not have the `Admin`
role.

**Honeycomb settings**

| Name                | Description                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `Name`              | The data source name. This is how you see the data source in<br>panels, queries, and Explore. |
| `Honeycomb API key` | The API key that you obtained from Honeycomb.                                                 |
| `URL`               | The URL of the Honeycomb API. For example,<br>`https://api.honeycomb.io`.                     |
| `Team`              | The Honeycomb team associated with the API key.                                               |

## Query the Honeycomb data source

To query metrics, enter values into the editor fields:

- Select a dataset.
- The default query is a `COUNT` over the selected dataset.
- To refine the query, select values for any of the remaining fields,
  such as **Visualization**,
  **Visualization**, **Where**,
  **Constraint**, **Group by**,
  **Order by**, or **Limit**.

## Templates and variables

To add a new Honeycomb query variable, see [Adding a query variable](variables-types.md#add-a-query-variable "variables-types.md#add-a-query-variable").

YOu can create variables containing Datasets, Columns, or Column
Values.

- If no dataset is selected, the variable will contain datasets.
- If only a dataset is selected, the variable will contain column
  names.
- If both a dataset and a column are selected, the variable will
  contain column values. Column values can be further constrained using
  the **Where** fields in the editor. .

## View query in Honeycomb UI

To see the query you have created in the Honeycomb UI from the dashboard
panel, choose any point in the graph and choose **Open in
Honeycomb**.

To see the query you have created in the Honeycomb UI from the Query Editor,
choose **Open in Honeycomb**.

## Import a dashboard for Honeycomb

To import a dashboard, see [Importing a dashboard](dashboard-export-and-import.md#importing-a-dashboard "dashboard-export-and-import.md#importing-a-dashboard").

To find your imported dashboards, choose **Configuration**,
**Data sources**.

To see the avaialble pre-made dashboards, choose the Honeycomb data source and
choose the **Dashboards** tab.
