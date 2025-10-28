# Amazon RDS: Allows full RDS database access

within a specific Region

This example shows how you might create an identity-based policy that allows full RDS database access within a specific Region.
This policy grants the permissions necessary to complete this action programmatically from the AWS API or AWS CLI. To use this policy, replace the `italicized placeholder text` in the example policy with your own information.
Then, follow the directions in [create a policy](access_policies_create.md "access_policies_create.md") or [edit a policy](access_policies_manage-edit.md "access_policies_manage-edit.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "rds:*",
 "Resource": ["arn:aws:rds:`us-east-1`:*:*"]
 },
 {
 "Effect": "Allow",
 "Action": ["rds:Describe*"],
 "Resource": ["*"]
 }
 ]
}`

```
