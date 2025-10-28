# Setting up Amazon SES event

publishing

This section describes what you need to do to configure Amazon SES to publish your email
sending events to the following AWS services:

- Amazon CloudWatch
- Amazon Data Firehose
- Amazon Pinpoint
- Amazon Simple Notification Service (Amazon SNS)
  The following steps required for setting up event publishing are covered in the topics
  below:

1. You must create a _configuration set_ using the Amazon SES console
   or API.
2. Add one or more _event destinations_ (CloudWatch, Firehose, Pinpoint, or
   SNS) to the configuration set, and configure parameters unique to the event
   destination.
3. When you send an email, you specify which configuration set to use that contains
   your event destination.

###### Topics in this section

- [Step 1: Create a configuration
  set](event-publishing-create-configuration-set.md "event-publishing-create-configuration-set.md")
- [Step 2: Add an event
  destination](event-publishing-add-event-destination.md "event-publishing-add-event-destination.md")
- [Step 3: Specify your configuration set when
  you send email](event-publishing-send-email.md "event-publishing-send-email.md")
