**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Register Amazon Pinpoint endpoints in your application

When a user starts a session (for example, by launching your mobile app), your mobile or
web application can automatically register (or update) an _endpoint_ with
Amazon Pinpoint. The endpoint represents the device that the user starts the session with. It includes
attributes that describe the device, and it can also include custom attributes that you
define. Endpoints can also represent other methods of communicating with customers, such as
email addresses or mobile phone numbers.

After your application registers endpoints, you can segment your audience based on
endpoint attributes. You can then engage these segments with tailored messaging campaigns.
You can also use the **Analytics** page in the Amazon Pinpoint console to view charts
about endpoint registration and activity, such as **New endpoints** and
**Daily active endpoints**.

You can assign a single user ID to multiple endpoints. A user ID represents a single user,
while each endpoint that is assigned the user ID represents one of the user's devices. After
you assign user IDs to your endpoints, you can view charts about user activity in the
console, such as **Daily active users** and **Monthly active
users**.

## Before you begin

If you haven't done so already, integrate the AWS Mobile SDK for Android or iOS or
integrate the AWS Amplify JavaScript library with your application. For more
information, see [Connect your frontend application to Amazon Pinpoint using AWS
Amplify](integrate-sdk.md "integrate-sdk.md").

## Register endpoints with the AWS mobile

SDKs for Android or iOS

You can use the AWS Mobile SDKs for Android or iOS to register and customize
endpoints. For more information, and to view code examples, see the following
documents:

- [Registering endpoints in your application](https://docs.amplify.aws/gen1/swift/sdk/analytics/endpoints/ "https://docs.amplify.aws/gen1/swift/sdk/analytics/endpoints/") in the Android SDK
  documentation.
- [Registering endpoints in your application](https://docs.amplify.aws/gen1/android/sdk/analytics/endpoints/ "https://docs.amplify.aws/gen1/android/sdk/analytics/endpoints/") in the iOS SDK
  documentation.

## Register endpoints with the AWS Amplify

JavaScript library

You can use the AWS Amplify JavaScript library to register and update endpoints in
your apps. For more information, and to view code examples, see [Update
endpoint](https://docs.amplify.aws/gen1/nextjs/build-a-backend/more-features/analytics/analytics-migration-guide/#analyticsupdateendpoint "https://docs.amplify.aws/gen1/nextjs/build-a-backend/more-features/analytics/analytics-migration-guide/#analyticsupdateendpoint") in the AWS Amplify JavaScript documentation.

## Next steps

After you update your app to register endpoints, device
information and custom attributes are provided to Amazon Pinpoint when users launch your app. You can use this information to
define audience segments. You can also use the console to see endpoint metrics and users who are assigned user IDs.
You can also complete the steps in [Report Amazon Pinpoint events in your application](integrate-events.md "integrate-events.md") to update your app to report usage data.
