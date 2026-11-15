

# Smart Farm on AWS
<a name="smart-farm-on-aws"></a>

Publication date: **October 24, 2022 ([Diagram history](diagram-history.md))**

This Connected Farm reference architecture enables sensors, computer vision, and edge inference in agriculture by focusing on ensuring scalability, elasticity, and a responsiveness for each operation’s growing and changing needs.

## Smart Farm on AWS diagram
<a name="smart-farm-on-aws-diagram1"></a>

![Reference architecture diagram showing how to create a Connected Farm that enables sensors, computer vision, and edge inference in agriculture by focusing on ensuring scalability, elasticity, and a responsiveness for each operation’s growing and changing needs.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/agriculture/images/smart-farm-on-aws.png)


1. Third-party sensors or drones not using [FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/) send data through [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for protocol conversion.

1. Sensors or cameras running FreeRTOS send data to [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), providing protection from intermittent connectivity.

1. AWS IoT Greengrass streams enable ingestion from edge devices to [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/).

1. Use real-time video via [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/) for streaming and replay of video content. 

1. Derive real-time insights with [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/) and notify users via [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

1. Enable analytics with [OpenSearch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) and use [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for a data lake strategy.

1. Transfer owned data, like planting records or farm finances, securely into your data lake with [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. Securely consume data from a sensor ecosystem hosted on AWS with [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/).

1. Empower users with insights delivered via [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) or visualizations with [Quick](https://docs.aws.amazon.com/quick/latest/userguide/).

1. Build and deploy machine learning (ML) models for edge inference with [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/). Use Amazon SageMaker Ground Truth to manage data labeling workflow.

1. Each time a new file is written into Amazon S3, [AWS Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/) crawls the data to infer the schema and make it available into the AWS Glue Data Catalog. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) does on-demand querying.

1. Use a Lambda function that imports the AWS IoT Device Defender reports into [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/) to centralize incident response.

## Further reading
<a name="smart-farm-on-aws-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 