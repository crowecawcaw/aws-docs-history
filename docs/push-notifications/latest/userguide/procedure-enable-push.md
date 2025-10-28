# Creating an application and enabling push channels

Before you can use AWS End User Messaging Push to send push notifications, you first have to create an application and enable the push notifications channel.

## Contextual

**Application**
An application is a storage container for all of your AWS End User Messaging Push settings. The application also stores your Amazon Pinpoint channels, campaigns, and journeys settings.

**Key**

A private signing key used by AWS End User Messaging Push to cryptographically sign APNs
authentication tokens. You obtain the signing key from your Apple developer
account.

If you provide a signing key,AWS End User Messaging Push uses a token to authenticate with APNs
for every push notification that you send. With your signing key, you can
send push notifications to APNs production and sandbox
environments.

Unlike certificates, your signing key doesn't expire. You only provide
your key once, and you don't need to renew it later. You can use the same
signing key for multiple apps. For more information, see [Communicate with APNs using authentication tokens](https://help.apple.com/developer-account/#/deva05921840 "https://help.apple.com/developer-account/#/deva05921840") in
_Xcode Help_.

**Certificate**

A TLS certificate that AWS End User Messaging Push uses to authenticate with APNs when you
send push notifications. An APNs certificate can support both production
and sandbox environments, or it can support only the sandbox environment.
You obtain the certificate from your Apple developer account.

A certificate expires after one year. When this happens, you must create a
new certificate, which you then provide to AWS End User Messaging Push to renew push notification
deliveries. For more information, see [Communicate with APNs using a TLS certificate](https://help.apple.com/developer-account/#/dev82a71386a "https://help.apple.com/developer-account/#/dev82a71386a") in _Xcode Help_.

## Prerequisites

Before you can use any push channel you need valid credentials for the push service. For
more information on obtaining credentials, see [Getting started with AWS End User Messaging Push](getting-started.md "getting-started.md").

## Procedure

Follow these directions to create an application and enable any of the push channels. To complete this procedure you are only required to enter an application name. You can enable or disable any of the push channels at a later time.

1. Open the AWS End User Messaging Push console at
   [https://console.aws.amazon.com/push-notifications/](https://console.aws.amazon.com/push-notifications/ "https://console.aws.amazon.com/push-notifications/").
2. Choose **Create application**.
3. For **Application name** enter the name for your application.
4. (Optional) Follow this optional step to enable the **Apple Push Notification service
   (APNs)**.
   1. For **Apple Push Notification service (APNs)** select
      **Enable**.
   2. For **Default authentication type** choose either:
      1. If you choose **Key credentials**, provide the
         following information from your Apple developer account. AWS End User Messaging Push requires
         this information to construct authentication tokens.
         - **Key ID** – The ID that's assigned to
           your signing key.
         - **Bundle identifier** – The ID that's
           assigned to your iOS app.
         - **Team identifier** – The ID that's
           assigned to your Apple developer account team.
         - **Authentication key** – The .p8 file
           that you download from your Apple developer account when you
           create an authentication key.

      2. If you choose **Certificate credentials**, provide
         the following information:
         - **SSL certificate** – The .p12 file
           for your TLS certificate.
         - **Certificate password** – If you
           assigned a password to your certificate, enter it here.
         - **Certificate type** – Select the type
           of certificate to use.

5. (Optional) Follow this optional step to enable the **Firebase Cloud Messaging (FCM)**.
   1. For **Firebase Cloud Messaging (FCM)** select
      **Enable**.
   2. For **Default authentication type** choose either:
      1. For **Token credentials (recommended)** choose **Choose files** and then choose your service JSON file.
      2. For **Key credentials** enter your key in **API key**.

6. (Optional) Follow this optional step to enable the **Baidu Cloud Push**.
   1. For **Baidu Cloud Push** select
      **Enable**.
   2. For **API key** enter your API key.
   3. For **Secret key** enter your secret key.

7. (Optional) Follow this optional step to enable the **Amazon Device Messaging**.
   1. For **Amazon Device Messaging** select
      **Enable**.
   2. For **Client ID** enter your client ID.
   3. For **Client secret** enter your client secret.

8. Choose **Create application**.
