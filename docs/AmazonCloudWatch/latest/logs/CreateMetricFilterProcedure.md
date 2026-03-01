# Create a metric filter for a log group

To create a metric filter for a log group, follow these steps. The metric won't be
visible until there are some data points for it.

###### To create a metric filter using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Log groups**.
3. Choose the name of the log group.
4. Choose `Actions`, and then choose **Create metric
   filter**.
5. For **Filter pattern**, enter a filter pattern. For more
   information, see [Filter pattern syntax for metric filters, subscription filters, filter log events, and Live Tail](FilterAndPatternSyntax.md "FilterAndPatternSyntax.md").
6. (Optional) If you are using centralized log groups, under
   **Filter selection criteria**, you can specify filters
   based on source account (`@aws.account`), source region
   (`@aws.region`), or both conditions.
7. (Optional) To test your filter pattern, under **Test
   Pattern**, enter one or more log events to test the pattern.
   Each log event must be formatted on one line. Line breaks are used to
   separate log events in the **Log event messages** box.
8. Choose **Next**, and then enter a name for your metric
   filter.
9. Under **Metric details**, for **Metric
   namespace**, enter a name for the CloudWatch namespace where the
   metric will be published. If the namespace doesn't already exist, make sure
   that **Create new** is selected.
10. For **Metric name**, enter a name for the new metric.
11. For **Metric value**, if your metric filter is counting
    occurrences of the keywords in the filter, enter 1. This increments the
    metric by 1 for each log event that includes one of the keywords.

Alternatively, enter a token, such as `$size`. This
increments the metric by the value of the number in the `size`
field for every log event that contains a `size` field. 12. (Optional) For **Unit**, select a unit to assign to the
metric. If you do not specify a unit, the unit is set as `None`. 13. (Optional) Enter the names and tokens for as many as three dimensions for
the metric. If you assign dimensions to metrics that metric filters create,
you cannot assign default values for those metrics.

###### Note

Dimensions are supported only in JSON or space-delimited metric
filters. 14. Choose **Create metric filter**. You can find the metric
filter that you created from the navigation pane. Choose
**Logs**, and then choose **Log
groups**. Choose the name of the log group that you created
your metric filter for, and then select the **Metric
filters** tab.
