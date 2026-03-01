# Permissions that the integration needs

If you create an IAM role for the integration to use, instead of allowing CloudWatch Logs to
create the role, it must include the following permissions and trust policy. For more
information about how to create an IAM role, see [Create a role to
delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudWatchLogsAccess",
 "Effect": "Allow",
 "Action": [
 "logs:StartQuery",
 "logs:GetLogGroupFields",
 "logs:GetQueryResults"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "CloudWatchLogsDescribeLogGroupsAccess",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonOpenSearchCollectionAccess",
 "Effect": "Allow",
 "Action": [
 "aoss:APIAccessAll"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aoss:collection": "cloudwatch-logs-*"
 }
 }
 }
 ]
}`

```

###### Note

The previous role grants access to read from all log groups in the account, to
enable you to create dashboards for any log account, including cross-account log
groups. If you want to restrict access to specific log groups and create dashboards
for only those log groups, you can update the first statement in that policy to the
following:

```
{
      "Sid": "CloudWatchLogsAccess",
      "Effect": "Allow",
      "Action": [
        "logs:StartQuery",
        "logs:GetLogGroupFields",
        "logs:GetQueryResults"
      ],
      "Resource": [
        "arn:aws:logs:us-east-1:123456789012:log-group:myLogGroup:*",
        "arn:aws:logs:us-east-1:123456789012:log-group:myLogGroup"
      ]
}
```
