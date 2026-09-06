

# Centralized Log Analytics
<a name="centralized-log-analytics"></a>

Publication date: **November 7, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to search, analyze, and visualize machine data by using for operational insights.

## Centralized Log Analytics
<a name="diagram1"></a>

![Architecture diagram showing centralized log analytics with .](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/centralized-log-analytics/images/centralized-log-analytics.png)


1. Collectors such as FluentBit, Amazon Kinesis Agent, and the [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) Agent (or services such as [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)) collect log lines and store them in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

1. Amazon S3 sends an object create event to [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html).

1. Amazon SQS invokes an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function that transforms the log lines from strings to structured JSON (if necessary).

1. The Lambda function uses the OpenSearch \_bulk API to deliver the JSON-formatted log lines to [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html).

1. The user logs into OpenSearch Dashboards to perform interactive log analytics, build visualizations or notebooks, and monitor dashboards.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [ product page](https://aws.amazon.com/opensearch-service/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 7, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.