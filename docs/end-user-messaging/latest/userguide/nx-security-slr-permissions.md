

# Service-linked role permissions for AWS End User Messaging
<a name="nx-security-slr-permissions"></a>

For the WhatsApp channel, AWS End User Messaging uses the service-linked role named `AWSServiceRoleForSocialMessaging` to publish metrics and provide insights for your social message sending. The `AWSServiceRoleForSocialMessaging` service-linked role trusts the `social-messaging.amazonaws.com` service to assume the role.

The role permissions policy named `AWSSocialMessagingServiceRolePolicy` allows AWS End User Messaging to complete the action `cloudwatch:PutMetricData` on all AWS resources in the `AWS/SocialMessaging` namespace.

For the SMS, MMS, voice, and RCS channels, AWS End User Messaging uses the service-linked role named `AWSServiceRoleForSMSVoice` to publish metrics for your message sending. The `AWSServiceRoleForSMSVoice` service-linked role trusts the `sms-voice.amazonaws.com` service to assume the role. The role permissions policy named `SMSVoiceServiceRolePolicy` allows AWS End User Messaging to complete the action `cloudwatch:PutMetricData` on all AWS resources in the `AWS/SMSVoice` namespace.

AWS End User Messaging also uses the service-linked role named `AWSServiceRoleForEndUserMessaging`, which trusts the `end-user-messaging.amazonaws.com` service to assume the role. The role permissions policy named `EndUserMessagingServiceRolePolicy` allows AWS End User Messaging to complete the action `cloudwatch:PutMetricData` on all AWS resources in the `AWS/EndUserMessaging` namespace.