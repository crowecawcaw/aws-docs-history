# IAM policy to grant read-only permissions on items in a DynamoDB table

The following permissions policy grants permissions for the `GetItem`,
`BatchGetItem`, `Scan`, `Query`, and
`ConditionCheckItem` DynamoDB actions only, and as a result, sets
read-only access on the `Books` table.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadOnlyAPIActionsOnBooks",
 "Effect": "Allow",
 "Action": [
 "dynamodb:GetItem",
 "dynamodb:BatchGetItem",
 "dynamodb:Scan",
 "dynamodb:Query",
 "dynamodb:ConditionCheckItem"
 ],
 "Resource": "arn:aws:dynamodb:us-west-2:123456789012:table/Books"
 }
 ]
}`

```
