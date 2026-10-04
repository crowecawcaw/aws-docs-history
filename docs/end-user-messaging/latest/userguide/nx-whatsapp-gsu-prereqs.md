

# Prerequisites
<a name="nx-whatsapp-gsu-prereqs"></a>

Before you begin, complete the following:


| Prerequisite | What to do | 
| --- | --- | 
| AWS account | Create an AWS account if you do not have one. There is no charge to create an AWS account, but you incur costs when you send messages. For more information about pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/). | 
| IAM permissions | Configure an IAM policy that allows the account you sign in with to use AWS End User Messaging. See the example policy that follows this table. | 
| Meta Business account | Create a Meta Business account if you do not have one. You need a Meta Business account to link a WhatsApp Business Account (WABA) to AWS End User Messaging. You can create or connect your Meta Business account during the embedded onboarding flow in Step 1. | 
| Meta and WhatsApp terms | Review and accept the WhatsApp Business Terms of Service, the WhatsApp Business Solution Terms, and the WhatsApp Business Messaging Policy. Your use of the WhatsApp Business Solution is subject to these terms, and Meta or WhatsApp can prohibit your use of the solution at any time. For more information, see the [WhatsApp Business Terms of Service](https://www.whatsapp.com/legal/business-terms). | 
| AWS CLI (optional) | Install and configure the AWS CLI if you want to run API commands from the command line. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). | 

To get started quickly, the following example IAM policy allows all AWS End User Messaging social messaging actions on all resources. For production, scope the policy down to the specific actions and resources you use.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "social-messaging:*",
            "Resource": "*"
        }
    ]
}
```