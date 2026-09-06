

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Integrate Amazon Pinpoint with your application
<a name="integrate"></a>

Integrate Amazon Pinpoint with your client code to understand and engage your users.

After you integrate and your users launch your application, it connects to the Amazon Pinpoint service to add or update *endpoints*. Endpoints represent the destinations that you can message—such as user devices, email addresses, or phone numbers.

Your application can then provide usage data, or *events*. View event data in the Amazon Pinpoint console to learn how many users you have, how often they use your application, when they use it, and more. 

After your application supplies endpoints and events, you can use this information to tailor messaging campaigns for specific audiences, or *segments*. (You can also directly message simple lists of recipients without creating campaigns.)

Use the topics in this section to integrate Amazon Pinpoint with a mobile or web application. These topics include code examples and procedures to integrate with a JavaScript, Android, Swift, or Flutter application. To start integrating your apps, see [Connect your frontend application to Amazon Pinpoint using AWS Amplify](integrate-sdk.md).

Outside of your client, you can use [supported AWS SDKs](sdk-general-information-section.md) or the [Amazon Pinpoint API](https://docs.aws.amazon.com/pinpoint/latest/apireference/) to import endpoints, export event data, define customer segments, create and run campaigns, and more.

**Topics**
+ [Using Amazon Pinpoint with an AWS SDK](sdk-general-information-section.md)
+ [Connect your frontend application to Amazon Pinpoint using AWS Amplify](integrate-sdk.md)
+ [Register Amazon Pinpoint endpoints in your application](integrate-endpoints.md)
+ [Report Amazon Pinpoint events in your application](integrate-events.md)