

# Tracing Data Lake Ingest and Processing
<a name="traceability-data-lake-ingest"></a>

Publication date: **July 15, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to trace your data lake ingestion and processing using AWS X-Ray. You can emit traces from key checkpoints in the flow to diagnose data lake processing lifecycle issues and identify performance bottlenecks.

## Tracing Data Lake Ingest and Processing Using AWS X-Ray
<a name="diagram1"></a>

![Architecture diagram showing data lake ingest and processing traceability using AWS X-Ray, AWS Step Functions, AWS Lambda, and Amazon Simple Storage Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/traceability-serverless-analytics/images/traceability-serverless-analytics-1.png)


The following steps describe the architecture:

1. Diverse producers deliver data into the data lake built on [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

1. The data first lands in an Amazon S3 bucket for raw data. This is the first trace since AWS X-Ray enables trace messages for Amazon S3 Event Notifications.

1. Data lake curation blocks prepare the data for analytics. [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) triggers these processing blocks. AWS X-Ray integrates with Step Functions to help you identify performance bottlenecks and troubleshoot requests that resulted in an error.

1. AWS X-Ray can trace [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions. Lambda runs the X-Ray daemon and records a segment with details about the function invocation and results. For further instrumentation, bundle the X-Ray SDK with the function to record outgoing calls and add annotations and metadata.

1. Data curation continues with the Step Functions state machine triggering the next curation block. Like the first block, X-Ray can capture Step Functions and Lambda functions.

1. The data lands in an aggregated bucket ready for analytics. This is the last trace in the data lake ingestion flow. With traces emitting from all key checkpoints, you can diagnose data lake processing lifecycle issues.

1. Diverse analytics tools such as [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html), Amazon Redshift, and [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) enable you to visualize the data from the data lake built on Amazon S3.

## Further reading
<a name="further-reading-1"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Quick editions](https://docs.aws.amazon.com/quicksight/latest/user/editions.html)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | July 15, 2021 | 
| [Initial publication](traceability-downstream-analytics.md#diagram-history-2) | Reference architecture diagram first published. | July 15, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.