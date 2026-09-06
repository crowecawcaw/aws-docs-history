

# Creating a scheduled report
<a name="schedule-dashboard-reports-create"></a>

You can create a scheduled report for a dashboard to automatically generate and deliver PDF snapshots to your recipients on a recurring basis.

**To create a scheduled report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Dashboards**.

1. Select the dashboard you want to schedule for email delivery.

1. Choose **Actions**, and then choose **Manage email reports**.

1. Choose **Create report**.

1. **Create report details** - Configure the basic information about the report:
   + **Report name** - Enter a name for the report.
   + **Description** (optional) - Enter a description to help identify your report.
   + **Widget selection** - Choose **Full dashboard** (default) to include all widgets, or **Single widget** to limit the report to one widget.
   + **Reporting period** - Choose **Widget-specific ranges** to preserve each widget's individual date range settings, or apply a unified date range for all widgets. Relative date ranges update with each delivery to provide the most relevant data based on when the report is generated.

   Use **Preview report** to verify the layout before proceeding. Choose **Next**.

1. **Select recipients** - Configure the notification settings for recipients:
   + **Email setup method** - Choose **Select from existing configurations** to use a previously configured [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) configuration, or choose **Enter new email address** to create a new configuration that multiple reports can use for delivery.

   First-time recipients must verify their email address. For non-AWS users, you can use email distribution lists — only one team member with AWS console access needs to verify the list address, after which all members receive dashboard reports automatically. Choose **Next**.

1. **Configure report scheduling** - Configure when and how often the report will be delivered:
   + **Frequency** - Choose **Daily**, **Weekly**, or **Monthly**.
   + **Delivery time (UTC)** - Specify the time when the report will be generated. Reports are usually delivered within a few minutes of the scheduled time
   + **Start date** - Select when to start sending the report.
   + **End date** - Select when to stop sending the report. Maximum allowed duration is three years from the start date.

   Choose **Next**.

1. **Configure additional settings** - Set up service access and optional tags:
   + **Service access** - Grant AWS Billing and Cost Management permissions to generate and deliver scheduled PDF reports, access permitted cost and usage data, and manage email delivery on your behalf. Choose one of the following:
     + **Create and use a new execution role** - Recommended for first-time setup. Creates a new IAM role with the permissions required for scheduled report generation and delivery. For more information, see [Execution role permissions for scheduled reports](schedule-dashboard-reports-permissions.md).
     + **Choose an existing execution role** - Select a previously created execution role from your account. Use this if you have already created a role for scheduled reports.
     + **Enter execution role ARN manually** - Specify the ARN of an execution role directly. Use this if the role was created in a different context or if you manage roles through infrastructure as code.
   + **Resource tags** (optional) - Add tags to help search and filter your resources or track costs. You can add up to 50 tags.

   Choose **Next**.

1. **Review and create** - Review all your selections across the previous steps. You can choose **Edit** next to any step to modify its settings. When satisfied, choose **Create**.

**Note**  
Recipients receive an email containing a secure link to download the password-protected PDF report. The password is included in the email body. The download link expires after 15 days. No AWS permissions are required to download or view the PDF report.