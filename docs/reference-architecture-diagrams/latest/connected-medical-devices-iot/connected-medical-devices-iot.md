

# Connected Medical Devices with AWS IoT
<a name="connected-medical-devices-iot"></a>

Publication date: **November 10, 2020 ([Diagram history](#med-devices-history))**

With this architecture, you can manage manufacturer medical devices deployed in hospitals, clinics, and homes. The solution uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) for edge compute, device management, and secure connectivity. [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) handles cloud-based telemetry and device provisioning.

## Connected medical devices diagram
<a name="med-devices-diagram"></a>

![Reference architecture diagram showing how to manage connected medical devices by using AWS IoT Greengrass, AWS IoT Core, Lambda, DynamoDB, and SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/connected-medical-devices-iot/images/connected-medical-devices-iot.png)


The following steps describe the data flow and device management for this architecture:

1. Deploy medical devices in a hospital or clinic network without internet connectivity. Allow only outbound communication to an edge gateway running AWS IoT Greengrass.

1. Use the edge gateway to proxy one or more medical devices. Run local on-premises applications for operators and technicians for command and control. Create only AWS IoT Greengrass cores as Things in AWS IoT Core. Store metadata for medical devices in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. Use [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) as the single secure endpoint invoked from AWS IoT Greengrass for all API calls. APIs include device provisioning and access to AWS services and third-party endpoints.

1. Send streaming video from medical devices to [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) in the AWS Cloud. Persist video in the [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) data lake. Implement data and video insights by linking with device metadata in DynamoDB.

1. Send telemetry data from devices through AWS IoT Greengrass to AWS IoT Core by using Message Queuing Telemetry Transport (MQTT). Store telemetry in [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/) for historical analytics.

1. Upload data files generated from medical procedures directly to Amazon S3. Link files with device metadata in DynamoDB.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) for extract, transform, and load (ETL) processing. Query data with [Athena](https://docs.aws.amazon.com/athena/latest/ug/) and visualize insights with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html).

1. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to train machine learning (ML) models and deploy them to the edge for inferencing on AWS IoT Greengrass.

1. Detect complex events by using [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/). Publish event notifications through [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

1. Use [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) for user authentication and authorization.

## Further reading
<a name="med-devices-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="med-devices-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#med-devices-history) | Reference architecture diagram first published. | November 10, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.