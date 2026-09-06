

# Decoupled Serverless Scheduler, Part 1
<a name="decoupled-serverless-scheduler-part1"></a>

Publication date: **February 18, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to deploy a decoupled serverless scheduler to run any HPC application at scale. You submit jobs to [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) using [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) Run Command, and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) orchestrates the job execution on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instances.

## Decoupled Serverless Scheduler, Part 1
<a name="diagram1"></a>

![Architecture diagram showing the decoupled serverless scheduler Part 1 using Amazon Simple Queue Service, AWS Step Functions, AWS Lambda, Amazon DynamoDB, and Amazon Elastic Compute Cloud.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/decoupled-serverless-scheduler/images/decoupled-serverless-scheduler-1.png)


The following steps describe the architecture:

1. Jobs submitted to Amazon SQS use AWS Systems Manager Run Command such as bash or Windows PowerShell.

1. You launch an Amazon EC2 instance or cluster of Amazon EC2 instances with the tag key `scheduler-queue`.

1. On Amazon EC2 launch, an [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) Event triggers an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function.

1. The Lambda function looks for the tag key `scheduler-queue` and triggers a new Step Functions state machine, passing the instance ID and tag value (SQS job queue name).

1. The workflow polls Amazon SQS for a new job, and continues to poll until there are no more jobs.

1. The workflow runs the job on previously launched Amazon EC2 instances or cluster of Amazon EC2 instances.

1. The workflow continuously writes job status to a [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) table.

1. You monitor job status through the AWS Management Console or AWS Command Line Interface (AWS CLI).

## Further reading
<a name="further-reading-1"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Decoupled Serverless Scheduler on GitHub](https://github.com/aws-samples/aws-decoupled-serverless-scheduler)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | February 18, 2021 | 
| [Initial publication](decoupled-serverless-scheduler-part2.md#diagram-history-2) | Reference architecture diagram first published. | February 18, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.