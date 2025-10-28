# Console Read-Only Access Policy

- AWSElasticDisasterRecoveryReadOnlyAccess

You can attach the AWSElasticDisasterRecoveryReadOnlyAccess policy to your IAM
identities.

This policy provides permissions to all read-only public APIs of AWS Elastic Disaster Recovery
(AWS DRS), as well as some read-only APIs of IAM, EC2 and SSM in order to list and view installed roles
Recovery Instances, Source Servers and post-launch actions. Attach this
policy to your users or roles.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DRSReadOnlyAccess1",
 "Effect": "Allow",
 "Action": [
 "drs:DescribeJobLogItems",
 "drs:DescribeJobs",
 "drs:DescribeRecoveryInstances",
 "drs:DescribeRecoverySnapshots",
 "drs:DescribeReplicationConfigurationTemplates",
 "drs:DescribeSourceServers",
 "drs:GetFailbackReplicationConfiguration",
 "drs:GetLaunchConfiguration",
 "drs:GetReplicationConfiguration",
 "drs:ListExtensibleSourceServers",
 "drs:ListStagingAccounts",
 "drs:ListTagsForResource",
 "drs:ListLaunchActions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DRSReadOnlyAccess2",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeLaunchTemplateVersions",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DRSReadOnlyAccess4",
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "*"
 },
 {
 "Sid": "DRSReadOnlyAccess5",
 "Effect": "Allow",
 "Action": "ssm:ListCommandInvocations",
 "Resource": "*"
 },
 {
 "Sid": "DRSReadOnlyAccess6",
 "Effect": "Allow",
 "Action": "ssm:GetParameter",
 "Resource": "arn:aws:ssm:*:*:parameter/ManagedByAWSElasticDisasterRecovery-*"
 },
 {
 "Sid": "DRSReadOnlyAccess7",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeDocument",
 "ssm:GetDocument"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:document/AWS-CreateImage",
 "arn:aws:ssm:*:*:document/AWSMigration-ValidateNetworkConnectivity",
 "arn:aws:ssm:*:*:document/AWSMigration-VerifyMountedVolumes",
 "arn:aws:ssm:*:*:document/AWSMigration-ValidateHttpResponse",
 "arn:aws:ssm:*:*:document/AWSMigration-ValidateDiskSpace",
 "arn:aws:ssm:*:*:document/AWSMigration-VerifyProcessIsRunning",
 "arn:aws:ssm:*:*:document/AWSMigration-LinuxTimeSyncSetting",
 "arn:aws:ssm:*:*:document/AWSEC2-ApplicationInsightsCloudwatchAgentInstallAndConfigure"
 ]
 },
 {
 "Sid": "DRSReadOnlyAccess8",
 "Effect": "Allow",
 "Action": [
 "ssm:GetAutomationExecution"
 ],
 "Resource": "arn:aws:ssm:*:*:automation-execution/*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/AWSElasticDisasterRecoveryManaged": "false"
 }
 }
 }
 ]
}`

```
