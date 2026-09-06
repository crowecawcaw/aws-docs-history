

# Analyzing PostgreSQL logs using CloudWatch Logs Insights
<a name="AuroraPostgreSQL.CloudWatch.Analyzing"></a>

With the PostgreSQL logs from your Aurora PostgreSQL DB cluster published as CloudWatch Logs, you can use CloudWatch Logs Insights to interactively search and analyze your log data in Amazon CloudWatch Logs. CloudWatch Logs Insights includes a query language, sample queries, and other tools for analyzing your log data so that you can identify potential issues and verify fixes. To learn more, see [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) in the *Amazon CloudWatch Logs User Guide*.

**To analyze PostgreSQL logs with CloudWatch Logs Insights**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, open **Logs** and choose **Log insights**.

1. In **Select log group(s)**, select the log group for your Aurora PostgreSQL DB cluster.  
![Choose the Aurora PostgreSQL log group.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg-cwl-insights-select-log-group.png)

1. In the query editor, delete the query that is currently shown, enter the following, and then choose **Run query**.

   ```
   ##Autovacuum execution time in seconds per 5 minute
   fields @message
   | parse @message "elapsed: * s" as @duration_sec
   | filter @message like / automatic vacuum /
   | display @duration_sec
   | sort @timestamp
   | stats avg(@duration_sec) as avg_duration_sec, 
   max(@duration_sec) as max_duration_sec 
   by bin(5 min)
   ```  
![Query in the query editor.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg-cwl-insights-query.png)

1. Choose the **Visualization** tab.  
![The Visualization tab.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg-cwl-insights-visualization.png)

1. Choose **Add to dashboard**.

1. In **Select a dashboard**, either select a dashboard or enter a name to create a new dashboard.

1. In **Widget type**, choose a widget type for your visualization.  
![The dashboard.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg-cwl-insights-dashboard.png)

1. (Optional) Add more widgets based on your log query results.

   1. Choose **Add widget**.

   1. Choose a widget type, such as **Line**.  
![Choose a widget.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg-cwl-insights-widget.png)

   1. In the **Add to this dashboard** window, choose **Logs**.  
![Add logs to the dashboard.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg-cwl-add-logs-to-dashboard.png)

   1. In **Select log group(s)**, select the log group for your DB cluster.

   1. In the query editor, delete the query that is currently shown, enter the following, and then choose **Run query**.

      ```
      ##Autovacuum tuples statistics per 5 min
      fields @timestamp, @message
      | parse @message "tuples: " as @tuples_temp
      | parse @tuples_temp "* removed," as @tuples_removed
      | parse @tuples_temp "remain, * are dead but not yet removable, " as @tuples_not_removable
      | filter @message like / automatic vacuum /
      | sort @timestamp
      | stats  avg(@tuples_removed) as avg_tuples_removed, 
      avg(@tuples_not_removable) as avg_tuples_not_removable 
      by bin(5 min)
      ```  
![Query in the query editor.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg-cwl-insights-query2.png)

   1. Choose **Create widget**.

      Your dashboard should look similar to the following image.  
![Dashboard with two graphs.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/apg-cwl-insights-dashboard-two-graphs.png)