

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# IAM role for streaming email events to Firehose
<a name="permissions-stream-email-events-kinesis"></a>

In the Amazon Pinpoint Email API, you can create *configuration sets* that specify how to handle certain email events. For example, you can create a configuration set that sends delivery notifications to a specific *event destination*, such as an Amazon SNS topic or an Amazon Data Firehose delivery stream. When you send email through the Amazon Pinpoint Email API using that configuration set, Amazon Pinpoint sends information about email-related events to the event destination that you specified in the configuration set.

The Amazon Pinpoint Email API can deliver information about the following types of email events to the event destinations that you specify:
+ **Sends** – The call to Amazon Pinpoint was successful, and Amazon Pinpoint attempted to deliver the email. 
+ **Deliveries** – Amazon Pinpoint successfully delivered the email to the recipient's mail server.
+ **Rejections** – Amazon Pinpoint accepted the email, determined that it contained malware, and rejected it. Amazon Pinpoint didn't attempt to deliver the email to the recipient's mail server.
+ **Rendering Failures** – The email wasn't sent because of a template rendering issue. This event type only occurs when you send an email that includes substitution tags. This event type can occur when substitution values are missing. It can also occur when there's a mismatch between the substitution tags that you used in the email and the substitution data that you provided.
**Note**  
If you use substitution tags in the emails that you send by using the Amazon Pinpoint Email API, you should always create a configuration set that records Rendering Failure events.
+ **Bounces** – The recipient's mail server permanently rejected the email.
+ **Complaints** – The email was successfully delivered to the recipient, but the recipient used the "Report Spam" (or equivalent) feature of their email client to report the message. 
+ **Opens** – The recipient received the message and opened it in their email client. 
+ **Clicks** – The recipient clicked one or more links that were contained in the email.
**Note**  
Every time a recipient opens or clicks an email, Amazon Pinpoint generates unique open or click events, respectively. In other words, if a specific recipient opens a message five times, Amazon Pinpoint reports five separate Open events.

If you want to send data about these events to a Firehose stream, you must create an IAM role that has the appropriate permissions. The role must use the following policies:
+ A trust policy that allows Amazon Pinpoint to assume the role.
+ A permissions policy that allows the Amazon Pinpoint Email API to send email delivery and response records to your stream.

After you create the role, you can configure Amazon Pinpoint to send events to your stream automatically. For more information, see [Streaming Amazon Pinpoint events to Kinesis](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html) in the *Amazon Pinpoint Developer Guide*.

## Trust policy
<a name="permissions-stream-email-events-kinesis-trustpolicy"></a>

To allow the Amazon Pinpoint Email API to assume the IAM role and perform the actions allowed by the permissions policy, attach the following trust policy to the role:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ses.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "{{accountId}}"
        }
      }
    }
  ]
}
```

------

In the preceding example, replace {{accountId}} with the ID of your AWS account.

## Permissions policy
<a name="permissions-stream-email-events-kinesis-permissionspolicies"></a>

To allow the Amazon Pinpoint Email API to send email event data to a Firehose delivery stream, attach the following permissions policy to a role.

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
            "arn:aws:firehose:{{us-east-1}}:{{111122223333}}:deliverystream/{{deliveryStreamName}}"
        ]
    }
}
```

------

In the preceding example, replace {{region}} with the name of the AWS Region in which you created the delivery stream. Replace {{accountId}} with the ID of your AWS account. Finally, replace {{deliveryStreamName}} with the name of the delivery stream.

## Creating the IAM role (AWS CLI)
<a name="permissions-stream-email-events-kinesis-create"></a>

Complete the following steps to create the IAM role by using the AWS Command Line Interface (AWS CLI). For information about installing and configuring the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) in the *AWS Command Line Interface User Guide*.

**To create the IAM role by using the AWS CLI**

1. Create a JSON file that contains the trust policy for your role, and then save the file locally. You can copy the [trust policy](#permissions-stream-email-events-kinesis-trustpolicy) that's provided earlier in this topic.

1. Use the [create-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) command to create the role and attach the trust policy:

   ```
   aws iam create-role --role-name {{PinpointEventStreamRole}} \ 
   --assume-role-policy-document file://{{PinpointEventStreamTrustPolicy.json}}
   ```

   In the preceding example, replace {{PinpointEventStreamTrustPolicy.json}} with the full path to the file that contains the trust policy.

   After you run this command, the AWS CLI returns the following output:

1. Create a JSON file that contains the permissions policy for your role, and then save the file locally. You can copy the [permissions policy](#permissions-stream-email-events-kinesis-permissionspolicies) that's provided earlier in this topic.

1. Use the [put-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html) command to attach the permissions policy to the role:

   ```
   aws iam put-role-policy \
   --role-name {{PinpointEventStreamRole}} \
   --policy-name {{PinpointEventStreamPermissionsPolicy}} 
   --policy-document file://{{PinpointEventStreamPermissionsPolicy.json}}
   ```

   In the preceding example, replace {{PinpointEventStreamPermissionsPolicy.json}} with the full path to the file that contains the permissions policy.