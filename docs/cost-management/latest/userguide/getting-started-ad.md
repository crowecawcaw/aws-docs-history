# Getting started with AWS Cost Anomaly Detection

With AWS Cost Anomaly Detection in AWS Billing and Cost Management, you can configure your cost monitors and alert
subscriptions in several different ways.

###### Topics

- [Creating your cost monitors and alert
  subscriptions](#create-ad-alerts "#create-ad-alerts")
- [Detected anomalies overview](#detector-history-values "#detector-history-values")
- [Viewing your detected anomalies and potential root
  causes](#view-ad-monitor "#view-ad-monitor")
- [Monitor types](#monitor-type-def "#monitor-type-def")

## Creating your cost monitors and alert

subscriptions

Configure AWS Cost Anomaly Detection so that it detects anomalies at a lower granularity and spend
patterns, in context to your monitor type.

For example, your spend patterns for Amazon EC2 usage might be different from your
AWS Lambda or Amazon S3 spend patterns. By segmenting spends by AWS services, AWS Cost Anomaly Detection
can detect separate spend patterns that help decrease false positive alerts. You can
also create cost monitors. They can evaluate specific cost allocation tags, member
accounts within an organization (AWS Organizations), and cost categories based on your
AWS account structure.

As you create your cost monitors, configure your alert subscriptions specific to
each monitor.

You can also create individual alerts by setting up AWS User
Notifications.

###### Note

You can only access cost monitors and alert subscriptions under the account
that created them. For example, suppose that the cost monitor was created under
a member account. Then, the management account can't view or edit the cost
monitors, alert subscriptions, or detected anomalies.

Cost monitors

###### To create a cost monitor

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose
   **Cost Anomaly Detection**.
3. Choose the **Cost monitors** tab.
4. Choose **Create monitor**.
5. In **Step 1**, choose a monitor type and name
   your monitor.

For more information about each monitor type and best
practices, see [Monitor types](#monitor-type-def "#monitor-type-def").

For **Monitor name**, enter a name for your
anomaly monitor. We recommend that the name is a short
description. That way, you know what the monitor represents when
you view your monitors on the **Cost monitors**
tab. 6. (Optional) Add a tag to your monitor. For more information
about tags, see [Tagging AWS
resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference
guide_.

    1. Enter the key value for the tag.
    2. Choose **Add new tag** to add
     additional tags. The maximum number of tags that you can
     add is 50.

7. Choose **Next**.
8. In **Step 2**, configure your alert
   subscriptions.

For **Alert subscription**, if you don't have
an existing subscription, choose **Create a new
subscription**. If you have existing subscriptions,
select **Choose an existing
subscription**.

###### Note

An alert subscription notifies you when a cost monitor
detects an anomaly. Depending on the alert frequency, you
can notify designated individuals by email or Amazon SNS.

For Amazon SNS topics, configure to create an
Amazon Q Developer in chat applications configuration. This configuration maps the SNS topic
to a Slack channel or an Amazon Chime chat room. For example,
create a subscription for the Finance team in your
organization. For more information, see [Receiving anomaly alerts in chat applications](cad-alert-chime.md "cad-alert-chime.md").

For **Subscription name**, enter a name that
describes your use case. For example, if the subscription is
meant for leadership, the subscription name might be “Leadership
report.”

Under **Alerting frequency**, choose your
preferred notification frequency.

    * **Individual alerts** - The alert
     notifies you as soon as an anomaly is detected. You
     might receive multiple alerts throughout a day. These
     notifications require an Amazon SNS topic.


    You can configure the Amazon SNS topic to
     create an Amazon Q Developer in chat applications configuration that maps the SNS topic to
     a Slack channel or an Amazon Chime chat room. For more
     information, see [Receiving anomaly alerts in chat applications](cad-alert-chime.md "cad-alert-chime.md").
    * **Daily summaries** - An email
     notification with a daily summary of top 10 alerts from
     the previous day, sorted by cost impact. The system
     generates this summary at 00:00 UTC daily, though actual
     delivery time may vary. For example, an anomaly detected
     at 04:30 UTC on January 14 will be included in the daily
     summary sent at 00:00 UTC on January 15. At least one
     email recipient must be specified. For immediate alerts,
     we recommend using the individual alerts option.
    * **Weekly summaries** - An email
     notification with a weekly summary of alerts. You
     receive one email per week containing information about
     multiple anomalies that occurred during that week. At
     least one email recipient must be specified.

Under **Alert recipients**, enter email
addresses for this subscription.

For **Threshold**, enter a number to
configure the anomalies that you want to generate alerts
for.

There are two types of thresholds: absolute and percentage.
Absolute thresholds trigger alerts when an anomaly's total cost
impact exceeds your chosen threshold. Percentage thresholds
trigger alerts when an anomaly's total impact percentage exceeds
your chosen threshold. Total impact percentage is the percentage
difference between the total expected spend and total actual
spend.

(Optional) Choose **Add threshold** to
configure a second threshold on the same subscription.
Thresholds can be combined by choosing **AND**
or **OR** from the dropdown list.

###### Note

AWS Cost Anomaly Detection sends you a notification when an anomaly reaches
or exceeds the **Threshold**. If an anomaly
continues over multiple days, then alert recipients will
continue to get notifications while the threshold is
met.

Even if an anomaly is below the alert threshold, the
machine learning model continues to detect spend anomalies
on your account. All the anomalies that the machine learning
model detected (with cost impacts that are greater or less
than the threshold) are available in the **Detected
anomalies** tab. 9. (Optional) Add a tag to your alert subscription. For more
information about tags, see [Tagging AWS
resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference
guide_.

    1. Enter the key value for the tag.
    2. Choose **Add new tag** to add
     additional tags. The maximum number of tags that you can
     add is 50.

10. (Optional) Choose **Add alert subscriptions**
    to create another alert subscription. With this option, you can
    create a new subscription using the same monitor.
11. Choose **Create monitor**.

Alert subscriptions

###### To create an alert

subscription

You must create at least one alert subscription for each monitor.
The "create cost monitor steps" that are described earlier already
include the alert subscription creation process. If you want to
create additional subscriptions, follow these steps.

1. Choose the **Alert subscriptions**
   tab.
2. Choose **Create a subscription**.
3. For **Subscription name**, enter a name that
   describes your use case. For example, if the subscription is
   meant for leadership, then the subscription name might be
   “Leadership report.”
4. Under **Alerting frequency**, choose your
   preferred notification frequency.
   - **Individual alerts** - The alert
     notifies you as soon as an anomaly is detected. You
     might receive multiple alerts throughout a day. These
     notifications require an Amazon SNS topic.

   You can configure the Amazon SNS topic to
   create an Amazon Q Developer in chat applications configuration that maps the SNS topic to
   a Slack channel or an Amazon Chime chat room. For more
   information, see [Receiving anomaly alerts in chat applications](cad-alert-chime.md "cad-alert-chime.md").
   - **Daily summaries** - An email
     notification with a daily summary of top 10 alerts from
     the previous day, sorted by cost impact. The system
     generates this summary at 00:00 UTC daily, though actual
     delivery time may vary. For example, an anomaly detected
     at 04:30 UTC on January 14 will be included in the daily
     summary sent at 00:00 UTC on January 15. At least one
     email recipient must be specified. For immediate alerts,
     we recommend using the individual alerts option.
   - **Weekly summaries** - An email
     notification with a weekly summary of alerts. You
     receive one email per week containing information about
     multiple anomalies that occurred during that week. At
     least one email recipient must be specified.

5. Under **Alert recipients**, enter email
   addresses for this subscription.
6. For **Threshold**, enter a number to
   configure the anomalies that you want to generate alerts
   for.

There are two types of thresholds: absolute and percentage.
Absolute thresholds trigger alerts when an anomaly's total cost
impact exceeds your chosen threshold. Percentage thresholds
trigger alerts when an anomaly's total impact percentage exceeds
your chosen threshold. Total impact percentage is the percentage
difference between the total expected spend and total actual
spend.

(Optional) Choose **Add threshold** to
configure a second threshold on the same subscription.
Thresholds can be combined by choosing **AND**
or **OR** from the dropdown list.

###### Note

AWS Cost Anomaly Detection sends you a notification when an anomaly reaches
or exceeds the **Threshold**. If an anomaly
continues over multiple days, then alert recipients will
continue to get notifications while the threshold is
met.

Even if an anomaly is below the alert threshold, the
machine learning model continues to detect spend anomalies
on your account. All the anomalies that the machine learning
model detected (with cost impacts that are greater or less
than the threshold) are available in the **Detected
anomalies** tab. 7. In the **Cost monitors** section, select the
monitors that you want to be associated with the alert
subscription. 8. (Optional) Add a tag to your alert subscription. For more
information about tags, see [Tagging AWS
resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference
guide_.

    1. Enter the key value for the tag.
    2. Choose **Add new tag** to add
     additional tags. The maximum number of tags that you can
     add is 50.

9. Choose **Create subscription**.

AWS User Notifications
For information about how to create individual alerts, see [Using AWS User Notifications with Cost
Anomaly Detection](cad-user-notifications.md "cad-user-notifications.md").

## Detected anomalies overview

On the **Detected anomalies** tab, you can view a list of all the
anomalies detected over a selected time frame. By default, you can see the anomalies
that are detected in the last 90 days. You can search the anomalies by
**Severity**, **Assessment**,
**Services**, **Usage type**,
**Region**, **Monitor type**,
**Account**, or **Anomaly ID**. You can sort
by **Start date**, **Last detected**,
**Duration**, **Cost impact**,
**Impact %**, **Monitor name**, and
**Top root cause (Service)**.

The following default columns are included on the **Detected
anomalies** tab:

**Start date**

The day that the anomaly started.

**Last detected**

The last time that the anomaly was detected.

**Duration**

The duration that the anomaly lasted. An anomaly can be
ongoing.

**Cost impact**

The spend increase detected compared to the expected spend amount. It
is calculated as **actual spend - expected spend**. For
example, a total cost impact of $20 on a service monitor means that
there was a $20 increase detected in a particular service with a total
duration of the specified days.

**Impact %**

The percentage difference between the actual spend and expected spend.
It is calculated as **(total cost impact / expected spend) \*
100**. For example, if the total cost impact was $20 and the
expected spend was $60, then the impact percentage would be 33.33%. This
value cannot be calculated when expected spend is zero, so in those
situations the value will show as “N/A”.

**Monitor name**

The name of the anomaly monitor.

**Top root cause (Service)**

The top service root cause for the anomaly. Choosing the service name
in the Top root cause column displays the three other root cause
dimensions—account, Region, and usage type—for the anomaly’s top root
cause.

**View more**

A link to the Anomaly details page with information on the root cause
analysis and cost impact of the anomaly. The link also indicates the
number of root causes detected for an anomaly.

The **Detected anomalies** tab can also be configured to display
additional columns of information. Any changes you make will be saved at the account
level for all subsequent visits to the **Detected anomalies** tab.
The following **optional columns** are included on the
**Detected anomalies** tab.

**Account**

The account ID and account name that caused the anomaly. If the
account is empty, AWS has detected an anomaly, but the root cause is
undetermined.

**Region**

The Region detected as the top root cause for the anomaly.

**Usage type**

The usage type detected as the top root cause for the anomaly.

**Expected spend**

The amount our machine learning models expected you to spend during
the anomaly’s duration, based on your historical spending
pattern.

**Actual spend**

The total amount you actually spent during the anomaly’s
duration.

**Assessment**

For each detected anomaly, you can submit an assessment to help
improve our anomaly detection systems. The possible values are
**Not submitted**, **Not an
issue**, or **Accurate anomaly**.

**Severity**

Represents how abnormal a certain anomaly is accounting for historical
spending patterns. A low severity generally suggests a small spike
compared to historical spend and a high severity suggests a big spike.
However, a small spike with historically consistent spend is categorized
as high severity. And, similarly, a big spike with irregular historical
spend is categorized as low severity.

## Viewing your detected anomalies and potential root

causes

After you create your monitors, AWS Cost Anomaly Detection evaluates your future spend. Based on
your defined alert subscriptions, you might start receiving alerts within 24
hours.

###### To view your anomalies from an email

alert

1. Choose the provided **View in Anomaly Detection**
   link.
2. On the **Anomaly details** page, you can view the root
   cause analysis and cost impact of the anomaly.
3. (Optional) Choose **View in Cost Explorer** to view a
   time series graph of the cost impact.
4. (Optional) Choose **View root cause** in the
   **Top ranked potential root causes** table for a root
   cause of interest to see a time series graph that's filtered by that root
   cause.
5. (Optional) Choose **Submit assessment** in the
   **Did you find this detected anomaly to be helpful?**
   information alert to provide feedback and help improve our detection
   accuracy.

###### To view your anomalies from the AWS Billing and Cost Management

console

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Anomaly Detection**.
3. (Optional) On the **Detected anomalies** tab, use the
   search area to narrow the list of detected anomalies for a particular
   category. The categories that you can choose are Severity, Assessment,
   Service, Account, Usage type, Region, and Monitor type.
4. (Optional) Choose the **Start date** for a particular
   anomaly to view the details.
5. On the **Anomaly details** page, you can view the root
   cause analysis and cost impact of the anomaly.
6. (Optional) Choose **View in Cost Explorer** to view a
   time series graph of the cost impact and, if necessary, dive deeper into the
   data.
7. (Optional) Choose **View root cause** in the
   **Top ranked potential root causes** table to see a
   time series graph that's filtered by the root cause.
8. (Optional) Choose **Submit assessment** in the
   **Did you find this detected anomaly to be helpful?**
   information alert to provide feedback and help improve our detection
   accuracy.

###### To view your anomalies from an Amazon SNS

topic

1. Subscribe an endpoint to the Amazon SNS topic that you created for a cost
   monitor with individual alerts. For instructions, see [Subscribing to an Amazon SNS topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md") in the
   _Amazon Simple Notification Service Developer Guide_.
2. After your endpoint receives messages from the Amazon SNS topic, open a message
   and then find the **anomalyDetailsLink** URL. The following
   example is a message from AWS Cost Anomaly Detection through Amazon SNS.

```
{
    "accountId": "123456789012",
    "anomalyDetailsLink": "https://console.aws.amazon.com/cost-management/home#/anomaly-detection/monitors/abcdef12-1234-4ea0-84cc-918a97d736ef/anomalies/12345678-abcd-ef12-3456-987654321a12",
    "anomalyEndDate": "2021-05-25T00:00:00Z",
    "anomalyId": "12345678-abcd-ef12-3456-987654321a12",
    "anomalyScore": {
        "currentScore": 0.47,
        "maxScore": 0.47
    },
    "anomalyStartDate": "2021-05-25T00:00:00Z",
    "dimensionalValue": "ServiceName",
    "impact": {
        "maxImpact": 151,
        "totalActualSpend": 1301,
        "totalExpectedSpend": 300,
        "totalImpact": 1001,
        "totalImpactPercentage": 333.67
    },
    "monitorArn": "arn:aws:ce::123456789012:anomalymonitor/abcdef12-1234-4ea0-84cc-918a97d736ef",
    "rootCauses": [
        {
            "linkedAccount": "AnomalousLinkedAccount",
            "linkedAccountName": "AnomalousLinkedAccountName",
            "region": "AnomalousRegionName",
            "service": "AnomalousServiceName",
            "usageType": "AnomalousUsageType",
            "impact": {
                "contribution": 601,
            }
        }
    ],
    "subscriptionId": "874c100c-59a6-4abb-a10a-4682cc3f2d69",
    "subscriptionName": "alertSubscription"
}
```

3. Open the **anomalyDetailsLink** URL in a web browser. The
   URL takes you to the associated **Anomaly details** page.
   This page shows the root cause analysis and cost impact of the
   anomaly.

## Monitor types

You can choose the monitor type that fits your account structure. Currently, we
offer the following monitor types:

- **AWS services** - We recommend this monitor if you
  don't need to segment your spend by internal organizations or environments.
  This single monitor evaluates all the AWS services that are used by your
  individual AWS account for anomalies. When you add new AWS services, the
  monitor automatically begins to evaluate the new service for anomalies. That
  way, you don't have to manually configure your settings.

###### Note

Management accounts can have one AWS services monitor and up to 500
custom monitors (linked account, cost allocation tag, and cost category)
for a total of 501 anomaly monitors. Member accounts only have access to
the AWS services monitor.

- **Linked account** - This monitor evaluates the total
  spend of an individual, or group of, member accounts. If your Organizations need to
  segment spend by team, product, services, or environment, this monitor is
  useful. The maximum number of member accounts that you can select for each
  monitor is 10.
- **Cost category** - This monitor is recommended if you
  use cost categories to organize and manage your spend. This monitor type is
  restricted to one `key:value` pair.
- **Cost allocation tag** - This monitor is similar to
  **Linked account**. If you to need to segment your
  spend by team, product, services, or environment, this monitor is useful.
  This monitor type is restricted to one key, but accepts multiple values. The
  maximum number of values that you can select for each monitor is 10.

We recommend that you do not create monitors that span multiple monitor types.
This might lead to evaluating overlapping spends that generate duplicate
alerts.

For more information about creating your Amazon SNS topic, see [Creating an Amazon SNS topic for anomaly notifications](ad-SNS.md "ad-SNS.md").
