# Connect to an Azure Monitor data

source

The Azure Monitor data source supports multiple services in the Azure cloud:

- **Azure Monitor service** is the platform
  service that provides a single source for monitoring Azure resources. For
  more information, see [Querying the Azure Monitor
  service](#query-the-azure-monitor-service "#query-the-azure-monitor-service").
- **Application Insights server** is an
  extensible Application Performance Management (APM) service for web
  developers on multiple platforms and can be used to monitor your live web
  application - it will automatically detect performance anomalies. For more
  information, see [Querying the
  Application Insights Analytics service](#query-the-application-insights-analytics-service "#query-the-application-insights-analytics-service").
- **Azure Log Analytics** (or Azure Logs) gives
  you access to log data collected by Azure Monitor. For more information, see
  [Querying the Azure
  Log Analytics service](#querying-the-azure-log-analytics-service "#querying-the-azure-log-analytics-service").
- Use the **Application Insights Analytics
  service** to query [Application Insights data](https://docs.microsoft.com/en-us/azure/azure-monitor/app/analytics "https://docs.microsoft.com/en-us/azure/azure-monitor/app/analytics") using the same query language used
  for Azure Log Analytics. For more information, see [Querying the
  Application Insights Analytics service](#query-the-application-insights-analytics-service "#query-the-application-insights-analytics-service").

## Adding the data source

The data source can access metrics from four different services. You can
configure access to the services that you use. It is also possible to use the
same credentials for multiple services if that is how you have set it up in
Azure Entra ID.

- [Register a Microsoft Entra app and create a service principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal "https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal")

1. Accessed from the Grafana main menu, newly installed data sources can
   be added immediately within the Data Sources section. Next, choose the
   **Add data source** button in the upper right. The
   Azure Monitor data source will be available for selection in the Cloud
   section in the list of data sources.
2. In the name field, Grafana will automatically fill in a name for the
   data source: `Azure Monitor` or something such as `Azure
Monitor - 3`. If you are configuring multiple data sources,
   change the name to something more informative.
3. If you are using Azure Monitor, you need four pieces of information
   from the Azure portal (for detailed instructions, see the link provided
   earlier):
   - **Tenant Id** (Azure Entra ID, Properties, Directory ID)
   - **Client Id** (Azure Entra ID, App Registrations, Choose your app, Application ID)
   - **Client Secret** (Azure Entra ID, App Registrations, Choose your app, Keys)
   - **Default Subscription Id**
     (Subscriptions, Choose subscription, Overview, Subscription ID)

4. Paste these four items into the fields in the Azure Monitor API
   Details section.
   - The Subscription Id can be changed per query. Save the data
     source and refresh the page to see the list of subscriptions
     available for the specified Client Id.

5. If you are also using the Azure Log Analytics service, you must
   specify these two configuration values or reuse the Client Id and Secret
   from the previous step.
   - Client Id (Azure Entra ID, App Registrations, Choose
     your app, Application ID)
   - Client Secret (Azure Entra ID, App Registrations,
     Choose your app, Keys, Create a key, Use client secret)

6. If you are using Application Insights, you need two pieces of
   information from the Azure Portal (for detailed instructions, see the
   link provided earlier):
   - Application ID
   - API Key

7. Paste these two items into the appropriate fields in the Application
   Insights API Details section.
8. Test that the configuration details are correct by choosing the
   **Save & Test** button.

Alternatively on step 4, if you are creating a new Azure Entra ID
App, use the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest "https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest"):

```

az ad sp create-for-rbac -n "http://localhost:3000"

```

## Choosing a service

In the query editor for a panel, after you choose your Azure Monitor data
source, the first step is to select a service. There are four options:

- `Azure Monitor`
- `Application Insights`
- `Azure Log Analytics`
- `Insights Analytics`

The query editor changes depending on which option you select. Azure Monitor
is the default.

## Querying the Azure Monitor

service

The Azure Monitor service provides metrics for all the Azure services that
you have running. It helps you understand how your applications on Azure are
performing, andit proactively finds issues affecting your applications.

If your Azure Monitor credentials give you access to multiple subscriptions,
choose the appropriate subscription first.

Examples of metrics that you can get from the service are:

- `Microsoft.Compute/virtualMachines - Percentage CPU`
- `Microsoft.Network/networkInterfaces - Bytes sent`
- `Microsoft.Storage/storageAccounts - Used Capacity`

The query editor allows you to query multiple dimensions for metrics that
support them. Metrics that support multiple dimensions are those listed in the
[Azure Monitor supported Metrics List](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported "https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported") that have one or more values
listed in the **Dimension** column for the metric.

### Formatting legend keys with aliases for Azure Monitor

The default legend formatting for the Azure Monitor API is:

`metricName{dimensionName=dimensionValue,dimensionTwoName=DimensionTwoValue}`

These can be long, but you can change this formatting by using aliases.
In the **Legend Format** field, you can combine
the following aliases any way that you want.

Azure Monitor examples:

- `Blob Type: {{ blobtype }}`
- `{{ resourcegroup }} - {{ resourcename }}`

### Alias patterns for Azure

Monitor

- `{{ resourcegroup }}` = replaced with the value of the
  Resource Group
- `{{ namespace }}` = replaced with the value of the
  Namespace (for example, Microsoft.Compute/virtualMachines)
- `{{ resourcename }}` = replaced with the value of the
  Resource Name
- `{{ metric }}` = replaced with metric name (for
  example, Percentage CPU)
- `{{ dimensionname }}` = _Legacy as of 7.1+ (for
  backwards compatibility)_ replaced with the first
  dimension’s key/label (as sorted by the key/label) (for
  example, blobtype)
- `{{ dimensionvalue }}` = _Legacy as of 7.1+ (for
  backwards compatibility)_ replaced with first
  dimension’s value (as sorted by the key/label) (for
  example, BlockBlob)
- `{{ arbitraryDim }}` = _Available in
  7.1+_ replaced with the value of the corresponding
  dimension. (for example, `{{ blobtype }}` becomes
  BlockBlob)

### Creating

template variables for Azure Monitor

Instead of hardcoding things such as server, application and sensor name
in your metric queries you can use variables in their place. Variables are
shown as dropdown select boxes at the top of the dashboard. You can use
these dropdown boxes to change the data being displayed in your dashboard.

Note that the Azure Monitor service does not support multiple values yet.
To visualize multiple time series (for example, metrics for server1 and
server2), add multiple queries so that you can view them on the same graph
or in the same table.

The Azure Monitor data source plugin provides the following queries that
you can specify in the **Query** field in the Variable edit
view. You can use them to fill a variable’s options list.

| Name                                                                                                  | Description                                                                        |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `Subscriptions()`                                                                                     | Returns a list of subscriptions.                                                   |
| `ResourceGroups()`                                                                                    | Returns a list of resource groups.                                                 |
| `ResourceGroups(12345678-aaaa-bbbb-cccc-123456789aaa)`                                                | Returns a list of resource groups for a specified<br>subscription.                 |
| `Namespaces(aResourceGroup)`                                                                          | Returns a list of namespaces for the specified resource<br>group.                  |
| `Namespaces(12345678-aaaa-bbbb-cccc-123456789aaa,<br>aResourceGroup)`                                 | Returns a list of namespaces for the specified resource<br>group and subscription. |
| `ResourceNames(aResourceGroup, aNamespace)`                                                           | Returns a list of resource names.                                                  |
| `ResourceNames(12345678-aaaa-bbbb-cccc-123456789aaa,<br>aResourceGroup, aNamespace)`                  | Returns a list of resource names for a specified<br>subscription.                  |
| `MetricNamespace(aResourceGroup, aNamespace,<br>aResourceName)`                                       | Returns a list of metric namespaces.                                               |
| `MetricNamespace(12345678-aaaa-bbbb-cccc-123456789aaa,<br>aResourceGroup, aNamespace, aResourceName)` | Returns a list of metric namespaces for a specified<br>subscription.               |
| `MetricNames(aResourceGroup, aNamespace,<br>aResourceName)`                                           | Returns a list of metric names.                                                    |
| `MetricNames(12345678-aaaa-bbbb-cccc-123456789aaa,<br>aResourceGroup, aNamespace, aResourceName)`     | Returns a list of metric names for a specified<br>subscription.                    |

Examples:

- Resource Groups query: `ResourceGroups()`
- Passing in metric name variable: `Namespaces(cosmo)`
- Chaining template variables: `ResourceNames($rg, $ns)`
- Do not quote parameters: `MetricNames(hg,
Microsoft.Network/publicIPAddresses, grafanaIP)`

For more information about templating and template variables, see [Templates](templates-and-variables.md#templates "templates-and-variables.md#templates").

### List of supported

Azure Monitor metrics

Not all metrics returned by the Azure Monitor API have values. To make
building a query easier, the Grafana data source has a list of supported
Azure Monitor metrics, and it ignores metrics that will never have values.
This list is updated regularly as new services and metrics are added to the
Azure cloud.

### Azure Monitor alerting

Grafana alerting is supported for the Azure Monitor service. This is not
Azure Alerts support. For more information about Grafana alerting, see [Grafana alerting](alerts-overview.md "alerts-overview.md").

## Querying the

Application Insights service

### Formatting legend keys with aliases for Application Insights

The default legend formatting is:

`metricName{dimensionName=dimensionValue,dimensionTwoName=DimensionTwoValue}`

In the Legend Format field, the following aliases can be combined any way
you want.

Application Insights examples:

- `city: {{ client/city }}`
- `{{ metric }} [Location: {{ client/countryOrRegion }}, {{
client/city }}]`

### Alias patterns for

Application Insights

- `{{ groupbyvalue }}` = _Legacy as of Grafana
  7.1+ (for backwards compatibility)_ replaced with the
  first dimension’s key/label (as sorted by the key/label)
- `{{ groupbyname }}` = _Legacy as of Grafana 7.1+
  (for backwards compatibility)_ replaced with first
  dimension’s value (as sorted by the key/label) (for
  example, BlockBlob)
- `{{ metric }}` = replaced with metric name (for
  example, requests/count)
- `{{ arbitraryDim }}` = _Available in
  7.1+_ replaced with the value of the corresponding
  dimension. (for example, `{{ client/city }}` becomes
  Chicago)

### Filter

expressions for Application Insights

The filter field takes an OData filter expression.

Examples:

- `client/city eq 'Boydton'`
- `client/city ne 'Boydton'`
- `client/city ne 'Boydton' and client/city ne 'Dublin'`
- `client/city eq 'Boydton' or client/city eq 'Dublin'`

### Templating with variables for Application Insights

Use the one of the following queries in the **Query**
field in the Variable edit view.

For more information about templating and template variables, see [Templates](templates-and-variables.md#templates "templates-and-variables.md#templates").

| Name                               | Description                                                            |
| ---------------------------------- | ---------------------------------------------------------------------- |
| `AppInsightsMetricNames()`         | Returns a list of metric names.                                        |
| `AppInsightsGroupBys(aMetricName)` | Returns a list of `group by` clauses for the<br>specified metric name. |

Examples:

- Metric Names query: `AppInsightsMetricNames()`
- Passing in metric name variable:
  `AppInsightsGroupBys(requests/count)`
- Chaining template variables:
  `AppInsightsGroupBys($metricnames)`

### Application Insights

alerting

Grafana alerting is supported for Application Insights. This is not Azure
Alerts support. For more information about Grafana alerting, see [Grafana alerting](alerts-overview.md "alerts-overview.md").

## Querying the Azure

Log Analytics service

Queries are written in the new [Azure Log Analytics (or KustoDB) Query Language](https://docs.microsoft.com/en-us/azure/azure-monitor/log-query/query-language "https://docs.microsoft.com/en-us/azure/azure-monitor/log-query/query-language"). A Log Analytics
query can be formatted as time series data or as table data.

If your credentials give you access to multiple subscriptions, then choose
the appropriate subscription before entering queries.

### Time series queries

Time series queries are for the graph panel and other panels such as the
SingleStat panel. Each query must contain at least a datetime column and a
numeric value column. The result must be sorted in ascending order by the
datetime column.

The following code example shows a query that returns the aggregated
count grouped by hour.

```

Perf
| where $__timeFilter(TimeGenerated)
| summarize count() by bin(TimeGenerated, 1h)
| order by TimeGenerated asc

```

A query can also have one or more non-numeric/non-datetime columns, and
those columns are considered dimensions and become labels in the response.
For example, a query that returns the aggregated count grouped by hour,
Computer, and the CounterName.

```

Perf
| where $__timeFilter(TimeGenerated)
| summarize count() by bin(TimeGenerated, 1h), Computer, CounterName
| order by TimeGenerated asc

```

You can also select additional number value columns (with, or without
multiple dimensions). For example, getting a count and average value by
hour, Computer, CounterName, and InstanceName:

```

Perf
| where $__timeFilter(TimeGenerated)
| summarize Samples=count(), ["Avg Value"]=avg(CounterValue)
    by bin(TimeGenerated, $__interval), Computer, CounterName, InstanceName
| order by TimeGenerated asc

```

###### Note

**Tip**: In the previous query, the Kusto
syntax and `Samples=count()``["Avg
 Value"]=...` are used to rename those columns — the
second syntax allowing for the space. This changes the name of the
metric that Grafana uses. As a result, things such as series legends and
table columns will match what you specify. In this example,
`Samples` is displayed instead of `_count`.

### Table queries

Table queries are mainly used in the table panel, and they show a list of
columns and rows. This example query returns rows with the six specified
columns.

```

AzureActivity
| where $__timeFilter()
| project TimeGenerated, ResourceGroup, Category, OperationName, ActivityStatus, Caller
| order by TimeGenerated desc

```

### Formatting the

display name for Log Analytics

The default display name format is:

`metricName{dimensionName=dimensionValue,dimensionTwoName=DimensionTwoValue}`

This can be customized by using the display name field option.

### Azure Log Analytics

macros

To make writing queries easier, Grafana provides several macros that you
can use in the where clause of a query:

- `$__timeFilter()` – Expands to `TimeGenerated
 ≥ datetime(2018-06-05T18:09:58.907Z) and`
  `TimeGenerated ≤ datetime(2018-06-05T20:09:58.907Z)`
  where the from and to datetimes are from the Grafana time picker.
- `$__timeFilter(datetimeColumn)` – Expands to
  `datetimeColumn ≥ datetime(2018-06-05T18:09:58.907Z)
 and`
  `datetimeColumn ≤ datetime(2018-06-05T20:09:58.907Z)`
  where the from and to datetimes are from the Grafana time picker.
- `$__timeFrom()` – Returns the From datetime from
  the Grafana picker. Example:
  `datetime(2018-06-05T18:09:58.907Z)`.
- `$__timeTo()` – Returns the From datetime from the
  Grafana picker. Example:
  `datetime(2018-06-05T20:09:58.907Z)`.
- `$__escapeMulti($myVar)` – is to be used with
  multi-value template variables that contain illegal characters. If
  `$myVar` has the following two values as a string
  `'\\grafana-vm\Network(eth0)\Total','\\hello!'`, then
  it expands to: `@'\\grafana-vm\Network(eth0)\Total',
@'\\hello!'`. If using single value variables there is no
  need for this macro, escape the variable inline instead:
  `@'\$myVar'`.
- `$__contains(colName, $myVar)` – is to be used with
  multi-value template variables. If `$myVar` has the value
  `'value1','value2'`, it expands to: `colName in
('value1','value2')`.

If using the **All** option, check the
**Include All Option** check box and in the
**Custom all value** field, enter the following
value: `all`. If `$myVar` has the
value `all`, the macro will instead expand to `1 ==
 1`. For template variables with numerous options, this
increases the query performance by not building a large
"where..in" clause.

### Azure Log Analytics

built-in variables

There are also some Grafana variables that can be used in Azure Log
Analytics queries:

- `$__interval` - Grafana calculates the minimum time grain
  that can be used to group by time in queries. It returns a time
  grain such as `5m` or `1h` that can be used in
  the bin function; for example, `summarize count() by
bin(TimeGenerated, $__interval)`. For more information
  about interval variables, see [Adding an interval variable](variables-types.md#add-an-interval-variable "variables-types.md#add-an-interval-variable").

### Templating with variables for Azure Log Analytics

Any Log Analytics query that returns a list of values can be used in the
**Query** field in the Variable edit view. There is
also one Grafana function for Log Analytics that returns a list of
workspaces.

For information about templates and template variables, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

| Name                                               | Description                                                                                               |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `workspaces()`                                     | Returns a list of workspaces for the default<br>subscription.                                             |
| `workspaces(12345678-aaaa-bbbb-cccc-123456789aaa)` | Returns a list of workspaces for the specified<br>subscription (the parameter can be quoted or unquoted). |

The following table shows example variable queries.

| Query                                                                                         | Description                                                   |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `subscriptions()`                                                                             | Returns a list of Azure subscriptions.                        |
| `workspaces()`                                                                                | Returns a list of workspaces for default subscription.        |
| `workspaces("12345678-aaaa-bbbb-cccc-123456789aaa")`                                          | Returns a list of workspaces for a specified<br>subscription. |
| `workspaces("$subscription")`                                                                 | With template variable for the subscription parameter.        |
| `workspace("myWorkspace").Heartbeat \|<br>distinct Computer`                                  | Returns a list of virtual machines.                           |
| `workspace("$workspace").Heartbeat \|<br>distinct Computer`                                   | Returns a list of virtual machines with template<br>variable. |
| `workspace("$workspace").Perf \| distinct<br>ObjectName`                                      | Returns a list of objects from the Perf table.                |
| `workspace("$workspace").Perf \| where<br>ObjectName == "$object" \| distinct<br>CounterName` | Returns a list of metric names from the Perf table.           |

The following code xample shows a time series query using
variables.

```

Perf
| where ObjectName == "$object" and CounterName == "$metric"
| where TimeGenerated >= $__timeFrom() and TimeGenerated <= $__timeTo()
| where  $__contains(Computer, $computer)
| summarize avg(CounterValue) by bin(TimeGenerated, $__interval), Computer
| order by TimeGenerated asc

```

### Deep linking from Grafana panels to the Log Analytics query editor in

Azure Portal

Choose a time series in the panel to see a context menu with a link to
**View in Azure Portal**. Choosing that link opens the
Azure Log Analytics query editor in the Azure Portal and runs the query from
the Grafana panel there.

If you’re not currently logged in to the Azure Portal, then the link
opens the login page. The provided link is valid for any account, but it
only displays the query if your account has access to the Azure Log
Analytics workspace specified in the query.

### Azure Log Analytics

alerting

Grafana alerting is supported for Application Insights. This is not Azure
Alerts support. For more information about alerting in Grafana workspaces,
see [Grafana alerting](alerts-overview.md "alerts-overview.md").

## Querying the

Application Insights Analytics service

If you change the service type to **Insights
Analytics**, then a similar editor to the Log Analytics service is
available. This service also uses the Kusto language, so the instructions for
querying data are identical to [Querying the Azure
Log Analytics service](#querying-the-azure-log-analytics-service "#querying-the-azure-log-analytics-service"), except that you query
Application Insights Analytics data instead.
