# Troubleshooting the Amazon Q Developer dashboard

If the Amazon Q Developer dashboard page is not available, do the following:

- **Verify your permissions**. To view the dashboard, you need the
  following permissions:
  - `q:ListDashboardMetrics`
  - `codewhisperer:ListProfiles`
  - `sso:ListInstances`
  - `user-subscriptions:ListUserSubscriptions`
  - To see metrics generated before November 22, 2024, you also need:
    `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics`

  For more information about permissions, see [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").

- **Verify your settings**. In the Amazon Q Developer console, choose
  **Settings** and make sure that the **Amazon Q Developer usage dashboard**
  toggle is enabled.
  For more information about the dashboard, see [Viewing usage metrics (dashboard)](dashboard.md "dashboard.md").
