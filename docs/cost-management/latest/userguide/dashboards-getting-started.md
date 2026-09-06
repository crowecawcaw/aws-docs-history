

# Getting started with dashboards
<a name="dashboards-getting-started"></a>

AWS Billing and Cost Management Dashboards are collections of widgets that visualize your cost and usage data. Each dashboard can contain up to 20 widgets, which can show costs, usage, and savings plans and reserved instances coverage and utilization, budgets data, and cost efficiency metrics. One of the powerful features of dashboards is that they can be shared within or outside your organization, allowing for collaborative cost management.

## Prerequisites
<a name="dashboards-prerequisites"></a>

Before creating or using dashboards, ensure you have:
+ Activated the required IAM user and role access to the Billing and Cost Management console. For more information about IAM actions, see [Using identity-based policies (IAM policies) for AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html).
+ Enabled fine-grained AWS IAM actions for AWS Billing and Cost Management. For more information, see [Changes to AWS Billing, Cost Management, and Account Consoles Permissions](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/).
+ (Optional) Enabled AWS RAM sharing with AWS Organizations if you plan to share dashboards within your organization. For more information, see [How AWS RAM works with IAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies.html) in the *AWS Resource Access Manager User Guide*.
+ (Optional) If you are setting up email delivery for a scheduled report for a user for the first time, the user will need to verify their email address through a one time verification email before they can start receiving scheduled reports.

**Note**  
Creating dashboards using AWS CloudFormation is not currently supported.

To share dashboards with member accounts in your organization, you must access the management account of your organization using an IAM principal that has permissions to create and share resources using AWS Resource Access Manager (AWS RAM). Permissions are not required for member accounts that receive a shared dashboard. To learn more, see [Sharing dashboards](https://docs.aws.amazon.com/cost-management/latest/userguide/share-dashboards.html). For details about IAM actions for sharing dashboards, see [How AWS RAM works with IAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies.html) in the *AWS Resource Access Manager User Guide*.

## Accessing Dashboards
<a name="dashboards-console"></a>

You can access Dashboards from the Billing and Cost Management console.

To access Dashboards

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Dashboards**.

## Understanding your dashboard list
<a name="dashboards-types"></a>

Your dashboard list can contain dashboards from three sources, and what you can edit depends on where a dashboard came from.
+ Dashboards that you create are fully editable. You choose which widgets to add, configure them, and arrange the layout, and you can share a dashboard that you own with other accounts.
+ Managed Dashboards are preconfigured by AWS. They appear in your dashboard list automatically, are populated with your own account data, and are read-only. Managed Dashboards are identified by a lock icon. To change a Managed Dashboard, duplicate it. The copy is a dashboard that you own and can edit freely.
+ Dashboards that are shared with you were created in another account and shared with you through AWS Resource Access Manager (AWS RAM). You can view them, but only the owning account can change them.

On the dashboard list page, you can use tabs to filter your list: **All dashboards**, **Managed**, and **Shared with me**.

## Understanding dashboard permissions
<a name="dashboards-permissions"></a>

Dashboard permissions are managed through IAM policies. To work with dashboards effectively, you need to understand both the permissions required for managing dashboards and those needed for accessing the underlying data.

Required dashboard permissions include:
+ `CreateDashboard` - Create new dashboards
+ `GetDashboard` - View dashboard details
+ `UpdateDashboard` - Modify existing dashboards
+ `DeleteDashboard` - Remove dashboards
+ `ListDashboards` - View available dashboards
+ `CreateScheduledReport` - Create scheduled email reports
+ `GetScheduledReport` - View scheduled report details
+ `UpdateScheduledReport` - Modify scheduled report configurations
+ `DeleteScheduledReport` - Remove scheduled report configurations
+ `ListScheduledReports` - View available scheduled reports
+ `ExecuteScheduledReport` - Triggers immediate execution of a scheduled report

The following is an example IAM policy that grants all dashboard permissions:

------
#### [ JSON ]

****  

```
{
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
}
```

------

When working with dashboards, users need permissions to access the dashboard resource itself and permissions to access the underlying cost and usage data APIs. For shared dashboards, permissions are managed through AWS RAM.

**Note**  
To schedule email delivery of dashboard reports, you also need the following permissions:  
`iam:PassRole` – Required for passing the IAM execution role to the API.
`bcm-dashboards:GetDashboard`, `ce:GetDimensionValues`, `ce:GetCostAndUsageWithResources`, `ce:GetCostAndUsage`, `ce:GetCostForecast`, `ce:GetTags`, `ce:GetUsageForecast`, `ce:GetCostCategories`, `ce:GetSavingsPlansCoverage`, `ce:GetReservationUtilization`, `ce:GetReservationCoverage`, `ce:GetSavingsPlansUtilization`, `ce:GetSavingsPlansUtilizationDetails`, `budgets:ViewBudget`, `budgets:DescribeBudgetActionsForAccount`, `cost-optimization-hub:ListEfficiencyMetrics`, `billing:ListBillingViews` – Required for the execution role to retrieve dashboard and cost data. For more information, see [Execution role permissions for scheduled reports](https://docs.aws.amazon.com/cost-management/latest/userguide/schedule-dashboard-reports.html#schedule-dashboard-reports-permissions).

**Note**  
Viewing AWS Managed Dashboards requires `ListDashboards` and `GetDashboard` permissions. If you attempt write operations (`UpdateDashboard`, `DeleteDashboard`) on a Managed Dashboard, the API returns a `AccessDeniedException`.