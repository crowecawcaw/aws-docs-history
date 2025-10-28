**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint settings

###### Note

We have updated our documentation by consolidating and moving the following topics. Each
link takes you to the topic's new location.

The following topic's under **General settings** have been moved:

- [General settings](projects.md "projects.md")
- [Configuring default settings for a project](projects-manage-edit.md "projects-manage-edit.md")
- [Deleting a project](projects-manage-delete.md "projects-manage-delete.md")
  The following topic's under **Email settings** have been moved:

- [Email settings](channels-email.md "channels-email.md")
- [Viewing details about email usage](channels-email-monitor.md#channels-email-usage-details "channels-email-monitor.md#channels-email-usage-details")
- [Enabling and disabling the email channel](channels-email-enable.md "channels-email-enable.md")
- [Verifying identities](channels-email-manage-verify.md "channels-email-manage-verify.md")
- [Creating an email orchestration sending role in Amazon Pinpoint](channels-email-orchestration-sending-role.md "channels-email-orchestration-sending-role.md")
  The following topic's under **SMS and voice settings** have been moved:

- [SMS and voice settings](channels-sms.md "channels-sms.md")
- [Managing SMS and voice settings](channels-sms-manage.md "channels-sms-manage.md")
  The following topic's under **Mobile and web app analytics settings** have been moved:

- [Mobile and web app analytics settings](analytics.md#settings-analytics "analytics.md#settings-analytics")
  The following topic's under **Event stream settings** have been moved:

- [Event stream settings](analytics-streaming.md "analytics-streaming.md")
  Generally, you configure settings for each project, and these settings apply by default to
  all the campaigns and journeys in the project. If you want to tailor an individual campaign
  or journey to meet specific needs, you can change certain settings for the campaign or
  journey. Your changes then override the default settings for the project, and the campaign
  or journey uses the custom settings that you chose.

In addition to the settings that are specific to an individual project, campaign, or journey,
there are also some account-level settings. These account-level settings apply to all the
projects for your Amazon Pinpoint account and, in some cases, other AWS services. These settings
include:

- Production access and sending quotas for channels.
- SMTP credentials and other settings for sending email by using the Amazon Pinpoint SMTP
  interface.
- Dedicated phone numbers for sending SMS and voice messages, and for receiving SMS
  messages.
- Verified identities for sending email and SMS messages.
- SMS information such as short codes, long codes, 10DLC, keywords, and registered sender
  IDs for sending SMS messages.
  To view all the settings for your Amazon Pinpoint account, open an Amazon Pinpoint project, choose
  **Settings** in the navigation pane, and then choose the type of
  setting that you want to view.
