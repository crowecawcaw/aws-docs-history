# Region switch plan execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan to run child plans.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "arc-region-switch:StartPlanExecution",
 "arc-region-switch:GetPlanExecution",
 "arc-region-switch:CancelPlanExecution",
 "arc-region-switch:UpdatePlanExecution",
 "arc-region-switch:ListPlanExecutions"
 ],
 "Resource": [
 "arn:aws:arc-region-switch::123456789012:plan/child-plan-1/abcde1",
 "arn:aws:arc-region-switch::123456789012:plan/child-plan-2/fghij2"
 ]
 }
 ]
}`

```
