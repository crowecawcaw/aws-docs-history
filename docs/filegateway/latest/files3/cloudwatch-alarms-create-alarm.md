# Create a custom CloudWatch alarm for your

gateway

CloudWatch uses Amazon Simple Notification Service (Amazon SNS) to send alarm notifications when an alarm changes state.
An alarm watches a single metric over a time period that you specify, and performs one
or more actions based on the value of the metric relative to a given threshold over a
number of time periods. The action is a notification that's sent to an Amazon SNS topic. You
can create an Amazon SNS topic when you create a CloudWatch alarm. For more information about
Amazon SNS, see [What is Amazon
SNS?](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") in the _Amazon Simple Notification Service Developer Guide_.

###### To create a CloudWatch alarm in the Storage Gateway console

1.  Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/").
2.  In the navigation pane, choose **Gateways**, then choose the
    gateway for which you want to create an alarm.
3.  On the gateway details page, choose the **Monitoring**
    tab.
4.  Under **Alarms**, choose **Create alarm** to
    open the CloudWatch console.
5.  Use the CloudWatch console to create the type of alarm that you want. You can create
    the following types of alarms:
    - Static threshold alarm: An alarm based on a set threshold for a chosen
      metric. The alarm enter the ALARM state when the metric breaches the
      threshold for a specified number of evaluation periods.

    To create a static threshold alarm, see [Creating
    a CloudWatch alarm based on a static threshold](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") in the
    _Amazon CloudWatch User Guide_.
    - Anomaly detection alarm: Anomaly detection mines past metric data and
      creates a model of expected values. You set a value for the anomaly
      detection threshold, and CloudWatch uses this threshold with the model to
      determine the "normal" range of values for the metric. A higher value
      for the threshold produces a thicker band of "normal" values. You can
      choose to activate the alarm only when the metric value is above the
      band of expected values, only when it's below the band, or when it's
      above or below the band.

    To create an anomaly detection alarm, see [Creating a CloudWatch alarm based on anomaly detection](../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md") in the
    _Amazon CloudWatch User Guide_.
    - Metric math expression alarm: An alarm based one or more metrics used
      in a math expression. You specify the expression, threshold, and
      evaluation periods.

    To create a metric math expression alarm, see [Creating a CloudWatch alarm based on a metric math expression](../../../AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.md "../../../AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.md") in
    the _Amazon CloudWatch User Guide_.
    - Composite alarm: An alarm that determines its alarm state by watching
      the alarm states of other alarms. A composite alarm can help you reduce
      alarm noise.

    To create a composite alarm, see [Creating a composite alarm](../../../AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.md") in the _Amazon CloudWatch User
    Guide_.

6.  After you create the alarm in the CloudWatch console, return to the Storage Gateway
    console. You can view the alarm by doing one of the following:

        * In the navigation pane, choose **Gateways**, then
         choose the gateway for which you want to view alarms. On the
         **Details** tab, under **Alarms**,
         choose **CloudWatch Alarms**.
        * In the navigation pane, choose **Gateways**, choose
         the gateway for which you want to view alarms, then choose the
         **Monitoring** tab.


        The **Alarms** section lists all of the CloudWatch alarms
         for a specific gateway. From here, you can select and delete one or more
         alarms, turn alarm actions on or off, and create new alarms.
        * In the navigation pane, choose **Gateways**, then
         choose the alarm state of the gateway for which you want to view
         alarms.

    For information about how to edit or delete an alarm, see [Editing or
    deleting a CloudWatch alarm](../../../AmazonCloudWatch/latest/monitoring/Edit-CloudWatch-Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Edit-CloudWatch-Alarm.md").

###### Note

When you delete a gateway using the Storage Gateway console, all CloudWatch alarms associated
with the gateway are also automatically deleted.
