

# Getting started with Amazon EC2 High Availability for SQL Server
<a name="sql-high-availability-get-started"></a>

To get started with Amazon EC2 High Availability for SQL Server (SQL HA), perform the following steps:

**Topics**
+ [Step 1: Set up SSM Agent](#sql-high-availability-ssm)
+ [Step 2: Attach AWS managed policy to instances](#sql-high-availability-role)
+ [Step 3: (*Optional*) Store SQL Server credentials in AWS Secrets Manager](#sql-high-availability-secret)
+ [Step 4: EnableSQL HA license savings](#sql-high-availability-register)
+ [Windows user setup](sql-high-availability-windows-user-setup.md)

## Step 1: Set up SSM Agent
<a name="sql-high-availability-ssm"></a>

The Systems Manager Agent (SSM Agent) must be installed and running on the Amazon EC2 SQL Server instances with the High Availability deployments. The SSM Agent executes an SSM document to determine and report the SQL HA state for the instance.

The SSM Agent is preinstalled, by default, on the Amazon Machine Images (AMIs) for Windows and SQL Server provided by Amazon. For more information, see [AWS Windows AMIs](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-amis.html). To check if SSM Agent is correctly configured on your instances, you can use the System Manager console, or call [ DescribeInstanceInformation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstanceInformation.html) to verify the SSM Agent [ PingStatus](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstanceInformation.html#systemsmanager-Type-InstanceInformation-PingStatus) is Online. If necessary, you can manually download and install the latest version of SSM Agent on your Amazon EC2 SQL Server instances. For more information, see [ Manually install the SSM Agent on Amazon EC2 instances for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-windows.html).

## Step 2: Attach AWS managed policy to instances
<a name="sql-high-availability-role"></a>

To ensure that your instance has the required IAM permissions, you must attach the following AWS managed policies to the instance:
+ **AWSEC2SqlHaInstancePolicy** — grants permissions for SQL HA to execute AWS Systems Manager (SSM) Run Command document `AWSEC2-DetectSqlHaState` to automatically detect the standby state of your SQL Server instances.
+ **AmazonSSMManagedInstanceCore** — enables AWS Systems Manager service core functionality.

For more information, see Attach an IAM role to an Amazon EC2 instance.

**Note**  
If needed, you can create and attach your own custom IAM role. However, at a minimum, the role must include all of the permissions that are included in the **AWSEC2SqlHaInstancePolicy** AWS managed policy.

## Step 3: (*Optional*) Store SQL Server credentials in AWS Secrets Manager
<a name="sql-high-availability-secret"></a>

**By default**, AWS Systems Manager uses the built-in `[NT AUTHORITY\SYSTEM]` user to access SQL Server HA metadata. If you choose to use the built-in `[NT AUTHORITY\SYSTEM]` user, you may need to configure Windows user permissions to ensure the service can obtain High Availability metadata from your SQL Server instances. For more information, see [Windows user setup for Amazon EC2 High Availability for SQL Server](sql-high-availability-windows-user-setup.md).

**Alternatively**, if your security policies have restricted or disabled the `[NT AUTHORITY\SYSTEM]` account, you will need to store and use your SQL Server credentials in AWS Secrets Manager. For more information, see [ Create a secret in AWS Secrets Manager with appropriate SQL Server permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).

## Step 4: EnableSQL HA license savings
<a name="sql-high-availability-register"></a>

You must enable SQL HA standby detection for Windows SQL Server license-included instances to receive SQL Server license savings. Use one of the following methods:

------
#### [ Console ]

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation panel, choose **Instances**.

1. Select the instances in the High Availability deployment to enable SQL HA standby detection monitoring, choose **Actions**, **Instance settings**, **Modify SQL High Availability settings**.

1. In the **Review prerequisites** step, review each instance to make sure it is configured correctly.
   + The **SSM agent status** column indicates the state of the SSM Agent on the instance. **Online** indicates that the SSM Agent is running and accessible.
   + The **Recommended IAM policies** column indicates whether the instance has an attached IAM role with the required permissions. We recommend attaching the service managed policy AWSEC2SqlHaInstancePolicy to the instance or you can use any equivalent custom inline policy. **Verified** indicates that the instance has the managed policy attached while it doesn't verify the permission if you use other custom policies. The **IAM role** column indicates the currently attached IAM role. To attach a different role, choose **Modify IAM role**.

1. Choose **Next**.

1. In the **Manage SQL High Availability license savings** step, for each instance do the following:
   + For **SQL High Availability license savings**, select **Enable**.
   + (*Optional*) For **SQL Server credentials**, select the secret that has the SQL Server credentials for that instance .

1. Choose **Next**.

1. In the **Review and apply changes** step, review the configuration and then choose **Apply changes**.

------
#### [ AWS CLI ]

Use the [ enable-instance-sql-ha-standby-detections](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-instance-sql-ha-standby-detections.html) command. For `instance-ids` specify the IDs of the instances to opt in. Specify multiple instance IDs as a space-separated list. If you choose to perform Step 3: Create secret for SQL Server credentials, specify the optional `--sql-server-credentials` parameter. This parameter takes the Amazon Web Services secret ARN that has the SQL Server credentials.

```
aws ec2 enable-instance-sql-ha-standby-detections \
--instance-ids {{i-1234567890abcdef0}} {{i-0fedcba0987654321}} \
--sql-server-credentials {{arn:aws:secretsmanager:us-east-1:111122223333:secret:my-sql-creds}}
```

You can run these commands from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) pre-installed.

------
#### [ PowerShell ]

Use the [ Enable-EC2InstanceSqlHaStandbyDetection](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-EC2InstanceSqlHaStandbyDetection.html) cmdlet. For `-InstanceId` specify the IDs of the instances to opt in. If you choose to perform Step 3: Create secret for SQL Server credentials, specify the optional `-SqlServerCredential` parameter. This parameter takes the Amazon Web Services secret ARN that has the SQL Server credentials.

```
Enable-EC2InstanceSqlHaStandbyDetection `
-InstanceId '{{i-1234567890abcdef0}}','{{i-0fedcba0987654321}}' `
-SqlServerCredential '{{arn:aws:secretsmanager:us-east-1:111122223333:secret:my-sql-creds}}'
```

You can run these cmdlets from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) pre-installed. Run `pwsh` to start PowerShell.

------