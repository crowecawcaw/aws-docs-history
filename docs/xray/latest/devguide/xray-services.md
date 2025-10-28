# Integrating AWS X-Ray with other AWS services

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

Many AWS services provide varying levels of X-Ray integration, including sampling and adding headers to
incoming requests, running the X-Ray daemon, and automatically sending trace data to X-Ray. Integration with
X-Ray can include the following:

- _Active instrumentation_ – Samples and instruments incoming requests
- _Passive instrumentation_ – Instruments requests that have been sampled by another
  service
- _Request tracing_ – Adds a tracing header to all incoming requests and propagates
  it downstream
- _Tooling_ – Runs the X-Ray daemon to receive segments from the X-Ray SDK

###### Note

The X-Ray SDKs include plugins for additional integration with AWS services. For example, you can use the
X-Ray SDK for Java Elastic Beanstalk plugin to add information about the Elastic Beanstalk environment that runs your application, including
the environment name and ID.

Here are some examples of AWS services that are integrated with X-Ray:

- [AWS Distro for OpenTelemetry (ADOT)](xray-services-adot.md "xray-services-adot.md") – With ADOT, engineers can instrument their
  applications once and send correlated metrics and traces to multiple
  AWS monitoring solutions including Amazon CloudWatch, AWS X-Ray, Amazon OpenSearch Service, and Amazon Managed Service for Prometheus.
- [AWS Lambda](xray-services-lambda.md "xray-services-lambda.md") – Active and passive instrumentation of incoming
  requests on all runtimes. AWS Lambda adds two nodes to your trace map, one for the AWS Lambda service, and one
  for the function. When you enable instrumentation, AWS Lambda also runs the X-Ray daemon on Java and Node.js
  runtimes for use with the X-Ray SDK.
- [Amazon API Gateway](xray-services-apigateway.md "xray-services-apigateway.md") – Active and passive instrumentation. API Gateway uses
  sampling rules to determine which requests to record, and adds a node for the gateway stage to your service
  map.
- [AWS Elastic Beanstalk](xray-services-beanstalk.md "xray-services-beanstalk.md") – Tooling. Elastic Beanstalk includes the X-Ray daemon on the
  following platforms:

      + *Java SE* – 2.3.0 and later configurations
      + *Tomcat* – 2.4.0 and later configurations
      + *Node.js* – 3.2.0 and later configurations
      + *Windows Server* – All configurations other than Windows Server Core that have
       been released after December 9th, 2016

  You can use the Elastic Beanstalk console to tell Elastic Beanstalk to run the daemon on these platforms, or use the
  `XRayEnabled` option in the `aws:elasticbeanstalk:xray` namespace.

- [Elastic Load Balancing](xray-services-elb.md "xray-services-elb.md") – Request tracing on Application Load Balancers.
  The Application Load Balancer adds the trace ID to the request header before sending it to a target
  group.
- [Amazon EventBridge](xray-services-eventbridge.md "xray-services-eventbridge.md") – Passive instrumentation. If a service that publishes events to EventBridge
  is instrumented with the X-Ray SDK, event targets will receive the tracing header and can continue to
  propagate the original trace ID.
- [Amazon Simple Notification Service](xray-services-sns.md "xray-services-sns.md") – Passive instrumentation. If an Amazon SNS publisher traces
  its client with the X-Ray SDK, subscribers can retrieve the tracing header and continue to propagate the
  original trace from the publisher with the same trace ID.
- [Amazon Simple Queue Service](xray-services-sqs.md "xray-services-sqs.md") – Passive instrumentation. If a service traces requests
  by using the X-Ray SDK, Amazon SQS can send the tracing header and continue to propagate the original trace from
  the sender to the consumer with a consistent trace ID.
- [Amazon Bedrock AgentCore](xray-services-sqs.md "xray-services-sqs.md") – AgentCore supports distributed tracing through X-Ray integration, allowing you to track requests as they flow
  through your agent applications. When you enable observability for your AgentCore resources, you can propagate trace context across service boundaries and gain visibility into the performance of your AI agents and tools.
  Choose from the following topics to explore the full set of integrated AWS services.

###### Topics

- [Amazon Bedrock AgentCore and AWS X-Ray](xray-services-agentcore.md "xray-services-agentcore.md")
- [Amazon Elastic Compute Cloud and AWS X-Ray](xray-services-ec2.md "xray-services-ec2.md")
- [Amazon SNS and AWS X-Ray](xray-services-sns.md "xray-services-sns.md")
- [Amazon SQS and AWS X-Ray](xray-services-sqs.md "xray-services-sqs.md")
- [Amazon S3 and AWS X-Ray](xray-services-s3.md "xray-services-s3.md")
- [AWS Distro for OpenTelemetry and AWS X-Ray](xray-services-adot.md "xray-services-adot.md")
- [Tracking X-Ray encryption configuration changes with AWS Config](xray-api-config.md "xray-api-config.md")
- [AWS AppSync and AWS X-Ray](xray-services-appsync.md "xray-services-appsync.md")
- [Amazon API Gateway active tracing support for AWS X-Ray](xray-services-apigateway.md "xray-services-apigateway.md")
- [Amazon EC2 and AWS App Mesh](xray-services-appmesh.md "xray-services-appmesh.md")
- [AWS App Runner and X-Ray](xray-services-app-runner.md "xray-services-app-runner.md")
- [Logging X-Ray API calls with AWS CloudTrail](xray-api-cloudtrail.md "xray-api-cloudtrail.md")
- [CloudWatch integration with X-Ray](xray-services-cloudwatch.md "xray-services-cloudwatch.md")
- [AWS Elastic Beanstalk and AWS X-Ray](xray-services-beanstalk.md "xray-services-beanstalk.md")
- [Elastic Load Balancing and AWS X-Ray](xray-services-elb.md "xray-services-elb.md")
- [Amazon EventBridge and AWS X-Ray](xray-services-eventbridge.md "xray-services-eventbridge.md")
- [AWS Lambda and AWS X-Ray](xray-services-lambda.md "xray-services-lambda.md")
- [AWS Step Functions and AWS X-Ray](xray-services-stepfunctions.md "xray-services-stepfunctions.md")
