# Complete plan execution role permissions

Creating a comprehensive policy that includes permissions for all execution blocks would require a policy that is quite large. In practice, you
should only include permissions for the execution blocks that you use in your specific plans.

The following is an example policy that you can use as a starting place for a plan execution role policy. Make sure that
you add additional policies that required for specific execution blocks that you include in your plan. Only include
the permissions required for the specific execution blocks that you use in your plan, to follow the principle of least privilege

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:SimulatePrincipalPolicy",
 "Resource": "arn:aws:iam::123456789012:role/RegionSwitchExecutionRole"
 },
 {
 "Effect": "Allow",
 "Action": [
 "arc-region-switch:GetPlan",
 "arc-region-switch:GetPlanExecution",
 "arc-region-switch:ListPlanExecutions"
 ],
 "Resource": "*"
 }
 ]
}`

```
