# Prerequisites for setting up Amazon Neptune using AWS CloudFormation

Before you create an Amazon Neptune cluster using an AWS CloudFormation template, you need
to have the following:

- An Amazon EC2 key pair.
- The permissions required for using AWS CloudFormation.

## Create an Amazon EC2 Key Pair to use for launching a Neptune cluster using AWS CloudFormation

In order to launch a Neptune DB cluster using an AWS CloudFormation template, you must have an
Amazon EC2key pair (and its associated PEM file) available in the region where you create
the AWS CloudFormation stack.

If you need to create the key pair, see either [Creating
a Key Pair Using Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#having-ec2-create-your-key-pair "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#having-ec2-create-your-key-pair") in the Amazon EC2 User Guide, or [Creating a Key Pair Using Amazon EC2](../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md#having-ec2-create-your-key-pair "../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md#having-ec2-create-your-key-pair") in the Amazon EC2 User Guide for
instructions.

## Add IAM policies to grant permissions needed to use the AWS CloudFormation template

First, you need to have an IAM user set up with permissions needed for working with
Neptune, as described in [Creating an IAM user with permissions for Neptune](manage-console-iam-user.md "manage-console-iam-user.md").

Then you need to add the AWS managed policy, `AWSCloudFormationReadOnlyAccess`,
to that user.

Finally, you need to create the following customer-managed policy and add it to that
user:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/*",
 "Condition": {
 "StringEquals": {
 "iam:passedToService": "rds.amazonaws.com"
 }
 }
 },
 {
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
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics",
 "sns:ListSubscriptions",
 "sns:Publish"
 ],
 "Resource": "arn:aws:sns:*:`111122223333`:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:ListRetirableGrants",
 "kms:ListKeys",
 "kms:ListAliases",
 "kms:ListKeyPolicies"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics"
 ],
 "Resource": "arn:aws:cloudwatch:*:`111122223333`:service/*-*",
 "Condition": {
 "StringLike": {
 "cloudwatch:namespace": "AWS/Neptune"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeVpcs",
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcAttribute"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:vpc/*",
 "arn:aws:ec2:*:`111122223333`:subnet/*",
 "arn:aws:ec2:*:`111122223333`:security-group/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "rds:CreateDBCluster",
 "rds:CreateDBInstance",
 "rds:AddTagsToResource",
 "rds:ListTagsForResource",
 "rds:RemoveTagsFromResource",
 "rds:RemoveRoleFromDBCluster",
 "rds:ResetDBParameterGroup",
 "rds:CreateDBSubnetGroup",
 "rds:ModifyDBParameterGroup",
 "rds:DownloadDBLogFilePortion",
 "rds:CopyDBParameterGroup",
 "rds:AddRoleToDBCluster",
 "rds:ModifyDBInstance",
 "rds:ModifyDBClusterParameterGroup",
 "rds:ModifyDBClusterSnapshotAttribute",
 "rds:DeleteDBInstance",
 "rds:CopyDBClusterParameterGroup",
 "rds:CreateDBParameterGroup",
 "rds:DescribeDBSecurityGroups",
 "rds:DeleteDBSubnetGroup",
 "rds:DescribeValidDBInstanceModifications",
 "rds:ModifyDBCluster",
 "rds:CreateDBClusterSnapshot",
 "rds:DeleteDBParameterGroup",
 "rds:CreateDBClusterParameterGroup",
 "rds:RemoveTagsFromResource",
 "rds:PromoteReadReplicaDBCluster",
 "rds:RestoreDBClusterFromSnapshot",
 "rds:DescribeDBSubnetGroups",
 "rds:DescribePendingMaintenanceActions",
 "rds:DescribeDBParameterGroups",
 "rds:FailoverDBCluster",
 "rds:DescribeDBInstances",
 "rds:DescribeDBParameters",
 "rds:DeleteDBCluster",
 "rds:ResetDBClusterParameterGroup",
 "rds:RestoreDBClusterToPointInTime",
 "rds:DescribeDBClusterSnapshotAttributes",
 "rds:AddTagsToResource",
 "rds:DescribeDBClusterParameters",
 "rds:CopyDBClusterSnapshot",
 "rds:DescribeDBLogFiles",
 "rds:DeleteDBClusterSnapshot",
 "rds:ListTagsForResource",
 "rds:RebootDBInstance",
 "rds:DescribeDBClusterSnapshots",
 "rds:DeleteDBClusterParameterGroup",
 "rds:ApplyPendingMaintenanceAction",
 "rds:DescribeDBClusters",
 "rds:DescribeDBClusterParameterGroups",
 "rds:ModifyDBSubnetGroup"
 ],
 "Resource": [
 "arn:aws:rds:*:`111122223333`:cluster-snapshot:*",
 "arn:aws:rds:*:`111122223333`:cluster:*",
 "arn:aws:rds:*:`111122223333`:pg:*",
 "arn:aws:rds:*:`111122223333`:cluster-pg:*",
 "arn:aws:rds:*:`111122223333`:secgrp:*",
 "arn:aws:rds:*:`111122223333`:db:*",
 "arn:aws:rds:*:`111122223333`:subgrp:*"
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
 "Effect": "Allow",
 "Action": [
 "logs:GetLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:`111122223333`:log-group:*:log-stream:*",
 "arn:aws:logs:*:`111122223333`:log-group:*"
 ]
 }
 ]
}`

```

###### Note

The following permissions are only required to delete a stack:
`iam:DeleteRole`, `iam:RemoveRoleFromInstanceProfile`,
`iam:DeleteRolePolicy`, `iam:DeleteInstanceProfile`, and
`ec2:DeleteVpcEndpoints`.

Also note that `ec2:*Vpc` grants `ec2:DeleteVpc`
permissions.
