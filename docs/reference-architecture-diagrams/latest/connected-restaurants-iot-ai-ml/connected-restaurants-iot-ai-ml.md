

# Connected Restaurants using IoT and AI/ML
<a name="connected-restaurants-iot-ai-ml"></a>

Publication date: **December 21, 2022 ([Diagram history](#conrest-history))**

With this architecture, you can build smart, connected restaurants. Use IoT and artificial intelligence/machine learning (AI/ML) to maintain food quality and safety. Preserve cold storage, manage queues, and monitor foot and vehicle traffic. The solution uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) to maintain cost efficiency and improve operability.

## Connected restaurants diagram
<a name="conrest-diagram"></a>

![How to build connected restaurants by using AWS IoT Core, AWS IoT Greengrass, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/connected-restaurants-iot-ai-ml/images/connected-restaurants-using-iot-ai-ml-ra.png)


The following steps describe the architecture:

1. Use [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) Core to connect, publish, and subscribe to data. Communicate by using the Message Queuing Telemetry Transport (MQTT) protocol with IoT devices that run on FreeRTOS and other operating systems.

1. Use [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) to maintain device shadows for all IoT devices. Connect to the AWS Cloud, manage devices, update over-the-air (OTA), and secure the devices.

1. Use purpose-built databases such as [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) and serverless architecture. Store events, deliver microservices, and generate events for the operational data store.

1. Build a near real-time operational dashboard by using microservices and [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/).

1. Use [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/) to deliver alerts to multiple channels.

1. Build a data lake to store raw data and create curated datasets in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) for data processing.

1. Discover and govern data in Amazon S3 by using AWS Glue crawlers, the AWS Glue Data Catalog, and [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/). Deploy [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/) to detect sensitive data.

1. Use AWS Glue jobs and Amazon EMR to transform or enrich the data.

1. Use [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/), [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), and [Amazon Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) for analytics. (Optional) Build data marts in Amazon Redshift for heavily used analytics. For one-time needs, use Athena or Amazon Redshift Spectrum for direct analysis on the data lake.

1. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to build, train, and deploy inference models. (Optional) Deploy edge models on AWS IoT Greengrass Core. Use the Facilitate Social Distancing and Queue Depth Management solutions for compliance and enhanced customer experience.

1. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) to integrate with third-party providers.

## Further reading
<a name="conrest-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="conrest-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#conrest-history) | Reference architecture diagram first published. | December 21, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.