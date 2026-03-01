# Best practice alarm recommendations for AWS services

CloudWatch provides out-of-the box alarm recommendations. These are CloudWatch alarms that we
recommend that you create for metrics that are published by other AWS services. These
recommendations can help you identify the metrics that you should set alarms for to follow
best practices for monitoring. The recommendations also suggest the alarm thresholds to set.
Following these recommendations can help you not miss important monitoring of your AWS
infrastructure.

To find the alarm recommendations, you use the metrics section of the CloudWatch console, and
select the alarm recommendations filter toggle. If you navigate to the recommended alarms in
the console and then create a recommended alarm, CloudWatch can pre-fill some of the alarm settings.
For some recommended alarms, the alarm threshold value is also pre-filled. You can also use
the console to download infrastructure-as-code alarm definitions for recommended alarms, and
then use this code to create the alarm in AWS CloudFormation, the AWS CLI, or Terraform.

You can also see the list of recommended alarms in [Recommended alarms](Best_Practice_Recommended_Alarms_AWS_Services.md "Best_Practice_Recommended_Alarms_AWS_Services.md").

You are charged for the alarms that you create, at the same rate as any other alarms that
you create in CloudWatch. Using the recommendations incurs no extra charges. For more information,
see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Find and create recommended alarms

Follow these steps to find the metrics that CloudWatch recommends that you set alarms for, and
optionally to create one of these alarms. The first procedure explains how to find the
metrics that have recommended alarms, and how to create one of these alarms.

You can also get a bulk download of infrastructure-as-code alarm definitions for all
recommended alarms in an AWS namespace, such as `AWS/Lambda` or
`AWS/S3`. Those instructions are later in this topic.

###### To find the metrics with recommended alarms, and create a single recommended alarm

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, **All
   metrics**.
3. Above the **Metrics** table, Choose **Alarm
   recommendations**.

The list of metric namespaces is filtered to include only the metrics that have
alarm recommendations and that services in your account are publishing. 4. Choose the namespace for a service.

The list of metrics under this namespace is filtered to include only those that have
alarm recommendations. 5. To see the alarm intent and recommended threshold for a metric, choose
**View details**. 6. To create an alarm for one of the metrics, do one of the following:

    * To use the console to create the alarm, do the following:


    	1. Select the checkbox for the metric and choose the **Graphed
    	 metrics** tab.
    	2. Choose the alarm icon.



    	![Create an alarm from a graphed metric](images/metric_graph_alarm.png)

    	The alarm creation wizard appears, with the metric name, statistic, and
    	 period filled in based on the alarm recommendation. If the recommendation
    	 includes a specific threshold value, that value is also pre-filled.
    	3. Choose **Next**.
    	4. Under **Notification**, select an SNS topic to notify when
    	 the alarm transitions to `ALARM` state, `OK` state, or
    	 `INSUFFICIENT_DATA` state.


    	To have the alarm send multiple notifications for the same alarm state or
    	 for different alarm states, choose **Add notification**.


    	To have the alarm not send notifications, choose
    	 **Remove**.
    	5. To have the alarm perform Auto Scaling or EC2 actions, choose the
    	 appropriate button and choose the alarm state and action to perform.
    	6. When finished, choose **Next**.
    	7. Enter a name and description for the alarm. The name must contain only ASCII
    	 characters. Then choose **Next**.
    	8. Under **Preview and create**, confirm that the information
    	 and conditions are what you want, then choose **Create
    	 alarm**.
    * To download an infrastructure-as-code alarm definition to use in either
     AWS CloudFormation, AWS CLI, or Terraform, choose **Download alarm code** and
     select the format that you want. The downloaded code will have the recommended
     settings for the metric name, statistic, and threshold.

###### To download infrastructure-as-code alarm definitions for all recommended alarms for an AWS service

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, **All
   metrics**.
3. Above the **Metrics** table, Choose **Alarm
   recommendations**.

The list of metric namespaces is filtered to include only the metrics that have
alarm recommendations and that services in your account are publishing. 4. Choose the namespace for a service.

The list of metrics under this namespace is filtered to include only those that have
alarm recommendations. 5. The **Download alarm code** displays how many alarms are
recommended for the metrics in this namespace. To download infrastructure-as-code alarm
definitions for all recommended alarms, choose **Download alarm code**
and then choose the code format that you want.
