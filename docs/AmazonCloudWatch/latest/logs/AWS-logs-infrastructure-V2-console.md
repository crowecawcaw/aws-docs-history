# Console-specific

permissions

In addition to the permissions listed in the previous sections, if you are setting up
log delivery using the console instead of the APIs, you also need the following
additional permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowLogDeliveryActionsConsoleCWL",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:us-east-1:`111122223333`:log-group:*"
 ]
 },
 {
 "Sid": "AllowLogDeliveryActionsConsoleS3",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Sid": "AllowLogDeliveryActionsConsoleFH",
 "Effect": "Allow",
 "Action": [
 "firehose:ListDeliveryStreams",
 "firehose:DescribeDeliveryStream"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
