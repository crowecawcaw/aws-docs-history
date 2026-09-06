

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Create or import segments in Amazon Pinpoint
<a name="segments"></a>

A user *segment* represents a subset of users based on shared characteristics, such as how recently the users have used your app or which device platform they use. A segment designates which users receive the messages delivered by a campaign. Define segments so that you can reach the right audience when you want to invite users back to your app, make special offers, or otherwise increase user engagement and purchasing.

After you create a segment, you can use it in one or more campaigns. A campaign delivers tailored messages to the users in the segment.

For more information, see [Segments](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments.html).

**Topics**
+ [Build segments in Amazon Pinpoint](segments-dimensional.md)
+ [Import segments in Amazon Pinpoint](segments-importing.md)
+ [Customize Amazon Pinpoint segments using an AWS Lambda function](segments-dynamic.md)