

# Migrating to Amazon Pinpoint in the AWS Mobile SDKs or JavaScript Library
<a name="migrate-sdk"></a>

After April 30, 2018, the Amazon Mobile Analytics client in the AWS Mobile SDKs will no longer be updated, and support for existing versions of the client will no longer be offered.

If you're currently using Mobile Analytics with the AWS Mobile SDKs, your apps will continue to report events to Mobile Analytics after this date. This event data will be visible in the Amazon Pinpoint console. However, we strongly recommend that you switch to the Amazon Pinpoint analytics features in the latest AWS Mobile SDKs or JavaScript library, which offer matching functionality. By migrating, you help ensure that you're able to use the latest features and that you receive support for any issues.

Use the steps in this section to migrate your Mobile Analytics app so that it uses Amazon Pinpoint through one of the following:
+ The AWS Mobile SDK for Android
+ The AWS Mobile SDK for iOS
+ The AWS Amplify JavaScript library

If your app currently uses Mobile Analytics through the AWS Mobile SDKs for Unity or Xamarin, you can continue to use these SDKs without migrating until they support Amazon Pinpoint.

To migrate, you use AWS Mobile Hub or the AWS Mobile CLI to:
+ Integrate the latest AWS Mobile SDK or JavaScript library with your app.
+ Create the resources that your app requires to communicate with Amazon Pinpoint.

Then, you customize your app's configuration and IAM permissions so that it reports analytics data to the Amazon Pinpoint project that matches your Mobile Analytics app.

**Topics**
+ [Step 1: Look Up Your Project ID](#migrate-sdk-lookup-id)
+ [Step 2: Integrate SDKs or JavaScript Library](#migrate-sdk-integrate)
+ [Step 3: Enable Analytics](#migrate-sdk-analytics)
+ [Step 4: Delete the Project That Mobile Hub Created](#migrate-sdk-delete-mh-project)
+ [Step 5: Update Your App Configuration](#migrate-sdk-config)
+ [Step 6: Update the IAM Role](#migrate-sdk-app-id-in-iam-role)
+ [Step 7: Build and Test](#migrate-sdk-build-and-test)

## Step 1: Look Up Your Project ID
<a name="migrate-sdk-lookup-id"></a>

The projects that are listed in the Amazon Pinpoint console include the apps that you defined in Mobile Analytics. Look up the project ID for the app that you're migrating. You'll use it in later steps when you customize your app's configuration and IAM permissions.

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/).

1. On the **Projects** page, find the app that you're migrating, and note the value in the **ID** column.

## Step 2: Integrate the AWS Mobile SDK or JavaScript Library
<a name="migrate-sdk-integrate"></a>

To connect to Amazon Pinpoint from your app, integrate the AWS Mobile SDK or JavaScript library with your code. 

### For Android or iOS Apps
<a name="migrate-sdk-integrate-android-ios"></a>

For Android or iOS apps, integrate the AWS Mobile SDK for Android or iOS. To integrate, see [Get Started (Android and iOS)](https://docs.aws.amazon.com/aws-mobile/latest/developerguide/getting-started.html) in the *AWS Mobile Developer Guide*. This topic helps you:
+ Create a project with Mobile Hub. The **Messaging & Analytics** feature is enabled by default.
+ Connect your app to the backend AWS resources that Mobile Hub provisions.
+ Integrate the AWS Mobile SDK for Android or iOS with your app.

### For JavaScript Apps
<a name="migrate-sdk-integrate-js"></a>

For web or mobile JavaScript apps, integrate the AWS Amplify library. To integrate, see [Get Started (Web)](https://docs.aws.amazon.com/aws-mobile/latest/developerguide/web-getting-started.html) or [Get Started (React Native)](https://docs.aws.amazon.com/aws-mobile/latest/developerguide/react-native-getting-started.html) in the *AWS Mobile Developer Guide*. These topics help you:
+ Use the AWS Mobile CLI to create a project. Analytics and web hosting are enabled by default.
+ Create backend AWS resources for your app.
+ Connect your app to the backend resources.
+ Integrate the AWS Amplify library with your app.

## Step 3: Enable Amazon Pinpoint Analytics
<a name="migrate-sdk-analytics"></a>

Now that you've integrated the latest version of the AWS Mobile SDK or JavaScript library, you can submit analytics events by using Amazon Pinpoint instead of Mobile Analytics.

### For Android or iOS Apps
<a name="migrate-sdk-analytics-android-ios"></a>

To update your Android or iOS app, see [Add Analytics to your Mobile App with Amazon Pinpoint](https://docs.aws.amazon.com/aws-mobile/latest/developerguide/add-aws-mobile-analytics.html) in the *AWS Mobile Developer Guide*.

### For JavaScript Apps
<a name="migrate-sdk-analytics-js"></a>

To update your JavaScript app, see [Add Analytics (Web)](https://docs.aws.amazon.com/aws-mobile/latest/developerguide/web-add-analytics.html) or [Add Analytics (React Native)](https://docs.aws.amazon.com/aws-mobile/latest/developerguide/react-native-add-analytics.html) in the *AWS Mobile Developer Guide*.

## Step 4: Delete the Amazon Pinpoint Project That Mobile Hub Created
<a name="migrate-sdk-delete-mh-project"></a>

When you created a project in Mobile Hub, a corresponding project was automatically created in Amazon Pinpoint. You aren't using this Amazon Pinpoint project. Instead, you're using the project that matches your original Mobile Analytics app.

1. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/).

1. On the **Projects** page, find the project that was created by Mobile Hub. It's named as *mobilehubprojectname*\_MobileHub.

1. Copy the project ID.

1. Use a terminal to delete the project with the following AWS CLI command:

   ```
   $ aws pinpoint delete-app --application-id {{project-id}}
   {
       "ApplicationResponse": {
           "Id": "d2b352520bcc4f5492ddbd7ef05f9147",
           "Name": "amamigrationdocstest_MobileHub"
       }
   }
   ```

   The project is removed from Amazon Pinpoint.

## Step 5: Update the App ID in Your App Configuration
<a name="migrate-sdk-config"></a>

Customize the default configuration for your app so that it reports analytics data to the Amazon Pinpoint project for your Mobile Analytics app.

### For Android or iOS Apps
<a name="migrate-sdk-config-android-ios"></a>

Your app now includes a cloud configuration file that connects it to the backend resources that Mobile Hub creates. After you update the app ID in the file, your app sends analytics data to the Amazon Pinpoint project for your Mobile Analytics app.

1. In your app package, open the `awsconfiguration.json` file.

1. In the `PinpointAnalytics` object, replace the value for `AppID` with the ID that you got from the Amazon Pinpoint console.

   ```
   . . .
   "PinpointAnalytics": {
     "Default": {
       "AppId": "{{app-id}}",
       "Region": "us-east-1"
     }
   },
   . . .
   ```

### For JavaScript Apps
<a name="migrate-sdk-config-js"></a>

Configure the AWS Amplify Analytics module in your app code so that your app reports analytics data to the Amazon Pinpoint project for your Mobile Analytics app.

To update your app code, see the [Manual Setup](https://aws.github.io/aws-amplify/media/analytics_guide#manual-setup) instructions for the Analytics module in the AWS Amplify documentation. In the configuration code, for the `appID` parameter, use the ID that you got from the Amazon Pinpoint console.

## Step 6: Update the App ID in the IAM Role
<a name="migrate-sdk-app-id-in-iam-role"></a>

When you created a project by using Mobile Hub or the AWS Mobile CLI, an IAM role was created in your AWS account. This role includes a policy that allows your app to report events and update endpoints with Amazon Pinpoint. The role includes the project ID for your Mobile Hub project. Update this ID so that your app can communicate with the Amazon Pinpoint project for your Mobile Analytics app.

1. Open the Mobile Hub console at [https://console.aws.amazon.com/mobilehub/](https://console.aws.amazon.com/mobilehub/).

1. Choose the project that you created.

1. At the top-right of the console, choose **Resources**.

1. Under **AWS Identity and Access Management Roles**, the console shows the IAM role that was provisioned in your AWS account. Choose the role. 

   The IAM console opens, and the **Roles** page is shown.

1. Under **Permissions**, expand the policy named as *project-name*\_mobileanalytics\_MOBILEHUB\_*mobile-hub-project-id*.

1. Choose **Edit policy**.

1. On the **Edit** page, choose the **JSON** tab.

1. In the JSON editor, where the policy allows the `mobiletargeting:UpdateEndpoint` action, update the value that's assigned to the `Resource` key. Change the app ID to the ID that you got from the Amazon Pinpoint console.

   ```
   . . .
   {
       "Effect": "Allow",
       "Action": [
           "mobiletargeting:UpdateEndpoint"
       ],
       "Resource": [
           "arn:aws:mobiletargeting:*:123456789012:apps/{{app-id}}*"
       ]
   }
   . . .
   ```
**Important**  
Remember to keep the wildcard character (`*`) following the app ID.

1. Choose **Review policy**, and then choose **Save changes**.

## Step 7: Build and Test
<a name="migrate-sdk-build-and-test"></a>

Now that you've integrated the latest AWS Mobile SDK or JavaScript library, and have updated your app code, your app reports events to Amazon Pinpoint. As Amazon Pinpoint receives events, it updates the charts on the **Analytics** pages in the console.

1. Build your updated app, and run it on a test device or emulator.

1. Launch your app, and perform other actions in your app that cause it to report events to Amazon Pinpoint.

1. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/).

1. On the **Projects** page, choose the project for your app.

1. In the navigation menu, choose **Analytics**.

1. Check the charts to verify whether Amazon Pinpoint is showing the analytics that you expect. For example, the **Sessions** chart indicates how many times you open the app, and the **New endpoints** chart indicates how many test devices or emulators launch the app for the first time. Custom events are shown on the **Events** page. Allow up to 15 minutes for the charts to display an event.