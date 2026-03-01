# Create an alarm based on a connected data source

You can create alarms that watch metrics from data sources that aren't in CloudWatch. For more
information about creating connections to these other data sources, see [Query metrics from other data sources](MultiDataSourceQuerying.md "MultiDataSourceQuerying.md").

###### To create an alarm on metrics from a data source that you have connected to

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, **All
   metrics**.
3. Choose the **Multi source query** tab.
4. For **Data source**, select the data source that you want to
   use.
5. The query builder prompts you for the information necessary for the query to
   retrieve the metrics to use for the alarm. The workflow is different for each data
   source, and is tailored to the data source. For example, for Amazon Managed Service for Prometheus and Prometheus data
   sources, a PromQL query editor box with a query helper appears.
6. When you have finished constructing the query, choose **Graph
   query**.
7. If the sample graph looks the way that you expect, choose **Create
   alarm**.
8. The **Specify metric and conditions** page appears. If the query
   you are using produces more than one time series, you see a warning banner at the top of
   the page. If you do, select a function to use to aggregate the time series in
   **Aggregation function**.
9. (Optional) Add a **Label** for the alarm.
10. For **Whenever `your-metric-name` is . .
    .**, choose **Greater**, **Greater/Equal**,
    **Lower/Equal**, or **Lower**. Then for
    **than . . .**, specify a number for your threshold value.
11. Choose **Additional configuration**. For **Datapoints to
    alarm**, specify how many evaluation periods (data points) must be in the
    `ALARM` state to trigger the alarm. If the two values here match, you
    create an alarm that goes to `ALARM` state if that many consecutive periods
    are breaching.

To create an M out of N alarm, specify a number for the first value that is lower
than the number for the second value. For more information, see [Alarm evaluation](alarm-evaluation.md "alarm-evaluation.md"). 12. For **Missing data treatment**, choose how the alarm behaves when
some data points are missing. For more information, see [Configuring how CloudWatch alarms treat missing data](alarms-and-missing-data.md "alarms-and-missing-data.md"). 13. Choose **Next**. 14. For **Notification**, specify an Amazon SNS topic to notify when your
alarm transitions to the `ALARM`, `OK`, or
`INSUFFICIENT_DATA` state.

    1. (Optional) To send multiple notifications for the same alarm state or for
     different alarm states, choose **Add
     notification**.


    ###### Note

    We recommend that you set the alarm to take actions when it goes into
     **Insufficient data** state in addition to when it goes into
     **Alarm** state. This is because many issues with the Lambda
     function that connects to the data source can cause the alarm to transition to
     **Insufficient data**.
    2. (Optional) To not send Amazon SNS notifications, choose **Remove**.

15. To have the alarm perform Auto Scaling, Lambda, or Systems Manager actions, choose the
    appropriate button and choose the alarm state and action to perform. If you choose a
    Lambda function as an alarm action, you specify the function name or ARN, and you can
    optionally choose a specific version of the function.

Alarms can perform Systems Manager actions only when they go into ALARM state. For more
information about Systems Manager actions, see see [Configuring CloudWatch to create OpsItems from alarms](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md") and [Incident creation](../../../incident-manager/latest/userguide/incident-creation.md "../../../incident-manager/latest/userguide/incident-creation.md").

###### Note

To create an alarm that performs an SSM Incident Manager action, you must have
certain permissions. For more information, see [Identity-based policy examples for AWS Systems Manager Incident
Manager](../../../incident-manager/latest/userguide/security_iam_id-based-policy-examples.md "../../../incident-manager/latest/userguide/security_iam_id-based-policy-examples.md"). 16. Choose **Next**. 17. Under **Name and description**, enter a name and description for
your alarm, and choose **Next**. The name must contain only UTF-8
characters, and can't contain ASCII control characters. The description can include
markdown formatting, which is displayed only in the alarm **Details**
tab in the CloudWatch console. The markdown can be useful to add links to runbooks or other
internal resources.

###### Tip

The alarm name must contain only UTF-8 characters. It can't contain ASCII control
characters. 18. Under **Preview and create**, confirm that your alarm's
information and conditions are correct, and choose **Create alarm**.
