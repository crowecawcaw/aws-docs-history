

# Prerequisites
<a name="nx-push-get-set-up-prerequisites"></a>

Before you begin, complete the following:


| Prerequisite | What to do | 
| --- | --- | 
| AWS account | Create an AWS account if you do not have one. There is no charge to create an AWS account, but you incur costs when you send messages. For more information about pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/). | 
| IAM permissions | Configure an IAM policy that allows the account you sign in with to create an application, enable push channels, and send push notifications with AWS End User Messaging Push. See the example policy that follows this table. | 
| Push provider accounts | Create accounts with the push notification services you want to use – Apple Push Notification service (APNs), Firebase Cloud Messaging (FCM), Amazon Device Messaging (ADM), or Baidu Cloud Push – so you can obtain the provider credentials in Step 1. | 
| AWS CLI (optional) | Install and configure the AWS CLI if you want to run API commands from the command line. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). | 

To get started quickly, the following example IAM policy allows all AWS End User Messaging Push actions on all resources. For production, scope the policy down to the specific actions and resources you use.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "mobiletargeting:*",
            "Resource": "*"
        }
    ]
}
```