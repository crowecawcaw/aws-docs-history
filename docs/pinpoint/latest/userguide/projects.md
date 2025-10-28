**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint projects

In Amazon Pinpoint, a _project_ is a collection of recipient information,
segments, campaigns, and journeys. New Amazon Pinpoint users should start by creating a project. If
you've used the Amazon Pinpoint API, you might have seen references to _applications_. In Amazon Pinpoint, projects and applications are interchangeable
terms.

Generally, you configure settings for each project, and these settings apply by default to
all the campaigns and journeys in the project. If you want to tailor an individual campaign
or journey to meet specific needs, you can change certain settings for the campaign or
journey. Your changes then override the default settings for the project, and the campaign
or journey uses the custom settings that you chose.

In addition to the settings that are specific to an individual project, campaign, or
journey, there are also some account-level settings. These account-level settings apply to
all the projects for your Amazon Pinpoint account and, in some cases, other AWS services. These
settings include:

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

###### Topics

- [Managing Amazon Pinpoint projects](projects-manage.md "projects-manage.md")
