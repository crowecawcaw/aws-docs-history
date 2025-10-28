**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Integrate Amazon Pinpoint with your application

Integrate Amazon Pinpoint with your client code to understand and engage your users.

After you integrate and your users launch your application, it connects to the Amazon Pinpoint service
to add or update _endpoints_. Endpoints represent the
destinations that you can message—such as user devices, email addresses, or phone
numbers.

Your application can then provide usage data, or _events_.
View event data in the Amazon Pinpoint console to learn how many users you have, how often they use
your application, when they use it, and more.

After your application supplies endpoints and events, you can use this information to
tailor messaging campaigns for specific audiences, or _segments_. (You can also directly message simple lists of recipients without
creating campaigns.)

Use the topics in this section to integrate Amazon Pinpoint with a mobile or web application. These
topics include code examples and procedures to integrate with a JavaScript, Android, Swift,
or Flutter application. To start integrating your apps, see [Connect your frontend application to Amazon Pinpoint using AWS
Amplify](integrate-sdk.md "integrate-sdk.md").

Outside of your client, you can use [supported
AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md") or the [Amazon Pinpoint API](../apireference.md "../apireference.md") to import
endpoints, export event data, define customer segments, create and run campaigns, and
more.

###### Topics

- [Using Amazon Pinpoint with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md")
- [Connect your frontend application to Amazon Pinpoint using AWS
  Amplify](integrate-sdk.md "integrate-sdk.md")
- [Register Amazon Pinpoint endpoints in your application](integrate-endpoints.md "integrate-endpoints.md")
- [Report Amazon Pinpoint events in your application](integrate-events.md "integrate-events.md")
