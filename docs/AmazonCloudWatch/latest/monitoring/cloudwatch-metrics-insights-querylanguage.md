# Query components and syntax in CloudWatch Metrics Insights

CloudWatch Metrics Insights syntax is as follows.

```
SELECT `FUNCTION`(`metricName`)
FROM `namespace` | SCHEMA(...)
[ WHERE `labelKey` OPERATOR `labelValue` [AND ... ] ]
[ GROUP BY `labelKey` [ , ... ] ]
[ ORDER BY `FUNCTION`() [ DESC | ASC ] ]
[ LIMIT `number` ]
```

The possible clauses in a Metrics Insights query are as follows. None of the keywords
are case sensitive, but the identifiers such as the names of metrics, namespaces, and
dimensions are case sensitive.

**SELECT**

Required. Specifies the function to use to aggregate observations in each time
bucket (determined by the provided period). Also specifies the name of the metric to
query.

The valid values for **FUNCTION** are `AVG`,
`COUNT`, `MAX`, `MIN`, and `SUM`.

- `AVG` calculates the average of the observations matched by the
  query.
- `COUNT` returns the count of the observations matched by the
  query.
- `MAX` returns the maximum value of the observations matched by the
  query.
- `MIN` returns the minimum value of the observations matched by the
  query.
- `SUM` calculates the sum of the observations matched by the
  query.

**FROM**

Required. Specifies the source of the metric. You can specify either the metric
namespace that contains the metric that is to be queried, or a
**SCHEMA** table function. Examples of metric namespaces include
`"AWS/EC2"`, `"AWS/Lambda"`, and metric namespaces that you
have created for your custom metrics.

Metric namespaces that include **/** or any other character that
is not a letter, number, or underscore must be surrounded by double quotation marks.
For more information, see [What needs quotation marks or escape characters?](#cloudwatch-metrics-insights-syntaxdetails "#cloudwatch-metrics-insights-syntaxdetails").

**SCHEMA**

An optional table function that can be used within a **FROM**
clause. Use **SCHEMA** to scope down the query results to only the
metrics that exactly match a list of dimensions, or to metrics that have no
dimensions.

If you use a **SCHEMA** clause, it must contain at least one
argument, and this first argument must be the metric namespace being queried. If you
specify **SCHEMA** with only this namespace argument, the results are
scoped down to only metrics that do not have any dimensions.

If you specify **SCHEMA** with additional arguments, the
additional arguments after the namespace argument must be _label_
keys. Label keys must be dimension names. If you specify one or more of these label
keys, the results are scoped down to only those metrics that have that exact set of
dimensions. The order of these label keys does not matter.

For example:

- **SELECT AVG(CPUUtilization) FROM "AWS/EC2"** matches all
  `CPUUtilization` metrics in the `AWS/EC2` namespace, no
  matter their dimensions, and returns a single aggregated time series.
- **SELECT AVG(CPUUtilization) FROM SCHEMA("AWS/EC2")** matches
  only the `CPUUtilization` metrics in the `AWS/EC2` namespace
  that do not have any dimensions defined.
- **SELECT AVG(CPUUtilization) FROM SCHEMA("AWS/EC2",
  InstanceId)** matches only the `CPUUtilization` metrics that
  were reported to CloudWatch with exactly one dimension, `InstanceId`.
- **SELECT SUM(RequestCount) FROM SCHEMA("AWS/ApplicationELB",
  LoadBalancer, AvailabilityZone)** matches only the
  `RequestCount` metrics that were reported to CloudWatch from
  `AWS/ApplicationELB` with exactly two dimensions,
  `LoadBalancer` and `AvailabilityZone`.

**WHERE**

Optional. Filters the results to only those metrics that match your specified
expression using specific label values for one or more label keys. For example,
**WHERE InstanceType = 'c3.4xlarge'** filters the results to only
`c3.4xlarge` instance types, and **WHERE InstanceType !=
'c3.4xlarge'** filters the results to all instance types except
`c3.4xlarge`.

When you run a query in a monitoring account, you can use `WHERE
 AWS.AccountId` to limit results to only the account that you specify. For
example, `WHERE AWS.AccountId=444455556666` queries metrics from
only account `444455556666`. To limit your query to only metrics
in the monitoring account itself, use `WHERE
 AWS.AccountId=CURRENT_ACCOUNT_ID()`.

Label values must always be enclosed with single quotation marks.

**Using tags in WHERE clauses**

You can filter results by AWS resource tags using the syntax `tag.keyName`. Tag filters follow the same operator rules as dimension filters. For example:

- WHERE `tag.env = 'prod'` filters to metrics from resources tagged with _env=prod_
- WHERE `tag.department != 'test'` excludes metrics from resources tagged with _department=test_

Tag filters can be combined with dimension filters:

`WHERE tag.env = 'prod' AND InstanceType = 'm5.large'`

**Supported operators**

The **WHERE** clause supports the following operators:

- **=** Label value must match the specified string.
- **!=** Label value must not match the specified
  string.
- **AND** Both conditions that are specified must be true to
  match. You can use multiple **AND** keywords to specify two or
  more conditions.

**GROUP BY**

Optional. Groups the query results into multiple time series, each one
corresponding to a different value for the specified label key or keys. For example,
using `GROUP BY InstanceId` returns a different time series for each value
of `InstanceId`. Using `GROUP BY ServiceName, Operation` creates
a different time series for each possible combination of the values of
`ServiceName` and `Operation`.

With a **GROUP BY** clause, by default the results are ordered
in alphabetical ascending order, using the sequence of labels specified in
the **GROUP BY** clause. To change the order of the results, add an **ORDER BY**
clause to your query.

When you run a query in a monitoring account, you can use `GROUP BY AWS.AccountId`
to group the results based on the accounts they are from.

**Using tags in GROUP BY clauses**

You can group results by AWS resource tag values using the syntax `tag.keyName`. For example:

- _GROUP BY tag.environment_ creates separate time series for each environment tag value
- _GROUP BY tag.team, InstanceType_ groups by both tag and dimension values
- _GROUP BY tag.team, AWS.AccountId_ groups by both tag and linked source AccountIDs

###### Note

If some of the matching metrics don't include a specific label key
specified in the **GROUP BY** clause, a null group named `Other` is returned.
For example, if you specify `GROUP BY ServiceName, Operation`
and some of the returned metrics don't include `ServiceName` as a dimension, then
those metrics are displayed as having `Other` as the value for `ServiceName`.

**ORDER BY**

Optional. Specifies the order to use for the returned time series, if the query
returns more than one time series. The order is based on the values found by the
**FUNCTION** that you specify in the **ORDER BY**
clause. The **FUNCTION** is used to calculate a single scalar value
from each returned time series, and that value is used to determine the order.

You also specify whether to use ascending **ASC** or descending
**DESC** order. If you omit this, the default is ascending
**ASC**.

For example, adding an `ORDER BY MAX() DESC` clause orders the results
by the maximum data point observed within the time range, in descending order: meaning
that the time series that has the highest maximum data point is returned first.

The valid functions to use within an **ORDER BY** clause are
`AVG()`, `COUNT()`, `MAX()`, `MIN()`,
and `SUM()`.

If you use an **ORDER BY** clause with a
**LIMIT** clause, the resulting query is a "Top N" query.
**ORDER BY** is also useful for queries that might return a large
number of metrics, because each query can return no more than 500 time series. If a
query matches more than 500 time series, and you use an **ORDER BY**
clause, the time series are sorted and then the 500 time series that come first in the
sort order are the ones that are returned.

**LIMIT**

Optional. Limits the number of time series returned by the query to the value that
you specify. The maximum value that you can specify is 500, and a query that does not
specify a **LIMIT** can also return no more than 500 time
series.

Using a **LIMIT** clause with an **ORDER BY**
clause gives you a "Top N" query.

## What needs quotation marks or escape characters?

In a query, label values must always be surrounded with single quotation marks. For
example, **SELECT MAX(CPUUtilization) FROM "AWS/EC2" WHERE AutoScalingGroupName =
'my-production-fleet'**.

Metric namespaces, metric names, and label keys that contain characters other than
letters, numbers, and underscore (\_) must be surrounded by double quote marks. For
example, **SELECT MAX("My.Metric")**.

If one of these contains a double quotation mark or single quotation mark itself (such
as `Bytes"Input"`), you must escape each quotation mark with a backslash, as in
**SELECT AVG("Bytes\"Input\"")**.

If a metric namespace, metric name, or label key, contains a word that is a reserved
keyword in Metrics Insights, these must also be enclosed in double quotation marks. For
example, if you have a metric named `LIMIT`, you would use `SELECT
 AVG("LIMIT")`. It is also valid to enclose any namespace, metric name, or label in
double quotation marks even if it does not include a reserved keyword.

For a complete list of reserved keywords, see [Reserved keywords](cloudwatch-metrics-insights-reserved-keywords.md "cloudwatch-metrics-insights-reserved-keywords.md").

## Build a rich query step by step

This section illustrates building a full example that uses all possible clauses, step by step.

You can start with the following query, which aggregates all of the Application Load Balancer

`RequestCount` metrics that are collected with both the dimensions
`LoadBalancer` and `AvailabilityZone`.

```
SELECT SUM(RequestCount)
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone)

```

To see metrics only from a specific load balancer, you can add a

**WHERE** clause to limit the metrics returned to only those metrics
where the value of the `LoadBalancer` dimension is
`app/load-balancer-1`.

```
SELECT SUM(RequestCount)
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone)
WHERE LoadBalancer = 'app/load-balancer-1'
```

The preceding query aggregates the `RequestCount` metrics from all

Availability Zones for this load balancer into one time series. If you want to see

different time series for each Availability Zone, we can add a **GROUP
BY** clause.

```
SELECT SUM(RequestCount)
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone)
WHERE LoadBalancer = 'app/load-balancer-1'
GROUP BY AvailabilityZone
```

Next, you can order the results to see the highest values first. The following
**ORDER BY** clause orders the time series in descending order, by the maximum value reported
by each time series during the query time range:

```
SELECT SUM(RequestCount)
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone)
WHERE LoadBalancer = 'app/load-balancer-1'
GROUP BY AvailabilityZone
ORDER BY MAX() DESC
```

You can also use tags to further filter the results. For example, if you want to see results only for load balancers tagged with a specific environment, we can add tag filtering to the
WHERE clause:

```
SELECT SUM(RequestCount) FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone) WHERE LoadBalancer = 'app/load-balancer-1' AND tag.Environment = 'prod' GROUP BY AvailabilityZone ORDER BY MAX() DESC
```

You can also group the results by tag values instead of (or in addition to) dimensions. For example, grouping by the Application tag:

```
SELECT SUM(RequestCount) FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone) WHERE tag.Environment = 'prod' GROUP BY tag.Application ORDER BY MAX() DESC
```

Finally, if we are primarily interested in a "Top N" type of query, we can use a
**LIMIT** clause. This final example limits the results to only the
time series with the five highest `MAX` values.

```
SELECT SUM(RequestCount)
FROM SCHEMA("AWS/ApplicationELB", LoadBalancer, AvailabilityZone)
WHERE LoadBalancer = 'app/load-balancer-1'
GROUP BY AvailabilityZone
ORDER BY MAX() DESC
LIMIT 5

```

## Cross-account query examples

These examples are valid when run in an account set up as a monitoring account in CloudWatch
cross-account observability.

The following example searches all Amazon EC2 instances in the source account
123456789012 and returns the average.

```
SELECT AVG(CpuUtilization)
FROM "AWS/EC2"
WHERE AWS.AccountId ='123456789012'
```

The following example queries the `CPUUtilization` metric in
`AWS/EC2` in all the linked source accounts, and groups the results by
account ID and instance type.

```
SELECT AVG(CpuUtilization)
FROM "AWS/EC2"
GROUP BY AWS.AccountId, InstanceType
```

The following example queries the `CPUUtilization` in the monitoring
account itself.

```
SELECT AVG(CpuUtilization)
FROM "AWS/EC2"
WHERE AWS.AccountId = CURRENT_ACCOUNT_ID()

```
