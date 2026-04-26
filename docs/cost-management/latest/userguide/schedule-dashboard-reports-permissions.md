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
        "ce:GetSavingsPlansUtilizationDetails"
      ],
      "Resource": "*"
    }
  ]
}
```

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
