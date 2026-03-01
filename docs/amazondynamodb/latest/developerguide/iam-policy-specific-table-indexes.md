# IAM policy to grant access to a specific DynamoDB table and its indexes

The following policy grants permissions for data modification actions on a DynamoDB
table called `Books` and all of that table's indexes. For more
information about how indexes work, see [Improving data access with secondary indexes in DynamoDB](SecondaryIndexes.md "SecondaryIndexes.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessTableAllIndexesOnBooks",
 "Effect": "Allow",
 "Action": [
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem",
 "dynamodb:BatchWriteItem",
 "dynamodb:GetItem",
 "dynamodb:BatchGetItem",
 "dynamodb:Scan",
 "dynamodb:Query",
 "dynamodb:ConditionCheckItem"
 ],
 "Resource": [
 "arn:aws:dynamodb:us-west-2:123456789012:table/Books",
 "arn:aws:dynamodb:us-west-2:123456789012:table/Books/index/*"
 ]
 }
 ]
}`

```
