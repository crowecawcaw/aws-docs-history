**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Updating email settings

You can use the Amazon Pinpoint console to update the email settings for a project. For example, you
can change the verified identity that's associated with the project or verify a new identity
for the project.

###### To update your email settings

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you want to
   update email settings for.
3. In the navigation pane, under **Settings**, choose
   **Email**.
4. On the **Identities** tab, choose **Edit**.
5. Under **Identity type**, choose the type of identity that you want
   to add or update: **Email address** or
   **Domain**.
6. Choose whether you want to update an existing identity or verify a new
   identity.
7. Enter the email address or domain, and then choose
   **Verify**.

If you enter an email address, Amazon Pinpoint sends a verification email to the address that
you entered. Follow the instructions in the email to complete the verification
process.

If you enter an email domain, the console displays a TXT record that you must
add to the DNS settings for your domain. 8. Follow the instructions shown on the console. For more information about verifying an
email address or domain, see [Verifying email identities](channels-email-manage-verify.md "channels-email-manage-verify.md"). 9. If you need to create or update your **Orchestration sending role arn**, see [Creating an email orchestration
sending role in Amazon Pinpoint](channels-email-orchestration-sending-role.md "channels-email-orchestration-sending-role.md"). 10. When you finish, choose **Save**.
