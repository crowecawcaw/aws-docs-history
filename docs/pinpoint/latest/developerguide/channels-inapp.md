**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Customize in-app messages with Amazon Pinpoint and Amplify

You can use in-app messages to send targeted messages to users of your applications.
In-app messages are highly customizable. They can include buttons that open websites or take
users to specific parts of your app. You can configure background and text colors, position
the text, and add buttons and images to the notification. You can send a single message, or
create a carousel that contains up to five unique messages. For an overview of in-app
messages, including instructions for creating in-app message templates, see [Creating in-app
templates](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") in the _Amazon Pinpoint User Guide_.

You can use AWS Amplify to seamlessly integrate the in-app messaging capabilities of
Amazon Pinpoint into your app. Amplify can automatically handle the processes of fetching messages,
rendering messages, and sending analytics data to Amazon Pinpoint. This integration is currently
supported for React Native applications. For more information, see [In-App Messaging](https://docs.amplify.aws/gen1/javascript/build-a-backend/more-features/in-app-messaging/ "https://docs.amplify.aws/gen1/javascript/build-a-backend/more-features/in-app-messaging/") in the _Amplify Framework
Documentation_.
