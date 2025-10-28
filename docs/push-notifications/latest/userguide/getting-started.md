# Getting started with AWS End User Messaging Push

In order to set up AWS End User Messaging Push so that it can send push notifications to your apps, you
first have to provide the credentials that authorize AWS End User Messaging Push to send messages to your
app. The credentials that you provide depend on which push notification system you use:

- For Apple Push Notification service (APN) credentials, see [Obtain an encryption key and key ID from Apple](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns#Obtain-an-encryption-key-and-key-ID-from-Apple "https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns#Obtain-an-encryption-key-and-key-ID-from-Apple") and
  [Obtain a provider certificate from Apple](https://developer.apple.com/documentation/usernotifications/establishing-a-certificate-based-connection-to-apns#Obtain-a-provider-certificate-from-Apple "https://developer.apple.com/documentation/usernotifications/establishing-a-certificate-based-connection-to-apns#Obtain-a-provider-certificate-from-Apple") in the Apple Developer documentation.
- For Firebase Cloud Messaging (FCM) credentials they can be obtained through the Firebase
  console, see [Firebase Cloud
  Messaging](https://firebase.google.com/docs/cloud-messaging "https://firebase.google.com/docs/cloud-messaging").
- For Baidu credentials, see [Baidu](https://push.baidu.com/ "https://push.baidu.com/").
- For Amazon Device Messaging (ADM) credentials, see [Obtain
  Credentials](https://developer.amazon.com/docs/adm/obtain-credentials.html "https://developer.amazon.com/docs/adm/obtain-credentials.html").
