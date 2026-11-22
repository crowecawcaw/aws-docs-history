

# Monitoring health checks using CloudWatch

Route 53 health checks integrate with CloudWatch metrics so that you can do the following:
+ Verify that a health check is properly configured.
+ Review the status of a health check over a specified period of time.
+ Configure CloudWatch to send an Amazon SNS alert when the status of a health check is unhealthy. Note that several minutes might elapse between the time that a health check fails and the time that you receive the associated SNS notification. 

For more information, see [How Amazon Route 53 determines whether a health check is healthy](dns-failover-determining-health-of-endpoints.md).

**Topics**
+ [View the status of your health check](#health-checks-monitoring-status)
+ [View health check alarms](#health-checks-monitoring-alarms)
+ [View health check metrics on the CloudWatch console](#view-health-checks-metrics-cw)
+ [Create an alarm with an SNS notification](#health-checks-create-alarm-notification)

## View the status of your health check
<a name="health-checks-monitoring-status"></a><a name="health-checks-monitoring-status-proc"></a>

**To view the status of a health check**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Health checks**. 

1. Choose the linked ID of the health check for which you want to view metrics. 

1. In the bottom pane, choose the **Metrics** tab.

   The two graphs display the status for the last hour in one-minute intervals:  
**Health check status**  
The graph shows the Route 53 assessment of endpoint health. **1** indicates healthy and **0** indicates unhealthy.  
**Health checkers that report the endpoint healthy (%)**  
For health checks that monitor an endpoint only, the graph shows the percentage of Route 53 health checkers that consider the selected endpoint to be healthy.  
When a health check is disabled, this metric isn't available.  
**Number of healthy child health checks**  
For calculated health checks only, the graph shows the number of child health checks that are healthy. 

1. To view a larger graph and specify different settings, choose the three dots on the upper right, and then **Enlarge**. You can change the following settings:  
**Statistic**  
Changes the calculation that CloudWatch performs on the data.  
**Time range**  
Displays the status of a health check over a different period, for example, overnight or last week.  
**Period**  
Changes the interval between data points in the graph.

   Note the following:
   + If you just created a health check, you might need to wait for a few minutes for data to appear in the graph and for the health check metric to appear in the list of available metrics.
   + The graph doesn't refresh itself automatically. To update the display, choose the refresh (![Icon to refresh the CloudWatch graph](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/cloudwatch-refresh-icon.png)) icon.

## View health check alarms
<a name="health-checks-monitoring-alarms"></a><a name="health-checks-monitoring-alarms-proc"></a>

**To view CloudWatch alarm status and edit alarms for Amazon Route 53**

1. In the navigation pane of the Route 53 console, choose **Health checks**.

1. Choose the linked ID of the health check for which you want to view the alarms.

1. In the details page, on the bottom of the page, choose the **Alarms** tab.

   The **Alarms** list contains all the Route 53 alarms that you have created for the selected health check.

   The **State** column shows the current status of each alarm:  
**OK**  
CloudWatch has accumulated enough statistics from Route 53 health checks to determine that the endpoint doesn't meet the alarm threshold.  
**INSUFFICIENT DATA**  
CloudWatch hasn't accumulated enough statistics to determine whether the endpoint meets the alarm threshold. This is the initial state of a new alarm. The alarm state also changes to **INSUFFICIENT DATA** if CloudWatch metrics become unavailable or if you delete the health check without deleting the associated alarm.   
**ALARM**  
CloudWatch has accumulated enough statistics from Route 53 health checks to determine that the endpoint meets the alarm threshold and to send notification to the specified email address.

1. To view an alarm in the CloudWatch console, which provides more detailed information about the alarm (for example, a history of updates to the alarm and changes in status), choose the linked name of the alarm. You can also edit the alarm on the CloudWatch console.

1. To create a new CloudWatch alarm on the CloudWatch console, choose **Create a CloudWatch alarm**. For more information, see [Find and create recommended alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html#Best-Practice-Alarms-create) in the *CloudWatch User guide*.

## View health check metrics on the CloudWatch console
<a name="view-health-checks-metrics-cw"></a><a name="monitoring-metrics-in-cloudwatch-console-procedure"></a>

**To view Route 53 metrics on the CloudWatch console**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Change the current region to **US East (N. Virginia)**. Route 53 metrics are not available if you select any other region as the current region.

1. In the navigation pane, choose **Metrics**.

1. On the **All metrics** tab, choose **Route 53**.

1. Choose **Health Check Metrics**.

1. You can also set up SNS notification on the CloudWatch console. For more information, see [Create recommended alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html#Best-Practice-Alarms-create) in the *CloudWatch User Guide*.

## Create an alarm with an SNS notification
<a name="health-checks-create-alarm-notification"></a>

To create an alarm that sends an Amazon SNS notification when a health check is unhealthy, use the CloudWatch console. For more information, see [Find and create recommended alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html#Best-Practice-Alarms-create) in the *CloudWatch User Guide*.