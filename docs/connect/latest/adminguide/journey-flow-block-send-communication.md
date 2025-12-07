# Send communication

###### Important

Before using this block, ensure you completed [channel configuration](how-to-create-campaigns.md "how-to-create-campaigns.md") including claimed phone numbers for agent assisted voice or automated voice, claim a phone number or originating identity in AWS End User Messaging SMS and then import the number into Amazon Connect for SMS or WhatsApp, and enabled email at Amazon Connect instance. For instructions, see [Set up SMS messaging](setup-sms-messaging.md "setup-sms-messaging.md"), [Enable email campaigns](enable-email.md "enable-email.md").

## Description

Use this block to send communications through channels such as voice, SMS, WhatsApp, or email. Before using this block, ensure channel setup is complete:

- Voice: Claim phone numbers for automated or agent-assisted calls.
- SMS / WhatsApp: Claim numbers or originating identities in AWS End User Messaging, then import them into Connect.
- Email: Enable email campaigns in your Connect instance.

**Example use cases**

- Send onboarding, appointment reminder, or promotional messages.
- Trigger fallback logic to reach a customer on another channel when a prior attempt fails.

## Contact types

| Contact type   | Supported?             |
| -------------- | ---------------------- |
| Voice          | Yes                    |
| SMS            | Yes                    |
| WhatsApp       | Yes                    |
| Email          | Yes                    |
| Custom channel | Yes, via Custom action |

## How to configure this block

You can configure the **Send communication** block by using the Amazon Connect admin website or by using the SendCommunication action in Flow language.

### Common properties

| Property                      | Description                                                                       |
| ----------------------------- | --------------------------------------------------------------------------------- |
| From                          | Select the originating phone number or email address claimed for your instance.   |
| Message template (non-voice)  | Choose a predefined template for SMS, WhatsApp, or email.                         |
| Template alias / version      | Select a specific version or alias of the message template.                       |
| Store outbound communication  | Optionally save the outbound message ID in flow attributes for delivery tracking. |
| Dial criteria (voice)         | Specify dialing behavior or targeting logic for voice calls.                      |
| Engagement preference (voice) | Define how to prioritize multiple contact numbers per customer.                   |

## Send an SMS (text message)

Configure the following properties on the page to send an SMS message:

- **From**: The phone number that the message is to be sent from. The dropdown menu shows a list of phone numbers that are claimed for your Amazon Connect instance.
- **Message template**: Use the dropdown menu to choose from a list of SMS templates. You can choose one template to be sent to the customer.
- **Template alias or version**: Use the dropdown menu to choose different SMS template alias or version.
- **Store outbound communication**: You can choose to store outbound communication in flow attributes. By saving the outbound message ID in a flow attribute, you can track its delivery status.

## Send an email

Configure the following properties on the page to send an email message:

- **From**: The email address that the message is to be sent from. The dropdown menu shows a list of email addresses that are claimed for your Amazon Connect instance.
- **Display name**: You can personalize how you email address appears to your customers in their inbox.
- **Message template**: Use the dropdown menu to choose from a list of email templates. You can choose one template to be sent to the customer.
- **Template alias or version**: Use the dropdown menu to choose different email template alias or version.
- **Store outbound communication**: You can choose to store outbound communication in flow attributes. By saving the outbound message ID in a flow attribute, you can track its delivery status.

## Voice call

Configure the following properties on the page to use outbound voice channel:

- **Dial criteria**: Configure how the voice call should be handled based on detection criteria. Use the dropdown to choose a segment that the voice call will target for.
- **Engagement preference**: If your contact list includes single account with more than 1 profile, such as joint account holders, and 1 profile could have more than 1 phone number, you can use engagement preference to set contact strategy based on preference.
- **Store outbound communication**: You can choose to store outbound communication in flow attributes. By saving the outbound message ID in a flow attribute, you can track its delivery status.
