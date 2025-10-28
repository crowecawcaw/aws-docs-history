# AWS managed policies for Amazon DocumentDB

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself.
It takes time and expertise to [create IAM customer managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need.
To get started quickly, you can use our AWS managed policies.
These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _AWS Identity and Access Management User Guide_.

AWS services maintain and update AWS managed policies.
You can't change the permissions in AWS managed policies.
Services occasionally add additional permissions to an AWS managed policy to support new features.
This type of update affects all identities (users, groups, and roles) where the policy is attached.
Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services.
For example, the `ViewOnlyAccess` AWS managed policy provides read-only access to many AWS services and resources.
When a service launches a new feature, AWS adds read-only permissions for new operations and resources.
For a list and descriptions of job function policies, see [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _AWS Identity and Access Management User Guide_.

The following AWS managed policies, which you can attach to users in your account, are specific to Amazon DocumentDB:

- [AmazonDocDBFullAccess](#AmazonDocDBFullAccess "#AmazonDocDBFullAccess") – Grants full access to all Amazon DocumentDB resources for the root AWS account.
- [AmazonDocDBReadOnlyAccess](#AmazonDocDBReadOnlyAccess "#AmazonDocDBReadOnlyAccess") – Grants read-only access to all Amazon DocumentDB resources for the root AWS account.
- [AmazonDocDBConsoleFullAccess](#AmazonDocDBConsoleFullAccess "#AmazonDocDBConsoleFullAccess") – Grants full access to manage Amazon DocumentDB and Amazon DocumentDB elastic cluster resources using the AWS Management Console.
- [AmazonDocDBElasticReadOnlyAccess](#AmazonDocDB-ElasticReadOnlyAccess "#AmazonDocDB-ElasticReadOnlyAccess") – Grants read-only access to all Amazon DocumentDB elastic cluster resources for the root AWS account.
- [AmazonDocDBElasticFullAccess](#AmazonDocDB-ElasticFullAccess "#AmazonDocDB-ElasticFullAccess") – Grants full access to all Amazon DocumentDB elastic cluster resources for the root AWS account.

## AmazonDocDBFullAccess

This policy grants administrative permissions that allow a principal full access to all Amazon DocumentDB actions.
The permissions in this policy are grouped as follows:

- The Amazon DocumentDB permissions allow all Amazon DocumentDB actions.
- Some of the Amazon EC2 permissions in this policy are required to validate the passed resources in an API request.
  This is to make sure Amazon DocumentDB is able to successfully use the resources with a cluster.
  The rest of the Amazon EC2 permissions in this policy allow Amazon DocumentDB to create AWS resources that are needed to make it possible for you to connect to your clusters.
- The Amazon DocumentDB permissions are used during API calls to validate the passed resources in a request.
  They are required for Amazon DocumentDB to be able to use the passed key with the Amazon DocumentDB cluster.
- The CloudWatch Logs are required for Amazon DocumentDB to be able to ensure that the log delivery destinations are reachable, and that they are valid for broker log use.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "rds:AddRoleToDBCluster",
 "rds:AddSourceIdentifierToSubscription",
 "rds:AddTagsToResource",
 "rds:ApplyPendingMaintenanceAction",
 "rds:CopyDBClusterParameterGroup",
 "rds:CopyDBClusterSnapshot",
 "rds:CopyDBParameterGroup",
 "rds:CreateDBCluster",
 "rds:CreateDBClusterParameterGroup",
 "rds:CreateDBClusterSnapshot",
 "rds:CreateDBInstance",
 "rds:CreateDBParameterGroup",
 "rds:CreateDBSubnetGroup",
 "rds:CreateEventSubscription",
 "rds:DeleteDBCluster",
 "rds:DeleteDBClusterParameterGroup",
 "rds:DeleteDBClusterSnapshot",
 "rds:DeleteDBInstance",
 "rds:DeleteDBParameterGroup",
 "rds:DeleteDBSubnetGroup",
 "rds:DeleteEventSubscription",
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
 "rds:DescribeOptionGroups",
 "rds:DescribeOrderableDBInstanceOptions",
 "rds:DescribePendingMaintenanceActions",
 "rds:DescribeValidDBInstanceModifications",
 "rds:DownloadDBLogFilePortion",
 "rds:FailoverDBCluster",
 "rds:ListTagsForResource",
 "rds:ModifyDBCluster",
 "rds:ModifyDBClusterParameterGroup",
 "rds:ModifyDBClusterSnapshotAttribute",
 "rds:ModifyDBInstance",
 "rds:ModifyDBParameterGroup",
 "rds:ModifyDBSubnetGroup",
 "rds:ModifyEventSubscription",
 "rds:PromoteReadReplicaDBCluster",
 "rds:RebootDBInstance",
 "rds:RemoveRoleFromDBCluster",
 "rds:RemoveSourceIdentifierFromSubscription",
 "rds:RemoveTagsFromResource",
 "rds:ResetDBClusterParameterGroup",
 "rds:ResetDBParameterGroup",
 "rds:RestoreDBClusterFromSnapshot",
 "rds:RestoreDBClusterToPointInTime"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ]
 },
 {
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
 "Effect": "Allow",
 "Resource": [
 "*"
 ]
 },
 {
 "Action": "iam:CreateServiceLinkedRole",
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/aws-service-role/rds.amazonaws.com/AWSServiceRoleForRDS",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "rds.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AmazonDocDBReadOnlyAccess

This policy grants read-only permissions that allow users to view information in Amazon DocumentDB.
Principals with this policy attached can't make any updates or delete exiting resources, nor can they create new Amazon DocumentDB resources.
For example, principals with these permissions can view the list of clusters and configurations associated with their account, but cannot change the configuration or settings of any clusters.
The permissions in this policy are grouped as follows:

- Amazon DocumentDB permissions allow you to list Amazon DocumentDB resources, describe them, and get information about them.
- Amazon EC2 permissions are used to describe the Amazon VPC, subnets, security groups, and ENIs that are associated with a cluster.
- An Amazon DocumentDB permission is used to describe the key that is associated with the cluster.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
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
 "rds:DescribeOrderableDBInstanceOptions",
 "rds:DescribePendingMaintenanceActions",
 "rds:DownloadDBLogFilePortion",
 "rds:ListTagsForResource"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeVpcs"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "kms:ListKeys",
 "kms:ListRetirableGrants",
 "kms:ListAliases",
 "kms:ListKeyPolicies"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "logs:DescribeLogStreams",
 "logs:GetLogEvents"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/rds/*:log-stream:*",
 "arn:aws:logs:*:*:log-group:/aws/docdb/*:log-stream:*"
 ]
 }
 ]
}`

```

## AmazonDocDBConsoleFullAccess

Grants full access to manage Amazon DocumentDB resources using the AWS Management Console for following:

- The Amazon DocumentDB permissions to allow all Amazon DocumentDB and Amazon DocumentDB cluster actions.
- Some of the Amazon EC2 permissions in this policy are required to validate the passed resources in an API request.
  This is to make sure Amazon DocumentDB is able to successfully use the resources to provision and maintain the cluster.
  The rest of the Amazon EC2 permissions in this policy allow Amazon DocumentDB to create AWS resources that are needed to make it possible for you to connect to your clusters like VPCEndpoint.
- AWS KMS permissions are used during API calls to AWS KMS to validate the passed resources in a request.
  They are required for Amazon DocumentDB to be able to use the passed key to encrypt and decrypt the data at rest with the Amazon DocumentDB elastic cluster.
- The CloudWatch Logs are required for Amazon DocumentDB to be able to ensure that the log delivery destinations are reachable, and that they are valid for auditing and profiling log use.
- Secrets Manager permissions are required to validate given secret and use it setup the admin user for Amazon DocumentDB elastic clusters.
- Amazon RDS permissions are required for Amazon DocumentDB cluster management actions.
  For certain management features, Amazon DocumentDB uses operational technology that is shared with Amazon RDS.
- SNS permissions allows principals to Amazon Simple Notification Service (Amazon SNS) subscriptions and topics, and to publish Amazon SNS messages.
- IAM permissions are required for creating the service linked roles required for metrics and logs publishing.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DocdbSids",
 "Effect": "Allow",
 "Action": [
 "docdb-elastic:CreateCluster",
 "docdb-elastic:UpdateCluster",
 "docdb-elastic:GetCluster",
 "docdb-elastic:DeleteCluster",
 "docdb-elastic:ListClusters",
 "docdb-elastic:CreateClusterSnapshot",
 "docdb-elastic:GetClusterSnapshot",
 "docdb-elastic:DeleteClusterSnapshot",
 "docdb-elastic:ListClusterSnapshots",
 "docdb-elastic:RestoreClusterFromSnapshot",
 "docdb-elastic:TagResource",
 "docdb-elastic:UntagResource",
 "docdb-elastic:ListTagsForResource",
 "docdb-elastic:CopyClusterSnapshot",
 "docdb-elastic:StartCluster",
 "docdb-elastic:StopCluster",
 "docdb-elastic:GetPendingMaintenanceAction",
 "docdb-elastic:ListPendingMaintenanceActions",
 "docdb-elastic:ApplyPendingMaintenanceAction",
 "rds:AddRoleToDBCluster",
 "rds:AddSourceIdentifierToSubscription",
 "rds:AddTagsToResource",
 "rds:ApplyPendingMaintenanceAction",
 "rds:CopyDBClusterParameterGroup",
 "rds:CopyDBClusterSnapshot",
 "rds:CopyDBParameterGroup",
 "rds:CreateDBCluster",
 "rds:CreateDBClusterParameterGroup",
 "rds:CreateDBClusterSnapshot",
 "rds:CreateDBInstance",
 "rds:CreateDBParameterGroup",
 "rds:CreateDBSubnetGroup",
 "rds:CreateEventSubscription",
 "rds:CreateGlobalCluster",
 "rds:DeleteDBCluster",
 "rds:DeleteDBClusterParameterGroup",
 "rds:DeleteDBClusterSnapshot",
 "rds:DeleteDBInstance",
 "rds:DeleteDBParameterGroup",
 "rds:DeleteDBSubnetGroup",
 "rds:DeleteEventSubscription",
 "rds:DeleteGlobalCluster",
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
 "rds:ListTagsForResource",
 "rds:ModifyDBCluster",
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
 "rds:RestoreDBClusterToPointInTime"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "DependencySids",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "cloudwatch:GetMetricData",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics",
 "ec2:AllocateAddress",
 "ec2:AssignIpv6Addresses",
 "ec2:AssignPrivateIpAddresses",
 "ec2:AssociateAddress",
 "ec2:AssociateRouteTable",
 "ec2:AssociateSubnetCidrBlock",
 "ec2:AssociateVpcCidrBlock",
 "ec2:AttachInternetGateway",
 "ec2:AttachNetworkInterface",
 "ec2:CreateCustomerGateway",
 "ec2:CreateDefaultSubnet",
 "ec2:CreateDefaultVpc",
 "ec2:CreateInternetGateway",
 "ec2:CreateNatGateway",
 "ec2:CreateNetworkInterface",
 "ec2:CreateRoute",
 "ec2:CreateRouteTable",
 "ec2:CreateSecurityGroup",
 "ec2:CreateSubnet",
 "ec2:CreateVpc",
 "ec2:CreateVpcEndpoint",
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAddresses",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeCustomerGateways",
 "ec2:DescribeInstances",
 "ec2:DescribeNatGateways",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribePrefixLists",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroupReferences",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcs",
 "ec2:ModifyNetworkInterfaceAttribute",
 "ec2:ModifySubnetAttribute",
 "ec2:ModifyVpcAttribute",
 "ec2:ModifyVpcEndpoint",
 "kms:DescribeKey",
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
 "Sid": "DocdbSLRSid",
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
 "Sid": "DocdbElasticSLRSid",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/docdb-elastic.amazonaws.com/AWSServiceRoleForDocDB-Elastic",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "docdb-elastic.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AmazonDocDBElasticReadOnlyAccess

This policy grants read-only permissions that allow users to view elastic cluster information in Amazon DocumentDB.
Principals with this policy attached can't make any updates or delete exiting resources, nor can they create new Amazon DocumentDB resources.
For example, principals with these permissions can view the list of clusters and configurations associated with their account, but cannot change the configuration or settings of any clusters.
The permissions in this policy are grouped as follows:

- Amazon DocumentDB elastic cluster permissions allow you to list Amazon DocumentDB elastic cluster resources, describe them, and get information about them.
- CloudWatch permissions are used to verify service metrics.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "docdb-elastic:ListClusters",
 "docdb-elastic:GetCluster",
 "docdb-elastic:ListClusterSnapshots",
 "docdb-elastic:GetClusterSnapshot",
 "docdb-elastic:ListTagsForResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData",
 "cloudwatch:ListMetrics",
 "cloudwatch:GetMetricStatistics"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AmazonDocDBElasticFullAccess

This policy grants administrative permissions that allow a principal full access to all Amazon DocumentDB actions for Amazon DocumentDB elastic cluster.

This policy uses AWS tags (https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) within conditions to scope access to resources.
If you are using a secret, it must be tagged with tag key `DocDBElasticFullAccess` and a tag value.
If you are using a customer managed key, it must be tagged with tag key `DocDBElasticFullAccess` and a tag value.

The permissions in this policy are grouped as follows:

- Amazon DocumentDB elastic cluster permissions allow all Amazon DocumentDB actions.
- Some of the Amazon EC2 permissions in this policy are required to validate the passed resources in an API request.
  This is to make sure Amazon DocumentDB is able to successfully use the resources to provision and maintain the cluster.
  The rest of the Amazon EC2 permissions in this policy allow Amazon DocumentDB to create AWS resources that are needed to make it possible for you to connect to your clusters like a VPC endpoint.
- AWS KMS permissions are required for Amazon DocumentDB to be able to use the passed key to encrypt and decrypt the data at rest within the Amazon DocumentDB elastic cluster.

###### Note

The customer managed key must have a tag with key `DocDBElasticFullAccess` and a tag value.

- SecretsManager permissions are required to validate given secret and use it setup the admin user for Amazon DocumentDB elastic clusters.

###### Note

The secret used must have a tag with key `DocDBElasticFullAccess` and a tag value.

- IAM permissions are required for creating the service linked roles required for metrics and logs publishing.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DocdbElasticSid",
 "Effect": "Allow",
 "Action": [
 "docdb-elastic:CreateCluster",
 "docdb-elastic:UpdateCluster",
 "docdb-elastic:GetCluster",
 "docdb-elastic:DeleteCluster",
 "docdb-elastic:ListClusters",
 "docdb-elastic:CreateClusterSnapshot",
 "docdb-elastic:GetClusterSnapshot",
 "docdb-elastic:DeleteClusterSnapshot",
 "docdb-elastic:ListClusterSnapshots",
 "docdb-elastic:RestoreClusterFromSnapshot",
 "docdb-elastic:TagResource",
 "docdb-elastic:UntagResource",
 "docdb-elastic:ListTagsForResource",
 "docdb-elastic:CopyClusterSnapshot",
 "docdb-elastic:StartCluster",
 "docdb-elastic:StopCluster",
 "docdb-elastic:GetPendingMaintenanceAction",
 "docdb-elastic:ListPendingMaintenanceActions",
 "docdb-elastic:ApplyPendingMaintenanceAction"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "EC2Sid",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateVpcEndpoint",
 "ec2:DescribeVpcEndpoints",
 "ec2:DeleteVpcEndpoints",
 "ec2:ModifyVpcEndpoint",
 "ec2:DescribeVpcAttribute",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeAvailabilityZones",
 "secretsmanager:ListSecrets"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:CalledViaFirst": "docdb-elastic.amazonaws.com"
 }
 }
 },
 {
 "Sid": "KMSSid",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "docdb-elastic.*.amazonaws.com"
 ],
 "aws:ResourceTag/DocDBElasticFullAccess": "*"
 }
 }
 },
 {
 "Sid": "KMSGrantSid",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/DocDBElasticFullAccess": "*",
 "kms:ViaService": [
 "docdb-elastic.*.amazonaws.com"
 ]
 },
 "Bool": {
 "kms:GrantIsForAWSResource": true
 }
 }
 },
 {
 "Sid": "SecretManagerSid",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:ListSecretVersionIds",
 "secretsmanager:DescribeSecret",
 "secretsmanager:GetSecretValue",
 "secretsmanager:GetResourcePolicy"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "secretsmanager:ResourceTag/DocDBElasticFullAccess": "*"
 },
 "StringEquals": {
 "aws:CalledViaFirst": "docdb-elastic.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudwatchSid",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData",
 "cloudwatch:ListMetrics",
 "cloudwatch:GetMetricStatistics"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "SLRSid",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/docdb-elastic.amazonaws.com/AWSServiceRoleForDocDB-Elastic",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "docdb-elastic.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AmazonDocDB-ElasticServiceRolePolicy

You can't attach `AmazonDocDBElasticServiceRolePolicy` to your AWS Identity and Access Management entities.
This policy is attached to a service-linked role that allows Amazon DocumentDB to perform actions on your behalf.
For more information, see [Service-linked roles in elastic clusters](elastic-service-linked-roles.md "elastic-service-linked-roles.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/DocDB-Elastic"
 ]
 }
 }
 }
 ]
}`

```

## Amazon DocumentDB updates to AWS managed policies

| Change                                                                                                                                                                                                                                                                     | Description                                                                                                                | Date       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [AmazonDocDBElasticFullAccess](#AmazonDocDB-ElasticFullAccess "#AmazonDocDB-ElasticFullAccess"), [AmazonDocDBConsoleFullAccess](#AmazonDocDBConsoleFullAccess "#AmazonDocDBConsoleFullAccess") - Change                                                                    | Policies updated to add pending maintenance actions.                                                                       | 2/11/2025  |
| [AmazonDocDBElasticFullAccess](#AmazonDocDB-ElasticFullAccess "#AmazonDocDB-ElasticFullAccess"), [AmazonDocDBConsoleFullAccess](#AmazonDocDBConsoleFullAccess "#AmazonDocDBConsoleFullAccess") - Change                                                                    | Policies updated to add start/stop cluster and copy cluster snapshot actions.                                              | 2/21/2024  |
| [AmazonDocDBElasticReadOnlyAccess](#AmazonDocDB-ElasticReadOnlyAccess "#AmazonDocDB-ElasticReadOnlyAccess"), [AmazonDocDBElasticFullAccess](#AmazonDocDB-ElasticFullAccess "#AmazonDocDB-ElasticFullAccess") - Change                                                      | Policies updated to add `cloudwatch:GetMetricData` action.                                                                 | 6/21/2023  |
| [AmazonDocDBElasticReadOnlyAccess](#AmazonDocDB-ElasticReadOnlyAccess "#AmazonDocDB-ElasticReadOnlyAccess") - New policy                                                                                                                                                   | New managed policy for Amazon DocumentDB elastic clusters.                                                                 | 6/8/2023   |
| [AmazonDocDBElasticFullAccess](#AmazonDocDB-ElasticFullAccess "#AmazonDocDB-ElasticFullAccess") - New policy                                                                                                                                                               | New managed policy for Amazon DocumentDB elastic clusters.                                                                 | 6/5/2023   |
| [AmazonDocDB-ElasticServiceRolePolicy](#docdb-elastic-service-role "#docdb-elastic-service-role") – New policy                                                                                                                                                             | Amazon DocumentDB creates a new AWSServiceRoleForDocDB-Elastic service linked role for Amazon DocumentDB elastic clusters. | 11/30/2022 |
| [AmazonDocDBConsoleFullAccess](#AmazonDocDBConsoleFullAccess "#AmazonDocDBConsoleFullAccess") - Change                                                                                                                                                                     | Policy updated to add Amazon DocumentDB global and elastic cluster permissions.                                            | 11/30/2022 |
| [AmazonDocDBConsoleFullAccess](#AmazonDocDBConsoleFullAccess "#AmazonDocDBConsoleFullAccess"), [AmazonDocDBFullAccess](#AmazonDocDBFullAccess "#AmazonDocDBFullAccess"), [AmazonDocDBReadOnlyAccess](#AmazonDocDBReadOnlyAccess "#AmazonDocDBReadOnlyAccess") - New Policy | Service launch.                                                                                                            | 1/19/2017  |
