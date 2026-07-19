# Manual approval execution block sample policy

The following is a sample policy to attach if you add execution blocks to a Region switch plan for manual approvals.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "arc-region-switch:ApprovePlanExecutionStep"
 ],
 "Resource": "arn:aws:arc-region-switch::123456789012:plan/sample-plan:0123abc"
 }
 ]
}`

```
