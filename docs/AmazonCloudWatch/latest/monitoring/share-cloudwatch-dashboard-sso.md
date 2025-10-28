# Sharing all CloudWatch dashboards in the account by using

SSO

Use the steps in this section to share all the dashboards in your account with
users by using single sign-on (SSO).

###### Note

By default, any CloudWatch Logs widgets on the dashboard are not visible to people who you share the dashboard with.
For more information, see [Allowing people that you share with to see logs table widgets](cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-logwidget "cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-logwidget").

By default, any composite alarm widgets on the dashboard are not visible to people who you share the dashboard with.
For more information, see [Allowing people that you share with to see composite alarms](cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-composite-alarms "cloudwatch-dashboard-sharing.md#share-cloudwatch-dashboard-composite-alarms").

###### To share your CloudWatch dashboards with users who are in an SSO provider's list

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**.
3. Choose the name of your dashboard.
4. Choose **Actions**, **Share dashboard**.
5. Choose **Go to CloudWatch Settings**.
6. If the SSO provider that you want
   isn't listed in **Available SSO providers**,
   choose
   **Manage SSO providers** and follow the instructions
   in [Setting up SSO for CloudWatch dashboard
   sharing](share-cloudwatch-dashboards-setup-SSO.md "share-cloudwatch-dashboards-setup-SSO.md").

Then return to the CloudWatch console and refresh the browser. The SSO provider
that you enabled should now appear in the list. 7. Choose the SSO provider that you want in the **Available SSO providers**
list. 8. Choose **Save changes**.
