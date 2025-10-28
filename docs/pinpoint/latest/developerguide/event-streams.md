**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Stream app event data through Kinesis and Firehose using Amazon Pinpoint

In Amazon Pinpoint, an _event_ is an action that occurs when a user interacts
with one of your applications, when you send a message from a campaign or journey, or when
you send a transactional SMS or email message. For example, if you send an email message,
several events occur:

- When you send the message, a _send_ event occurs.
- When the message reaches the recipient's inbox, a _delivered_
  event occurs.
- When the recipient opens the message, an _open_ event occurs.
  You can configure Amazon Pinpoint to send information about events to Amazon Kinesis. The Kinesis platform
  offers services that you can use to collect, process, and analyze data from AWS services
  in real time. Amazon Pinpoint can send event data to Firehose, which streams this data to AWS data
  stores such as Amazon S3 or Amazon Redshift. Amazon Pinpoint can also stream data to Kinesis Data Streams, which ingests and stores
  multiple data streams for processing by analytics applications.

The Amazon Pinpoint event stream includes information about user interactions with applications
(apps) that you connect to Amazon Pinpoint. It also includes information about all the messages that
you send from campaigns, through any channel, and from journeys. This can also include any
custom events that you've defined. Finally, it includes information about all the
transactional email and SMS messages that you send.

###### Note

Amazon Pinpoint doesn't stream information about transactional push notifications or voice
messages.

This chapter provides information about setting up Amazon Pinpoint to stream event data to Kinesis. It
also contains examples of the event data that Amazon Pinpoint streams.

###### Topics

- [Set up Amazon Pinpoint to stream app event data through Amazon Kinesis or Amazon Data Firehose](event-streams-setup.md "event-streams-setup.md")
- [App event data stream from Amazon Pinpoint](event-streams-data-app.md "event-streams-data-app.md")
- [Campaign event data stream from Amazon Pinpoint](event-streams-data-campaign.md "event-streams-data-campaign.md")
- [Journey event data from Amazon Pinpoint](event-streams-data-journey.md "event-streams-data-journey.md")
- [Email event data stream from Amazon Pinpoint](event-streams-data-email.md "event-streams-data-email.md")
- [SMS event data stream from Amazon Pinpoint](event-streams-data-sms.md "event-streams-data-sms.md")
- [Delete an event stream from Amazon Pinpoint](event-streams-disable.md "event-streams-disable.md")
