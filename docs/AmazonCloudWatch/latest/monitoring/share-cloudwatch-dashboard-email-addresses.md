# Sharing a CloudWatch dashboard with specific users

Use the steps in this section to share a dashboard with as many as five email addresses that you choose.

###### Note

By default, any CloudWatch Logs widgets on the dashboard are not visible to people who you share the dashboard with.
For more information, see [Allowing people that you share with to see logs table widgets](cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-logwidget "cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-logwidget").

By default, any composite alarm widgets on the dashboard are not visible to people who you share the dashboard with.
For more information, see [Allowing people that you share with to see composite alarms](cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-composite-alarms "cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-composite-alarms").

###### To share a dashboard with specific users

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**.
3. Choose the name of your dashboard.
4. Choose **Actions**, **Share dashboard**.
5. Next to **Share your dashboard and require a username and password**,
   choose **Start sharing**.
6. Under **Add email addresses**, enter the email addresses that
   you want to share the dashboard with. You can include as many as five email addresses.
7. When you have all the email addresses entered, read the agreement and select the
   confirmation box. Then choose **Preview policy**.
8. Confirm that the resources that will be shared are what you want, and choose **Confirm and generate shareable link**.
9. On the next page, choose **Copy link to clipboard**. You can then paste this
   link into email and send it to the invited users. They automatically receive
   a separate email with their user name and a temporary password to use to
   connect to the dashboard.
