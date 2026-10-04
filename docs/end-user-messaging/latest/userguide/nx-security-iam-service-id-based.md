

# Identity-based policies for AWS End User Messaging
<a name="nx-security-iam-service-id-based"></a>

**Supports identity-based policies: Yes**

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

AWS End User Messaging supports identity-based policies that use actions in both of its API namespaces: the `sms-voice` namespace for the SMS, MMS, voice, and RCS channels, and the `social-messaging` namespace for the WhatsApp channel.