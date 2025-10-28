# Granting `NeptuneReadOnlyAccess` to Amazon Neptune databases using AWS managed policy

The [NeptuneReadOnlyAccess](https://console.aws.amazon.com/iam/home#policies/NeptuneReadOnlyAccess "https://console.aws.amazon.com/iam/home#policies/NeptuneReadOnlyAccess")
managed policy below grants read-only access to all Neptune actions and resources for both
administrative and data-access purposes.

###### Note

This policy was updated on 2022-07-21 to include read-only data-access permissions
as well as read-only administrative permissions and to include permissions for global database
actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowReadOnlyPermissionsForRDS",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeAccountAttributes",
 "rds:DescribeCertificates",
 "rds:DescribeDBClusterParameterGroups",
 "rds:DescribeDBClusterParameters",
 "rds:DescribeDBClusterSnapshotAttributes",
 "rds:DescribeDBClusterSnapshots",
 "rds:DescribeDBClusters",
 "rds:DescribeDBEngineVersions",
 "rds:DescribeDBInstances",
 "rds:DescribeDBLogFiles",
 "rds:DescribeDBParameterGroups",
 "rds:DescribeDBParameters",
 "rds:DescribeDBSubnetGroups",
 "rds:DescribeEventCategories",
 "rds:DescribeEventSubscriptions",
 "rds:DescribeEvents",
 "rds:DescribeGlobalClusters",
 "rds:DescribeOrderableDBInstanceOptions",
 "rds:DescribePendingMaintenanceActions",
 "rds:DownloadDBLogFilePortion",
 "rds:ListTagsForResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadOnlyPermissionsForCloudwatch",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadOnlyPermissionsForEC2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowReadOnlyPermissionsForKMS",
 "Effect": "Allow",
 "Action": [
 "kms:ListKeys",
 "kms:ListRetirableGrants",
 "kms:ListAliases",
 "kms:ListKeyPolicies"
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
 "arn:aws:logs:*:*:log-group:/aws/rds/*:log-stream:*",
 "arn:aws:logs:*:*:log-group:/aws/neptune/*:log-stream:*"
 ]
 },
 {
 "Sid": "AllowReadOnlyPermissionsForNeptuneDB",
 "Effect": "Allow",
 "Action": [
 "neptune-db:Read*",
 "neptune-db:Get*",
 "neptune-db:List*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
