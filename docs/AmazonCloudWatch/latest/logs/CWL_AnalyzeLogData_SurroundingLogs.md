# Viewing surrounding logs in CloudWatch Logs Insights

You can view log events that occurred before and after a specific log record
returned by your CloudWatch Logs Insights query. Surrounding logs help you understand the context
around errors, warnings, or other significant events.

## How surrounding logs work

When you run a CloudWatch Logs Insights query, each log record in the results includes a
**Surrounding logs** option. When you choose this option,
CloudWatch Logs Insights displays additional log events from the same log stream that occurred
immediately before and after the selected record. These events appear even if
they don't match your original query filters.

You can configure the number of surrounding log lines to display. Choose
from 5, 10, 20, 50, or 100 log lines above and below the selected record.

Surrounding logs are useful in the following scenarios:

- Debugging errors by viewing the events that led to a failure
- Investigating warnings or timeouts in distributed systems
- Understanding the sequence of events across your application
- Analyzing issues in high-volume log environments

## View surrounding logs

###### To view surrounding logs

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Logs
   Insights**.
3. Run your query.
4. In the query results, locate the log record that you want to
   investigate.
5. Choose **Surrounding logs**.

![The Surrounding logs option on a query result record in CloudWatch Logs Insights.](images/surrounding-logs-button.png) 6. In the **Number of events** dropdown, choose the
number of log events to display above and below the selected record.
You can choose 5, 10, 20, 50, or 100.

![Configuring the number of surrounding log events to display above and below the selected record.](images/surrounding-logs-configure-events.png)

## Search within surrounding logs

After you open the surrounding logs panel, you can search for specific
keywords to locate relevant context.

###### To search within surrounding logs

1. In the surrounding logs panel, enter your search term in the search
   box.
2. Review the highlighted matching log lines.
3. Use the navigation controls to move between matches.

![Searching for keywords within the surrounding logs panel, with highlighted matches and navigation controls.](images/surrounding-logs-keyword-search.png)
