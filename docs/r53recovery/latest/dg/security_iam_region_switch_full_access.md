# Full access permissions

The following IAM policy grants full access for all Region switch APIs:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "arc-region-switch.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "arc-region-switch:CreatePlan",
 "arc-region-switch:UpdatePlan",
 "arc-region-switch:GetPlan",
 "arc-region-switch:ListPlans",
 "arc-region-switch:DeletePlan",
 "arc-region-switch:GetPlanInRegion",
 "arc-region-switch:ListPlansInRegion",
 "arc-region-switch:ApprovePlanExecutionStep",
 "arc-region-switch:GetPlanEvaluationStatus",
 "arc-region-switch:GetPlanExecution",
 "arc-region-switch:StartPlanExecution",
 "arc-region-switch:CancelPlanExecution",
 "arc-region-switch:ListRoute53HealthChecks",
 "arc-region-switch:ListPlanExecutions",
 "arc-region-switch:ListPlanExecutionEvents",
 "arc-region-switch:ListTagsForResource",
 "arc-region-switch:TagResource",
 "arc-region-switch:UntagResource",
 "arc-region-switch:UpdatePlanExecution",
 "arc-region-switch:UpdatePlanExecutionStep"
 ],
 "Resource": "*"
 }
 ]
}`

```
