# Debugging with logs from published apps in Amazon CloudWatch Logs

Amazon CloudWatch Logs monitors your AWS resources and the applications you run on AWS
in real time. You can use CloudWatch Logs to collect and track metrics, which are variables you can measure for
your resources and applications.

For debugging App Studio apps, CloudWatch Logs is useful for tracking errors that occur during an app's execution,
auditing information, and providing context on user actions and proprietary interactions.
The logs offer historical data, which you can use to audit application usage and access patterns,
as well as review errors encountered by users.

###### Note

CloudWatch Logs does not provide real-time traces of parameter values passed from the UI of an application.

Use the following procedure to access logs from your App Studio apps in CloudWatch Logs.

1. In the App Studio application studio for your app, locate and note your app ID by looking at in the URL.
   The app ID may look something like this: `802a3bd6-ed4d-424c-9f6b-405aa42a62c5`.
2. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the navigation pane, choose **Log groups**.
4. Here you will find five **log groups** per application.
   Depending on the type of information you are interested in, select a group and write a query for the data you want to discover.

The following list contains the log groups and information about when to use each:

    1. `/aws/appstudio/`teamId`/`appId`/TEST/app`:
     Use to debug automation responses, component errors, or JavaScript code related to the version of your app
     currently published to the Testing environment.
    2. `/aws/appstudio/`teamId`/`appId`/TEST/audit`:
     Use to debug JavaScript code errors, such as conditional visibility or transformation, query failures, and login or permissions user
     errors related to the version of your app currently published to the Testing environment.
    3. `/aws/appstudio/`teamId`/setup`: Use to monitor builder or admin actions.
    4. `/aws/appstudio/`teamId`/`appId`/PRODUCTION/app`:
     Use to debug automation responses, query failures, component errors, or JavaScript code related to the version of your app currently
     published to the Production environment.
    5. `/aws/appstudio/`teamId`/`appId`/PRODUCTION/audit`:
     Use to debug JavaScript code errors, such as conditional visibility or transformation, as well as login or permissions user
     errors related to the version of your app currently published to the Production environment.

###### Note

Most of the logs to be used for debugging are categorized under the `DebugLogClient` namespace. 5. Once you are in a log group, you can either pick the most recent log streams, or one with
a last event time closest to the time of interest, or you can choose to search all log streams
to search across all events on that log group. For more information about viewing log data in CloudWatch Logs, see
[View log data sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#ViewingLogData "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#ViewingLogData").

## Using CloudWatch Logs Insights queries to filter and sort logs

You can use CloudWatch Logs Insights to query multiple log groups at once. Once you
identify a list of log groups that contain session information, navigate to CloudWatch Logs Insights and select the log groups.
Then, further narrow down target log entries by customizing the query. Here are some sample queries:

**List of logs that contain the keyword: `error`**

```
fields @timestamp, @message
| filter @message like 'error'
| sort @timestamp desc
```

**Debug logs from the Testing environment:**

```
fields @timestamp, @message
| filter namespace = "DebugLogClient"
| sort @timestamp desc
```

**Overall 504/404/500 error counts over 5 minute intervals:**

```
filter @message like '/api/automation' and (@message like ': 404' or @message like ': 500' or @message like ': 504')
| fields @timestamp, method, path, statusCode
| stats count(*) as errorCount by bin(5m)
```

For more information
about CloudWatch Logs Insights, [Analyzing log data with CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md")
in the Amazon CloudWatch Logs User Guide.
