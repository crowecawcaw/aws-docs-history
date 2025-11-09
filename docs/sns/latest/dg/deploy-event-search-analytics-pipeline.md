# Deploying and subscribing the

Event Search and Analytics Pipeline to Amazon SNS

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| For event archiving and analytics, Amazon SNS now recommends using its native integration with Amazon Data Firehose.<br>You can subscribe Firehose delivery streams to SNS topics, which allows you to send<br>notifications to archiving and analytics endpoints such as Amazon Simple Storage Service (Amazon S3) buckets, Amazon Redshift<br>tables, Amazon OpenSearch Service (OpenSearch Service), and more. Using Amazon SNS with Firehose delivery streams is a fully-managed and codeless solution that<br>doesn't require you to use AWS Lambda functions. For more information,<br>see [Fanout to Firehose delivery streams](sns-firehose-as-subscriber.md "sns-firehose-as-subscriber.md"). |

This page shows how to deploy the [Event Search and Analytics
Pipeline](sns-fork-pipeline-as-subscriber.md#sns-fork-event-search-and-analytics-pipeline "sns-fork-pipeline-as-subscriber.md#sns-fork-event-search-and-analytics-pipeline") and subscribe it to an Amazon SNS topic. This process automatically turns
the AWS SAM template associated with the pipeline into an AWS CloudFormation stack, and then deploys
the stack into your AWS account. This process also creates and configures the set of
resources that comprise the Event Search and Analytics Pipeline, including the
following:

- Amazon SQS queue
- Lambda function
- Firehose delivery stream
- Amazon OpenSearch Service domain
- Amazon S3 dead-letter bucket
  For more information about configuring a stream with an index as a destination, see
  `ElasticsearchDestinationConfiguration` in the
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
    2. Search for `fork-event-search-analytics-pipeline` and then
       choose the application.

4.  On the **fork-event-search-analytics-pipeline** page, do the
    following:

        1. In the **Application settings** section, enter an
         **Application name** (for example,
         `my-app-search`).


        ###### Note

        For each deployment, the application name must be unique. If you
         reuse an application name, the deployment will update only the
         previously deployed AWS CloudFormation stack (rather than create a new
         one).
        2. (Optional) For **DataTransformationFunctionArn**,
         enter the ARN of the Lambda function used for transforming incoming
         events. If you don't enter a value, data transformation is
         disabled.
        3. (Optional) Enter one of the following **LogLevel**
         settings for the execution of your application's Lambda function:




        	* `DEBUG`
        	* `ERROR`
        	* `INFO` (default)
        	* `WARNING`
        4. (Optional) For **SearchDomainArn**, enter the ARN of
         the OpenSearch Service domain, a cluster that configures the needed compute and
         storage functionality. If you don't enter a value, a new domain is
         created with the default configuration.
        5. For **TopicArn**, enter the ARN of the Amazon SNS topic to
         which this instance of the fork pipeline is to be subscribed.
        6. For **SearchIndexName**, enter the name of the OpenSearch Service
         index for event search and analytics.


        ###### Note

        The following quotas apply to index names:



        	* Can't include uppercase letters
        	* Can't include the following characters: `\ / * ? "
        	 < > | ` , #`
        	* Can't begin with the following characters: `- +
        	 _`
        	* Can't be the following: `. ..`
        	* Can't be longer than 80 characters
        	* Can't be longer than 255 bytes
        	* Can't contain a colon (from OpenSearch Service 7.0)
        7. (Optional) Enter one of the following
         **SearchIndexRotationPeriod** settings for the
         rotation period of the OpenSearch Service index:




        	* `NoRotation` (default)
        	* `OneDay`
        	* `OneHour`
        	* `OneMonth`
        	* `OneWeek`
        Index rotation appends a timestamp to the index name, facilitating the
         expiration of old data.
        8. For **SearchTypeName**, enter the name of the OpenSearch Service
         type for organizing the events in an index.


        ###### Note



        	* OpenSearch Service type names can contain any character (except null
        	 bytes) but can't begin with `_`.
        	* For OpenSearch Service 6.x, there can be only one type per index. If you
        	 specify a new type for an existing index that already has
        	 another type, Firehose returns a runtime error.
        9. (Optional) For **StreamBufferingIntervalInSeconds**
         and **StreamBufferingSizeInMBs**, enter the values for
         configuring the buffering of incoming events. If you don't enter any
         values, 300 seconds and 5 MB are used.
        10. (Optional) Enter one of the following
         **StreamCompressionFormat** settings for
         compressing incoming events:




        	* `GZIP`
        	* `SNAPPY`
        	* `UNCOMPRESSED` (default)
        	* `ZIP`
        11. (Optional) For **StreamPrefix**, enter the string
         prefix to name files stored in the Amazon S3 dead-letter bucket. If you don't
         enter a value, no prefix is used.
        12. (Optional) For **StreamRetryDurationInSecons**, enter
         the retry duration for cases when Firehose can't index events in the OpenSearch Service
         index. If you don't enter a value, then 300 seconds is used.
        13. (Optional) For **SubscriptionFilterPolicy**, enter
         the Amazon SNS subscription filter policy, in JSON format, to be used for
         filtering incoming events. The filter policy decides which events are
         indexed in the OpenSearch Service index. If you don't enter a value, no filtering is
         used (all events are indexed).
        14. Choose **I acknowledge that this app creates custom IAM roles,
         resource policies and deploys nested applications.** and
         then choose **Deploy**.

    On the **Deployment status for
    `my-app-search`** page, Lambda displays the
    **Your application is being deployed** status.

In the **Resources** section, AWS CloudFormation begins to create the stack and
displays the **CREATE_IN_PROGRESS** status for each resource. When the
process is complete, AWS CloudFormation displays the **CREATE_COMPLETE**
status.

When the deployment is complete, Lambda displays the **Your application has
been deployed** status.

Messages published to your Amazon SNS topic are indexed in the OpenSearch Service index provisioned by
the Event Search and Analytics pipeline automatically. If the pipeline can't index an
event, it stores it in a Amazon S3 dead-letter bucket.
