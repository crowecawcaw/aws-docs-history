**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Channel resiliency considerations in Amazon Pinpoint

There are several factors that you should consider when creating a resilient Amazon Pinpoint
architecture. This section provides information about concerns that are specific to certain
communication channels, such as email and SMS.

###### Topics in this chapter:

- [Email channel architecture considerations](#channels-email "#channels-email")
- [SMS channel architecture considerations](#channels-sms "#channels-sms")
- [Architecture considerations for other channels](#channels-others "#channels-others")

## Email channel architecture considerations

When designing a multi-Region architecture for Amazon Pinpoint, make sure that you consider two
important factors in your architecture: reputation and opt-outs.

###### Topics in this section:

- [Reputation](#channels-email-reputation "#channels-email-reputation")
- [Opt-outs](#channels-email-optouts "#channels-email-optouts")
- [Templates](#channels-email-templates "#channels-email-templates")

### Reputation

When deciding whether to mark an email as spam or deliver it to the inbox, email
providers calculate a reputation score. This score considers multiple factors to
determine if the email you send is trustworthy. There are two aspects of reputation to
consider:

- **IP reputation** – Each IP address that
  you use to send email has its own reputation score. Many customers, especially
  those who send high volumes of email, use dedicated IP addresses. These
  dedicated IP addresses are unique to each AWS Region, and they can't be used
  across Regions. If you use dedicated IPs, you must consider if you want to use
  dedicated IPs in all of the Regions in which you use Amazon Pinpoint. If you maintain
  dedicated IPs in multiple Regions, it's vital to send regular, predictable
  volumes of email through those IPs to keep them warm. Email providers don't like
  to see massive increases in email volume from IP addresses that were previously
  inactive.

For more information about requesting dedicated email IP addresses, see [Requesting and relinquishing dedicated IP addresses](../userguide/channels-email-dedicated-ips-case.md "../userguide/channels-email-dedicated-ips-case.md") in the
_Amazon Pinpoint User Guide_.

- **Domain and subdomain reputation** – Email
  providers also calculate Reputation scores based on your sending domain,
  regardless of the IP addresses that you use to send your messages. If you use a
  multi-Region architecture with Amazon Pinpoint, you must configure DomainKeys Identified
  Mail (DKIM) and Sender Policy Framework (SPF) in each Region. This means that
  you must create multiple records in the DNS configuration for your
  domain.

For more information about verifying email domains, see [Verifying a domain](../userguide/channels-email-manage-verify.md#channels-email-manage-verify-domain "../userguide/channels-email-manage-verify.md#channels-email-manage-verify-domain") in the
_Amazon Pinpoint User Guide_.

### Opt-outs

When your recipients unsubscribe from email communications, you must manage that
preference across all AWS Regions. Email providers will block messages from domains
that continue to send messages after users opt out.

The Amazon Pinpoint [event stream](../developerguide/event-streams.md "../developerguide/event-streams.md")
provides data about unsubscribe events. For more information about email events, see
[Email
events](../developerguide/event-streams-data-email.md "../developerguide/event-streams-data-email.md") in the _Amazon Pinpoint Developer Guide_.

There are various techniques for synchronizing email events across AWS Regions. The
better technique depends on which destination that you send email events to. For
example, if you send events to Amazon S3, you can use the Cross-Region Replication (CRR)
feature to automatically duplicate data in another Region. For more information about
synchronization, see [Synchronizing event data](customerdata-events.md "customerdata-events.md").

### Templates

If you use email templates, you should have copies of those templates in each
Region. You can duplicate email templates by using the [ListTemplates](../apireference/templates.md#ListTemplates "../apireference/templates.md#ListTemplates") API operation to find the ID of the template that you
want to duplicate. When you have the template ID, you can use the
[GetEmailTemplate](../apireference/templates-template-name-email.md#GetEmailTemplate "../apireference/templates-template-name-email.md#GetEmailTemplate") operation to obtain the details of the template.
Finally, you can use the [CreateEmailTemplate](../apireference/templates-template-name-email.md#CreateEmailTemplate "../apireference/templates-template-name-email.md#CreateEmailTemplate")operation to create the template
in another Region.

You can also use the `AWS::Pinpoint::EmailTemplate` entity in AWS CloudFormation
to deploy email templates to other AWS Regions automatically. For more information,
see [AWS::Pinpoint::EmailTemplate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.md") in the
_AWS CloudFormation User Guide_.

## SMS channel architecture considerations

You can use Amazon Pinpoint to send SMS messages to recipients in almost every country around the
world. When you design a multi-Region architecture for sending SMS messages, you must
consider several factors: country-specific regulations, fallback numbers, throughput limits,
and opt-outs.

### Country-specific regulations

Setting up a system for sending SMS messages globally can be difficult and
time-consuming. Governments, regulators, and mobile carriers in each country have their
own rules about application-to-person SMS messaging, including messages sent from
services such as Amazon Pinpoint.

For example, when you send messages to recipients in the United States, you must
use a dedicated phone number, such as a short code, toll-free number, or 10DLC
number. Phone numbers are resources that are unique to each AWS Region, so they
can't be shared across Regions. Additionally, each of these phone number types has
its own registration process and a different set of capabilities. If you require the
ability to send more than 100 messages per second, you must [request
short codes for messaging](../userguide/channels-sms-awssupport-short-code.md "../userguide/channels-sms-awssupport-short-code.md"). Short codes can take several weeks or even
months to obtain, and the carriers impose several requirements on them, so it's
important to plan ahead. You can also use a combination of phone number types. For
example, if you have a warm standby architecture, your active Region might use a
short code, while your standby Regions have [10DLC numbers](../userguide/settings-sms-10dlc.md "../userguide/settings-sms-10dlc.md")
(which support lower throughput rates than short codes).

Another example of a country with specific requirements is India. If your business
is based in India, you can register an alphanumeric Sender ID for sending your
messages. This Sender ID can identify your brand in your messages, and it's less
expensive to send messages to Indian recipients using a registered Sender ID than
through a non-registered phone number. If you use an Indian Sender ID in multiple
AWS Regions, you must set up your account to use that Sender ID in all of those
Regions. For more information, see [India Sender ID
registration process](../userguide/channels-sms-senderid-india.md "../userguide/channels-sms-senderid-india.md").

### Fallback numbers

Different types of phone numbers can use different routes to reach your recipients.
For example, in the US, a short code takes a different path downstream from AWS to
reach end users than a 10DLC number takes. Having a variety of options, both within the
same AWS Region and across Regions, can provide additional resiliency.

### Throughput limits

In an [active-active](architectures.md#architectures-activeactive "architectures.md#architectures-activeactive") architecture,
you can use Amazon Pinpoint to have the same SMS throughput in all Regions. However, in a [warm standby](architectures.md#architectures-warmstandby "architectures.md#architectures-warmstandby") architecture, it might be
acceptable to have slightly lower throughput rates in your standby Regions. With SMS
messaging, it typically costs more to send at higher throughput rates because you must
obtain resources such as short codes. As you design a multi-Region SMS architecture,
make sure to evaluate your throughput requirements.

### Opt-outs

When your recipients unsubscribe from SMS communications, you must manage that
preference across all AWS Regions. In some countries, there can be severe monetary
penalties for not honoring the SMS opt-out preferences of your recipients. Additionally,
mobile carriers can block messages from your phone number or Sender ID if they determine
that you aren't honoring opt-outs.

The Amazon Pinpoint event stream emits data about opt-out events. For more information about
SMS events, see [SMS
events](../developerguide/event-streams-data-sms.md "../developerguide/event-streams-data-sms.md") in the _Amazon Pinpoint Developer Guide_.

There are various techniques for synchronizing SMS events across AWS Regions. The
better technique depends on which destination that you send events to. For example, if
you send events to Amazon S3, you can use the Cross-Region Replication (CRR) feature to
duplicate data in another Region automatically. For more information about SMS events,
see [Synchronizing event data](customerdata-events.md "customerdata-events.md").

### Templates

If you use SMS templates, you should have copies of those templates in each Region.
You can duplicate SMS templates by using the [ListTemplates](../apireference/templates.md#ListTemplates "../apireference/templates.md#ListTemplates") API operation to find the ID of the template that you want to
duplicate. When you have the template ID, you can use the [GetSmsTemplate](../apireference/templates-template-name-sms.md#GetSmsTemplate "../apireference/templates-template-name-sms.md#GetSmsTemplate") operation to obtain the details of the template. Finally,
you can use the [CreateSmsTemplate](../apireference/templates-template-name-sms.md#CreateSmsTemplate "../apireference/templates-template-name-sms.md#CreateSmsTemplate") operation to create the template in another
Region.

You can also use the `AWS::Pinpoint::SmsTemplate` entity in AWS CloudFormation to
deploy SMS templates to other AWS Regions automatically. For more information, see
[AWS::Pinpoint::SmsTemplate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.md") in the
_AWS CloudFormation User Guide_.

## Architecture considerations for other channels

Amazon Pinpoint supports several communication channels. This section includes factors that you
should account for when designing a resilient architecture that includes the push
notification, in-app notification, voice, or custom channels.

Other sections in this guide contain dedicated sections related to using the SMS and email
channels in a multi-Region architecture. For more information about those channels, see
[Email channel architecture considerations](#channels-email "#channels-email") and [SMS channel architecture considerations](#channels-sms "#channels-sms").

### Push notification channel

If you use the push notification channel in multiple AWS Regions, you must
separately configure the push notification services (such as Firebase Cloud Messaging or
Apple Push Notification Service) in each Region. Typically, this involves providing an
API key or certificate for each notification service.

For more information about setting up the push notification channel, see [Setting up Amazon Pinpoint mobile push channels](../userguide/channels-push-setup.md "../userguide/channels-push-setup.md") in the
_Amazon Pinpoint User Guide_.

If you use templates for your push notifications, make sure that your templates exist
in each Region. You can duplicate push notification templates by using the [ListTemplates](../apireference/templates.md#ListTemplates "../apireference/templates.md#ListTemplates") API operation to find the ID of the template that you want to
duplicate. When you have the template ID, you can use the [GetPushTemplate](../apireference/templates-template-name-push.md#GetPushTemplate "../apireference/templates-template-name-push.md#GetPushTemplate") operation to obtain the details of the template, and then
you can use the [CreatePushTemplate](../apireference/templates-template-name-push.md#CreatePushTemplate "../apireference/templates-template-name-push.md#CreatePushTemplate") operation to create the template in another
Region.

### Custom channels

Custom channels in Amazon Pinpoint can call AWS Lambda functions or webhooks. If you use custom
channels in multiple AWS Regions, make sure that all of the resources that the custom
channel relies on are present in each Region. For example, if your custom channel calls
a Lambda function, that function must be present in each Region. If that Lambda function
calls other AWS services, then you must reproduce those services in each
Region.

For more information about custom channels, see [Creating custom channels
in Amazon Pinpoint](../developerguide/channels-custom.md "../developerguide/channels-custom.md") in the _Amazon Pinpoint Developer Guide_.

You can use the `AWS::Lambda::Function` entity in AWS CloudFormation to deploy
custom channel Lambda functions to other AWS Regions automatically. For more
information, see [AWS::Lambda::Function](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md") in the
_AWS CloudFormation User Guide_.

### Voice channel

To send voice messages to recipients in a specific country, you must have a dedicated
phone number for that country. If you use the voice channel in multiple AWS Regions,
you must obtain phone numbers in each Region. Phone numbers are Region-specific
resources, which means that the same phone number can't be used in more than one
AWS Region.

For more information about setting up the voice channel, see [Setting up the Amazon Pinpoint voice channel](../userguide/channels-voice-setup.md "../userguide/channels-voice-setup.md") in the
_Amazon Pinpoint User Guide_.

By default, new Amazon Pinpoint accounts are placed in the voice sandbox. While an account is in
the sandbox, Amazon Pinpoint places limits on the messages that you can send. For example, you can
only send 20 messages per day, and you can only send messages to a limited number of
countries. You can request to have your account removed from the sandbox, which removes
these limitations. If you use the voice channel, make sure that you have your account
removed from the sandbox in each Region.

For more information about setting the voice sandbox, see [Amazon Pinpoint voice
sandbox](../userguide/channels-voice-sandbox.md "../userguide/channels-voice-sandbox.md") in the _Amazon Pinpoint User Guide_.

If you use templates for your voice messages, make sure that your templates exist in
each Region. You can duplicate voice templates by using the [ListTemplates](../apireference/templates.md#ListTemplates "../apireference/templates.md#ListTemplates") API operation to find the ID of the template that you want to
duplicate. When you have the template ID, you can use the [GetVoiceTemplate](../apireference/templates-template-name-voice.md#GetVoiceTemplate "../apireference/templates-template-name-voice.md#GetVoiceTemplate") operation to obtain the details of the template, and then
use the [CreateVoiceTemplate](../apireference/templates-template-name-voice.md#CreateVoiceTemplate "../apireference/templates-template-name-voice.md#CreateVoiceTemplate") operation to create the template in another
Region.

### In-app notification channel

The in-app notification channel in Amazon Pinpoint relies on your campaigns or journeys creating
in-app messages for a given endpoint, and it relies on your apps retrieving those
messages from Amazon Pinpoint. If you use the in-app notification channel in multiple
AWS Regions, make sure that your in-app message templates exist in each Region. You
can duplicate in-app message templates by using the [ListTemplates](../apireference/templates.md#ListTemplates "../apireference/templates.md#ListTemplates") API operation to find the ID of the template that you want to
duplicate. When you have the template ID, you can use the [GetInAppTemplate](../apireference/templates-template-name-inapp.md#GetInAppTemplate "../apireference/templates-template-name-inapp.md#GetInAppTemplate") operation to obtain the details of the template. Finally,
you can use the [CreateInAppTemplate](../apireference/templates-template-name-inapp.md#CreateInAppTemplate "../apireference/templates-template-name-inapp.md#CreateInAppTemplate") operation to create the template in another
Region.

You can also use the `AWS::Pinpoint::InAppTemplate` entity in AWS CloudFormation
to deploy in-app message templates to other AWS Regions automatically. For more
information about in-app message templates, see [AWS::Pinpoint::InAppTemplate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-inapptemplate.md") in the
_AWS CloudFormation User Guide_.

For more information about the in-app channel, see [Sending and retrieving
in-app messages in Amazon Pinpoint](../developerguide/channels-inapp.md "../developerguide/channels-inapp.md") in the _Amazon Pinpoint Developer Guide_.
