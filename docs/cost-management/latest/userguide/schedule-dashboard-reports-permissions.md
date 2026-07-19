# Execution role permissions for scheduled reports

When you create a scheduled report, you must provide an IAM execution role that grants
AWS Billing and Cost Management permissions to generate and deliver reports on your behalf.
The execution role requires the following permissions and trust policy.

**Permissions policy**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AwsBcmDashboardsScheduleReportsDataAccess",
      "Effect": "Allow",
      "Action": [
        "bcm-dashboards:GetDashboard"
      ],
      "Resource": [
        "arn:aws:bcm-dashboards::*:dashboard/*"
      ]
    },
    {
      "Sid": "AwsBcmDashboardsScheduleReportsDataAccessCE",
      "Effect": "Allow",
      "Action": [
        "ce:GetDimensionValues",
        "ce:GetCostAndUsageWithResources",
        "ce:GetCostAndUsage",
        "ce:GetCostForecast",
        "ce:GetTags",
        "ce:GetUsageForecast",
        "ce:GetCostCategories",
        "ce:GetSavingsPlansCoverage",
        "ce:GetReservationUtilization",
        "ce:GetReservationCoverage",
        "ce:GetSavingsPlansUtilization",
        "ce:GetSavingsPlansUtilizationDetails",
        "budgets:ViewBudget",
        "budgets:DescribeBudgetActionsForAccount",
        "cost-optimization-hub:ListEfficiencyMetrics",
        "billing:ListBillingViews"
      ],
      "Resource": "*"
    }
  ]
}

```

###### Note

If you created an execution role before the launch of the AWS Budgets report widget, your existing role will not include the budgets API permissions. To schedule reports for dashboards that contain AWS Budgets report widgets, update your execution role to include the budgets permissions listed above. You can update your service roles from the Additional configuration section when creating or editing a scheduled report. This update will fail if a role was manually modified in IAM. To resolve this, create a new role or restore the policy version to its original state. For more information, see [Setting the default version of a policy](../../../IAM/latest/UserGuide/access_policies_manage-edit-console.md "../../../IAM/latest/UserGuide/access_policies_manage-edit-console.md") in the _IAM User Guide_.

**Trust policy**

The execution role must trust the `bcm-dashboards.amazonaws.com` service
principal. Replace `<account-id>` with your AWS account ID.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowBcmDashboardScheduledReportAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "bcm-dashboards.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<account-id>"
        },
        "StringLike": {
          "aws:SourceArn": "arn:aws:bcm-dashboards::<account-id>:*"
        }
      }
    }
  ]
}
```
