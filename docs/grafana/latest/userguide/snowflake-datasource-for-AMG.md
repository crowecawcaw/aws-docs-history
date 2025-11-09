# Connect to a Snowflake data

source

With the Snowflake Enterprise data source, you can visualize your Snowflake data
alongside all of your other data sources in Grafana as well as log and metric data
in context. This data source includes a powerful type-ahead query editor, supports
complex annotations, set alerting thresholds, control access and permissions and
more.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Overview

### What is Snowflake?

Snowflake offers a cloud-based data storage and analytics service,
generally termed "data warehouse-as-a-service" that offers a
solution for data warehousing, data lakes, data engineering, data science,
data application development, and data sharing. Over the last few years,
Snowflake has gained massive popularity because of its ability to affordably
store and analyze data using cloud-based hardware and software; recently
culminating in the largest software IPO ever. Today, many companies use
Snowflake as their primary database to store application and business data
such as transaction counts, active user sessions, and even time series and
metric data.

### Making the most of

Snowflake and Amazon Managed Grafana

**Visualize Snowflake data without moving it**:
Grafana’s unique architecture queries data directly where it lives rather
than moving it and paying for redundant storage and ingestion.

**Compose panels from varied sources:** With
pre-built and custom dashboards, bring data together from many different
data sources into a single pane of glass.

**Transform and compute at the user level**:
Users can transform data and run various computations on data they see,
requiring less data preparation.

**Combine, compute, and visualize within
panels**: Create mixed-data source panels that display related
data from Snowflake and other sources.

### Features

**Query editor:** The query editor is a Smart
SQL autocompletion editor that allows you to visualize time series or table
data, handles SQL syntax errors, and autocompletes basic SQL keywords.

**Data source permissions**: Control who can
view or query Snowflake data in Grafana

**Annotations:** Overlay Snowflake events on
any Grafana graph, to correlate events with other graph data

**Alerting:** Set alerts based metrics stores
in Snowflake

**Variables for queries:** Create template
variables in Grafana based on Snowflake data, and include variables in
Snowflake queries to make interactive dashboards.

**Multi-metric queries:** Write a single query
that returns multiple metrics, each in its own column

## Get started with the

Snowflake plugin

Here are five quick steps to get started with the Snowflake plugin in
Grafana:

### Step 1: Set up the

Snowflake Data Source

To configure the data source, choose **Configuration**,
**Data Sources**, **Add data source**,
Snowflake.

Add your authentication details, and the data source is ready to query!

The following configuration fields are available.

| Name                 | Description                           |
| -------------------- | ------------------------------------- |
| Account              | Account for Snowflake.                |
| Username             | Username for the service account.     |
| Password             | Password for the service account.     |
| Schema (optional)    | Sets a default schema for queries.    |
| Warehouse (optional) | Sets a default warehouse for queries. |
| Database (optional)  | Sets a default database for queries.  |
| Role (optional)      | Assumes a role for queries.           |

### Step 2: Write

queries for your Snowflake data

Create a panel in a dashboard, and select a Snowflake Data Source to
start using the query editor.

- Date / time can appear anywhere in the query as long as it is
  included.
- A numerical column must be included. This can be an aggregation
  or an int/float column.
- Optionally, you can include string columns to create separate
  data series, if your time series data is formatted for different
  metrics.

#### Layout of a Snowflake

query

```

select
  <time_column>,
  <any_numerical_column>
  <other_column_1>,
  <other_column_2>,
  <...>
from
  <any_table>
where
  $__timeFilter(<time_column>) // predefined where clause for time range
  and $<custom_variable> = 1 // custom variables start with dollar sign

```

#### SQL

query format for time series group by interval

```

select
  $__timeGroup(created_ts, '1h'), // group time by interval of 1h
  <time_column>,
  <any_numerical_column>,
  <metric_column>
from
  <any_table>
where
  $__timeFilter(<time_column>) // predefined where clause for time range
  and $<custom_variable> = 1 // custom variables start with dollar sign
group by <time_column>

```

#### SQL query format for

tables

```

select
  <time_column>, // optional if result format option is table
  <any_column_1>
  <any_column_2>
  <any_column_3>
from
  <any_table>
where
  $__timeFilter(time_column) // macro for time range, optional if format as option is table
  and $<custom_variable> = 1 // custom variables start with dollar sign

```

### Step 3: Create

and use Template Variables

#### Using template

variables

You can include template variables in queries, as shown in the
following example.

```

 select
   <column>
 from
   <table>
 WHERE column >= '$variable'

```

The following example shows using multi-value variables in a query.

```

select
  <column>
from
  <table>
WHERE <column> regexp '${variable:regex}'

```

#### Using the Snowflake data source to create variables

In the dashboard settings, choose **Variables**, and
choose **New**.

Using the "Query" variable type, select the Snowflake
data source as the "Data source".

###### Important

Be sure to select only one column in your variable query.

Example:

```

SELECT DISTINCT query_type from account_usage.query_history;

```

will give you these variables:

```

All DESCRIBE USE UNKNOWN GRANT SELECT CREATE DROP SHOW

```

### Step 4: Set up an alert

You can set alerts on specific Snowflake metrics or on queries you’ve
created.

Choose the alert tab button within the query editor, and choose **Create Alert**.

### Step 5. Create an

annotation

Annotations allow you to overlay events on a graph.

To create an annotation, in the dashboard settings, choose
**Annotations**, and **New**, and
select Snowflake as the data source.

Because annotations are events, they require at least one time column and
one column to describe the event.

The following example code shows a query to annotate all failed logins to
Snowflake.

```

SELECT
  EVENT_TIMESTAMP as time,
  EVENT_TYPE,
  CLIENT_IP
FROM ACCOUNT_USAGE.LOGIN_HISTORY
WHERE $__timeFilter(time) AND IS_SUCCESS!='YES'
ORDER BY time ASC;

```

And

- time: `TIME`
- title: `EVENT_TYPE`
- text: `CLIENT_IP`

This will overlay annotations of all failed logins to Snowflake on your
dashboard panels.

## Additional functionality

### Using the Display Name

field

This plugin uses the Display Name field in the Field tab of the Options
panel to shorten or alter a legend key based on its name, labels, or values.
Other data sources use custom `alias` functionality to modify
legend keys, but the Display Name function is a more consistent way to do
so.

### Data source

permissions

Limit access to Snowflake by choosing the **Permissions** tab in the data source configuration page to
enable data source permissions. On the permission page, Admins can enable
permissions and restrict query permissions to specific Users and Teams.

### Understand your Snowflake billing and usage data

Within the Snowflake data source, you can import a billing and usage
dashboard that shows you useful billing and usage information.

Add the dashboard in the Snowflake Data Source configuration page:

This dashboard uses the ACCOUNT_USAGE database, and requires the querier
to have the ACCOUNTADMIN role. To do this securely, create a new Grafana
data source that has a user with the ACCOUNTADMIN role. Then select that
data source in the variables.
