

# Spatial Computing 3D Content Management
<a name="spatial-computing-3d-content-management"></a>

Publication date: **August 27, 2021 ([Diagram history](#sc3d-history))**

With this architecture, you can create a single source of truth for 3D assets. Automate ingestion, transformation, and versioning of 3D assets. Process computer-aided design (CAD), photogrammetry, light detection and ranging (LiDAR), or other existing 3D data. The solution uses [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/).

## Spatial computing 3D content management diagram
<a name="sc3d-diagram"></a>

![Reference architecture diagram showing how to create a single source of truth for 3D assets by using Amazon S3, DynamoDB, Lambda, Step Functions, AWS AppSync, API Gateway, Amazon Cognito, and Amazon EC2.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/spatial-computing-3d-content-management/images/sc-3d-cms-aws-reference-architecture-mws-ra.png)


The following steps describe the architecture:

1. With a graphical user interface (GUI) or command-line interface (CLI) client, users upload 3D data, make queries against existing data, and connect to virtual workstations.

1. On initial upload, the system creates an asset entry in a DynamoDB table. Uploading source data to Amazon S3 triggers an event that invokes a Lambda function to initiate a Step Functions workflow.

1. The workflow has three states: inspect the validity of uploaded source data, process the data with AWS Marketplace or open source tools, and record the results in the asset database.

1. Use [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/) to manage create, read, write, and delete operations to asset entries with GraphQL mutations. Consuming applications subscribe to GraphQL subscriptions for real-time updates. Implement a REST API with [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for request and response communication.

1. [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) handles authentication. [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/) user group policies control fine-grained access over asset resources.

1. Virtual workstation desktops stream over the network with [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) graphics instances backed by [Amazon DCV](https://docs.aws.amazon.com/dcv/latest/adminguide/) for manual content authoring.

## Further reading
<a name="sc3d-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="sc3d-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#sc3d-history) | Reference architecture diagram first published. | August 27, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.