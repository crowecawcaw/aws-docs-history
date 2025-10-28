# Sharing dashboards

You can share dashboards with accounts in your AWS Organization or with external accounts
(using AWS Resource Access Manager). When you share a dashboard, only dashboard configurations
are shared, not the underlying data. Recipients receive access to the dashboard layout and
widget configurations, and will see data based on their own access permissions.

The shared configuration includes all filter values, tag keys and values, and widget
parameters. For example, if you have widgets filtered to show data for specific accounts, those
account numbers will be visible to recipients in the filter configurations. Similarly, any tag
keys and values used in your dashboard will be visible in the shared configuration.

###### To share a dashboard

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Dashboards**.
3. Select the dashboard you want to share.
4. Choose **Share**.
5. Select the accounts you want to share the dashboard with:
   - Share with accounts in your AWS Organization
   - Share with external AWS accounts

6. Set permissions:
   - Read-only access ("Can view") Recipients can view the dashboard but cannot make
     changes
   - Edit access ("Can edit") Recipients can view and modify the dashboard
     configuration

7. Choose **Share**.
   When you share a dashboard, new resource shares are automatically created in AWS RAM. If
   AWS RAM sharing with AWS Organizations is enabled, users in recipient accounts can access
   shared dashboards immediately (subject to their identity-based IAM permissions). If AWS RAM
   sharing with Organizations is not enabled, administrators in recipient accounts will need to
   accept the resource share invitation.

###### Note

- If sharing outside your organization, recipients must accept the share invitation in
  AWS RAM. Recipients should navigate to **Resource shares** under
  **Shared with me** in the AWS RAM console, ensuring they are in the
  same Region where the share was created. After selecting and accepting the invitation in
  **Resource shares**, the shared dashboard will appear in the
  recipient's Billing and Cost Management console under **Dashboards**. If
  the invitation is not immediately visible, recipients should verify they are using the
  correct AWS account and Region.
- To view or edit shared dashboards, users in recipient accounts must have appropriate
  IAM permissions (for example, `ListDashboards`,
  `GetDashboard`).
- To see data in shared dashboards, users must also have permissions to the underlying
  APIs that provide that data (for example, `GetCostAndUsage`).
- You can revoke access to shared dashboards at any time.
