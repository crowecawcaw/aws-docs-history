# Getting started with dashboards

AWS Billing and Cost Management Dashboards are collections of widgets that visualize your
cost and usage data. Each dashboard can contain up to 20 widgets, which can show costs, usage,
and savings plans and reserved instances coverage and utilization, budgets data, and cost efficiency metrics. One of the powerful features
of dashboards is that they can be shared within or outside your organization, allowing for
collaborative cost management.

## Prerequisites

Before creating or using dashboards, ensure you have:

- Activated the required IAM user and role access to the Billing and Cost Management
  console. For more information about IAM actions, see [Using identity-based policies (IAM policies) for AWS Cost Management](billing-permissions-ref.md "billing-permissions-ref.md").
- Enabled fine-grained AWS IAM actions for AWS Billing and Cost Management. For more
  information, see [Changes to AWS Billing, Cost Management, and Account Consoles
  Permissions](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/").
- (Optional) Enabled AWS RAM sharing with AWS Organizations if you plan to share
  dashboards within your organization. For more information, see [How AWS RAM
  works with IAM](../../../ram/latest/userguide/security-iam-policies.md "../../../ram/latest/userguide/security-iam-policies.md") in the _AWS Resource Access Manager User
  Guide_.
- (Optional) If you are setting up email delivery for a scheduled report for a user for the first time, the user will need to verify their email address through a one time verification email before they can start receiving scheduled reports.

###### Note

Creating dashboards using AWS CloudFormation is not currently supported.

To share dashboards with member accounts in your organization, you must access the
management account of your organization using an IAM principal that has permissions to create
and share resources using AWS Resource Access Manager (AWS RAM). Permissions are not
required for member accounts that receive a shared dashboard. To learn more, see [Sharing
dashboards](share-dashboards.md "share-dashboards.md"). For details about IAM actions for sharing dashboards, see [How AWS RAM
works with IAM](../../../ram/latest/userguide/security-iam-policies.md "../../../ram/latest/userguide/security-iam-policies.md") in the _AWS Resource Access Manager User
Guide_.

## Accessing Dashboards

You can access Dashboards from the Billing and Cost Management console.

To access Dashboards

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Dashboards**.

## Understanding dashboard permissions

Dashboard permissions are managed through IAM policies. To work with dashboards
effectively, you need to understand both the permissions required for managing dashboards and
those needed for accessing the underlying data.

Required dashboard permissions include:

- `CreateDashboard` - Create new dashboards
- `GetDashboard` - View dashboard details
- `UpdateDashboard` - Modify existing dashboards
- `DeleteDashboard` - Remove dashboards
- `ListDashboards` - View available dashboards
- `CreateScheduledReport` - Create scheduled email reports
- `GetScheduledReport` - View scheduled report details
- `UpdateScheduledReport` - Modify scheduled report configurations
- `DeleteScheduledReport` - Remove scheduled report configurations
- `ListScheduledReports` - View available scheduled reports
- `ExecuteScheduledReport` - Triggers immediate execution of a scheduled report

The following is an example IAM policy that grants all dashboard permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "bcm-dashboards:CreateDashboard",
 "bcm-dashboards:GetDashboard",
 "bcm-dashboards:UpdateDashboard",
 "bcm-dashboards:DeleteDashboard",
 "bcm-dashboards:ListDashboards"
 ],
 "Resource": "*"
 }
 ]
}`

```

When working with dashboards, users need permissions to access the dashboard resource
itself and permissions to access the underlying cost and usage data APIs. For shared
dashboards, permissions are managed through AWS RAM.

###### Note

To schedule email delivery of dashboard reports, you also need the following
permissions:

- `iam:PassRole` – Required for passing the IAM execution role to the
  API.
- `bcm-dashboards:GetDashboard`, `ce:GetDimensionValues`,
  `ce:GetCostAndUsageWithResources`, `ce:GetCostAndUsage`,
  `ce:GetCostForecast`, `ce:GetTags`,
  `ce:GetUsageForecast`, `ce:GetCostCategories`,
  `ce:GetSavingsPlansCoverage`, `ce:GetReservationUtilization`,
  `ce:GetReservationCoverage`, `ce:GetSavingsPlansUtilization`,
  `ce:GetSavingsPlansUtilizationDetails`, `budgets:ViewBudget`, `budgets:DescribeBudgetActionsForAccount`, `cost-optimization-hub:ListEfficiencyMetrics`, `billing:ListBillingViews` – Required for the execution role
  to retrieve dashboard and cost data. For more information, see [Execution role permissions for scheduled reports](schedule-dashboard-reports.md#schedule-dashboard-reports-permissions "schedule-dashboard-reports.md#schedule-dashboard-reports-permissions").
