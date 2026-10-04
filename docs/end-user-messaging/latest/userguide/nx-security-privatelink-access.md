

# Controlling access to the interface endpoint
<a name="nx-security-privatelink-access"></a>

AWS End User Messaging supports making calls to all of its API actions through the interface endpoint. By default, full access to AWS End User Messaging is allowed through the interface endpoint. To control the traffic that is allowed to reach AWS End User Messaging through the interface endpoint, you can associate a security group with the endpoint network interfaces, attach a VPC endpoint policy, or both.

A VPC endpoint policy is an IAM resource that you attach to an interface endpoint to control which principals can perform which AWS End User Messaging actions on which resources through the endpoint. The following example endpoint policy grants access to the listed actions for all principals on all resources. Use the `sms-voice` actions for the SMS, MMS, voice, and RCS channels, and the `social-messaging` actions for the WhatsApp channel.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": [
                "sms-voice:SendTextMessage",
                "social-messaging:SendWhatsAppMessage"
            ],
            "Resource": "*"
        }
    ]
}
```