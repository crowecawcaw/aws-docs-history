# Connect to an SAP HANA data source

[SAP
HANA](https://www.sap.com/products/technology-platform/hana.html "https://www.sap.com/products/technology-platform/hana.html")is a high-performance, in-memory database that speeds up
data-driven, real-time decisions and \ actions. It is developed and marketed by SAP.
The SAP HANA data source plugin helps you to connect your SAP HANA instance with
Grafana.

With the SAP HANA Grafana Enterprise plugin, you can visualize your SAP HANA data
alongside all of your other data sources in Grafana as well as log and metric data
in context. This plugin includes a built-in query editor, supports annotations, and
it allows you to set alerting thresholds, control access, set permissions, and
more.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Features

- **Query editor**— The plugin comes with an
  built-in SQL query editor with syntax highlighting that allows you to
  visualize time series or table data and auto completes basic Grafana
  macros.
- **Data source permissions**— Control who can
  view or query SAP HANA data in Grafana.
- **Annotations**— Overlay SAP HANA events or
  data on any Grafana graph to correlate events with other graph
  data.
- **Alerting**— Set alerts-based metrics stores
  in SAP HANA.
- **Variables for queries**— Create template
  variables in Grafana, which are based on SAP HANA data, and include
  variables in SAP HANA queries to make dashboards interactive.

## Adding the data source

1. Open the Grafana console in the Amazon Managed Grafana workspace and make sure you
   are logged in.
2. In the side menu under **Configuration** (the gear
   icon), choose **Data Sources**.
3. Choose **Add data source**.

###### Note

If you don't see the **Data Sources** link in
your side menu, it means that your current user does not have the
`Admin` role. 4. Select **SAP HANA** from the list of data sources. 5. In the Config editor, enter the following information:

    * For **Server address**, Provide the address
     of the SAP HANA instance. Example :
     `xxxxxxx-xxxx-xxxx-xxxx-xxxxxxx.hana.trial-us10.hanacloud.ondemand.com`.
    * For **Server port**, provide the port of the
     SAP HANA instance.
    * For **Username**, enter the username to use
     to connect to the SAP HANA instance.
    * For **Password**, enter the password for this
     user.
    * (Optional) Enable **Skip TLS verify** if you
     want to skip TLS verification.
    * (Optional) Enable **TLS Client Auth** if you
     need to provide a client cert and key.
    * (Optional) Enable **With CA cert** if you
     want to enable verifying self-signed TLS Certs.
    * (Optional) For **Default schema**, enter a
     default schema to be used. If you omit this, you will need to
     specify the schema in every query.

**Access and permissions**

To connect Grafana to SAP HANA, use dedicated credentials. Only provide
required permissions to the user. First, create a restricted user with username
and password. The following query is an example to create a restricted user.
This query also disables the force password change.

```
CREATE RESTRICTED USER <USER> PASSWORD <PASSWORD> NO FORCE_FIRST_PASSWORD_CHANGE;
```

Next, allow the the user to connect the system through clients such as Grafana
with the following:

```
ALTER USER <USER> ENABLE CLIENT CONNECT;
```

Finally, give the user access to the necessary views, tables, and
schemas.

```
ALTER USER <USER> GRANT ROLE PUBLIC;
GRANT SELECT ON SCHEMA <SCHEMA> TO <USER>;
```

**User level permissions**

Limit access to SAP HANA by clicking on the Permissions tab in the data source
configuration page to enable data source permissions. On the permission page,
Admins can enable permissions and restrict query permissions to specific Users
and Teams.

## Query editor

The SAP HANA Grafana plugin comes with an SQL query editor where you can enter
any HANA queries. If your query return timeseries data, you can format it as
timeseries for visualizing them in a graph panel. The query editor provides auto
completion for supported Grafana macros and syntax highlighting of your SQL
query.

## Annotations

You can use SAP HANA queries as the sources of Grafana annotations. Your
annotation query should return at least one time column and one text column. For
more information about annotations, see [Annotations](dashboard-annotations.md "dashboard-annotations.md").

###### To create annotations from SAP HANA

1. Choose the **Dashboard settings** gear icon.
2. From the left menu, choose **Annotations**,
   **New**.
3. From the **Data source** drop-down menu, select your
   SAP HANA data source instance.
4. In the **Query** field, enter a SAP HANA query that
   returns at least one time field and one text field.
5. In the **Format as** drop-down menu, select
   **Time Series**.
6. For each annotation, configure the **From** fields.

## Templates and variables

To add a new SAP HANA query variable, see [Adding a query variable](variables-types.md#add-a-query-variable "variables-types.md#add-a-query-variable"). Use your SAP HANA data source as
your data source.

The following example query returns the distinct list of `username`
from the `users` table.

```
select distinct("username") from "users"

```

###### Note

Be sure to only select one column in your variable query. If your query
returns two columns, the first column will used as display value and the
second column will be used as the actual value of the variable. If your
query returns more than two columns, they will be rejected.

### Templates and variables

You can use any Grafana variable in your query. The following examples
shows how to use the single / multi variable in your query.

```
-- For example, following query
select * from "users" where "city" = ${city}
-- will be translated into
select * from "users" where "city" = 'london'
--- where you can see ${city} variable translated into actual value in the variable

```

Similar to text, variables also works for numeric fields. In the below
example, `${age}` is a text box variable where it accepts numbers
and then compares against the numeric field in the table.

```
select * from "users" where "age" > ${age}
--- wil be translated into
select * from "users" where "age" > '36'

```

If your variable returns multiple values, then you can use it in SAP HANA
query's `in` condition like below. Note the brackets surrounding
the variable to make the `where in` condition valid in SAP
HANA.

```
select * from "users" where "city" in (${cities})
--- will be translated into
select * from "users" where "city" in ('london','perth','delhi')
--- where you can see ${cities} turned into a list of grafana variables selected.
--- You can also write the same query using shorthand notation as shown below
select * from "users" where "city" in ($cities)

```

### Macros

- `$__timeFilter(<time_column>)`— Applies
  Grafana's time range to the specified column when used in the raw
  query. Applicable to date/timestamp/long time columns.
- `$__timeFilter(<time_column>,
<format>)`— Same as above. But gives the ability
  to specify the format of the time_column stored in the
  database.
- `$__timeFilter(<time_column>, "epoch",
<format>)`— Same as above but can be used
  when your time column is in epoch. format can be one of 's','ms' and
  'ns'.
- `$__fromTimeFilter(<time_column>)`— Same
  as above but can be used when your time column is in epoch. format
  can be one of 's','ms' and 'ns'.
- `$__fromTimeFilter(<time_column>,
<comparison_predicate>)`— Same as above but
  able to specify comparison_predicate.
- `$__fromTimeFilter(<time_column>,
<format>)`— Same as above but able to specify
  format of the time column.
- `$__fromTimeFilter(<time_column>, <format>,
<comparison_predicate>)`— Same as above but
  able to specify comparison_predicate.
- `$__toTimeFilter(<time_column>)`— Returns
  time condition based on grafana's to time over a time field.
- `$__toTimeFilter(<time_column>,
<comparison_predicate>)`— Same as above but
  able to specify comparison_predicate.
- `$__toTimeFilter(<time_column>,
<format>)`— Same as above but able to specify
  format of the time column.
- `$__toTimeFilter(<time_column>,
<comparison_predicate>)`— Same as above but
  able to specify comparison_predicate.
- `$__timeGroup(<time_column>,
<interval>)`— Expands the time column into
  interval groups. Applicable to date/timestamp/long time
  columns..

**$\_\_timeFilter(<time_column>)
macro**

The following example explains the
`$__timeFilter(<time_column>)` macro:

```
- In the following example, the query
select ts, temperature from weather where $__timeFilter(ts)
--- will be translated into
select ts, temperature from weather where ts > '2021-02-24T12:52:48Z' AND ts < '2021-03-24T12:52:48Z'
--- where you can see the grafana dashboard's time range is applied to the column ts in the query.
```

**$\_\_timeFilter(<time_column>, <format>)
macro**

In some cases, time columns in the database are stored in custom formats.
The following example explains the `$__timeFilter(<time_column>,
 <format>)` macro, which helps to filter custom timestamps
based on grafana's time picker:

```
SELECT TO_TIMESTAMP("TS",'YYYYMMDDHH24MISS') AS METRIC_TIME , "VALUE" FROM "SCH"."TBL" WHERE $__timeFilter("TS","YYYYMMDDHH24MISS") -- TS is in 20210421162012 format
SELECT TO_TIMESTAMP("TS",'YYYY-MON-DD') AS METRIC_TIME , "VALUE" FROM "SCH"."TBL" WHERE $__timeFilter("TS","YYYY-MON-DD") -- TS is in 2021-JAN-15 format
```

In the macro, the format can be one of the valid HANA formats matchting
your timestamp column. For example, `YYYYMMDDHH24MISS` is a valid
format when your data is stored in `20210421162012`
format.

**$\_\_timeFilter(<time_column>, "epoch"
<format>) macro**

In some cases, timestamps are stored as epoch timestamps in your DB. The
following example explains the `$__timeFilter(<time_column>,
 "epoch" <format>)` macro which helps to filter epoch
timestamps based on grafana's time picker. In the macro, format can be one
of ms,s or ns. If not specified, s will be treated as default format.

```
SELECT ADD_SECONDS('1970-01-01', "TIMESTAMP") AS "METRIC_TIME", "VALUE" FROM "SCH"."TBL" WHERE $__timeFilter("TIMESTAMP","epoch") -- Example : TIMESTAMP field stored in epoch_second format 1257894000
SELECT ADD_SECONDS('1970-01-01', "TIMESTAMP") AS "METRIC_TIME", "VALUE" FROM "SCH"."TBL" WHERE $__timeFilter("TIMESTAMP","epoch","s") -- Example : TIMESTAMP field stored in epoch_second format 1257894000
SELECT ADD_SECONDS('1970-01-01', "TIMESTAMP"/1000) AS "METRIC_TIME", "VALUE" FROM "SCH"."TBL" WHERE $__timeFilter("TIMESTAMP","epoch","ms") -- Example : TIMESTAMP field stored in epoch_ms format 1257894000000
SELECT ADD_SECONDS('1970-01-01', "TIMESTAMP"/1000000000) AS "METRIC_TIME", "VALUE" FROM "SCH"."TBL" WHERE $__timeFilter("TIMESTAMP","epoch","ns") -- Example : TIMESTAMP field stored in epoch_nanoseconds format 1257894000000000000
```

Instead of using third argument to the $\_\_timeFilter, you can use one of
epoch_s, epoch_ms or epoch_ns as your second argument..

```
SELECT ADD_SECONDS('1970-01-01', "TIMESTAMP"/1000) AS "METRIC_TIME", "VALUE" FROM "SCH"."TBL" WHERE $__timeFilter("TIMESTAMP","epoch","ms")
-- is same as
SELECT ADD_SECONDS('1970-01-01', "TIMESTAMP"/1000) AS "METRIC_TIME", "VALUE" FROM "SCH"."TBL" WHERE $__timeFilter("TIMESTAMP","epoch_ms")

```

**$\_\_fromTimeFilter() and $\_\_toTimeFilter()
macros**

The `$__fromTimeFilter()` macro expands to a condition over a
time field based on Grafana time picker's from time.

This accepts three parameters. First parameter is time field name. You can
pass comparison_predicate or format of the time column as second argument.
If you want to pass both, then format is second parameter and use
comparison_predicate as your third parameter.

**<format>** If the format is not
specified, plugin wil assume that the time column is of timestamp/date type.
If your time column is stored in any other format than timestamp/date, then
pass the format as second argument. <format> can be one of epoch_s,
epoch_ms,epoch_ns or any other custom format like YYYY-MM-DD.

**<comparison_predicate>** optional
parameter. If not passed, plugin will use > as comparison predicate.
<comparison_predicate> can be one of =, !=, <>, <, <=,

> , >=

`$__toTimeFilter()` works the same as $\_\_fromTimeFilter().
Instead of using Grafana's from time, it will use to time. Also the default
comparison predicate will be <.

**$\_\_timeGroup(<time_column>,
<interval>)**

For example, the macro $\_\_timeGroup(timecol,1h) is expanded to
SERIES_ROUND("timecol", 'INTERVAL 1 HOUR') in the query.

The following example explains the `$__timeGroup(<time_column>,
 <interval>) macro.`

```
SELECT $__timeGroup(timestamp,1h),  "user", sum("value") as "value"
FROM "salesdata"
WHERE $__timeFilter("timestamp")
GROUP BY $__timeGroup(timestamp,1h), "user"
ORDER BY $__timeGroup(timestamp,1h) ASC

```

This is translated into the following query where
`$__timeGroup(timestamp,1h)` is expanded into
`SERIES_ROUND("timestamp", 'INTERVAL 1 HOUR')`.

```
SELECT SERIES_ROUND("timestamp", 'INTERVAL 1 HOUR') as "timestamp",  "user", sum("value") as "value"
FROM "salesdata"
WHERE "timestamp" > '2020-01-01T00:00:00Z' AND "timestamp" < '2020-01-01T23:00:00Z'
GROUP BY SERIES_ROUND("timestamp", 'INTERVAL 1 HOUR'), "user"
ORDER BY "timestamp" ASC
```

###### Note

When using group by with $\_\_timeGroup macro, make sure that your
select, sort by fields follows the same name as your group by field.
Otherwise, HANA might not recognize the query.

If you don't want to hard code the interval in $\_\_timeGroup() function,
then you can leave that to Grafana by specifying $\_\_interval as your
interval. Grafana will calculate that interval from dashboard time range.
Example query:

```
SELECT $__timeGroup(timestamp, $__interval), sum("value") as "value"
FROM "salesdata"
WHERE $__timeFilter("timestamp")
GROUP BY $__timeGroup(timestamp, $__interval)
ORDER BY $__timeGroup(timestamp, $__interval) ASC
```

That query is translated into the followin query based on the dashboard
time range.

```
SELECT SERIES_ROUND("timestamp", 'INTERVAL 1 MINUTE'), sum("value") as "value"
FROM "salesdata"
WHERE "timestamp" > '2019-12-31T23:09:14Z' AND "timestamp" < '2020-01-01T23:17:54Z'
GROUP BY SERIES_ROUND("timestamp", 'INTERVAL 1 MINUTE')
ORDER BY SERIES_ROUND("timestamp", 'INTERVAL 1 MINUTE') ASC
```

### Alerting

###### To set up a SAP HANA alert in Grafana

1. Create a graph panel in your dashboard.
2. Create a SAP HANA query in time series format.
3. Choose the **Alert** tab and specify the alerting
   criteria.
4. Choose **Test Rule** to test the alert
   query.
5. Specify the alert recipients, message, and error handling.
6. Save the dashboard.

#### Alerting on

non-timeseries data

To alert on non-timeseries data, use the
`TO_TIMESTAMP('${__to:date}')` macro to make
non-timeseries metrics into timeseries. This will convert your metric
into single point time series query. The format of the query is given
below

```
SELECT TO_TIMESTAMP('${__to:date}'),  <METRIC> FROM <TABLE≶ WHERE <YOUR CONDITIONS>

```

In the following example, a table has four fields called username,
age, city and role. This table doesn't have any time field. We want to
notify when the number of users with dev role is less than three.

```
SELECT  TO_TIMESTAMP('${__to:date}'), count(*) as "count" FROM (
   SELECT 'John' AS "username", 32 AS "age", 'Chennai' as "city", 'dev' as "role" FROM dummy
   UNION ALL SELECT 'Jacob' AS "username", 32 AS "age", 'London' as "city", 'accountant' as "role" FROM dummy
   UNION ALL SELECT 'Ali' AS "username", 42 AS "age", 'Delhi' as "city", 'admin' as "role" FROM dummy
   UNION ALL SELECT 'Raja' AS "username", 12 AS "age", 'New York' as "city", 'ceo' as "role" FROM dummy
   UNION ALL SELECT 'Sara' AS "username", 35 AS "age", 'Cape Town' as "city", 'dev' as "role" FROM dummy
   UNION ALL SELECT 'Ricky' AS "username", 25 AS "age", 'London' as "city", 'accountant' as "role" FROM dummy
   UNION ALL SELECT 'Angelina' AS "username", 31 AS "age", 'London' as "city", 'cxo' as "role" FROM dummy
) WHERE "role" = 'dev'

```
