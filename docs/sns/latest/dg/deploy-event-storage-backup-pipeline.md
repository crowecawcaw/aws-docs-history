# Deploying and subscribing the

Event Storage and Backup Pipeline to Amazon SNS

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| For event archiving and analytics, Amazon SNS now recommends using its native integration with Amazon Data Firehose.<br>You can subscribe Firehose delivery streams to SNS topics, which allows you to send<br>notifications to archiving and analytics endpoints such as Amazon Simple Storage Service (Amazon S3) buckets, Amazon Redshift<br>tables, Amazon OpenSearch Service (OpenSearch Service), and more. Using Amazon SNS with Firehose delivery streams is a fully-managed and codeless solution that<br>doesn't require you to use AWS Lambda functions. For more information,<br>see [Fanout to Firehose delivery streams](sns-firehose-as-subscriber.md "sns-firehose-as-subscriber.md"). |

This page shows how to deploy the [Event Storage and Backup
Pipeline](sns-fork-pipeline-as-subscriber.md#sns-fork-event-storage-and-backup-pipeline "sns-fork-pipeline-as-subscriber.md#sns-fork-event-storage-and-backup-pipeline") and subscribe it to an Amazon SNS topic. This process automatically turns
the AWS SAM template associated with the pipeline into an CloudFormation stack, and then deploys
the stack into your AWS account. This process also creates and configures the set of
resources that comprise the Event Storage and Backup Pipeline, including the
following:

- Amazon SQS queue
- Lambda function
- Firehose delivery stream
- Amazon S3 backup bucket
  For more information about configuring a stream with an Amazon S3 bucket as a destination,
  see `S3DestinationConfiguration` in the
  _Amazon Data Firehose API Reference_.

For more information about transforming events and about configuring event buffering,
event compression, and event encryption, see [Creating an Delivery Stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the
_Amazon Data Firehose Developer Guide_.

For more information about filtering events, see [Amazon SNS subscription filter
policies](sns-subscription-filter-policies.md "sns-subscription-filter-policies.md") in this guide.

1.  Sign in to the [AWS Lambda
    console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2.  On the navigation panel, choose **Functions** and then choose
    **Create function**.
3.  On the **Create function** page, do the following:
    1. Choose **Browse serverless app repository**,
       **Public applications**, **Show apps that
       create custom IAM roles or resource policies**.
    2. Search for `fork-event-storage-backup-pipeline` and then
       choose the application.

4.  On the **fork-event-storage-backup-pipeline** page, do the
    following:

        1. In the **Application settings** section, enter an
         **Application name** (for example,
         `my-app-backup`).


        ###### Note



        	* For each deployment, the application name must be unique.
        	 If you reuse an application name, the deployment will update
        	 only the previously deployed CloudFormation stack (rather than create
        	 a new one).
        2. (Optional) For **BucketArn**, enter the ARN of the Amazon S3
         bucket into which incoming events are loaded. If you don't enter a
         value, a new Amazon S3 bucket is created in your AWS account.
        3. (Optional) For **DataTransformationFunctionArn**,
         enter the ARN of the Lambda function through which the incoming events
         are transformed. If you don't enter a value, data transformation is
         disabled.
        4. (Optional) Enter one of the following **LogLevel**
         settings for the execution of your application's Lambda function:




        	* `DEBUG`
        	* `ERROR`
        	* `INFO` (default)
        	* `WARNING`
        5. For **TopicArn**, enter the ARN of the Amazon SNS topic to
         which this instance of the fork pipeline is to be subscribed.
        6. (Optional) For **StreamBufferingIntervalInSeconds**
         and **StreamBufferingSizeInMBs**, enter the values for
         configuring the buffering of incoming events. If you don't enter any
         values, 300 seconds and 5 MB are used.
        7. (Optional) Enter one of the following
         **StreamCompressionFormat** settings for
         compressing incoming events:




        	* `GZIP`
        	* `SNAPPY`
        	* `UNCOMPRESSED` (default)
        	* `ZIP`
        8. (Optional) For **StreamPrefix**, enter the string
         prefix to name files stored in the Amazon S3 backup bucket. If you don't enter
         a value, no prefix is used.
        9. (Optional) For **SubscriptionFilterPolicy**, enter
         the Amazon SNS subscription filter policy, in JSON format, to be used for
         filtering incoming events. The filter policy decides which events are
         indexed in the OpenSearch Service index. If you don't enter a value, no
         filtering is used (all events are indexed).
        10. (Optional) For **SubscriptionFilterPolicyScope**,
         enter the string `MessageBody` or
         `MessageAttributes` to enable payload-based or
         attribute-based message filtering.
        11. Choose **I acknowledge that this app creates custom IAM roles,
         resource policies and deploys nested applications.** and
         then choose **Deploy**.

    On the **Deployment status for `my-app`**
    page, Lambda displays the **Your application is being deployed**
    status.

In the **Resources** section, CloudFormation begins to create the stack and
displays the **CREATE_IN_PROGRESS** status for each resource. When the
process is complete, CloudFormation displays the **CREATE_COMPLETE**
status.

When the deployment is complete, Lambda displays the **Your application has
been deployed** status.

Messages published to your Amazon SNS topic are stored in the Amazon S3 backup bucket provisioned
by the Event Storage and Backup pipeline automatically.
