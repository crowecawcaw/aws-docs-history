AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Setting up FireLens log file routing for containers with AWS App2Container

When you set up your application containers to use FireLens for Amazon ECS you can route your
application logs to CloudWatch, Kinesis Data Streams, or Firehose for log storage and analytics. After you have
configured the FireLens settings in your application analysis and deployment JSON files,
App2Container creates the artifacts that you need to deploy your application to Amazon EC2 or
AWS Fargate. This includes:

- Creation of initial Kinesis Data Streams or Firehose streams, if applicable
- Creation of an IAM role with the permissions needed to enable FireLens log routing
  to the destinations that you have specified
- Deployment artifacts that contain the FireLens parameters that you specified in
  your JSON configuration files, including the Amazon ECS task definition and AWS CloudFormation
  template files
  For more information about using FireLens for Amazon ECS, see
  [Custom log routing](../../../AmazonECS/latest/developerguide/using_firelens.md "../../../AmazonECS/latest/developerguide/using_firelens.md")
  in the _Amazon Elastic Container Service Developer Guide_.

###### Note

App2Container initially supports FireLens log file routing for Amazon ECS for Linux containers only.

###### Contents

- [FireLens log routing for Linux](firelens-setup-linux.md "firelens-setup-linux.md")
