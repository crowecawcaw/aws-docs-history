

# Creating Multi-Account IoT Pipelines On-The-Fly on AWS
<a name="multi-account-iot-pipelines"></a>

Publication date: **October 16, 2020 ([Diagram history](#diagram-history))**

This reference architecture diagram shows how to deploy AWS IoT Analytics pipelines into different AWS Organizations accounts. It uses Amazon Managed Service for Apache Flink to buffer and route data from new devices and groups.

## Creating Multi-Account IoT Pipelines On-The-Fly on AWS
<a name="diagram1"></a>

![Reference architecture diagram showing how to automatically deploy AWS IoT Analytics pipelines into different AWS Organizations accounts by using Amazon Managed Service for Apache Flink, AWS Lambda, DynamoDB, and AWS IoT Analytics.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multi-account-iot-pipelines/images/multi-account-iot-pipelines.png)


1. Ingest device telemetry data through the telemetry [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) stream.

1. Detect when Amazon Managed Service for Apache Flink ingests an unregistered device group (shard). Buffer incoming messages in a custom window and emit an event.

1. The shard [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function creates a new account and [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket if an account does not have enough capacity.

1. Use the AWS SDK to create an AWS IoT Analytics channel, Pipeline, and data store for the new shard and register them in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).

1. Emit a registration event that contains the AWS IoT Analytics channel information. This event triggers the Amazon Managed Service for Apache Flink window to continue processing buffered messages for this shard.

1. Detect new devices in the group and emit an asynchronous event to the register-dataset Lambda function. This creates an AWS IoT Analytics dataset while continuing to ingest the telemetry.

1. For each device group, Amazon Managed Service for Apache Flink reads the AWS IoT Analytics channel registration. It then uploads device data to the correct channel in the registered account.

1. AWS IoT Analytics stores device group messages in the channel and transforms them in the pipeline. AWS IoT Analytics then stores the transformed data in the data store backed by Amazon S3.

1. Each device's AWS IoT Analytics dataset uses a delta time query on the datastore. This filters data to a specific device for the most recent 5 minutes to simplify queries.

1. Query device data with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) or [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html).

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS IoT product page](https://aws.amazon.com/iot/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | October 16, 2020 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.