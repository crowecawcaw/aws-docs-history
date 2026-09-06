

# In-store monitoring use case
<a name="smart-grocery-in-store-monitoring"></a>

With this use case, you can build an in-store monitoring solution by using IoT sensors, computer vision, and AWS analytics services for real-time operations visibility.

## Architecture diagram
<a name="sg-uc3-diagram"></a>

![In-store monitoring architecture with AWS IoT Greengrass, AWS Panorama, Amazon Kinesis Data Streams, and Amazon S3 data lake on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/smart-grocery-scan-and-go/images/smart-grocery-with-scan-and-go-computer-vision-and-iot-capability-ra-4.png)


The following steps describe the architecture:

1. Use [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) core to manage connections and aggregate data from in-store sensors and devices by using Message Queuing Telemetry Transport (MQTT). Use [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) to manage all in-store smart devices.

1. Use the [AWS Panorama](https://docs.aws.amazon.com/panorama/latest/dev/) on-premises appliance to apply AI/ML models to data from in-store IP cameras. Use [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/) and Amazon SageMaker AI inference training to build and maintain computer vision models.

1. [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/kinesis/latest/dev/) and Amazon Kinesis Data Firehose stream in-store device and IoT data into [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Amazon Kinesis Video Streams optimizes IP camera feeds into AWS Panorama.

1. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) stores events, connects to smart grocery services, and generates notifications. [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) is the core data warehouse.

1. Use a scalable Amazon S3 data lake to store all in-store and digital data by using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/). Use [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) for reporting and analytics.

1. Build a real-time operations dashboard by using AWS AppSync. Use [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/) for targeted, location-based messaging.

## Further reading
<a name="sg-uc3-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sg-uc3-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](smart-grocery-scan-and-go.md#sg-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-scan-and-go-use-case.md#sg-uc1-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-curbside-pickup.md#sg-uc2-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](#sg-uc3-history) | Reference architecture diagram first published. | May 18, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.