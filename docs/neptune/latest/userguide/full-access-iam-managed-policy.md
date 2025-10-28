# Granting `NeptuneFullAccess` to Amazon Neptune databases using AWS managed policy

The [NeptuneFullAccess](https://console.aws.amazon.com/iam/home#policies/NeptuneFullAccess "https://console.aws.amazon.com/iam/home#policies/NeptuneFullAccess")
managed policy below grants full access to all Neptune actions and resources for both
administrative and data-access purposes. It is recommended if you need full access from
the AWS CLI or from an SDK, but not from the AWS Management Console.

###### Note

This policy was updated on 2022-07-21 to include full data-access permissions as
well as full administrative permissions and to include permissions for global database
actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowNeptuneCreate",
 "Effect": "Allow",
 "Action": [
 "rds:CreateDBCluster",
 "rds:CreateDBInstance"
 ],
 "Resource": [
 "arn:aws:rds:*:*:*"
 ],
 "Condition": {
 "StringEquals": {
 "rds:DatabaseEngine": [
 "graphdb",
 "neptune"
 ]
 }
 }
 },
 {
 "Sid": "AllowManagementPermissionsForRDS",
 "Effect": "Allow",
 "Action": [
 "rds:AddRoleToDBCluster",
 "rds:AddSourceIdentifierToSubscription",
 "rds:AddTagsToResource",
 "rds:ApplyPendingMaintenanceAction",
 "rds:CopyDBClusterParameterGroup",
 "rds:CopyDBClusterSnapshot",
 "rds:CopyDBParameterGroup",
 "rds:CreateDBClusterEndpoint",
 "rds:CreateDBClusterParameterGroup",
 "rds:CreateDBClusterSnapshot",
 "rds:CreateDBParameterGroup",
 "rds:CreateDBSubnetGroup",
 "rds:CreateEventSubscription",
 "rds:CreateGlobalCluster",
 "rds:DeleteDBCluster",
 "rds:DeleteDBClusterEndpoint",
 "rds:DeleteDBClusterParameterGroup",
 "rds:DeleteDBClusterSnapshot",
 "rds:DeleteDBInstance",
 "rds:DeleteDBParameterGroup",
 "rds:DeleteDBSubnetGroup",
 "rds:DeleteEventSubscription",
 "rds:DeleteGlobalCluster",
 "rds:DescribeDBClusterEndpoints",
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
 "rds:DescribeDBSecurityGroups",
 "rds:DescribeDBSubnetGroups",
 "rds:DescribeEngineDefaultClusterParameters",
 "rds:DescribeEngineDefaultParameters",
 "rds:DescribeEventCategories",
 "rds:DescribeEventSubscriptions",
 "rds:DescribeEvents",
 "rds:DescribeGlobalClusters",
 "rds:DescribeOptionGroups",
 "rds:DescribeOrderableDBInstanceOptions",
 "rds:DescribePendingMaintenanceActions",
 "rds:DescribeValidDBInstanceModifications",
 "rds:DownloadDBLogFilePortion",
 "rds:FailoverDBCluster",
 "rds:FailoverGlobalCluster",
 "rds:ListTagsForResource",
 "rds:ModifyDBCluster",
 "rds:ModifyDBClusterEndpoint",
 "rds:ModifyDBClusterParameterGroup",
 "rds:ModifyDBClusterSnapshotAttribute",
 "rds:ModifyDBInstance",
 "rds:ModifyDBParameterGroup",
 "rds:ModifyDBSubnetGroup",
 "rds:ModifyEventSubscription",
 "rds:ModifyGlobalCluster",
 "rds:PromoteReadReplicaDBCluster",
 "rds:RebootDBInstance",
 "rds:RemoveFromGlobalCluster",
 "rds:RemoveRoleFromDBCluster",
 "rds:RemoveSourceIdentifierFromSubscription",
 "rds:RemoveTagsFromResource",
 "rds:ResetDBClusterParameterGroup",
 "rds:ResetDBParameterGroup",
 "rds:RestoreDBClusterFromSnapshot",
 "rds:RestoreDBClusterToPointInTime",
 "rds:StartDBCluster",
 "rds:StopDBCluster"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowOtherDepedentPermissions",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics",
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeVpcs",
 "kms:ListAliases",
 "kms:ListKeyPolicies",
 "kms:ListKeys",
 "kms:ListRetirableGrants",
 "logs:DescribeLogStreams",
 "logs:GetLogEvents",
 "sns:ListSubscriptions",
 "sns:ListTopics",
 "sns:Publish"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowPassRoleForNeptune",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:passedToService": "rds.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowCreateSLRForNeptune",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/rds.amazonaws.com/AWSServiceRoleForRDS",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "rds.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowDataAccessForNeptune",
 "Effect": "Allow",
 "Action": [
 "neptune-db:*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
