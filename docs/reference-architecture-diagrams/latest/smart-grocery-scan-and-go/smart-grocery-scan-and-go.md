

# Smart Grocery with Scan-and-Go, Computer Vision, and IoT
<a name="smart-grocery-scan-and-go"></a>

Publication date: **May 18, 2022 ([Diagram history](#sg-history))**

With this architecture, you can build a smart grocery with Scan-and-Go shopping, traditional point-of-sale (POS), self-checkout, Internet of Things (IoT) connectivity around freezers and storage, and computer vision by using AWS Panorama for shelf-stock intelligence, traffic patterns, queue analysis, and curbside fulfillment automation.

## Architecture diagram
<a name="sg-diagram"></a>

![Smart grocery overview architecture with IoT, computer vision, serverless application layer, and data lake on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/smart-grocery-scan-and-go/images/smart-grocery-with-scan-and-go-computer-vision-and-iot-capability-ra-1.png)


The following steps describe the architecture:

1. Use [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) core to manage connections and aggregate data from in-store sensors and smart retail devices by using the open-standard Message Queuing Telemetry Transport (MQTT) protocol.

1. Use the [AWS Panorama](https://docs.aws.amazon.com/panorama/latest/dev/) on-premises appliance to apply ML and AI models to data from existing in-store IP cameras for smart grocery picking and fulfillment workflows.

1. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/), and AWS AppSync form an integration layer between customer-facing digital ordering applications, associate-facing order-picking applications, and their business logic and data sources.

1. The core smart grocery application layer uses serverless services like [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) to orchestrate order management workflows and connect to transaction, customer, and inventory data.

1. [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/kinesis/latest/dev/) and Amazon Kinesis Data Firehose stream in-store smart device and IoT data. Amazon Kinesis Video Streams optimizes IP camera video feeds for computer vision.

1. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) stores events, connects to smart grocery services, and generates notifications for transactional data.

1. A scalable data lake stores all in-store and digital data (transactional, sensor, telemetry) in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Build a real-time operations dashboard by using AWS AppSync. Use [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/) to deliver targeted, location-based messaging across channels.

## Further reading
<a name="sg-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sg-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#sg-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-scan-and-go-use-case.md#sg-uc1-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-curbside-pickup.md#sg-uc2-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-in-store-monitoring.md#sg-uc3-history) | Reference architecture diagram first published. | May 18, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.