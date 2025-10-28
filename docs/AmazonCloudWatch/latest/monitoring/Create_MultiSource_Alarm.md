# Create an alarm based on a connected data

source

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
than the number for the second value. For more information, see [Evaluating an alarm](AlarmThatSendsEmail.md#alarm-evaluation "AlarmThatSendsEmail.md#alarm-evaluation"). 12. For **Missing data treatment**, choose how the alarm behaves when
some data points are missing. For more information, see [Configuring how CloudWatch alarms treat missing
data](AlarmThatSendsEmail.md#alarms-and-missing-data "AlarmThatSendsEmail.md#alarms-and-missing-data"). 13. Choose **Next**. 14. For **Notification**, specify an Amazon SNS topic to notify when your
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

## Details about alarms for connected data

sources

- When CloudWatch evaluates an alarm, it does so every minute, even if the period for the
  alarm is longer than one minute. For the alarm to work, the Lambda function must be
  able to return a list of timestamps starting on any minute, not only on multiples of
  the period length. These timestamps must be spaced one period length apart.

Therefore, if the data source queried by the Lambda can only return timestamps that
are multiples of the period length, the function should "re-sample" the fetched data
to match the timestamps expected by the `GetMetricData` request.

For example, an alarm with a five-minute period is evaluated every minute using
five-minute windows that shift by one minute each time. In this case:

    + For the alarm evaluation at 12:15:00, CloudWatch expects data points with timestamps
     of `12:00:00`, `12:05:00`, and `12:10:00`.
    + Then for the alarm evaluation at 12:16:00, CloudWatch expects data points with
     timestamps of `12:01:00`, `12:06:00`, and
     `12:11:00`.

- When CloudWatch evaluates an alarm, any data points returned by the Lambda function that
  don't align with the expected timestamps are dropped, and the alarm is evaluated using
  the remaining expected data points. For example, when the alarm is evaluated at
  `12:15:00` it expects data with timestamps of `12:00:00`,
  `12:05:00`, and `12:10:00`. If it receives data with
  timestamps of `12:00:00`, `12:05:00`, `12:06:00`, and
  `12:10:00`, the data from `12:06:00` is dropped and CloudWatch
  evaluates the alarm using the other timestamps.

Then for the next evaluation at `12:16:00`, it expects data with
timestamps of `12:01:00`, `12:06:00`, and `12:11:00`.
If it only has the data with timestamps of `12:00:00`,
`12:05:00`, and `12:10:00`, all of these data points are
ignored at 12:16:00 and the alarm transitions into the state according to how you
specified the alarm to treat missing data. For more information, see [Evaluating an alarm](AlarmThatSendsEmail.md#alarm-evaluation "AlarmThatSendsEmail.md#alarm-evaluation").

- We recommend that you create these alarms to take actions when they transition to
  the `INSUFFICIENT_DATA` state, because several Lambda function failure use
  cases will transition the alarm to `INSUFFICIENT_DATA` regardless of the
  way that you set the alarm to treat missing data.
- If the Lambda function returns an error:
  - If there is a permission problem with calling the Lambda function, the alarm
    begins having missing data transitions according to how you specified the alarm to
    treat missing data when you created it.
  - Any other error coming from the Lambda function causes the alarm to transition
    to `INSUFFICIENT_DATA`.

- If the Lambda function returns partial data:
  - The alarm continues to be evaluated on the data points that are
    returned.
  - You can use the following methods to find whether an alarm on a Lambda function
    is currently evaluating its alarm state based on partial data:
    - In the console, choose an alarm and choose the
      **Details** page. If you see the message
      **Evaluation warning: Not evaluating all data appears on that
      page**, it is evaluating on partial data.
    - If you see the value `PARTIAL_DATA` in the
      `EvaluationState` field when you use the
      `describe-alarms` AWS CLI command or the DescribeAlarms API, it is
      evaluating on partial data.

  - An alarm also publishes events to Amazon EventBridge when it goes into the partial data
    state.

- If the metric requested by the Lambda function has some delay so that the last data
  point is always missing, you should use a workaround. You can create an M out of N
  alarm or increase the evaluation period of the alarm. For more information about M out
  of N alarms, see [Evaluating an alarm](AlarmThatSendsEmail.md#alarm-evaluation "AlarmThatSendsEmail.md#alarm-evaluation").
