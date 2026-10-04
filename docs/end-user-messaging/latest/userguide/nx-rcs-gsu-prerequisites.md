

# Prerequisites
<a name="nx-rcs-gsu-prerequisites"></a>

Before you begin, complete the following:


| Prerequisite | What to do | 
| --- | --- | 
| AWS account | Create an AWS account if you do not have one. There is no charge to create an AWS account, but you incur costs when you lease origination identities and send messages. For more information about pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/). | 
| IAM permissions | Configure an IAM policy that allows the account you sign in with to use AWS End User Messaging. See the example policy that follows this table. | 
| AWS CLI (optional) | Install and configure the AWS CLI if you want to run API commands from the command line. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). | 

To get started quickly, the following example IAM policy allows all AWS End User Messaging SMS and voice actions on all resources. For production, scope the policy down to the specific actions and resources you use.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sms-voice:*",
            "Resource": "*"
        }
    ]
}
```

The [SMS and Voice v2 API Reference](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/Welcome.html) includes the supported HTTP methods, parameters, and schemas.

**Note**  
To receive and verify your first RCS messages, you also need a phone with RCS enabled: an Android phone with RCS messaging enabled in the default messaging app, or an iPhone running iOS 18 or later. This phone serves as your test device.