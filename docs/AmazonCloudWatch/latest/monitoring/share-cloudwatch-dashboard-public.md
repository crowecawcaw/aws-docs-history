# Sharing a CloudWatch dashboard publicly

Follow the steps in this section to share a dashboard publicly. This can be useful
to display the dashboard on a big screen in a team room, or embed it in a Wiki
page.

###### Important

Sharing a dashboard publicly makes it accessible to anyone who has the link, with no
authentication. Do this only for dashboards that do not contain sensitive information.

###### Note

By default, any CloudWatch Logs widgets on the dashboard are not visible to people who you share the dashboard with.
For more information, see [Allowing people that you share with to see logs table widgets](cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-logwidget "cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-logwidget").

By default, any composite alarm widgets on the dashboard are not visible to people who you share the dashboard with.
For more information, see [Allowing people that you share with to see composite alarms](cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-composite-alarms "cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-composite-alarms").

###### To share a dashboard publicly

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**.
3. Choose the name of your dashboard.
4. Choose **Actions**, **Share dashboard**.
5. Next to **Share your dashboard publicly**,
   choose **Start sharing**.
6. Enter `Confirm` in the text box.
7. Read the agreement and select the
   confirmation box. Then choose **Preview policy**.
8. Confirm that the resources that will be shared are what you want, and choose **Confirm and generate shareable link**.
9. On the next page, choose **Copy link to clipboard**. You can then
   share this link. Anyone you share the link with can access the dashboard, without
   providing credentials.
