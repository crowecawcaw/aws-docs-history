# Migrating to Amazon Pinpoint in the AWS Mobile SDKs or JavaScript

Library

After April 30, 2018, the Amazon Mobile Analytics client in the AWS Mobile SDKs will no longer be updated,
and support for existing versions of the client will no longer be offered.

If you're currently using Mobile Analytics with the AWS Mobile SDKs, your apps will continue to report
events to Mobile Analytics after this date. This event data will be visible in the Amazon Pinpoint console.
However, we strongly recommend that you switch to the Amazon Pinpoint analytics features in the latest
AWS Mobile SDKs or JavaScript library, which offer matching functionality. By migrating,
you help ensure that you're able to use the latest features and that you receive support for
any issues.

Use the steps in this section to migrate your Mobile Analytics app so that it uses Amazon Pinpoint through
one of the following:

- The AWS Mobile SDK for Android
- The AWS Mobile SDK for iOS
- The AWS Amplify JavaScript library
  If your app currently uses Mobile Analytics through the AWS Mobile SDKs for Unity or Xamarin, you can
  continue to use these SDKs without migrating until they support Amazon Pinpoint.

To migrate, you use AWS Mobile Hub or the AWS Mobile CLI to:

- Integrate the latest AWS Mobile SDK or JavaScript library with your app.
- Create the resources that your app requires to communicate with Amazon Pinpoint.
  Then, you customize your app's configuration and IAM permissions so that it reports
  analytics data to the Amazon Pinpoint project that matches your Mobile Analytics app.

###### Topics

- [Step 1: Look Up Your Project ID](#migrate-sdk-lookup-id "#migrate-sdk-lookup-id")
- [Step 2: Integrate SDKs or JavaScript Library](#migrate-sdk-integrate "#migrate-sdk-integrate")
- [Step 3: Enable Analytics](#migrate-sdk-analytics "#migrate-sdk-analytics")
- [Step 4: Delete the Project That Mobile Hub Created](#migrate-sdk-delete-mh-project "#migrate-sdk-delete-mh-project")
- [Step 5: Update Your App Configuration](#migrate-sdk-config "#migrate-sdk-config")
- [Step 6: Update the IAM Role](#migrate-sdk-app-id-in-iam-role "#migrate-sdk-app-id-in-iam-role")
- [Step 7: Build and Test](#migrate-sdk-build-and-test "#migrate-sdk-build-and-test")

## Step 1: Look Up Your Project ID

The projects that are listed in the Amazon Pinpoint console include the apps that you defined in Mobile Analytics.
Look up the project ID for the app that you're migrating. You'll use it in later steps when
you customize your app's configuration and IAM permissions.

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **Projects** page, find the app that you're migrating, and note the
   value in the **ID** column.

## Step 2: Integrate the AWS Mobile SDK or JavaScript

Library

To connect to Amazon Pinpoint from your app, integrate the AWS Mobile SDK or JavaScript library with
your code.

### For Android or iOS Apps

For Android or iOS apps, integrate the AWS Mobile SDK for Android or iOS. To integrate,
see [Get
Started (Android and iOS)](../../../aws-mobile/latest/developerguide/getting-started.md "../../../aws-mobile/latest/developerguide/getting-started.md") in the _AWS Mobile Developer
Guide_. This topic helps you:

- Create a project with Mobile Hub. The **Messaging & Analytics** feature
  is enabled by default.
- Connect your app to the backend AWS resources that Mobile Hub provisions.
- Integrate the AWS Mobile SDK for Android or iOS with your app.

### For JavaScript Apps

For web or mobile JavaScript apps, integrate the AWS Amplify library. To integrate, see
[Get Started (Web)](../../../aws-mobile/latest/developerguide/web-getting-started.md "../../../aws-mobile/latest/developerguide/web-getting-started.md") or [Get Started (React Native)](../../../aws-mobile/latest/developerguide/react-native-getting-started.md "../../../aws-mobile/latest/developerguide/react-native-getting-started.md") in the _AWS Mobile Developer
Guide_. These topics help you:

- Use the AWS Mobile CLI to create a project. Analytics and web hosting are enabled by
  default.
- Create backend AWS resources for your app.
- Connect your app to the backend resources.
- Integrate the AWS Amplify library with your app.

## Step 3: Enable Amazon Pinpoint Analytics

Now that you've integrated the latest version of the AWS Mobile SDK or JavaScript library,
you can submit analytics events by using Amazon Pinpoint instead of Mobile Analytics.

### For Android or iOS Apps

To update your Android or iOS app, see [Add Analytics to your Mobile App with Amazon Pinpoint](../../../aws-mobile/latest/developerguide/add-aws-mobile-analytics.md "../../../aws-mobile/latest/developerguide/add-aws-mobile-analytics.md") in the _AWS
Mobile Developer Guide_.

### For JavaScript Apps

To update your JavaScript app, see [Add Analytics (Web)](../../../aws-mobile/latest/developerguide/web-add-analytics.md "../../../aws-mobile/latest/developerguide/web-add-analytics.md") or [Add Analytics (React Native)](../../../aws-mobile/latest/developerguide/react-native-add-analytics.md "../../../aws-mobile/latest/developerguide/react-native-add-analytics.md") in the _AWS Mobile Developer
Guide_.

## Step 4: Delete the Amazon Pinpoint Project That Mobile Hub

Created

When you created a project in Mobile Hub, a corresponding project was automatically created in
Amazon Pinpoint. You aren't using this Amazon Pinpoint project. Instead, you're using the project that
matches your original Mobile Analytics app.

1. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **Projects** page, find the project that was created by Mobile Hub.
   It's named as _mobilehubprojectname_\_MobileHub.
3. Copy the project ID.
4. Use a terminal to delete the project with the following AWS CLI command:

````
`$` `aws pinpoint delete-app --application-id `project-id```{
 "ApplicationResponse": {
 "Id": "d2b352520bcc4f5492ddbd7ef05f9147",
 "Name": "amamigrationdocstest_MobileHub"
 }
}`
````

The project is removed from Amazon Pinpoint.

## Step 5: Update the App ID in Your App

Configuration

Customize the default configuration for your app so that it reports analytics data to the
Amazon Pinpoint project for your Mobile Analytics app.

### For Android or iOS Apps

Your app now includes a cloud configuration file that connects it to the backend resources
that Mobile Hub creates. After you update the app ID in the file, your app sends
analytics data to the Amazon Pinpoint project for your Mobile Analytics app.

1. In your app package, open the `awsconfiguration.json`
   file.
2. In the `PinpointAnalytics` object, replace the value for `AppID`
   with the ID that you got from the Amazon Pinpoint console.

```
. . .
"PinpointAnalytics": {
  "Default": {
    "AppId": "`app-id`",
    "Region": "us-east-1"
  }
},
. . .
```

### For JavaScript Apps

Configure the AWS Amplify Analytics module in your app code so that your app reports
analytics data to the Amazon Pinpoint project for your Mobile Analytics app.

To update your app code, see the [Manual Setup](https://aws.github.io/aws-amplify/media/analytics_guide#manual-setup "https://aws.github.io/aws-amplify/media/analytics_guide#manual-setup") instructions for the Analytics module in the AWS Amplify
documentation. In the configuration code, for the `appID` parameter, use
the ID that you got from the Amazon Pinpoint console.

## Step 6: Update the App ID in the IAM

Role

When you created a project by using Mobile Hub or the AWS Mobile CLI, an IAM role was created
in your AWS account. This role includes a policy that allows your app to report events
and update endpoints with Amazon Pinpoint. The role includes the project ID for your Mobile Hub
project. Update this ID so that your app can communicate with the Amazon Pinpoint project for your
Mobile Analytics app.

1. Open the Mobile Hub console at [https://console.aws.amazon.com/mobilehub/](https://console.aws.amazon.com/mobilehub/ "https://console.aws.amazon.com/mobilehub/").
2. Choose the project that you created.
3. At the top-right of the console, choose **Resources**.
4. Under **AWS Identity and Access Management Roles**, the console shows the IAM role that was
   provisioned in your AWS account. Choose the role.

The IAM console opens, and the **Roles** page is
shown. 5. Under **Permissions**, expand the policy named as _project-name_\_mobileanalytics_MOBILEHUB\__mobile-hub-project-id_. 6. Choose **Edit policy**. 7. On the **Edit** page, choose the **JSON**
tab. 8. In the JSON editor, where the policy allows the
`mobiletargeting:UpdateEndpoint` action, update the value that's
assigned to the `Resource` key. Change the app ID to the ID that you
got from the Amazon Pinpoint console.

```
. . .
{
    "Effect": "Allow",
    "Action": [
        "mobiletargeting:UpdateEndpoint"
    ],
    "Resource": [
        "arn:aws:mobiletargeting:*:123456789012:apps/`app-id`*"
    ]
}
. . .
```

###### Important

Remember to keep the wildcard character (`*`) following the app ID. 9. Choose **Review policy**, and then choose **Save
changes**.

## Step 7: Build and Test

Now that you've integrated the latest AWS Mobile SDK or JavaScript library, and have
updated your app code, your app reports events to Amazon Pinpoint. As Amazon Pinpoint receives events, it
updates the charts on the **Analytics** pages in the console.

1. Build your updated app, and run it on a test device or emulator.
2. Launch your app, and perform other actions in your app that cause it to report
   events to Amazon Pinpoint.
3. Open the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
4. On the **Projects** page, choose the project for your
   app.
5. In the navigation menu, choose **Analytics**.
6. Check the charts to verify whether Amazon Pinpoint is showing the analytics that you expect. For
   example, the **Sessions** chart indicates how many times you
   open the app, and the **New endpoints** chart indicates how
   many test devices or emulators launch the app for the first time. Custom events
   are shown on the **Events** page. Allow up to 15 minutes for
   the charts to display an event.
