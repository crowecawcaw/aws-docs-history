# Integrating optimized services with Step Functions

Your workflow can call optimized services directly using the `Resource` field
of a `Task` state. The following topics explain the supported APIs, parameters, and request/response syntax in Amazon States Language for coordinating AWS services.

Depending on workflow type and availability, your workflows call services using one of three service integration patterns:

- [Request a Response (default)](connect-to-resource.md#connect-default "connect-to-resource.md#connect-default") - wait for HTTP response, then go to the next state
- [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") - wait for the job to complete
- [Wait for Callback (.waitForTaskToken)](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token") - pause a workflow until a task token is returned
  Standard Workflows and Express Workflows support the same **integrations** but not the same **integration
  patterns**.

- **Standard Workflows** support _Request Response_ integrations. Certain services support _Run a Job
  (.sync)_, or _Wait for Callback
  (.waitForTaskToken)_ , and both in some cases. See the following optimized integrations table for details.
- **Express Workflows** only support _Request Response_ integrations.

To help decide between the two types, see [Choosing workflow type in Step Functions](choosing-workflow-type.md "choosing-workflow-type.md").

**AWS SDK integrations in Step Functions**

| Integrated service                                                                                                                                     | Request Response   | Run a Job<br>• _.sync_ | Wait for Callback<br>• _.waitForTaskToken_ |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ---------------------- | ------------------------------------------ |
| [Over two hundred services](supported-services-awssdk.md#supported-services-awssdk-list "supported-services-awssdk.md#supported-services-awssdk-list") | Standard & Express | _Not supported_        | Standard                                   |

**Optimized integrations in Step Functions**

| Integrated service                                                              | Request Response   | Run a Job<br>• _.sync_ | Wait for Callback<br>• _.waitForTaskToken_ |
| ------------------------------------------------------------------------------- | ------------------ | ---------------------- | ------------------------------------------ |
| [Amazon API Gateway](connect-api-gateway.md "connect-api-gateway.md")           | Standard & Express | _Not supported_        | Standard                                   |
| [Amazon Athena](connect-athena.md "connect-athena.md")                          | Standard & Express | Standard               | _Not supported_                            |
| [AWS Batch](connect-batch.md "connect-batch.md")                                | Standard & Express | Standard               | _Not supported_                            |
| [Amazon Bedrock](connect-bedrock.md "connect-bedrock.md")                       | Standard & Express | Standard               | Standard                                   |
| [AWS CodeBuild](connect-codebuild.md "connect-codebuild.md")                    | Standard & Express | Standard               | _Not supported_                            |
| [Amazon DynamoDB](connect-ddb.md "connect-ddb.md")                              | Standard & Express | _Not supported_        | _Not supported_                            |
| [Amazon ECS/Fargate](connect-ecs.md "connect-ecs.md")                           | Standard & Express | Standard               | Standard                                   |
| [Amazon EKS](connect-eks.md "connect-eks.md")                                   | Standard & Express | Standard               | Standard                                   |
| [Amazon EMR](connect-emr.md "connect-emr.md")                                   | Standard & Express | Standard               | _Not supported_                            |
| [Amazon EMR on EKS](connect-emr-eks.md "connect-emr-eks.md")                    | Standard & Express | Standard               | _Not supported_                            |
| [Amazon EMR Serverless](connect-emr-serverless.md "connect-emr-serverless.md")  | Standard & Express | Standard               | _Not supported_                            |
| [Amazon EventBridge](connect-eventbridge.md "connect-eventbridge.md")           | Standard & Express | _Not supported_        | Standard                                   |
| [AWS Glue](connect-glue.md "connect-glue.md")                                   | Standard & Express | Standard               | _Not supported_                            |
| [AWS Glue DataBrew](connect-databrew.md "connect-databrew.md")                  | Standard & Express | Standard               | _Not supported_                            |
| [AWS Lambda](connect-lambda.md "connect-lambda.md")                             | Standard & Express | _Not supported_        | Standard                                   |
| [AWS Elemental MediaConvert](connect-mediaconvert.md "connect-mediaconvert.md") | Standard & Express | Standard               | _Not supported_                            |
| [Amazon SageMaker AI](connect-sagemaker.md "connect-sagemaker.md")              | Standard & Express | Standard               | _Not supported_                            |
| [Amazon SNS](connect-sns.md "connect-sns.md")                                   | Standard & Express | _Not supported_        | Standard                                   |
| [Amazon SQS](connect-sqs.md "connect-sqs.md")                                   | Standard & Express | _Not supported_        | Standard                                   |
| [AWS Step Functions](connect-stepfunctions.md "connect-stepfunctions.md")       | Standard & Express | Standard               | Standard                                   |
