

# Viewing surrounding logs in CloudWatch Logs Insights
<a name="CWL_AnalyzeLogData_SurroundingLogs"></a>

You can view log events that occurred before and after a specific log record returned by your CloudWatch Logs Insights query. Surrounding logs help you understand the context around errors, warnings, or other significant events.

## How surrounding logs work
<a name="CWL_AnalyzeLogData_SurroundingLogs_HowItWorks"></a>

When you run a CloudWatch Logs Insights query, each log record in the results includes a **Surrounding logs** option. When you choose this option, CloudWatch Logs Insights displays additional log events from the same log stream that occurred immediately before and after the selected record. These events appear even if they don't match your original query filters.

You can configure the number of surrounding log lines to display. Choose from 5, 10, 20, 50, or 100 log lines above and below the selected record.

Surrounding logs are useful in the following scenarios:
+ Debugging errors by viewing the events that led to a failure
+ Investigating warnings or timeouts in distributed systems
+ Understanding the sequence of events across your application
+ Analyzing issues in high-volume log environments

## View surrounding logs
<a name="CWL_AnalyzeLogData_SurroundingLogs_ViewLogs"></a>

**To view surrounding logs**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, **Logs Insights**.

1. Run your query.

1. In the query results, locate the log record that you want to investigate.

1. Choose **Surrounding logs**.  
![The Surrounding logs option on a query result record in CloudWatch Logs Insights.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/images/surrounding-logs-button.png)

1. In the **Number of events** dropdown, choose the number of log events to display above and below the selected record. You can choose 5, 10, 20, 50, or 100.  
![Configuring the number of surrounding log events to display above and below the selected record.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/images/surrounding-logs-configure-events.png)

## Search within surrounding logs
<a name="CWL_AnalyzeLogData_SurroundingLogs_Search"></a>

After you open the surrounding logs panel, you can search for specific keywords to locate relevant context.

**To search within surrounding logs**

1. In the surrounding logs panel, enter your search term in the search box.

1. Review the highlighted matching log lines.

1. Use the navigation controls to move between matches.

![Searching for keywords within the surrounding logs panel, with highlighted matches and navigation controls.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/images/surrounding-logs-keyword-search.png)
