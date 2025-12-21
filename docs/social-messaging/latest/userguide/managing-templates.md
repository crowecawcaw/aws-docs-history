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

Templates are associated with your WhatsApp Business Account (WABA), can be managed through the
AWS End User Messaging Social console, and are reviewed by WhatsApp.

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

## Using message templates in the AWS Console

Create and manage your WhatsApp message templates directly in the AWS End User Messaging Social console.

1. Open the AWS End User Messaging Social console at
   [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/ "https://console.aws.amazon.com/social-messaging/").
2. Choose **Business account**, and then choose a WABA.
3. On the **Message templates** tab, you can:
   - **Create new templates** by choosing **Create template** and following the template creation workflow
   - **View template status** to see which templates are approved, pending, or rejected
   - **Edit existing templates** by selecting a template and choosing **Edit**
   - **Delete templates** that are no longer needed

Templates must be approved by Meta before they can be used to send messages to your customers. You can monitor the approval status of your templates in the console.

## Next steps

Once you've created or edited a template, you must submit it for review with WhatsApp.
Meta's review can take up to 24 hours. Meta sends an email to your Business Manager
admin and updates the template status. You can check the status of your template in the AWS End User Messaging Social console.
