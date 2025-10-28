# Reviewing logs for sensitive data

discovery jobs

After you start running sensitive data discovery jobs in Amazon Macie, you can review logs for
your jobs by using Amazon CloudWatch Logs. CloudWatch Logs provides features that are designed to help you
review, analyze, and monitor log data. You can use these features to work with log
streams and events for jobs as you would work with any other type of log data in
CloudWatch Logs.

For example, you can search and filter aggregate data to identify specific types of
events that occurred for all of your jobs during a specific time range. Or you can
perform a targeted review of all the events that occurred for a particular job. CloudWatch Logs
also provides options for monitoring log data, defining metric filters, and creating
custom alarms.

###### Tip

To quickly navigate to the log data for a particular job, you can use the Amazon Macie
console. To do this, choose the job's name on the **Jobs** page. At
the top of the details panel, choose **Show results**, and then
choose **Show CloudWatch logs**. Macie opens the Amazon CloudWatch console and
displays a table of log events for the job.

###### To review logs for sensitive data discovery jobs

Follow these steps to navigate to and review log data by using the Amazon CloudWatch console. To
review the data programmatically, use the [Amazon CloudWatch Logs
API](../../../AmazonCloudWatchLogs/latest/APIReference/Welcome.md "../../../AmazonCloudWatchLogs/latest/APIReference/Welcome.md").

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you ran jobs that you want to review logs for.
3. In the navigation pane, choose **Logs**, and then choose
   **Log groups**.
4. On the **Log groups** page, choose the
   **/aws/macie/classificationjobs** log group. CloudWatch displays
   a table of log streams for the jobs that you've run. There is one unique stream
   for each job. The name of each stream correlates to the unique identifier for a
   job.
5. On the **Log streams** tab, do one of the following:
   - To review the log events for a particular job, choose the log stream for the job. To
     find the stream more easily, enter the job's unique identifier in the
     filter box above the table. After you choose the log stream, CloudWatch
     displays a table of log events for the job.
   - To review log events for all of your jobs, choose **Search all log
     streams**. CloudWatch displays a table of log events for all of
     your jobs.

6. (Optional) In the filter box above the table, enter terms, phrases, or values that specify
   characteristics of specific events to review. For more information, see [Search log data using filter patterns](../../../AmazonCloudWatch/latest/logs/SearchDataFilterPattern.md "../../../AmazonCloudWatch/latest/logs/SearchDataFilterPattern.md") in the _Amazon CloudWatch Logs User Guide_.
7. To review the details of a specific log event, choose expand (
   ![The expand row icon, which is a right-facing solid arrow.](images/icon-caret-right-filled.png)
   )
   in the row for the event. CloudWatch displays the event's details in JSON format. To
   learn more about these details, see [Understanding log
   events for jobs](discovery-jobs-monitor-cw-logs-ref.md "discovery-jobs-monitor-cw-logs-ref.md").
   As you familiarize yourself with the data in the log events, you can perform additional
   tasks to streamline analysis and monitoring of the data. For example, you can [create metrics filters](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md") that turn log data into numerical CloudWatch metrics. You
   can also [create custom
   alarms](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") that make it easier to identify and respond to specific log events.
   For more information, see the [Amazon CloudWatch Logs User
   Guide](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").
