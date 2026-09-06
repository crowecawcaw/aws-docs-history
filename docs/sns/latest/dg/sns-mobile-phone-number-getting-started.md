

# Getting started with Amazon SNS SMS
<a name="sns-mobile-phone-number-getting-started"></a>

**Important**  
The Amazon SNS SMS Developer Guide has been updated. Amazon SNS has integrated with [AWS End User Messaging SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-service.html) for the delivery of SMS messages. This guide contains the latest information on how to create, configure, and manage your Amazon SNS SMS messages.

This topic guides you through managing your SMS sandbox and configuring IAM and resource-based policies to grant Amazon SNS the necessary permissions for accessing and utilizing the AWS End User Messaging SMS APIs. 

## Prerequisites
<a name="sns-mobile-phone-number-prerequisites"></a>

Amazon SNS recommends updating your IAM policy to include the following actions to ensure comprehensive control and visibility over your Amazon SNS resources:
+ [`AmazonSNSFullAccess`](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSNSFullAccess)
+ [`AmazonSNSReadOnly`](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSNSReadOnlyAccess) 