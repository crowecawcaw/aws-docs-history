

# Connected Lodging Properties Using IoT and AI/ML
<a name="connected-lodging-properties-iot"></a>

Publication date: **August 28, 2020 ([Diagram history](#conlodge-history))**

With this architecture, you can build smart, connected lodging properties. Use IoT and artificial intelligence/machine learning (AI/ML) to provide touchless room personalization. The solution monitors queue depths, tracks foot and vehicle traffic, and maintains sanitation compliance. It uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) at the edge and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for inference models.

## Connected lodging properties diagram
<a name="conlodge-diagram"></a>

![How to build connected lodging properties by using AWS IoT Core, AWS IoT Greengrass, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/connected-lodging-properties-iot/images/connected-lodging-properties-iot.png)


The following steps describe the architecture:

1. Use [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) Core to connect, publish, and subscribe to data. Communicate by using the Message Queuing Telemetry Transport (MQTT) protocol with IoT devices that run on FreeRTOS.

1. Use [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) to maintain device shadows for all IoT devices. Connect to the AWS Cloud, manage devices, update over-the-air (OTA), and secure the devices.

1. Use purpose-built databases such as [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) and serverless architecture. Store events, deliver microservices, and generate events for an operational data store.

1. Use Alexa Voice Service to personalize guest rooms with voice-enabled controls.

1. Use [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/) to deliver alerts to multiple channels. Send notifications for operational events and property management.

1. Build a data lake to store raw data and create curated datasets in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) for data processing.

1. Use SageMaker AI to build, train, and deploy inference models. (Optional) Deploy edge models on AWS IoT Greengrass Core.

1. Use [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/), [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), and [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) for analytics. (Optional) Build data marts in Amazon Redshift for heavily used analytics.

1. Use social distancing and queue depth management solutions for compliance and enhanced guest experience.

## Further reading
<a name="conlodge-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="conlodge-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#conlodge-history) | Reference architecture diagram first published. | August 28, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.