**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Getting started with Amazon Pinpoint

To start sending targeted messages in Amazon Pinpoint, you have to complete a few steps. For
example, you have to add customer contact information into Amazon Pinpoint, and then create segments
that target certain customers. Next, you have to create your messages and schedule your
campaigns. Finally, after you send your campaigns, you can use the analytics dashboards that
are built into Amazon Pinpoint to see how well the campaigns performed.

This tutorial includes procedures for all steps involved in sending an email campaign to a
segment of customers with the Amazon Pinpoint console.

###### Note

As soon as you set up a new Amazon Pinpoint account, it is placed in a sandbox for email, SMS,
and voice message channels until you request production access. In the sandbox, you can
access all of Amazon Pinpoint's features, with the following restrictions on your email, SMS, and
voice messages:

- For email sandbox restrictions, see [Amazon Pinpoint email sandbox](channels-email-setup-production-access.md "channels-email-setup-production-access.md").
- For SMS sandbox restrictions, see [SMS sandbox](../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms "../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms") in the _AWS End User Messaging SMS User Guide_.
- For voice sandbox restrictions, see [Voice sandbox](../../../sms-voice/latest/userguide/sandbox.md#sandbox-voice "../../../sms-voice/latest/userguide/sandbox.md#sandbox-voice") in the _AWS End User Messaging SMS User Guide_.
- There are no Amazon Pinpoint sandbox restrictions for push notifications.
  To move to production access from the sandbox, create an AWS Support case for a
  **Service limit increase** request for each channel you want to
  move.

## About this tutorial

This section contains an overview of this tutorial.

###### Intended Audience

This tutorial is designed for marketing and business users.

If you're a software developer or system administrator, you might also find the [tutorials](../developerguide/tutorials.md "../developerguide/tutorials.md") in the
_Amazon Pinpoint Developer Guide_ to be useful.

###### Features Used

This tutorial shows you how to complete all of the following steps by using the
Amazon Pinpoint console:

- Importing customer data from a file.
- Creating a segment that targets specific users based on their
  attributes.
- Creating an email campaign and scheduling it to be sent at a specific
  time.
- Viewing email delivery and response data by using the analytics dashboards
  that are built into Amazon Pinpoint.

###### Time Required

It should take about 30–45 minutes to complete this tutorial.

###### Regional Restrictions

There are no regional restrictions associated with using this solution.

###### Resource Usage Costs

There's no charge for creating an AWS account. However, by implementing this solution,
you might incur some or all of the costs that are listed in the following
table.

| Description                     | Cost (US dollars)                                                                                                                                                                                                                                                                         |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Message sending costs           | You pay $0.0001 for each email that you send through Amazon Pinpoint.                                                                                                                                                                                                                     |
| Monthly targeted audience costs | You pay $0 for the first 5,000 endpoints that you target in Amazon Pinpoint<br>each month. (An \*endpoint<br>• is a<br>destination that you can send messages to, such as a user's email<br>address or mobile phone number.) After that, you pay $0.0012 per<br>endpoint that you target. |

If you use this tutorial to send 5 messages to 5 separate endpoints in one month, you
incur charges of $0.0005.

For detailed information about the costs that you might incur using Amazon Pinpoint, see [Amazon Pinpoint pricing](https://aws.amazon.com/pinpoint/pricing/ "https://aws.amazon.com/pinpoint/pricing/").

**Next:**
[Create and Configure a
Project](gettingstarted-create-project.md "gettingstarted-create-project.md")
