# IAM role required for creating applications in Amazon Connect Agent Workspace

On top of the `AmazonConnect_FullAccess` IAM policy, users need the following IAM permissions for creating an app
and associating it with an Amazon Connect instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "app-integrations:CreateApplication",
 "app-integrations:GetApplication",
 "iam:GetRolePolicy",
 "iam:PutRolePolicy",
 "iam:DeleteRolePolicy"
 ],
 "Resource": "arn:aws:app-integrations:`us-east-1`:`111122223333`:application/*",
 "Effect": "Allow"
 }
 ]
}`

```
