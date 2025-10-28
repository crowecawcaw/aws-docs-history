End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Amazon CloudWatch logging role policy for AWS IoT Events

The following policy documents provide the role policy and trust policy that allow AWS IoT Events
to submit logs to CloudWatch on your behalf.

Role policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:PutMetricFilter",
 "logs:PutRetentionPolicy",
 "logs:GetLogEvents",
 "logs:DeleteLogStream"
 ],
 "Resource": [
 "arn:aws:logs:*:*:*"
 ]
 }
 ]
}`

```

Trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [

 "iotevents.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

You also need an IAM permissions policy attached to the user that allows the user to
pass roles, as follows. For more information, see [Granting a user permissions to pass a role
to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`123456789012`:role/Role_To_Pass"
 }
 ]
}`

```

You can use the following command to put the resource policy for CloudWatch logs. This allows
AWS IoT Events to put log events into CloudWatch streams.

```

aws logs put-resource-policy --policy-name ioteventsLoggingPolicy --policy-document "{ \"Version\": \"2012-10-17\",		 	 	  \"Statement\": [ { \"Sid\": \"IoTEventsToCloudWatchLogs\", \"Effect\": \"Allow\", \"Principal\": { \"Service\": [ \"iotevents.amazonaws.com\" ] }, \"Action\":\"logs:PutLogEvents\", \"Resource\": \"*\" } ] }"
```

Use the following command to put logging options. Replace the `roleArn` with
the logging role that you created.

```

aws iotevents put-logging-options --cli-input-json "{ \"loggingOptions\": {\"roleArn\": \"arn:aws:iam::123456789012:role/testLoggingRole\", \"level\": \"INFO\", \"enabled\": true } }"
```
