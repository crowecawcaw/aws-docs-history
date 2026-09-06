

# Publishing Aurora PostgreSQL logs to Amazon CloudWatch Logs
<a name="AuroraPostgreSQL.CloudWatch"></a>

You can configure your Aurora PostgreSQL DB cluster to export log data to Amazon CloudWatch Logs on a regular basis. When you do so, events from your Aurora PostgreSQL DB cluster's PostgreSQL log are automatically *published* to Amazon CloudWatch, as Amazon CloudWatch Logs. In CloudWatch, you can find the exported log data in a *Log group* for your Aurora PostgreSQL DB cluster. The log group contains one or more *log streams* that contain the events from the PostgreSQL log from each instance in the cluster. 

Publishing the logs to CloudWatch Logs allows you to keep your cluster's PostgreSQL log records in highly durable storage. With the log data available in CloudWatch Logs, you can evaluate and improve your cluster's operations. You can also use CloudWatch to create alarms and view metrics. To learn more, see [Monitoring log events in Amazon CloudWatch](AuroraPostgreSQL.CloudWatch.Monitor.md).

**Note**  
Publishing your PostgreSQL logs to CloudWatch Logs consumes storage, and you incur charges for that storage. Be sure to delete any CloudWatch Logs that you no longer need. 

Turning the export log option off for an existing Aurora PostgreSQL DB cluster doesn't affect any data that's already held in CloudWatch Logs. Existing logs remain available in CloudWatch Logs based on your log retention settings. To learn more about CloudWatch Logs, see [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) 

Aurora PostgreSQL supports publishing logs to CloudWatch Logs for the following versions. 
+ 16.1 and all higher versions
+ 15.2 and higher 15 versions
+ 14.3 and higher 14 versions
+ 13.3 and higher 13 versions
+ 12.8 and higher 12 versions
+ 11.9 and higher 11 versions

For information about turning on the option to publish logs to CloudWatch Logs, monitoring log events in CloudWatch Logs, and analyzing logs using CloudWatch Logs Insights, see the following topics.

**Topics**
+ [Turning on the option to publish logs to Amazon CloudWatch](AuroraPostgreSQL.CloudWatch.Publishing.md)
+ [Monitoring log events in Amazon CloudWatch](AuroraPostgreSQL.CloudWatch.Monitor.md)
+ [Analyzing PostgreSQL logs using CloudWatch Logs Insights](AuroraPostgreSQL.CloudWatch.Analyzing.md)