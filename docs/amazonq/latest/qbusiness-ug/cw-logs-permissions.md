# Permissions for monitoring Amazon Q Business with

Amazon CloudWatch Logs

To set up Amazon CloudWatch Logs for Amazon Q Business, use the following IAM policy to grant the necessary
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudWatchLogsDeliveryPermissions",
 "Effect": "Allow",
 "Action": "logs:CreateDelivery",
 "Resource": [
 "arn:aws:logs:us-east-1:111122223333:delivery-source:*",
 "arn:aws:logs:us-east-1:111122223333:delivery:*",
 "arn:aws:logs:us-east-1:111122223333:delivery-destination:*"
 ]
 },
 {
 "Sid": "QBusinessLogDeliveryPermissions",
 "Effect": "Allow",
 "Action": "qbusiness:AllowVendedLogDeliveryForResource",
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 ]
 }
 ]
}`

```

For example IAM policies with all the required permissions for your specific logging
destination, see [Enable logging from
AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") in the _Amazon CloudWatch Logs User Guide_.
