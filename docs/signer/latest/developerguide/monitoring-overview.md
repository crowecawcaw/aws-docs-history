# Monitor Signer

Monitoring is an important part of maintaining the reliability, availability, and performance of
Signer and your other AWS solutions. AWS provides the following monitoring tools to
watch Signer, report when something is wrong, and take automatic actions when
appropriate:

- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see
  the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
  _Amazon EventBridge_ is a serverless event bus service that makes it easy to connect your
  applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your
  own applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that
  data to targets such as Lambda. This enables you to monitor events that happen in services, and build
  event-driven architectures. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

## Automation with CloudWatch Events

You can automate your use of AWS Signer by tracking and responding to system events that
are managed by Amazon CloudWatch Events. Events resulting from job-completion state changes and from
application availability issues are delivered to CloudWatch Events in near-real time. You can define
simple rules to indicate which events are of interest to you, and to specify actions to take
when an event matches a rule. Examples of actions you can trigger include:

- Invoking an AWS Lambda function
- Invoking the Amazon EC2 `RunInstance` API action
- Relaying the event to Amazon Kinesis Data Streams
- Activating an AWS Step Functions state machine

AWS Signer reports to CloudWatch Events whenever the state of a signing job changes. Customers using
a single account for both the signing profile and signing job will see only a single event.
Customers using separate accounts for the signing profile and signing jobs will see the same
event sent to each account.

The following JSON shows an example of the "Signer Job Status Change" event that
AWS Signer reports.

```
{
   "version":"0",
   "id":"`event_ID`",
   "detail-type":"Signer Job Status Change",
   "source":"aws.signer",
   "account":"`account_ID`",
   "time":"2018-04-26T20:01:47Z",
   "region":"`region`",
   "resources":[
      "arn:aws:signer:us-east-1:`account_ID`:/signing-jobs/`job_ID`"
   ],
   "detail":{
      "certificate_arn":"arn:aws:acm:`region`:`account_ID`:certificate/`certificate_ID`",
      "job_id":"`job_ID`",
      "destination":{
         "bucketName":"`S3_bucket_name`",
         "key":"`S3_key_ID`"
      },
      "source":{
         "bucketName":"`S3_bucket_name`",
         "key":"code",
         "version":"`version_ID`"
      },
      "platform":"Platform",
      "status":"Succeeded"
   }
}
```

For more information, see the [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md").
