

# WhatsApp Message Templates
<a name="nx-features-whatsapp-templates"></a>

**Important**  
Starting on 4/1/2025 Meta will block marketing message templates sent to the US country code of `+1`. For more information, see [Per-User Marketing Template Message Limits](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits) in the *WhatsApp Business Platform Cloud API Reference*.

You can use message templates to create message types that you use frequently, such as weekly newsletters or appointment reminders. Template messages are the only type of message that can be sent to customers who have yet to message you, or who have not sent you a message in the last 24 hours. You can manage message templates using the AWS End User Messaging API and the AWS End User Messaging Social console.

Meta assigns each template a quality rating and status. The quality rating impacts a template's status and lowers a template's pacing or sending rate.

Templates are associated with your WhatsApp Business Account (WABA), can be managed through the AWS End User Messaging Social console, and are reviewed by WhatsApp.

You can send the following template types:
+ Text-based
+ Media-based
+ Interactive message
+ Location-based
+ Authentication templates with one-time password buttons
+ Multi-Product Message templates

Meta provides pre-approved sample templates. To learn more, see [Sample message templates](https://www.facebook.com/business/help/722393685250070).

For more information on the types of message templates, see [Message template](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates) in the *WhatsApp Business Platform Cloud API Reference*.

**Topics**
+ [Manage templates in the console](nx-features-whatsapp-templates-console.md)
+ [Create templates with the API](nx-features-whatsapp-templates-examples.md)
+ [Next steps](nx-features-whatsapp-templates-next.md)
+ [Template pacing](nx-features-whatsapp-templates-pacing.md)
+ [Get feedback on a lowered status](nx-features-whatsapp-templates-feedback.md)
+ [Template status and quality rating](nx-features-whatsapp-templates-status.md)
+ [Reasons why a template is rejected](nx-features-whatsapp-templates-rejection.md)