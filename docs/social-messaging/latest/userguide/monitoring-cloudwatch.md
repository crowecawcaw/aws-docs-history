# Monitoring AWS End User Messaging Social with Amazon CloudWatch

You can monitor AWS End User Messaging Social using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

For AWS End User Messaging Social, consider monitoring the `MetaTemplateMessageFeeCount` and `WhatsAppMessageFeeCount` metrics, and trigger an alarm when a spend threshold has been reached.

###### Note

Before you can use the CloudWatch metrics you must [create a service-link role](using-service-linked-roles.md#create-slr "using-service-linked-roles.md#create-slr").

The following tables list the metrics and dimensions that AWS End User Messaging Social exports to the `AWS/SocialMessaging` namespace.

| Metric                      | Unit  | Description                             |
| --------------------------- | ----- | --------------------------------------- |
| WhatsAppMessageFeeCount     | Count | The count of WhatsApp message fees      |
| MetaTemplateMessageFeeCount | Count | The count of Meta template message fees |

| Dimension                      | Description                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| MessageFeeType                 | Valid fee types are Authentication, Authentication_International, Inbound, Marketing,<br>Service,Standard, Utility |
| DestinationCountryCode         | The two letter ISO code for the country                                                                            |
| WhatsAppPhoneNumberArn         | The arn of the phone number                                                                                        |
| MetaTemplateMessageFeeType     | Valid fee types are regular, free_customer_service, free_entry_point                                               |
| MetaTemplateMessageFeeCategory | Valid fee categories are service, marketing, utility, authentication,<br>authentication_international              |
