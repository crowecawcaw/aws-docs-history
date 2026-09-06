

# Creating an Amazon EventBridge pipe
<a name="eb-pipes-create"></a>

EventBridge Pipes enables you to create point-to-point integrations between sources and targets, including advanced event transformations and enrichment. 

To create an EventBridge pipe, you perform the following steps: 

1. [Specifying a source](#pipes-configure-source)

1. [Configuring event filtering (optional)](#pipes-configure-filtering)

1. [Defining event enrichment (optional)](#pipes-define-enrichment)

1. [Configuring a target](#pipes-configure-target)

1. [Configuring the pipe settings](#pipes-configure-pipe-settings)

To quickly set up a sample pipe, see [Getting started: Create an Amazon EventBridge pipe](pipes-get-started.md). This topic uses CloudFormation to deploy a pipe and its associated resources, and walks you through an overview of a pipe's capabilities.

For information on how to create a pipe using the AWS CLI, see [create-pipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/create-pipe.html) in the *AWS CLI Command Reference*.

## Specifying a source
<a name="pipes-configure-source"></a>

To start, specify the source from which you want the pipe to receive events.

**To specify a pipe source by using the console**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. On the navigation pane, choose **Pipes**.

1. Choose **Create pipe**.

1. Enter a name for the pipe.

1. (Optional) Add a description for the pipe.

1. On the **Build pipe** tab, for **Source**, choose the type of source you want to specify for this pipe, and configure the source.

   Configuration properties differ based on the type of source you choose:

------
#### [ Confluent ]

**To configure a Confluent Cloud stream as a source, by using the console**

   1. For **Source**, choose **Confluent Cloud**.

   1. For **Bootstrap servers**, enter the `host:port` pair addresses of your brokers.

   1. For **Topic name**, enter the name of topic that the pipe will read from.

   1. (Optional) For **VPC**, choose the VPC that you want. Then, for **VPC subnets**, choose the desired subnets. For **VPC security groups**, choose the security groups.

   1. For **Authentication - optional**, turn on **Use Authentication** and do the following:

      1. For **Authentication method**, choose the authentication type.

      1. For **Secret key**, choose the secret key.

      For more information, see [Authenticate to Confluent Cloud resources](https://docs.confluent.io/cloud/current/access-management/authenticate/overview.html) in the Confluent documentation.

   1. (Optional) For **Additional setting - optional**, do the following:

      1. For **Starting position**, choose one of the following:
         + **Latest** – Start reading the stream with the most recent record in the shard.
         + **Trim horizon** – Start reading the stream with the last untrimmed record in the shard. This is the oldest record in the shard.

      1. For **Batch size - optional**, enter a maximum number of records for each batch. The default value is 100.

      1. For **Batch window - optional**, enter a maximum number of seconds to gather records before proceeding.

------
#### [ DynamoDB ]

   1. For **Source**, choose **DynamoDB**.

   1. For **DynamoDB stream**, choose the stream you want to use as a source.

   1. For **Starting position**, choose one of the following:
      + **Latest** – Start reading the stream with the most recent record in the shard.
      + **Trim horizon** – Start reading the stream with the last untrimmed record in the shard. This is the oldest record in the shard.

   1. (Optional) For **Additional setting - optional**, do the following:

      1. For **Batch size - optional**, enter a maximum number of records for each batch. The default value is 10.

      1. For **Batch window - optional**, enter a maximum number of seconds to gather records before proceeding.

      1. For **Concurrent batches per shard - optional**, enter the number of batches from the same shard that can be read at the same time.

      1. For **On partial batch item failure**, choose the following:
         + **AUTOMATIC\_BISECT** – Halve each batch and retry each half until all the records are processed or there is one failed message remaining in the batch.
**Note**  
If you don't choose **AUTOMATIC\_BISECT**, you can return specific failed records and only those get retried.

------
#### [ Kinesis ]

**To configure a Kinesis source by using the console**

   1. For **Source**, choose **Kinesis**.

   1. For **Kinesis stream**, choose the stream that you want to use as a source.

   1. For **Starting position**, choose one of the following:
      + **Latest** – Start reading the stream with the most recent record in the shard.
      + **Trim horizon** – Start reading the stream with the last untrimmed record in the shard. This is the oldest record in the shard.
      + **At timestamp** – Start reading the stream from a specified time. Under **Timestamp**, enter a data and time using YYYY/MM/DD and hh:mm:ss format.

   1. (Optional) For **Additional setting - optional**, do the following:

      1. For **Batch size - optional**, enter a maximum number of records for each batch. The default value is 10.

      1. (Optional) For **Batch window - optional**, enter a maximum number of seconds to gather records before proceeding.

      1. For **Concurrent batches per shard - optional**, enter the number of batches from the same shard that can be read at the same time.

      1. For **On partial batch item failure**, choose the following:
         + **AUTOMATIC\_BISECT** – Halve each batch and retry each half until all the records are processed or there is one failed message remaining in the batch.
**Note**  
If you don't choose **AUTOMATIC\_BISECT**, you can return specific failed records and only those get retried.

------
#### [ Amazon MQ ]

**To configure an Amazon MQ source by using the console**

   1. For **Source**, choose **Amazon MQ**.

   1. For **Amazon MQ broker**, choose the stream you want to use as a source.

   1. For **Queue name**, enter the name of the queue that the pipe will read from.

   1. For **Authentication Method**, choose **BASIC\_AUTH**.

   1. For **Secret key**, choose the secret key.

   1. (Optional) For **Additional setting - optional**, do the following:

      1. For **Batch size - optional**, enter a maximum number of messages for each batch. The default value is 100.

      1. For **Batch window - optional**, enter a maximum number of seconds to gather records before proceeding.

------
#### [ Amazon MSK ]

**To configure an Amazon MSK source by using the console**

   1. For **Source**, choose **Amazon MSK**.

   1. For **Amazon MSK cluster**, choose the cluster that you want to use.

   1. For **Topic name**, enter the name of topic that the pipe will read from.

   1. (Optional) For **Consumer Group ID - optional**, enter the ID of the consumer group you want the pipe to join.

   1. (Optional) For **Authentication - optional**, turn on **Use Authentication** and do the following:

      1. For **Authentication method**, choose the type you want.

      1. For **Secret key**, choose the secret key.

   1. (Optional) For **Additional setting - optional**, do the following:

      1. For **Batch size - optional**, enter a maximum number of records for each batch. The default value is 100.

      1. For **Batch window - optional**, enter a maximum number of seconds to gather records before proceeding.

      1. For **Starting position**, choose one of the following:
         + **Latest** – Start reading the topic with the most recent record in the shard.
         + **Trim horizon** – Start reading the topic with the last untrimmed record in the shard. This is the oldest record in the shard.
**Note**  
**Trim horizon** is the same as **Earliest** for Apache Kafka.

------
#### [ Self managed Apache Kafka ]

**To configure a self managed Apache Kafka source by using the console**

   1. For **Source**, choose **Self-managed Apache Kafka**.

   1. For **Bootstrap servers**, enter the `host:port` pair addresses of your brokers.

   1. For **Topic name**, enter the name of topic that the pipe will read from.

   1. (Optional) For **VPC**, choose the VPC that you want. Then, for **VPC subnets**, choose the desired subnets. For **VPC security groups**, choose the security groups.

   1. (Optional) For **Authentication - optional**, turn on **Use Authentication** and do the following:

      1. For **Authentication method**, choose the authentication type.

      1. For **Secret key**, choose the secret key.

   1. (Optional) For **Additional setting - optional**, do the following:

      1. For **Starting position**, choose one of the following:
         + **Latest** – Start reading the stream with the most recent record in the shard.
         + **Trim horizon** – Start reading the stream with the last untrimmed record in the shard. This is the oldest record in the shard.

      1. For **Batch size - optional**, enter a maximum number of records for each batch. The default value is 100.

      1. For **Batch window - optional**, enter a maximum number of seconds to gather records before proceeding.

------
#### [ Amazon SQS ]

**To configure an Amazon SQS source by using the console**

   1. For **Source**, choose **SQS**.

   1. For **SQS queue**, choose the queue you want to use.

   1. (Optional) For **Additional setting - optional**, do the following:

      1. For **Batch size - optional**, enter a maximum number of records for each batch. The default value is 100.

      1. For **Batch window - optional**, enter a maximum number of seconds to gather records before proceeding.

------

## Configuring event filtering (optional)
<a name="pipes-configure-filtering"></a>

You can add filtering to your pipe so you’re sending only a subset of events from your source to the target.

**To configure filtering by using the console**

1. Choose **Filtering**.

1. Under **Sample event - optional**, you’ll see a sample event that you can use to build your event pattern, or you can enter your own event by choosing **Enter your own**.

1. Under **Event pattern**, enter the event pattern that you want to use to filter the events. For more information about constructing filters, see [Event filtering in Amazon EventBridge Pipes](eb-pipes-event-filtering.md).

   The following is an example event pattern that only sends events with the value **Seattle** in the **City** field.

   ```
   {
     "data": {
       "City": ["Seattle"]
     }
   }
   ```

Now that events are being filtered, you can add optional enrichment and a target for the pipe.

## Defining event enrichment (optional)
<a name="pipes-define-enrichment"></a>

You can send the event data for enrichment to a Lambda function, AWS Step Functions state machine, Amazon API Gateway, or API destination.

**To select enrichment**

1. Choose **Enrichment**.

1. Under **Details**, for **Service**, select the service and related settings you want to use for enrichment.

You can also transform the data before sending it to be enhanced.

**(Optional) To define the input transformer**

1. Choose **Enrichment Input Transformer - optional**.

1. For **Sample events/Event Payload**, choose the sample event type.

1. For **Transformer**, enter the transformer syntax, such as `"Event happened at <$.detail.field>."` where `<$.detail.field>` is a reference to a field from the sample event. You can also double-click a field from the sample event to add it to the transformer.

1. For **Output**, verify that the output looks like you want it to.

Now that the data has been filtered and enhanced, you must define a target to send the event data to.

## Configuring a target
<a name="pipes-configure-target"></a>

**To configure a target**

1. Choose **Target**.

1. Under **Details**, for **Target service**, choose the target. The fields that display vary depending on the target that you choose. Enter information specific to this target type, as needed.

You can also transform the data before sending it to the target.

**(Optional) To define the input transformer**

1. Choose **Target Input Transformer - optional**.

1. For **Sample events/Event Payload**, choose the sample event type.

1. For **Transformer**, enter the transformer syntax, such as `"Event happened at <$.detail.field>."` where `<$.detail.field>` is a reference to a field from the sample event. You can also double-click a field from the sample event to add it to the transformer.

1. For **Output**, verify that the output looks like you want it to.

Now that the pipe is configured, make sure that its settings are configured correctly.

## Configuring the pipe settings
<a name="pipes-configure-pipe-settings"></a>

A pipe is active by default, but you can deactivate it. You can also specify the permissions of the pipe, set up pipe logging, and add tags.

**To configure the pipe settings**

1. Choose the **Pipe settings** tab.

1. By default, newly created pipes are active as soon as they're created. If you want to create an inactive pipe, under **Activation**, for **Activate pipe**, turn off **Active**.

1. Under **Permissions**, for **Execution role**, do one of the following:

   1. To have EventBridge create a new execution role for this pipe, choose **Create a new role for this specific resource.** Under **Role name**, you can optionally edit the role name.

   1. To use an existing execution role, choose **Use existing role**. Under **Role name**, choose the role.
**Role manager enabled**  
If role manager is enabled in your account, EventBridge attaches the role for you. EventBridge replaces the **Create a new role for this specific resource** and **Use existing role** options with a **Customize** option. To use a different role, choose **Customize**. For more information, see [IAM role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

1. (Optional) If you have specified a Kinesis or DynamoDB stream as the pipe source, you can configure a retry policy and dead-letter queue (DLQ).

   For **Retry policy and Dead-letter queue - optional**, do the following:

   Under **Retry policy**, do the following:

   1. If you want to turn on retry policies, turn on **Retry**. By default, newly created pipes don't have a retry policy turned on. 

   1. For **Maximum age of event**, enter a value between one minute (00:01) and 24 hours (24:00).

   1. For **Retry attempts**, enter a number between 0 and 185.

   1. If you want to use a dead-letter queue (DLQ), turn on **Dead-letter queue**, choose the method of your choice, and choose the queue or topic you'd like to use. By default, newly created pipes don't use a DLQ. 

1. Choose the KMS key for EventBridge to use when encrypting pipe data.

   For more information on how EventBridge uses KMS keys, see [Encryption at rest](eb-data-protection.md#eb-encryption-at-rest).
   + Choose **Use AWS owned key** for EventBridge to encrypt the data using an AWS owned key.

     This AWS owned key is a KMS key that EventBridge owns and manages for use in multiple AWS accounts. In general, unless you are required to audit or control the encryption key that protects your resources, an AWS owned key is a good choice. 

     This is the default.
   + Choose **Use customer managed key** for EventBridge to encrypt the data using the customer managed key that you specify or create.

     Customer managed keys are KMS keys in your AWS account that you create, own, and manage. You have full control over these KMS keys.

     1. Specify an existing customer managed key, or choose **Create a new KMS key**.

       EventBridge displays the key status and any key aliases that have been associated with the specified customer managed key.

1. (Optional) Under **Logs - optional**, you can set up how EventBridge Pipes sends logging information to supported services, including how to configure those logs. 

   For more information about logging pipe records, see [Logging Amazon EventBridge Pipes performance](eb-pipes-logs.md).

   CloudWatch logs is selected as a log destination by default, as is the `ERROR` log level. So, by default, EventBridge Pipes creates a new CloudWatch log group to which it sends log records containing the `ERROR` level of detail.

   To have EventBridge Pipes send log records to any of the supported log destinations, do the following: 

   1. Under **Logs - optional**, choose the destinations to which you want log records delivered.

   1. For **Log level**, choose the level of information for EventBridge to include in log records. The `ERROR` log level is selected by default.

      For more information, see [Specifying EventBridge Pipes log level](eb-pipes-logs.md#eb-pipes-logs-level).

   1. Select **Include execution data** if you want EventBridge to include event payload information and service request and response information in log records.

      For more information, see [Including execution data in EventBridge Pipes logs](eb-pipes-logs.md#eb-pipes-logs-execution-data).

   1. Configure each log destination you selected:

      For CloudWatch Logs logs, under **CloudWatch logs** do the following:
      + For **CloudWatch log group**, choose whether to have EventBridge create a new log group, or you can select an existing log group or specifying the ARN of an existing log group.
      + For new log groups, edit the log group name as desired.

      CloudWatch logs is selected by default.

      For Firehose stream logs, under **Firehose stream log**, select the Firehose stream. 

      For Amazon S3 logs, under **S3 logs** do the following:
      + Enter the name of the bucket to use as the log destination.
      + Enter the AWS account ID of the bucket owner.
      + Enter any prefix text you want used when EventBridge creates S3 objects.

        For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide*.
      + Choose how you want EventBridge to format S3 log records:
        + `json`: JSON 
        + `plain`: Plain text
        + `w3c`: [W3C extended logging file format](https://www.w3.org/TR/WD-logfile)

1. (Optional) Under **Tags - optional**, choose **Add new tag** and enter one or more tags for the rule. For more information, see [Tagging resources in Amazon EventBridge](eb-tagging.md).

1. Choose **Create pipe**.

## Validating configuration parameters
<a name="pipes-validation"></a>

After a pipe is created, EventBridge validates the following configuration parameters:
+ **IAM role** – Because the source of a pipe can't be changed after the pipe is created, EventBridge verifies that the provided IAM role can access the source.
**Note**  
EventBridge doesn't perform the same validation for enrichments or targets because they can be updated after the pipe is created.
+ **Batching** – EventBridge validates that the batch size of the source doesn't exceed the maximum batch size of the target. If it does, EventBridge requires a lower batch size. Additionally, if a target doesn't support batching, you can't configure batching in EventBridge for the source.
+ **Enrichments** – EventBridge validates that the batch size for API Gateway and API destination enrichments is 1 because only batch sizes of 1 are supported.