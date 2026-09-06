

# Creating an Amazon SNS platform application
<a name="mobile-push-send-register"></a>

To send notifications from Amazon SNS to mobile endpoints—whether directly or through subscriptions to a topic—you must first create a platform application. After registering the app with AWS, you need to create an endpoint for both the app and the mobile device. This endpoint allows Amazon SNS to send messages to the device.

**To create a platform application**

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home).

1. In the navigation pane, select **Push notifications**.

1. In the **Platform applications** section, choose **Create platform application**.

1. Choose your **AWS Region**. For a list of AWS Regions where you can create mobile applications, see [Amazon SNS mobile application supported Regions](sns-mobile-push-supported-regions.md).

1. Enter the following **application details**:
   + **Application name** – Provide a **name** for your platform application. The name must be between 1 and 256 characters and can contain uppercase and lowercase letters, numbers, underscores, hyphens, and periods.
   + **Push notification platform** – Select the appropriate **notification service** that the app is registered with (For example, Apple Push Notification Service (APNs), Firebase Cloud Messaging (FCM)).

1. Depending on the platform you selected, you’ll need to provide specific credentials:
   + For **APNs** (Apple Push Notification Service) – Choose between **token-based** or **certificate-based** authentication.
     + For token-based authentication, upload a **.p8 file** (generated via Keychain Access).
     + For certificate-based authentication, upload a **.p12 file** (also exported from Keychain Access).
   + For **FCM** (Firebase Cloud Messaging) – Enter the **Server key** from Firebase Console.
   + For **other platforms** (such as ADM or GCM) – Enter the respective **API keys** or **credentials**.

1. After entering the necessary details, choose **Create platform application**. This action registers the app with Amazon SNS and creates the corresponding platform application object.

1. Upon creation, Amazon SNS generates and returns a [`PlatformApplicationArn`](https://docs.aws.amazon.com/sns/latest/api/API_PlatformApplication.html) (Amazon Resource Name). This ARN uniquely identifies your platform application and is used when creating endpoints for mobile devices.