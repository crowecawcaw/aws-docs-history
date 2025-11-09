# Connect to an Oracle Database data

source

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Adding the data source

Select **Data sources** on the left panel of Grafana.

Select Add Datasource:

Enter `oracle` to find the data source.

Enter Oracle server details.

Enter a hostname (or IP address) along with the port number, and the username
and password to connect.

With the tnsnames option toggle, any valid entry found in your tnsnames.ora
configuration file can be used, along with basic authentication.

Similar to the previous example, but using Kerberos for authentication. See
the kerberos specific setup guide for details on how to configure the OS or
docker container to use kerberos.

Optionally change the time zone used to connect to the Oracle server and to
be used by timezone aware macros. The default setting is UTC.

Save and Test the data source, you should see a green message with
"Database Connection OK"

## Usage

### Macros

To simplify syntax and to allow for dynamic parts, such as date range
filters, the query can contain macros. The column name must be contained
within double-quotes (`"`).

| Macro example                                                                               | Description                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \*$\_\_time(dateColumn)\<br>•                                                               | Will be replaced by an<br>expression to rename the column to `time`. For example,<br>`dateColumn as time` \*$\_\_timeEpoch(dateColumn)\*                                                                                                                                                                                | Will be replaced by an expression to rename the column<br>to `time` and converting the value to unix<br>timestamp (in milliseconds).                                                               |
| \*$\_\_timeFilter(dateColumn)\<br>•                                                         | Will be replaced by a time<br>range filter using the specified column name. For example,<br>`dateColumn BETWEEN TO\_DATE('19700101','yyyymmdd') +<br>(1/24/60/60/1000) \<br>• 1500376552001 AND<br>TO\_DATE('19700101','yyyymmdd') + (1/24/60/60/1000) \*<br>1500376552002` \*$\_\_timeFrom()\*                         | Will be replaced by the start of the currently active<br>time selection converted to `DATE` data type. For<br>example, `TO_DATE('19700101','yyyymmdd') +<br>(1/24/60/60/1000)<br>• 1500376552001`. |
| \*$\_\_timeTo()\<br>•                                                                       | Will be replaced by the end of the<br>currently active time selection converted to `DATE` data<br>type. \*$\_\_timeGroup(dateColumn,"5m")\*                                                                                                                                                                             | Will be replaced by an expression usable in GROUP BY<br>clause.                                                                                                                                    |
| \*$\_\_timeGroup(dateColumn,"5m"[,<br>fillvalue])\*                                         | Will be replaced by an expression usable in GROUP BY<br>clause. Providing a fillValue of NULL or floating value will<br>automatically fill empty series in time range with that<br>value. For example,<br>_t**i**m**e**G**r**o**u**p**c**r**e**a**t**e**d**A\*\*t_, ′1*m*′, 0.\*\_\_timeGroup(dateColumn,"5m",<br>0)\*. |
| \*_t**i**m**e**G**r**o**u**p_(_d**a**t**e**C**o**l**u**m\*\*n_, ‘5*m*’, *N**U**L\*\*L*) \*  | _S**a**m**e**a**s**a**b**o**v**e**b**u**t**N**U**L**L**w**i**l**l**b**e**u**s**e**d**a**s**v**a**l**u**e**f**o**r**m**i**s**s**i**n**g**p**o**i**n**t**s_.\*\_\_timeGroup(dateColumn,"5m",<br>previous)\*                                                                                                               | Same as above but the previous value in that series will<br>be used as fill value if no value has been seen yet NULL<br>will be used.                                                              |
| \*$\_\_unixEpochFilter(dateColumn)\<br>•                                                    | Will be replaced by a<br>time range filter using the specified column name with times<br>represented as unix timestamp (in milliseconds). For<br>example, `dateColumn >= 1500376552001 AND dateColumn<br><= 1500376552002` \*$\_\_unixEpochFrom()\*                                                                     | Will be replaced by the start of the currently active<br>time selection as unix timestamp. For example,<br>`1500376552001`.                                                                        |
| \*$\_\_unixEpochTo()\*                                                                      | Will be replaced by the end of the currently active time<br>selection as unix timestamp. For example,<br>`1500376552002`.                                                                                                                                                                                               |

The plugin also supports notation using braces `{}`. Use this
notation when queries are needed inside parameters.

###### Note

Use one notation type per query. If the query needs braces, all macros
in the query must use braces.

```

$__timeGroup{"dateColumn",'5m'}
$__timeGroup{SYS_DATE_UTC("SDATE"),'5m'}
$__timeGroup{FROM_TZ(CAST("SDATE" as timestamp), 'UTC'), '1h'}

```

The query editor has a **Generated SQL** link that shows
up after a query has run, while in panel edit mode. When you choose the
link, it expands and shows the raw interpolated SQL string that was run.

### Table queries

If the **Format as** query option is set to
**Table** then you can basically do any type of SQL
query. The table panel will automatically show the results of whatever
columns & rows your query returns. You can control the name of the Table
panel columns by using regular `as` SQL column selection syntax.

### Time series queries

If you set **Format as** to **Time
series**, for use in Graph panel for example, the query must
return a column named `time` that returns either a SQL datetime
or any numeric data type representing unix epoch in seconds. Grafana
interprets DATE and TIMESTAMP columns without explicit time zone as UTC. Any
column except `time` and `metric` is treated as a
value column. You can return a column named `metric` that is used
as metric name for the value column.

The following code example shows the `metric` column.

```

SELECT
  $__timeGroup("time_date_time", '5m') AS time,
  MIN("value_double"),
  'MIN' as metric
FROM test_data
WHERE $__timeFilter("time_date_time")
GROUP BY $__timeGroup("time_date_time", '5m')
ORDER BY time

```

### More queries

– using oracle-fake-data-gen

```

SELECT
  $__timeGroup("createdAt", '5m') AS time,
  MIN("value"),
  'MIN' as metric
FROM "grafana_metric"
WHERE $__timeFilter("createdAt")
GROUP BY $__timeGroup("createdAt", '5m')
ORDER BY time

```

The following code example shows a Fake Data time series.

```

SELECT
  "createdAt",
  "value"
FROM "grafana_metric"
WHERE $__timeFilter("createdAt")
ORDER BY "createdAt" ASC

```

```

SELECT
  "createdAt" as time,
  "value" as value
FROM "grafana_metric"
WHERE $__timeFilter("createdAt")
ORDER BY time ASC

```

The following example shows a useful table result.

```

select tc.table_name Table_name
,tc.column_id Column_id
,lower(tc.column_name) Column_name
,lower(tc.data_type) Data_type
,nvl(tc.data_precision,tc.data_length) Length
,lower(tc.data_scale) Data_scale
,tc.nullable nullable
FROM all_tab_columns tc
,all_tables t
WHERE tc.table_name = t.table_name

```

### Templating

Instead of hardcoding things such as server, application and sensor name
in you metric queries you can use variables in their place. Variables are
shown as dropdown select boxes at the top of the dashboard. These dropdown
boxes makes it easy to change the data being displayed in your dashboard.

#### Query variable

If you add a template variable of the type `Query`, you
can write a Oracle query that can return things such as measurement
names, key names or key values that are shown as a dropdown select box.

For example, you can have a variable that contains all values for the
`hostname` column in a table if you specify a query like
this in the templating variable _Query_ setting.

```

SELECT "hostname" FROM host

```

A query can return multiple columns and Grafana will automatically
create a list from them. For example, the following query will return a
list with values from `hostname` and `hostname2`.

```

SELECT "host.hostname", "other_host.hostname2" FROM host JOIN other_host ON host.city = other_host.city

```

To use time range dependent macros such as
`$__timeFilter("time_column")` in your query
the refresh mode of the template variable needs to be set to
_On Time Range Change_.

```

SELECT "event_name" FROM event_log WHERE $__timeFilter("time_column")

```

Another option is a query that can create a key/value variable. The
query should return two columns that are named `__text` and
`__value`. The `__text` column value should be
unique (if it is not unique then the first value is used). The options
in the dropdown list will have a text and value that allows you to have
a friendly name as text and an id as the value. The following example
code shows a query with `hostname` as the text and
`id` as the value.

```

SELECT "hostname" AS __text, "id" AS __value FROM host

```

You can also create nested variables. For example, if you had another
variable named `region`. Then you could have the hosts
variable only show hosts from the current selected region with a query
like this (if `region` is a multi-value variable then use the
`IN` comparison operator rather than `=` to
match against multiple values).

```

SELECT "hostname" FROM host WHERE region IN('$region')

```

#### Using variables in

queries

Template variable values are only quoted when the template variable
is a `multi-value`.

If the variable is a multi-value variable then use the
`IN` comparison operator rather than `=` to
match against multiple values.

There are two syntaxes:

`$<varname>` Example with a template variable named
`hostname`:

```

SELECT
  "atimestamp" as time,
  "aint" as value
FROM table
WHERE $__timeFilter("atimestamp") AND "hostname" IN('$hostname')
ORDER BY "atimestamp" ASC

```

`[[varname]]` Example with a template variable named
`hostname`:

```

SELECT
  "atimestamp" as time,
  "aint" as value
FROM table
WHERE $__timeFilter("atimestamp") AND "hostname" IN('[[hostname]]')
ORDER BY atimestamp ASC

```
