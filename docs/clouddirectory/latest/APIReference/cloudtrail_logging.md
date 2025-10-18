Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# Logging Cloud Directory API Calls with CloudTrail

Amazon Cloud Directory is integrated with AWS CloudTrail, a service that captures all of the
 Cloud Directory API calls and delivers the log files to an Amazon S3 bucket that you specify. CloudTrail
 captures API calls from the Cloud Directory section of the AWS Directory Service console or from your code to the
 Cloud Directory APIs. Using the information collected by CloudTrail, you can determine the request that
 was made to Cloud Directory, the source IP address from which the request was made, who made the
 request, when it was made, and so on. To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Cloud Directory Information in CloudTrail


CloudTrail is enabled on your AWS account when you create the account. When supported event
 activity occurs in Cloud Directory, that activity is recorded in a CloudTrail event along with other
 AWS service events in **Event history**. You can view, search, and download
 recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
 History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md"). 


For an ongoing record of events in your AWS account, including events for Cloud Directory,
 create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. 
 By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events
 from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you
 specify. Additionally, you can configure other AWS services to further analyze and act upon
 the event data collected in CloudTrail logs. For more information, see the following: 



* [Overview for
 Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
* [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
* [Configuring Amazon SNS
 Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
* [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
 Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

When CloudTrail logging is enabled in your AWS account, API calls made to Cloud Directory
 actions are tracked in CloudTrail log files, where they are written with other AWS service
 records. CloudTrail determines when to create and write to a new file based on a time period and
 file size.


The following Cloud Directory actions are logged by CloudTrail and are documented in this API
 Reference guide. 



* [ApplySchema](API_ApplySchema.md "API_ApplySchema.md")
* [CreateDirectory](API_CreateDirectory.md "API_CreateDirectory.md")
* [CreateFacet](API_CreateFacet.md "API_CreateFacet.md")
* [CreateSchema](API_CreateSchema.md "API_CreateSchema.md")
* [DeleteDirectory](API_DeleteDirectory.md "API_DeleteDirectory.md")
* [DeleteFacet](API_DeleteFacet.md "API_DeleteFacet.md")
* [DeleteSchema](API_DeleteSchema.md "API_DeleteSchema.md")
* [DisableDirectory](API_DisableDirectory.md "API_DisableDirectory.md")
* [EnableDirectory](API_EnableDirectory.md "API_EnableDirectory.md")
* [GetDirectory](API_GetDirectory.md "API_GetDirectory.md")
* [GetFacet](API_GetFacet.md "API_GetFacet.md")
* [GetSchemaAsJson](API_GetSchemaAsJson.md "API_GetSchemaAsJson.md")
* [ListAppliedSchemaArns](API_ListAppliedSchemaArns.md "API_ListAppliedSchemaArns.md")
* [ListDevelopmentSchemaArns](API_ListDevelopmentSchemaArns.md "API_ListDevelopmentSchemaArns.md")
* [ListDirectories](API_ListDirectories.md "API_ListDirectories.md")
* [ListFacetAttributes](API_ListFacetAttributes.md "API_ListFacetAttributes.md")
* [ListFacetNames](API_ListFacetNames.md "API_ListFacetNames.md")
* [ListManagedSchemaArns](API_ListManagedSchemaArns.md "API_ListManagedSchemaArns.md")
* [ListPublishedSchemaArns](API_ListPublishedSchemaArns.md "API_ListPublishedSchemaArns.md")
* [ListTagsForResource](API_ListTagsForResource.md "API_ListTagsForResource.md")
* [PublishSchema](API_PublishSchema.md "API_PublishSchema.md")
* [PutSchemaFromJson](API_PutSchemaFromJson.md "API_PutSchemaFromJson.md")
* [TagResource](API_TagResource.md "API_TagResource.md")
* [UpdateFacet](API_UpdateFacet.md "API_UpdateFacet.md")
* [UpdateSchema](API_UpdateSchema.md "API_UpdateSchema.md")
* [UntagResource](API_UntagResource.md "API_UntagResource.md")

For example, calls to the **ApplySchema**, **ListDirectories** and **CreateSchema**
 sections generate entries in the CloudTrail log files.


Every log entry contains information about who generated the request. The user identity
 information in the log entry helps you determine the following:



* Whether the request was made with root or IAM user credentials
* Whether the request was made with temporary security credentials for a role or
 federated user
* Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").


You can store your log files in your Amazon S3 bucket for as long as you want, but you can also
 define Amazon S3 lifecycle rules to archive or delete log files automatically. By default, your log
 files are encrypted with Amazon S3 server-side encryption (SSE).


If you want to be notified upon log file delivery, you can configure CloudTrail to publish Amazon SNS
 notifications when new log files are delivered. For more information, see [Configuring Amazon SNS Notifications for
 CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md").


You can also aggregate Cloud Directory log files from multiple AWS regions and multiple
 AWS accounts into a single Amazon S3 bucket. For more information, see [Receiving CloudTrail
 Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail Log
 Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md").


## Understanding Cloud Directory Log File
 Entries


CloudTrail log files can contain one or more log entries. Each entry lists multiple
 JSON-formatted events. A log entry represents a single request from any source and includes
 information about the requested action, the date and time of the action, request parameters,
 and so on. Log entries are not an ordered stack trace of the public API calls, so they do not
 appear in any specific order.


Sensitive information, such as passwords, authentication tokens, file comments, and file
 contents are redacted in the log entries.


The following example shows a CloudTrail log entry that demonstrates the following Cloud Directory
 actions:



* `ApplySchema`
* `ListDirectories`
* `CreateSchema`


```
ApplySchema:
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "ASDFLKJHEXAMPLE1QWERT",
        "arn": "arn:aws:iam::11223Example:user/nickpi",
        "accountId": "11223Example",
        "accessKeyId": "ALSKDJFHGQPWOExample",
        "userName": "nickpi"
    },
    "eventTime": "2017-01-06T00:09:08Z",
    "eventSource": "clouddirectory.amazonaws.com",
    "eventName": "ApplySchema",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.92",
    "userAgent": "Apache-HttpClient/4.3 (java 1.5)",
    "requestParameters": {
        "directoryArn": "arn:aws:clouddirectory:us-east-1:11223Example:directory/AsCGClGIlkIqweR836u9pyU",
        "publishedSchemaArn": "arn:aws:clouddirectory:us-east-1:11223Example:schema/published/simple_org-123456/1.0"
    },
    "responseElements": {
        "directoryArn": "arn:aws:clouddirectory:us-east-1:11223Example:directory/AsCGClGIlkIqweR836u9pyU",
        "appliedSchemaArn": "arn:aws:clouddirectory:us-east-1:11223Example:directory/AsCGClGIlkIqweR836u9pyU/schema/simple_org-123456/1.0"
    },
    "requestID": "12j45lk0-a1s2-00ie-b180-2b70510bd66f",
    "eventID": "733409ba-a869-4e7b-95a1-4d5d204e697c",
    "eventType": "AwsApiCall",
    "recipientAccountId": "11223Example"
}

ListDirectories:
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "ASDFLKJHEXAMPLE1QWERT",
        "arn": "arn:aws:iam::11223Example:user/nickpi",
        "accountId": "11223Example",
        "accessKeyId": "ALSKDJFHGQPWOExample",
        "userName": "nickpi"
    },
    "eventTime": "2017-01-06T00:09:54Z",
    "eventSource": "clouddirectory.amazonaws.com",
    "eventName": "ListDirectories",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.92",
    "userAgent": "Apache-HttpClient/4.3 (java 1.5)",
    "requestParameters": {
        "maxResults": 10
    },
    "responseElements": null,
    "requestID": "56j45l00-a1s2-00ie-b180-2b70660bd66f",
    "eventID": "uwjdf8-f003-4ef7-b15d-8a34149479ac",
    "eventType": "AwsApiCall",
    "recipientAccountId": "11223Example"
}

CreateSchema:
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "ASDFLKJHEXAMPLE1QWERT",
        "arn": "arn:aws:iam::11223Example:user/nickpi",
        "accountId": "11223Example",
        "accessKeyId": "ALSKDJFHGQPWOExample",
        "userName": "nickpi"
    },
    "eventTime": "2017-01-06T00:08:54Z",
    "eventSource": "clouddirectory.amazonaws.com",
    "eventName": "CreateSchema",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.92",
    "userAgent": "Apache-HttpClient/4.3 (java 1.5)",
    "requestParameters": {
        "name": "newName-111"
    },
    "responseElements": {
        "schemaArn": "arn:aws:clouddirectory:us-east-1:11223Example:schema/development/newName-111"
    },
    "requestID": "4jshkjsg-d3a4-11e6-b180-dfhkasdh",
    "eventID": "skdjf-0acb-426c-b64b-fsaj",
    "eventType": "AwsApiCall",
    "recipientAccountId": "11223Example"
}
```
