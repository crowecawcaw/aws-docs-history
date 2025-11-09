# Connect to a Dynatrace data

source

Data source for [https://www.dynatrace.com/](https://www.dynatrace.com "https://www.dynatrace.com"). To use this data source, you must have a
Dynatrace account.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

**Known limitations**

Template variables can't be multi-select. Only single selection is
supported.

Only v2 metric APIs are supported.

## Features

### Core features

- Template Variables
  - Metric Names
  - Single selection only (**no
    multi-select**)
  - Ad-Hoc Filters

- Annotations
  - Not currently supported

- Aliasing
  - Metric Names
  - Aggregation
  - Display Name
  - Host
  - Description

- Alerting
  - Full alerting support

### Dynatrace specific

features

Supports both built-in and custom metrics using the Dynatrace metrics v2
API. For more information, see the Dynatrace documentation: [Metrics API v2](https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/ "https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/") and [Metric ingestion](https://www.dynatrace.com/support/help/how-to-use-dynatrace/metrics/metric-ingestion/ "https://www.dynatrace.com/support/help/how-to-use-dynatrace/metrics/metric-ingestion/").

Depending on the metric, the API might support additional transformation
options.

## Dynatrace permissions

You will need the following permissions in Dynatrace - Read metrics using API
V2 (metrics.read) permission - Read entities using API V2 (entities.read)
permission

## Get an API key from Dynatrace

To set up an API token, see [Dynatrace API - Tokens and authentication](https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication/?api-token%3C-%3Epersonal-access-token=api-token "https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication/?api-token%3C-%3Epersonal-access-token=api-token")

Set the `metrics.read` and `entities.read` permissions
for your API token.

### Configuration

1.  Choose **Settings/Data Sources** within the
    logical Grafana server UI and choose **Add data
    source**.
2.  On the **Add data source** page, filter for
    **Dynatrace**, and select the Dynatrace plugin.
3.  Configuring a Dynatrace data source requires the following
    parameters:

        * `Name` - The name you want to apply to the
         Dynatrace data source (default: Dynatrace).
        * `Dynatrace API Type` - The type of Dynatrace
         instance that you’re connecting to. This is either
         `SaaS` or `Managed Cluster`.
        * `Dynatrace API Token` - This is the API token you
         generated in the previous step..

    The next two settings depend on whether you are Dynatrace SaaS or
    managed

        * In a SaaS example of
         `yfc55578.live.dynatrace.com`, your
         **Environment ID** would be
         `yfc55578`.
        * In the Managed example of
         `yd8888.managed-sprint.dynalabs.io/e/abc99984-3af2-55tt-72kl-0672983gc45`,
         your **Environment ID** would be
         `abc99984-3af2-55tt-72kl-0672983gc45` and
         your **Domain** would be
         `yd8888.managed-sprint.dynalabs.io`

4.  After all of the configuration values have been set, choose
    **Save & Test** to validate the
    configuration and save your changes.

### Query the data source

Use the query editor to query Dynatrace metrics and problems. The query
type can be `metric` or `problem`.

**Metric query type**

- `Metric`— Select the metric that you want to
  see. To get the metric list from Dynatrace again, choose
  **Refresh** button.
- `Aggregations`— Select the aggregation you want
  to use for a specific metric. Choose the aggregations value to
  change the aggregation type or choose **+** to add
  another aggregation.
- `Transformations`— You can select
  transformations in the query editor. Afterwards, enter a number of
  parameters into the selected transformation. Currently, only the
  merge transformation is supported. For more information about the
  merge transforms, see [Merge transformation](https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/metric-selector/#merge-transformation "https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/metric-selector/#merge-transformation").
- `Filters`— The Dynatrace data source dynamically
  queries the appropriate filters for each metric. To add a filter,
  choose the **+** symbol next to the
  **Filters** label on the Dynatrace query
  editor, select which field to filter on, select the operator to use,
  and then select a value to filter by. The Dynatrace data source
  allows you to create Filter Groups that you can join together to
  create complex logical comparisons. For most use cases, Filter
  Groups are not required. When creating filters with Tags, regardless
  of the conjunction selected, Dynatrace will always use AND.
  Dynatrace does not support OR filters with Tags.
- `Alias`— There are two different types of
  aliases you will encounter while using the Dynatrace data source.
  The first is a static alias. An alias of this type is available on
  every query that you build, and the name of the alias starts with a
  lowercase letter. The second is a dynamic alias, which changes based
  on the metric that you are using in your query, and the name of the
  alias starts with an uppercase letter. The Dynatrace plugin supports
  several different aliases: `Metric Names`,
  `Aggregation`, `Display Name`,
  `Host`, and `Description`.

| Name           | Value                                                             |
| -------------- | ----------------------------------------------------------------- |
| `$name`        | builtin:apps.other.keyUserActions.reportedErrorCount.os           |
| `$aggregation` | auto,value                                                        |
| `$displayName` | Reported error count (by key user action, OS) [mobile,<br>custom] |

**Problems query type**

- `Problem Query Type`— Select a problem query
  type. Currently, only the feed problem query type is supported. For
  information about the feed problem query type, see [Merge transformation](https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/metric-selector/#merge-transformation "https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v2/metric-selector/#merge-transformation")
- `Status Filter`— Filter the result problems by
  the status.
- `Impact Filter`— Filter the result problems by
  the impact level.
- `Severity Filter`— Filter the result problems by
  the severity level.
- `Expand Details`— Include related events to the
  response, if set..

#### Using template

variables

To add a new Dynatrace query variable, see [add a new template variable](variables-types.md#add-a-query-variable "variables-types.md#add-a-query-variable").
Use your Dynatrace data source as your data source for the following
available queries:

- `Query type`— Select a query type. The query
  type associates some data with some key or descriptor.

| Query type                 | Description                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| `Metric names`             | Returns a list of all metric names                                                             |
| `Filter keys`              | Returns a list of all the possible<br>dimensions (e.g. Hostname) that can be used to<br>filter |
| `Filter values for key`    | Returns a list of all filtered values by a<br>key name or a key name template variable         |
| `Problem status options`   | Returns a list of all problem<br>statuses                                                      |
| `Problem impact options`   | Returns a list of all problem impacted<br>areas                                                |
| `Problem severity options` | Returns a list of all problem severity<br>types                                                |

- `Regex`— (Optional) Filter out any of the
  returned values from your query with a regular
  expression.

###### Note

`Multi-value` and `Include All option` are
currently not supported by the Dynatrace data source.

After creating a variable, you can find it in the
**Metric** drop-down menu.

##### Import a dashboard for

Dynatrace

To import a dashboard, see [Importing a dashboard](dashboard-export-and-import.md#importing-a-dashboard "dashboard-export-and-import.md#importing-a-dashboard"). Imported dashboards can
be found in **Configuration** > **Data
Sources** > select your Dynatrace data source > select
the **Dashboards** tab to see available pre-made
dashboards.
