

# Expose your data lake as a GraphQL API

Publication date: **April 25, 2022 ([Diagram history](diagram-history.md))**

This architecture shows how to build a data lake using [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) and share it as a self-documented GraphQL API. You can automatically build the API with a reactive CI/CD pipeline, and allow authorized external clients to query your data lake using GraphQL syntax over HTTPS.

## Expose your data lake as a GraphQL API diagram
<a name="data-lake-graphql-api-diagram1"></a>

![Architecture diagram for exposing a data lake as a GraphQL API using AWS AppSync, Athena, Lake Formation, and AWS Glue.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/data-lake-graphql-api.png)


The following steps describe the architecture:

1. Set up a data lake using Lake Formation and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Crawl the data in the Amazon S3 buckets with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) to build a data catalog.

1. Monitor any changes in the AWS Glue Data Catalog with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/), and trigger an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function on every catalog change to update the schema of the external API.

1. In the Lambda function, query the latest data catalog and security settings, automatically generate source code to build and deploy a new version of the external API's schema and resolvers, and commit the code to [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/).

1. Set up CodeCommit to automatically start a new CI/CD pipeline on [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) after any code commit.

1. Use CodePipeline to build a new version of the API with [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/) using the newly generated source code, and use [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/) to deploy both the new [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/) GraphQL API and the new Lambda query resolvers.

1. Allow your GraphQL clients to securely invoke the external API over HTTPS with your chosen authentication mechanism. Activate the AppSync server-side caching.

1. Use the AppSync Lambda query resolvers to translate the GraphQL query into SQL queries supported by [Athena](https://docs.aws.amazon.com/athena/latest/ug/).

1. Run Athena jobs synchronously with the athena-express library, appropriately timing out and limiting the result set.

## Further reading
<a name="data-lake-graphql-api-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)