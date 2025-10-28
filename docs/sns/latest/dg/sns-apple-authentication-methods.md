# Amazon SNS Apple push notification

authentication methods

You can authorize Amazon SNS to send push notifications to your iOS or macOS app by providing
information that identifies you as the developer of the app. To authenticate, provide either
a _key_ or a _certificate_
[when creating a platform application](../api/API_SetPlatformApplicationAttributes.md "../api/API_SetPlatformApplicationAttributes.md"), both of which you can get from your Apple
Developer account.

**Token signing key**

A private signing key that Amazon SNS uses to sign Apple Push Notification Service (APNs)
authentication tokens.

If you provide a signing key, Amazon SNS uses a token to authenticate with APNs
for every push notification that you send. With your signing key, you can send
push notifications to APNs production and sandbox environments.

Your signing key doesn't expire, and you can use the same signing key for
multiple apps. For more information, see [Communicate with APNs using authentication tokens](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_token-based_connection_to_apns "https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_token-based_connection_to_apns") in the
**Developer Account Help** section of the Apple
website.

**Certificate**

A TLS certificate that Amazon SNS uses to authenticate with APNs when you send
push notifications. You obtain the certificate from your Apple Developer
account.

Certificates expire after one year. When this happens, you must create a new
certificate and provide it to Amazon SNS. For more information, see [Establishing a Certificate-Based Connection to APNs](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_certificate-based_connection_to_apns "https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_certificate-based_connection_to_apns") on the Apple
Developer website.

###### To manage APNs settings using the AWS Management Console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the navigation pane, select **Push notifications**.
3. In the **Platform applications** section, select the **application** whose APNs settings you want to edit, and
   then choose **Edit**. If you haven't already created a platform
   application, follow the [Creating an Amazon SNS platform application](mobile-push-send-register.md "mobile-push-send-register.md") guide to do so now.
4. Choose **Edit** to modify the settings for your platform
   application.
5. In the**Authentication type** section, choose one of the
   following options:
   - **Token-based authentication** (recommended for modern
     APNs integrations)
   - **Certificate-based authentication** (older
     method)

6. Configure your **credentials** based on the
   authentication type:
   - **For token-based authentication:**
     - Upload the **.p8 file**, which is the
       authentication token signing key you downloaded from your Apple
       Developer account.
     - Enter the **Signing Key ID** that you
       find in your Apple Developer account. Navigate to **Certificates**, **IDs
       & Profiles**, **Keys**, and select the **key** you want to use.
     - Provide the **Team Identifier** from
       your Apple Developer account. You can find this on the Membership
       page.
     - Enter the **Bundle Identifier**
       assigned to your app. You can find this under Certificates, IDs and
       Profiles, App IDs.

   - **For certificate-based
     authentication:**
     - Upload the **.p12 file** for your TLS
       certificate. This file can be exported from Keychain Access on macOS
       after downloading the certificate from your Apple Developer
       account.
     - If you assigned a **password** to
       your .p12 certificate, enter it here.

7. After entering the necessary credentials, choose **Save changes**
   to update the settings.
