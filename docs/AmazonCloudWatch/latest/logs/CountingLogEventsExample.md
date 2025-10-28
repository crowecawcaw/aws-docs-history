# Example: Count log events

The simplest type of log event monitoring is to count the number of log events
that occur. You might want to do this to keep a count of all events, to create a
"heartbeat" style monitor or just to practice creating metric filters.

In the following CLI example, a metric filter called MyAppAccessCount is applied
to the log group MyApp/access.log to create the metric EventCount in the CloudWatch
namespace MyNamespace. The filter is configured to match any log event content and
to increment the metric by "1".

###### To create a metric filter using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log groups**.
3. Choose the name of a log group.
4. Choose `Actions`, **Create metric
   filter**.
5. Leave **Filter Pattern** and **Select Log Data to
   Test** blank.
6. Choose **Next**, and then for **Filter
   Name**, type `EventCount`.
7. Under **Metric Details**, for **Metric
   Namespace**, type `MyNameSpace`.
8. For **Metric Name**, type
   `MyAppEventCount`.
9. Confirm that **Metric Value** is 1. This specifies that
   the count is incremented by 1 for every log event.
10. For **Default Value** enter 0, and then choose
    **Next**. Specifying a default value ensures that data
    is reported even during periods when no log events occur, preventing spotty
    metrics where data sometimes does not exist.
11. Choose **Create metric filter**.

###### To create a metric filter using the AWS CLI

At a command prompt, run the following command:

```
`aws logs put-metric-filter \
 --log-group-name MyApp/access.log \
 --filter-name EventCount \
 --filter-pattern " " \
 --metric-transformations \
 metricName=MyAppEventCount,metricNamespace=MyNamespace,metricValue=1,defaultValue=0`
```

You can test this new policy by posting any event data. You should see data points
published to the metric MyAppAccessEventCount.

###### To post event data using the AWS CLI

At a command prompt, run the following command:

```
`aws logs put-log-events \
 --log-group-name MyApp/access.log --log-stream-name TestStream1 \
 --log-events \
 timestamp=1394793518000,message="Test event 1" \
 timestamp=1394793518000,message="Test event 2" \
 timestamp=1394793528000,message="This message also contains an Error"`
```
