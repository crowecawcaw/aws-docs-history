**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Managing the Amazon Pinpoint SMS channel

You can manage SMS settings, such as your default message type (transactional or
promotional) and your monthly spending quota, directly in the Amazon Pinpoint console.

## Updating SMS channel settings

You can change several SMS-related settings. Most of these settings apply to your
entire AWS account, but some apply to specific projects.

###### To edit SMS settings for a project

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you
   want to edit SMS settings for.
3. In the navigation pane, under **Settings**, choose
   **SMS and voice**.
4. In the **SMS settings** section, choose
   **Edit**.
5. Change the SMS settings for your project as needed. You can change the
   following settings:
   - **Enable the SMS channel for this
     project**

   Select this option to enable or disable the SMS channel for the project. If this setting isn't
   enabled, you can't send SMS messages from this project. This setting
   only applies to the current project.
   - **Account-level settings** – Change these settings to modify the SMS
     settings for your AWS account. These settings apply to your entire
     Amazon Pinpoint account and to all AWS services that you can use to send SMS
     messages, such as Amazon Simple Notification Service (Amazon SNS). You can change the following
     settings:
     - **Default message type** – Choose the category of SMS
       messages that you plan to send from this account. If you send
       account-related messages or time-sensitive messages such as
       one-time passcodes, choose **Transactional**.
       If you plan to send messages that contain marketing material or
       other promotional content, choose
       **Promotional**. This setting applies to
       your entire AWS account.
     - **Account spending limit** – The maximum amount of money
       (in US Dollars) that you can spend sending messages each month.
       You can use this setting to make sure that your SMS sending
       doesn't exceed your budget, or as a way to prevent unexpected
       increases in spending. The price to send an SMS message varies
       depending on the destination country for that message. For
       current prices, see [Amazon Pinpoint Pricing](https://aws.amazon.com/pinpoint/pricing/#SMS_text_messages "https://aws.amazon.com/pinpoint/pricing/#SMS_text_messages"). This setting applies to your entire
       AWS account.
     - **Account sender ID** – The alphabetic sender ID that you
       want to use when you send messages from your account. This
       setting applies to your entire AWS account.

     ###### Note

     Alphabetic sender IDs are only supported in certain
     countries. If you
     don't send messages to countries where sender ID is supported by the mobile
     carriers in that country, you don't need to specify anything in this
     field. Sender IDs aren't supported in common messaging
     destinations such as the United States, Canada, and
     Brazil.

     Additionally, some countries require sender IDs to be pre-registered
     with government agencies or industry organizations.

     For a list of countries that support alphabetic sender IDs, see
     [Supported countries and regions (SMS channel)](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") in the _AWS End User Messaging SMS User Guide_.

6. When you finish, choose **Save changes**.
