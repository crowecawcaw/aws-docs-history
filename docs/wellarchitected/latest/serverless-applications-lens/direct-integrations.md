

# Direct integrations
<a name="direct-integrations"></a>

If your Lambda function is not performing custom logic while integrating with other AWS services, chances are that it may be unnecessary. API Gateway, AWS AppSync, Step Functions, EventBridge, and Lambda destinations can directly integrate with a number of services and provide you more value and less operational overhead. Most public serverless applications provide an API with an agnostic implementation of the contract provided, as described in [RESTful Microservices](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/restful-microservices.html). An example scenario where a direct integration is a better fit is ingesting click stream data through a REST API. 

![Diagram showing sending data to Amazon S3 using Firehose](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/sending-data-to-amazon-s3-using-kinesis-data-firehose.png)


In this scenario, API Gateway will execute a Lambda function that will simply ingest the incoming record into Firehose, which subsequently batches records before storing into a S3 bucket. As no additional logic is necessary for this example, we can use an API Gateway service proxy to directly integrate with Firehose. 

![Diagram showing reducing cost of sending data to Amazon S3 by implementing AWS service proxy](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/sending-data-to-amazon-s3-by-implementing-aws-service-proxy.png)


With this approach, we remove the cost of using Lambda and unnecessary invocations by implementing the AWS Service Proxy within API Gateway. A tradeoff when using the AWS Service Proxy is that a direct integration might introduce some extra complexity if multiple shards are necessary to meet the ingestion rate. In addition in the case that you need to transform the messages being sent to Firehose from API Gateway you will need to use [mapping templates](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html) at the API Gateway layer. Adding mapping templates might introduce extra complexity on the debugging and testing side versus using a Lambda function instead. If latency-sensitive, you can stream data directly to your Firehose by having the correct credentials at the expense of abstraction, contract, and API features. 

![Diagram showing reducing cost of sending data to Amazon S3 by streaming directly using the Firehose SDK](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/sending-data-to-amazon-s3-by-streaming-directly-using-kinesis-data-firehose-sdk.png)


For scenarios where you need to connect with internal resources within your VPC or on-premises and no custom logic is required, use API Gateway private integration. 

![Reference architecture iagram showing Amazon API Gateway private integration over Lambda in VPC to access private resources](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/amazon-api-gateway-private-integration-over-lambda-in-vpc.png)


With this approach, API Gateway sends each incoming request to an Elastic Load Balancer that you own in your VPC, which can forward the traffic to any backend, either in the same VPC or on-premises through an IP address. For REST APIs, Network Load Balancer is supported as a private integration. For HTTP APIs, both Application Load Balancer and Network Load Balancer are supported. This approach has both cost and performance benefits as you don’t need an additional hop to send requests to a private backend with the added benefits of authorization, throttling, and caching mechanisms. Another scenario is a fan-out pattern where Amazon SNS broadcasts messages to all of its subscribers. This approach requires additional application logic to filter and avoid an unnecessary Lambda invocation.

![Reference architecture diagram showing Amazon SNS without message attribute filtering](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/amazon-sns-without-message-attribute-filtering.png)


Amazon SNS can filter events based on message attributes and more efficiently deliver the message to the correct subscriber.

![Diagram showing Amazon SNS with message attribute filtering](http://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/images/amazon-sns-with-message-attribute-filtering.png)
