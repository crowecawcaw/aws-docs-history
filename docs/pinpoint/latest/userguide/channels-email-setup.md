**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Setting up the Amazon Pinpoint email channel

To set up the Amazon Pinpoint email channel, you start by verifying the email address or domain that
you want to use when you send email from that project. Next, you create a project, enable
the email channel in that project, and choose an email address or domain to use.

When you enable the email channel for the first time, Amazon Pinpoint doesn't immediately provide
production access for email messaging. Instead, your AWS account has access only to the
email sandbox, which imposes restrictions on your email traffic. To gain production access,
[submit a request](channels-email-setup-production-access.md "channels-email-setup-production-access.md") to
Support.

Use the **Email** settings page to view information about email usage for
your Amazon Pinpoint account, such as the number of emails that you've sent during the past 24 hours
and whether there are sending restrictions on your account.

You can also use the **Email** settings page to enable or disable the
email channel for the current project. If you disable the email channel for the project, you
can't send email from campaigns or journeys in the project. However, you can send
transactional email from your Amazon Pinpoint account. To enable Amazon Pinpoint to send email for your
campaigns or journeys you must create or update an IAM role to allow Amazon Pinpoint to send email
on your behalf through Amazon SES, see [Creating an email orchestration
sending role in Amazon Pinpoint](channels-email-orchestration-sending-role.md "channels-email-orchestration-sending-role.md").

In addition, you can use the **Email** settings page to verify email
identities for the current project. In Amazon Pinpoint, an _identity_
is an email address or domain that you use to send email. Every email address that you want
to use as a _From_, _Source_, _Sender_, or _Return path_ address in email has to be verified before you can
send email with it by using Amazon Pinpoint.

###### Topics

- [Creating an Amazon Pinpoint project with email
  support](channels-email-setup-create.md "channels-email-setup-create.md")
- [Verifying email identities](channels-email-manage-verify.md "channels-email-manage-verify.md")
- [Creating an email orchestration
  sending role in Amazon Pinpoint](channels-email-orchestration-sending-role.md "channels-email-orchestration-sending-role.md")
