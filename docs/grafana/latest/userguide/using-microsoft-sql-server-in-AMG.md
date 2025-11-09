# Connect to a Microsoft SQL

Server data source

Use the Microsoft SQL Server (MSSQL) data source to query and visualize data from
any Microsoft SQL Server 2005 or newer, including Microsoft Azure SQL Database.

###### Important

Grafana version 8.0 changes the underlying data structure for data frames for
the Microsoft SQL Server, Postgres, and MySQL. As a result, a time series query
result is returned in a wide format. For more information, see [Wide format](https://grafana.com/developers/plugin-tools/introduction/data-frames#wide-format "https://grafana.com/developers/plugin-tools/introduction/data-frames#wide-format") in the Grafana data frames documentation.

To make your visualizations work as they did before, you might have to do some
manual migrations. One solution is documented on Github at [Postgres/MySQL/MSSQL:
Breaking change in v8.0 related to time series queries and ordering of data
column](https://github.com/grafana/grafana/issues/35534 "https://github.com/grafana/grafana/issues/35534").

## Adding the data source

1. Open the side menu by choosing the Grafana icon in the top header.
2. In the side menu under the link,**Configuration**
   you should find a **Data Sources** link.
3. Choose the **+ Add data source** button in the top
   header.
4. Select **Microsoft SQL Server** from the
   **Type** dropdown list.

### Data source options

| Name           | Description                                                                                                                                                 |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Name`         | The data source name. This is how you see the data<br>source in panels and queries.                                                                         |
| `Default`      | Default data source means that it will be pre-selected<br>for new panels.                                                                                   |
| `Host`         | The IP address/hostname and optional port of your MSSQL<br>instance. If port is omitted, default 1433 will be used.                                         |
| `Database`     | Name of your MSSQL database.                                                                                                                                |
| `User`         | Database user’s login/username.                                                                                                                             |
| `Password`     | Database user’s password.                                                                                                                                   |
| `Encrypt`      | This option determines whether or to which extent a<br>secure SSL TCP/IP connection will be negotiated with the<br>server, default `false` (Grafana v5.4+). |
| `Max open`     | The maximum number of open connections to the database,<br>default `unlimited` (Grafana v5.4+).                                                             |
| `Max idle`     | The maximum number of connections in the idle connection<br>pool, default `2` (Grafana v5.4+).                                                              |
| `Max lifetime` | The maximum amount of time in seconds a connection can<br>be reused, default `14400`/4 hours.                                                               |

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
should only be granted SELECT permissions on the specified database and
tables you want to query. Grafana does not validate that the query is
safe. The query could include any SQL statement. For example, statements
such as `DELETE FROM user;` and `DROP TABLE user;`
would be run. To protect against this, we highly recommend that you
create a specific MSSQL user with restricted permissions.

The following example code shows creating a specific MSSQL user with
restricted permissions.

```

 CREATE USER grafanareader WITH PASSWORD 'password'
 GRANT SELECT ON dbo.YourTable3 TO grafanareader

```

Make sure that the user does not get any unwanted permissions from the
public role.

### Known issues

If you’re using an older version of Microsoft SQL Server such as
2008 and 2008R2, you might need to disable encryption to be able to connect.
If possible, we recommend you to use the latest service pack available for
optimal compatibility.

## Query editor

You will find the MSSQL query editor in the metrics tab in the graph,
Singlestat, or table panel’s edit mode. You enter edit mode by choosing the
panel title and then choosing Edit. The editor allows you to define a SQL query
to select data to be visualized.

1. Select _Format as_
   `Time series` (for use in Graph or Singlestat panel’s among
   others) or `Table` (for use in Table panel among others).
2. This is the actual editor where you write your SQL queries.
3. Show help section for MSSQL below the query editor.
4. Show the SQL query that was run. Will be available first after a
   successful query has been run.
5. Add an additional query where an additional query editor will be
   displayed.

## Macros

To simplify syntax and to allow for dynamic parts, such as date range
filters, the query can contain macros.

| Macro example                                | Description                                                                                                                                                                                                                                                                                                               |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$__time(dateColumn)`                        | Will be replaced by an expression to rename the column to<br>_time_. For example, \*dateColumn<br>as time<br>• .                                                                                                                                                                                                          |
| `$__timeEpoch(dateColumn)`                   | Will be replaced by an expression to convert a DATETIME<br>column type to Unix timestamp and rename it to<br>_time_. For example,<br>_DATEDIFF(second, "1970-01-01",<br>dateColumn) AS time_.                                                                                                                             |
| `$__timeFilter(dateColumn)`                  | Will be replaced by a time range filter using the specified<br>column name. For example, _dateColumn BETWEEN<br>"2017-04-21T05:01:17Z" AND<br>"2017-04-21T05:06:17Z"_.                                                                                                                                                    |
| `$__timeFrom()`                              | Will be replaced by the start of the currently active time<br>selection. For example,<br>_"2017-04-21T05:01:17Z"_.                                                                                                                                                                                                        |
| `$__timeTo()`                                | Will be replaced by the end of the currently active time<br>selection. For example,<br>_"2017-04-21T05:06:17Z"_.                                                                                                                                                                                                          |
| `$__timeGroup(dateColumn,'5m'[, fillvalue])` | Will be replaced by an expression usable in GROUP BY clause.<br>Providing a *fillValue<br>• of<br>*NULL<br>• or *floating<br>value<br>• will automatically fill empty series in<br>time range with that value. For example,<br>*CAST(ROUND(DATEDIFF(second,<br>"1970-01-01", time_column)/300.0, 0) as<br>bigint)\*300\*. |
| `$__timeGroup(dateColumn,'5m', 0)`           | Same as preceding but with a fill parameter so missing<br>points in that series will be added by grafana and 0 will be<br>used as value.                                                                                                                                                                                  |
| `$__timeGroup(dateColumn,'5m', NULL)`        | Same as above but NULL will be used as value for missing<br>points.                                                                                                                                                                                                                                                       |
| `$__timeGroup(dateColumn,'5m', previous)`    | Same as above but the previous value in that series will be<br>used as fill value if no value has been seen yet NULL will be<br>used (only available in Grafana 5.3+).                                                                                                                                                    |

The query editor has a **Generated SQL** link that shows up
after a query has been run, while in panel edit mode. Choose it and it will
expand and show the raw interpolated SQL string that was run.

## Table queries

If the query option is set to ,**Format
as\*\***Table\*\* then you can basically do any type
of SQL query. The table panel will automatically show the results of whatever
columns and rows your query returns.

The following example code shows a database table.

```

CREATE TABLE [event] (
  time_sec bigint,
  description nvarchar(100),
  tags nvarchar(100),
)

```

```

CREATE TABLE [mssql_types] (
  c_bit bit, c_tinyint tinyint, c_smallint smallint, c_int int, c_bigint bigint, c_money money, c_smallmoney smallmoney, c_numeric numeric(10,5),
  c_real real, c_decimal decimal(10,2), c_float float,
  c_char char(10), c_varchar varchar(10), c_text text,
  c_nchar nchar(12), c_nvarchar nvarchar(12), c_ntext ntext,
  c_datetime datetime,  c_datetime2 datetime2, c_smalldatetime smalldatetime, c_date date, c_time time, c_datetimeoffset datetimeoffset
)

INSERT INTO [mssql_types]
SELECT
  1, 5, 20020, 980300, 1420070400, '$20000.15', '£2.15', 12345.12,
  1.11, 2.22, 3.33,
  'char10', 'varchar10', 'text',
  N'☺nchar12☺', N'☺nvarchar12☺', N'☺text☺',
  GETDATE(), CAST(GETDATE() AS DATETIME2), CAST(GETDATE() AS SMALLDATETIME), CAST(GETDATE() AS DATE), CAST(GETDATE() AS TIME), SWITCHOFFSET(CAST(GETDATE() AS DATETIMEOFFSET), '-07:00')

```

The following example code shows a query.

```

SELECT * FROM [mssql_types]

```

You can control the name of the Table panel columns by using regular
`AS` SQL column selection syntax, as shown in the following
example code.

```

SELECT
  c_bit as [column1], c_tinyint as [column2]
FROM
  [mssql_types]

```

The resulting table panel:

## Time series queries

If you set **Format as** to **Time
series**, for use in Graph panel for example, the query must have a
column named `time` that returns either a SQL datetime or any numeric
data type representing Unix epoch in seconds. You can return a column named
`metric` that is used as metric name for the value column. Any
column except `time` and `metric` is treated as a value
column. If you omit the `metric` column, the name of the value column
will be the metric name. You can select multiple value columns, each will have
its name as metric. If you return multiple value columns and a column named
`metric` then this column is used as prefix for the series name.

Result sets of time series queries must be sorted by time.

The following example code shows a database table.

```

CREATE TABLE [event] (
  time_sec bigint,
  description nvarchar(100),
  tags nvarchar(100),
)

```

```

CREATE TABLE metric_values (
  time datetime,
  measurement nvarchar(100),
  valueOne int,
  valueTwo int,
)

INSERT metric_values (time, measurement, valueOne, valueTwo) VALUES('2018-03-15 12:30:00', 'Metric A', 62, 6)
INSERT metric_values (time, measurement, valueOne, valueTwo) VALUES('2018-03-15 12:30:00', 'Metric B', 49, 11)
...
INSERT metric_values (time, measurement, valueOne, valueTwo) VALUES('2018-03-15 13:55:00', 'Metric A', 14, 25)
INSERT metric_values (time, measurement, valueOne, valueTwo) VALUES('2018-03-15 13:55:00', 'Metric B', 48, 10)

```

The following example code shows one `value` and one
`metric` column.

```

SELECT
  time,
  valueOne,
  measurement as metric
FROM
  metric_values
WHERE
  $__timeFilter(time)
ORDER BY 1

```

When the preceding query is used in a graph panel, it will produce two series
named `Metric A` and `Metric B` with the values
`valueOne` and `valueTwo` plotted over
`time`.

The following example code shows multiple `value` columns.

```

SELECT
  time,
  valueOne,
  valueTwo
FROM
  metric_values
WHERE
  $__timeFilter(time)
ORDER BY 1

```

When the preceding query is used in a graph panel, it will produce two series
named `Metric A` and `Metric B` with the values
`valueOne` and `valueTwo` plotted over
`time`.

The following example code shows using the $\_\_timeGroup macro.

```

SELECT
  $__timeGroup(time, '3m') as time,
  measurement as metric,
  avg(valueOne)
FROM
  metric_values
WHERE
  $__timeFilter(time)
GROUP BY
  $__timeGroup(time, '3m'),
  measurement
ORDER BY 1

```

When the previous query is used in a graph panel, it will produce two series
named `Metric A` and `Metric B` with the values
`valueOne` and `valueTwo` plotted over
`time`. Any two series lacking a value in a three-minute window
will render a line between those two lines. You’ll notice that the graph to the
right never goes down to zero.

The following example code shows using the $\_\_timeGroup macro with fill
parameter set to zero.

```

SELECT
  $__timeGroup(time, '3m', 0) as time,
  measurement as metric,
  sum(valueTwo)
FROM
  metric_values
WHERE
  $__timeFilter(time)
GROUP BY
  $__timeGroup(time, '3m'),
  measurement
ORDER BY 1

```

When this query is used in a graph panel, the result is two series named
`Metric A` and `Metric B` with a sum of
`valueTwo` plotted over `time`. Any series lacking a
value in a 3 minute window will have a value of zero which you’ll see rendered
in the graph to the right.

## Templating

Instead of hardcoding things such as server, application and sensor name in
your metric queries you can use variables in their place. Variables are shown as
dropdown select boxes at the top of the dashboard. You can use these dropdown
boxes to change the data being displayed in your dashboard.

For more information about templating and template variables, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

### Query variable

If you add a template variable of the type `Query`, you can
write a MSSQL query that can return things such as measurement names, key
names or key values that are shown as a dropdown select box.

For example, you can have a variable that contains all values for the
`hostname` column in a table if you specify a query such as
this in the templating variable _Query_ setting.

```

SELECT hostname FROM host

```

A query can return multiple columns and Grafana will automatically create
a list from them. For example, the following query will return a list with
values from `hostname` and `hostname2`.

```

SELECT [host].[hostname], [other_host].[hostname2] FROM host JOIN other_host ON [host].[city] = [other_host].[city]

```

Another option is a query that can create a key/value variable. The query
should return two columns that are named `__text` and
`__value`. The `__text` column value should be
unique (if it is not unique then the first value is used). The options in
the dropdown list will have a text and value that allow you to have a
friendly name as text and an id as the value. An example query with
`hostname` as the text and `id` as the value:

```

SELECT hostname __text, id __value FROM host

```

You can also create nested variables. For example, if you had another
variable named `region`. Then you could have the hosts variable
only show hosts from the current selected region with a query such as this
(if `region` is a multi-value variable, then use the
`IN` comparison operator rather than `=` to match
against multiple values).

```

SELECT hostname FROM host WHERE region IN ($region)

```

### Using variables in

queries

###### Note

Template variable values are only quoted when the template variable
is a `multi-value`.

If the variable is a multi-value variable then use the `IN`
comparison operator rather than `=` to match against multiple
values.

There are two syntaxes:

`$<varname>` Example with a template variable named
`hostname`:

```

SELECT
  atimestamp time,
  aint value
FROM table
WHERE $__timeFilter(atimestamp) and hostname in($hostname)
ORDER BY atimestamp

```

`[[varname]]` Example with a template variable named
`hostname`:

```

SELECT
  atimestamp as time,
  aint as value
FROM table
WHERE $__timeFilter(atimestamp) and hostname in([[hostname]])
ORDER BY atimestamp

```

#### Turning off quoting for multi-value variables

Grafana automatically creates a quoted, comma-separated string for
multi-value variables. For example, if `server01` and
`server02` are selected then it will be formatted as:
`'server01', 'server02'`. To turn off quoting, use the
csv formatting option for variables.

`${servers:csv}`

For more information about variable formatting options, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

## Annotations

You can use annotations to overlay rich event information on top of graphs.
You add annotation queries via the Dashboard menu / Annotations view. For more
information, see [Annotations](dashboard-annotations.md "dashboard-annotations.md").

**Columns:**

| Name      | Description                                                                                                          |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| `time`    | The name of the date/time field. Could be a column with a<br>native SQL date/time data type or epoch value.          |
| `timeend` | Optional name of the end date/time field. Could be a column<br>with a native SQL date/time data type or epoch value. |
| `text`    | Event description field.                                                                                             |
| `tags`    | Optional field name to use for event tags as a comma<br>separated string.                                            |

The following example code shows database tables.

```

CREATE TABLE [events] (
  time_sec bigint,
  description nvarchar(100),
  tags nvarchar(100),
)

```

We also use the database table defined in [Time series queries](#mssql-time-series-queries "#mssql-time-series-queries").

The following example code shows a query using a time column with epoch
values.

```

SELECT
  time_sec as time,
  description as [text],
  tags
FROM
  [events]
WHERE
  $__unixEpochFilter(time_sec)
ORDER BY 1

```

The following example code shows a region query using time and timeend
columns with epoch values.

```

SELECT
  time_sec as time,
  time_end_sec as timeend,
  description as [text],
  tags
FROM
  [events]
WHERE
  $__unixEpochFilter(time_sec)
ORDER BY 1

```

The following example code shows a query using a time column of native SQL
date/time data type.

```

SELECT
  time,
  measurement as text,
  convert(varchar, valueOne) + ',' + convert(varchar, valueTwo) as tags
FROM
  metric_values
WHERE
  $__timeFilter(time_column)
ORDER BY 1

```

## Stored procedure support

Stored procedures have been verified to work. However, there might be edge
cases where it won’t work as you would expect. Stored procedures should be
supported in table, time series, and annotation queries as long as you use the
same naming of columns and return data in the same format as described
previously in the respective sections.

Macro functions will not work inside a stored procedure.

### Examples

For the following examples, the database table is defined in Time series
queries. Let’s say that you want to visualize four series in a graph panel,
such as all combinations of columns `valueOne`,
`valueTwo` and `measurement`. The graph panel to
the right visualizes what we want to achieve. To solve this, you must use
two queries:

The following example code shows the first query.

```

SELECT
  $__timeGroup(time, '5m') as time,
  measurement + ' - value one' as metric,
  avg(valueOne) as valueOne
FROM
  metric_values
WHERE
  $__timeFilter(time)
GROUP BY
  $__timeGroup(time, '5m'),
  measurement
ORDER BY 1

```

The following example code shows the second query.

```

SELECT
  $__timeGroup(time, '5m') as time,
  measurement + ' - value two' as metric,
  avg(valueTwo) as valueTwo
FROM
  metric_values
GROUP BY
  $__timeGroup(time, '5m'),
  measurement
ORDER BY 1

```

#### Stored procedure using time in epoch format

You can define a stored procedure that will return all data that you
need to render four series in a graph panel such as above. In this case,
the stored procedure accepts two parameters, `@from` and
`@to`, of `int` data types, which should be a
time range (from-to) in epoch format which will be used to filter the
data to return from the stored procedure.

This mimics the `$__timeGroup(time, '5m')` in the select
and group by expressions, and that’s why numerous lengthy expressions
are needed. These could be extracted to MSSQL functions, if
wanted.

```

CREATE PROCEDURE sp_test_epoch(
  @from int,
  @to   int
)   AS
BEGIN
  SELECT
    cast(cast(DATEDIFF(second, {d '1970-01-01'}, DATEADD(second, DATEDIFF(second,GETDATE(),GETUTCDATE()), time))/600 as int)*600 as int) as time,
    measurement + ' - value one' as metric,
    avg(valueOne) as value
  FROM
    metric_values
  WHERE
    time >= DATEADD(s, @from, '1970-01-01') AND time <= DATEADD(s, @to, '1970-01-01')
  GROUP BY
    cast(cast(DATEDIFF(second, {d '1970-01-01'}, DATEADD(second, DATEDIFF(second,GETDATE(),GETUTCDATE()), time))/600 as int)*600 as int),
    measurement
  UNION ALL
  SELECT
    cast(cast(DATEDIFF(second, {d '1970-01-01'}, DATEADD(second, DATEDIFF(second,GETDATE(),GETUTCDATE()), time))/600 as int)*600 as int) as time,
    measurement + ' - value two' as metric,
    avg(valueTwo) as value
  FROM
    metric_values
  WHERE
    time >= DATEADD(s, @from, '1970-01-01') AND time <= DATEADD(s, @to, '1970-01-01')
  GROUP BY
    cast(cast(DATEDIFF(second, {d '1970-01-01'}, DATEADD(second, DATEDIFF(second,GETDATE(),GETUTCDATE()), time))/600 as int)*600 as int),
    measurement
  ORDER BY 1
END

```

Then you can use the following query for your graph panel.

```

DECLARE
  @from int = $__unixEpochFrom(),
  @to int = $__unixEpochTo()

EXEC dbo.sp_test_epoch @from, @to

```

#### Stored procedure using time in datetime format

You can define a stored procedure that will return all data that you
need to render four series in a graph panel such as above. In this case,
the stored procedure accepts two parameters, `@from` and
`@to`, of `datetime` data types, which should
be a time range (from-to) that will be used to filter the data to return
from the stored procedure.

This mimics the `$__timeGroup(time, '5m')` in the select
and group by expressions, and that’s why numerous lengthy expressions
are needed. These could be extracted to MSSQL functions, if wanted.

```

CREATE PROCEDURE sp_test_datetime(
  @from datetime,
  @to   datetime
)   AS
BEGIN
  SELECT
    cast(cast(DATEDIFF(second, {d '1970-01-01'}, time)/600 as int)*600 as int) as time,
    measurement + ' - value one' as metric,
    avg(valueOne) as value
  FROM
    metric_values
  WHERE
    time >= @from AND time <= @to
  GROUP BY
    cast(cast(DATEDIFF(second, {d '1970-01-01'}, time)/600 as int)*600 as int),
    measurement
  UNION ALL
  SELECT
    cast(cast(DATEDIFF(second, {d '1970-01-01'}, time)/600 as int)*600 as int) as time,
    measurement + ' - value two' as metric,
    avg(valueTwo) as value
  FROM
    metric_values
  WHERE
    time >= @from AND time <= @to
  GROUP BY
    cast(cast(DATEDIFF(second, {d '1970-01-01'}, time)/600 as int)*600 as int),
    measurement
  ORDER BY 1
END

```

Then you can use the following query for your graph panel.

```

DECLARE
  @from datetime = $__timeFrom(),
  @to datetime = $__timeTo()

EXEC dbo.sp_test_datetime @from, @to

```

## Alerting

Time series queries should work in alerting conditions. Table formatted
queries are not yet supported in alert rule conditions.
