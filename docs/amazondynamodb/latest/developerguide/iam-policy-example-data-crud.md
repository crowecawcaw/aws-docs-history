# IAM policy to read, write, update, and delete access on a DynamoDB table

Use this policy if you need to allow your application to create, read, update, and
delete data in Amazon DynamoDB tables, indexes, and streams. Substitute the AWS Region
name, your account ID, and the table name or wildcard character (\*) where
appropriate.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DynamoDBIndexAndStreamAccess",
 "Effect": "Allow",
 "Action": [
 "dynamodb:GetShardIterator",
 "dynamodb:Scan",
 "dynamodb:Query",
 "dynamodb:DescribeStream",
 "dynamodb:GetRecords",
 "dynamodb:ListStreams"
 ],
 "Resource": [
 "arn:aws:dynamodb:us-west-2:123456789012:table/Books/index/*",
 "arn:aws:dynamodb:us-west-2:123456789012:table/Books/stream/*"
 ]
 },
 {
 "Sid": "DynamoDBTableAccess",
 "Effect": "Allow",
 "Action": [
 "dynamodb:BatchGetItem",
 "dynamodb:BatchWriteItem",
 "dynamodb:ConditionCheckItem",
 "dynamodb:PutItem",
 "dynamodb:DescribeTable",
 "dynamodb:DeleteItem",
 "dynamodb:GetItem",
 "dynamodb:Scan",
 "dynamodb:Query",
 "dynamodb:UpdateItem"
 ],
 "Resource": "arn:aws:dynamodb:us-west-2:123456789012:table/Books"
 },
 {
 "Sid": "DynamoDBDescribeLimitsAccess",
 "Effect": "Allow",
 "Action": "dynamodb:DescribeLimits",
 "Resource": [
 "arn:aws:dynamodb:us-west-2:123456789012:table/Books",
 "arn:aws:dynamodb:us-west-2:123456789012:table/Books/index/*"
 ]
 }
 ]
}`

```

To expand this policy to cover all DynamoDB tables in all AWS Regions for this
account, use a wildcard (\*) for the Region and table name. For example:

```
"Resource":[
                "arn:aws:dynamodb:*:123456789012:table/*",
                "arn:aws:dynamodb:*:123456789012:table/*/index/*"
                ]
```
