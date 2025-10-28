# Enabling MSDTC

Use the following process to enable MSDTC for your DB instance:

1. Create a new option group, or choose an existing option group.
2. Add the `MSDTC` option to the option group.
3. Create a new parameter group, or choose an existing parameter group.
4. Modify the parameter group to set the `in-doubt xact resolution` parameter to 1 or 2.
5. Associate the option group and parameter group with the DB instance.

## Creating the option group for MSDTC

Use the AWS Management Console or the AWS CLI to create an option group that corresponds to the SQL
Server engine and version of your DB instance.

###### Note

You can also use an existing option group if it's for the correct SQL Server engine
and version.

The following procedure creates an option group for SQL Server Standard Edition 2016.

###### To create the option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose **Create group**.
4. In the **Create option group** pane, do the following:
   1. For **Name**, enter a name for the option group that is unique
      within your AWS account, such as
      `msdtc-se-2016`. The name can
      contain only letters, digits, and hyphens.
   2. For **Description**, enter a brief description of the option group,
      such as `MSDTC option group for SQL Server SE
2016`. The description is used for
      display purposes.
   3. For **Engine**, choose **sqlserver-se**.
   4. For **Major engine version**, choose
      **13.00**.

5. Choose **Create**.
   The following example creates an option group for SQL Server Standard Edition
6.

###### To create the option group

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds create-option-group \
    --option-group-name `msdtc-se-2016` \
    --engine-name `sqlserver-se` \
    --major-engine-version `13.00` \
    --option-group-description "`MSDTC option group for SQL Server SE 2016`"
```

For Windows:

```
aws rds create-option-group ^
    --option-group-name `msdtc-se-2016` ^
    --engine-name `sqlserver-se` ^
    --major-engine-version `13.00` ^
    --option-group-description "`MSDTC option group for SQL Server SE 2016`"
```

## Adding the MSDTC option to the option group

Next, use the AWS Management Console or the AWS CLI to add the `MSDTC` option to the option
group.

The following option settings are required:

- **Port** – The port that you use to access MSDTC. Allowed values
  are 1150–49151 except for 1234, 1434, 3260, 3343, 3389, and

47001.  The default value is 5000.

Make sure that the port you want to use is enabled in your firewall rules. Also, make
sure as needed that this port is enabled in the inbound and outbound
rules for the security group associated with your DB instance. For more
information, see [Can't connect to Amazon RDS DB instance](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Connecting").

- **Security groups** – The VPC security group memberships
  for your RDS DB instance.
- **Authentication type** – The authentication mode between hosts.
  The following authentication types are supported:
  - Mutual – The RDS instances are mutually authenticated to each other using
    integrated authentication. If this option is selected, all
    instances associated with this option group must be
    domain-joined.
  - None – No authentication is performed between hosts. We don't recommend using
    this mode in production environments.

- **Transaction log size** – The size of the MSDTC transaction
  log. Allowed values are 4–1024 MB. The default size is 4
  MB.

The following option settings are optional:

- **Enable inbound connections** – Whether to allow inbound MSDTC
  connections to instances associated with this option group.
- **Enable outbound connections** – Whether to allow outbound
  MSDTC connections from instances associated with this option
  group.
- **Enable XA** – Whether to allow XA transactions. For more
  information on the XA protocol, see [XA
  specification](https://publications.opengroup.org/c193 "https://publications.opengroup.org/c193").
- **Enable SNA LU** – Whether to allow the SNA LU protocol to be
  used for distributed transactions. For more information on SNA LU
  protocol support, see [Managing IBM CICS LU 6.2 transactions](<https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms685136(v=vs.85)> "https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms685136(v=vs.85)") in the Microsoft documentation.

###### To add the MSDTC option

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group that you just created.
4. Choose **Add option**.
5. Under **Option details**, choose **MSDTC** for **Option name**.
6. Under **Option settings**:
   1. For **Port**, enter the port number for accessing MSDTC. The default
      is **5000**.
   2. For **Security groups**, choose the VPC security group to associate with the option.
   3. For **Authentication type**, choose **Mutual** or **None**.
   4. For **Transaction log size**, enter a value from 4–1024. The default is **4**.

7. Under **Additional configuration**, do the following:
   1. For **Connections**, as needed choose **Enable inbound
      connections** and **Enable outbound
      connections**.
   2. For **Allowed protocols**, as needed choose **Enable
      XA** and **Enable SNA
      LU**.

8. Under **Scheduling**, choose whether to add the option immediately or at the next maintenance window.
9. Choose **Add option**.

To add this option, no reboot is required.

###### To add the MSDTC option

1. Create a JSON file, for example `msdtc-option.json`, with the following
   required parameters.

```
{
"OptionGroupName":"`msdtc-se-2016`",
"OptionsToInclude": [
	{
	"OptionName":"MSDTC",
	"Port":`5000`,
	"VpcSecurityGroupMemberships":["`sg-0abcdef123`"],
	"OptionSettings":[{"Name":"AUTHENTICATION","Value":"`MUTUAL`"},{"Name":"TRANSACTION_LOG_SIZE","Value":"`4`"}]
	}],
"ApplyImmediately": true
}
```

2. Add the `MSDTC` option to the option group.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --cli-input-json file://`msdtc-option.json` \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --cli-input-json file://`msdtc-option.json` ^
    --apply-immediately
```

No reboot is required.

## Creating the parameter group for MSDTC

Create or modify a parameter group for the `in-doubt xact resolution` parameter
that corresponds to the SQL Server edition and version of your DB
instance.

The following example creates a parameter group for SQL Server Standard Edition 2016.

###### To create the parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose **Create parameter group**.
4. In the **Create parameter group** pane, do the following:
   1. For **Parameter group family**, choose
      **sqlserver-se-13.0**.
   2. For **Group name**, enter an identifier for the parameter group,
      such as `msdtc-sqlserver-se-13`.
   3. For **Description**, enter `in-doubt xact
resolution`.

5. Choose **Create**.
   The following example creates a parameter group for SQL Server Standard Edition
6.

###### To create the parameter group

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
    --db-parameter-group-name `msdtc-sqlserver-se-13` \
    --db-parameter-group-family "`sqlserver-se-13.0`" \
    --description "`in-doubt xact resolution`"
```

For Windows:

```
aws rds create-db-parameter-group ^
    --db-parameter-group-name `msdtc-sqlserver-se-13` ^
    --db-parameter-group-family "`sqlserver-se-13.0`" ^
    --description "`in-doubt xact resolution`"
```

## Modifying the parameter for MSDTC

Modify the `in-doubt xact resolution` parameter in the parameter group that
corresponds to the SQL Server edition and version of your DB instance.

For MSDTC, set the `in-doubt xact resolution` parameter to one of the
following:

- `1` – `Presume commit`. Any MSDTC in-doubt transactions are
  presumed to have committed.
- `2` – `Presume abort`. Any MSDTC in-doubt transactions are
  presumed to have stopped.

For more information, see [in-doubt xact resolution server configuration option](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/in-doubt-xact-resolution-server-configuration-option "https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/in-doubt-xact-resolution-server-configuration-option") in the
Microsoft documentation.

The following example modifies the parameter group that you created for SQL Server
Standard Edition 2016.

###### To modify the parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose the parameter group, such as **msdtc-sqlserver-se-13**.
4. Under **Parameters**, filter the parameter list for `xact`.
5. Choose **in-doubt xact resolution**.
6. Choose **Edit parameters**.
7. Enter `1` or `2`.
8. Choose **Save changes**.
   The following example modifies the parameter group that you created for SQL Server
   Standard Edition 2016.

###### To modify the parameter group

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name `msdtc-sqlserver-se-13` \
    --parameters "ParameterName='in-doubt xact resolution',ParameterValue=`1`,ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-parameter-group ^
    --db-parameter-group-name `msdtc-sqlserver-se-13` ^
    --parameters "ParameterName='in-doubt xact resolution',ParameterValue=`1`,ApplyMethod=immediate"
```

## Associating the option group and parameter group with the DB instance

You can use the AWS Management Console or the AWS CLI to associate the MSDTC option group and parameter
group with the DB instance.

You can associate the MSDTC option group and parameter group with a new or existing DB
instance.

- For a new DB instance, associate them when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, associate them by modifying the instance. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

###### Note

If you use an domain-joined existing DB instance, it must already have an Active
Directory domain and AWS Identity and Access Management (IAM) role associated with
it. If you create a new domain-joined instance, specify an
existing Active Directory domain and IAM role. For more
information, see [Working with AWS Managed Active Directory with RDS for SQL Server](USER_SQLServerWinAuth.md "USER_SQLServerWinAuth.md").
You can associate the MSDTC option group and parameter group with a new or existing DB
instance.

###### Note

If you use an existing domain-joined DB instance, it must already have an Active
Directory domain and IAM role associated with it. If you create a
new domain-joined instance, specify an existing Active Directory
domain and IAM role. For more information, see [Working with AWS Managed Active Directory with RDS for SQL Server](USER_SQLServerWinAuth.md "USER_SQLServerWinAuth.md").

###### To create a DB instance with the MSDTC option group and parameter group

- Specify the same DB engine type and major version as you used when creating the option group.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mydbinstance` \
    --db-instance-class `db.m5.2xlarge` \
    --engine `sqlserver-se` \
    --engine-version `13.00.5426.0.v1` \
    --allocated-storage `100` \
    --manage-master-user-password \
    --master-username `admin` \
    --storage-type `gp2` \
    --license-model `li` \
    --domain-iam-role-name `my-directory-iam-role` \
    --domain `my-domain-id` \
    --option-group-name `msdtc-se-2016` \
    --db-parameter-group-name `msdtc-sqlserver-se-13`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --db-instance-class `db.m5.2xlarge` ^
    --engine `sqlserver-se` ^
    --engine-version `13.00.5426.0.v1` ^
    --allocated-storage `100` ^
    --manage-master-user-password ^
    --master-username `admin` ^
    --storage-type `gp2` ^
    --license-model `li` ^
    --domain-iam-role-name `my-directory-iam-role` ^
    --domain `my-domain-id` ^
    --option-group-name `msdtc-se-2016` ^
    --db-parameter-group-name `msdtc-sqlserver-se-13`
```

###### To modify a DB instance and associate the MSDTC option group and parameter group

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --option-group-name `msdtc-se-2016` \
    --db-parameter-group-name `msdtc-sqlserver-se-13` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --option-group-name `msdtc-se-2016` ^
    --db-parameter-group-name `msdtc-sqlserver-se-13` ^
    --apply-immediately
```

## Modifying the MSDTC option

After you enable the `MSDTC` option, you can modify its settings. For
information about how to modify option settings, see [Modifying an option setting](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.ModifyOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.ModifyOption").

###### Note

Some changes to MSDTC option settings require the MSDTC service to be restarted. This
requirement can affect running distributed transactions.
