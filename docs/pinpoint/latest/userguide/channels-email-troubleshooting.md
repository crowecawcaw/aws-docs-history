

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Troubleshooting the email channel
<a name="channels-email-troubleshooting"></a>

Verify that logging is turned on to assist in identifying the cause of failure. For more information on logging, see [Monitoring and logging](troubleshooting.md#troubleshooting-logging) and [Email events](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-email.html).

## Rendering issues
<a name="troubleshooting-email-message-not-displayed"></a>
+ When using an email template, a rendering failure occurs when message variables are missing, formatted incorrectly, or when there is a mismatch between message variables and endpoint data causing emails to fail during sending. 
+ To identify rendering failures, review the Amazon SES CloudWatch metric `RenderingFailure` during the time frame that the campaign ran. Rendering failures appear in the Amazon Pinpoint event logs as [\_email.rendering\_failure events](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-email.html#event-streams-data-email-attributes).
+ To resolve the issue, verify that all message variables have a corresponding endpoint attribute present and are in the correct format. For more information, see [Adding personalized content to message templates](message-templates-personalizing.md).
+ Configure default values for all message variables in the template to avoid rendering failures when an attribute is missing for an endpoint.
+ Test running the campaign without the template to confirm whether endpoints can successfully receive messages. This action can help confirm that the issue is related to template variables.

## Bounce status
<a name="troubleshooting-email-message-bounce"></a>

****Solution for soft bounce****
+ A *soft bounce* occurs because of a temporary failure and will appear under the **\_email.softbounce** event type in the logs. Amazon Pinpoint handles soft bounces by attempting to redeliver the soft bounced emails for a specified period of time.
+ A soft bounce can occur in the following scenarios:
  + The recipient mailbox is full.
  + The recipient mailbox is temporarily unavailable.
  + The server limits are exceeded.
  + The server is overloaded.
+ The specific error codes related to soft bounces are 421, 450, 451, or 452. For the descriptions of these error codes, see [Simple Mail Transfer Protocol (SMTP) Enhanced Status Codes Registry](https://www.iana.org/assignments/smtp-enhanced-status-codes/smtp-enhanced-status-codes.xhtml). The **smtp\_response** in the logs provide the error code for the bounce event.

****Solution for hard bounce****
+ A *hard bounce* is a persistent delivery failure that appears under the **\_email.hardbounce ** event type in the logs. These failures aren't retried.
+ A hard bounce can occur in the following scenarios:
  + The email address doesn’t exist.
  + The domain name doesn’t exist.
  + The recipient’s email server has blocked the emails.
  + The email address is on the account suppression list.
+ Monitor the number of hard bounces in your project and remove hard-bouncing email addresses from your recipient lists. Hard bounces can negatively impact your sending reputation and the deliverability of your email message. For more information, review the best practices on [Bounces](channels-email-best-practices.md#channels-email-best-practices-bounce-rate).