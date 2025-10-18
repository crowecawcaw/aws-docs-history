# Monitoring details in Internet Monitor (Configure page)

On the **Configure** page, you can see details about your monitor, including a list of resources that
 you monitor traffic for and the thresholds for when health events are triggered. You can also explore and compare values
 for the traffic percentage for your monitor, and its impact on how many city-networks are included for (monitored by) 
 your monitor. Finally, you can view information about measurements that are published to an Amazon S3 bucket.

You can configure a monitor to change most options, such as the percentage of traffic to monitor. For more
 information, see [Configure your monitor](#IMUpdateMonitorConfig "#IMUpdateMonitorConfig").


## Monitor details


The **Monitor details** section includes basic information about your monitor,
 including the name, the percentage of traffic currently being monitored for your application, a
 city-networks maximum limit (if you've set one), and status information about the monitor.


The following explains the values that you might see for **Status** and
 **Status info** (data processing status).




| Status | Description |
| --- | --- |
| Active | Monitor is created and active. |
| Pending | Monitor is currently being created and is not yet active. |
| Inactive | Monitor is created but has been set to inactive. |
| Error | Monitor is in an error state. |
| Status details (Data processing status) | Description |
| --- | --- |
| OK | Monitor is actively processing data. |
| Inactive | Monitor is inactive and is not processing data. |
| Collecting data | Monitor is actively collecting data. |
| Insufficient data | Monitor is actively processing data, but there aren't enough datapoints to produce insights. |
| Fault access CloudWatch | Monitor has encountered a problem delivering CloudWatch metrics data and log events. | ## Health event thresholds In this section, you can see the current thresholds for health events that are configured for this monitor. If you haven't configured any custom thresholds, the values shown here are the default values. By default, health events are not triggered based on local thresholds. If local health event thresholds would be useful for your Internet Monitor scenario, you can enable the option and specify the thresholds to use. You can learn more about how health event thresholds work, and review the potential impact of adding local thresholds or changing existing thresholds. For more information, see [Change health event thresholds](CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview "CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview"). ## Traffic coverage In this section, you can explore options for the traffic coverage for your monitor. When you change the traffic percentage for a monitor, Internet Monitor monitors different amounts of application traffic. If you set a traffic percentage to less than 100% (100% is the default value), some portion of the city-networks that your clients use to access your application might not be monitored. By exploring the impact of different traffic percentage values, you can see how different values that you might set would impact your city-networks coverage. The **Total monitored city-networks** graph shows you how many city-networks are currently monitored, and how many would be monitored if you set the traffic percentage to 100%. To view different traffic percentage values on the graph, select percentages in the drop-down menu. After you explore the options, you can change the traffic percentage to monitor by choosing **Update monitoring coverage**. If you want to set a maximum city-networks limit, at the top of the page, choose **Edit monitor**. Then, under **Advanced options**, set a maximum city-networks value. ## Configure your monitor As on every page in the Internet Monitor dashboard, you can choose **Edit monitor** to change options for your monitor, including adding or removing resources. For details about how to update the following configuration options, see the provided links. **View health event thresholds** In this section, you can see the current thresholds for health events that are configured for this monitor. To update health thresholds, see [Change health event thresholds](CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview "CloudWatch-IM-get-started.md#IMUpdateThresholdFromOverview"). **View and evaluate traffic coverage** In this section, you can compare the effect of changing the percentage of traffic that you monitor for your application on the number of city-networks that are included (for monitoring) when you choose different percentage values. You can also change the percentage of traffic that you monitor, or change the limit for the number of city-networks your monitor includes. To change the percentage of traffic, choose **Update monitoring coverage**. For detailed steps and information, see [Explore changing your application traffic percentage](IMTrafficPercentage.md#IMExploreTrafficPercentage "IMTrafficPercentage.md#IMExploreTrafficPercentage"). **Configuration details for publishing internet measurements to Amazon S3** If you have configured Internet Monitor to publish internet measurements for your monitor to an Amazon S3 bucket, the information about your configuration is shown here. To configure this option, see [Publishing internet measurements to S3](CloudWatch-IM-get-started.md#IMPublishToS3 "CloudWatch-IM-get-started.md#IMPublishToS3").
