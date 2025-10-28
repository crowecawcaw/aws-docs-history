**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Monitoring email activity with Amazon Pinpoint

For emails that you send for a project, Amazon Pinpoint provides options for monitoring your email
activity.

## Amazon Pinpoint analytics

The **Analytics** pages on the Amazon Pinpoint console provide many email-related
metrics for the campaigns and transactional messages that you send for a project. For
example, you can view the number of email endpoints that you can send messages to, and the
number of endpoints that you've already sent messages to. Also, you can view the open,
click, and opt-out rates for messages that you've already sent. For campaign messages, you
can view these metrics across all of your campaigns or for individual campaigns. To learn
more about these metrics and how to view them, see [Amazon Pinpoint analytics](analytics.md "analytics.md").

Amazon Pinpoint provides similar metrics for email that you send for a journey. For example, you
can view the number of messages that were opened by participants in each activity of a
journey. After you publish a journey, you can view the data for these metrics by using the
**Journey metrics** pane in the journey workspace. To learn more about
these metrics, see [View journey metrics](journeys-metrics.md "journeys-metrics.md").

## Streaming email event data

To monitor data, such as successful and failed email deliveries, configure Amazon Pinpoint to
stream email event data to Amazon Kinesis Data Streams or Amazon Data Firehose. Then, you can use the Kinesis platform to
analyze this email data. For more information, see [Streaming Amazon Pinpoint events to Kinesis](analytics-streaming.md#analytics-streaming-kinesis "analytics-streaming.md#analytics-streaming-kinesis").

For examples of the event data that Amazon Pinpoint streams to Kinesis, see [Email events](../developerguide/event-streams-data-email.md "../developerguide/event-streams-data-email.md") in the _Amazon Pinpoint Developer Guide_.

## Viewing details about email usage

The **Email usage and restrictions** section of the
**Email** settings page provides information about email usage for
your Amazon Pinpoint account. You can see how many emails have been sent from your account during
the past 24 hours. You can compare that number to the maximum number of emails that your
account is allowed to send during a 24-hour period, referred to as your
_sending quota_. You can also see the maximum number of emails
that you can send per second, referred to as your _sending rate_. For
additional detailed reports, see the analytics pages for [Campaigns](analytics-campaigns.md "analytics-campaigns.md") and [Transactional messaging](analytics-transactional-messages.md "analytics-transactional-messages.md").

###### Note

The email sending quota, rate, and usage values that are shown in this section apply
to your entire AWS account in the current AWS Region. If you've used Amazon SES to send
emails in the same Region, then this section shows how many email messages you've sent
from both Amazon SES and Amazon Pinpoint.

The **Email usage and restrictions** section also indicates whether
your account is in the sandbox. If your account is in the sandbox, your sending quota
and sending rate are set to relatively low values, and you can send email only to
verified email addresses or domains. For information about requesting an increase to
your sending quota or sending rate, see [Managing email sending quotas](channels-email-manage-limits.md "channels-email-manage-limits.md"). For information about removing your
account from the sandbox, see [Amazon Pinpoint email sandbox](channels-email-setup-production-access.md "channels-email-setup-production-access.md").

## Tracking open and click events in

email

Amazon Pinpoint automatically tracks how many of your emails were opened or clicked by their
recipients. In order to track the number of opens and clicks, Amazon Pinpoint makes minor changes to
the emails that you send.

First, Amazon Pinpoint adds a tiny, transparent image to the end of each email that you send. This
image is hosted on an AWS server. The file name of this image is unique for each
recipient. When a recipient opens an email, their email client downloads this file from our
servers. When an email client downloads a tracking image from our servers, we count it as an
open event.

Second, Amazon Pinpoint replaces all links in your emails with links that refer to a domain that is
hosted by AWS. This link includes a parameter that is unique for each recipient. When a
recipient clicks one of these links, they are first sent to the AWS-hosted domain, and
then immediately redirected to their intended destination. When a recipient visits one of
these redirect links, we count it as a click event.

If a message recipient clicks multiple links in a message or clicks the same link more
than once, those clicks will be counted as one click if they occur within the same hour.
Multiple clicks taking place at different hours will be counted as separate clicks. For
example, a link is clicked at 8:30 AM and 8:45 AM it will count as one click but if the link
is clicked at 8:30 AM and 9:05 AM it will count as two clicks because the hour has changed.
Email opens are counted the same way as clicks.

In order to view open and click events, you have to set up event streaming. For more
information about creating event streams, see [Streaming events with Amazon Pinpoint](analytics-streaming.md "analytics-streaming.md").

###### Note

If you have event streaming enabled you will still receive duplicate events and should
handle such duplicates in your workflows accordingly.

If a recipient's email server performs link validation checks then these checks will appear as click events.
