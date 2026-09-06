

# Using Athena data source
<a name="Athena-using-the-data-source"></a>

## IAM policies
<a name="Athena-policies"></a>

 Grafana needs permissions granted via IAM to be able to read Athena metrics. You can attach these permissions to IAM roles and utilize Grafana's built-in support for assuming roles. Note that you will need to [ Configure the required policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) for your role before adding the data source to Grafana. You will need an admin or an editor role for adding a data source. The built-in Amazon Grafana Athena access policy is defined in the [AWS managed policy: AmazonGrafanaAthenaAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGrafanaAthenaAccess) section. 

## Query Athena data
<a name="Athena-query"></a>

Athena data source provides a standard SQL query editor. Amazon Managed Grafana includes some macros to help with writing more complex timeseries queries. 

Macros


|  Macro  |  Description  |  Example  |  Output Example  | 
| --- | --- | --- | --- | 
|  $\_\_dateFilter(column)  |  $\_\_dateFilter creates a conditional filter that selects the data (using column) based on the date range of the panel.  |  $\_\_date(my\_date)  | my\_date BETWEEN date '2017-07-18' AND date '2017-07-18' | 
|  $\_\_parseTime(column,format)  |  $\_\_parseTime casts a varchar as a timestamp with the given format.  |  $\_\_parseTime(eventtime, 'yyyy-MM-dd''T''HH:mm:ss''Z')  | parse\_datetime(time,'yyyy-MM-dd''T''HH:mm:ss''Z') | 
|  $\_\_timeFilter(column,format)  |  $\_\_timeFilter creates a conditional that filters the data (using column ) based on the time range of the panel. The second argument is used to optionally parse the column from a varchar to a timestamp with a specific format.  | $\_\_timeFilter(time, 'yyyy-MM-dd HH:mm:ss') | TIMESTAMP time BETWEEN TIMESTAMP '2017-07-18T11:15:52Z' AND TIMESTAMP '2017-07-18T11:15:52Z' | 
|  $\_\_timeFrom()  |  $\_\_timeFrom outputs the current starting time of the range of the panel with quotes.  | $\_\_timeFrom() | TIMESTAMP '2017-07-18 11:15:52' | 
|  $\_\_timeTo()  |  $\_\_timeTo  outputs the current ending time of the range of the panel with quotes.  | $\_\_timeTo() | TIMESTAMP '2017-07-18 11:15:52' | 
|  $\_\_timeGroup(column, '1m', format)  |  $\_\_timeGroup  groups timestamps so that there is only 1 point for every period on the graph. The third argument is used to optionally parse the column from a varchar to a timestamp with a specific format.  | $\_\_timeGroup(time,'5m','yyyy-MM-dd''T''HH:mm:ss.SSSSSS''Z') | FROM\_UNIXTIME(FLOOR(TO\_UNIXTIME(parse\_datetime(time,'yyyy-MM-dd''T''HH:mm:ss.SSSSSS''Z'))/300)\*300) | 
|  $\_\_table  |   $\_\_table returns the table selected in the Table selector.  | $\_\_table | my\_table | 
|  $\_\_column  |  $\_\_column returns the column selected in the Column selector (it requires a table).  | $\_\_column  | col1  | 

**Visualization**

Most queries in Athena will be best represented by a table visualization. A query displays return data in a table. If it can be queried, then it can be put displayed as a table.

This example returns results for a table visualization: 

```
SELECT {column_1}, {column_2} FROM {{{table}}};
```

**Timeseries/ Graph visualizations **

For timeseries and graph visualizations, you must: 
+ select a column with a `date` or a `datetime` type. The `date` column must be in ascending order (using `ORDER BY column ASC`).
+ also select a numeric column.

**Inspecting the query **

Amazon Managed Grafana supports macros that Athena does not, which means a query might not work when copied and pasted directly into Athena. To view the full interpolated query, which works directly in Athena, click the **Query Inspector** button. The full query is displayed under the **Query** tab.

## Templates and variables
<a name="using-Athena-templates-variables"></a>

For more information about adding a Athena query variable, see [Adding a query variable](variables-types.md#add-a-query-variable). Use your Athena data source as your data source for the available queries.

Any value queried from an Athena table can be used as a variable. Avoid selecting too many values, as this can cause performance issues.

After creating a variable, you can use it in your Athena queries by using [Variable syntax](templates-and-variables.md#variable-syntax). For more information about variables, see [Templates and variables](templates-and-variables.md).

## Annotations
<a name="using-Athena-annotations"></a>

[Annotations](dashboard-annotations.md) allow you to overlay rich event information on top of graphs. You can add annotations by selecting the panel or by adding annotation queries using the **Dashboard** menu **Annotations** view. 

An example query to automatically add annotations:

```
SELECT
  time as time,
  environment as tags,
  humidity as text
FROM
  tableName
WHERE
  $__dateFilter(time) and humidity > 95
```

The following table represents the descriptions of the columns that can be used to render annotations:


|  Name  |  Description  | 
| --- | --- | 
|  Time  |  The name of the date/time field. Could be a column with a native SQL date/time data type or epoch value.  | 
|  Timeend  |  Optional name of the end date/time field. Could be a column with a native SQL date/time data type or epoch value. (Grafana v6.6\+)  | 
|  Text  |  Event description field.  | 
|  Tags  |  Optional field name to use for event tags as a comma separated string.  | 

## Async query data support
<a name="athena-async-query"></a>

Athena queries in Amazon Managed Grafana are handled in an asynchronous manner to avoid timeouts. Asynchronous queries use separate requests to start the query, then check on its progress, and finally to fetch the results. This avoids timeouts for queries that run for a long time.

## Query result reuse
<a name="athena-query-reuse"></a>

You can reuse the results of previous queries to improve query performance. To enable query reuse, enable is in the **Query result reuse** section of the query editor. This must be done for each query you want to reuse queries.

**Note**  
This feature requires that your Athena instance be on engine version 3. For more information, see [Changing Athena engine versions](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-changing.html) in the *Amazon Athena User Guide*.