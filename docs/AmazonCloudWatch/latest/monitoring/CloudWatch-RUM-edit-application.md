# Editing your CloudWatch RUM app monitor settings

To change an app monitor's settings, follow these steps. You can
change any settings except the app monitor name.

###### To edit how your application uses CloudWatch RUM

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **RUM**.
3. Choose **List view**.
4. Choose the button next to the name of the application, and then choose **Actions**,
   **Edit**.
5. Change any settings except the application name. For more information about the settings,
   see [Creating a CloudWatch RUM app monitor](CloudWatch-RUM-get-started-create-app-monitor.md "CloudWatch-RUM-get-started-create-app-monitor.md").
6. When finished, choose **Save**.

Changing the settings changes the code snippet. You must now paste the updated
code snippet into your application. 7. After the JavaScript code snippet is created, choose **Copy to clipboard** or
**Download**, and then choose
**Done**.

To start monitoring with the new settings, you insert the code snippet into your application.
Insert the code snippet inside the `<head>`
element of your application,
before the `<body>` element or any other `<script>` tags.
