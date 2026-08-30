# Data Lake Ingest and Processing with Downstream Analytics

This architecture shows how to monitor data processing pipelines within the data lake using downstream analytics. You can publish relevant logs, metrics, and events to detect abnormal behaviors and visualize trends in near real time.

## Data Lake Ingest and Processing with Downstream Analytics

![Architecture diagram showing data lake downstream analytics using Amazon CloudWatch, Amazon Kinesis Data Streams, Amazon Kinesis Data Analytics, and Amazon Quick Sight.](images/traceability-serverless-analytics-2.png)

The following steps describe the architecture:

1. Data processing pipelines within the data lake produce data. Any number of source pipelines can produce in this step.
2. The data pipeline components publish relevant logs, metrics, or events to [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").
3. An [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") function fetches data from CloudWatch and pushes pre-processed data to [Amazon Kinesis Data Streams](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md").
4. The Kinesis data stream is the central storage for near real-time streaming data.
5. Amazon Kinesis Data Analytics analyzes data in near real time and saves aggregated metrics to an Amazon Timestream database for further analysis. A Kinesis Data Analytics query can also detect abnormal behaviors of data in the pipeline.
6. Amazon Timestream supports time series analytics and defines time series as a native data type. It supports advanced aggregates, window functions, and complex data types such as arrays and rows.
7. The Amazon Kinesis Data Analytics threshold query sends near real-time analytics to Lambda.
8. Based on the processed data from Kinesis Data Analytics, the Lambda function can send real-time alerts using [Amazon Simple Notification Service](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").
9. [Amazon Quick Sight](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") dashboards visualize trends such as number of successful pipelines, error rate, error type distribution, and more.

## Further reading

For additional information, refer to the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                                     | Description                                     | Date          |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------- |
| [Initial publication](traceability-data-lake-ingest.md#diagram-history "traceability-data-lake-ingest.md#diagram-history") | Reference architecture diagram first published. | July 15, 2021 |
| Initial publication                                                                                                        | Reference architecture diagram first published. | July 15, 2021 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
