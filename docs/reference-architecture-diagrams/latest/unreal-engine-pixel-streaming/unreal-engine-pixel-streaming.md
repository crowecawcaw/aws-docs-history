

# Unreal Engine's Pixel Streaming on AWS
<a name="unreal-engine-pixel-streaming"></a>

Publication date: **January 6, 2023 ([Diagram history](#pixel-history))**

This architecture shows a simple implementation of Unreal Engine's Pixel Streaming feature on AWS. The architecture uses a serverless matchmaker composed of [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/). Both the streaming instance and signaling servers are hosted in the same [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instance.

## Unreal Engine's Pixel Streaming on AWS diagram
<a name="pixel-diagram"></a>

![Reference architecture diagram showing how to deploy Unreal Engine's Pixel Streaming on AWS by using a serverless matchmaker with Amazon SQS, Lambda, and DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/unreal-engine-pixel-streaming/images/unreal-engine-pixel-streaming.png)


The following steps describe the architecture:

1. The client requests an [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) identity and temporary AWS credentials.

1. The client signs a request to [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) with the temporary credentials.

1. API Gateway forwards the request to Amazon SQS to ensure requests are handled in order.

1. Lambda checks DynamoDB for an available streaming instance. If none are available, it can request a new instance.

1. DynamoDB stores required metadata such as the instance status, IP address, port number, and user reservation details.

1. If an instance is not available, Lambda requests that a new one be created.

1. [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) stores static assets such as game builds and bootstrap scripts.

1. After a new instance is created, its metadata is written to DynamoDB by using Lambda.

1. A separate route in API Gateway lets the client poll DynamoDB for their assigned instance.

1. The client uses the IP and port returned from DynamoDB to connect to their assigned instance.

## Further reading
<a name="pixel-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="pixel-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#pixel-history) | Reference architecture diagram first published. | January 6, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.