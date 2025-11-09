# Using the metric

query editor

The metric query editor allows you to build two types of queries -
**Metric Search** and **Metric
Query**. The **Metric Query** option queries data
using CloudWatch Metrics Insights.

## Common query editor

fields

There are three fields that are common to both **Metric
Search** and **Metric Query**
modes.

**Common
fields**

**Id**

The `GetMetricData` API requires that all
queries have a unique ID. Use this field to specify an ID of
choice. The ID can include numbers, letters, and
underscores, and must start with a lowercase letter. If no
ID is specified, Amazon Managed Grafana generates an ID using the
following pattern: `query[refId of the current query
 row]`. For example, `queryA` represents
the first query row in the panel editor.

**Period**

A period is the length of time associated with a specific
CloudWatch statistic. Periods are defined in numbers of seconds.
Valid values include 1, 5, 10, 30, or any multiple of 60. If
you keep the period field blank or set to `auto`,
then it calculates automatically based on the time range and
the CloudWatch retention policy. The formula used is `time
 range in seconds / 2000`, and then it moves on to
the next higher value in an array of predefined periods [60,
300, 900, 3600, 21600, 86400] after removing periods based
on retention. To see which period Amazon Managed Grafana is using, choose
**Show Query Preview** in the query
editor.

**Alias**

The following alias patterns apply.

| Alias pattern          | Description                                                                     | Example result   |
| ---------------------- | ------------------------------------------------------------------------------- | ---------------- |
| `{{region}}`           | Returns the Region.                                                             | `us-east-1`      |
| `{{period}}`           | Returns the period.                                                             | `3000`           |
| `{{metric}}`           | Returns the metric.                                                             | `CPUUtilization` |
| `{{label}}`            | Returns the label returned by the API<br>operation (**Metric Search**<br>only). | `i-01343`        |
| `{{namespace}}`        | Returns the namespace (\*_Metric<br>Search_<br>• only).                         | `AWS/EC2`        |
| `{{stat}}`             | Returns the statistic (\*_Metric<br>Search_<br>• only).                         | `Average`        |
| `{{[dimension name]}}` | Returns the dimension name<br>(\*_Metric Search_<br>• only).                    | `i-01343`        |
