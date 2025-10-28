# Receiving push notifications in your application

The following topics describe how to modify your Swift, Android, React Native, or Flutter app so that it receives push notifications.

###### Topics

- [Setting up Swift Push Notifications](#apns-setup "#apns-setup")
- [Setting up Android push notifications](#mobile-push-android "#mobile-push-android")
- [Setting up Flutter Push Notifications](#mobile-push-flutter "#mobile-push-flutter")
- [Setting up React Native Push Notifications](#mobile-push-react-native "#mobile-push-react-native")
- [Create an application in AWS End User Messaging Push](#mobile-push-create-project "#mobile-push-create-project")
- [Handling push notifications](#integrate-push-services "#integrate-push-services")

## Setting up Swift Push Notifications

Push notifications for iOS apps are sent using the Apple Push Notification service (APNs). Before you can
send push notifications to iOS devices, you must create an app ID on the Apple Developer
portal, and you must create the required certificates. You can find more information about
completing these steps in [Setting up
push notification services](https://docs.amplify.aws/lib/push-notifications/getting-started/q/platform/ios/ "https://docs.amplify.aws/lib/push-notifications/getting-started/q/platform/ios/") in the AWS Amplify documentation.

### Working with APNs tokens

As a best practice, you should develop your app so that your customers' device tokens
are regenerated when the app is reinstalled.

If a recipient upgrades their device to a new major version of iOS (for example, from
iOS 12 to iOS 13), and later reinstalls your app, the app generates a new token. If your
app doesn't refresh the token, the older token is used to send the notification. As a
result, Apple Push Notification service (APNs) rejects the notification, because the
token is now invalid. When you attempt to send the notification, you receive a message
failure notification from APNs.

## Setting up Android push notifications

Push notifications for Android apps are sent using Firebase Cloud Messaging (FCM), which replaces
Google Cloud Messaging (GCM). Before you can send push notifications to Android devices, you must
obtain FCM credentials. You can then use those credentials to create an Android project
and launch a sample app that can receive push notifications. You can find more information
about completing these steps in the [Push
notifications](https://docs.amplify.aws/lib/push-notifications/getting-started/q/platform/android/ "https://docs.amplify.aws/lib/push-notifications/getting-started/q/platform/android/") section in the AWS Amplify documentation.

## Setting up Flutter Push Notifications

Push notifications for Flutter apps are sent using Firebase Cloud Messaging (FCM) for
Android, and APNs for iOS. You can find more information about completing these steps in the Push
notifications section of the [AWS
Amplify Flutter documentation](https://docs.amplify.aws/gen1/flutter/build-a-backend/push-notifications/set-up-push-notifications/ "https://docs.amplify.aws/gen1/flutter/build-a-backend/push-notifications/set-up-push-notifications/").

## Setting up React Native Push Notifications

Push notifications for React Native apps are sent using Firebase Cloud Messaging (FCM) for
Android, and APNs for iOS. You can find more information about completing these steps in the Push
notifications section of the [AWS Amplify JavaScript](https://docs.amplify.aws/gen1/react-native/build-a-backend/push-notifications/set-up-push-notifications/ "https://docs.amplify.aws/gen1/react-native/build-a-backend/push-notifications/set-up-push-notifications/") documentation.

## Create an application in AWS End User Messaging Push

To start sending push notifications in AWS End User Messaging Push, you have to create an application. Next, you have
to enable the push notification channels that you want to use by providing the appropriate
credentials.

You can create new applications and set up push notification channels by using the AWS End User Messaging Push
console. For more information, see [Creating an application and enabling push channels](procedure-enable-push.md "procedure-enable-push.md").

You can also create and set up application by using the [API](../../../pinpoint/latest/apireference.md "../../../pinpoint/latest/apireference.md"), an [AWS SDK](https://aws.amazon.com/developer/tools/#sdk "https://aws.amazon.com/developer/tools/#sdk"), or the [AWS Command Line Interface](../../../cli/latest/reference/pinpoint.md "../../../cli/latest/reference/pinpoint.md") (AWS CLI). To create an application, use the
`Apps` resource. To configure push notification channels, use the following
resources:

- [APNs channel](../../../pinpoint/latest/apireference/apps-application-id-channels-apns.md "../../../pinpoint/latest/apireference/apps-application-id-channels-apns.md") to send
  messages to users of iOS devices by using the Apple Push Notification service.
- [ADM channel](../../../pinpoint/latest/apireference/apps-application-id-channels-adm.md "../../../pinpoint/latest/apireference/apps-application-id-channels-adm.md") to send
  messages to users of Amazon Kindle Fire devices.
- [Baidu channel](../../../pinpoint/latest/apireference/apps-application-id-channels-baidu.md "../../../pinpoint/latest/apireference/apps-application-id-channels-baidu.md") to
  send messages to Baidu users.
- [GCM channel](../../../pinpoint/latest/apireference/apps-application-id-channels-gcm.md "../../../pinpoint/latest/apireference/apps-application-id-channels-gcm.md") to send
  messages to Android devices by using Firebase Cloud Messaging (FCM), which replaces Google Cloud Messaging
  (GCM).

## Handling push notifications

After you obtain the credentials that are required to send push notifications, you can
update your application so that they're able to receive push notifications. For more information,
see [Push
notifications—Getting started](https://docs.amplify.aws/lib/push-notifications/getting-started/ "https://docs.amplify.aws/lib/push-notifications/getting-started/") in the AWS Amplify documentation.
