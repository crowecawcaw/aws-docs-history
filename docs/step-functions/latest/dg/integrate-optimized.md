

# Integrating optimized services with Step Functions
<a name="integrate-optimized"></a>

Your workflow can call optimized services directly using the `Resource` field of a `Task` state. The following topics explain the supported APIs, parameters, and request/response syntax in Amazon States Language for coordinating AWS services. 

Depending on workflow type and availability, your workflows call services using one of three service integration patterns:
+ [Request a Response (default)](connect-to-resource.md#connect-default) - wait for HTTP response, then go to the next state
+ [Run a Job (`.sync`)](connect-to-resource.md#connect-sync) - wait for the job to complete
+ [Wait for Callback (`.waitForTaskToken`)](connect-to-resource.md#connect-wait-token) - pause a workflow until a task token is returned

Standard Workflows and Express Workflows support the same **integrations** but not the same **integration patterns**. 
+  **Standard Workflows** support *Request Response* integrations. Certain services support *Run a Job (.sync)*, or *Wait for Callback (.waitForTaskToken)* , and both in some cases. See the following optimized integrations table for details. 
+  **Express Workflows** only support *Request Response* integrations. 

 To help decide between the two types, see [Choosing workflow type in Step Functions](choosing-workflow-type.md). 



**AWS SDK integrations in Step Functions**


| Integrated service | Request Response | Run a Job - *.sync* | Wait for Callback - *.waitForTaskToken* | 
| --- | --- | --- | --- | 
| [Over two hundred services](supported-services-awssdk.md#supported-services-awssdk-list) | Standard & Express | Not supported | Standard | 

**Optimized integrations in Step Functions**


| Integrated service | Request Response | Run a Job - *.sync* | Wait for Callback - *.waitForTaskToken* | 
| --- | --- | --- | --- | 
| [Amazon API Gateway](connect-api-gateway.md) | Standard & Express | Not supported | Standard | 
| [Amazon Athena](connect-athena.md) | Standard & Express | Standard | Not supported | 
| [AWS Batch](connect-batch.md) | Standard & Express | Standard | Not supported | 
| [Amazon Bedrock](connect-bedrock.md) | Standard & Express | Standard | Standard | 
| [Amazon Bedrock AgentCore](connect-bedrockagentcore.md) | Standard & Express | Not supported | Not supported | 
| [AWS CodeBuild](connect-codebuild.md) | Standard & Express | Standard | Not supported | 
| [Amazon DynamoDB](connect-ddb.md) | Standard & Express | Not supported | Not supported | 
| [Amazon ECS/Fargate](connect-ecs.md) | Standard & Express | Standard | Standard | 
| [Amazon EKS](connect-eks.md) | Standard & Express | Standard | Standard | 
| [Amazon EMR](connect-emr.md) | Standard & Express | Standard | Not supported | 
| [Amazon EMR on EKS](connect-emr-eks.md) | Standard & Express | Standard | Not supported | 
| [Amazon EMR Serverless](connect-emr-serverless.md) | Standard & Express | Standard | Not supported | 
| [Amazon EventBridge](connect-eventbridge.md) | Standard & Express | Not supported | Standard | 
| [AWS Glue](connect-glue.md) | Standard & Express | Standard | Not supported | 
| [AWS Glue DataBrew](connect-databrew.md) | Standard & Express | Standard | Not supported | 
| [AWS Lambda](connect-lambda.md) | Standard & Express | Not supported | Standard | 
| [AWS Elemental MediaConvert](connect-mediaconvert.md) | Standard & Express | Standard | Not supported | 
| [Amazon SageMaker AI](connect-sagemaker.md) | Standard & Express | Standard | Not supported | 
| [Amazon SNS](connect-sns.md) | Standard & Express | Not supported | Standard | 
| [Amazon SQS](connect-sqs.md) | Standard & Express | Not supported | Standard | 
| [AWS Step Functions](connect-stepfunctions.md) | Standard & Express | Standard | Standard | 