**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Specify the audience for the campaign

When you create a campaign, you choose a _segment_
to send that campaign to. A segment is a group of your customers that share certain attributes.
For example, a segment might contain all of your customers who use version 2.0 of your app on an
Android device, or all customers who live in the city of Los Angeles.

###### Prerequisite

Before you begin, complete [Create a campaign](campaigns-begin.md "campaigns-begin.md").

###### To specify a segment

1. On the **Choose a segment** page, choose one of the following
   options:
   - **Use an existing segment** – Choose this option if
     you've already created a segment and you're ready to send your campaign to
     it.
   - **Create a segment** – Choose this option if you haven't
     created any segments yet, or if you want to create a new segment for this
     campaign. If you choose this option, create a segment by completing the procedures
     in [Building segments](segments-building.md "segments-building.md").

###### Note

If you want to send your campaign when certain events occur (as opposed to sending
it at a specific time), you must use a dynamic segment (as opposed to an imported
segment). To learn more, see [Building segments](segments-building.md "segments-building.md"). 2. (Optional) Under **Segment hold-out**, specify the percentage of
segment members who shouldn't receive this campaign. Amazon Pinpoint chooses the appropriate
number of segment members at random, and omits them from the campaign.

You can use this feature to perform _hold-out
testing_. In a _hold-out test_, you omit a
sample group of random recipients, and then compare their behaviors (for example, the
number of purchases they make) against the behaviors of the customers who received the
campaign. In this way, you can determine the effectiveness of your campaigns.

###### Next

[Configure the message](campaigns-message.md "campaigns-message.md")
