

# Modern Serverless Mobile/Web Application Architecture
<a name="modern-serverless-mobile-web"></a>

Publication date: **May 10, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to build a modern serverless mobile and web application in AWS. You use [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) for the frontend and Amazon ECS on AWS Fargate containers for backend processing, along with continuous integration and delivery (CI/CD) and analytics to derive insight from application logs and structured data.

## Modern Serverless Mobile/Web Application Architecture
<a name="diagram1"></a>

![Architecture diagram showing a modern serverless mobile and web application using AWS AppSync, Amazon Cognito, AWS Lambda, Amazon DynamoDB, and Amazon Elastic Container Service with AWS Fargate.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/modern-serverless-mobile-web/images/modern-serverless-mobile-web.png)


The following steps describe the architecture:

1. Users authenticate with [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) user pools by retrieving a JWT token, and then use those tokens to retrieve AWS credentials that allow the app to access other AWS services.

1. The mobile and web client interacts with [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) frameworks, which allow communication with backend services from iOS, Android, web, and React Native front ends.

1. The authenticated clients call AWS AppSync to perform GraphQL operations such as queries, mutations, and subscriptions.

1. The Lambda resolvers communicate with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) using temporary IAM credentials based on assumed IAM roles. A JWT token specific to the authenticated user is forwarded to Lambda for processing.

1. The [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) resolver connects existing tables to a GraphQL schema by creating a data source to read, write, and subscribe to real-time data.

1. Lambda sends data to the Amazon Elasticsearch Service domain from DynamoDB whenever new data arrives in the database table, triggering an event notification to Lambda for indexing.

1. The HTTP resolver and endpoints are protected with temporary IAM credentials. A JWT token is forwarded to [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

1. API Gateway uses AWS PrivateLink to encapsulate connections between API Gateway and [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) configured in another VPC with a security group controlling access.

1. A Network Load Balancer (NLB) is configured with a specific port assigned to each service through private integrations towards the Amazon ECS on AWS Fargate cluster, running across multiple Availability Zones.

1. Amazon ECS on AWS Fargate connects to Amazon Elastic Container Registry (Amazon ECR) through an interface VPC endpoint for private access to ECR APIs through private IP addresses.

1. The application workload hosted in Amazon ECS on AWS Fargate containers accesses DynamoDB Accelerator (DAX) in the in-memory cache layer to retrieve frequently accessed information.

1. DynamoDB provides serverless performance at scale for mission-critical workloads including support for ACID transactions.

1. AWS CodeCommit acts as a repository for storing application code whenever the developer modifies or commits changes.

1. AWS CodeBuild compiles source code, runs tests, and produces software packages ready to deploy on a dynamically created build server.

1. AWS CodeDeploy automates software deployments to AWS Fargate with code associated to new features based on developer changes.

1. [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) creates an end-to-end pipeline that fetches application code, builds and tests with CodeBuild, and deploys from Amazon ECR to Fargate.

1. The latest Docker images from the build process are stored in Amazon ECR and pulled for deployment in Fargate across multiple Availability Zones for high availability.

1. Amazon Redshift complements DynamoDB with advanced business intelligence capabilities. DynamoDB table data is copied into Amazon Redshift for complex data analysis queries including joins.

1. The unstructured data from Amazon ECS on AWS Fargate is sent to [Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) in near real time towards the data lake in Amazon Simple Storage Service.

1. [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) creates and publishes interactive business intelligence dashboards using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) as the data source.

1. [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) ETL connects to data stored in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) using the AWS Glue Data Catalog to store metadata such as table and column names.

1. Amazon Athena is an interactive query service that analyzes data registered with the AWS Glue Data Catalog using Presto to process DML statements.

1. User management differs between the [Quick Standard and Enterprise editions](https://docs.aws.amazon.com/quicksight/latest/user/editions.html). Both editions support identity federation through SAML 2.0.

1. Amazon Kinesis Data Firehose is serverless and requires no administration with pay-as-you-go pricing for the volume of data you transmit and process.

1. Amazon Pinpoint segments the campaign audience to reach the right customers and personalizes messages with the right content for push, SMS, email, and voice.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | May 10, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.