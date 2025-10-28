# Filter pattern syntax for

metric filters

###### Note

**How metric filters differ from CloudWatch Logs Insights queries**

Metric filters differ from CloudWatch Logs Insights queries in that a specified numerical
value is added to a metric filter each time a matching log is found. For more
information, see [Configuring metric values for a
metric filter](#changing-default-increment-value "#changing-default-increment-value").

For information about how to query your log groups with the Amazon CloudWatch Logs Insights
query language, see [CloudWatch Logs Insights language query syntax](CWL_QuerySyntax.md "CWL_QuerySyntax.md").

**Generic filter pattern examples**

For more information on generic filter pattern syntax applicable to metric filters
as well as [subscription
filters](SubscriptionFilters.md "SubscriptionFilters.md") and [filter log
events](SearchDataFilterPattern.md "SearchDataFilterPattern.md"), see [Filter pattern
syntax for metric filters, subscription filters, and filter log events](FilterAndPatternSyntax.md "FilterAndPatternSyntax.md"),
which includes the following examples:

- Supported regular expressions (regex) syntax
- Matching terms in unstructured log events
- Matching terms in JSON log events
- Matching terms in space-delimited log events
  _Metric filters_ allow you to search and filter log data coming
  into CloudWatch Logs, extract metric observations from the filtered log data, and transform the
  data points into a CloudWatch Logs metric. You define the terms and patterns to look for in log
  data as it is sent to CloudWatch Logs. Metric filters are assigned to log groups, and all of the
  filters assigned to a log group are applied to their log streams.

When a metric filter matches a term, it increments the metric's count by a specified
numerical value. For example, you can create a metric filter that counts the number of
times the word **_ERROR_** occurs in your log
events.

You can assign units of measure and dimensions to metrics. For example, if you create
a metric filter that counts the number of times the word
**_ERROR_** occurs in your log events, you
can specify a dimension that's called `ErrorCode` to show the total number of
log events that contain the word **_ERROR_** and
filter data by reported error codes.

###### Tip

When you assign a unit of measure to a metric, make sure to specify the correct
one. If you change the unit later, your change might not take effect. For the
complete list of the units that CloudWatch supports, see [MetricDatum](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md") in the Amazon CloudWatch API Reference.

###### Topics

- [Configuring metric values for a
  metric filter](#changing-default-increment-value "#changing-default-increment-value")
- [Publishing dimensions with metrics
  from values in JSON or space-delimited log events](#logs-metric-filters-dimensions "#logs-metric-filters-dimensions")
- [Using values in log events to
  increment a metric's value](#publishing-values-found-in-logs "#publishing-values-found-in-logs")

## Configuring metric values for a

metric filter

When you create a metric filter, you define your filter pattern and specify your
metric's value and default value. You can set metric values to numbers, named
identifiers, or numeric identifiers. If you don't specify a default value, CloudWatch
won't report data when your metric filter doesn't find a match. We recommend that
you specify a default value, even if the value is 0. Setting a default value helps
CloudWatch report data more accurately and prevents CloudWatch from aggregating spotty metrics.
CloudWatch aggregates and reports metric values every minute.

When your metric filter finds a match in your log events, it increments your
metric's count by your metric's value. If your metric filter doesn't find a match,
CloudWatch reports the metric's default value. For example, your log group publishes two
records every minute, the metric value is 1, and the default value is 0. If your
metric filter finds matches in both log records within the first minute, the metric
value for that minute is 2. If your metric filter doesn't find matches in either
records during the second minute, the default value for that minute is 0. If you
assign dimensions to metrics that metric filters generate, you can't specify default
values for those metrics.

You also can set up a metric filter to increment a metric with a value extracted
from a log event, instead of a static value. For more information, see [Using values in log events to
increment a metric's value](#publishing-values-found-in-logs "#publishing-values-found-in-logs").

## Publishing dimensions with metrics

from values in JSON or space-delimited log events

You can use the CloudWatch console or AWS CLI to create metric filters that publish
dimensions with metrics that JSON and space-delimited log events generate.
Dimensions are name/value value pairs and only available for JSON and space-delimited
filter patterns. You can create JSON and space-delimited metric filters with up to
three dimensions. For more information about dimensions and information about how to
assign dimensions to metrics, see the following sections:

- [Dimensions](../monitoring/cloudwatch_concepts.md#Dimension "../monitoring/cloudwatch_concepts.md#Dimension") in the _Amazon CloudWatch User
  guide_
- [Example: Extract fields from an Apache log and assign
  dimensions](ExtractBytesExample.md "ExtractBytesExample.md") in the _Amazon CloudWatch Logs User
  Guide_

###### Important

Dimensions contain values that gather charges the same as custom metrics. To
prevent unexpected charges, don't specify high-cardinality fields, such as
`IPAddress` or `requestID`, as dimensions.

If you extract metrics from log events, you're charged for custom metrics. To
prevent you from collecting accidental high charges, Amazon might disable your
metric filter if it generates 1000 different name/value pairs for specified
dimensions over a certain amount of time.

You can create billing alarms that notify you of your estimated charges. For
more information, see [Creating a billing alarm to monitor your estimated AWS
charges](../monitoring/monitor_estimated_charges_with_cloudwatch.md "../monitoring/monitor_estimated_charges_with_cloudwatch.md").

The following examples contain code snippets that describe how to specify
dimensions in a JSON metric filter.

Example: JSON log event

```
{
  "eventType": "UpdateTrail",
  "sourceIPAddress": "111.111.111.111",
  "arrayKey": [
        "value",
        "another value"
  ],
  "objectList": [
       {"name": "a",
         "id": 1
       },
       {"name": "b",
         "id": 2
       }
  ]

}
```

###### Note

If you test the example metric filter with the example
JSON log event, you must enter the example JSON log on a
single line.

Example: Metric filter
The metric filter increments the metric whenever a JSON log
event contain the properties `eventType` and
`"sourceIPAddress"`.

```

{ $.eventType = "*" && $.sourceIPAddress != 123.123.* }

```

When you create a JSON metric filter, you can specify any of
the properties in the metric filter as a dimension. For example,
to set `eventType` as a dimension, use the
following:

```

"eventType" : $.eventType

```

The example metric contains a dimension that's named
`"eventType"`, and the dimension's value in the
example log event is `"UpdateTrail"`.

The following examples contain code snippets that describe how to specify
dimensions in a space-delimited metric filter.

Example: Space-delimited log event

```


127.0.0.1 Prod frank [10/Oct/2000:13:25:15 -0700] "GET /index.html HTTP/1.0" 404 1534


```

Example: Metric filter

```


[ip, server, username, timestamp, request, status_code, bytes > 1000]


```

The metric filter increments the metric when a space-delimited
log event includes any of the fields that are specified in the
filter. For example, the metric filter finds following fields
and values in the example space-delimited log event.

```
{
   "$bytes": "1534",
   "$status_code": "404",

   "$request": "GET /index.html HTTP/1.0",
   "$timestamp": "10/Oct/2000:13:25:15 -0700",
   "$username": "frank",
   "$server": "Prod",
   "$ip": "127.0.0.1"
}
```

When you create a space-delimited metric filter, you can
specify any of the fields in the metric filter as a dimension.
For example, to set `server` as a dimension, use the
following:

```

"server" : $server
```

The example metric filter has a dimension that's named
`server`, and the dimension's value in the
example log event is `"Prod"`.

Example: Match terms with AND (&&) and OR
(||)
You can use the logical operators AND ("&&") and OR
("||") to create space-delimited metric filters that contain
conditions. The following metric filter returns log events where
the first word in the events is ERROR or any superstring of
WARN.

```

[w1=ERROR || w1=%WARN%, w2]

```

## Using values in log events to

increment a metric's value

You can create metric filters that publish numeric values found in your log
events. The procedure in this section uses the following example metric filter to
show how you can publish a numeric value in a JSON log event to a metric.

```
{ $.latency = * } metricValue: $.latency
```

###### To create a metric filter that publishes a value in a log event

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Log groups**.
3. Select or create a log group.

For information about how to create a log group, see [Create a log group in CloudWatch Logs](Working-with-log-groups-and-streams.md "Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch Logs User
Guide_. 4. Choose **Actions**, and then choose **Create
metric filter**. 5. For **Filter Pattern**, enter `{ $.latency = *
 }`, and then choose **Next**. 6. For **Metric Name**, enter
**myMetric**. 7. For **Metric Value**, enter
`$.latency`. 8. (Optional) For **Default Value**, enter
**0**, and then choose
**Next**.

We recommend that you specify a default value, even if the value is 0.
Setting a default value helps CloudWatch report data more accurately and prevents
CloudWatch from aggregating spotty metrics. CloudWatch aggregates and reports metric
values every minute. 9. Choose **Create metric filter**.

The example metric filter matches the term `"latency"` in the example
JSON log event and publishes a numeric value of 50 to the metric
**myMetric**.

```
{
"latency": 50,
"requestType": "GET"
}
```
