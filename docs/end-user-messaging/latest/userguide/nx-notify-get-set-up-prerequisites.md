

# Prerequisites
<a name="nx-notify-get-set-up-prerequisites"></a>

Before you begin, complete the following:


| Prerequisite | What to do | 
| --- | --- | 
| AWS account | Create an AWS account if you do not have one. There is no charge to create an AWS account, but you incur costs when you send messages. Notify pricing includes a per-message Notify service fee plus standard SMS or voice transport rates based on the destination country. For more information, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/). | 
| IAM permissions | Configure an IAM policy that allows the account you sign in with to use Notify. The actions you need depend on which sending mode you choose. See the sending modes that follow this table. | 
| AWS CLI (optional) | Install and configure the AWS CLI if you want to run API commands from the command line. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). | 

**Choose a sending mode**

Notify provides two ways to send a verification message, which differ in who generates the one-time passcode. The mode you choose determines which API namespace you call and which IAM actions you need.

AWS End User Messaging generates and validates the code  
AWS End User Messaging generates the passcode, sends it, and validates the code the recipient enters, backed by a notify code configuration that defines your passcode policy. Use the `endusermessaging` namespace operations `SendNotifyCodeVerification` and `ValidateNotifyCodeVerification`. This mode requires the `end-user-messaging` IAM actions. Because Notify delivers the message through your origination identities, the caller also needs the `sms-voice` actions. Start with [Step 1: Create a notify code policy](nx-notify-get-set-up-policy.md).  
To get started quickly, the following example IAM policy allows the required actions on all resources. For production, scope the policy down to the specific actions and resources you use.  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "end-user-messaging:*",
                "sms-voice:*"
            ],
            "Resource": "*"
        }
    ]
}
```

You generate the code  
You generate the passcode in your own application and pass it to Notify, which delivers it over AWS-managed origination identities using a pre-approved template. Use the `sms-voice` namespace operations `SendNotifyTextMessage` and `SendNotifyVoiceMessage`. This mode requires only the `sms-voice` IAM actions. You do not need a notify code configuration; skip [Step 1: Create a notify code policy](nx-notify-get-set-up-policy.md) and start with [Step 2: Create a Notify configuration](nx-notify-get-set-up-create.md).  
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