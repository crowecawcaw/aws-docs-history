

# Curbside pickup use case
<a name="smart-grocery-curbside-pickup"></a>

With this use case, you can automate curbside pickup by using geofencing, computer vision, and serverless order management on AWS.

## Architecture diagram
<a name="sg-uc2-diagram"></a>

![Curbside pickup architecture with Amazon Location Service, AWS Panorama, AWS Step Functions, and Amazon S3 data lake on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/smart-grocery-scan-and-go/images/smart-grocery-with-scan-and-go-computer-vision-and-iot-capability-ra-3.png)


The following steps describe the architecture:

1. [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/) provides geofencing and notifies an in-store associate when a customer enters the parking lot. Cameras and sensors monitor vehicle movement and read the tag number.

1. An application and pre-trained ML model on the [AWS Panorama](https://docs.aws.amazon.com/panorama/latest/dev/) appliance processes camera video and notifies the in-store team for curbside delivery.

1. Processed videos go to [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/) and Amazon SageMaker AI inference training.

1. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/), and AWS AppSync form the integration layer between ordering and fulfillment applications.

1. The core application layer uses [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) to orchestrate order management.

1. [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/kinesis/latest/dev/) ingests sensor data into [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Amazon Kinesis Video Streams streams camera feeds.

1. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) stores events from sensors and cameras with notifications for the in-store team.

1. Build an Amazon S3 data lake for raw and curated data (images, video, customer details).

1. Build a real-time operational dashboard by using AWS AppSync. Deliver alerts across channels with [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/).

## Further reading
<a name="sg-uc2-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sg-uc2-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](smart-grocery-scan-and-go.md#sg-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-scan-and-go-use-case.md#sg-uc1-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](#sg-uc2-history) | Reference architecture diagram first published. | May 18, 2022 | 
| [Initial publication](smart-grocery-in-store-monitoring.md#sg-uc3-history) | Reference architecture diagram first published. | May 18, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.