# Using message templates in AWS End User Messaging Social

###### Important

Starting on 4/1/2025 Meta will block marketing message templates sent to the US
country code of `+1`. For more information, see [Per-User Marketing Template Message Limits](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits "https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits") in the _WhatsApp
Business Platform Cloud API Reference_.

You can use message templates to create message types that you use frequently, such as weekly
newsletters or appointment reminders. Template messages are the only type of message that
can be sent to customers who have yet to message you, or who have not sent you a message in
the last 24 hours.

Meta assigns each template a quality rating and status. The quality rating impacts a
template's status and lowers a template's pacing or sending rate.

Templates are associated with your WhatsApp Business Account (WABA), managed through the
WhatsApp Manager, and reviewed by WhatsApp.

You can send the following template types:

- Text-based
- Media-based
- Interactive message
- Location-based
- Authentication templates with one-time password buttons
- Multi-Product Message templates
  Meta provides pre-approved sample templates. To learn more, see [Sample message
  templates](https://www.facebook.com/business/help/722393685250070 "https://www.facebook.com/business/help/722393685250070").

For more information on the types of message templates, see [Message template](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates "https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates") in the _WhatsApp Business Platform Cloud API
Reference_.

## Using message templates with WhatsApp

Manager

Use the [WhatsApp
Manager](https://www.facebook.com/business/help/2055875911147364 "https://www.facebook.com/business/help/2055875911147364") to create, modify, or check a templates status.

1. Open the AWS End User Messaging Social console at
   [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/ "https://console.aws.amazon.com/social-messaging/").
2. Choose **Business account**, and then choose a WABA.
3. On the **Message templates** tab, choose **Manage
   message templates**. The [WhatsApp
   manager](https://www.facebook.com/business/help/2055875911147364 "https://www.facebook.com/business/help/2055875911147364") opens in a new window where you can manage your templates by
   choosing **Message templates**.

## Next steps

Once you've created or edited a template, you must submit it for review with WhatsApp.
Meta's review can take up to 24 hours. Meta sends an email to your Business Manager
admin and updates the template status in WhatsApp manager. Use the [WhatsApp
manager](https://www.facebook.com/business/help/2055875911147364 "https://www.facebook.com/business/help/2055875911147364") to check the status of your template.
