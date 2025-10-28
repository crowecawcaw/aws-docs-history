# Controlling access using IAM

You can use AWS Identity and Access Management (IAM) to manage access to your
Cost Management preferences for individual users. You can then grant or revoke
access on an individual level for each IAM role or user. You’ll need to add the
following actions in order to be able to view and edit preferences:
`ce:GetPreferences`, `ce:UpdatePreferences`,
`ce:GetDimensionValues`, and
`ce:GetApproximateUsageRecords`.

The following is a sample IAM policy with the relevant actions that would provide
you with access to view and edit your Cost Management preferences in order to enable
multi-year and granular data:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "ce:GetPreferences",
 "ce:UpdatePreferences",
 "ce:GetDimensionValues",
 "ce:GetApproximateUsageRecords"
 ],
 "Resource": "*"
 }
 ]
}`

```
