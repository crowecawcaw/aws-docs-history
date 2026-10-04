

# Creating a service-linked role for AWS End User Messaging
<a name="nx-security-slr-create"></a>

You can use the IAM console to create a service-linked role with the metrics use case. In the AWS CLI or the AWS API, create a service-linked role with the applicable service name: `sms-voice.amazonaws.com` for the SMS, MMS, voice, and RCS channels, or `social-messaging.amazonaws.com` for the WhatsApp channel. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

You can create the service-linked role with the following AWS CLI command:

```
aws iam create-service-linked-role --aws-service-name social-messaging.amazonaws.com
```