# Fanout Amazon SNS events to

AWS Event Fork Pipelines

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| For event archiving and analytics, Amazon SNS now recommends using its native integration with Amazon Data Firehose.<br>You can subscribe Firehose delivery streams to SNS topics, which allows you to send<br>notifications to archiving and analytics endpoints such as Amazon Simple Storage Service (Amazon S3) buckets, Amazon Redshift<br>tables, Amazon OpenSearch Service (OpenSearch Service), and more. Using Amazon SNS with Firehose delivery streams is a fully-managed and codeless solution that<br>doesn't require you to use AWS Lambda functions. For more information,<br>see [Fanout to Firehose delivery streams](sns-firehose-as-subscriber.md "sns-firehose-as-subscriber.md"). |

You can use Amazon SNS to build event-driven applications which use subscriber services to
perform work automatically in response to events triggered by publisher services. This
architectural pattern can make services more reusable, interoperable, and scalable. However, it
can be labor-intensive to fork the processing of events into pipelines that address common event
handling requirements, such as event storage, backup, search, analytics, and replay.

To accelerate the development of your event-driven applications, you can subscribe
event-handling pipelines—powered by AWS Event Fork Pipelines—to Amazon SNS topics. AWS Event Fork Pipelines is a suite of open-source
[nested applications](../../../serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.md"), based on the [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/ "https://aws.amazon.com/serverless/sam/") (AWS
SAM), which you can deploy directly from the [AWS Event Fork Pipelines suite](https://serverlessrepo.aws.amazon.com/applications?query=aws-event-fork-pipelines "https://serverlessrepo.aws.amazon.com/applications?query=aws-event-fork-pipelines") (choose **Show apps that create custom IAM roles or resource policies**) into your AWS account.

For an AWS Event Fork Pipelines use case, see [Deploying and testing
the Amazon SNS event fork pipelines sample application](sns-deploy-test-fork-pipelines-sample-application.md "sns-deploy-test-fork-pipelines-sample-application.md").

###### Topics

- [How AWS Event Fork Pipelines works](#how-sns-fork-works "#how-sns-fork-works")
- [Deploying AWS Event Fork Pipelines](#deploying-sns-fork-pipelines "#deploying-sns-fork-pipelines")
- [Deploying and testing
  the Amazon SNS event fork pipelines sample application](sns-deploy-test-fork-pipelines-sample-application.md "sns-deploy-test-fork-pipelines-sample-application.md")
- [Subscribing AWS Event Fork Pipelines to an
  Amazon SNS topic](sns-subscribe-event-fork-pipelines.md "sns-subscribe-event-fork-pipelines.md")

## How AWS Event Fork Pipelines works

AWS Event Fork Pipelines is a serverless design pattern. However, it is also a suite of nested
serverless applications based on AWS SAM (which you can deploy directly from the AWS Serverless Application Repository
(AWS SAR) to your AWS account in order to enrich your event-driven platforms). You can
deploy these nested applications individually, as your architecture requires.

###### Topics

- [The event storage and backup
  pipeline](#sns-fork-event-storage-and-backup-pipeline "#sns-fork-event-storage-and-backup-pipeline")
- [The event search and
  analytics pipeline](#sns-fork-event-search-and-analytics-pipeline "#sns-fork-event-search-and-analytics-pipeline")
- [The event replay pipeline](#sns-fork-event-replay-pipeline "#sns-fork-event-replay-pipeline")

The following diagram shows an AWS Event Fork Pipelines application supplemented by three nested
applications. You can deploy any of the pipelines from the AWS Event Fork Pipelines suite on the AWS
SAR independently, as your architecture requires.

![The the AWS Event Fork Pipelines architecture, showing how events from an Amazon SNS topic are filtered and processed through three distinct pipelines: Event Storage and Backup, Event Search and Analytics, and Event Replay. These pipelines are depicted as vertically stacked boxes, each independently processing events in parallel from the same Amazon SNS topic.](images/sns-fork-pipeline-as-subscriber-how-it-works.png)

Each pipeline is subscribed to the same Amazon SNS topic, allowing itself to process events in
parallel as these events are published to the topic. Each pipeline is independent and can set
its own [Subscription Filter Policy](sns-subscription-filter-policies.md "sns-subscription-filter-policies.md").
This allows a pipeline to process only a subset of the events that it is interested in (rather
than all events published to the topic).

###### Note

Because you place the three AWS Event Fork Pipelines alongside your regular event processing
pipelines (possibly already subscribed to your Amazon SNS topic), you don’t need to change any
portion of your current message publisher to take advantage of AWS Event Fork Pipelines in your
existing workloads.

### The event storage and backup

pipeline

The following diagram shows the [Event Storage and Backup Pipeline](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~fork-event-storage-backup-pipeline "https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~fork-event-storage-backup-pipeline"). You can subscribe this pipeline to your Amazon SNS
topic to automatically back up the events flowing through your system.

This pipeline is comprised of an Amazon SQS queue that buffers the events delivered by the
Amazon SNS topic, an AWS Lambda function that automatically polls for these events in the queue
and pushes them into an stream, and an Amazon S3 bucket that durably backs up the
events loaded by the stream.

![The Fork-Event-Storage-Backup-Pipeline, which is designed to process and back up events from an Amazon SNS topic. The flow starts with an Amazon SNS topic from which events are fanned out to an Amazon SQS queue. These filtered events are then processed by an Lambda function, which forwards them to an Data Firehose. The Firehose stream is responsible for buffering, transforming, and compressing the events before loading them into an Amazon S3 backup bucket. Finally, Amazon Athena can be used to query the stored data. The diagram uses a series of icons and arrows to illustrate the flow from one service to the next, clearly labeling each component of the pipeline.](images/sns-fork-event-storage-and-backup-pipeline.png)

To fine-tune the behavior of your Firehose stream, you can configure it to buffer,
transform, and compress your events prior to loading them into the bucket. As events are
loaded, you can use Amazon Athena to query the bucket using standard SQL queries. You can also
configure the pipeline to reuse an existing Amazon S3 bucket or create a new one.

### The event search and

analytics pipeline

The following diagram shows the [Event Search and Analytics Pipeline](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~fork-event-search-analytics-pipeline "https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~fork-event-search-analytics-pipeline"). You can subscribe this pipeline to your
Amazon SNS topic to index the events that flow through your system in a search domain and then
run analytics on them.

This pipeline is comprised of an Amazon SQS queue that buffers the events delivered by the
Amazon SNS topic, an AWS Lambda function that polls events from the queue and pushes them into an
stream, an Amazon OpenSearch Service domain that indexes the events loaded by the Firehose stream,
and an Amazon S3 bucket that stores the dead-letter events that can’t be indexed in the search
domain.

![The Event Search and Analytics Pipeline within an AWS architecture. It starts on the left with the Amazon SNS topic receiving all events. These events are then funneled through a dashed line representing "fan out filtered events" into an Amazon SQS queue. From the queue, events are processed by an Lambda function which then forwards them to an Data Firehose stream. The Data Firehose directs the events into two destinations: one route leads to an Amazon Elasticsearch Service for indexing, and the other route sends unprocessable or "dead-letter" events to an Amazon S3 dead-letter bucket. On the far right, the output from the Elasticsearch Service feeds into a Kibana dashboard for analytics and visualization. The entire flow is laid out horizontally and each component is connected by lines showing the direction of data flow.](images/sns-fork-event-search-and-analytics-pipeline.png)

To fine-tune your Firehose stream in terms of event buffering, transformation, and
compression, you can configure this pipeline.

You can also configure whether the pipeline should reuse an existing OpenSearch domain in
your AWS account or create a new one for you. As events are indexed in the search domain,
you can use Kibana to run analytics on your events and update visual dashboards in
real-time.

### The event replay pipeline

The following diagram shows the [Event Replay Pipeline](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~fork-event-replay-pipeline "https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~fork-event-replay-pipeline"). To record the events that have been processed by your
system for the past 14 days (for example when your platform needs to recover from failure),
you can subscribe this pipeline to your Amazon SNS topic and then reprocess the events.

This pipeline is comprised of an Amazon SQS queue that buffers the events delivered by the
Amazon SNS topic, and an AWS Lambda function that polls events from the queue and redrives them
into your regular event processing pipeline, which is also subscribed to your topic.

![The Event Replay Pipeline in a flowchart format. From left to right, it begins with an Amazon SNS topic that distributes filtered events to two parallel processes. The upper flow represents your regular event processing pipeline, which includes an Amazon SQS queue that processes events. The lower flow, labeled as the "fork-event-replay-pipeline," includes an Amazon SQS replay queue where events are temporarily stored before being processed by a Lambda replay function. This Lambda function has the capability to re-drive events into your regular event processing pipeline or hold them for replay, based on whether the replay feature is enabled or disabled. The diagram also indicates that operators have control over enabling or disabling the event replay functionality.](images/sns-fork-event-replay-pipeline.png)

###### Note

By default, the replay function is disabled, not redriving your events. If you need to
reprocess events, you must enable the Amazon SQS replay queue as an event source for the
AWS Lambda replay function.

## Deploying AWS Event Fork Pipelines

The [AWS Event Fork Pipelines suite](https://serverlessrepo.aws.amazon.com/applications?query=aws-event-fork-pipelines "https://serverlessrepo.aws.amazon.com/applications?query=aws-event-fork-pipelines") (choose **Show apps that create custom IAM roles or
resource policies**) is available as a group of public applications in the AWS Serverless Application Repository,
from where you can deploy and test them manually using the [AWS Lambda console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/"). For information
about deploying pipelines using the AWS Lambda console, see [Subscribing AWS Event Fork Pipelines to an
Amazon SNS topic](sns-subscribe-event-fork-pipelines.md "sns-subscribe-event-fork-pipelines.md").

In a production scenario, we recommend embedding AWS Event Fork Pipelines within your overall
application's AWS SAM template. The nested-application feature lets you do this by adding
the resource `AWS::Serverless::Application` to your AWS SAM template, referencing the
AWS SAR `ApplicationId` and the `SemanticVersion` of the nested
application.

For example, you can use the Event Storage and Backup Pipeline as a nested application by
adding the following YAML snippet to the `Resources` section of your AWS SAM
template.

```
Backup:
    Type: AWS::Serverless::Application
  Properties:
    Location:
      ApplicationId: arn:aws:serverlessrepo:us-east-2:123456789012:applications/fork-event-storage-backup-pipeline
      SemanticVersion: 1.0.0
    Parameters:
      #The ARN of the Amazon SNS topic whose messages should be backed up to the Amazon S3 bucket.
      TopicArn: !Ref MySNSTopic
```

When you specify parameter values, you can use AWS CloudFormation intrinsic functions to reference
other resources in your template. For example, in the YAML snippet above, the
`TopicArn` parameter references the `AWS::SNS::Topic` resource
`MySNSTopic`, defined elsewhere in the AWS SAM template. For more information, see
the [Intrinsic Function
Reference](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.md") in the _AWS CloudFormation User Guide_.

###### Note

The AWS Lambda console page for your AWS SAR application includes the **Copy as
SAM Resource** button, which copies the YAML required for nesting an AWS SAR
application to the clipboard.
