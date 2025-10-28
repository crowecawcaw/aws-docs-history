# Granting `NeptuneGraphReadOnlyAccess` using AWS managed policy

The [NeptuneGraphReadOnlyAccess](https://console.aws.amazon.com/iam/home#policies/NeptuneGraphReadOnlyAccess "https://console.aws.amazon.com/iam/home#policies/NeptuneGraphReadOnlyAccess")
managed policy below provides read only access to all Amazon Neptune Analytics resources along with read only
permissions for dependent services.

This policy includes permissions to do the following:

- **For Amazon EC2** – Retrieve information about VPCs,
  subnets, security groups and availability zones.
- **For AWS KMS** – Retrieve information about KMS keys and aliases.
- **For CloudWatch** – Retrieve information about CloudWatch metrics.
- **For CloudWatch Logs** – Retrieve information about CloudWatch log streams and events.

###### Note

This policy was released on 2023-11-29.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowReadOnlyPermissionsForNeptuneGraph",
 "Effect": "Allow",
 "Action": [
 "neptune-graph:Get*",
 "neptune-graph:List*",
 "neptune-graph:Read*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadOnlyPermissionsForEC2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeAvailabilityZones"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadOnlyPermissionsForKMS",
 "Effect": "Allow",
 "Action": [
 "kms:ListKeys",
 "kms:ListAliases"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadOnlyPermissionsForCloudwatch",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData",
 "cloudwatch:ListMetrics",
 "cloudwatch:GetMetricStatistics"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadOnlyPermissionsForLogs",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:GetLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/neptune/*:log-stream:*"
 ]
 }
 ]
}`

```
