# Accessing the Performance Insights dashboard

Amazon RDS provides a consolidated view of Performance Insights and CloudWatch metrics in the Performance Insights dashboard.

To access the Performance Insights dashboard, use the following procedure.

###### To view the Performance Insights dashboard in the AWS Management Console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the left navigation pane, choose **Performance Insights**.
3. Choose a DB instance.

For DB instances with Performance Insights turned on, you can also access the Performance Insights dashboard by choosing the
**Sessions** item in the list of DB instances. Under
**Current activity**, the **Sessions** item
shows the database load in average active sessions over the last five minutes. The
bar graphically shows the load. When the bar is empty, the DB instance is idle. As
the load increases, the bar fills with blue. When the load passes the number of
virtual CPUs (vCPUs) on the DB instance class, the bar turns red, indicating a
potential bottleneck.

![Filter metrics](images/perf_insights_0a.png) 4. (Optional) Choose the date or time range in the upper right and specify a different
relative or absolute time interval. You can now specify a time period, and generate a database performance analysis report. The
report provides the identified insights and recommendations. For more information,
see [Creating a
performance analysis report in Performance Insights](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md").

![Filter metrics by time interval](images/perf_insights_0c.png)

In the following screenshot, the DB load interval is 5 hours.

![Set time interval to 5 hours](images/perf_insights_1.png) 5. (Optional) To zoom in on a portion of the DB load chart, choose the start time and drag to the end of the time period you want.

The selected area is highlighted in the DB load chart.

![DB load for a specified time interval](images/perf_insights_zoom_in.png)

When you release the mouse, the DB load chart zooms in on the selected AWS Region, and the **Top _dimensions_** table is recalculated.

![Zoom in on the selected DB load](images/perf_insights_zoom_in_b.png) 6. (Optional) To refresh your data automatically, select **Auto
refresh**.

![Set automatic refresh](images/perf_insights_1b.png)

The Performance Insights dashboard automatically refreshes with new data. The refresh rate depends on the
amount of data displayed:

    * 5 minutes refreshes every 10 seconds.
    * 1 hour refreshes every 5 minutes.
    * 5 hours refreshes every 5 minutes.
    * 24 hours refreshes every 30 minutes.
    * 1 week refreshes every day.
    * 1 month refreshes every day.
