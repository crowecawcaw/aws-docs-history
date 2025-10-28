# AWS CLI examples for Performance Insights

In the following sections, learn more about the AWS Command Line Interface (AWS CLI) for Performance Insights and use AWS CLI examples.

###### Topics

- [Built-in help for the AWS CLI for Performance Insights](#USER_PerfInsights.API.CLI "#USER_PerfInsights.API.CLI")
- [Retrieving counter metrics](#USER_PerfInsights.API.Examples.CounterMetrics "#USER_PerfInsights.API.Examples.CounterMetrics")
- [Retrieving the DB load average for top wait
  events](#USER_PerfInsights.API.Examples.DBLoadAverage "#USER_PerfInsights.API.Examples.DBLoadAverage")
- [Retrieving the DB load average for top
  SQL](#USER_PerfInsights.API.Examples.DBLoadAverageTop10SQL "#USER_PerfInsights.API.Examples.DBLoadAverageTop10SQL")
- [Retrieving the DB load average
  filtered by SQL](#USER_PerfInsights.API.Examples.DBLoadAverageFilterBySQL "#USER_PerfInsights.API.Examples.DBLoadAverageFilterBySQL")
- [Retrieving the full text of a SQL
  statement](#USER_PerfInsights.API.Examples.GetDimensionKeyDetails "#USER_PerfInsights.API.Examples.GetDimensionKeyDetails")
- [Creating a performance analysis report for a time period](#USER_PerfInsights.API.Examples.CreatePerfAnalysisReport "#USER_PerfInsights.API.Examples.CreatePerfAnalysisReport")
- [Retrieving a performance analysis report](#USER_PerfInsights.API.Examples.GetPerfAnalysisReport "#USER_PerfInsights.API.Examples.GetPerfAnalysisReport")
- [Listing all the performance analysis reports for the DB instance](#USER_PerfInsights.API.Examples.ListPerfAnalysisReports "#USER_PerfInsights.API.Examples.ListPerfAnalysisReports")
- [Deleting a performance analysis report](#USER_PerfInsights.API.Examples.DeletePerfAnalysisReport "#USER_PerfInsights.API.Examples.DeletePerfAnalysisReport")
- [Adding tag to a performance analysis report](#USER_PerfInsights.API.Examples.TagPerfAnalysisReport "#USER_PerfInsights.API.Examples.TagPerfAnalysisReport")
- [Listing all the tags for a performance analysis report](#USER_PerfInsights.API.Examples.ListTagsPerfAnalysisReport "#USER_PerfInsights.API.Examples.ListTagsPerfAnalysisReport")
- [Deleting tags from a performance analysis report](#USER_PerfInsights.API.Examples.UntagPerfAnalysisReport "#USER_PerfInsights.API.Examples.UntagPerfAnalysisReport")

## Built-in help for the AWS CLI for Performance Insights

You can view Performance Insights data using the AWS CLI. You can view help for the AWS CLI commands for
Performance Insights by entering the following on the command line.

```
aws pi help
```

If you don't have the AWS CLI installed, see [Installing the
AWS CLI](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in the _AWS CLI User Guide_ for information
about installing it.

## Retrieving counter metrics

The following screenshot shows two counter metrics charts in the AWS Management Console.

![Counter Metrics charts.](images/perf-insights-api-counters-charts.png)

The following example shows how to gather the same data that the AWS Management Console uses to generate the two counter
metric charts.

For Linux, macOS, or Unix:

```
aws pi get-resource-metrics \
   --service-type RDS \
   --identifier db-`ID` \
   --start-time `2018-10-30T00:00:00Z` \
   --end-time   `2018-10-30T01:00:00Z` \
   --period-in-seconds `60` \
   --metric-queries '[{"Metric": "os.cpuUtilization.user.avg"  },
                      {"Metric": "os.cpuUtilization.idle.avg"}]'
```

For Windows:

```
aws pi get-resource-metrics ^
   --service-type RDS ^
   --identifier db-`ID` ^
   --start-time `2018-10-30T00:00:00Z` ^
   --end-time   `2018-10-30T01:00:00Z` ^
   --period-in-seconds `60` ^
   --metric-queries '[{"Metric": "os.cpuUtilization.user.avg"  },
                      {"Metric": "os.cpuUtilization.idle.avg"}]'
```

You can also make a command easier to read by specifying a file for the `--metrics-query`
option. The following example uses a file called query.json for the option. The file has the following
contents.

```
[
    {
        "Metric": "os.cpuUtilization.user.avg"
    },
    {
        "Metric": "os.cpuUtilization.idle.avg"
    }
]
```

Run the following command to use the file.

For Linux, macOS, or Unix:

```
aws pi get-resource-metrics \
   --service-type RDS \
   --identifier db-`ID` \
   --start-time `2018-10-30T00:00:00Z` \
   --end-time   `2018-10-30T01:00:00Z` \
   --period-in-seconds `60` \
   --metric-queries file://`query.json`
```

For Windows:

```
aws pi get-resource-metrics ^
   --service-type RDS ^
   --identifier db-`ID` ^
   --start-time `2018-10-30T00:00:00Z` ^
   --end-time   `2018-10-30T01:00:00Z` ^
   --period-in-seconds `60` ^
   --metric-queries file://`query.json`
```

The preceding example specifies the following values for the options:

- `--service-type` – `RDS` for Amazon RDS
- `--identifier` – The resource ID for the DB instance
- `--start-time` and `--end-time` – The ISO 8601 `DateTime`
  values for the period to query, with multiple supported formats

It queries for a one-hour time range:

- `--period-in-seconds` – `60` for a per-minute query
- `--metric-queries` – An array of two queries, each just for one metric.

The metric name uses dots to classify the metric in a useful category, with the final element being
a function. In the example, the function is `avg` for each query. As with Amazon CloudWatch, the
supported functions are `min`, `max`, `total`, and
`avg`.

The response looks similar to the following.

```
{
    "Identifier": "db-XXX",
    "AlignedStartTime": 1540857600.0,
    "AlignedEndTime": 1540861200.0,
    "MetricList": [
        { //A list of key/datapoints
            "Key": {
                "Metric": "os.cpuUtilization.user.avg" //Metric1
            },
            "DataPoints": [
                //Each list of datapoints has the same timestamps and same number of items
                {
                    "Timestamp": 1540857660.0, //Minute1
                    "Value": 4.0
                },
                {
                    "Timestamp": 1540857720.0, //Minute2
                    "Value": 4.0
                },
                {
                    "Timestamp": 1540857780.0, //Minute 3
                    "Value": 10.0
                }
                //... 60 datapoints for the os.cpuUtilization.user.avg metric
            ]
        },
        {
            "Key": {
                "Metric": "os.cpuUtilization.idle.avg" //Metric2
            },
            "DataPoints": [
                {
                    "Timestamp": 1540857660.0, //Minute1
                    "Value": 12.0
                },
                {
                    "Timestamp": 1540857720.0, //Minute2
                    "Value": 13.5
                },
                //... 60 datapoints for the os.cpuUtilization.idle.avg metric
            ]
        }
    ] //end of MetricList
} //end of response
```

The response has an `Identifier`, `AlignedStartTime`, and
`AlignedEndTime`. B the `--period-in-seconds` value was `60`, the start and
end times have been aligned to the minute. If the `--period-in-seconds` was `3600`, the
start and end times would have been aligned to the hour.

The `MetricList` in the response has a number of entries, each with a `Key` and a
`DataPoints` entry. Each `DataPoint` has a `Timestamp` and a
`Value`. Each `Datapoints` list has 60 data points because the queries are for
per-minute data over an hour, with `Timestamp1/Minute1`, `Timestamp2/Minute2`, and so
on, up to `Timestamp60/Minute60`.

Because the query is for two different counter metrics, there are two elements in the response
`MetricList`.

## Retrieving the DB load average for top wait

events

The following example is the same query that the AWS Management Console uses to generate a stacked area line graph. This
example retrieves the `db.load.avg` for the last hour with load divided according to the top seven
wait events. The command is the same as the command in [Retrieving counter metrics](#USER_PerfInsights.API.Examples.CounterMetrics "#USER_PerfInsights.API.Examples.CounterMetrics"). However, the query.json file has the
following contents.

```
[
    {
        "Metric": "db.load.avg",
        "GroupBy": { "Group": "db.wait_event", "Limit": 7 }
    }
]
```

Run the following command.

For Linux, macOS, or Unix:

```
aws pi get-resource-metrics \
   --service-type RDS \
   --identifier db-`ID` \
   --start-time `2018-10-30T00:00:00Z` \
   --end-time   `2018-10-30T01:00:00Z` \
   --period-in-seconds `60` \
   --metric-queries file://`query.json`
```

For Windows:

```
aws pi get-resource-metrics ^
   --service-type RDS ^
   --identifier db-`ID` ^
   --start-time `2018-10-30T00:00:00Z` ^
   --end-time   `2018-10-30T01:00:00Z` ^
   --period-in-seconds `60` ^
   --metric-queries file://`query.json`
```

The example specifies the metric of `db.load.avg` and a `GroupBy` of the top seven
wait events. For details about valid values for this example, see [DimensionGroup](../../../performance-insights/latest/APIReference/API_DimensionGroup.md "../../../performance-insights/latest/APIReference/API_DimensionGroup.md") in the _Performance Insights API
Reference._

The response looks similar to the following.

```
{
    "Identifier": "db-XXX",
    "AlignedStartTime": 1540857600.0,
    "AlignedEndTime": 1540861200.0,
    "MetricList": [
        { //A list of key/datapoints
            "Key": {
                //A Metric with no dimensions. This is the total db.load.avg
                "Metric": "db.load.avg"
            },
            "DataPoints": [
                //Each list of datapoints has the same timestamps and same number of items
                {
                    "Timestamp": 1540857660.0, //Minute1
                    "Value": 0.5166666666666667
                },
                {
                    "Timestamp": 1540857720.0, //Minute2
                    "Value": 0.38333333333333336
                },
                {
                    "Timestamp": 1540857780.0, //Minute 3
                    "Value": 0.26666666666666666
                }
                //... 60 datapoints for the total db.load.avg key
            ]
        },
        {
            "Key": {
                //Another key. This is db.load.avg broken down by CPU
                "Metric": "db.load.avg",
                "Dimensions": {
                    "db.wait_event.name": "CPU",
                    "db.wait_event.type": "CPU"
                }
            },
            "DataPoints": [
                {
                    "Timestamp": 1540857660.0, //Minute1
                    "Value": 0.35
                },
                {
                    "Timestamp": 1540857720.0, //Minute2
                    "Value": 0.15
                },
                //... 60 datapoints for the CPU key
            ]
        },
        //... In total we have 8 key/datapoints entries, 1) total, 2-8) Top Wait Events
    ] //end of MetricList
} //end of response
```

In this response, there are eight entries in the `MetricList`. There is one entry for the total
`db.load.avg`, and seven entries each for the `db.load.avg` divided according to
one of the top seven wait events. Unlike in the first example, because there was a grouping dimension, there
must be one key for each grouping of the metric. There can't be only one key for each metric, as in the
basic counter metric use case.

## Retrieving the DB load average for top

SQL

The following example groups `db.wait_events` by the top 10 SQL statements. There are two
different groups for SQL statements:

- `db.sql` – The full SQL statement, such as `select * from customers where
customer_id = 123`
- `db.sql_tokenized` – The tokenized SQL statement, such as `select * from
customers where customer_id = ?`

When analyzing database performance, it can be useful to consider SQL statements that only differ by their
parameters as one logic item. So, you can use `db.sql_tokenized` when querying. However,
especially when you're interested in explain plans, sometimes it's more useful to examine full SQL
statements with parameters, and query grouping by `db.sql`. There is a parent-child relationship
between tokenized and full SQL, with multiple full SQL (children) grouped under the same tokenized SQL
(parent).

The command in this example is the similar to the command in [Retrieving the DB load average for top wait
events](#USER_PerfInsights.API.Examples.DBLoadAverage "#USER_PerfInsights.API.Examples.DBLoadAverage"). However, the query.json file has the
following contents.

```
[
    {
        "Metric": "db.load.avg",
        "GroupBy": { "Group": "db.sql_tokenized", "Limit": 10 }
    }
]
```

The following example uses `db.sql_tokenized`.

For Linux, macOS, or Unix:

```
aws pi get-resource-metrics \
   --service-type RDS \
   --identifier db-`ID` \
   --start-time `2018-10-29T00:00:00Z` \
   --end-time   `2018-10-30T00:00:00Z` \
   --period-in-seconds `3600` \
   --metric-queries file://`query.json`
```

For Windows:

```
aws pi get-resource-metrics ^
   --service-type RDS ^
   --identifier db-`ID` ^
   --start-time `2018-10-29T00:00:00Z` ^
   --end-time   `2018-10-30T00:00:00Z`  ^
   --period-in-seconds `3600` ^
   --metric-queries file://`query.json`
```

This example queries over 24 hours, with a one hour period-in-seconds.

The example specifies the metric of `db.load.avg` and a `GroupBy` of the top seven
wait events. For details about valid values for this example, see [DimensionGroup](../../../performance-insights/latest/APIReference/API_DimensionGroup.md "../../../performance-insights/latest/APIReference/API_DimensionGroup.md") in the _Performance Insights API
Reference._

The response looks similar to the following.

```
{
    "AlignedStartTime": 1540771200.0,
    "AlignedEndTime": 1540857600.0,
    "Identifier": "db-XXX",

    "MetricList": [ //11 entries in the MetricList
        {
            "Key": { //First key is total
                "Metric": "db.load.avg"
            }
            "DataPoints": [ //Each DataPoints list has 24 per-hour Timestamps and a value
                {
                    "Value": 1.6964980544747081,
                    "Timestamp": 1540774800.0
                },
                //... 24 datapoints
            ]
        },
        {
            "Key": { //Next key is the top tokenized SQL
                "Dimensions": {
                    "db.sql_tokenized.statement": "INSERT INTO authors (id,name,email) VALUES\n( nextval(?)  ,?,?)",
                    "db.sql_tokenized.db_id": "pi-2372568224",
                    "db.sql_tokenized.id": "AKIAIOSFODNN7EXAMPLE"
                },
                "Metric": "db.load.avg"
            },
            "DataPoints": [ //... 24 datapoints
            ]
        },
        // In total 11 entries, 10 Keys of top tokenized SQL, 1 total key
    ] //End of MetricList
} //End of response
```

This response has 11 entries in the `MetricList` (1 total, 10 top tokenized SQL), with each
entry having 24 per-hour `DataPoints`.

For tokenized SQL, there are three entries in each dimensions list:

- `db.sql_tokenized.statement` – The tokenized SQL statement.
- `db.sql_tokenized.db_id` – Either the native database ID used to refer to the
  SQL, or a synthetic ID that Performance Insights generates for you if the native database ID
  isn't available. This example returns the `pi-2372568224` synthetic ID.
- `db.sql_tokenized.id` – The ID of the query inside Performance Insights.

In the AWS Management Console, this ID is called the Support ID. It's named this because the ID is data
that AWS Support can examine to help you troubleshoot an issue with your database. AWS takes the
security and privacy of your data extremely seriously, and almost all data is stored encrypted with
your AWS KMS key. Therefore, nobody inside AWS can look at this data. In the
example preceding, both the `tokenized.statement` and the `tokenized.db_id` are
stored encrypted. If you have an issue with your database, AWS Support can help you by referencing
the Support ID.

When querying, it might be convenient to specify a `Group` in `GroupBy`. However, for
finer-grained control over the data that's returned, specify the list of dimensions. For example, if all
that is needed is the `db.sql_tokenized.statement`, then a `Dimensions` attribute can
be added to the query.json file.

```
[
    {
        "Metric": "db.load.avg",
        "GroupBy": {
            "Group": "db.sql_tokenized",
            "Dimensions":["db.sql_tokenized.statement"],
            "Limit": 10
        }
    }
]
```

## Retrieving the DB load average

filtered by SQL

![Filter by SQL chart.](images/perf-insights-api-filter-chart.png)

The preceding image shows that a particular query is selected, and the top average active sessions stacked
area line graph is scoped to that query. Although the query is still for the top seven overall wait events,
the value of the response is filtered. The filter causes it to take into account only sessions that are a
match for the particular filter.

The corresponding API query in this example is similar to the command in [Retrieving the DB load average for top
SQL](#USER_PerfInsights.API.Examples.DBLoadAverageTop10SQL "#USER_PerfInsights.API.Examples.DBLoadAverageTop10SQL"). However, the query.json file has
the following contents.

```
[
 {
        "Metric": "db.load.avg",
        "GroupBy": { "Group": "db.wait_event", "Limit": 5  },
        "Filter": { "db.sql_tokenized.id": "AKIAIOSFODNN7EXAMPLE" }
    }
]
```

For Linux, macOS, or Unix:

```
aws pi get-resource-metrics \
   --service-type RDS \
   --identifier db-`ID` \
   --start-time `2018-10-30T00:00:00Z` \
   --end-time   `2018-10-30T01:00:00Z` \
   --period-in-seconds `60` \
   --metric-queries file://`query.json`
```

For Windows:

```
aws pi get-resource-metrics ^
   --service-type RDS ^
   --identifier db-`ID` ^
   --start-time `2018-10-30T00:00:00Z` ^
   --end-time   `2018-10-30T01:00:00Z` ^
   --period-in-seconds `60` ^
   --metric-queries file://`query.json`
```

The response looks similar to the following.

```
{
    "Identifier": "db-XXX",
    "AlignedStartTime": 1556215200.0,
    "MetricList": [
        {
            "Key": {
                "Metric": "db.load.avg"
            },
            "DataPoints": [
                {
                    "Timestamp": 1556218800.0,
                    "Value": 1.4878117913832196
                },
                {
                    "Timestamp": 1556222400.0,
                    "Value": 1.192823803967328
                }
            ]
        },
        {
            "Key": {
                "Metric": "db.load.avg",
                "Dimensions": {
                    "db.wait_event.type": "io",
                    "db.wait_event.name": "wait/io/aurora_redo_log_flush"
                }
            },
            "DataPoints": [
                {
                    "Timestamp": 1556218800.0,
                    "Value": 1.1360544217687074
                },
                {
                    "Timestamp": 1556222400.0,
                    "Value": 1.058051341890315
                }
            ]
        },
        {
            "Key": {
                "Metric": "db.load.avg",
                "Dimensions": {
                    "db.wait_event.type": "io",
                    "db.wait_event.name": "wait/io/table/sql/handler"
                }
            },
            "DataPoints": [
                {
                    "Timestamp": 1556218800.0,
                    "Value": 0.16241496598639457
                },
                {
                    "Timestamp": 1556222400.0,
                    "Value": 0.05163360560093349
                }
            ]
        },
        {
            "Key": {
                "Metric": "db.load.avg",
                "Dimensions": {
                    "db.wait_event.type": "synch",
                    "db.wait_event.name": "wait/synch/mutex/innodb/aurora_lock_thread_slot_futex"
                }
            },
            "DataPoints": [
                {
                    "Timestamp": 1556218800.0,
                    "Value": 0.11479591836734694
                },
                {
                    "Timestamp": 1556222400.0,
                    "Value": 0.013127187864644107
                }
            ]
        },
        {
            "Key": {
                "Metric": "db.load.avg",
                "Dimensions": {
                    "db.wait_event.type": "CPU",
                    "db.wait_event.name": "CPU"
                }
            },
            "DataPoints": [
                {
                    "Timestamp": 1556218800.0,
                    "Value": 0.05215419501133787
                },
                {
                    "Timestamp": 1556222400.0,
                    "Value": 0.05805134189031505
                }
            ]
        },
        {
            "Key": {
                "Metric": "db.load.avg",
                "Dimensions": {
                    "db.wait_event.type": "synch",
                    "db.wait_event.name": "wait/synch/mutex/innodb/lock_wait_mutex"
                }
            },
            "DataPoints": [
                {
                    "Timestamp": 1556218800.0,
                    "Value": 0.017573696145124718
                },
                {
                    "Timestamp": 1556222400.0,
                    "Value": 0.002333722287047841
                }
            ]
        }
    ],
    "AlignedEndTime": 1556222400.0
} //end of response
```

In this response, all values are filtered according to the contribution of tokenized SQL
AKIAIOSFODNN7EXAMPLE specified in the query.json file. The keys also might follow a different order than a
query without a filter, because it's the top five wait events that affected the filtered SQL.

## Retrieving the full text of a SQL

statement

The following example retrieves the full text of a SQL statement for DB instance
`db-10BCD2EFGHIJ3KL4M5NO6PQRS5`. The `--group` is `db.sql`, and the
`--group-identifier` is `db.sql.id`. In this example,
`my-sql-id` represents a SQL ID retrieved by invoking `pi
 get-resource-metrics` or `pi describe-dimension-keys`.

Run the following command.

For Linux, macOS, or Unix:

```
aws pi get-dimension-key-details \
   --service-type RDS \
   --identifier db-10BCD2EFGHIJ3KL4M5NO6PQRS5 \
   --group db.sql \
   --group-identifier `my-sql-id` \
   --requested-dimensions statement
```

For Windows:

```
aws pi get-dimension-key-details ^
   --service-type RDS ^
   --identifier db-10BCD2EFGHIJ3KL4M5NO6PQRS5 ^
   --group db.sql ^
   --group-identifier `my-sql-id` ^
   --requested-dimensions statement
```

In this example, the dimensions details are available. Thus, Performance Insights retrieves the full text of
the SQL statement, without truncating it.

```
{
    "Dimensions":[
    {
        "Value": "SELECT e.last_name, d.department_name FROM employees e, departments d WHERE e.department_id=d.department_id",
        "Dimension": "db.sql.statement",
        "Status": "AVAILABLE"
    },
    ...
    ]
}
```

## Creating a performance analysis report for a time period

The following example creates a performance analysis report with the `1682969503` start time and `1682979503` end time
for the `db-loadtest-0` database.

```
aws pi create-performance-analysis-report \
        --service-type RDS \
        --identifier db-loadtest-0 \
        --start-time 1682969503 \
        --end-time 1682979503 \
        --region us-west-2
```

The response is the unique identifier `report-0234d3ed98e28fb17`
for the report.

```
{
   "AnalysisReportId": "report-0234d3ed98e28fb17"
}
```

## Retrieving a performance analysis report

The following example retrieves the analysis report details for the
`report-0d99cc91c4422ee61` report.

```
aws pi get-performance-analysis-report \
--service-type RDS \
--identifier db-loadtest-0 \
--analysis-report-id report-0d99cc91c4422ee61 \
--region us-west-2
```

The response provides the report status, ID, time details, and insights.

```

        {
    "AnalysisReport": {
        "Status": "Succeeded",
        "ServiceType": "RDS",
        "Identifier": "db-loadtest-0",
        "StartTime": 1680583486.584,
        "AnalysisReportId": "report-0d99cc91c4422ee61",
        "EndTime": 1680587086.584,
        "CreateTime": 1680587087.139,
        "Insights": [
           ... (Condensed for space)
        ]
    }
}
```

## Listing all the performance analysis reports for the DB instance

The following example lists all the available performance analysis reports for the `db-loadtest-0` database.

```
aws pi list-performance-analysis-reports \
--service-type RDS \
--identifier db-loadtest-0 \
--region us-west-2
```

The response lists all the reports with the report ID, status, and time period details.

```
{
    "AnalysisReports": [
        {
            "Status": "Succeeded",
            "EndTime": 1680587086.584,
            "CreationTime": 1680587087.139,
            "StartTime": 1680583486.584,
            "AnalysisReportId": "report-0d99cc91c4422ee61"
        },
        {
            "Status": "Succeeded",
            "EndTime": 1681491137.914,
            "CreationTime": 1681491145.973,
            "StartTime": 1681487537.914,
            "AnalysisReportId": "report-002633115cc002233"
        },
        {
            "Status": "Succeeded",
            "EndTime": 1681493499.849,
            "CreationTime": 1681493507.762,
            "StartTime": 1681489899.849,
            "AnalysisReportId": "report-043b1e006b47246f9"
        },
        {
            "Status": "InProgress",
            "EndTime": 1682979503.0,
            "CreationTime": 1682979618.994,
            "StartTime": 1682969503.0,
            "AnalysisReportId": "report-01ad15f9b88bcbd56"
        }
    ]
}
```

## Deleting a performance analysis report

The following example deletes the analysis report for the `db-loadtest-0` database.

```
aws pi delete-performance-analysis-report \
--service-type RDS \
--identifier db-loadtest-0 \
--analysis-report-id report-0d99cc91c4422ee61 \
--region us-west-2
```

## Adding tag to a performance analysis report

The following example adds a tag with a key `name` and value `test-tag`
to the `report-01ad15f9b88bcbd56` report.

```
aws pi tag-resource \
--service-type RDS \
--resource-arn arn:aws:pi:us-west-2:356798100956:perf-reports/RDS/db-loadtest-0/report-01ad15f9b88bcbd56 \
--tags Key=name,Value=test-tag \
--region us-west-2
```

## Listing all the tags for a performance analysis report

The following example lists all the tags for the `report-01ad15f9b88bcbd56` report.

```
aws pi list-tags-for-resource \
--service-type RDS \
--resource-arn arn:aws:pi:us-west-2:356798100956:perf-reports/RDS/db-loadtest-0/report-01ad15f9b88bcbd56 \
--region us-west-2
```

The response lists the value and key for all the tags added to the report:

```
{
    "Tags": [
        {
            "Value": "test-tag",
            "Key": "name"
        }
    ]
}
```

## Deleting tags from a performance analysis report

The following example deletes the `name` tag from the `report-01ad15f9b88bcbd56` report.

```
aws pi untag-resource \
--service-type RDS \
--resource-arn arn:aws:pi:us-west-2:356798100956:perf-reports/RDS/db-loadtest-0/report-01ad15f9b88bcbd56 \
--tag-keys name \
--region us-west-2
```

After the tag is deleted, calling the `list-tags-for-resource` API doesn't list this tag.
