# IAM policy to allow an AWS Lambda function to access DynamoDB stream records

If you want certain actions to be performed based on events in a DynamoDB stream, you
can write an AWS Lambda function that is triggered by these events. A Lambda function
such as this needs permissions to read data from a DynamoDB stream. For more
information about using Lambda with DynamoDB Streams, see [DynamoDB Streams and AWS Lambda triggers](Streams.md "Streams.md").

To grant permissions to Lambda, use the permissions policy that is associated with
the Lambda function's IAM role (also known as an execution role). Specify this policy when you create the Lambda
function.

For example, you can associate the following permissions policy with an execution
role to grant Lambda permissions to perform the DynamoDB Streams actions listed.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "APIAccessForDynamoDBStreams",
 "Effect": "Allow",
 "Action": [
 "dynamodb:GetRecords",
 "dynamodb:GetShardIterator",
 "dynamodb:DescribeStream",
 "dynamodb:ListStreams"
 ],
 "Resource": "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores/stream/*"
 }
 ]
}`

```

For more information, see [AWS Lambda permissions](../../../lambda/latest/dg/intro-permission-model.md "../../../lambda/latest/dg/intro-permission-model.md") in the
_AWS Lambda Developer Guide_.
