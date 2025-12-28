# Read-only permissions

The following IAM policy grants read-only access permissions for Region switch:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "arc-region-switch:GetPlan",
 "arc-region-switch:ListPlans",
 "arc-region-switch:GetPlanInRegion",
 "arc-region-switch:ListPlansInRegion",
 "arc-region-switch:GetPlanEvaluationStatus",
 "arc-region-switch:GetPlanExecution",
 "arc-region-switch:ListRoute53HealthChecks",
 "arc-region-switch:ListRoute53HealthChecksInRegion",
 "arc-region-switch:ListPlanExecutions",
 "arc-region-switch:ListPlanExecutionEvents",
 "arc-region-switch:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```
