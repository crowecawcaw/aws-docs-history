**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint email channel

###### Note

Amazon Pinpoint has always used Amazon SES for email delivery, and this update gives you more control
over how Amazon Pinpoint uses your Amazon SES resources in your AWS account. For example, an Amazon SES
resource can be a [verified identity](../../../ses/latest/dg/verify-addresses-and-domains.md "../../../ses/latest/dg/verify-addresses-and-domains.md") or [configuration
set](../../../ses/latest/dg/using-configuration-sets.md "../../../ses/latest/dg/using-configuration-sets.md"). As part of this update, email billing will transition from Amazon Pinpoint to
Amazon SES after you've updated your AWS account permissions.

**Existing Amazon Pinpoint customers**: Starting on
_4/30/2024_, you should update your existing email projects to
use the **Orchestration sending role arn**. All of your journeys and
campaigns that send email will continue to function and use the Amazon Pinpoint API until you
update the **Orchestration sending role arn**.

- For more information on creating the IAM role for **Orchestration
  sending role arn**, see [Creating an email orchestration
  sending role in Amazon Pinpoint](channels-email-orchestration-sending-role.md "channels-email-orchestration-sending-role.md").
- For direct send, your IAM identity must have `ses:SendEmail` and
  `ses:SendRawEmail` permissions.
- To check if your project has been updated with an **Orchestration
  sending role arn**, see [Find your email
  orchestration sending role ARN in Amazon Pinpoint](channels-email-orchestration-sending-role.md#channels-email-orchestration-sending-role-verify "channels-email-orchestration-sending-role.md#channels-email-orchestration-sending-role-verify").
  **New Amazon Pinpoint customers**: Use the **Orchestration
  sending role arn** to send emails from your journeys or campaigns. Your
  journeys and campaigns that send email will use the Amazon SES API.

- For more information on creating the IAM role, see [Creating an email orchestration
  sending role in Amazon Pinpoint](channels-email-orchestration-sending-role.md "channels-email-orchestration-sending-role.md").
- For direct send, your IAM identity must have `ses:SendEmail` and
  `ses:SendRawEmail` permissions.
  You can test IAM policies to verify how they will work with a given identity by
  using the IAM policy simulator. For more information, see [Testing IAM policies with the IAM policy simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md")
  in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

Use the Email channel in Amazon Pinpoint to send email messages to your end users.

If you haven't used Amazon Pinpoint to send email, your account is in the [email sandbox](channels-email-setup-production-access.md "channels-email-setup-production-access.md") by default. When
your account is in the email sandbox, you can only send email to addresses that you verify.
Additionally, you can only send 200 emails in a 24-hour period, at a maximum throughput rate
of one message per second. You can request to have your account removed from the sandbox by
[requesting production access
for email](channels-email-manage-limits.md#channels-email-manage-limits-increase-case "channels-email-manage-limits.md#channels-email-manage-limits-increase-case").

You can [monitor your email activity](channels-email-monitor.md "channels-email-monitor.md") by
viewing analytics in the Amazon Pinpoint console or by streaming email events to Kinesis.

As your email needs change, you can manage the email channel by [updating your email address or domain](channels-email-manage-update.md "channels-email-manage-update.md"), or
[requesting an increase to your sending
quotas](channels-email-manage-limits.md "channels-email-manage-limits.md").

## Choosing between Amazon Pinpoint and Amazon Simple Email Service

(Amazon SES)

AWS also offers an email-only service called Amazon SES. Amazon Pinpoint uses Amazon SES highly scalable
email infrastructure to send email. The two services offer different features and are
intended for different audiences and use cases.

Amazon SES has an API and an SMTP interface, both of which are well suited to sending email
from your applications or services. You can also use the Amazon SES SMTP interface to
integrate with existing third-party applications, such as Customer Relationship
Management (CRM) applications. Amazon SES also offers email features not included in Amazon Pinpoint,
including email receiving capabilities, dedicated IP pools, and cross-account sending
authorization capabilities.

Amazon Pinpoint is well-suited to users who want to send orchestrated communications, including
scheduled campaigns and multi-step customer journeys. Amazon Pinpoint also includes features not
included with Amazon SES, such as audience segmentation, campaign and journey analytics, and
a web-based console that is accessible to less technical users.

For more information about sending email using Amazon SES, see the [Amazon SES Developer Guide](../../../ses/latest/dg/Welcome.md "../../../ses/latest/dg/Welcome.md").

###### Topics

- [Amazon Pinpoint email sandbox](channels-email-setup-production-access.md "channels-email-setup-production-access.md")
- [Setting up the Amazon Pinpoint email channel](channels-email-setup.md "channels-email-setup.md")
- [Monitoring email activity with Amazon Pinpoint](channels-email-monitor.md "channels-email-monitor.md")
- [Managing the Amazon Pinpoint email channel](channels-email-manage.md "channels-email-manage.md")
- [Sending email in Amazon Pinpoint](channels-email-send.md "channels-email-send.md")
- [Using dedicated IP addresses with
  Amazon Pinpoint](channels-email-dedicated-ips.md "channels-email-dedicated-ips.md")
- [The Amazon Pinpoint Deliverability dashboard](channels-email-deliverability-dashboard.md "channels-email-deliverability-dashboard.md")
- [Email best practices](channels-email-best-practices.md "channels-email-best-practices.md")
- [Troubleshooting the email channel](channels-email-troubleshooting.md "channels-email-troubleshooting.md")
