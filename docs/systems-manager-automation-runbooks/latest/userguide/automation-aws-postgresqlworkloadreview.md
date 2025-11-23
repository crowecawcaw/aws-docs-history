# `AWSPremiumSupport-PostgreSQLWorkloadReview`

**Description**

The `AWSPremiumSupport-PostgreSQLWorkloadReview` runbook captures
multiple snapshots of your Amazon Relational Database Service (Amazon RDS) PostgreSQL database usage statistics.
The statistics captured are required for an Support [Proactive Services](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/ "https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/") expert to perform an operational review. The
statistics are collected using a set of custom SQL and shell scripts. These scripts
are downloaded to a temporary Amazon Elastic Compute Cloud (Amazon EC2) instance in your AWS account that
is created by this runbook. The runbook requires you to provide credentials using an
AWS Secrets Manager secret containing a username and password key-value pair. The username
must have permissions to query the standard PostgreSQL statistics views and
functions.

This runbook automatically creates the following AWS resources in your
AWS account using an AWS CloudFormation stack. You can monitor the stack creation using the
CloudFormation console.

- A virtual private cloud (VPC) and an Amazon EC2 instance launched in a private
  subnet of the VPC with optional connectivity to the internet using a NAT
  gateway.
- An AWS Identity and Access Management (IAM) role that is attached to the temporary Amazon EC2 instance
  with permissions to retrieve the Secrets Manager secret value. The role also provides
  permissions to upload files to an Amazon Simple Storage Service (Amazon S3) bucket of your choice, and
  optionally to an Support case.
- A VPC peering connection to allow connectivity between your DB instance
  and the temporary Amazon EC2 instance.
- Systems Manager, Secrets Manager, and Amazon S3 VPC endpoints that are attached to the temporary
  VPC.
- A maintenance window with registered tasks that periodically start and
  stop the temporary Amazon EC2 instance, run data collection scripts, and upload
  files to an Amazon S3 bucket. An IAM role is also created for the maintenance
  window that provides permissions to perform the registered tasks.
  When the runbook completes, the CloudFormation stack that is used to create the necessary
  AWS resources is deleted and the report is uploaded to the Amazon S3 bucket of your
  choice, and optionally an Support case.

###### Note

By default, the root Amazon EBS volume of the temporary Amazon EC2 instance is
preserved. You can override this option by setting the
`EbsVolumeDeleteOnTermination` parameter to
`true`.

**Prerequisites**

- **Enterprise Support subscription** This
  runbook and the Proactive Services Workload Diagnostics and Reviews require
  an Enterprise Support Subscription. Before using this runbook, contact your
  Technical Account Manager (TAM) or Specialist TAM (STAM) for instructions.
  For more information, see [Support Proactive Services](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/ "https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/").
- **Account and AWS Region quotas** Be sure you
  have not reached the maximum number of Amazon EC2 instances or VPCs that you can
  create in your account and Region where you use this runbook. If you need to
  request a limit increase, see the [Service limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase/ "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase/").
- **Database configuration**
  1.  The database you specify in the `DatabaseName`
      parameter should have the `pg_stat_statements` extension
      configured. If you have not configured
      `pg_stat_statements` in
      `shared_preload_libraries`, then you must edit the
      value in the DB Parameter Group and apply the changes. Changes to
      the parameter `shared_preload_libraries` requires you to
      reboot your DB instance. For more information, see [Working with parameter groups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.md"). Adding
      `pg_stat_statements` to
      `shared_preload_libraries` will add some performance
      overhead. However, this is useful for tracking performance of
      individual statements. For more information about the
      `pg_stat_statements` extension, see the [PostgreSQL documentation](https://www.postgresql.org/docs/10/pgstatstatements.html "https://www.postgresql.org/docs/10/pgstatstatements.html"). If you don't configure the
      `pg_stat_statements` extension or if the extension is
      not present in the database being used for statistics collection,
      the statement level analysis will not be presented in the
      operational review.
  2.  Make sure that `track_counts` and
      `track_activities` parameters are not turned off. If
      these parameters are turned off in the DB Parameter Group, no
      meaningful statistics will be available. Changing these parameters
      will require you to reboot your DB instance. For more information,
      see [Working with parameters on your Amazon RDS for PostgreSQL DB
      instance](../../../AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../../../AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.md").
  3.  If the `track_io_timing` parameter is turned off, the
      I/O level statistics will not be included in the operational review.
      Changing `track_io_timing` will require you to reboot
      your DB instance and will incur additional performance overhead
      depending on the DB instance workload. Despite the performance
      overhead for critical workloads, this parameter provides useful
      information related to I/O time per query.

**Billing and charges** Your AWS account will be
charged for the costs associated with the temporary Amazon EC2 instance, associated Amazon EBS
volume, the NAT gateway, and the data transferred while this automation is running.
By default, this runbook creates a `t3.micro` Amazon Linux 2 instance to collect
the statistics. The runbook starts and stops the instance between steps to reduce
costs.

**Data security and governance** This runbook collects
statistics by querying the [PostgreSQL
statistics views and functions](https://www.postgresql.org/docs/current/monitoring-stats.html "https://www.postgresql.org/docs/current/monitoring-stats.html"). Make sure the credentials provided in
the `SecretId` parameter only allow read-only permissions to the
statistics views and functions. As part of the automation, the collection scripts
are uploaded to your Amazon S3 bucket and can be located in
`s3://`amzn-s3-demo-bucket`/`automation
execution id`/queries/`.

These scripts collect data that is used by an AWS Specialist to review key
performance indicators at object level. The script collects information such as
table name, schema name, and index name. If any of this information contains
sensitive information like revenue indicators, username, email address, or any other
personally identifiable information, then we recommend that you discontinue with
this workload review. Contact your AWS TAM to discuss an alternative approach for
the workload review.

Make sure you have the necessary approval and clearance to share the statistics
and metadata collected by this automation with AWS.

**Security considerations** If you set the
`UpdateRdsSecurityGroup` parameter to `yes`, the runbook
updates the security group associated with your DB instance to allow inbound traffic
from the temporary Amazon EC2 instance's private IP address.

If you set the `UpdateRdsRouteTable` parameter to `yes`, the
runbook updates the route table associated with the subnet your DB instance is
running in to allow traffic to the temporary Amazon EC2 instance through the VPC peering
connection.

**User creation** To allow the collection script to
connect to your Amazon RDS database, you must set up a user with permissions to read the
statistic views. Then you must store the credentials in Secrets Manager. We recommend creating
a new dedicated user for this automation. Creating a separate user allows you to
audit and track activities performed by this automation.

1. Create a new user.

`psql -h <database_connection_endpoint> -p
 <database_port> -U <admin_user> -c "CREATE USER
 <user_name> PASSWORD '<password>';"` 2. Ensure that this user can only make read-only connections.

`psql -h <database_connection_endpoint> -p
 <database_port> -U <admin_user> -c "ALTER USER
 <user_name> SET default_transaction_read_only=true;"` 3. Set user level limits.

`psql -h <database_connection_endpoint> -p
 <database_port> -U <admin_user> -c "ALTER USER
 <user_name> SET work_mem=4096;"`

`psql -h <database_connection_endpoint> -p
 <database_port> -U <admin_user> -c "ALTER USER
 <user_name> SET statement_timeout=10000;"`

`psql -h <database_connection_endpoint> -p
 <database_port> -U <admin_user> -c "ALTER USER
 <user_name> SET
 idle_in_transaction_session_timeout=60000;"` 4. Grant `pg_monitor` permissions to the new user so it can access
the DB statistics. (The `pg_monitor` role is a member of
`pg_read_all_settings`, `pg_read_all_stats`, and
`pg_stat_scan_table`.)

`psql -h <database_connection_endpoint> -p
 <database_port> -U <admin_user> -c "GRANT pg_monitor to
 <user_name>;"`

**Permissions added to the temporary Amazon EC2 instance profile by
this Systems Manager Automation** The following permissions are added to the
IAM role associated with the temporary Amazon EC2 instance. The
`AmazonSSMManagedInstanceCore` managed policy is also associated with
the IAM role to allow the Amazon EC2 instance to be managed by Systems Manager.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:DescribeTags"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`automation-execution-id`/*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-id`",
 "Effect": "Allow"
 },
 {
 "Action": [
 "support:AddAttachmentsToSet",
 "support:AddCommunicationToCase",
 "support:DescribeCases"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

**Permissions added to the temporary maintenance window by this
Systems Manager Automation** The following permissions are automatically added to
the IAM role associated with the Maintenance Windows tasks. The Maintenance Windows tasks starts, stops,
and sends commands to the temporary Amazon EC2 instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ssm:GetAutomationExecution",
 "ssm:ListCommands",
 "ssm:ListCommandInvocations",
 "ssm:GetCommandInvocation",
 "ssm:GetCalendarState",
 "ssm:CancelCommand",
 "ec2:DescribeInstanceStatus"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "ssm:SendCommand",
 "ec2:StartInstances",
 "ec2:StopInstances",
 "ssm:StartAutomationExecution"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`temporary-instance-id`",
 "arn:aws:ssm:*:*:document/AWS-RunShellScript",
 "arn:aws:ssm:*:*:automation-definition/AWS-StopEC2Instance:$DEFAULT",
 "arn:aws:ssm:*:*:automation-definition/AWS-StartEC2Instance:$DEFAULT"
 ],
 "Effect": "Allow"
 },
 {
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "ssm.amazonaws.com"
 },
 "ArnLike": {
 "iam:AssociatedResourceARN": "arn:aws:ssm:*:*:automation-definition/AWS-*"
 }
 },
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/SSM-*",
 "Effect": "Allow"
 }
 ]
}`

```

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-PostgreSQLWorkloadReview "https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-PostgreSQLWorkloadReview")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- DBInstanceIdentifier

Type: String

Description: (Required) The ID of your DB instance.

- DatabaseName

Type: String

Description: (Required) The database name hosted on your DB
instance.

- SecretId

Type: String

Description: (Required) The ARN of your Secrets Manager secret containing the
username and password key value pair. The CloudFormation stack creates an IAM
policy with permissions for the `GetSecretValue` operation to
this ARN. The credentials are used to allow the temporary instance to
collect the database statistics. Contact your TAM or STAM to discuss the
minimum required permissions.

- Acknowledge

Type: String

Description: (Required) Enter `yes` if you
acknowledge that this runbook will create temporary resources in your
account to collect statistics from your DB instance. We recommend contacting
your TAM or STAM before running this automation.

- SupportCase

Type: String

Description: (Optional) The Support case number provided by your TAM or
STAM. If provided, the runbook updates the case and attaches the data
collected. This option requires the temporary Amazon EC2 instance to have
internet connectivity to access the Support API endpoint. You must set the
`AllowVpcInternetAccess` parameter to `true`. The
case subject must contain the phrase
`AWSPremiumSupport-PostgreSQLWorkloadReview`.

- S3BucketName

Type: String

Description: (Required) The Amazon S3 bucket name in your account where you
want to upload the data collected by the automation. Verify the bucket
policy does not grant any unnecessary read or write permissions to
principals that do not need access to the contents of the bucket. We
recommend creating a new temporary Amazon S3 bucket for the purpose of this
automation. The runbook provides permissions to the
`s3:PutObject` API operation to the IAM role attached to
the temporary Amazon EC2 instance. The uploaded files will be located in
`s3://`bucket
name`/`automation execution
id`/`.

- InstanceType

Type: String

Description: (Optional) The type of the temporary Amazon EC2 instance that will
run the custom SQL and shell scripts.

Valid values: t2.micro | t2.small | t2.medium | t2.large | t3.micro |
t3.small | t3.medium | t3.large

Default: t3.micro

- VpcCidr

Type: String

Description: (Optional) The IP address range in CIDR notation for the new
VPC (for example, `172.31.0.0/16`). Make sure you select a CIDR
that does not overlap or match any existing VPC with connectivity to your DB
instance. The smallest VPC you can create uses a /28 subnet mask, and the
largest VPC uses a /16 subnet mask.

Default: 172.31.0.0/16

- StackResourcesNamePrefix

Type: String

Description: (Optional) The CloudFormation stack resources name prefix and tag. The
runbook creates the CloudFormation stack resources using this prefix as part of the
name and tag applied to the resources. The structure for the tag key-value
pair is
``StackResourcesNamePrefix`:{{automation:EXECUTION_ID}}`.

Default: AWSPostgreSQLWorkloadReview

- Schedule

Type: String

Description: (Optional) The maintenance window schedule. Specifies how
often the maintenance window runs the tasks. The default value is every
`1 hour`.

Valid values: 15 minutes | 30 minutes | 1 hour | 2 hours | 4 hours | 6
hours | 12 hours | 1 day | 2 days | 4 days

Default: 1 hour

- Duration

Type: Integer

Description: (Optional) The maximum duration, in minutes, you want to
allow the automation to run. The maximum duration supported is 8,640 minutes
(6 days). The default value is 4,320 minutes (3 days).

Valid values: 30-8640

Default: 4320

- UpdateRdsRouteTable

Type: String

Description: (Optional) If set to `true`, the runbook updates
the route table associated with the subnet your DB instance runs in. An IPv4
route is added to route traffic to the temporary Amazon EC2 instance private IPV4
address through the newly created VPC peering connection.

Valid values: true | false

Default: false

- AllowVpcInternetAccess

Type: String

Description: (Optional) If set to `true`, the runbook creates a
NAT gateway to provide internet connectivity to the temporary Amazon EC2 instance
to communicate with the Support API endpoint. You can leave this parameter as
`false` if you only want the runbook to upload the output to
your Amazon S3 bucket.

Valid values: true | false

Default: false

- UpdateRdsSecurityGroup

Type: String

Description: (Optional) If set to `true`, the runbook updates
the security group associated with your DB instance to allow traffic from
the temporary instance's private IP address.

Valid values: false | true

Default: false

- EbsVolumeDeleteOnTermination

Type: String

Description: (Optional) If set to `true`, the temporary Amazon EC2
instance's root volume is deleted after the runbook completes and deletes
the CloudFormation stack.

Valid values: false | true

Default: false
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudformation:CreateStack`
- `cloudformation:DeleteStack`
- `cloudformation:DescribeStackEvents`
- `cloudformation:DescribeStackResource`
- `cloudformation:DescribeStacks`
- `cloudformation:UpdateStack`
- `ec2:AcceptVpcPeeringConnection`
- `ec2:AllocateAddress`
- `ec2:AssociateRouteTable`
- `ec2:AssociateVpcCidrBlock`
- `ec2:AttachInternetGateway`
- `ec2:AuthorizeSecurityGroupEgress`
- `ec2:AuthorizeSecurityGroupIngress`
- `ec2:CreateEgressOnlyInternetGateway`
- `ec2:CreateInternetGateway`
- `ec2:CreateNatGateway`
- `ec2:CreateRoute`
- `ec2:CreateRouteTable`
- `ec2:CreateSecurityGroup`
- `ec2:CreateSubnet`
- `ec2:CreateTags`
- `ec2:CreateVpc`
- `ec2:CreateVpcEndpoint`
- `ec2:CreateVpcPeeringConnection`
- `ec2:DeleteEgressOnlyInternetGateway`
- `ec2:DeleteInternetGateway`
- `ec2:DeleteNatGateway`
- `ec2:DeleteRoute`
- `ec2:DeleteRouteTable`
- `ec2:DeleteSecurityGroup`
- `ec2:DeleteSubnet`
- `ec2:DeleteTags`
- `ec2:DeleteVpc`
- `ec2:DeleteVpcEndpoints`
- `ec2:DescribeAddresses`
- `ec2:DescribeEgressOnlyInternetGateways`
- `ec2:DescribeImages`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeInternetGateways`
- `ec2:DescribeNatGateways`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`
- `ec2:DescribeVpcEndpoints`
- `ec2:DescribeVpcPeeringConnections`
- `ec2:DescribeVpcs`
- `ec2:DetachInternetGateway`
- `ec2:DisassociateRouteTable`
- `ec2:DisassociateVpcCidrBlock`
- `ec2:ModifySubnetAttribute`
- `ec2:ModifyVpcAttribute`
- `ec2:RebootInstances`
- `ec2:ReleaseAddress`
- `ec2:RevokeSecurityGroupEgress`
- `ec2:RevokeSecurityGroupIngress`
- `ec2:StartInstances`
- `ec2:StopInstances`
- `ec2:RunInstances`
- `ec2:TerminateInstances`
- `iam:AddRoleToInstanceProfile`
- `iam:AttachRolePolicy`
- `iam:CreateInstanceProfile`
- `iam:CreateRole`
- `iam:DeleteInstanceProfile`
- `iam:DeleteRole`
- `iam:DeleteRolePolicy`
- `iam:DetachRolePolicy`
- `iam:GetInstanceProfile`
- `iam:GetRole`
- `iam:GetRolePolicy`
- `iam:PassRole`
- `iam:PutRolePolicy`
- `iam:RemoveRoleFromInstanceProfile`
- `iam:TagPolicy`
- `iam:TagRole`
- `rds:DescribeDBInstances`
- `s3:GetAccountPublicAccessBlock`
- `s3:GetBucketAcl`
- `s3:GetBucketPolicyStatus`
- `s3:GetBucketPublicAccessBlock`
- `s3:ListBucket`
- `ssm:AddTagsToResource`
- `ssm:CancelMaintenanceWindowExecution`
- `ssm:CreateDocument`
- `ssm:CreateMaintenanceWindow`
- `ssm:DeleteDocument`
- `ssm:DeleteMaintenanceWindow`
- `ssm:DeregisterTaskFromMaintenanceWindow`
- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeDocument`
- `ssm:DescribeInstanceInformation`
- `ssm:DescribeMaintenanceWindowExecutions`
- `ssm:GetCalendarState`
- `ssm:GetDocument`
- `ssm:GetMaintenanceWindowExecution`
- `ssm:GetParameters`
- `ssm:ListCommandInvocations`
- `ssm:ListCommands`
- `ssm:ListTagsForResource`
- `ssm:RegisterTaskWithMaintenanceWindow`
- `ssm:RemoveTagsFromResource`
- `ssm:SendCommand`
- `support:AddAttachmentsToSet`
- `support:AddCommunicationToCase`
- `support:DescribeCases`

**Document Steps**

1. `aws:assertAwsResourceProperty` - Confirms the DB instance is
   in the `available` state.
2. `aws:executeAwsApi` - Gathers details about the DB
   instance.
3. `aws:executeScript` - Checks if the Amazon S3 bucket specified in
   the `S3BucketName` allows anonymous, or public read or write
   access permissions.
4. `aws:executeScript` - Gets the CloudFormation template content from the
   Automation runbook attachment that is used to create the temporary AWS
   resources in your AWS account.
5. `aws:createStack` - Creates the CloudFormation stack resources.
6. `aws:waitForAwsResourceProperty` - Waits until the Amazon EC2
   instance created by the CloudFormation template is running.
7. `aws:executeAwsApi` - Gets the IDs for the temporary Amazon EC2
   instance and VPC peering connection created by CloudFormation.
8. `aws:executeAwsApi` - Gets the IP address for the temporary
   Amazon EC2 instance to configure connectivity with your DB instance.
9. `aws:executeAwsApi` - Tags the Amazon EBS volume attached to the
   temporary Amazon EC2 instance.
10. `aws:waitForAwsResourceProperty` - Waits until the temporary
    Amazon EC2 instance passes status checks.
11. `aws:waitForAwsResourceProperty` - Waits until the temporary
    Amazon EC2 instance is managed by Systems Manager. If this step times out or fails, then
    the runbook reboots the instance.
    1. `aws:executeAwsApi` - Reboots the temporary Amazon EC2
       instance if the previous step failed or timed out.
    2. `aws:waitForAwsResourceProperty` - Waits until the
       temporary Amazon EC2 instance is managed by Systems Manager after reboot.

12. `aws:runCommand` - Installs the metadata collector application
    requirements on the temporary Amazon EC2 instance.
13. `aws:runCommand` - Configures access to your DB instance by
    creating a configuration file on the temporary Amazon EC2 instance.
14. `aws:executeAwsApi` - Creates a maintenance window to
    periodically run the metadata collector application using Run Command. The
    maintenance window starts and stops the instance between commands.
15. `aws:waitForAwsResourceProperty` - Waits until the maintenance
    window created by the CloudFormation template is ready.
16. `aws:executeAwsApi` - Gets the IDs for the maintenance window
    and change calendar created by CloudFormation.
17. `aws:sleep` - Waits until the end date of the maintenance
    window.
18. `aws:executeAwsApi` - Turns off the maintenance window.
19. `aws:executeScript` - Gets the results of the tasks run during
    the maintenance window.
20. `aws:waitForAwsResourceProperty` - Waits for the maintenance
    window to finish the last task before continuing.
21. `aws:branch` - Branches the workflow based on whether you
    provided a value for the `SupportCase` parameter.
    1. `aws:changeInstanceState` - Starts the temporary Amazon EC2
       instance and waits for status checks to pass before uploading the
       report.
    2. `aws:waitForAwsResourceProperty` - Waits until the
       temporary Amazon EC2 instance is managed by Systems Manager. If this step timeouts
       or fail, then the runbook reboots the instance.
       1. `aws:executeAwsApi` - Reboots the temporary
          Amazon EC2 instance if the previous step failed or timed
          out.
       2. `aws:waitForAwsResourceProperty` - Waits until
          the temporary Amazon EC2 instance is managed by Systems Manager after
          reboot.

    3. `aws:runCommand` - Attaches the metadata report to the
       Support case if you provided a value for the `SupportCase`
       parameter. The script compresses and splits the report into 5 MB
       files. The maximum number of files the script attaches to a Support
       case is 12.

22. `aws:changeInstanceState` - Stops the temporary Amazon EC2 instance
    in case the CloudFormation stack fails to delete.
23. `aws:executeAwsApi` - Describes the CloudFormation stack events if the
    runbooks fails to create or update the CloudFormation stack.
24. `aws:waitForAwsResourceProperty` - Waits until the CloudFormation stack
    is in a terminal status before deleting.
25. `aws:executeAwsApi` - Deletes the CloudFormation stack excluding the
    maintenance window. The root Amazon EBS volume associated with the temporary
    Amazon EC2 instance is preserved if the `EbsVolumeDeleteOnTermination`
    parameter value was set to `false`.
