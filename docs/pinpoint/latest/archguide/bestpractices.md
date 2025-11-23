**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Best practices for creating resilient Amazon Pinpoint

architectures

This chapter contains best practices for creating resilient architectures in Amazon Pinpoint.

###### Topics in this chapter:

- [Enable the Amazon Pinpoint event stream](#bestpractices-eventstream "#bestpractices-eventstream")
- [Use exponential backoff](#bestpractices-exponentialbackoff "#bestpractices-exponentialbackoff")
- [Tailor your retry strategy to the channels that
  you use](#bestpractices-retries "#bestpractices-retries")
- [Replicate infrastructure with code](#bestpractices-infraascode "#bestpractices-infraascode")

## Enable the Amazon Pinpoint event stream

When you build a resilient, multi-Region architecture, you should always enable the
Amazon Pinpoint event stream. The event stream automatically delivers important information about
the campaigns that you send. It also provides data about the email and SMS messages that
you send, including information about whether those messages were delivered. This
information is useful for tracking message delivery rates, and for troubleshooting
delivery issues. For more information about enabling the Amazon Pinpoint event stream, see [Streaming Amazon Pinpoint events to Kinesis](../developerguide/event-streams.md "../developerguide/event-streams.md") in the
_Amazon Pinpoint Developer Guide_.

As you plan your resilient Amazon Pinpoint architecture, make sure that you account for the
replication of event data in your resilient Amazon Pinpoint architecture. For more information about duplicating event data,
see [Synchronizing event data](customerdata-events.md "customerdata-events.md").

## Use exponential backoff

If your calls to an AWS API result in failure, we recommend that you wait an
increasing amount of time before issuing the command again. For more information, see
[Retry
behavior](../../../general/latest/gr/api-retries.md "../../../general/latest/gr/api-retries.md") in the _AWS General Reference_.

## Tailor your retry strategy to the channels that

you use

Depending on the channels that you use with Amazon Pinpoint, you might need to adopt a different
message retry strategy. Some channels, such as push notifications, provide results in
real time. That is, either your message is accepted and sent to the push notification
service, or it isn't.

The nature of other channels, such as SMS and email, is that delivery of your message
might be delayed because of factors outside of the control of AWS. For example, when
you send an SMS message, it might not be delivered right away because the recipient's
device isn't on a mobile network, their device is turned off, or there's a temporary
issue with the mobile network. In these cases, the recipient's mobile provider might
attempt to redeliver the message for several hours, which increases the amount of time
that passes before you receive a success or failure notification. Even if a message is
delivered right away, it might still take several minutes for the mobile carrier to send
an acknowledgment back to the Amazon Pinpoint event stream.

Make sure that you account for the asynchronous behavior of the email and SMS channels
when designing your retry strategy. Don't expect delivery confirmations to arrive
immediately. Configure your monitoring systems with this asynchronous behavior in
mind.

## Replicate infrastructure with code

We recommend that you replicate your infrastructure in other Regions in an automated
way. By automating the replication process, you can minimize human error.
AWS services, such as CloudFormation, make it possible to recreate your architecture in other
AWS Regions. Having a repeatable way to deploy and update AWS services helps your
configurations remain consistent across Regions.

Amazon Pinpoint
supports CloudFormation. However, there are some Amazon Pinpoint capabilities that CloudFormation doesn't currently
include, including the following:

- **Journeys** – Amazon Pinpoint Journeys can't
  currently be created by using CloudFormation templates. However, the Amazon Pinpoint API includes
  extensive support for [creating journeys](../apireference/apps-application-id-journeys.md#CreateJourney "../apireference/apps-application-id-journeys.md#CreateJourney"), [updating journeys](../apireference/apps-application-id-journeys-journey-id.md#UpdateJourney "../apireference/apps-application-id-journeys-journey-id.md#UpdateJourney"), [viewing the details of a journey](../apireference/apps-application-id-journeys-journey-id.md#GetJourney "../apireference/apps-application-id-journeys-journey-id.md#GetJourney"), and [changing the state of a journey](../apireference/apps-application-id-journeys-journey-id-state.md#UpdateJourneyState "../apireference/apps-application-id-journeys-journey-id-state.md#UpdateJourneyState"). You can use AWS Lambda functions to
  call the necessary Amazon Pinpoint API operations, and you can include those functions in
  your CloudFormation templates.
- **SMS origination identities** –
  Origination identities are the identities that are used for sending SMS
  messages. Examples of origination identities include short codes, long codes,
  toll-free numbers, and 10DLC numbers. In some countries,
  obtaining these origination identities requires a registration process. For
  example, to obtain a Sender ID for sending SMS messages to recipients in India,
  you must register your company and use case with regulatory authorities. Along
  similar lines, if you want to use a short code to send SMS messages to
  recipients in the United States, you must register your use case with the mobile
  carriers.

For more information about requesting various types of origination identities,
see [Requesting SMS
support](../userguide/channels-sms-awssupport.md "../userguide/channels-sms-awssupport.md") in the _Amazon Pinpoint User Guide_. For more
information about the types of origination identities that are available in each
country,
see [Supported
countries and regions](../userguide/channels-sms-countries.md "../userguide/channels-sms-countries.md") in the
_Amazon Pinpoint User Guide_.
