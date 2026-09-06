

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Amazon Q Business chat metrics
<a name="qbusiness-metrics-chat"></a>

The following table shows the [Chat and conversation management](conversation-api.md) metrics that Amazon Q Business sends to CloudWatch in real time. 


| Metric name | Unit | Description | 
| --- | --- | --- | 
| `ActionErrorCount` | Count | The number of errors because of actions.<br />Valid dimensions: `ApplicationId`, `PluginId` | 
| `ActionInvocationCount` | Count | The number of actions invoked.<br />Valid dimensions: `ApplicationId`, `PluginId` | 
| `BlockedChatMessages` | Count | The number of chat messages that were blocked by Amazon Q Business due to an admin guardrail configuration. For example, a `BlockedTopic` or `Blocked Phrase`. . <br />Valid dimensions: `ApplicationId` | 
| `ChatMessages` | Count | The number of chat messages This metric is emitted every time a chat message is processed.<br />Valid dimensions: `ApplicationId` | 
| `ChatMessagesWithAttachment` | Count | The number of chat messages with file uploads.<br />Valid dimensions: `ApplicationId` | 
| `ChatMessagesWithNoAnswer` | Count | The number of chat messages that resulted in no answer. <br />Valid dimensions: `ApplicationId` | 
| `HallucinatedChatMessages` | Count | The number of system-generated chat messages with hallucination. You can create a hallucination rate metric by combining this metric with the `ChatMessages` metric. <br />Valid dimensions: `ApplicationId` | 
| `TimeToFirstToken` | Milliseconds | The time taken to generate the first token in a chat response. This metric measures the initial response latency for chat interactions.<br />Valid dimensions: `API name`, `ApplicationId` | 
| `Latency` | Milliseconds | The total time taken to complete a chat API request from start to finish. This metric measures the end-to-end response time for chat interactions.<br />Valid dimensions: `API name`, `ApplicationId` | 
| `DailyActiveUsers` | Count | The number of active users from the previous day. This metric is calculated using the *Maximum* statistic. For more information, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html). <br />Valid dimensions: `ApplicationId` | 
| `MonthlyActiveUsers` | Count | The total number of unique month-to-date active users. This metric will be calculated from the 00:00 UTC on the first day of the month till 00:00 UTC from the current day. This metric is calculated using the *Maximum* statistic. For more information, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html). <br />Valid dimensions: `ApplicationId` | 
| `WeeklyActiveUsers` | Count | The total number of unique week-to-date active users. This metric will be calculated from 00:00 UTC on Sunday till 00:00 UTC from the current day. This metric is calculated using the *Maximum* statistic. For more information, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html). <br />Valid dimensions: `ApplicationId` | 
| `NewConversations` | Count | The number of new conversations started. <br />Valid dimensions: `ApplicationId` | 
| `ThumbsDownCount` | Count | The feedback count for thumbs down.<br />Valid dimensions: `ApplicationId`, `UsefulnessReason` | 
| `ThumbsUpCount` | Count | The feedback count for thumbs up.<br />Valid dimensions: `ApplicationId`, `UsefulnessReason` | 