

# Decoupled Serverless Scheduler, Part 2
<a name="decoupled-serverless-scheduler-part2"></a>

This architecture shows how to extend the decoupled serverless scheduler by using [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) event triggers and Amazon EC2 Auto Scaling Groups for automatic worker management. You upload input files and executables to Amazon S3 instead of Amazon SQS, eliminating the need for JSON job definitions.

## Decoupled Serverless Scheduler, Part 2
<a name="diagram2"></a>

![Architecture diagram showing the decoupled serverless scheduler Part 2 using Amazon Simple Storage Service, AWS Lambda, and Amazon Elastic Compute Cloud Auto Scaling Groups.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/decoupled-serverless-scheduler/images/decoupled-serverless-scheduler-2.png)


The following steps describe the architecture:

1. You upload input files and executables for jobs to Amazon S3.

1. The Amazon S3 event triggers an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function to create and submit new jobs.

1. Lambda monitors the job queue and updates the Amazon EC2 Auto Scaling Group with the desired instance count (customizable).

1. The Amazon EC2 Auto Scaling Group scales the number of workers from 0 to a defined maximum.

1. You download results from Amazon S3.

1. You monitor job status through the AWS Management Console or AWS CLI.

## Further reading
<a name="further-reading-2"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history-2"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](decoupled-serverless-scheduler-part1.md#diagram-history) | Reference architecture diagram first published. | February 18, 2021 | 
| [Initial publication](#diagram-history-2) | Reference architecture diagram first published. | February 18, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.