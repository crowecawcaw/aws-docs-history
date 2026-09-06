

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Event orchestration
<a name="event-orchestration"></a>

Event orchestration makes it easy for you to send events to AWS services for downstream processing, using [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). Amazon Fraud Detector provides you with simple rules you can use to automate processing of events after fraud detection. With event orchestration, you can automate downstream event processes such as, sending events to dashboards to get insights from event data, generating notifications based on the fraud detection outcomes, and updating events with a label based on the learning from fraud detection. 

Event orchestration provides easy access to services in the AWS environment, through Amazon EventBridge. You can configure Amazon EventBridge to either send events directly to AWS services or indirectly using [API destinations](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html). The AWS services you use to orchestrate your downstream processes are also called *targets*. Some of the targets you can use to orchestrate downstream processing are as follows:
+ For monitoring and analytics — [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html), [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ For storage — [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
+ For sending notifications — [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html), [Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)
+ For custom processing — [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

For more information on the orchestration targets supported by Amazon EventBridge, see [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html).

The following diagram provides a high-level view of how event orchestration works. 



![Image of event orchestration flow.](http://docs.aws.amazon.com/frauddetector/latest/ug/images/event-orchestration-high-level.png)
