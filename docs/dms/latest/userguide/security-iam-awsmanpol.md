# AWS managed policies for AWS Database Migration Service

###### Topics

- [AWS managed
  policy: AmazonDMSVPCManagementRole](#security-iam-awsmanpol-AmazonDMSVPCManagementRole "#security-iam-awsmanpol-AmazonDMSVPCManagementRole")
- [AWS managed
  policy: AWSDMSServerlessServiceRolePolicy](#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy "#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy")
- [AWS managed
  policy: AmazonDMSCloudWatchLogsRole](#security-iam-awsmanpol-AmazonDMSCloudWatchLogsRole "#security-iam-awsmanpol-AmazonDMSCloudWatchLogsRole")
- [AWS
  managed policy: AWSDMSFleetAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSDMSFleetAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSDMSFleetAdvisorServiceRolePolicy")
- [AWS managed policy:
  AmazonDMSRedshiftS3Role](#security-iam-awsmanpol-AmazonDMSRedshiftS3Role "#security-iam-awsmanpol-AmazonDMSRedshiftS3Role")
- [AWS DMS updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed

policy: AmazonDMSVPCManagementRole

This policy is attached to the `dms-vpc-role` role, which allows AWS DMS to
perform actions on your behalf.

This policy grants contributor permissions that allow AWS DMS to manage network
resources.

**Permissions details**

This policy includes the following operations:

- `ec2:CreateNetworkInterface` – AWS DMS needs this permission
  to create network interfaces. These interfaces are essential for the AWS DMS
  replication instance to connect to the source and target databases.
- `ec2:DeleteNetworkInterface` – AWS DMS needs this permission
  to clean up network interfaces that it created once they are no longer needed.
  This helps in resource management and avoiding unnecessary costs.
- `ec2:DescribeAvailabilityZones` – This permission allows
  AWS DMS to retrieve information about the availability zones in a region. AWS DMS
  uses this information to ensure that it provisions resources in the correct
  zones for redundancy and availability.
- `ec2:DescribeDhcpOptions` – AWS DMS retrieves the DHCP options
  set details for the specified VPC. This information is required to configure the
  networking correctly for the replication instances.
- `ec2:DescribeInternetGateways` – AWS DMS may require this
  permission to understand the internet gateways configured in the VPC. This
  information is crucial if the replication instance or databases need internet
  access.
- `ec2:DescribeNetworkInterfaces` – AWS DMS retrieves
  information about existing network interfaces within the VPC. This information
  is necessary for AWS DMS to configure the network interfaces correctly and ensure
  proper network connectivity for the migration process.
- `ec2:DescribeSecurityGroups` – Security groups control the
  inbound and outbound traffic to instances and resources. AWS DMS needs to describe
  security groups to correctly configure network interfaces and ensure proper
  communication between the replication instance and the databases.
- `ec2:DescribeSubnets` – This permission allows AWS DMS to list
  the subnets in a VPC. AWS DMS uses this information to launch replication
  instances in the appropriate subnets, ensuring they have the necessary network
  connectivity.
- `ec2:DescribeVpcs` – Describing VPCs is essential for AWS DMS
  to understand the network environment where the replication instance and
  databases reside. This includes knowing the CIDR blocks and other VPC-specific
  configurations.
- `ec2:ModifyNetworkInterfaceAttribute` – This permission is
  required for AWS DMS to modify attributes of the network interfaces it manages.
  This could include adjusting settings to ensure connectivity and
  security.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:ModifyNetworkInterfaceAttribute"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed

policy: AWSDMSServerlessServiceRolePolicy

This policy is attached to the `AWSServiceRoleForDMSServerless` role, which
allows AWS DMS to perform actions on your behalf. For more information, see [Service-linked role for AWS DMS Serverless](slr-services-sl.md "slr-services-sl.md").

This policy grants contributor permissions that allow AWS DMS to manage replication
resources.

**Permissions details**

This policy includes the following permissions.

- **AWS DMS** – Allows principals to interact
  with AWS DMS resources.
- **Amazon S3** – Allows S3 to create an S3
  bucket to store a serverless premigration assessment. The serverless
  premigration assessment result will be stored with a
  `dms-severless-premigration-assessment-<UUID>` prefix. The
  S3 bucket is created for one user per Region and its bucket policy limits access
  to only the service's service role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "id0",
 "Effect": "Allow",
 "Action": [
 "dms:CreateReplicationInstance",
 "dms:CreateReplicationTask"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "dms:req-tag/ResourceCreatedBy": "DMSServerless"
 }
 }
 },
 {
 "Sid": "id1",
 "Effect": "Allow",
 "Action": [
 "dms:DescribeReplicationInstances",
 "dms:DescribeReplicationTasks"
 ],
 "Resource": "*"
 },
 {
 "Sid": "id2",
 "Effect": "Allow",
 "Action": [
 "dms:StartReplicationTask",
 "dms:StopReplicationTask",
 "dms:ModifyReplicationTask",
 "dms:DeleteReplicationTask",
 "dms:ModifyReplicationInstance",
 "dms:DeleteReplicationInstance"
 ],
 "Resource": [
 "arn:aws:dms:*:*:rep:*",
 "arn:aws:dms:*:*:task:*"
 ],
 "Condition": {
 "StringEqualsIgnoreCase": {
 "aws:ResourceTag/ResourceCreatedBy": "DMSServerless"
 }
 }
 },
 {
 "Sid": "id3",
 "Effect": "Allow",
 "Action": [
 "dms:TestConnection",
 "dms:DeleteConnection"
 ],
 "Resource": [
 "arn:aws:dms:*:*:rep:*",
 "arn:aws:dms:*:*:endpoint:*"
 ]
 },
 {
 "Sid": "id4",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:PutObjectTagging"
 ],
 "Resource": [
 "arn:aws:s3:::dms-serverless-premigration-results-*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "id5",
 "Effect": "Allow",
 "Action": [
 "s3:PutBucketPolicy",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "s3:CreateBucket"
 ],
 "Resource": [
 "arn:aws:s3:::dms-serverless-premigration-results-*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "id6",
 "Effect": "Allow",
 "Action": [
 "dms:StartReplicationTaskAssessmentRun"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEqualsIgnoreCase": {
 "aws:ResourceTag/ResourceCreatedBy": "DMSServerless"
 }
 }
 }
 ]
}`

```

## AWS managed

policy: AmazonDMSCloudWatchLogsRole

This policy is attached to the `dms-cloudwatch-logs-role` role, which
allows AWS DMS to perform actions on your behalf. For more information, see [Using service-linked roles for
AWS DMS](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants contributor permissions that allow AWS DMS to publish replication
logs to CloudWatch logs.

**Permissions details**

This policy includes the following permissions.

- `logs` – Allows principals to publish logs to CloudWatch Logs. This
  permission is required so that AWS DMS can use CloudWatch to display replication
  logs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDescribeOnAllLogGroups",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowDescribeOfAllLogStreamsOnDmsTasksLogGroup",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:dms-tasks-*",
 "arn:aws:logs:*:*:log-group:dms-serverless-replication-*"
 ]
 },
 {
 "Sid": "AllowCreationOfDmsLogGroups",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:dms-tasks-*",
 "arn:aws:logs:*:*:log-group:dms-serverless-replication-*:log-stream:"
 ]
 },
 {
 "Sid": "AllowCreationOfDmsLogStream",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:dms-tasks-*:log-stream:dms-task-*",
 "arn:aws:logs:*:*:log-group:dms-serverless-replication-*:log-stream:dms-serverless-*"
 ]
 },
 {
 "Sid": "AllowUploadOfLogEventsToDmsLogStream",
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:dms-tasks-*:log-stream:dms-task-*",
 "arn:aws:logs:*:*:log-group:dms-serverless-replication-*:log-stream:dms-serverless-*"
 ]
 }
 ]
}`

```

## AWS

managed policy: AWSDMSFleetAdvisorServiceRolePolicy

You can't attach AWSDMSFleetAdvisorServiceRolePolicy to your IAM entities. This
policy is attached to a service-linked role that allows AWS DMS Fleet Advisor to
perform actions on your behalf. For more information, see [Using service-linked roles for
AWS DMS](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants contributor permissions that allow AWS DMS Fleet Advisor to publish
Amazon CloudWatch metrics.

**Permissions details**

This policy includes the following permissions.

- `cloudwatch` – Allows principals to publish metric data
  points to Amazon CloudWatch. This permission is required so that AWS DMS Fleet Advisor can
  use CloudWatch to display charts with database metrics.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/DMS/FleetAdvisor"
 }
 }
 }
}`

```

## AWS managed policy:

AmazonDMSRedshiftS3Role

This policy provides permissions that allow AWS DMS to manage S3 settings for Redshift
endpoints.

**Permissions details**

This policy includes the following operations:

- `s3:CreateBucket` - Allows DMS to create S3 buckets with the "dms-"
  prefix
- `s3:ListBucket` - Allows DMS to list the contents of S3 buckets
  with the "dms-" prefix
- `s3:DeleteBucket` - Allows DMS to delete S3 buckets with the "dms-"
  prefix
- `s3:GetBucketLocation` - Allows DMS to retrieve the Region where an
  S3 bucket is located
- `s3:GetObject` - Allows DMS to retrieve objects from S3 buckets
  with the "dms-" prefix
- `s3:PutObject` - Allows DMS to add objects to S3 buckets with the
  "dms-" prefix
- `s3:DeleteObject` - Allows DMS to delete objects from S3 buckets
  with the "dms-" prefix
- `s3:GetObjectVersion` - Allows DMS to retrieve specific versions of
  objects in versioned buckets
- `s3:GetBucketPolicy` - Allows DMS to retrieve bucket
  policies
- `s3:PutBucketPolicy` - Allows DMS to create or update bucket
  policies
- `s3:GetBucketAcl` - Allows DMS to retrieve bucket access control
  lists (ACLs)
- `s3:PutBucketVersioning` - Allows DMS to enable or suspend
  versioning on buckets
- `s3:GetBucketVersioning` - Allows DMS to retrieve the versioning
  status of buckets
- `s3:PutLifecycleConfiguration` - Allows DMS to create or update
  lifecycle rules for buckets
- `s3:GetLifecycleConfiguration` - Allows DMS to retrieve lifecycle
  rules configured for buckets
- `s3:DeleteBucketPolicy` - Allows DMS to delete bucket
  policies

All these permissions apply only to resources with ARN pattern:
`arn:aws:s3:::dms-*`

**JSON policy document**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:ListBucket",
 "s3:DeleteBucket",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetObjectVersion",
 "s3:GetBucketPolicy",
 "s3:PutBucketPolicy",
 "s3:GetBucketAcl",
 "s3:PutBucketVersioning",
 "s3:GetBucketVersioning",
 "s3:PutLifecycleConfiguration",
 "s3:GetLifecycleConfiguration",
 "s3:DeleteBucketPolicy"
 ],
 "Resource": "arn:aws:s3:::dms-*"
 }
 ]
}`

```

## AWS DMS updates to AWS managed

policies

View details about updates to AWS managed policies for AWS DMS since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the AWS DMS Document history page.

| Change                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                           | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [Service-linked role for AWS DMS Serverless](slr-services-sl.md "slr-services-sl.md") –<br>Change                                                                                | AWS DMS updated `AWSDMSServerlessServiceRolePolicy`<br>to allow `dms:StartReplicationTaskAssessmentRun` to<br>support running premigration assessments. AWS DMS also updated the<br>serverless service-linked role to create S3 buckets and put the<br>premigration assessment results into those buckets.                                            | February 14, 2025 |
| [AWSDMSServerlessServiceRolePolicy](#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy "#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy") – Change              | AWS DMS added `dms:ModifyReplicationTask` which is<br>required by AWS DMS Serverless to call the<br>`ModifyReplicationTask` operation to modify a<br>replication task. AWS DMS added<br>`dms:ModifyReplicationInstance` which is required by<br>AWS DMS Serverless to call `ModifyReplicationInstance`<br>operation to modify a replication instance. | January 17, 2025  |
| [AmazonDMSVPCManagementRole](#security-iam-awsmanpol-AmazonDMSVPCManagementRole "#security-iam-awsmanpol-AmazonDMSVPCManagementRole") – Change                                   | AWS DMS added `ec2:DescribeDhcpOptions` and<br>`ec2:DescribeNetworkInterfaces` operations to allow<br>AWS DMS to manage network settings on your behalf.                                                                                                                                                                                              | June 17, 2024     |
| [AWSDMSServerlessServiceRolePolicy](#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy "#security-iam-awsmanpol-AWSDMSServerlessServiceRolePolicy") – New<br>policy       | AWS DMS added the `AWSDMSServerlessServiceRolePolicy`<br>role to allow AWS DMS to create and manage services on your behalf,<br>such as publishing Amazon CloudWatch metrics.                                                                                                                                                                         | May 22, 2023      |
| [AmazonDMSCloudWatchLogsRole](#security-iam-awsmanpol-AmazonDMSCloudWatchLogsRole "#security-iam-awsmanpol-AmazonDMSCloudWatchLogsRole") – Change                                | AWS DMS added the ARN for serverless resources to each of the<br>permissions granted, to allow uploading AWS DMS replication logs from<br>serverless replication configurations to CloudWatch Logs.                                                                                                                                                   | May 22, 2023      |
| [AWSDMSFleetAdvisorServiceRolePolicy](#security-iam-awsmanpol-AWSDMSFleetAdvisorServiceRolePolicy "#security-iam-awsmanpol-AWSDMSFleetAdvisorServiceRolePolicy") – New<br>policy | AWS DMS Fleet Advisor added a new policy to allow publishing<br>metric data points to Amazon CloudWatch.                                                                                                                                                                                                                                              | March 6, 2023     |
| AWS DMS started tracking<br>changes                                                                                                                                              | AWS DMS started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                     | March 6, 2023     |
