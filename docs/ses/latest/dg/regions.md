# Regions and Amazon SES

SES is available in several AWS Regions around the world. In each region, AWS
maintains multiple Availability Zones. These Availability Zones are physically isolated from
each other, but are united by private, low-latency, high-throughput, and highly redundant
network connections. These Availability Zones enable us to provide very high levels of
availability and redundancy, while also minimizing latency.

For a list of all of the SES regional endpoints, see [Amazon Simple Email Service endpoints and quotas](../../../general/latest/gr/ses.md "../../../general/latest/gr/ses.md") in the
_AWS General Reference_. To learn more about the number of Availability Zones
that are available in each region, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

This section contains information that you need to know if you plan to use SES in
multiple AWS Regions. It discusses the following subjects:

- [SES regions and endpoints](#region-endpoints "#region-endpoints")
- [Sandbox removal and sending limit
  increases](#region-quota-increases "#region-quota-increases")
- [Verification of email addresses and
  domains](#region-verification "#region-verification")
- [Easy DKIM](#region-dkim "#region-dkim")
- [Account-level suppression list](#region-suppression-list "#region-suppression-list")
- [Feedback notifications](#region-feedback-notifications "#region-feedback-notifications")
- [SMTP credentials](#region-smtp "#region-smtp")
- [Sending authorization](#region-sending-authorization "#region-sending-authorization")
- [Feedback endpoints used for custom MAIL FROM
  domains](#region-feedback "#region-feedback")
- [Email receiving](#region-receive-email "#region-receive-email")
- [Setting up (MX) records](receiving-email-mx-record.md "receiving-email-mx-record.md")
  For general information about AWS Regions, see [AWS
  service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _AWS General
  Reference._

## SES regions and endpoints

When you use SES to send email, you connect to a URL that provides an endpoint
for the SES API or SMTP interface. The _AWS General Reference_
contains a complete list of endpoints that you use to send and receive email through
SES. For more information, see [Amazon Simple Email Service
endpoints and quotas](../../../general/latest/gr/ses.md "../../../general/latest/gr/ses.md") in the AWS General Reference—specific sections are
referenced below:

- [API
  endpoints](../../../general/latest/gr/ses.md#ses_region "../../../general/latest/gr/ses.md#ses_region") – When you send email through
  SES, you can use the URLs listed in this table to make HTTPS requests to
  the SES API.
- [SMTP endpoints](../../../general/latest/gr/ses.md#ses_smtp_endpoints "../../../general/latest/gr/ses.md#ses_smtp_endpoints") – You can use the URLs listed in
  this table to send email when using the SMTP interface.
- [Email Receiving endpoints](../../../general/latest/gr/ses.md#ses_inbound_endpoints "../../../general/latest/gr/ses.md#ses_inbound_endpoints") – If you've configured
  SES to receive email that's sent to your domain, you can use the inbound
  SMTP endpoint URLs listed in this table when you [set up the mail exchanger
  (MX) records in the DNS settings for your domain](receiving-email-mx-record.md "receiving-email-mx-record.md").

###### Note

The inbound SMTP URLs aren't IMAP server addresses. In other words, you
can't use them to receive email by using an application such as Outlook. For
a service that provides an IMAP server for incoming email, see [Amazon WorkMail](https://aws.amazon.com/workmail "https://aws.amazon.com/workmail").

## Sandbox removal and sending limit

increases

The sandbox status for your account can differ between AWS Regions. In other words,
if your account has been removed from the sandbox in the US West (Oregon) region, it
might still be in the sandbox in the US East (N. Virginia) region, unless you've also had
it removed from the sandbox in that region.

Sending limits can also be different depending on the AWS Region. For example, if
your account is able to send 10 messages per second in the Europe (Ireland) region,
you might be able to send more or fewer messages in other regions.

When you [submit a request to have your
account removed from the sandbox](request-production-access.md "request-production-access.md"), or when you [submit a request to have your
account's sending quotas increased](manage-sending-quotas-request-increase.md#user-requested-increased-sending-quotas "manage-sending-quotas-request-increase.md#user-requested-increased-sending-quotas"), be sure to choose all of the
AWS Regions that your request applies to. You can submit several requests in a single
Support Center case.

## Verification of email addresses and

domains

Before you can send email using SES, you have to verify that you own the email
address or domain that you plan to send from. The verification status of email addresses
and domains also differs across AWS Regions. For example, if you verify a domain in
the US West (Oregon) region, you can't use that domain to send email in the
US East (N. Virginia) region until you complete the verification process again for that
region. For more information about verifying email addresses and domains, see [Verified identities in Amazon SES](verify-addresses-and-domains.md "verify-addresses-and-domains.md").

## Easy DKIM

You have to perform the Easy DKIM setup process for each AWS Region where you want
to use Easy DKIM. That is, in each region, you have to use the SES console or the
SES API to generate CNAME records. Next, you have to add all of the CNAME records
to the DNS configuration for your domain. For more information about setting up Easy
DKIM, see [Easy DKIM in Amazon SES](send-email-authentication-dkim-easy.md "send-email-authentication-dkim-easy.md").

Not all AWS Regions use the default SES DKIM domain,
`dkim.amazonses.com`—to see if your region uses a region specific
DKIM domain, check the [DKIM domains
table](../../../general/latest/gr/ses.md#ses_dkim_domains "../../../general/latest/gr/ses.md#ses_dkim_domains") in the _AWS General Reference_.

## Account-level suppression list

Your SES account-level suppression list applies to your AWS account only in
the current AWS Region. You can manually add or remove, individually or in bulk,
addresses from your account-level suppression list by using the SES API v2 or console.

For more information about using your account-level suppression list, see [Using the Amazon SES account-level suppression
list](sending-email-suppression-list.md "sending-email-suppression-list.md").

## Feedback notifications

There are two important points to note about setting up feedback notifications in
multiple AWS Regions:

- Verified identity settings, such as whether you receive feedback by email or
  through SNS, only apply to the region that you set them in. For example,
  if you verify *user@example.com* in the US West (Oregon)
  and US East (N. Virginia) regions and you want to receive bounced emails via
  SNS notifications, you have to use the SES API or the SES
  console to set up SNS feedback notifications for
  *user@example.com* in both regions.
- SNS topics that you use for feedback forwarding have to be in the same
  region where you use SES.

For more information about monitoring your sending activity through feedback
notifications, see [Setting up event
notifications for Amazon SES](monitor-sending-activity-using-notifications.md "monitor-sending-activity-using-notifications.md").

## SMTP credentials

The credentials that you use to send email through the SES SMTP interface are
unique to each AWS Region. If you use the SES SMTP interface to send email in
more than one region, you have to [generate a set of
SMTP credentials](smtp-credentials.md "smtp-credentials.md") for each region.

###### Note

If you created your SMTP credentials before January 10, 2019, your SMTP
credentials were created using an older version of the AWS Signature. For security
purposes, you should delete credentials that you created before this date, and
replace them with newer credentials. You can [delete older
credentials by using the IAM console](../../../IAM/latest/UserGuide/id_users_manage.md#id_users_deleting "../../../IAM/latest/UserGuide/id_users_manage.md#id_users_deleting").

## Feedback endpoints used for custom MAIL FROM

domains

If you use a custom MAIL FROM domain, SES requires you to publish an MX record
so that your domain can receive the bounce and complaint notifications that email
providers send you. You can use the same custom MAIL FROM domain for verified identities
in different AWS Regions because the bounce and complaint notifications are sent to a
region specific feedback endpoint.

When you configure a custom MAIL FROM domain, SES automatically specifies the
correct feedback endpoint for the region where the custom MAIL FROM is being configured.
This endpoint is provided in the MX record's value field for you to publish (add) to
your domain's DNS configuration.

The custom MAIL FROM setup process is described in [Using a custom MAIL FROM domain](mail-from.md "mail-from.md"). For reference, the feedback endpoints that SES
uses for the different AWS Regions is listed in the [Feedback endpoints](../../../general/latest/gr/ses.md#ses_feedback_endpoints "../../../general/latest/gr/ses.md#ses_feedback_endpoints") table
in the AWS General Reference.

## Sending authorization

Delegate senders can only send emails from the AWS Region where the identity owner's
identity is verified. The sending authorization policy that gives permission to the
delegate sender must be attached to the identity in that region. For more information
about sending authorization, see [Using sending authorization with Amazon SES](sending-authorization.md "sending-authorization.md").

## Email receiving

With the exception of Amazon S3 buckets, all of the AWS resources that you use for
receiving email with SES have to be in the same AWS Region as the SES
endpoint. For example, if you use SES in the US West (Oregon) region, then any
SNS topics, KMS keys, and Lambda functions that you use also have to be in the
US West (Oregon) region. Similarly, to receive email with SES within a region,
you have to create an active receipt rule set in that region. Email receiving concepts
and setup process are explained in [Email receiving with Amazon SES](receiving-email.md "receiving-email.md").

The [Email Receiving
endpoints](../../../general/latest/gr/ses.md#ses_inbound_endpoints "../../../general/latest/gr/ses.md#ses_inbound_endpoints") table in the AWS General Reference lists the email receiving endpoints for
all of the AWS Regions where SES supports email receiving.
