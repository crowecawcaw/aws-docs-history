# Getting started with Amazon EC2 High Availability for SQL Server

To get started with Amazon EC2 High Availability for SQL Server (SQL HA), perform the following steps:

###### Topics

- [Step 1: Set up SSM Agent](#sql-high-availability-ssm "#sql-high-availability-ssm")
- [Step 2: Attach AWS managed policy to instances](#sql-high-availability-role "#sql-high-availability-role")
- [Step 3: (Optional) Store
  SQL Server credentials in AWS Secrets Manager](#sql-high-availability-secret "#sql-high-availability-secret")
- [Step 4: EnableSQL HA license savings](#sql-high-availability-register "#sql-high-availability-register")
- [Windows user setup](sql-high-availability-windows-user-setup.md "sql-high-availability-windows-user-setup.md")

## Step 1: Set up SSM Agent

The Systems Manager Agent (SSM Agent) must be installed and running on the Amazon EC2
SQL Server instances with the High Availability deployments. The SSM Agent executes an SSM
document to determine and report the SQL HA state for the instance.

The SSM Agent is preinstalled, by default, on the Amazon Machine Images (AMIs) for Windows
and SQL Server provided by Amazon. For more information, see [AWS Windows AMIs](../../../ec2/latest/windows-ami-reference/windows-amis.md "../../../ec2/latest/windows-ami-reference/windows-amis.md"). To
check if SSM Agent is correctly configured on your instances, you can use the System Manager
console, or call [DescribeInstanceInformation](../../../systems-manager/latest/APIReference/API_DescribeInstanceInformation.md "../../../systems-manager/latest/APIReference/API_DescribeInstanceInformation.md") to verify the SSM Agent [PingStatus](../../../systems-manager/latest/APIReference/API_InstanceInformation.md#systemsmanager-Type-InstanceInformation-PingStatus "../../../systems-manager/latest/APIReference/API_InstanceInformation.md#systemsmanager-Type-InstanceInformation-PingStatus") is Online. If necessary, you can manually download and install
the latest version of SSM Agent on your Amazon EC2 SQL Server instances. For more information, see
[Manually install the SSM Agent on Amazon EC2 instances for Windows Server](../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md").

## Step 2: Attach AWS managed policy to instances

To ensure that your instance has the required IAM permissions, you must attach the following
AWS managed policies to the instance:

- **AWSEC2SqlHaInstancePolicy** — grants permissions for
  SQL HA to execute AWS Systems Manager (SSM) Run Command document `AWSEC2-DetectSqlHaState`
  to automatically detect the standby state of your SQL Server instances.
- **AmazonSSMManagedInstanceCore** — enables AWS Systems Manager
  service core functionality.

For more information, see Attach an IAM role to an Amazon EC2 instance.

###### Note

If needed, you can create and attach your own custom IAM role. However, at a minimum,
the role must include all of the permissions that are included in the
**AWSEC2SqlHaInstancePolicy** AWS managed policy.

## Step 3: (_Optional_) Store

SQL Server credentials in AWS Secrets Manager

**By default**, AWS Systems Manager uses the built-in `[NT AUTHORITY\SYSTEM]`
user to access SQL Server HA metadata. If you choose to use the built-in `[NT AUTHORITY\SYSTEM]` user,
you may need to configure Windows user permissions to ensure the service can obtain High Availability metadata from your
SQL Server instances. For more information, see [Windows
user setup for Amazon EC2 High Availability for SQL Server](sql-high-availability-windows-user-setup.md "sql-high-availability-windows-user-setup.md").

**Alternatively**, if your security policies have restricted or disabled the
`[NT AUTHORITY\SYSTEM]` account, you will need to store and use your SQL Server credentials in AWS Secrets Manager.
For more information, see [Create a secret in AWS Secrets Manager with appropriate SQL Server permissions](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md").

## Step 4: EnableSQL HA license savings

You must enable SQL HA standby detection for Windows SQL Server license-included instances
to receive SQL Server license savings. Use one of the following methods:

Console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Instances**.
3. Select the instances in the High Availability deployment to enable SQL HA standby
   detection monitoring, choose **Actions**, **Instance
   settings**, **Modify SQL High Availability settings**.
4. In the **Review prerequisites** step, review each
   instance to make sure it is configured correctly.
   - The **SSM agent status** column indicates the
     state of the SSM Agent on the instance. **Online**
     indicates that the SSM Agent is running and accessible.
   - The **Recommended IAM policies** column indicates
     whether the instance has an attached IAM role with the required
     permissions. We recommend attaching the service managed policy
     AWSEC2SqlHaInstancePolicy to the instance or you can use any
     equivalent custom inline policy. **Verified**
     indicates that the instance has the managed policy attached while it
     doesn't verify the permission if you use other custom policies. The
     **IAM role** column indicates the currently
     attached IAM role. To attach a different role, choose
     **Modify IAM role**.

5. Choose **Next**.
6. In the **Manage SQL High Availability license savings** step, for each
   instance do the following:
   - For **SQL High Availability license savings**, select
     **Enable**.
   - (_Optional_) For **SQL Server credentials**,
     select the secret that has the SQL Server credentials for that instance .

7. Choose **Next**.
8. In the **Review and apply changes** step, review the
   configuration and then choose **Apply changes**.

AWS CLI
Use the [enable-instance-sql-ha-standby-detections](../../../cli/latest/reference/ec2/enable-instance-sql-ha-standby-detections.md "../../../cli/latest/reference/ec2/enable-instance-sql-ha-standby-detections.md") command. For `instance-ids`
specify the IDs of the instances to opt in. If you choose to perform Step 3: Create secret
for SQL Server credentials, specify the optional `--sql-server-credentials` with the
Amazon Web Services secret arn that has the SQL Server credentials in.

```
aws ec2 enable-instance-sql-ha-standby-detections \
--instance-ids `instance_ids` \
--sql-server-credentials `secret_manager_secret_arn`
```
