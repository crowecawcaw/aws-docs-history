

# Scheduling email delivery of dashboard reports
<a name="schedule-dashboard-reports"></a>

You can schedule automated email delivery of your dashboard reports to stakeholders on a recurring basis. Scheduled reports generate a PDF snapshot of your dashboard at the configured time and deliver it to your specified recipients through email. This allows stakeholders who don't have AWS console access to receive regular visibility into cost and usage data.

Each scheduled report is configured with a delivery frequency (daily, weekly, or monthly), a specific delivery time, and a list of recipients. You can schedule delivery of your entire dashboard or a single widget. Report generation begins at the scheduled time and delivery follows shortly after.

When changes are made to a dashboard, they are automatically reflected in subsequent scheduled deliveries without requiring reconfiguration of the report.

**Note**  
Scheduled email delivery is available only for dashboards that you create. To schedule email delivery for a Managed Dashboard, first duplicate it as a custom dashboard, then configure the scheduled report on your custom copy.  
To schedule email delivery, you need permissions for `bcm-dashboards:CreateScheduledReport`.

**Note**  
AWS User Notifications is automatically configured in your account, including Notification Hubs, when you schedule email delivery of a dashboard report. For more information, see [Getting started with AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html) in the *AWS User Notifications User Guide*.

**Topics**
+ [Execution role permissions for scheduled reports](schedule-dashboard-reports-permissions.md)
+ [Creating a scheduled report](schedule-dashboard-reports-create.md)
+ [Understanding scheduled report emails](schedule-dashboard-reports-emails.md)
+ [Managing scheduled reports](schedule-dashboard-reports-manage.md)