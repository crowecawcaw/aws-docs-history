

# Connected Airports Using IoT and AI/ML
<a name="connected-airports"></a>

Publication date: **December 23, 2022 ([Diagram history](#connected-airports-history))**

This reference architecture shows how to build a smart, connected airport using Internet of Things (IoT) and artificial intelligence/machine learning (AI/ML). Airport operators use this architecture to generate near real-time data for aircraft movement, gate turns, baggage tracking, queue depth, and passenger traffic.

Traditional airports rely on manual processes and disconnected systems. These approaches cannot provide the real-time visibility that operations teams need. This architecture connects IoT devices at the edge, processes data in near real time, and applies ML models for predictive insights. You can also implement compliance measures such as social distancing and security monitoring.

This architecture references the [Aircraft Turn Tracking Passive Data Collection](../aircraft-turn-tracking/aircraft-turn-tracking.html) solution for gate turn event collection.

## Connected airports diagram
<a name="connected-airports-diagram"></a>

![Architecture for connected airports using AWS IoT Core, AWS IoT Greengrass, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/connected-airports/images/connected-airports-using-iot-ai-ml-ra.png)


The following steps describe the architecture:

1. Use [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) Core to connect, publish, and subscribe data. Use Message Queuing Telemetry Transport (MQTT) protocol with IoT devices.

1. Use [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) to maintain shadows of IoT devices. Connect to AWS Cloud, manage devices, update over the air (OTA), and secure devices.

1. Use purpose-built databases such as [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) and serverless architecture for events, microservices, and operational data.

1. Build a real-time operational dashboard by using microservices and AWS AppSync. Deliver alerts through [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/).

1. Build the data lake in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) for raw and curated processed data.

1. Discover and govern data in Amazon S3 by using AWS Glue crawlers, Glue Data Catalog, and [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/). Deploy Amazon Macie to detect sensitive data.

1. Use AWS Glue jobs and Amazon EMR for data transformation and enrichment.

1. Use [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), [Athena](https://docs.aws.amazon.com/athena/latest/ug/), and [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) for analytics. Build data marts in Amazon Redshift for heavily used analytics.

1. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to build, train, and deploy inference models. Deploy edge models on AWS IoT Greengrass Core.

1. Use the Aircraft Turn Tracking solution to passively collect gate turn events.

1. Use social distancing and queue depth management solutions for compliance.

## Further reading
<a name="connected-airports-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="connected-airports-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#connected-airports-history) | Reference architecture diagram first published. | December 23, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.