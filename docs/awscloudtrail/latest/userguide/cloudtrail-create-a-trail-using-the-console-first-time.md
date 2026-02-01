# Creating a trail with the CloudTrail console

A trail can be applied to all AWS Regions that are [enabled](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone") in your AWS account, or can be applied to a single Region. A trail that applies to
all AWS Regions that are enabled in your AWS account is referred to as a _multi-Region trail_. As a best practice, we recommend creating
a multi-Region trail because it captures activity in all enabled Regions. All trails created using the CloudTrail console are multi-Region trails. You can only create a single-Region trail using the AWS CLI or
[`CreateTrail`](../APIReference/API_CreateTrail.md "../APIReference/API_CreateTrail.md") API operation.

###### Note

After you create a trail, you can configure other AWS services to further analyze
and act upon the event data collected in CloudTrail logs. For more information, see [AWS service integrations with CloudTrail logs](cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations").

###### Topics

- [Creating a trail with the console](#creating-a-trail-in-the-console "#creating-a-trail-in-the-console")
- [Next steps](#cloudtrail-create-a-trail-using-the-console-first-time-next-steps "#cloudtrail-create-a-trail-using-the-console-first-time-next-steps")

## Creating a trail with the console

Use the following procedure to create a multi-Region trail. To log events in a single Region (not recommended),
[use the AWS CLI](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-single "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-single").

###### To create a CloudTrail trail with the AWS Management Console

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. On the CloudTrail service home page, the **Trails** page, or
   the **Trails** section of the
   **Dashboard** page, choose **Create
   trail**.
3. On the **Create Trail** page, for **Trail
   name**, type a name for your trail. For more information, see
   [Naming requirements for CloudTrail resources, S3 buckets, and KMS keys](cloudtrail-trail-naming-requirements.md "cloudtrail-trail-naming-requirements.md").
4. If this is an AWS Organizations organization trail, you can enable the trail for
   all accounts in your organization. To see this option, you must sign in to the
   console with a user or role in the management or delegated administrator
   account. To successfully create an organization trail, be sure that the user or
   role has [sufficient permissions](creating-an-organizational-trail-prepare.md#org_trail_permissions "creating-an-organizational-trail-prepare.md#org_trail_permissions").
   For more information, see [Creating a trail for an organization](creating-trail-organization.md "creating-trail-organization.md").
5. For **Storage location**, choose **Create new S3
   bucket** to create a bucket. When you create a bucket, CloudTrail
   creates and applies the required bucket policies. If you choose to create
   a new S3 bucket, your IAM policy needs to include permission for the
   `s3:PutEncryptionConfiguration` action because by
   default server-side encryption is enabled for the bucket.

###### Note

If you chose **Use existing S3 bucket**, specify a
bucket in **Trail log bucket name**, or choose
**Browse** to choose a bucket in your own account.
If you want to use a bucket in another account, you'll need to specify the bucket name. The bucket policy
must grant CloudTrail permission to write to it. For information about
manually editing the bucket policy, see [Amazon S3 bucket policy for CloudTrail](create-s3-bucket-policy-for-cloudtrail.md "create-s3-bucket-policy-for-cloudtrail.md").

To make it easier to find your logs, create a new folder (also known as a
_prefix_) in an existing bucket to
store your CloudTrail logs. Enter the prefix in
**Prefix**. 6. For **Log file SSE-KMS encryption**, choose
**Enabled** if you want to encrypt your log files and digest files using
SSE-KMS encryption instead of SSE-S3 encryption. The default is **Enabled**. If you don't enable SSE-KMS encryption,
your log files and digest files are encrypted using SSE-S3 encryption. For
more information about SSE-KMS encryption, see [Using server-side encryption with AWS Key Management Service (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md"). For
more information about SSE-S3 encryption, see [Using Server-Side Encryption with
Amazon S3-Managed Encryption Keys (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md").

If you enable SSE-KMS encryption, choose a **New** or
**Existing** AWS KMS key. In
**AWS KMS Alias**, specify an alias, in the format
`alias/``MyAliasName`. For more
information, see [Updating a resource to
use your KMS key with the console](create-kms-key-policy-for-cloudtrail-update-trail.md "create-kms-key-policy-for-cloudtrail-update-trail.md").
CloudTrail also supports AWS KMS multi-Region keys. For more information about
multi-Region keys, see [Using
multi-Region keys](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") in the _AWS Key Management Service
Developer Guide_.

###### Note

You can also type the ARN of a key from another account. For more
information, see [Updating a resource to
use your KMS key with the console](create-kms-key-policy-for-cloudtrail-update-trail.md "create-kms-key-policy-for-cloudtrail-update-trail.md").
The key policy must allow CloudTrail to use the key to encrypt your log files and digest files,
and allow the users you specify to read log files or digest files in unencrypted form.
For information about manually editing the key policy, see [Configure AWS KMS key policies for CloudTrail](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md"). 7. In **Additional settings**, configure the
following.

    1. For **Log file validation**, choose
     **Enabled** to have log digests delivered to
     your S3 bucket. You can use the digest files to verify that your log
     files did not change after CloudTrail delivered them. For more
     information, see [Validating CloudTrail log file integrity](cloudtrail-log-file-validation-intro.md "cloudtrail-log-file-validation-intro.md").
    2. For **SNS notification delivery**, choose
     **Enabled** to be notified each time a log is
     delivered to your bucket. CloudTrail stores multiple events in a log file.
     SNS notifications are sent for every log file, not for every event.
     For more information, see [Configuring Amazon SNS notifications for CloudTrail](configure-sns-notifications-for-cloudtrail.md "configure-sns-notifications-for-cloudtrail.md").


    If you enable SNS notifications, for **Create a new SNS
     topic**, choose **New** to create a
     topic, or choose **Existing** to use an existing
     topic. If you are creating a multi-Region trail, SNS
     notifications for log file deliveries from all enabled Regions are sent to
     the single SNS topic that you create.


    If you choose **New**, CloudTrail specifies a name for
     the new topic for you, or you can type a name. If you choose
     **Existing**, choose an SNS topic from the
     drop-down list. You can also enter the ARN of a topic from another
     Region or from an account with appropriate permissions. For more
     information, see [Amazon SNS topic policy for CloudTrail](cloudtrail-permissions-for-sns-notifications.md "cloudtrail-permissions-for-sns-notifications.md").


    If you create a topic, you must subscribe to the topic to be
     notified of log file delivery. You can subscribe from the Amazon SNS
     console. Due to the frequency of notifications, we recommend that
     you configure the subscription to use an Amazon SQS queue to handle
     notifications programmatically. For more information, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the *Amazon Simple Notification Service Developer Guide*.

8.  Optionally, configure CloudTrail to send log files to CloudWatch Logs by choosing
    **Enabled** in **CloudWatch Logs**. For more
    information, see [Sending events to CloudWatch Logs](send-cloudtrail-events-to-cloudwatch-logs.md "send-cloudtrail-events-to-cloudwatch-logs.md").
    1. If you enable integration with CloudWatch Logs, choose
       **New** to create a new log group, or
       **Existing** to use an existing one. If you
       choose **New**, CloudTrail specifies a name for the new
       log group for you, or you can type a name.
    2. If you choose **Existing**, choose a log group
       from the drop-down list.
    3. Choose **New** to create a new IAM role for
       permissions to send logs to CloudWatch Logs. Choose
       **Existing** to choose an existing IAM role
       from the drop-down list. The policy statement for the new or
       existing role is displayed when you expand **Policy
       document**. For more information about this role, see
       [Role policy document for CloudTrail to use CloudWatch Logs for monitoring](cloudtrail-required-policy-for-cloudwatch-logs.md "cloudtrail-required-policy-for-cloudwatch-logs.md").

    ###### Note

        * When you configure a trail, you can choose an S3 bucket and
         SNS topic that belong to another account. However, if you want
         CloudTrail to deliver events to a CloudWatch Logs log group, you must choose a
         log group that exists in your current account.
        * Only the management account can configure
         a CloudWatch Logs log group for an organization trail using the console. The delegated administrator can configure a CloudWatch Logs
         log group using the AWS CLI or CloudTrail `CreateTrail` or `UpdateTrail` API operations.

9.  For **Tags**, you can add up to 50 tag key pairs to help
    you identify, sort, and control access to your trail. Tags can help you identify both your CloudTrail trails and
    the Amazon S3 buckets that contain CloudTrail log files. You can then use resource
    groups for your CloudTrail resources. For more information, see [AWS Resource Groups](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md") and [Tags](cloudtrail-concepts.md#cloudtrail-concepts-tags "cloudtrail-concepts.md#cloudtrail-concepts-tags").
10. On the **Choose log events** page, choose the event types
    that you want to log. For **Management events**, do the
    following.
    1. For **API activity**, choose if you want your
       trail to log **Read** events,
       **Write** events, or both. For more
       information, see [Management events](logging-management-events-with-cloudtrail.md#logging-management-events "logging-management-events-with-cloudtrail.md#logging-management-events").
    2. Choose **Exclude AWS KMS events** to filter
       AWS Key Management Service (AWS KMS) events out of your trail. The default setting is
       to include all AWS KMS events.

    The option to log or exclude AWS KMS events is available only if you
    log management events on your trail. If you choose not to log
    management events, AWS KMS events are not logged, and you cannot
    change AWS KMS event logging settings.

    AWS KMS actions such as `Encrypt`, `Decrypt`,
    and `GenerateDataKey` typically generate a large volume
    (more than 99%) of events. These actions are now logged as
    **Read** events. Low-volume, relevant AWS KMS
    actions such as `Disable`, `Delete`, and
    `ScheduleKey` (which typically account for less than
    0.5% of AWS KMS event volume) are logged as **Write**
    events.

    To exclude high-volume events like `Encrypt`,
    `Decrypt`, and `GenerateDataKey`, but
    still log relevant events such as `Disable`,
    `Delete` and `ScheduleKey`, choose to log
    **Write** management events, and clear the
    check box for **Exclude AWS KMS events**. 3. Choose **Exclude Amazon RDS Data API events** to
    filter Amazon Relational Database Service Data API events out of your trail. The default
    setting is to include all Amazon RDS Data API events. For more
    information about Amazon RDS Data API events, see [Logging Data API calls with
    AWS CloudTrail](../../../AmazonRDS/latest/AuroraUserGuide/logging-using-cloudtrail-data-api.md "../../../AmazonRDS/latest/AuroraUserGuide/logging-using-cloudtrail-data-api.md") in the _Amazon RDS User Guide for
    Aurora_.

11. To log data events, choose **Data events**. Additional
    charges apply for logging data events. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").
12. ###### Important

Steps 12-16 are for configuring data events using advanced event
selectors, which is the default. Advanced event selectors let you configure
more [resource types](logging-data-events-with-cloudtrail.md#logging-data-events "logging-data-events-with-cloudtrail.md#logging-data-events") and offer fine-grained control over which data events your
trail captures. If you opted to use basic event selectors, complete the steps in [Configure data event settings using basic event selectors](#trail-data-events-basic-selectors "#trail-data-events-basic-selectors"), then return to step
17 of this procedure.

For **Resource type**, choose the resource type on
which you want to log data events. For more information about available resource types, see [Data events](logging-data-events-with-cloudtrail.md#logging-data-events "logging-data-events-with-cloudtrail.md#logging-data-events"). 13. Choose a log selector template. You can choose a predefined template, or choose **Custom**
to define your own event collection conditions.

You can choose from the following predefined
templates:

    * **Log all events** –
     Choose this template to log all events.
    * **Log only read events** –
     Choose this template to log only read events.
     Read-only events are events that do not change the
     state of a resource, such as `Get*` or `Describe*`
     events.
    * **Log only write events** – Choose this template to log only write events.
     Write events add, change, or delete resources, attributes, or artifacts,
     such as `Put*`, `Delete*`, or `Write*` events.
    * **Log only AWS Management Console events** –
     Choose this template to log only events originating from the AWS Management Console.
    * **Exclude AWS service initiated events** – Choose this template to exclude
     AWS service events, which have an `eventType` of `AwsServiceEvent`,
     and events initiated with AWS service-linked roles (SLRs).

###### Note

Choosing a predefined template for S3 buckets enables data event
logging for all buckets currently in your AWS account and any buckets
you create after you finish creating the trail. It also enables logging
of data event activity performed by any IAM identity in your AWS
account, even if that activity is performed on a bucket that belongs to
another AWS account.

If the trail applies only to one Region, choosing a predefined
template that logs all S3 buckets enables data event logging for all
buckets in the same Region as your trail and any buckets you create
later in that Region. It will not log data events for Amazon S3 buckets in
other Regions in your AWS account.

If you are creating a multi-Region trail choosing a predefined
template for Lambda functions enables data event logging for all
functions currently in your AWS account, and any Lambda functions you
might create in any Region after you finish creating the trail. If you
are creating a trail for a single Region (done by using the AWS CLI), this
selection enables data event logging for all functions currently in that
Region in your AWS account, and any Lambda functions you might create
in that Region after you finish creating the trail. It does not enable
data event logging for Lambda functions created in other Regions.

Logging data events for all functions also enables logging of data
event activity performed by any IAM identity in your AWS account, even
if that activity is performed on a function that belongs to another
AWS account. 14. (Optional) In **Selector name**, enter a name to identify your selector. The selector name is a
descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets". The selector name is listed as `Name` in the
advanced event selector and is viewable if you expand the
**JSON view**. 15. If you selected **Custom**, in **Advanced event selectors** build an expression based on the values of advanced event selector fields.

###### Note

Selectors don't support the use of wildcards like `*` . To match multiple values with a single condition,
you may use `StartsWith`, `EndsWith`, `NotStartsWith`, or `NotEndsWith` to explicitly match the beginning or end of the event field.

    1. Choose from the following fields.




    	* **`readOnly`**
    	 - `readOnly` can be set to
    	 **equals** a value of
    	 `true` or `false`. Read-only
    	 data events are events that do not change the state of a
    	 resource, such as `Get*` or
    	 `Describe*` events. Write events add,
    	 change, or delete resources, attributes, or artifacts,
    	 such as `Put*`, `Delete*`, or
    	 `Write*` events. To log both
    	 `read` and `write` events,
    	 don't add a `readOnly` selector.
    	* **`eventName`** -
    	 `eventName` can use any operator. You can
    	 use it to include or exclude any data event logged to
    	 CloudTrail, such as `PutBucket`,
    	 `GetItem`, or
    	 `GetSnapshotBlock`.
    	* **`eventSource`** – The event source to include or exclude. This field can use any operator.
    	* **eventType** – The event type to include or exclude. For example, you can set this field to
    	 **not equals** `AwsServiceEvent` to exclude
    	 [AWS service events](non-api-aws-service-events.md "non-api-aws-service-events.md"). For a list of event types,
    	 see [eventType](cloudtrail-event-reference-record-contents.md#ct-event-type "cloudtrail-event-reference-record-contents.md#ct-event-type") in
    	 [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").
    	* **sessionCredentialFromConsole** – Include or exclude events originating from an AWS Management Console session. This field can be set to **equals** or **not equals** with a value of
    	 `true`.
    	* **userIdentity.arn** – Include or exclude events for actions taken by specific IAM identities. For more information, see [CloudTrail userIdentity element](cloudtrail-event-reference-user-identity.md "cloudtrail-event-reference-user-identity.md").
    	* **`resources.ARN`** - You can use
    	 any operator with `resources.ARN`, but if you
    	 use **equals** or
    	 **does not equal**, the value must
    	 exactly match the ARN of a valid resource of the type
    	 you've specified in the template as the value of
    	 `resources.type`.


    	###### Note

    	You can't use the `resources.ARN` field to filter resource types that do not have ARNs.


    	For more information about the ARN formats of data event
    	 resources, see [Actions, resources, and condition
    	 keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") in the *Service Authorization Reference*.
    2. For each field, choose **+ Condition** to
     add as many conditions as you need, up to a maximum of 500
     specified values for all conditions. For example, to exclude
     data events for two S3 buckets from data events that are logged
     on your event data store, you can set the field to
     **resources.ARN**, set the operator for
     **does not start with**, and then paste in
     an S3 bucket ARN for which you do
     not want to log events.


    To add the second S3 bucket, choose **+
     Condition**, and then repeat the preceding
     instruction, pasting in the ARN for or browsing for a different
     bucket.


    For information about how CloudTrail evaluates multiple conditions, see
     [How CloudTrail evaluates multiple conditions for a field](filtering-data-events.md#filtering-data-events-conditions "filtering-data-events.md#filtering-data-events-conditions").


    ###### Note

    You can have a maximum of 500 values for all selectors on
     an event data store. This includes arrays of multiple values for a
     selector such as `eventName`. If you have single
     values for all selectors, you can have a maximum of 500
     conditions added to a selector.
    3. Choose **+ Field** to add additional fields
     as required. To avoid errors, do not set conflicting or
     duplicate values for fields. For example, do not specify an ARN
     in one selector to be equal to a value, then specify that the
     ARN not equal the same value in another selector.

16. To add another resource type on which to log data events, choose **Add
    data event type**. Repeat steps 12 through this step to configure
    advanced event selectors for the resource type.
17. To enable aggregation on data events, choose one or more aggregation templates. These templates define how your data events will be summarized. You can choose from the following templates:
    1.  **API Activity** to get 5-minute summaries of your data events based on the API calls made. Use this to understand your API usage patterns, including frequency, callers, and source.
    2.  **Resource Access** to get the activity patterns on your AWS resources. Use this to understand how your AWS resources are being accessed, how many times they are being accessed in the 5-minute window, who is accessing the resource, and what actions are being performed.
    3.  **User Actions** to get activity patterns based on IAM principals making API calls in your account.###### Note

Aggregations apply to all data events collected in your trail. 18. To log network activity events, choose **Network activity events**.
Network activity events enable VPC endpoint owners to record AWS API calls made using their VPC endpoints from a private VPC to the AWS service. Additional charges apply
for logging network activity events. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

To log network activity events, do the following:

    1. From **Network activity event source**, choose the source for network activity events.
    2. In **Log selector template**, choose a template.
     You can choose to log all network activity events, log all network activity access denied events, or choose **Custom** to
     build a custom log selector to filter on multiple fields, such as `eventName` and `vpcEndpointId`.
    3. (Optional) Enter a name to identify the selector. The selector name is listed as **Name** in the advanced event selector and is viewable if you expand the
     **JSON view**.
    4. In **Advanced event
     selectors** build expressions by choosing values for **Field**,
     **Operator**, and **Value**. You can skip this step if you are using a predefined log template.


    	1. For excluding or including network activity
    	 events, you can choose from the following fields in the console.




    		* **`eventName`** – You can use any operator with `eventName`.
    		 You can use it to include or exclude any event, such as `CreateKey`.
    		* **`errorCode`** – You can use it to filter on an error code. Currently, the only supported `errorCode` is `VpceAccessDenied`.
    		* **`vpcEndpointId`** – Identifies the VPC endpoint that the operation passed through. You can use
    		 any operator with `vpcEndpointId`.
    	2. For each field, choose **+ Condition** to add as many conditions as you need, up to a maximum of 500 specified values for all conditions.
    	3. Choose **+ Field** to add additional fields as required. To avoid errors, do not set conflicting or duplicate values for fields.
    5. To add another event source for which you want to log network activity events, choose **Add
     network activity event selector**.
    6. Optionally, expand **JSON view** to see your
     advanced event selectors as a JSON block.

19. Choose **Insights events** if you want your trail to log CloudTrail
    Insights events.

In **Event type**, select **Insights
events**. You must be logging **Write** management events to
log Insights events for **API call rate**. You must be logging
**Read** or **Write** management events to
log Insights events for **API error rate**.

CloudTrail Insights analyzes management events for
unusual activity, and logs events when anomalies are detected. By default,
trails don't log Insights events. For more information about Insights events,
see [Working with CloudTrail Insights](logging-insights-events-with-cloudtrail.md "logging-insights-events-with-cloudtrail.md"). Additional
charges apply for logging Insights events. For CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

Insights events are delivered to a different folder named
`/CloudTrail-Insight`of the same S3 bucket that is specified in
the **Storage location** area of the trail details page. CloudTrail
creates the new prefix for you. For example, if your current destination S3
bucket is named `amzn-s3-demo-bucket/AWSLogs/CloudTrail/`, the S3 bucket
name with a new prefix is named
`amzn-s3-demo-bucket/AWSLogs/CloudTrail-Insight/`. 20. When you are finished choosing event types to log, choose
**Next**. 21. On the **Review and create** page, review your choices.
Choose **Edit** in a section to change the trail settings
shown in that section. When you are ready to create the trail, choose
**Create trail**. 22. The new trail appears on the **Trails** page. In about 5 minutes,
CloudTrail publishes log files that show the
AWS API calls made in your account. You can see the log files in the S3
bucket that you specified.

If you enabled Insights events for a trail,
CloudTrail may take up to 36 hours to begin delivering these events,
provided that unusual activity is detected during that time.

###### Note

CloudTrail typically delivers logs within an average of about 5 minutes of an
API call. This time is not guaranteed. Review the [AWS CloudTrail Service Level Agreement](https://aws.amazon.com/cloudtrail/sla "https://aws.amazon.com/cloudtrail/sla") for more
information.

If you misconfigure your trail (for example, the S3 bucket is unreachable),
CloudTrail will attempt to redeliver the log files to your S3 bucket for 30 days, and
these attempted-to-deliver events will be subject to standard CloudTrail charges.
To avoid charges on a misconfigured trail, you need to delete the trail.

### Configure data event settings using basic event selectors

You can use advanced event selectors to configure all data event types as well as network activity events.

Advanced event selectors allow you to create
fine-grained selectors to log only those events of interest.

If you use basic event selectors to log data events, you're limited
to logging data events for Amazon S3 buckets, AWS Lambda functions, and Amazon DynamoDB tables.
You can't filter on the `eventName` field using basic event
selectors. You also can't log [network activity events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md").

![Basic event selectors for data events on a trail](/images/awscloudtrail/latest/userguide/images/cloudtrail-data-basic-selectors.png)

Use the following procedure to configure data event settings using basic event selectors.

###### To configure data event settings using basic event selectors

1. In **Events**, choose **Data events** to log data events. Additional
   charges apply for logging data events. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").
2. For Amazon S3 buckets:
   1. For **Data event source**, choose
      **S3**.
   2. You can choose to log **All current and future S3
      buckets**, or you can specify individual buckets or
      functions. By default, data events are logged for all current and
      future S3 buckets.

   ###### Note

   Keeping the default **All current and future S3
   buckets** option enables data event logging for all
   buckets currently in your AWS account and any buckets you
   create after you finish creating the trail. It also enables
   logging of data event activity performed by any IAM identity in
   your AWS account, even if that activity is performed on a
   bucket that belongs to another AWS account.

   If you are creating a trail for a single Region (done by using
   the AWS CLI), choosing **All current and future S3
   buckets** enables data event logging for all
   buckets in the same Region as your trail and any buckets you
   create later in that Region. It will not log data events for
   Amazon S3 buckets in other Regions in your AWS account. 3. If you leave the default, **All current and future S3
   buckets**, choose to log **Read**
   events, **Write** events, or both. 4. To select individual buckets, empty the **Read**
   and **Write** check boxes for **All current
   and future S3 buckets**. In **Individual bucket
   selection**, browse for a bucket on which to log data
   events. Find specific buckets by typing a bucket prefix for the
   bucket you want. You can select multiple buckets in this window.
   Choose **Add bucket** to log data events for more
   buckets. Choose to log **Read** events, such as
   `GetObject`, **Write** events, such
   as `PutObject`, or both.

   This setting takes precedence over individual settings you
   configure for individual buckets. For example, if you specify
   logging **Read** events for all S3 buckets, and
   then choose to add a specific bucket for data event logging,
   **Read** is already selected for the bucket you
   added. You cannot clear the selection. You can only configure the
   option for **Write**.

   To remove a bucket from logging, choose
   **X**.

3. To add another resource type on which to log data events, choose **Add
   data event type**.
4. For Lambda functions:
   1. For **Data event source**, choose
      **Lambda**.
   2. In **Lambda function**, choose **All
      regions** to log all Lambda functions, or
      **Input function as ARN** to log data events on
      a specific function.

   To log data events for all Lambda functions in your AWS account,
   select **Log all current and future functions**.
   This setting takes precedence over individual settings you configure
   for individual functions. All functions are logged, even if all
   functions are not displayed.

   ###### Note

   If you're creating a multi-Region trail, this selection
   enables data event logging for all functions currently in your
   AWS account, and any Lambda functions you might create in any
   Region after you finish creating the trail. If you are creating
   a trail for a single Region (done by using the AWS CLI), this
   selection enables data event logging for all functions currently
   in that Region in your AWS account, and any Lambda functions
   you might create in that Region after you finish creating the
   trail. It does not enable data event logging for Lambda functions
   created in other Regions.

   Logging data events for all functions also enables logging of
   data event activity performed by any IAM identity in your AWS
   account, even if that activity is performed on a function that
   belongs to another AWS account. 3. If you choose **Input function as ARN**, enter
   the ARN of a Lambda function.

   ###### Note

   If you have more than 15,000 Lambda functions in your account,
   you cannot view or select all functions in the CloudTrail console when
   creating a trail. You can still select the option to log all
   functions, even if they are not displayed. If you want to log
   data events for specific functions, you can manually add a
   function if you know its ARN. You can also finish creating the
   trail in the console, and then use the AWS CLI and the
   **put-event-selectors** command to configure
   data event logging for specific Lambda functions. For more
   information, see [Managing trails with the AWS CLI](cloudtrail-additional-cli-commands.md "cloudtrail-additional-cli-commands.md").

5. For DynamoDB tables:
   1. For **Data event source**, choose
      **DynamoDB**.
   2. In **DynamoDB table selection**, choose
      **Browse** to select a table, or paste in the
      ARN of a DynamoDB table to which you have access. A DynamoDB table ARN uses
      the following format:

   ```
   arn:`partition`:dynamodb:`region`:`account_ID`:table/`table_name`
   ```

   To add another table, choose **Add row**, and
   browse for a table or paste in the ARN of a table to which you have
   access.

6. To configure Insights events and other settings for your trail, go back to the preceding procedure in this topic, [Creating a trail with the console](#creating-a-trail-in-the-console "#creating-a-trail-in-the-console").

## Next steps

After you create your trail, you can return to the trail to make changes:

- If you haven't already, you can configure CloudTrail to send log files to CloudWatch Logs. For
  more information, see [Sending events to CloudWatch Logs](send-cloudtrail-events-to-cloudwatch-logs.md "send-cloudtrail-events-to-cloudwatch-logs.md").
- Create a table and use it to run a query in Amazon Athena to analyze your AWS
  service activity. For more information, see [Creating a
  Table for CloudTrail Logs in the CloudTrail Console](../../../athena/latest/ug/cloudtrail-logs.md#create-cloudtrail-table-ct "../../../athena/latest/ug/cloudtrail-logs.md#create-cloudtrail-table-ct") in the
  [Amazon Athena User Guide](../../../athena/latest/ug.md "../../../athena/latest/ug.md").
- Add custom tags (key-value pairs) to the trail.
- To create another trail, open the **Trails** page, and choose
  **Create trail**.
