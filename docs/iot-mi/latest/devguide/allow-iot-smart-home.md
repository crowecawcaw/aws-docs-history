# Invoke your C2C connector

AWS Lambda allows for resource-based policies to authorize who can invoke a Lambda. As
managed integrations for AWS IoT Device Management is an AWS service, you must allow managed integrations to invoke your C2C connector
Lambda via the resource policy.

Attach a resource policy with at least the following minimal permissions to your C2C connector Lambda. This provides
managed integrations with Lambda function invoke privileges. This policy includes a `Condition` key
to help you limit the usability of your `connectorId` to only intended users.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "default",
 "Statement": [
 {
 "Sid": "Your-Desired-Policy-ID",
 "Effect": "Allow",
 "Principal": {
 "Service": "iotmanagedintegrations.amazonaws.com"
 },
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:`ca-central-1`:`123456789012`:function:connector-lambda-name",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:iotmanagedintegrations:`ca-central-1`:`123456789012`:`account-association`/`account-association-id`"
 }
 }
 }
 ]
}`

```
