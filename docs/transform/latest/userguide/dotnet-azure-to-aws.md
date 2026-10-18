

# Convert cloud-native code to AWS services
<a name="dotnet-azure-to-aws"></a>

When moving cloud-native applications from other clouds to AWS, AWS Transform can help update code to use equivalent AWS services. For example, an Azure Functions serverless function that uses Azure Cosmos DB can be converted to an AWS Lambda function using Amazon DynamoDB. This feature converts application code only and does not handle migration of cloud infrastructure.

Cloud-native code conversion is automatic for eligible modern .NET applications. The agent shares details in the assessment report and modernization plan, which you can customize. To opt out of cloud-native code conversion and leave SDK code from other clouds unchanged, edit the modernization plan or give instructions in agent chat.

Code that cannot be converted to an equivalent on AWS is noted in TODO comments, stubbed code, or the Next Steps markdown file that AWS Transform generates.

Only the specific cloud services listed on this page are converted. To convert code for other cloud services, consider using [AWS Transform custom](https://docs.aws.amazon.com/transform/latest/userguide/custom.html) or an AI code companion such as Kiro.

## Azure to AWS conversions
<a name="dotnet-azure-to-aws-conversions"></a>

AWS Transform can convert Azure application code for these services:


| Service category | From | To | Code conversion details | 
| --- | --- | --- | --- | 
| Serverless functions | Azure Functions | AWS Lambda | Azure Functions are rewritten as AWS Lambda functions | 
| Object storage | Azure Blob Storage | Amazon S3 | Azure.Storage.Blobs SDK code → Amazon.S3 SDK code | 
| Message queuing | Azure Queue Storage | Amazon SQS | Azure.Storage.Queues SDK code → Amazon.SQS SDK code | 
| NoSQL database\* | Azure Cosmos DB | Amazon DynamoDB | Microsoft.Azure.Cosmos SDK code → Amazon.DynamoDBv2 SDK code | 

\* preview feature

## Customizing code conversion
<a name="dotnet-azure-to-aws-customizing"></a>

You can control the code conversion behavior by giving instructions in agent chat, editing the modernization plan, or providing a steering document. Examples of customizations you can ask for include the following:
+ Opt out of some or all service code conversions.
+ Specify variable names or naming conventions to use.
+ Add specific comments or change the verbosity of comments.
+ Redirect default conversion targets, such as converting Azure Blob Storage code to use Amazon DynamoDB instead of Amazon S3.