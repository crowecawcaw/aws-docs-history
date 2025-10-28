# Understanding a template's status and quality rating in WhatsApp

Each message template is assigned a quality rating based on usage, customer feedback,
and customer engagement. A template can be used only if the status is Active, but the
quality determines the template pacing. If a message template consistently receives
negative feedback or experiences low engagement, it will cause a change in the
template's status.

Meta changes a template's status or quality rating automatically based on negative or
positive feedback and engagement. If your template status changes, you will receive a
WhatsApp Manager notification, email, and event notification. Use the [WhatsApp
manager](https://www.facebook.com/business/help/2055875911147364 "https://www.facebook.com/business/help/2055875911147364") to check the status of your template.

If your template is rejected by WhatsApp, you can edit the template and resubmit for
approval or file an appeal with WhatsApp. To learn more, see [Appeals](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines#appeals "https://developers.facebook.com/docs/whatsapp/message-templates/guidelines#appeals") in the _WhatsApp Business Platform Cloud API
Reference_.

| Template status  | Quality rating | Meaning                                                                                                                                                                                                                                                                                                                                                             |
| ---------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In-Review        |                | The message template is being reviewed. This can take up to 24 hours to complete.                                                                                                                                                                                                                                                                                   |
| Rejected         |                | The message template was rejected, and you can file an appeal.                                                                                                                                                                                                                                                                                                      |
| Active           | Pending        | The message template hasn't receive quality feedback or read rate information from customers, but the template can still be used to send messages.                                                                                                                                                                                                                  |
| Active           | High           | The message template has received little to no negative customer feedback and can be used to send messages.                                                                                                                                                                                                                                                         |
| Active           | Medium         | The message template has received negative feedback from customers, or low read rates, and may be paused or turned off.                                                                                                                                                                                                                                             |
| Active           | Low            | The message template has received negative feedback from customers, or low read rates. Message templates with this status can be used, but are at risk of being paused or disabled. When a template moves to the Active-Low status, its sending is paused. The first pause is three hours, the second pause is six hours, and the next pause disables the template. |
| Paused           |                | The message template has been paused due to recurring negative feedback from customers, or low read rates.                                                                                                                                                                                                                                                          |
| Disabled         |                | The message template has been disabled due to recurring negative feedback from customers.                                                                                                                                                                                                                                                                           |
| Appeal Requested |                | An appeal has been requested.                                                                                                                                                                                                                                                                                                                                       |
