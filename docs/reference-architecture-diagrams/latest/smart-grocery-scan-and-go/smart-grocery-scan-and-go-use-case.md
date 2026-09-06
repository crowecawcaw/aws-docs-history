

# Scan-and-Go use case
<a name="smart-grocery-scan-and-go-use-case"></a>

With this use case, you can build a Scan-and-Go checkout experience by using in-store IP cameras, sensors, and POS integration with AWS computer vision and streaming services.

## Architecture diagram
<a name="sg-uc1-diagram"></a>

![Scan-and-Go architecture with AWS Panorama, Amazon Kinesis Data Streams, Amazon DynamoDB, and Amazon S3 data lake on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/smart-grocery-scan-and-go/images/smart-grocery-with-scan-and-go-computer-vision-and-iot-capability-ra-2.png)


The following steps describe the architecture:

1. In-store IP cameras capture real-time video of the checkout process. With sensors and POS, they identify products and make checkout seamless.

1. [AWS Panorama](https://docs.aws.amazon.com/panorama/latest/dev/) processes the video on-premises by using optimized AI/ML models. Results integrate into customer ordering and associate fulfillment applications.

1. Processed videos go to [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/) and Amazon SageMaker AI inference training to optimize computer vision models.

1. [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/kinesis/latest/dev/) ingests in-store sensor and device data. Amazon Kinesis Data Firehose loads it into an [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) data lake. Amazon Kinesis Video Streams optimizes IP camera feeds.

1. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) stores sensor telemetry from smart devices with trigger-based notifications. [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) is the core data warehouse for analytics.

1. Use a scalable Amazon S3 data lake to store raw device data and curated processed data such as images, shopper analytics, and commerce details.

## Further reading
<a name="sg-uc1-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sg-uc1-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](smart-grocery-scan-and-go.md#sg-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](#sg-uc1-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-curbside-pickup.md#sg-uc2-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-in-store-monitoring.md#sg-uc3-history) | Reference architecture diagram first published. | May 18, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.