

# AWS End User Messaging service-linked-role policy
<a name="nx-security-iam-managed-policies-slr"></a>

For the WhatsApp channel, AWS End User Messaging uses the service-linked-role policy `AWSSocialMessagingServiceRolePolicy`, which allows the service to publish metrics to Amazon CloudWatch in the `AWS/SocialMessaging` namespace. For more information, see [Using service-linked roles for AWS End User Messaging](nx-security-slr.md).

For the SMS, MMS, voice, and RCS channels, AWS End User Messaging uses the service-linked-role policy `SMSVoiceServiceRolePolicy`, which allows the service to publish metrics to Amazon CloudWatch in the `AWS/SMSVoice` namespace. AWS End User Messaging also uses the service-linked-role policy `EndUserMessagingServiceRolePolicy`, which allows the service to publish metrics to Amazon CloudWatch in the `AWS/EndUserMessaging` namespace. For more information, see [Using service-linked roles for AWS End User Messaging](nx-security-slr.md).