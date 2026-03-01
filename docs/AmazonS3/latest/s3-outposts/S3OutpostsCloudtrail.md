# Monitoring S3 on Outposts with AWS CloudTrail logs

Amazon S3 on Outposts is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, role, or an AWS service in S3 on Outposts. You can use AWS CloudTrail
to get information about S3 on Outposts bucket-level and object-level requests to audit
and log your S3 on Outposts event activity.

To enable CloudTrail data events for all your
Outposts buckets or for a list of specific Outposts buckets, you must [create a trail manually in CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md"). For more information about CloudTrail log file
entries, see [S3 on Outposts log file entries](../userguide/cloudtrail-logging-understanding-s3-entries.md#cloudtrail-logging-understanding-s3outposts-entries "../userguide/cloudtrail-logging-understanding-s3-entries.md#cloudtrail-logging-understanding-s3outposts-entries").

For a complete list of CloudTrail data events for S3 on Outposts, see [Amazon S3 data events in CloudTrail](../userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events "../userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events") in the _Amazon S3 User Guide_.

###### Note

- It's a best practice to create a lifecycle policy for your AWS CloudTrail data
  event Outposts bucket. Configure the lifecycle policy to periodically
  remove log files after the period of time that you need to audit them. Doing
  so reduces the amount of data that Amazon Athena analyzes for each query. For
  more information, see [Creating and managing a lifecycle configuration for your Amazon S3 on Outposts bucket](S3OutpostsLifecycleManaging.md "S3OutpostsLifecycleManaging.md").
- For examples of how to query CloudTrail logs, see the _AWS Big Data Blog_ post [Analyze Security, Compliance, and Operational Activity Using AWS CloudTrail
  and Amazon Athena](https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/ "https://aws.amazon.com/blogs/big-data/aws-cloudtrail-and-amazon-athena-dive-deep-to-analyze-security-compliance-and-operational-activity/").

## Enable CloudTrail logging for objects in an S3 on Outposts bucket

You can use the Amazon S3 console to configure an AWS CloudTrail trail to log data events for objects
in an Amazon S3 on Outposts bucket. CloudTrail supports logging S3 on Outposts object-level API
operations such as `GetObject`, `DeleteObject`, and
`PutObject`. These events are called _data
events_.

By default, CloudTrail trails don't log data events. However, you can configure trails to log
data events for S3 on Outposts buckets that you specify or to log data events for all the
S3 on Outposts buckets in your AWS account.

CloudTrail does not populate data events in the CloudTrail event history. Additionally, not all
S3 on Outposts bucket–level API operations are populated in the CloudTrail event history. For
more information about how to query CloudTrail logs, see [Using Amazon CloudWatch Logs
filter patterns and Amazon Athena to query CloudTrail logs](https://aws.amazon.com/premiumsupport/knowledge-center/find-cloudtrail-object-level-events/ "https://aws.amazon.com/premiumsupport/knowledge-center/find-cloudtrail-object-level-events/") on the AWS Knowledge
Center.

To configure a trail to log data events for an S3 on Outposts bucket, you can use either the
AWS CloudTrail console or the Amazon S3 console. If you are configuring a trail to log data events for
all the S3 on Outposts buckets in your AWS account, it's easier to use the CloudTrail console. For
information about using the CloudTrail console to configure a trail to log S3 on Outposts data
events, see [Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") in the _AWS CloudTrail User Guide_.

###### Important

Additional charges apply for data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

The following procedure shows how to use the Amazon S3 console to configure a CloudTrail trail to log
data events for an S3 on Outposts bucket.

###### Note

The AWS account that creates the bucket owns it and is the only one that can
configure S3 on Outposts data events to be sent to AWS CloudTrail.

###### To enable CloudTrail data events logging for objects in an S3 on Outposts bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Outposts buckets**.
3. Choose the name of the Outposts bucket whose data events you want to log by using
   CloudTrail.
4. Choose **Properties**.
5. In the **AWS CloudTrail data events** section, choose
   **Configure in CloudTrail**.

The AWS CloudTrail console opens.

You can create a new CloudTrail trail or reuse an existing trail and configure
S3 on Outposts data events to be logged in your trail. 6. On the CloudTrail console **Dashboard** page, choose **Create
trail**. 7. On the **Step 1 Choose trail attributes** page, provide a name
for the trail, choose an S3 bucket to store trail logs, specify any other settings
that you want, and then choose **Next**. 8. On the **Step 2 Choose log events** page, under **Event
type**, choose **Data events**.

For **Data event type**, choose **S3 Outposts**. Choose **Next**.

###### Note

    * When you create a trail and configure data event logging for
     S3 on Outposts, you must specify the data event type correctly.




    	+ If you use the CloudTrail console, choose **S3
    	 Outposts** for **Data event
    	 type**. For information about how to create trails
    	 in the CloudTrail console, see [Creating and updating a trail with the console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") in
    	 the *AWS CloudTrail User Guide*. For information about
    	 how to configure S3 on Outposts data event logging in the CloudTrail
    	 console, see
    	  [Logging data events for Amazon S3 Objects](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-examples "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-examples") in the
    	 *AWS CloudTrail User Guide*.
    	+ If you use the AWS Command Line Interface (AWS CLI) or the AWS SDKs, set the
    	 `resources.type` field to
    	 `AWS::S3Outposts::Object`. For more information
    	 about how to log S3 on Outposts data events with the AWS CLI, see
    	 [Log S3 on Outposts events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-CLI-outposts "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-CLI-outposts") in the
    	 *AWS CloudTrail User Guide*.
    * If you use the CloudTrail console or the Amazon S3 console to configure a trail
     to log data events for an S3 on Outposts bucket, the Amazon S3 console shows
     that object-level logging is enabled for the bucket.

9. On the **Step 3 Review and create** page, review the trail attributes and the
   log events that you configured. Then, choose **Create
   trail**.

###### To disable CloudTrail data events logging for objects in an S3 on Outposts bucket

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the left navigation pane, choose **Trails**.
3. Choose the name of the trail that you created to log events for your S3 on Outposts
   bucket.
4. On the details page for your trail, choose **Stop logging** in
   the upper-right corner.
5. In the dialog box that appears, choose **Stop logging**.

## Amazon S3 on Outposts AWS CloudTrail log file entries

Amazon S3 on Outposts management events are available via AWS CloudTrail. In addition, you can optionally [enable
logging for data events in AWS CloudTrail](../user-guide/enable-cloudtrail-events.md "../user-guide/enable-cloudtrail-events.md").

A _trail_ is a configuration that enables
delivery of events as log files to an S3 bucket in a Region that you specify.
CloudTrail logs for your Outposts buckets include a new field,
`edgeDeviceDetails`, which identifies the Outpost where the
specified bucket is located.

Additional log fields include the requested action, the date and time of the
action, and the request parameters. CloudTrail log files are not an ordered stack
trace of the public API calls, so they don't appear in any specific
order.

The following example shows a CloudTrail log entry that demonstrates a [PutObject](../API/API_PutObject.md "../API/API_PutObject.md") action on
`s3-outposts`.

```
{
      "eventVersion": "1.08",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "`111122223333`",
        "arn": "arn:aws:iam::`111122223333`:user/`yourUserName`",
        "accountId": "`222222222222`",
        "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
        "userName": "`yourUserName`"
      },
      "eventTime": "2020-11-30T15:44:33Z",
      "eventSource": "s3-outposts.amazonaws.com",
      "eventName": "PutObject",
      "awsRegion": "`us-east-1`",
      "sourceIPAddress": "`26.29.66.20`",
      "userAgent": "aws-cli/1.18.39 Python/3.4.10 Darwin/18.7.0 botocore/1.15.39",
      "requestParameters": {
        "expires": "Wed, 21 Oct 2020 07:28:00 GMT",
        "Content-Language": "english",
        "x-amz-server-side-encryption-customer-key-MD5": "`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`",
        "ObjectCannedACL": "BucketOwnerFullControl",
        "x-amz-server-side-encryption": "Aes256",
        "Content-Encoding": "gzip",
        "Content-Length": "10",
        "Cache-Control": "no-cache",
        "Content-Type": "text/html; charset=UTF-8",
        "Content-Disposition": "attachment",
        "Content-MD5": "`je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY`",
        "x-amz-storage-class": "Outposts",
        "x-amz-server-side-encryption-customer-algorithm": "Aes256",
        "bucketName": "``amzn-s3-demo-bucket1``",
        "Key": "path/upload.sh"
      },
      "responseElements": {
        "x-amz-server-side-encryption-customer-key-MD5": "`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`",
        "x-amz-server-side-encryption": "Aes256",
        "x-amz-version-id": "001",
        "x-amz-server-side-encryption-customer-algorithm": "Aes256",
        "ETag": "`d41d8cd98f00b204e9800998ecf8427f`"
      },
      "additionalEventData": {
        "CipherSuite": "`ECDHE-RSA-AES128-SHA`",
        "bytesTransferredIn": 10,
        "x-amz-id-2": "`29xXQBV2O+xOHKItvzY1suLv1i6A52E0zOX159fpfsItYd58JhXwKxXAXI4IQkp6`",
        "SignatureVersion": "SigV4",
        "bytesTransferredOut": 20,
        "AuthenticationMethod": "AuthHeader"
      },
      "requestID": "8E96D972160306FA",
      "eventID": "ee3b4e0c-ab12-459b-9998-0a5a6f2e4015",
      "readOnly": false,
      "resources": [
        {
          "accountId": "`222222222222`",
          "type": "AWS::S3Outposts::Object",
          "ARN": "arn:aws:s3-outposts:`us-east-1`:YYY:outpost/`op-01ac5d28a6a232904/bucket/path/upload.sh`"
        },
        {
          "accountId": "`222222222222`",
          "type": "AWS::S3Outposts::Bucket",
          "ARN": "arn:aws:s3-outposts:`us-east-1`:YYY:outpost/`op-01ac5d28a6a232904/bucket/`"
        }
      ],
      "eventType": "AwsApiCall",
      "managementEvent": false,
      "recipientAccountId": "444455556666",
      "sharedEventID": "02759a4c-c040-4758-b84b-7cbaaf17747a",
      "edgeDeviceDetails": {
        "type": "outposts",
        "deviceId": "`op-01ac5d28a6a232904`"
      },
      "eventCategory": "Data"
    }
```
