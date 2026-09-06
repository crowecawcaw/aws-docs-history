

# Connected Home Command and Control on AWS
<a name="connected-home-command-control"></a>

Publication date: **March 24, 2021 ([Diagram history](#diagram-history))**

This reference architecture diagram shows how to integrate Alexa with your connected home devices by using AWS.

## Connected Home Command and Control on AWS
<a name="diagram1"></a>

![Reference architecture diagram showing how to integrate Alexa with connected home devices by using AWS IoT Core, AWS Lambda, Amazon API Gateway, DynamoDB, and Amazon Kinesis.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/connected-home-command-control/images/connected-home-command-control.png)


1. An Alexa-enabled device running the Alexa Voice Services SDK or an Amazon Echo creates an Alexa invocation.

1. The Alexa skill uses [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) as its backend logic. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) validates authorization and access control for the Alexa skill before routing data to the correct Skill Handler.

1. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) holds user authorization data that associates your users to their skill and devices while API Gateway verifies whether the request should be accepted.

1. With [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html), you can connect devices to the cloud. AWS IoT Core sends and receives updates based on Alexa invocations.

1. Each Alexa invocation triggers an AWS IoT rule, which evaluates each invocation and routes the message to other AWS services.

1. Each Alexa invocation triggers a message to the AWS IoT Device Shadow. The Shadow service then sends a message to the device with settings that need to be updated to match the Alexa request.

1. AWS IoT Core securely sends IoT data to the devices that need to take action based on the Alexa command.

1. In addition to commands, Alexa can receive device data updates that happen locally. Your devices can send data to AWS IoT Core by using AWS IoT SDK, AWS IoT Greengrass, or Amazon FreeRTOS.

1. The devices send messages to AWS IoT Core, which uses an AWS IoT rule to write data to [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html).

1. Kinesis Data Streams delivers real-time data. Amazon Managed Service for Apache Flink, Spark (Amazon EMR), [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html), Lambda, and other services extract data for processing.

1. The Lambda function invokes the proactive notifications interface for the Alexa Voice Service (AVS). This gives you a visual or audio indication that new content is available from an Alexa domain or an enabled Alexa skill.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 24, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.