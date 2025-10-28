# Sending AWS Network Firewall logs to Amazon CloudWatch Logs

To send logs to Amazon CloudWatch Logs, you create a CloudWatch Logs log group. When you enable
logging in Network Firewall, you provide the log group name. After you enable
logging for your firewall, AWS Network Firewall delivers logs to the CloudWatch Logs log
group in log streams. Each log stream contains an hour of log records.

You can use any name for your CloudWatch Logs log group. Configure the log group in the
same Region as the firewall and using the same account as you use to manage the
firewall.

For information about configuring a CloudWatch Logs log group, see [Working with
Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").

###### Names of alert and flow logs

When you configure your Network Firewall firewall to send alert and flow logs
to the log group, the resulting log streams have the following naming
format:

```
/aws/network-firewall/`log-type`/`firewall-name`_`YYYY-MM-DD-HH`
```

In the specification, the log type is either `alert` or
`flow`.

The following shows an example log stream created on October 1, 2020, at 5 pm
for alert logging for firewall `test-firewall`.

```
/aws/network-firewall/alert/test-firewall_2020-10-01-17
```

###### Names of TLS logs

When you configure your Network Firewall firewall to send TLS logs to the log
group, the resulting log streams have the following naming format:

```
/aws/network-firewall/tls/`firewall-name`
```

The following shows the log stream for TLS logging for the example firewall
`test-firewall`.

```
/aws/network-firewall/tls/test-firewall
```

## Permissions to publish logs to CloudWatch Logs

You must have the following permissions settings to configure your firewall to send logs to a CloudWatch Logs log group and to access log metrics in Network Firewall.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Sid": "FirewallLogging"
 },
 {
 "Sid": "FirewallLoggingCWL",
 "Action": [
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:`log-group-name`"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

###### Important

Additional fees are incurred when Network Firewall queries CloudWatch to fetch log data for the detailed monitoring dashboard.
For best practices to minimize additional cost, see [Working with the firewall monitoring dashboard](nwfw-using-dashboard.md "nwfw-using-dashboard.md").

## (Optional) Permissions to access CloudWatch log metrics in Network Firewall

You must have the following permissions settings added to your existing CloudWatch permissions to configure your
firewall to query CloudWatch logs for the detailed monitoring dashboard.

###### Important

Additional fees are incurred when querying logs, whether through CloudWatch Logs or through Amazon Athena for logs stored in S3.
For best practices to minimize additional cost,
see [Working with the firewall monitoring dashboard](nwfw-using-dashboard.md "nwfw-using-dashboard.md").

```
{
            "Effect": "Allow",
            "Action": [
                "logs:StartQuery",
                "logs:GetQueryResults"
            ],
            "Resource": "`CloudWatch Logs log group ARN`"
        }
```

The following view shows both standard CloudWatch permissions and the additional permissions needed for detailed monitoring.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Sid": "FirewallLogging"
 },
 {
 "Sid": "FirewallLoggingCWL",
 "Action": [
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:`log-group-name`"
 ],
 "Effect": "Allow"
 },
 {
 "Sid": "FirewallLoggingSearch",
 "Effect": "Allow",
 "Action": [
 "logs:StartQuery",
 "logs:GetQueryResults"
 ],
 "Resource": "*"
 }
 ]
}`

```
