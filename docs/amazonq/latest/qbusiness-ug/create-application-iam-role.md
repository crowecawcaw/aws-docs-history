# IAM role for an Amazon Q Business application

When you create an Amazon Q Business application, you must provide Amazon Q with an
IAM role with permissions to write to an Amazon CloudWatch log and assign user
subscriptions to applications. You must also provide a trust policy that allows Amazon Q to
assume the role. The following are the policies that must be provided.

**To allow Amazon Q to access a CloudWatch log and assign user
subscriptions, use the following role policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonQApplicationPutMetricDataPermission",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/QBusiness"
 }
 }
 },
 {
 "Sid": "AmazonQApplicationDescribeLogGroupsPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonQApplicationCreateLogGroupPermission",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:us-east-1:111122223333:log-group:/aws/qbusiness/*"
 ]
 },
 {
 "Sid": "AmazonQApplicationLogStreamPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:us-east-1:111122223333:log-group:/aws/qbusiness/*:log-stream:*"
 ]
 }
 ]
}`

```

**To allow Amazon Q to assume a role, use the following
trust policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonQApplicationPermission",
 "Effect": "Allow",
 "Principal": {
 "Service": "qbusiness.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/*"
 }
 }
 }
 ]
}`

```

**Amazon Q also supports using a service-linked role
(`AWSServiceRoleForQBusiness`) for an Amazon Q application. The
following is the service-linked role policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessPutMetricDataPermission",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/QBusiness"
 }
 }
 },
 {
 "Sid": "QBusinessCreateLogGroupPermission",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/qbusiness/*"
 ]
 },
 {
 "Sid": "QBusinessDescribeLogGroupsPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Sid": "QBusinessLogStreamPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/qbusiness/*:log-stream:*"
 ]
 }
 ]
}`

```

For more information on using service-linked roles for an Amazon Q application, see
[Using service-linked roles](../business-use-dg/using-service-linked-roles.md "../business-use-dg/using-service-linked-roles.md").
