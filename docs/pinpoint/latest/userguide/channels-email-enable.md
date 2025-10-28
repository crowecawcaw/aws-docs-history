**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Enabling and disabling the email channel

To send email for campaigns and journeys in the current project, you first have to
enable the email channel for the project. If you don't plan to send email for any
campaigns or journeys in a project, you can disable the email channel for the project.

Note that you don't need to enable the email channel to send transactional emails,
which are emails that are typically sent only once in response to a specific action. For
information about sending transactional email, see [Sending email in Amazon Pinpoint](channels-email-send.md "channels-email-send.md").

###### To enable the email channel for a project

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you
   want to enable the email channel for.
3. In the navigation pane, under **Settings**, choose
   **Email**.
4. On the **Identities** tab, choose
   **Edit**.
5. Select **Enable the email channel for this project**.
6. If you haven't verified an email identity yet, complete the appropriate
   procedure in [Verifying email identities](channels-email-manage-verify.md "channels-email-manage-verify.md").
   Otherwise, choose the identity that you want to use.
7. Choose **Save**.
   The process for disabling the email channel is similar. If you disable the email
   channel, you can't send emails for any campaigns or journeys in the project. However,
   you can send transactional emails from your Amazon Pinpoint account.

###### To disable the email channel

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you
   want to disable the email channel for.
3. In the navigation pane, under **Settings**, choose
   **Email**.
4. On the **Identities** tab, choose
   **Edit**.
5. Clear **Enable the email channel for this project**, and then
   choose **Save**.
