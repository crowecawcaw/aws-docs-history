

# Chatting about your AWS resources
<a name="resources"></a>

With the AWS assistant, you can get answers about the resources in your AWS account. You can understand your infrastructure without navigating multiple service consoles, APIs, or scripts.

You can chat about your resources in the AWS Management Console and AWS Console Mobile Application.

The AWS assistant supports:

**Resource listing and details**  
Request lists or configuration details for resources in your account.

**Filtered queries**  
Filter by criteria such as AWS Region, resource category, resource ID, or tag.

**Cross-service analysis**  
Ask about relationships, configurations, and dependencies across multiple services.

**Troubleshooting**  
Identify potential causes and get tailored remediation steps and recommendations.

## How resource analysis works
<a name="resource-how-it-works"></a>

The AWS assistant uses AWS APIs to retrieve requested information. It can perform read-only get, list, and describe operations for multiple resources. For complex requests, it creates a sequence of read-only steps and explains them. It can request more information when needed.

The AWS assistant can display read-only tables and charts to summarize resources and costs. It cannot inspect data stored inside resources, such as the objects in an Amazon Simple Storage Service (Amazon S3) bucket. It also can't answer questions about your account security, identity, credentials, or cryptography.

## Required permissions
<a name="resource-permissions"></a>

In addition to the permissions in [Step 2: Verify required permissions](getting-started.md#permissions-overview), resource questions require permission for the AWS APIs that retrieve information about the resources in your question. You also need to allow the AWS assistant to retrieve resource information on your behalf with the `q:PassRequest` permission. For more information, see [Using `q:PassRequest`](permissions-reference.md#passrequest). For an example policy, see [Allow users to chat about resources](security-iam-examples.md#iam-example-resource-chat).

Normal AWS service charges apply when the AWS assistant performs read, list, or describe operations.

## Ask resource questions
<a name="ask-resource-questions"></a>

You can specify the Region in your prompt. If you don't specify one, the AWS assistant uses a Region established earlier in the conversation. Otherwise, it uses the current console Region. If you're on the console page of a global service, it uses the most recent console Region that you selected. It might ask a follow-up question when it needs a resource name, ID, Region, or time range.

Example prompts include:
+ Describe the encryption settings for S3 bucket `{{bucket-name}}`.
+ List the SQS queues that invoke my AWS Lambda functions.
+ Find the MySQL RDS clusters that need updates.
+ List my EC2 instances in `{{Region}}`.
+ List the alarms configured for instance `{{instance-id}}`.
+ List RDS databases without Amazon CloudWatch alarms.
+ List S3 buckets with tag value `{{tag-value}}`.
+ Show a chart of my costs by service last week.
+ Show a bar chart of my ten most expensive resources.
+ Create a chart showing budget compared with forecasted spend.

## Troubleshoot resources
<a name="troubleshoot-resources"></a>

In the AWS Management Console, open the AWS assistant and describe the problem. It analyzes the available information and identifies potential root causes. It then provides solutions, step-by-step instructions, or recommendations.

You can troubleshoot resources only in the AWS Management Console. Enter your prompt in English.

The following table lists the supported services, issues, and example prompts.


| AWS service | Supported issues | Example prompt | 
| --- | --- | --- | 
| Amazon Simple Storage Service (Amazon S3) | Permissions | Why can't I put objects into my S3 bucket amzn-s3-demo-bucket? | 
| AWS Glue | Job failures | Why did my AWS Glue job fail? | 
| Amazon Athena | Query issues | Why didn't my Amazon Athena query return results? | 
| Amazon Elastic Container Service (Amazon ECS) | Stopped tasks, AWS Fargate health checks, and disconnected agents | My ECS task stopped and I don't know why. | 
| Elastic Load Balancing | Load balancer health checks and HTTP 500, 502, 503, and 504 errors | Why is my load balancer returning 503 errors? | 
| Amazon Elastic Kubernetes Service (Amazon EKS) | ALB controller and managed add-on issues | Why are the add-ons in my EKS cluster failing? | 
| Amazon Elastic Container Registry (Amazon ECR) | Cross-account repository access | How do I allow another account to push and pull images? | 
| Amazon CloudWatch | Metric and performance monitoring | Show me the CPU utilization for my EC2 instance i-1234567890abcdef0 over the last 24 hours. | 

For resource troubleshooting, you need the same permissions as for other resource questions.