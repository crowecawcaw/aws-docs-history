# Resource: Read-only access for AWS Batch

The following policy grants users permissions to use all AWS Batch API actions with a name
that starts with `Describe` and `List`.

Unless another statement grants them permission to do so, users don't have permission to
perform any actions on the resources. By default, they're denied permission to use API
actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "batch:Describe*",
 "batch:List*",
 "batch:Get*"
 ],
 "Resource": "*"
 }
 ]
}`

```
