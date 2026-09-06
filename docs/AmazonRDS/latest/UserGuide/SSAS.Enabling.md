

# Turning on SSAS
<a name="SSAS.Enabling"></a>

Use the following process to turn on SSAS for your DB instance:

1. Create a new option group, or choose an existing option group.

1. Add the `SSAS` option to the option group.

1. Associate the option group with the DB instance.

1. Allow inbound access to the virtual private cloud (VPC) security group for the SSAS listener port.

1. Turn on Amazon S3 integration.

## Creating an option group for SSAS
<a name="SSAS.OptionGroup"></a>

Use the AWS Management Console or the AWS CLI to create an option group that corresponds to the SQL Server engine and version of the DB instance that you plan to use.

**Note**  
You can also use an existing option group if it's for the correct SQL Server engine and version.

### Console
<a name="SSAS.OptionGroup.Console"></a>

The following console procedure creates an option group for SQL Server Standard Edition 2017.

**To create the option group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Choose **Create group**.

1. In the **Create option group** pane, do the following:

   1. For **Name**, enter a name for the option group that is unique within your AWS account, such as **ssas-se-2017**. The name can contain only letters, digits, and hyphens.

   1. For **Description**, enter a brief description of the option group, such as **SSAS option group for SQL Server SE 2017**. The description is used for display purposes.

   1. For **Engine**, choose **sqlserver-se**.

   1. For **Major engine version**, choose **14.00**.

1. Choose **Create**.

### CLI
<a name="SSAS.OptionGroup.CLI"></a>

The following CLI example creates an option group for SQL Server Standard Edition 2017.

**To create the option group**
+ Use one of the following commands.  
**Example**  

  For Linux, macOS, or Unix:

  ```
  aws rds create-option-group \
      --option-group-name {{ssas-se-2017}} \
      --engine-name {{sqlserver-se}} \
      --major-engine-version {{14.00}} \
      --option-group-description "{{SSAS option group for SQL Server SE 2017}}"
  ```

  For Windows:

  ```
  aws rds create-option-group ^
      --option-group-name {{ssas-se-2017}} ^
      --engine-name {{sqlserver-se}} ^
      --major-engine-version {{14.00}} ^
      --option-group-description "{{SSAS option group for SQL Server SE 2017}}"
  ```

## Adding the SSAS option to the option group
<a name="SSAS.Add"></a>

Next, use the AWS Management Console or the AWS CLI to add the `SSAS` option to the option group.

### Console
<a name="SSAS.Add.Console"></a>

**To add the SSAS option**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Choose the option group that you just created.

1. Choose **Add option**.

1. Under **Option details**, choose **SSAS** for **Option name**.

1. Under **Option settings**, do the following:

   1. For **Max memory**, enter a value in the range 10–80.

      **Max memory** specifies the upper threshold above which SSAS begins releasing memory more aggressively to make room for requests that are running, and also new high-priority requests. The number is a percentage of the total memory of the DB instance. The allowed values are 10–80, and the default is 45.

   1. For **Mode**, choose the SSAS server mode, **Tabular** or **Multidimensional**.

      If you don't see the **Mode** option setting, it means that Multidimensional mode isn't supported in your AWS Region. For more information, see [Limitations](Appendix.SQLServer.Options.SSAS.md#SSAS.Limitations).

      **Tabular** is the default.

   1. For **Security groups**, choose the VPC security group to associate with the option.
**Note**  
The port for accessing SSAS, 2383, is prepopulated.

1. Under **Scheduling**, choose whether to add the option immediately or at the next maintenance window.

1. Choose **Add option**.

### CLI
<a name="SSAS.Add.CLI"></a>

**To add the SSAS option**

1. Create a JSON file, for example `ssas-option.json`, with the following parameters:
   + `OptionGroupName` – The name of option group that you created or chose previously (`ssas-se-2017` in the following example).
   + `Port` – The port that you use to access SSAS. The only supported port is 2383.
   + `VpcSecurityGroupMemberships` – Memberships for VPC security groups for your RDS DB instance.
   + `MAX_MEMORY` – The upper threshold above which SSAS should begin releasing memory more aggressively to make room for requests that are running, and also new high-priority requests. The number is a percentage of the total memory of the DB instance. The allowed values are 10–80, and the default is 45.
   + `MODE` – The SSAS server mode, either `Tabular` or `Multidimensional`. `Tabular` is the default.

     If you receive an error that the `MODE` option setting isn't valid, it means that Multidimensional mode isn't supported in your AWS Region. For more information, see [Limitations](Appendix.SQLServer.Options.SSAS.md#SSAS.Limitations).

   The following is an example of a JSON file with SSAS option settings.

   ```
   {
   "OptionGroupName": "{{ssas-se-2017}}",
   "OptionsToInclude": [
   	{
   	"OptionName": "SSAS",
   	"Port": 2383,
   	"VpcSecurityGroupMemberships": ["{{sg-0abcdef123}}"],
   	"OptionSettings": [{"Name":"MAX_MEMORY","Value":"{{60}}"},{"Name":"MODE","Value":"{{Multidimensional}}"}]
   	}],
   "ApplyImmediately": true
   }
   ```

1. Add the `SSAS` option to the option group.  
**Example**  

   For Linux, macOS, or Unix:

   ```
   aws rds add-option-to-option-group \
       --cli-input-json file://{{ssas-option.json}} \
       --apply-immediately
   ```

   For Windows:

   ```
   aws rds add-option-to-option-group ^
       --cli-input-json file://{{ssas-option.json}} ^
       --apply-immediately
   ```

## Associating the option group with your DB instance
<a name="SSAS.Apply"></a>

You can use the console or the CLI to associate the option group with your DB instance.

### Console
<a name="SSAS.Apply.Console"></a>

Associate your option group with a new or existing DB instance:
+ For a new DB instance, associate the option group with the DB instance when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).
+ For an existing DB instance, modify the instance and associate the new option group with it. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).
**Note**  
If you use an existing instance, it must already have an Active Directory domain and AWS Identity and Access Management (IAM) role associated with it. If you create a new instance, specify an existing Active Directory domain and IAM role. For more information, see [Working with Active Directory with RDS for SQL Server](User.SQLServer.ActiveDirectoryWindowsAuth.md).

### CLI
<a name="SSAS.Apply.CLI"></a>

You can associate your option group with a new or existing DB instance.

**Note**  
If you use an existing instance, it must already have an Active Directory domain and IAM role associated with it. If you create a new instance, specify an existing Active Directory domain and IAM role. For more information, see [Working with Active Directory with RDS for SQL Server](User.SQLServer.ActiveDirectoryWindowsAuth.md).

**To create a DB instance that uses the option group**
+ Specify the same DB engine type and major version that you used when creating the option group.  
**Example**  

  For Linux, macOS, or Unix:

  ```
  aws rds create-db-instance \
      --db-instance-identifier {{myssasinstance}} \
      --db-instance-class {{db.m5.2xlarge}} \
      --engine {{sqlserver-se}} \
      --engine-version {{14.00.3223.3.v1}} \
      --allocated-storage {{100}} \
      --manage-master-user-password \
      --master-username {{admin}} \
      --storage-type {{gp2}} \
      --license-model {{li}} \
      --domain-iam-role-name {{my-directory-iam-role}} \
      --domain {{my-domain-id}} \
      --option-group-name {{ssas-se-2017}}
  ```

  For Windows:

  ```
  aws rds create-db-instance ^
      --db-instance-identifier {{myssasinstance}} ^
      --db-instance-class {{db.m5.2xlarge}} ^
      --engine {{sqlserver-se}} ^
      --engine-version {{14.00.3223.3.v1}} ^
      --allocated-storage {{100}} ^
      --manage-master-user-password ^
      --master-username {{admin}} ^
      --storage-type {{gp2}} ^
      --license-model {{li}} ^
      --domain-iam-role-name {{my-directory-iam-role}} ^
      --domain {{my-domain-id}} ^
      --option-group-name {{ssas-se-2017}}
  ```

**To modify a DB instance to associate the option group**
+ Use one of the following commands.  
**Example**  

  For Linux, macOS, or Unix:

  ```
  aws rds modify-db-instance \
      --db-instance-identifier {{myssasinstance}} \
      --option-group-name {{ssas-se-2017}} \
      --apply-immediately
  ```

  For Windows:

  ```
  aws rds modify-db-instance ^
      --db-instance-identifier {{myssasinstance}} ^
      --option-group-name {{ssas-se-2017}} ^
      --apply-immediately
  ```

## Allowing inbound access to your VPC security group
<a name="SSAS.InboundRule"></a>

Create an inbound rule for the specified SSAS listener port in the VPC security group associated with your DB instance. For more information about setting up security groups, see [Provide access to your DB instance in your VPC by creating a security group](CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup).

## Enabling Amazon S3 integration
<a name="SSAS.EnableS3"></a>

To download model configuration files to your host for deployment, use Amazon S3 integration. For more information, see [Integrating an Amazon RDS for SQL Server DB instance with Amazon S3](User.SQLServer.Options.S3-integration.md). 