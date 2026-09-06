

# Creating and connecting to a DB instance for Amazon RDS Custom for SQL Server
<a name="custom-creating-sqlserver"></a>

You can create an RDS Custom DB instance, and then connect to it using AWS Systems Manager or Remote Desktop Protocol (RDP).

**Important**  
Before you can create or connect to an RDS Custom for SQL Server DB instance, make sure to complete the tasks in [Setting up your environment for Amazon RDS Custom for SQL Server](custom-setup-sqlserver.md).  
You can tag RDS Custom DB instances when you create them, but don't create or modify the `AWSRDSCustom` tag that's required for RDS Custom automation. For more information, see [Tagging RDS Custom for SQL Server resources](custom-managing-sqlserver.tagging.md).  
The first time that you create an RDS Custom for SQL Server DB instance, you might receive the following error: The service-linked role is in the process of being created. Try again later. If you do, wait a few minutes and then try again to create the DB instance.

**Topics**
+ [Creating an RDS Custom for SQL Server DB instance](#custom-creating-sqlserver.create)
+ [RDS Custom service-linked role](custom-creating-sqlserver.slr.md)
+ [Connecting to your RDS Custom DB instance using AWS Systems Manager](custom-creating-sqlserver.ssm.md)
+ [Connecting to your RDS Custom DB instance using RDP](custom-creating-sqlserver.rdp.md)

## Creating an RDS Custom for SQL Server DB instance
<a name="custom-creating-sqlserver.create"></a>

Create an Amazon RDS Custom for SQL Server DB instance using either the AWS Management Console or the AWS CLI. The procedure is similar to the procedure for creating an Amazon RDS DB instance.

For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).

### Console
<a name="custom-creating-sqlserver.CON"></a>

**To create an RDS Custom for SQL Server DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose **Create database**.

1. Choose **Standard create** for the database creation method.

1. For **Engine options**, choose **Microsoft SQL Server** for the engine type.

1. For **Database management type**, choose **Amazon RDS Custom**.

1. In the **Edition** section, choose the DB engine edition that you want to use.

1. (Optional) If you intend to create the DB instance from a CEV, check the **Use custom engine version (CEV)** check box. Select your CEV in the drop-down list.

1. For **Database version**, keep the default value version.

1. For **Templates**, choose **Production**.

1. In the **Settings** section, enter a unique name for the **DB instance identifier**.

1. To enter your master password, do the following:

   1. In the **Settings** section, open **Credential Settings**.

   1. Clear the **Auto generate a password** check box.

   1. Change the **Master username** value and enter the same password in **Master password** and **Confirm password**.

   By default, the new RDS Custom DB instance uses an automatically generated password for the master user.

1. In the **DB instance size** section, choose a value for **DB instance class**.

   For supported classes, see [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.instancesMS.md).

1. Choose **Storage** settings.

1. For **RDS Custom security**, do the following:

   1. For **IAM instance profile**, you have two options to choose the instance profile for your RDS Custom for SQL Server DB instance.

      1. Choose **Create a new instance profile** and provide an instance profile name suffix. For more information, see [Automated instance profile creation using the AWS Management Console](custom-setup-sqlserver.md#custom-setup-sqlserver.instanceProfileCreation).

      1. Choose an existing instance profile. From the ddropdown list, choose instance profile that begins with `AWSRDSCustom`.

   1. For **Encryption**, choose **Enter a key ARN** to list the available AWS KMS keys. Then choose your key from the list. 

      An AWS KMS key is required for RDS Custom. For more information, see [Make sure that you have a symmetric encryption AWS KMS key](custom-setup-sqlserver.md#custom-setup-sqlserver.cmk).

1. For the remaining sections, specify your preferred RDS Custom DB instance settings. For information about each setting, see [Settings for DB instances](USER_CreateDBInstance.Settings.md). The following settings don't appear in the console and aren't supported:
   + **Processor features**
   + **Storage autoscaling**
   + **Availability & durability**
   + **Password and Kerberos authentication** option in **Database authentication** (only **Password authentication** is supported)
   + **Database options** group in **Additional configuration**
   + **Performance Insights**
   + **Log exports**
   + **Enable auto minor version upgrade**
   + **Deletion protection**

   **Backup retention period** is supported, but you can't choose **0 days**.

1. Choose **Create database**. 

   The **View credential details** button appears on the **Databases** page. 

   To view the master user name and password for the RDS Custom DB instance, choose **View credential details**.

   To connect to the DB instance as the master user, use the user name and password that appear.
**Important**  
You can't view the master user password again. If you don't record it, you might have to change it. To change the master user password after the RDS Custom DB instance is available, modify the DB instance. For more information about modifying a DB instance, see [Managing an Amazon RDS Custom for SQL Server DB instance](custom-managing-sqlserver.md).

1. Choose **Databases** to view the list of RDS Custom DB instances.

1. Choose the RDS Custom DB instance that you just created.

   On the RDS console, the details for the new RDS Custom DB instance appear:
   + The DB instance has a status of **creating** until the RDS Custom DB instance is created and ready for use. When the state changes to **available**, you can connect to the DB instance. Depending on the instance class and storage allocated, it can take several minutes for the new DB instance to be available.
   + **Role** has the value **Instance (RDS Custom)**.
   + **RDS Custom automation mode** has the value **Full automation**. This setting means that the DB instance provides automatic monitoring and instance recovery.

### AWS CLI
<a name="custom-creating-sqlserver.CLI"></a>

You create an RDS Custom DB instance by using the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI command.

The following options are required:
+ `--db-instance-identifier`
+ `--db-instance-class` (for a list of supported instance classes, see [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.instancesMS.md))
+ `--engine` (`custom-sqlserver-ee`, `custom-sqlserver-se`, or `custom-sqlserver-web`)
+ `--kms-key-id`
+ `--custom-iam-instance-profile`

The following example creates an RDS Custom for SQL Server DB instance named `my-custom-instance`. The backup retention period is 3 days.

**Note**  
To create a DB instance from a custom engine version (CEV), supply an existing CEV name to the `--engine-version` parameter. For example, `--engine-version 15.00.4249.2.my_cevtest`

**Example**  
For Linux, macOS, or Unix:  

```
 1. aws rds create-db-instance \
 2.     --engine {{custom-sqlserver-ee}} \
 3.     --engine-version {{15.00.4073.23.v1}} \
 4.     --db-instance-identifier {{my-custom-instance}} \
 5.     --db-instance-class {{db.m5.xlarge}} \
 6.     --allocated-storage {{20}} \
 7.     --db-subnet-group {{mydbsubnetgroup}} \
 8.     --master-username {{myuser}} \
 9.     --master-user-password {{mypassword}} \
10.     --backup-retention-period {{3}} \
11.     --no-multi-az \
12.     --port {{8200}} \
13.     --kms-key-id {{mykmskey}} \
14.     --custom-iam-instance-profile {{AWSRDSCustomInstanceProfileForRdsCustomInstance}}
```
For Windows:  

```
 1. aws rds create-db-instance ^
 2.     --engine {{custom-sqlserver-ee}} ^
 3.     --engine-version {{15.00.4073.23.v1}} ^
 4.     --db-instance-identifier {{my-custom-instance}} ^
 5.     --db-instance-class {{db.m5.xlarge}} ^
 6.     --allocated-storage {{20}} ^
 7.     --db-subnet-group {{mydbsubnetgroup}} ^
 8.     --master-username {{myuser}} ^
 9.     --master-user-password {{mypassword}} ^
10.     --backup-retention-period {{3}} ^
11.     --no-multi-az ^
12.     --port {{8200}} ^
13.     --kms-key-id {{mykmskey}} ^
14.     --custom-iam-instance-profile {{AWSRDSCustomInstanceProfileForRdsCustomInstance}}
```
Specify a password other than the prompt shown here as a security best practice.

Get details about your instance by using the `describe-db-instances` command.

```
1. aws rds describe-db-instances --db-instance-identifier my-custom-instance
```

The following partial output shows the engine, parameter groups, and other information.

```
 1. {
 2.     "DBInstances": [
 3.         {
 4.             "PendingModifiedValues": {},
 5.             "Engine": "custom-sqlserver-ee",
 6.             "MultiAZ": false,
 7.             "DBSecurityGroups": [],
 8.             "DBParameterGroups": [
 9.                 {
10.                     "DBParameterGroupName": "default.custom-sqlserver-ee-15",
11.                     "ParameterApplyStatus": "in-sync"
12.                 }
13.             ],
14.             "AutomationMode": "full",
15.             "DBInstanceIdentifier": "my-custom-instance",
16.             "TagList": []
17.         }
18.     ]
19. }
```