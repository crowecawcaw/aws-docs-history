

# Monitoring health checks using CloudWatch
<a name="monitoring-health-checks"></a>

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
<a name="health-checks-monitoring-status"></a>

**Note**  
We're updating the health checks console for Route 53. During the transition period, you can continue to use the old console.

Choose the tab for the console you are using.
+ [New console](#health-checks-monitoring-status-new)
+ [Old console](#health-checks-monitoring-status-old)

------
#### [ New console ]<a name="health-checks-monitoring-status-proc"></a>

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
   + The graph doesn't refresh itself automatically. To update the display, choose the refresh (![Icon to refresh the CloudWatch graph](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/cloudwatch-refresh-icon.png)) icon.

------
#### [ Old console ]<a name="monitoring-status-procedure"></a>

**To view the status of a health check (new console)**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Health Checks**. 

1. Choose the rows for the applicable health checks. 

1. In the bottom pane, choose the **Monitoring** tab.

   The two graphs display the status for the last hour in one-minute intervals:  
**Health check status**  
The graph shows the Route 53 assessment of endpoint health. **1** indicates healthy and **0** indicates unhealthy.  
**Health checkers that report the endpoint healthy (%)**  
For health checks that monitor an endpoint only, the graph shows the percentage of Route 53 health checkers that consider the selected endpoint to be healthy.  
When a health check is disabled, this metric isn't available.  
**Number of healthy child health checks**  
For calculated health checks only, the graph shows the number of child health checks that are healthy. 
**Note**  
If you selected more than one health check, the graph displays a separate color-coded line for each health check.

1. To view a larger graph and specify different settings, choose the graph. You can change the following settings:  
**Statistic**  
Changes the calculation that CloudWatch performs on the data.  
**Time range**  
Displays the status of a health check over a different period, for example, overnight or last week.  
**Period**  
Changes the interval between data points in the graph.

   Note the following:
   + If you just created a health check, you might need to wait for a few minutes for data to appear in the graph and for the health check metric to appear in the list of available metrics.
   + The graph doesn't refresh itself automatically. To update the display, choose the refresh (![Icon to refresh the CloudWatch graph](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/cloudwatch-refresh-icon.png)) icon.

------

## View health check alarms
<a name="health-checks-monitoring-alarms"></a>

**Note**  
We're updating the health checks console for Route 53. During the transition period, you can continue to use the old console.

Choose the tab for the console you are using.
+ [New console](#health-checks-monitoring-alarms-new)
+ [Old console](#health-checks-monitoring-alarms-old)

------
#### [ New console ]<a name="health-checks-monitoring-alarms-proc"></a>

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

------
#### [ Old console ]<a name="monitoring-alarm-status-procedure"></a>

**To view CloudWatch alarm status and edit alarms for Amazon Route 53**

1. In the navigation pane of the Route 53 console, choose **Health Checks**.

1. Choose the row for any health check.

1. In the details pane (following *x* **Health Checks Selected**), choose the right caret (![Icon to expand the list of CloudWatch alarms](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/cloudwatch-expand-alarms-list.png)) icon.

   The **CloudWatch Alarms** list contains all the Route 53 alarms that you have created using the current AWS account.

   The **State** column shows the current status of each alarm:  
**OK**  
CloudWatch has accumulated enough statistics from Route 53 health checks to determine that the endpoint doesn't meet the alarm threshold.  
**INSUFFICIENT DATA**  
CloudWatch hasn't accumulated enough statistics to determine whether the endpoint meets the alarm threshold. This is the initial state of a new alarm. The alarm state also changes to **INSUFFICIENT DATA** if CloudWatch metrics become unavailable or if you delete the health check without deleting the associated alarm.   
**ALARM**  
CloudWatch has accumulated enough statistics from Route 53 health checks to determine that the endpoint meets the alarm threshold and to send notification to the specified email address.

1. To view or edit settings for an alarm, choose the name of the alarm.

1. To view an alarm in the CloudWatch console, which provides more detailed information about the alarm (for example, a history of updates to the alarm and changes in status), choose **View** in the **More Options** column for the alarm.

1. To view all the CloudWatch alarms that you created using the current AWS account, including alarms for other AWS services, choose **View All CloudWatch Alarms**.

1. To view all the available CloudWatch metrics, including metrics that aren't currently being used by the current AWS account, choose **View All CloudWatch Metrics**.

------

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

**Note**  
The following procedure applies to the old console only. The new console directs you to the CloudWatch console to create alarms. For more information, see [Find and create recommended alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html#Best-Practice-Alarms-create) in the *CloudWatch User guide*.<a name="monitoring-sns-notification-procedure"></a>

**To receive an Amazon SNS notification when a health check status is unhealthy (old console)**

1. In the navigation pane of the Route 53 console, choose **Health Checks**.

1. Choose the row for the applicable health check.

1. In the bottom pane, choose the **Alarms** tab.

   The table lists the alarms that you've already created for this health check.

1. Choose **Create Alarm**.

1. Specify the following values:  
**Alarm name**  
Enter the name that you want Route 53 to display in the **Name** column on the **Alarms** tab.  
**Alarm description**  
(Optional) Enter a description for the alarm. This value appears in the CloudWatch console.  
**Send notification**  
Choose whether you want Route 53 to send you notification if the status of this health check triggers an alarm.  
**Notification target (Only when "Send notification" is "Yes")**  
If you want CloudWatch to send notification to an existing SNS topic, choose the topic from the list.  
If you want CloudWatch to send notification but not to an existing SNS topic, do one of the following:  
   + **If you want CloudWatch to send email notification** – Choose **New SNS topic** and continue with this procedure.
   + **If you want CloudWatch to send notification by another method** – Open a new browser tab, go to the Amazon SNS console, and create the new topic. Then return to the Route 53 console, choose the name of the new topic from the **Notification target** list, and continue with this procedure.  
**Topic name (Only when you choose to create a new Amazon SNS topic)**  
Enter a name for the new Amazon SNS topic.  
**Recipient email addresses (Only when you choose to create a new Amazon SNS topic)**  
Enter the email address that you want Route 53 to send an SNS notification to when a health check triggers an alarm.  
**Alarm target**  
Choose the value that you want Route 53 to evaluate for this health check:  
   + **Health check status** – Route 53 health checkers report that the health check is healthy or unhealthy
   + **Health checkers that report the endpoint healthy (%)** (health checks that monitor an endpoint only) – The percentage of Route 53 health checkers that report that the status of the health check is healthy
   + **Number of healthy child health checks** (calculated health checks only) – The number of child health checks in a calculated health check that report that the status of the health check is healthy
   + **TCP connection time** (HTTP and TCP health checks only) – The time in milliseconds that it took Route 53 health checkers to establish a TCP connection with the endpoint
   + **Time to complete SSL handshake** (HTTPS health checks only) – The time in milliseconds that it took Route 53 health checkers to complete the SSL/TLS handshake
   + **Time to first byte** (HTTP and HTTPS health checks only) – The time in milliseconds that it took Route 53 health checkers to receive the first byte of the response to an HTTP or HTTPS request  
**Alarm target**  
For the alarm targets that are based on latency (**TCP connection time**, **Time to complete SSL handshake**, **Time to first byte**), choose whether you want CloudWatch to calculate latency for Route 53 health checkers in a specific region or for all regions (**Global**).  
Note that if you choose a Region, Route 53 measures latency only twice per minute, and the number of samples will be smaller than if you choose all regions. As a result, outlying values are more likely. To prevent spurious alarm notifications, we recommend that you specify a larger number of consecutive periods that the health check must fail before CloudWatch sends you a notification.   
**Fulfill condition**  
Use the following settings to determine when CloudWatch should trigger an alarm.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-checks.html)  
**For at least {{x}} consecutive periods of {{y}} minutes/hours/day**  
Specify how many consecutive time periods that the specified value must meet the criteria before Route 53 sends notification. Then specify the length of the time period.

1. When you choose **Create**, Amazon SNS sends you an email with information about the new SNS topic.

1. In the email, choose **Confirm subscription**. You must confirm your subscription to begin receiving CloudWatch notifications. 