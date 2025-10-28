**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint in-app messaging channel

You can use in-app messages to send targeted messages to users of your applications.
In-app messages are highly customizable. They can include buttons that open websites or take
users to specific parts of your app. You can configure background and text colors, position
the text, and add buttons and images to the notification. You can send a single message, or
create a carousel that contains up to five unique messages. Unlike other channels such as
email or SMS, in-app messages are enabled by default in all Amazon Pinpoint projects. Additionally,
in-app messages don't support the use of substitution variables.

You can use AWS Amplify to seamlessly integrate the in-app messaging capabilities of
Amazon Pinpoint into your app. Amplify can automatically handle the processes of fetching messages,
rendering messages, and sending analytics data to Amazon Pinpoint. This integration is currently
supported for React Native applications. For more information, see [In-App Messaging](https://docs.amplify.aws/gen1/javascript/build-a-backend/more-features/in-app-messaging/ "https://docs.amplify.aws/gen1/javascript/build-a-backend/more-features/in-app-messaging/") in the _Amplify Framework
Documentation_.

## How Amazon Pinpoint handles in-app messages

Displaying in-app messages to your users consists of three steps. The first step is to
create the message template. The message template defines the appearance and content of
the message. In-app messages can be single messages that appear on the screen, messages
that cover the entire screen, or carousels that consist of up to five messages. For more
information about creating in-app message templates, see [Creating in-app templates](message-templates-creating-inapp.md "message-templates-creating-inapp.md").

Next, you create an in-app campaign. You can configure your campaign to be sent when
certain events occur. For example, you can trigger the campaign to send when a user
reaches a certain level in a game, or when they look at a certain item in your online
store. For more information about creating campaigns, see [Amazon Pinpoint campaigns](campaigns.md "campaigns.md").

###### Note

In order to receive in-app messages, the endpoints that your campaign targets must
have an endpoint type of `IN_APP`.

Finally, to display the in-app messages in your app, your app must call the [GetInAppMessages](../apireference/apps-application-id-endpoints-endpoint-id-inappmessages.md "../apireference/apps-application-id-endpoints-endpoint-id-inappmessages.md") API to retrieve the messages. The response provides a
JSON-formatted list of the messages that each user is entitled to. When messages are
displayed to users, you can pass analytics events back to Amazon Pinpoint. By doing this, you can
collect metrics for the in-app message campaign. For more information about using in-app
notifications in your apps, see [Sending and
retrieving in-app messages](../developerguide/channels-inapp.md "../developerguide/channels-inapp.md") in the _Amazon Pinpoint Developer Guide_ or
[Dynamically personalize your in-product user experience using Amazon Pinpoint in-app
messaging](https://aws.amazon.com/blogs/messaging-and-targeting/dynamically-personalize-your-in-product-user-experience-using-amazon-pinpoint-in-app-messaging/ "https://aws.amazon.com/blogs/messaging-and-targeting/dynamically-personalize-your-in-product-user-experience-using-amazon-pinpoint-in-app-messaging/") on the AWS Messaging and Targeting Blog.
