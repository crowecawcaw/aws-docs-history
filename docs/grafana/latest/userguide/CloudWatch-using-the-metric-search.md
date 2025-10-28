# Using the metric

search option

To create a valid query in **Metric Search**, you
must specify the namespace, metric name and at least one statistic. If
**Match Exact** is turned on, you must also specify
all dimensions of the metric that you’re querying. The metrics schema
must match exactly. For more information, see [CloudWatch search expression syntax](../../../AmazonCloudWatch/latest/monitoring/search-expression-syntax.md "../../../AmazonCloudWatch/latest/monitoring/search-expression-syntax.md") .

If **Match Exact** is turned off, you can specify any
number of dimensions by which you want to filter. Up to 100 metrics
matching your filter criteria are returned.

## Dynamic

queries using dimension wildcard characters

You can monitor a dynamic list of metrics by using the asterisk
(`*`) wildcard character for one or more dimension
values.

This helps you monitor metrics for AWS resources, such as EC2
instances or containers. For example, when new instances get created
as part of an auto scaling event, they will automatically appear in
the graph without you having to track the new instance IDs. This
capability is currently limited to retrieving up to 100 metrics. You
can choose **Show Query Preview** to see the search
expression that is automatically built to support wildcard
characters.

By default, the search expression is defined in such a way that
the queried metrics must match the defined dimension names exactly.
This means that in the example only metrics with exactly one
dimension with name `InstanceId` are returned.

To include metrics that have other dimensions defined, you can
turn off **Match Exact**. Turning off
**Match Exact** also creates a search
expression even if you don’t use wildcard characters. Grafana
searches for any metric that matches at least the namespace, metric
name, and all defined dimensions.

## Multi-value template variables

When defining dimension values based on multi-valued template
variables, a search expression is used to query for the matching
metrics. This enables the use of multiple template variables in one
query. You can also use template variables for queries that have the
**Match Exact** option turned off.

Search expressions are currently limited to 1024 characters, so
your query might fail if you have a long list of values. If you want
to query all metrics that have any value for a certain dimension
name, we recommend using the asterisk (`*`) wildcard
character instead of the `All` option.

The use of multi-valued template variables is only supported for
dimension values. Using multi-valued template variables for
`Region`, `Namespace`, or `Metric
 Name` is not supported.

## Metric math

expressions

You can create new time series metrics by operating on top of
CloudWatch metrics using mathematical functions. Arithmetic operators,
unary subtraction, and other functions are supported and can be
applied to CloudWatch metrics. For more information about CloudWatch metric math
functions, see [Using metric math](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md").

As an example, to apply arithmetic operations on a metric, give
an ID (a unique string) to the raw metric. You can then use this ID
and apply arithmetic operations to it in the `Expression`
field of the new metric.

If you use the `Expression` field to reference another
query, such as `queryA * 2`, you cannot create an alert
rule based on that query.

## Period

A period is the length of time associated with a specific
Amazon CloudWatch statistic. Periods are defined in numbers of seconds. Valid
values include 1, 5, 10, 30, or any multiple of 60.

If you keep the period field blank or set to
**auto**, then it calculates automatically
based on the time range. The formula used is `time range in
 seconds / 2000`, and then it moves on to the next higher
value in an array of predefined periods `[60, 300, 900, 3600,
 21600, 86400]`. To see which period Amazon Managed Grafana is using,
choose **Show Query Preview** in the query editor.

## Deep linking from Grafana panels to the CloudWatch console

Choosing a time series in the panel shows a context menu with a
link to **View in CloudWatch console**. Choosing that
link opens a new tab that takes you to the CloudWatch console and displays
all the metrics for that query. If you’re not currently signed in to
the CloudWatch console, the link forwards you to the sign-in page. The
provided link is valid for any AWS account but only displays the
correct metrics if you’re signed in to the AWS account that
corresponds to the selected data source in Grafana.

This feature is not available for metrics that are based on
metric math expressions.
