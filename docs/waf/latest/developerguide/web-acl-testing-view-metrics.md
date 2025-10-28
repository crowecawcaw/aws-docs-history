**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Viewing metrics for your web

ACL

This section describes how to view metrics for your protection pack (web ACL).

After you've associated a protection pack (web ACL) with one or more AWS resources, you can view
the resulting metrics for the association in an Amazon CloudWatch graph.

For information about AWS WAF metrics, see [AWS WAF metrics and dimensions](waf-metrics.md "waf-metrics.md"). For information about CloudWatch metrics, see the [Amazon CloudWatch User
Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

For each of your rules in a protection pack (web ACL) and for all the requests that an associated resource
forwards to AWS WAF for a protection pack (web ACL), CloudWatch lets you do the following:

- View data for the preceding hour or preceding three hours.
- Change the interval between data points.
- Change the calculation that CloudWatch performs on the data, such as maximum,
  minimum, average, or sum.

###### Note

AWS WAF with CloudFront is a global service and metrics are available only when you
choose the **US East (N. Virginia)** Region in the AWS Management Console.
If you choose another Region, no AWS WAF metrics will appear in the CloudWatch
console.

###### To view data for the rules in a protection pack (web ACL)

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, change the Region to the one where your AWS resources are
   located. For CloudFront, choose the US East (N. Virginia) Region.
3. In the navigation pane, under **Metrics**, choose
   **All metrics** and then search under the
   **Browse** tab for `AWS::WAFV2`.
4. Select the check box for the protection pack (web ACL) that you want to view data
   for.
5. Change the applicable settings:

**Statistic**

Choose the calculation that CloudWatch performs on the data.

**Time range**

Choose whether you want to view data for the preceding hour or
the preceding three hours.

**Period**

Choose the interval between data points in the graph.

**Rules**

Choose the rules for which you want to view data.

###### Note

If you change the name of a rule and you want the rule's metric name to reflect the change, you
must update the metric name as well. AWS WAF doesn't automatically update the metric name for a rule when you change the rule name.
You can change the metric name when you edit the
rule in the console, by using the rule JSON editor. You can also change both names through the APIs and in any JSON listing that you
use to define your protection pack (web ACL) or rule group.

Note the following:

    * If you recently associated a protection pack (web ACL) with an AWS resource, you
     might need to wait a few minutes for data to appear in the graph and
     for the metric for the protection pack (web ACL) to appear in the list of available
     metrics.
    * If you associate more than one resource with a protection pack (web ACL), the CloudWatch
     data will include requests for all of them.
    * You can hover the cursor over a data point to get more
     information.
    * The graph doesn't refresh itself automatically. To update the
     display, choose the refresh (
    ![Icon to refresh the CloudWatch graph](images/cloudwatch-refresh-icon.png)
    ) icon.

For more information about CloudWatch metrics, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
