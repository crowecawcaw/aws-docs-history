

# Autoscaling Asynchronous Job Queues
<a name="autoscaling-async-job-queues"></a>

Publication date: **April 15, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to perform background processing jobs such as document generation, extract, transform, and load (ETL) tasks, and inference with [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html). You use [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to manage the job lifecycle.

## Autoscaling Asynchronous Job Queues
<a name="diagram1"></a>

![Architecture diagram showing autoscaling asynchronous job queues using Amazon API Gateway, Amazon Simple Queue Service, Amazon CloudWatch, Amazon Elastic Container Service with AWS Fargate, and Amazon DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/autoscaling-async-job-queues/images/autoscaling-async-job-queues.png)


The following steps describe the architecture:

1. Each job type requires an [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) instance (desiredCount = 0), an Amazon SQS queue, and associated [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms.

1. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) provides an interface to add, query, and cancel jobs.

1. The add job Lambda function creates the job state item in DynamoDB and enqueues the job ID on Amazon SQS.

1. The Amazon SQS job queue contains messages with the IDs of the jobs to be processed.

1. CloudWatch monitors the Amazon SQS queue depth. Alarms are triggered when the depth exceeds a configurable value and when the queue is empty.

1. Amazon ECS responds to the CloudWatch alarms, changing the desired count and scaling the number of parallel jobs.

1. AWS Fargate runs job processing containers from Amazon Elastic Container Registry (Amazon ECR). The containers poll Amazon SQS for job IDs, read the job item from DynamoDB, and perform processing, updating the job status in DynamoDB and publishing to an [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) topic on a status change.

1. A DynamoDB table stores the state, parameters, and results of the jobs by job ID.

1. Amazon ECR stores the job processing container images. An Amazon SNS topic publishes job items on state change notifications to subscribers.

1. Two control Lambda functions allow jobs to be queried and canceled from API Gateway by reading or updating the job item in DynamoDB.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 15, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.