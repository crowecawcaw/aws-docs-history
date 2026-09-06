

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# IAM role for streaming events to Kinesis
<a name="permissions-streams"></a>

Amazon Pinpoint can automatically send app usage data, or *event data*, from your app to an Amazon Kinesis data stream or Amazon Data Firehose delivery stream in your AWS account. Before Amazon Pinpoint can begin streaming the event data, you must delegate the required permissions to Amazon Pinpoint. 

If you use the console to set up event streaming, Amazon Pinpoint automatically creates an AWS Identity and Access Management (IAM) role with the required permissions. For more information, see [Streaming Amazon Pinpoint events to Kinesis](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-streaming.html#analytics-streaming-kinesis) in the *Amazon Pinpoint User Guide*.

If you want to create the role manually, attach the following policies to the role: 
+ A permissions policy that allows Amazon Pinpoint to send event data to your stream.
+ A trust policy that allows Amazon Pinpoint to assume the role.

After you create the role, you can configure Amazon Pinpoint to automatically send events to your stream. For more information, see [Stream app event data through Kinesis and Firehose using Amazon Pinpoint](event-streams.md) in this guide.

## Creating the IAM role (AWS CLI)
<a name="permissions-streams-create"></a>

Complete the following steps to manually create an IAM role by using the AWS Command Line Interface (AWS CLI). To learn how to create the role by using the Amazon Pinpoint console, see [Streaming Amazon Pinpoint events to Kinesis](https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-streaming.html#analytics-streaming-kinesis) in the *Amazon Pinpoint User Guide*.

If you haven't installed the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*. You also need to have created either a Kinesis stream or Firehose stream. For information about creating these resources, see [Creating and Managing Streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html) in the *Amazon Kinesis Data Streams Developer Guide* or [Creating an Amazon Data Firehose delivery stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) in the *Amazon Data Firehose Developer Guide*. 

**To create the IAM role by using the AWS CLI**

1. Create a new file. Paste the following policy into the document and make the following changes:
   + Replace {{region}} with the AWS Region that you use Amazon Pinpoint in.
   + Replace {{accountId}} with the unique ID for your AWS account.
   + Replace {{applicationId}} with the unique ID of the project.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "pinpoint.amazonaws.com"
               },
               "Action": "sts:AssumeRole",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "{{111122223333}}"
                   },
                   "ArnLike": {
                   "aws:SourceArn": "arn:aws:mobiletargeting:{{us-east-1}}:{{111122223333}}:apps/{{applicationId}}"
                   }
               }
           }
       ]
   }
   ```

------

   When you finish, save the file as `PinpointEventStreamTrustPolicy.json`.

1. Use the [`create-role`](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) command to create the role and attach the trust policy:

   ```
   aws iam create-role --role-name {{PinpointEventStreamRole}} --assume-role-policy-document file://PinpointEventStreamTrustPolicy.json
   ```

1. Create a new file that contains the permissions policy for your role.

   If you are configuring Amazon Pinpoint to send data to an Kinesis stream, paste the following policy into the file and replace the following:
   + Replace {{region}} with the AWS Region that you use Amazon Pinpoint in.
   + Replace {{accountId}} with the unique ID for your AWS account.
   + Replace {{streamName}} with the name of your Kinesis stream.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": {
           "Action": [
               "kinesis:PutRecords",
               "kinesis:DescribeStream"
           ],
           "Effect": "Allow",
           "Resource": [
               "arn:aws:kinesis:{{us-east-1}}:{{111122223333}}:stream/{{streamName}}"
           ]
       }
   }
   ```

------

   Alternatively, if you are configuring Amazon Pinpoint to send data to an Firehose stream, paste the following policy into the file and replace the following:
   + Replace {{region}} with the AWS Region that you use Amazon Pinpoint in.
   + Replace {{accountId}} with the unique ID for your AWS account.
   + Replace {{delivery-stream-name}} with the name of you Firehose stream.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": {
           "Effect": "Allow",
           "Action": [
               "firehose:PutRecordBatch",
               "firehose:DescribeDeliveryStream"
           ],
           "Resource": [
               "arn:aws:firehose:{{us-east-1}}:{{111122223333}}:deliverystream/{{delivery-stream-name}}"
           ]
       }
   }
   ```

------

   When you finish, save the file as `PinpointEventStreamPermissionsPolicy.json`.

1. Use the [`put-role-policy`](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html) command to attach the permissions policy to the role:

   ```
   aws iam put-role-policy --role-name {{PinpointEventStreamRole}} --policy-name PinpointEventStreamPermissionsPolicy --policy-document file://PinpointEventStreamPermissionsPolicy.json
   ```