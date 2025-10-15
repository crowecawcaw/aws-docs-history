# Enabling CloudTrail event logging for
 S3 buckets and objects

You can use CloudTrail data events to get information about bucket and object-level
 requests in Amazon S3. To enable CloudTrail data events for all of your buckets or for a list
 of specific buckets, you must [create a trail manually in CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html"). 

###### Note


* The default setting for CloudTrail is to find only management events. Check
 to ensure that you have the data events enabled for your account.
* With an S3 bucket that is generating a high workload, you could
 quickly generate thousands of logs in a short amount of time. Be mindful
 of how long you choose to enable CloudTrail data events for a busy bucket.
 CloudTrail stores Amazon S3 data event logs in an S3 bucket of your choosing. Consider using
 a bucket in a separate AWS account to better organize events from multiple buckets
 that you might own into a central place for easier querying and analysis. AWS Organizations
 helps you create an AWS account that is linked to the account that owns the bucket
 that you're monitoring. For more information, see [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html") in the
 *AWS Organizations User Guide*.

When you log data events for a trail in CloudTrail, you can choose to use advanced event
 selectors or basic event selectors to log data events for objects stored in general
 purpose buckets. To log data events for objects stored in directory buckets, you
 must use advanced event selectors. For more information, see  [Logging with AWS CloudTrail for S3 Express One Zone](s3-express-one-zone-logging.md "s3-express-one-zone-logging.md").

When you create a trail in the CloudTrail console using advanced event selectors, in the
 data events section, you can choose **Log all events** for the
 **Log selector template** to log all object-level events. When
 you create a trail in the CloudTrail console using basic event selectors, in the
 data events section, you can select the **Select all S3 buckets in your
 account** check box to log all object-level events. 

###### Note


* It's a best practice to create a lifecycle configuration for your
 AWS CloudTrail data event bucket. Configure the lifecycle configuration to
 periodically remove log files after the period of time you believe you
 need to audit them. Doing so reduces the amount of data that Athena
 analyzes for each query. For more information, see [Setting an S3 Lifecycle configuration on a
 bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").
* For more information about logging format, see [Logging Amazon S3 API calls using AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md").
* For examples of how to query CloudTrail logs, see the *AWS Big Data Blog* post [Analyze Security, Compliance, and Operational Activity Using
 AWS CloudTrail and Amazon Athena](https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/ "https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/").

## Enable logging for objects in a bucket using the
 console


You can use the AWS CloudTrail console to configure a CloudTrail trail to log data events for objects in
 an S3 bucket. CloudTrail supports logging Amazon S3 object-level API operations such as
 `GetObject`, `DeleteObject`, and `PutObject`. These events
 are called *data events*. 


By default, CloudTrail trails don't log data events, but you can configure trails to log data
 events for S3 buckets that you specify, or to log data events for all the Amazon S3 buckets in your
 AWS account. For more information, see [Logging Amazon S3 API calls using AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md"). 


CloudTrail does not populate data events in the CloudTrail event history. Additionally, not all
 bucket-level actions are populated in the CloudTrail event history. For more information about the
 Amazon S3 bucket–level API actions tracked by CloudTrail logging, see [Amazon S3 bucket-level actions
 that are tracked by CloudTrail logging](cloudtrail-logging-s3-info.md#cloudtrail-bucket-level-tracking "cloudtrail-logging-s3-info.md#cloudtrail-bucket-level-tracking").
 For more information about how to query CloudTrail logs, see the AWS Knowledge Center article about
 [using
 Amazon CloudWatch Logs filter patterns and Amazon Athena to query CloudTrail logs](https://aws.amazon.com/premiumsupport/knowledge-center/find-cloudtrail-object-level-events/ "https://aws.amazon.com/premiumsupport/knowledge-center/find-cloudtrail-object-level-events/").


###### Note

If you are logging data activity with AWS CloudTrail, the event record for an Amazon S3
 `DeleteObjects` data event includes both the `DeleteObjects` event and
 a `DeleteObject` event for each object deleted as part of that operation. You can
 exclude the additional visibility about deleted objects from the event record. For more
 information, see [AWS CLI examples for filtering data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/filtering-data-events.html#filtering-data-events-deleteobjects "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/filtering-data-events.html#filtering-data-events-deleteobjects") in the *AWS CloudTrail
 User Guide*.


To enable CloudTrail data events logging for objects in an S3 general purpose bucket or an S3
 directory bucket see [Creating a trail with the CloudTrail console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time") in the
 *AWS CloudTrail User Guide*.


For more information about logging objects in an S3 directory bucket, see [Logging with AWS CloudTrail for directory buckets](s3-express-one-zone-logging.md "s3-express-one-zone-logging.md").


For information about using the CloudTrail console to configure a trail to log S3 data events, see
 [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html") in the *AWS CloudTrail User Guide*. 


To disable CloudTrail data events logging for objects in an S3 bucket, see [Deleting a trail with the CloudTrail console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delete-trails-console.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delete-trails-console.html") in the
 *AWS CloudTrail User Guide*. 


###### Important

Additional charges apply for data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). 


For more information about CloudTrail logging with S3 buckets, see the following topics:



* [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md")
* [Viewing the properties for an S3 general purpose bucket](view-bucket-properties.md "view-bucket-properties.md")
* [Logging Amazon S3 API calls using AWS CloudTrail](cloudtrail-logging.md "cloudtrail-logging.md")
* [Working with CloudTrail log
 files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.html") in the *AWS CloudTrail User Guide*
