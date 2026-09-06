

# Tutorial: Use a metric math function to suppress an alarm
<a name="suppress-alarms-tutorial-suppress"></a>

The following tutorial walks you through how to suppress a CloudWatch alarm using metric math.

**Example scenario**

There's a planned activity that takes place between 1:00 to 3:00 AM UTC on the upcoming Tuesday. You want to create a CloudWatch metric math function that replaces the real data points during this time, with 0 (a data point that falls below the set threshold). 

1. Assess the criteria that causes your alarm to trigger. The following screenshot provides an example of alarm criteria:  
![CloudWatch screen showing alarm details.](http://docs.aws.amazon.com/IDR/latest/userguide/images/metric-math-assess-alarm-criteria.png)

   The alarm shown in the preceding screenshot monitors the `UnHealthyHostCount` metric for an Application Load Balancer target group. This alarm enters the `ALARM` state when the `UnHealthyHostCount` metric is greater than or equal to 3 for 5 out of 5 data points. The alarm treats missing data as bad (breaching the configured threshold).

1. Create the metric math function.

   In this example, the planned activity takes place between 1:00 to 3:00 AM UTC on the upcoming Tuesday. So, create a CloudWatch metric math function that replaces the real data points during this time, with 0 (a data point that falls below the set threshold). 

   Note that the replacement data point that you must configure differs depending on your alarm configuration. For example, if you have an alarm that monitors HTTP success rate, with a threshold of less than 98, then replace your real data points during the planned activity with a value above the configured threshold, 100. The following is an example metric math function for this scenario.

   ```
   IF((DAY(m1) == 2 && HOUR(m1) >= 1 && HOUR(m1) < 3), 0, m1)
   ```

   The preceding metric math function contains the following elements:
   + **DAY(m1) == 2**: Ensures that it's Tuesday (Monday = 1, Sunday = 7).
   + **HOUR(m1) >= 1 && HOUR(m1) < 3**: Specifies the time range from 1 AM to 3 AM UTC.
   + **IF(condition, value\_if\_true, value\_if\_false)**: If the conditions are true, the function replaces the metric value with 0. Otherwise, the original value (m1) is returned.

   For additional information on syntax and available functions, see [Metric math syntax and functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide*

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Alarms**, and then locate the alarm that you want to add the metric math function to.

1. In the metric math section, choose **Edit**.

1. Choose **Add math**, **Start with empty expression**.

1. Enter your math expression, and then choose **Apply**.

   The existing metric that the alarm monitors automatically becomes **m1** and your math expression is **e1**, as shown in the following example:  
![CloudWatch screen showing metric math expressions.](http://docs.aws.amazon.com/IDR/latest/userguide/images/metric-math-expression.png)

1. (Optional) Edit the label of the metric math expression to help others understand it’s function and why it was created, as shown in the following example:  
![CloudWatch screen showing editing of a metric match expression label.](http://docs.aws.amazon.com/IDR/latest/userguide/images/metric-math-edit-label.png)

1. Deselect **m1**, select **e1**, and then choose **Select metric**. This sets the alarm to monitor the math expression instead of the underlying metric directly.

1. Choose **Skip to Preview and create**.

1. Validate that the alarm is configured as expected, then choose **Update alarm to save the change**.

In the preceding example, without the metric math function applied, the real `UnHealthyHostCount` metric would have been reported during the planned activity. This would have resulted in the CloudWatch alarm entering the `ALARM` state and engaging Incident Detection and Response, as shown in the following example:

![CloudWatch screen showing data points leading to an alarm state.](http://docs.aws.amazon.com/IDR/latest/userguide/images/metric-math-example-alarm-state.png)


With the metric math function in place, the real data points are replaced with 0 during the activity, and the alarm remains in the `OK` state, suppressing Incident Detection and Response engagement. 

![CloudWatch screen showing data points with no alarm state.](http://docs.aws.amazon.com/IDR/latest/userguide/images/metric-math-datapoints-no-alarm.png)
