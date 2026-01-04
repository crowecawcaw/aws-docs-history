# Creating and connecting to a DB instance for

Amazon RDS Custom for SQL Server

You can create an RDS Custom DB instance, and then connect to it using AWS Systems Manager or Remote
Desktop Protocol (RDP).

###### Important

Before you can create or connect to an RDS Custom for SQL Server DB instance, make sure to complete the tasks in
[Setting up your environment for Amazon RDS Custom for SQL Server](custom-setup-sqlserver.md "custom-setup-sqlserver.md").

You can tag RDS Custom DB instances when you create them, but don't create or modify the `AWSRDSCustom` tag that's
required for RDS Custom automation. For more information, see [Tagging RDS Custom for SQL Server resources](custom-managing-sqlserver.md "custom-managing-sqlserver.md").

The first time that you create an RDS Custom for SQL Server DB instance, you might receive the
following error: **`The service-linked role is in the process of being created.
 Try again later.`** If you do, wait a few minutes and then try again to
create the DB instance.

###### Topics

- [Creating an RDS Custom for SQL Server DB instance](#custom-creating-sqlserver.create "#custom-creating-sqlserver.create")
- [RDS Custom service-linked role](custom-creating-sqlserver.md "custom-creating-sqlserver.md")
- [Connecting to your RDS Custom DB instance using AWS Systems Manager](custom-creating-sqlserver.md "custom-creating-sqlserver.md")
- [Connecting to your RDS Custom DB instance using RDP](custom-creating-sqlserver.md "custom-creating-sqlserver.md")

## Creating an RDS Custom for SQL Server DB instance

Create an Amazon RDS Custom for SQL Server DB instance using either the AWS Management Console or the AWS CLI. The procedure is similar to the procedure for
creating an Amazon RDS DB instance.

For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

###### To create an RDS Custom for SQL Server DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose **Create database**.
4. Choose **Standard create** for the database creation method.
5. For **Engine options**, choose **Microsoft
   SQL Server** for the engine type.
6. For **Database management type**, choose **Amazon RDS Custom**.
7. In the **Edition** section, choose the DB engine
   edition that you want to use.
8. (Optional) If you intend to create the DB instance from a CEV, check
   the **Use custom engine version (CEV)** check box.
   Select your CEV in the drop-down list.
9. For **Database version**, keep the default value version.
10. For **Templates**, choose
    **Production**.
11. In the **Settings** section, enter a unique name for
    the **DB instance identifier**.
12. To enter your master password, do the following:
    1. In the **Settings** section, open **Credential Settings**.
    2. Clear the **Auto generate a password** check box.
    3. Change the **Master username** value and enter the same password in **Master
       password** and **Confirm password**.By default, the new RDS Custom DB instance uses an automatically generated password for the master user.

13. In the **DB instance size** section, choose a value
    for **DB instance class**.

For supported classes, see [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.md "custom-reqs-limits.md"). 14. Choose **Storage** settings. 15. For **RDS Custom security**, do the following:

    1. For **IAM instance profile**, you have two options to choose the instance profile for your RDS Custom for SQL Server DB
     instance.




    	1. Choose **Create a new instance profile** and provide an instance profile name suffix.
    	 For more information, see [Automated instance profile creation using the AWS Management Console](custom-setup-sqlserver.md#custom-setup-sqlserver.instanceProfileCreation "custom-setup-sqlserver.md#custom-setup-sqlserver.instanceProfileCreation").
    	2. Choose an existing instance profile. From the ddropdown list,
    	 choose instance profile that begins with `AWSRDSCustom`.
    2. For **Encryption**, choose **Enter a key ARN** to list the available
     AWS KMS keys. Then choose your key from the list.


    An AWS KMS key is required for RDS Custom. For more information, see [Make sure that you have a symmetric encryption AWS KMS key](custom-setup-sqlserver.md#custom-setup-sqlserver.cmk "custom-setup-sqlserver.md#custom-setup-sqlserver.cmk").

16. For the remaining sections, specify your preferred RDS Custom DB instance settings. For information about each
    setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
    The following settings don't appear in the console and aren't supported:

        * **Processor features**
        * **Storage autoscaling**
        * **Availability & durability**
        * **Password and Kerberos authentication** option in **Database
         authentication** (only **Password authentication** is supported)
        * **Database options** group in **Additional configuration**
        * **Performance Insights**
        * **Log exports**
        * **Enable auto minor version upgrade**
        * **Deletion protection**

    **Backup retention period** is supported, but you can't choose **0
    days**.

17. Choose **Create database**.

The **View credential details** button appears on the **Databases**
page.

To view the master user name and password for the RDS Custom DB instance, choose **View credential
details**.

To connect to the DB instance as the master user, use the user name and password that appear.

###### Important

You can't view the master user password again. If you
don't record it, you might have to change it. To change the
master user password after the RDS Custom DB instance is available,
modify the DB instance. For more information about modifying a DB
instance, see [Managing an Amazon RDS Custom for SQL Server DB instance](custom-managing-sqlserver.md "custom-managing-sqlserver.md"). 18. Choose **Databases** to view the list of RDS Custom DB instances. 19. Choose the RDS Custom DB instance that you just created.

On the RDS console, the details for the new RDS Custom DB instance appear:

    * The DB instance has a status of **creating** until the RDS Custom DB instance is created
     and ready for use. When the state changes to **available**, you can connect to the DB
     instance. Depending on the instance class and storage allocated, it can take several minutes for the new
     DB instance to be available.
    * **Role** has the value **Instance (RDS Custom)**.
    * **RDS Custom automation mode** has the value **Full automation**. This
     setting means that the DB instance provides automatic monitoring and instance recovery.

You create an RDS Custom DB instance by using the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") AWS CLI command.

The following options are required:

- `--db-instance-identifier`
- `--db-instance-class` (for a list of supported instance
  classes, see [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.md "custom-reqs-limits.md"))
- `--engine` (`custom-sqlserver-ee`, `custom-sqlserver-se`, or
  `custom-sqlserver-web`)
- `--kms-key-id`
- `--custom-iam-instance-profile`
  The following example creates an RDS Custom for SQL Server DB instance named
  `my-custom-instance`. The backup retention period is 3
  days.

###### Note

To create a DB instance from a custom engine version (CEV), supply an existing CEV name
to the `--engine-version` parameter.
For example, `--engine-version 15.00.4249.2.my_cevtest`

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --engine `custom-sqlserver-ee` \
    --engine-version `15.00.4073.23.v1` \
    --db-instance-identifier `my-custom-instance` \
    --db-instance-class `db.m5.xlarge` \
    --allocated-storage `20` \
    --db-subnet-group `mydbsubnetgroup` \
    --master-username `myuser` \
    --master-user-password `mypassword` \
    --backup-retention-period `3` \
    --no-multi-az \
    --port `8200` \
    --kms-key-id `mykmskey` \
    --custom-iam-instance-profile `AWSRDSCustomInstanceProfileForRdsCustomInstance`
```

For Windows:

```
aws rds create-db-instance ^
    --engine `custom-sqlserver-ee` ^
    --engine-version `15.00.4073.23.v1` ^
    --db-instance-identifier `my-custom-instance` ^
    --db-instance-class `db.m5.xlarge` ^
    --allocated-storage `20` ^
    --db-subnet-group `mydbsubnetgroup` ^
    --master-username `myuser` ^
    --master-user-password `mypassword` ^
    --backup-retention-period `3` ^
    --no-multi-az ^
    --port `8200` ^
    --kms-key-id `mykmskey` ^
    --custom-iam-instance-profile `AWSRDSCustomInstanceProfileForRdsCustomInstance`
```

###### Note

Specify a password other than the prompt shown here as a security best practice.

Get details about your instance by using the `describe-db-instances` command.

```
aws rds describe-db-instances --db-instance-identifier my-custom-instance
```

The following partial output shows the engine, parameter groups, and other information.

```
{
    "DBInstances": [
        {
            "PendingModifiedValues": {},
            "Engine": "custom-sqlserver-ee",
            "MultiAZ": false,
            "DBSecurityGroups": [],
            "DBParameterGroups": [
                {
                    "DBParameterGroupName": "default.custom-sqlserver-ee-15",
                    "ParameterApplyStatus": "in-sync"
                }
            ],
            "AutomationMode": "full",
            "DBInstanceIdentifier": "my-custom-instance",
            "TagList": []
        }
    ]
}
```
