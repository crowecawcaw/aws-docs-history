# Connect to a MySQL data source

Add the MySQL data source to be able to query and visualize data from a MySQL
compatible database.

###### Important

Grafana version 8.0 changes the underlying data structure for data frames for
the MySQL, Postgres, and Microsoft SQL Server data sources. As a result, a time
series query result is returned in a wide format. For more information, see
[Wide format](https://grafana.com/developers/plugin-tools/introduction/data-frames#wide-format "https://grafana.com/developers/plugin-tools/introduction/data-frames#wide-format") in the Grafana data frames documentation.

To make your visualizations work as they did before, you might have to do some
manual migrations. One solution is documented on Github at [Postgres/MySQL/MSSQL:
Breaking change in v8.0 related to time series queries and ordering of data
column](https://github.com/grafana/grafana/issues/35534 "https://github.com/grafana/grafana/issues/35534").

## Adding the data source

1. Open the side menu by choosing the Grafana icon in the top header.
2. In the side menu under the **Dashboards** link, you
   should find a link named **Data Sources**.
3. Choose the **+ Add data source** button in the top
   header.
4. Select **MySQL** from the **Type**
   dropdown list.

### Data source options

| Name           | Description                                                                                                                                                                                                                                                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Name`         | The data source name. This is how you see the data<br>source in panels and queries.                                                                                                                                                                                                                                                                                        |
| `Default`      | Default data source means that it will be pre-selected<br>for new panels.                                                                                                                                                                                                                                                                                                  |
| `Host`         | The IP address/hostname and optional port of your MySQL<br>instance.                                                                                                                                                                                                                                                                                                       |
| `Database`     | Name of your MySQL database.                                                                                                                                                                                                                                                                                                                                               |
| `User`         | Database user’s login/username.                                                                                                                                                                                                                                                                                                                                            |
| `Password`     | Database user’s password.                                                                                                                                                                                                                                                                                                                                                  |
| `Max open`     | The maximum number of open connections to the database,<br>default `unlimited` (Grafana v5.4+).                                                                                                                                                                                                                                                                            |
| `Max idle`     | The maximum number of connections in the idle connection<br>pool, default `2` (Grafana v5.4+).                                                                                                                                                                                                                                                                             |
| `Max lifetime` | The maximum amount of time in seconds a connection can<br>be reused, default `14400`/4 hours. This should<br>always be lower than configured [wait_timeout](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_wait_timeout "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_wait_timeout") in MySQL (Grafana v5.4+). |

### Min time interval

A lower limit for the `$_interval`
`$_interval_ms` variables. Recommended to be set to write
frequency, for example `1m` if your data is written every minute.
This option can also be overridden/configured in a dashboard panel under
data source options. This value **must** be
formatted as a number followed by a valid time identifier; for
example, `1m` (1 minute) or `30s` (30 seconds).
The following time identifiers are supported.

| Identifier | Description |
| ---------- | ----------- |
| `y`        | Year        |
| `M`        | Month       |
| `w`        | Week        |
| `d`        | Day         |
| `h`        | Hour        |
| `m`        | Minute      |
| `s`        | Second      |
| `ms`       | Millisecond |

### Database user

permissions

###### Important

The database user that you specify when you add the data source
should be granted only SELECT permissions on the specified database and
tables that you want to query. Grafana does not validate that the query
is safe. The query could include any SQL statement. For example,
statements such as `USE otherdb;` and `DROP TABLE
 user;` would be run. To protect against this, we strongly
recommend that you create a specific MySQL user with restricted
permissions.

The following code example shows creating a specific MySQL user with
restricted permissions.

```

 CREATE USER 'grafanaReader' IDENTIFIED BY 'password';
 GRANT SELECT ON mydatabase.mytable TO 'grafanaReader';

```

To grant access to more databases and tables, you can use wildcard
characters (`*`) in place of database or table if you want.

## Query editor

You find the MySQL query editor in the metrics tab in a panel’s edit mode.
You enter edit mode by choosing the panel title, then **Edit**.

The query editor has a **Generated SQL** link that shows up
after a query has been run, while in panel edit mode. Choose it, and it will
expand and show the raw interpolated SQL string that was run.

### Select

table, time column, and metric column (FROM)

When you enter edit mode for the first time or add a new query, Grafana
will try to prefill the query builder with the first table that has a
timestamp column and a numeric column.

In the FROM field, Grafana will suggest tables that are in the configured
database. To select a table or view in another database that your database
user has access to, you can manually enter a fully qualified name
(database.table) such as `otherDb.metrics`.

The Time column field refers to the name of the column holding your time
values. Selecting a value for the Metric column field is optional. If a
value is selected, the Metric column field will be used as the series name.

The metric column suggestions will only contain columns with a text data
type (text, tinytext, mediumtext, longtext, varchar, char). If you want to
use a column with a different data type as metric column, you can enter the
column name with a cast: `CAST(numericColumn as CHAR)`. You can
also enter arbitrary SQL expressions in the metric column field that
evaluate to a text data type such as `CONCAT(column1, " ",
 CAST(numericColumn as CHAR))`.

### Columns and

aggregation functions (SELECT)

In the `SELECT` row, you can specify what columns and
functions you want to use. In the column field, you can write arbitrary
expressions instead of a column name such as `column1 * column2 /
 column3`.

If you use aggregate functions, you must group your result set. The
editor will automatically add a `GROUP BY time`if you add an
aggregate function.

You can add further value columns by choosing the plus button and
selecting `Column` from the menu. Multiple value columns will be
plotted as separate series in the graph panel.

### Filtering data (WHERE)

To add a filter, choose the plus icon to the right of the
`WHERE` condition. You can remove filters by choosing on the
filter and selecting `Remove`. A filter for the current selected
time range is automatically added to new queries.

### Group By

To group by time or any other columns, choose the plus icon at the end of
the GROUP BY row. The suggestion dropdown list will only show text columns
of your currently selected table but you can manually enter any column. You
can remove the group by choosing on the item and then selecting
`Remove`.

If you add any grouping, all selected columns must have an aggregate
function applied. The query builder will automatically add aggregate
functions to all columns without aggregate functions when you add groupings.

#### Gap filling

Grafana can fill in missing values when you group by time. The time
function accepts two arguments. The first argument is the time window
that you want to group by, and the second argument is the value you want
Grafana to fill missing items with.

### Text editor mode (raw)

You can switch to the raw query editor mode by choosing the hamburger
icon and selecting **Switch editor mode** or by choosing
**Edit SQL** below the query.

###### Note

If you use the raw query editor, be sure that your query at minimum
has `ORDER BY time` and a filter on the returned time range.

## Macros

To simplify syntax and to allow for dynamic parts, such as date range
filters, the query can contain macros.

| Macro example                                               | Description                                                                                                                                                                                                            |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$__time(dateColumn)`                                       | Will be replaced by an expression to convert to a UNIX<br>timestamp and rename the column to `time_sec`; for<br>example, _UNIX_TIMESTAMP(dateColumn) as<br>time_sec_.                                                  |
| `$__timeEpoch(dateColumn)`                                  | Will be replaced by an expression to convert to a UNIX<br>timestamp and rename the column to `time_sec`; for<br>example, _UNIX_TIMESTAMP(dateColumn) as<br>time_sec_.                                                  |
| `$__timeFilter(dateColumn)`                                 | Will be replaced by a time range filter using the specified<br>column name. For example, _dateColumn BETWEEN<br>FROM_UNIXTIME(1494410783) AND<br>FROM_UNIXTIME(1494410983)_.                                           |
| `$__timeFrom()`                                             | Will be replaced by the start of the currently active time<br>selection. For example,<br>_FROM_UNIXTIME(1494410783)_.                                                                                                  |
| `$__timeTo()`                                               | Will be replaced by the end of the currently active time<br>selection. For example,<br>_FROM_UNIXTIME(1494410983)_.                                                                                                    |
| `$__timeGroup(dateColumn,'5m')`                             | Will be replaced by an expression usable in GROUP BY clause.<br>For example,<br>*cast(cast(UNIX_TIMESTAMP(dateColumn)/(300) as<br>signed)*300 as signed),\*                                                            |
| `$__timeGroup(dateColumn,'5m', 0)`                          | Same as the previous row, but with a fill parameter so<br>missing points in that series will be added by grafana and 0<br>will be used as value.                                                                       |
| `$__timeGroup(dateColumn,'5m', NULL)`                       | Same as above but NULL will be used as value for missing<br>points.                                                                                                                                                    |
| `$__timeGroup(dateColumn,'5m', previous)`                   | Same as above but the previous value in that series will be<br>used as fill value if no value has been seen yet NULL will be<br>used (only available in Grafana 5.3+).                                                 |
| `$__timeGroupAlias(dateColumn,'5m')`                        | Will be replaced identical to `$__timeGroup` but<br>with an added column alias (available only in Grafana 5.3+).                                                                                                       |
| `$__unixEpochFilter(dateColumn)`                            | Will be replaced by a time range filter using the specified<br>column name with times represented as Unix timestamp. For<br>example, `dateColumn > 1494410783 AND dateColumn <<br>1494497183`.                         |
| `$__unixEpochFrom()`                                        | Will be replaced by the start of the currently active time<br>selection as Unix timestamp. For example,<br>`1494410783`.                                                                                               |
| `$__unixEpochTo()`                                          | Will be replaced by the end of the currently active time<br>selection as Unix timestamp. For example,<br>`1494497183`.                                                                                                 |
| `$__unixEpochNanoFilter(dateColumn)`                        | Will be replaced by a time range filter using the specified<br>column name with times represented as nanosecond timestamp. For<br>example, `dateColumn > 1494410783152415214 AND<br>dateColumn < 1494497183142514872`. |
| `$__unixEpochNanoFrom()`                                    | Will be replaced by the start of the currently active time<br>selection as nanosecond timestamp. For example,<br>`1494410783152415214`.                                                                                |
| `$__unixEpochNanoTo()`                                      | Will be replaced by the end of the currently active time<br>selection as nanosecond timestamp. For example,<br>`1494497183142514872`.                                                                                  |
| `$__unixEpochGroup(dateColumn,"5m",<br>[fillmode])`         | Same as `$__timeGroup` but for times stored as<br>Unix timestamp (available only in Grafana 5.3+).                                                                                                                     |
| `$\_\_unixEpochGroupAlias(dateColumn,"5m",<br>[fillmode])`` | Same as above but also adds a column alias (available only in<br>Grafana 5.3+).                                                                                                                                        |

The query editor has a **Generated SQL** link that shows up
after a query has run, while in panel edit mode. Choose it, and it will expand
and show the raw interpolated SQL string that was run.

## Table queries

If the **Format as** query option is set to
**Table**, you can basically do any type of SQL query. The
table panel will automatically show the results of whatever columns and rows
your query returns.

The following code shows an example query.

```

SELECT
  title as 'Title',
  user.login as 'Created By' ,
  dashboard.created as 'Created On'
 FROM dashboard
INNER JOIN user on user.id = dashboard.created_by
WHERE $__timeFilter(dashboard.created)

```

You can control the name of the Table panel columns by using regular
`as` SQL column selection syntax.

## Time series queries

If you set **Format as** to **Time
series**, for use in a graph panel for example, the query must return a
column named `time` that returns either a SQL datetime or any numeric
data type representing Unix epoch. Any column except `time` and
`metric` is treated as a value column. You can return a column
named `metric` that is used as metric name for the value column. If
you return multiple value columns and a column named `metric`, this
column is used as prefix for the series name (available only in Grafana
5.3+).

Result sets of time series queries must be sorted by time.

The following code example shows the `metric` column.

```

SELECT
  $__timeGroup(time_date_time,'5m'),
  min(value_double),
  'min' as metric
FROM test_data
WHERE $__timeFilter(time_date_time)
GROUP BY time
ORDER BY time

```

The following code example shows using the fill parameter in the $\_\_timeGroup
macro to convert null values to be zero instead.

```

SELECT
  $__timeGroup(createdAt,'5m',0),
  sum(value_double) as value,
  measurement
FROM test_data
WHERE
  $__timeFilter(createdAt)
GROUP BY time, measurement
ORDER BY time

```

The following code example shows multiple columns.

```

SELECT
  $__timeGroup(time_date_time,'5m'),
  min(value_double) as min_value,
  max(value_double) as max_value
FROM test_data
WHERE $__timeFilter(time_date_time)
GROUP BY time
ORDER BY time

```

There is no support for a dynamic group by time based on time range and panel
width.

## Templating

Instead of hardcoding things such as server, application and sensor name in
your metric queries you can use variables in their place. Variables are shown as
dropdown select boxes at the top of the dashboard. You can use these dropdown
boxes to change the data being displayed in your dashboard.

For more information about templating and template variables, see [Templates](templates-and-variables.md#templates "templates-and-variables.md#templates").

### Query variable

If you add a template variable of the type `Query`, you can
write a MySQL query that can return things such as measurement names, key
names, or key values that are shown as a dropdown select box.

For example, you can have a variable that contains all values for the
`hostname` column in a table if you specify a query such as
this in the templating variable _Query_ setting.

```

SELECT hostname FROM my_host

```

A query can return multiple columns and Grafana will automatically create
a list from them. For example, the following query will return a list with
values from `hostname` and `hostname2`.

```

SELECT my_host.hostname, my_other_host.hostname2 FROM my_host JOIN my_other_host ON my_host.city = my_other_host.city

```

To use time range dependent macros such as
`$__timeFilter(column)` in your query, the refresh mode of
the template variable must be set to _On Time Range
Change_.

```

SELECT event_name FROM event_log WHERE $__timeFilter(time_column)

```

Another option is a query that can create a key/value variable. The query
should return two columns that are named `__text` and
`__value`. The `__text` column value should be
unique (if it is not unique, the first value is used). The options in the
dropdown list will have a text and value so that you can have a friendly
name as text and an ID as the value.

The following code example shows a query with `hostname` as the
text and `id` as the value.

```

SELECT hostname AS __text, id AS __value FROM my_host

```

You can also create nested variables. For example, if you had another
variable named `region`. Then you could have the hosts variable
show only hosts from the current selected region with a query such as this
(if `region` is a multi-value variable then use the
`IN` comparison operator rather than `=` to match
against multiple values).

```

SELECT hostname FROM my_host  WHERE region IN($region)

```

#### Using `__searchFilter` to filter results in Query

Variable

Using `__searchFilter` in the query field will filter the
query result based on what the user types in the dropdown select box.
When nothing has been entered by the user, the default value for
`__searchFilter` is `%`.

###### Note

Important that you surround the `__searchFilter`
expression with quotes as Grafana does not do this for you.

The following example shows how to use `__searchFilter` as
part of the query field to enable searching for `hostname`
while the user types in the dropdown select box.

```

SELECT hostname FROM my_host  WHERE hostname LIKE '$__searchFilter'

```

### Using variables in

queries

From Grafana 4.3.0 to 4.6.0, template variables are always quoted
automatically so if it is a string value do not wrap them in quotes in where
clauses.

From Grafana 4.7.0, template variable values are only quoted when the
template variable is a `multi-value`.

If the variable is a multi-value variable, use the `IN`
comparison operator rather than `=` to match against multiple
values.

There are two syntaxes:

`$<varname>` Example with a template variable named
`hostname`:

```

SELECT
  UNIX_TIMESTAMP(atimestamp) as time,
  aint as value,
  avarchar as metric
FROM my_table
WHERE $__timeFilter(atimestamp) and hostname in($hostname)
ORDER BY atimestamp ASC

```

`[[varname]]` Example with a template variable named
`hostname`:

```

SELECT
  UNIX_TIMESTAMP(atimestamp) as time,
  aint as value,
  avarchar as metric
FROM my_table
WHERE $__timeFilter(atimestamp) and hostname in([[hostname]])
ORDER BY atimestamp ASC

```

#### Turning

off quoting for multi-value variables

Grafana automatically creates a quoted, comma-separated string for
multi-value variables. For example: if `server01` and
`server02` are selected then it will be formatted as:
`'server01', 'server02'`. To turn off quoting, use the
csv formatting option for variables.

`${servers:csv}`

For more information about variable formatting options, see [Advanced variable format
options](templates-and-variables.md#advanced-variable-format-options "templates-and-variables.md#advanced-variable-format-options").

## Annotations

You can use annotations to overlay rich event information on top of graphs.
You add annotation queries via the Dashboard menu / Annotations view. For more
information, see .

The following example code shows a query using a time column with epoch
values.

```

SELECT
  epoch_time as time,
  metric1 as text,
  CONCAT(tag1, ',', tag2) as tags
FROM
  public.test_data
WHERE
  $__unixEpochFilter(epoch_time)

```

The following example code shows a region query using time and timeend columns
with epoch values.

###### Note

Available only in Grafana v6.6+.

```

SELECT
  epoch_time as time,
  epoch_timeend as timeend,
  metric1 as text,
  CONCAT(tag1, ',', tag2) as tags
FROM
  public.test_data
WHERE
  $__unixEpochFilter(epoch_time)

```

The following example code shows a query using a time column of native SQL
date/time data type.

```

SELECT
  native_date_time as time,
  metric1 as text,
  CONCAT(tag1, ',', tag2) as tags
FROM
  public.test_data
WHERE
  $__timeFilter(native_date_time)

```

| Name      | Description                                                                                                          |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| `time`    | The name of the date/time field. Could be a column with a<br>native SQL date/time data type or epoch value.          |
| `timeend` | Optional name of the end date/time field. Could be a column<br>with a native SQL date/time data type or epoch value. |
| `text`    | Event description field.                                                                                             |
| `tags`    | Optional field name to use for event tags as a<br>comma-separated string.                                            |

## Alerting

Time series queries should work in alerting conditions. Table formatted
queries are not yet supported in alert rule conditions.
