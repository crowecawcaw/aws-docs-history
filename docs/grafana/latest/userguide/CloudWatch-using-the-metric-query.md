# Using the metric

query option to query CloudWatch Metrics Insights data

###### Note

Amazon CloudWatch Metrics Insights is in preview. CloudWatch Metrics Insights features are open to all
AWS accounts. Features might be subject to change.

You can query CloudWatch Metrics Insights data by choosing the `metric
 query` mode in the **Metric query editor**.

CloudWatch Metrics Insights is a powerful high-performance SQL query engine that you
can use to query your metrics at scale. It is a fast, flexible,
SQL-based query engine that you can use to identify trends and patterns
within all of your CloudWatch metrics in real time. It uses a dialect of SQL.
For more information about the Metrics Insights query syntax, see [Query syntax and
keywords](#metrics-insights-syntax-keywords "#metrics-insights-syntax-keywords").

## Query syntax and

keywords

CloudWatch Metrics Insights uses a dialect of SQL. The following example
shows the query syntax.

```
SELECT `FUNCTION`(`metricName`)
FROM `namespace` | [ SCHEMA(`namespace`[, labelKey [, ...] ]) ]
     [ WHERE `labelKey` OPERATOR labelValue [AND|OR|([...])*] [, ...] ]
[ GROUP BY `labelKey` [, ...]]
[ ORDER BY `FUNCTION`() [DESC | ASC] ]
[ LIMIT `number`]

```

Keywords are not case-sensitive, but the identifiers are
case-sensitive. Identifiers include the names of metrics,
namespaces, and dimensions.

The following table provides the query keywords and their
descriptions.

| Keyword      | Description                                                                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FUNCTION`   | Required. Specifies the aggregate function to<br>use, and also specifies the name of the metric to<br>query. Valid values are `AVG`,<br>`COUNT`, `MAX`,<br>`MIN`, and `SUM`.                                                 |
| `MetricName` | Required. For example,<br>`CPUUtilization`.                                                                                                                                                                                  |
| `FROM`       | Required. Specifies the source of the metric.<br>You can specify either the metric namespace that<br>contains the metric to query, or a SCHEMA table<br>function. Some namespace examples are<br>`AWS/EC2` and `AWS/Lambda`. |
| `SCHEMA`     | (Optional) Filters the query results to show<br>only the metrics that are an exact match, or the<br>metrics that do not match.                                                                                               |
| `WHERE`      | (Optional) Filters the results to show only the<br>metrics that match your specified expression. For<br>example, `WHERE InstanceType !=<br>'c3.4xlarge'`.                                                                    |
| `GROUP BY`   | (Optional) Groups the query results into<br>multiple time series. For example, `GROUP BY<br>ServiceName`.                                                                                                                    |
| `ORDER BY`   | (Optional) Specifies the order of time series to<br>return. Options are `ASC` and<br>`DESC`.                                                                                                                                 |
| `LIMIT`      | (Optional) Limits the number of time series to<br>return.                                                                                                                                                                    |

The following are some examples:

- ```
  SELECT AVG(CPUUtilization) FROM "AWS/EC2"
  ```

````

 Matches all `CPUUtilization` metrics in the
 `AWS/EC2` namespace, ignoring their
 dimensions, and returns a single aggregated time series.
* ```
SELECT AVG(CPUUtilization) FROM SCHEMA("AWS/EC2")
````

Matches only the `CPUUtilization` metrics in
the `AWS/EC2` namespace that do not have any
dimensions defined.

- ```
  SELECT AVG(CPUUtilization) FROM SCHEMA("AWS/EC2", InstanceId)
  ```

````

 Matches only the `CPUUtilization`metrics that
 were reported to CloudWatch with exactly one dimension,
 `InstanceId`.
* ```
SELECT SUM(RequestCount) FROM SCHEMA("AWS/ApplicationELB", LoadBalancer,
AvailabilityZone)
````

Mtches only the `RequestCount` metrics that
were reported to CloudWatch from `AWS/ApplicationELB`
with exactly two dimensions, `LoadBalancer`and
`AvailabilityZone`.

Label values must be enclosed by single quotation marks.

### Escape characters

In a query, label values must always be surrounded with single
quotation marks.   For example, `SELECT
 MAX(CPUUtilization) FROM "AWS/EC2" WHERE
 AutoScalingGroupName = 'my-production-fleet'`.

Metric namespaces, metric names, and label keys that contain
characters other than letters, numbers, and underscores
(`_`) must be surrounded by double quotation
marks. For example, `SELECT MAX("My.Metric")`. If one
of these contains a double quotation mark itself (such as
`Bytes"Input"`), you must escape that double
quotation mark with backslashes, as in `SELECT
 AVG("Bytes\"Input\"")`. If a metric namespace, metric
name, or label key, contains a word that is a reserved keyword
in Metrics Insights, these must also be enclosed in double
quotation marks. For example, if you have a metric named
`LIMIT`, you would use `SELECT
 AVG("LIMIT")`. It is also valid to enclose any
namespace, metric name, or label in double quotation marks even
if it does not include a reserved keyword.

## Builder mode and code

mode

You can create a query in `Builder` mode or
`Code` mode.

###### To create a query in `Builder` mode

1. Browse and select a metric namespace, metric name, filter,
   group, and order options using information from the
   preceding table.
2. For each of these options, choose from the list of
   possible options.

###### To create a query in `Code` mode

1. Write your query in the code editor.
2. To run the query, choose **Run query** in
   the code editor.

To create a query in the `builder` mode:

- Browse and select a metric namespace, metric name, filter,
  group, and order options using information from the table
  above.
- For each of these options, choose from the list of
  possible options.

Grafana automatically constructs a SQL query based on your
selections.

To create a query in the `code` mode:

- Write your query in the code editor.
- To run the query, choose the **Run query** on the code editor.

The code editor has a built-in autocomplete feature that gives
suggestions for keywords, aggregations, namespaces, metrics, labels,
and label values. The suggestions are shown when you enter a space,
comma, or dollar sign. You can also use the keyboard combination
`CTRL+Space`.

Code editor can autocomplete the query. However, use of template
variables in the code editor might interfere with the
autocompletion.

## CloudWatch Metrics Insights examples

###### Note

CloudWatch Metrics Insights is in open preview. The preview is open to all AWS accounts
and you do not need to request access. Features might be added or changed before
announcing General Availability.

This section contains examples of useful CloudWatch Metrics Insights queries that you can copy
and use directly or copy and modify in query editor. Some of these examples are already
available in the console, and you can access them by choosing **Add query**
in the **Metrics** view.

### EC2 examples

View CPU utilization per instance metrics

```

SELECT AVG(CPUUtilization)
FROM "AWS/EC2"
GROUP BY InstanceId

```

View the average CPU utilization across the entire fleet

```

SELECT AVG(CPUUtilization)
FROM SCHEMA("AWS/EC2", InstanceId)

```

View the 10 instances with the highest average CPU utilization

```

SELECT MAX(CPUUtilization)
FROM "AWS/EC2"
GROUP BY InstanceId
LIMIT 10

```

View the 10 instances with the highest CPU utilization, ordered by the maximum, in
descending order

```

SELECT AVG(CPUUtilization)
FROM "AWS/EC2"
GROUP BY InstanceId
ORDER BY MAX() DESC
LIMIT 10
```

In this case, the CloudWatch agent is collecting a CPUUtilization metric per
application. This query filters the average of this metric for a specific application
name.

```

SELECT AVG(CPUUtilization)
FROM "AWS/CWAgent"
WHERE ApplicationName = 'eCommerce'
SELECT AVG(ConcurrentExecutions)
FROM "AWS/Lambda"

```

View average execution time for the top 10 Lambda functions, ordered by the maximum,
in descending order

```

SELECT AVG(Duration)
FROM "AWS/Lambda"
GROUP BY FunctionName
ORDER BY MAX() DESC
LIMIT 10

```

View the maximum, average, and minimum of Lambda execution times

```

SELECT MAX(Duration)
FROM "AWS/Lambda"

```

### Application Load Balancer

examples

View metrics that have the dimensions **LoadBalancer** and
**AvailabilityZone**

```

SELECT SUM(RequestCount)
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone)

```

View metrics with number of active concurrent TCP connections

```
SELECT AVG(ActiveConnectionCount)
FROM "AWS/ApplicationELB"

```

### Amazon EBS examples

View top 10 average write bytes per volume in descending order

```

SELECT AVG(VolumeWriteBytes)
FROM "AWS/EBS"
GROUP BY VolumeId
ORDER BY MAX() DESC
LIMIT 10

```

View average Amazon EBS volume write time

```
SELECT AVG(VolumeTotalWriteTime)
FROM "AWS/EBS"


```

View average Amazon EBS volume idle time

```
SELECT AVG(VolumeIdleTime)
FROM "AWS/EBS"
View average burst balance per volume
SELECT AVG(BurstBalance)
FROM "AWS/EBS"
GROUP BY VolumeId
View average read bytes across Amazon EBS volumes
SELECT AVG(VolumeReadBytes)
FROM "AWS/EBS"

```

View average write bytes across Amazon EBS volumes

```
SELECT AVG(VolumeWriteBytes)
FROM "AWS/EBS"

```

### Amazon Simple Storage Service

examples

View average latency group by bucket name

```

SELECT AVG(TotalRequestLatency)
FROM "AWS/S3"
GROUP BY BucketName

```

View average number of objects per bucket across all Amazon S3 buckets

```

SELECT AVG(NumberOfObjects)
FROM "AWS/S3"
GROUP BY BucketName

```

### Amazon Simple

Notification Service examples

Amazon-simple-notificaation-service-examples

```

SELECT AVG(NumberOfMessagesPublished)
FROM "AWS/SNS"

```

View average number of messages failed for each topic name

```
SELECT AVG(NumberOfNotificationsFailed)
FROM "AWS/SNS"
GROUP BY TopicName

```

### AWS API usage examples

View top 20 AWS APIs by the number of calls in your account

```

SELECT COUNT(CallCount)
FROM "AWS/Usage"
WHERE "Type" = 'API'
GROUP BY "Service", "Resource"
ORDER BY SUM() DESC
LIMIT 20

```

## CloudWatch Metrics Insights limits

CloudWatch Metrics Insights currently has the following limits:

- You can query only the most recent three hours of data.
- A single query can process no more than 10,000 metrics. This means that if the `SELECT`, `FROM`, and
  `WHERE` clauses would match more than 10,000 metrics, only the first 10,000 of these metrics that are
  found will be processed by the query.
- A single query can return no more than 500 time series. This means that if the query is processing
  more than 500 metrics, not all metrics will be returned in the query results. If you use an `ORDER BY`
  clause, then all the metrics being processed will be sorted and the 500 that have the highest or lowest
  values according to your `ORDER BY` clause will be returned.
  If you do not include an `ORDER BY` clause, you can't control which 500 matching metrics are returned.
- Each `GetMetricData` operation can have only one query, but you can have multiple widgets in a
  dashboard that each include a query.
