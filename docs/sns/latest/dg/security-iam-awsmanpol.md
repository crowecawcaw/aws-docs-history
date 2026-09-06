

# AWS managed policies for Amazon Simple Notification Service
<a name="security-iam-awsmanpol"></a>



An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

 





## AWS managed policy: AmazonSNSFullAccess
<a name="security-iam-awsmanpol-AmazonSNSFullAccess"></a>

`AmazonSNSFullAccess` provides full access to Amazon SNS using the AWS Management Console. This policy also includes the following read and write actions for AWS End User Messaging SMS when called using Amazon SNS. You can attach this policy to your users, groups, or roles.

**Permissions details**

The following permissions apply only when using the Amazon SNS APIs:
+ `sns:*` – Allows full permissions to perform any action related to Amazon SNS. This wildcard (\*) means that the user can execute all possible Amazon SNS actions.
+ `sms-voice:DescribeVerifiedDestinationNumbers` – Allows you to retrieve a list of phone numbers that have been verified for sending SMS messages within the AWS account.
+ `sms-voice:CreateVerifiedDestinationNumber` – Allows you to verify a new phone number for use with SMS messaging services within AWS.
+ `sms-voice:SendDestinationNumberVerificationCode` – Allows you to send a verification code to a phone number that is in the process of being verified for SMS messaging within AWS. 
+ `sms-voice:SendTextMessage` – Allows you to create a new text message and send it to a recipient's phone number. `SendTextMessage` only sends an SMS message to one recipient each time it's invoked.
+ `sms-voice:DeleteVerifiedDestinationNumber` – Allows you to remove a phone number from the list of verified numbers within the AWS account
+ `sms-voice:VerifyDestinationNumber` – Allows you to initiate and complete the verification process for a phone number to be used for SMS messaging services within AWS.
+ `sms-voice:DescribeAccountAttributes` – Allows you to retrieve detailed information about the account-level attributes related to SMS messaging services within AWS.
+ `sms-voice:DescribeSpendLimits` – Allows you to retrieve information about the spending limits associated with SMS messaging services within the AWS account
+ `sms-voice:DescribePhoneNumbers` – Allows you to retrieve detailed information about the phone numbers associated with SMS messaging services within the AWS account 
+ `sms-voice:SetTextMessageSpendLimitOverride` – Allows you to set or override the spending limit for SMS text messaging within the AWS account
+ `sms-voice:DescribeOptedOutNumbers` – Allows you to retrieve a list of phone numbers that have opted out of receiving SMS messages from your AWS account.
+ `sms-voice:DeleteOptedOutNumber` – Allows you to remove a phone number from the list of opted-out numbers within the AWS account

**`AmazonSNSFullAccess` example policy**

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "SNSFullAccess",
            "Effect": "Allow",
            "Action": "sns:*",
            "Resource": "*"
        },
        {
            "Sid": "SMSAccessViaSNS",
            "Effect": "Allow",
            "Action": [
                "sms-voice:DescribeVerifiedDestinationNumbers",
                "sms-voice:CreateVerifiedDestinationNumber",
                "sms-voice:SendDestinationNumberVerificationCode",
                "sms-voice:SendTextMessage",
                "sms-voice:DeleteVerifiedDestinationNumber",
                "sms-voice:VerifyDestinationNumber",
                "sms-voice:DescribeAccountAttributes",
                "sms-voice:DescribeSpendLimits",
                "sms-voice:DescribePhoneNumbers",
                "sms-voice:SetTextMessageSpendLimitOverride",
                "sms-voice:DescribeOptedOutNumbers",
                "sms-voice:DeleteOptedOutNumber"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:CalledViaLast": "sns.amazonaws.com"
                }
            }
        }
    ]
}
```

------

To view the permissions for this policy, see [AmazonSNSFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSNSFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonSNSReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonSNSReadOnlyAccess"></a>

`AmazonSNSReadOnlyAccess` provides read-only access to Amazon SNS using the AWS Management Console. This policy also includes the following read-only actions for AWS End User Messaging SMS when called using Amazon SNS. You can attach this policy to your users, groups, and roles.

**Permissions details**

The following permissions apply only when using the Amazon SNS APIs:
+ `sns:GetTopicAttributes` – Allows you to retrieve the attributes of an Amazon SNS topic. This includes information such as the topic's ARN (Amazon Resource Name), the list of subscribers, delivery policies, access control policies, and any other metadata associated with the topic.
+ `sns:List*` – Allows you to perform any operation that begins with `List` for Amazon SNS resources. This includes permissions to list various elements related to Amazon SNS, such as:
  + `sns:ListTopics` – Allows you to retrieve a list of all Amazon SNS topics in the AWS account.
  + `sns:ListSubscriptions` – Allows you to retrieve a list of all subscriptions to Amazon SNS topics.
  + `sns:ListSubscriptionsByTopic` – Allows you to list all subscriptions for a specific Amazon SNS topic.
  + `sns:ListPlatformApplications` – Allows you to list all platform applications that are created for mobile push notifications.
  + `sns:ListEndpointsByPlatformApplication` – Allows you to list all endpoints associated with a platform application.
+ `sns:CheckIfPhoneNumberIsOptedOut` – Allows you to check whether a specific phone number has opted out of receiving SMS messages through Amazon SNS.
+ `sns:GetEndpointAttributes` – Allows you to retrieve the attributes of an endpoint associated with an Amazon SNS platform application. This could include attributes such as the endpoint's enabled status, custom user data, and any other metadata associated with the endpoint.
+ `sns:GetDataProtectionPolicy` – Allows you to retrieve the data protection policy associated with an Amazon SNS topic.
+ `sns:GetPlatformApplicationAttributes` – Allows you to retrieve the attributes of an Amazon SNS platform application. Platform applications are used in Amazon SNS to send push notifications to mobile devices through services such as Apple Push Notification Service (APNS) or Firebase Cloud Messaging (FCM).
+ `sns:GetSMSAttributes` – Allows you to retrieve the default SMS settings for the AWS account. 
+ `sns:GetSMSSandboxAccountStatus` – Allows you to retrieve the current status of the SMS sandbox for your AWS account.
+ `sns:GetSubscriptionAttributes` – Allows you to retrieve the attributes of a specific subscription to an Amazon SNS topic.
+ `sms-voice:DescribeVerifiedDestinationNumbers` – Allows you to view or retrieve a list of phone numbers that have been verified for sending SMS messages within the AWS account
+ `sms-voice:DescribeAccountAttributes` – Allows you to view or retrieve information about the account-level attributes related to SMS messaging services within AWS.
+ `sms-voice:DescribeSpendLimits` – Allows you to view or retrieve information about the spending limits associated with SMS messaging services within your AWS account
+ `sms-voice:DescribePhoneNumbers` – Allows you to view or retrieve information about the phone numbers that are used for SMS messaging services within the AWS account
+ `sms-voice:DescribeOptedOutNumbers` – Allows you to view or retrieve a list of phone numbers that have opted out of receiving SMS messages from your AWS account

**`AmazonSNSReadOnlyAccess` example policy**

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "SNSReadOnlyAccess",
            "Effect": "Allow",
            "Action": [
                "sns:GetTopicAttributes",
                "sns:List*",
                "sns:CheckIfPhoneNumberIsOptedOut",
                "sns:GetEndpointAttributes",
                "sns:GetDataProtectionPolicy",
                "sns:GetPlatformApplicationAttributes",
                "sns:GetSMSAttributes",
                "sns:GetSMSSandboxAccountStatus",
                "sns:GetSubscriptionAttributes"
            ],
            "Resource": "*"
        },
        {
            "Sid": "SMSAccessViaSNS",
            "Effect": "Allow",
            "Action": [
                "sms-voice:DescribeVerifiedDestinationNumbers",
                "sms-voice:DescribeAccountAttributes",
                "sms-voice:DescribeSpendLimits",
                "sms-voice:DescribePhoneNumbers",
                "sms-voice:DescribeOptedOutNumbers"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:CalledViaLast": "sns.amazonaws.com"
                }
            }
        }
    ]
}
```

------

To view the permissions for this policy, see [AmazonSNSFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSNSFullAccess.html) in the *AWS Managed Policy Reference*.

## Amazon SNS updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Amazon SNS since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon SNS Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
|  [AmazonSNSFullAccess](#security-iam-awsmanpol-AmazonSNSFullAccess) – Update to an existing policy | Amazon SNS added new permissions to allow full access to Amazon SNS using the AWS Management Console. | 09/24/2024 | 
| [AmazonSNSReadOnlyAccess](#security-iam-awsmanpol-AmazonSNSReadOnlyAccess) – Update to an existing policy | Amazon SNS added new permissions to allow read-only access to Amazon SNS using the AWS Management Console. | 09/24/2024 | 
| Amazon SNS started tracking changes | Amazon SNS started tracking changes for its AWS managed policies. | 08/27/2024 | 