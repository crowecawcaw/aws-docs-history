# Enabling Microsoft SQL Server resource governor for your RDS for SQL Server instance

Enable resource governor by adding the `RESOURCE_GOVERNOR` option to your RDS for SQL Server DB instance.
Use the following process:

1. Create a new option group, or choose an existing option group.
2. Add the `RESOURCE_GOVERNOR` option to the option group.
3. Associate the option group with the DB instance.

###### Note

Enabling resource governor through an option group doesn't require a reboot.

## Creating the option group for `RESOURCE_GOVERNOR`

To enable resource governor, create an option group or modify an option group that corresponds
to the SQL Server edition and version of the DB instance that you plan to use.
To complete this procedure, use the AWS Management Console or the AWS CLI.

Use the following procedure to create an option group for SQL Server Enterprise Edition 2022.

###### To create the option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose **Create group**.
4. In the **Create option group** window, do the following:
   1. For **Name**, enter a name for the option group that is unique within your AWS account,
      such as `resource-governor-ee-2022`. The name can contain only letters, digits, and hyphens.
   2. For **Description**, enter a brief description of the option group,
      such as `RESOURCE_GOVERNOR option group for SQL Server EE 2022`.
      The description is used for display purposes.
   3. For **Engine**, choose **sqlserver-ee**.
   4. For **Major engine version**, choose **16.00**.

5. Choose **Create**.
   The following procedure creates an option group for SQL Server Enterprise Edition 2022.

###### To create the option group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds create-option-group \
    --option-group-name `resource-governor-ee-2022` \
    --engine-name `sqlserver-ee` \
    --major-engine-version `16.00` \
    --option-group-description "`RESOURCE_GOVERNOR option group for SQL Server EE 2022`"
```

For Windows:

```
aws rds create-option-group ^
    --option-group-name `resource-governor-ee-2022` ^
    --engine-name `sqlserver-ee` ^
    --major-engine-version `16.00` ^
    --option-group-description "`RESOURCE_GOVERNOR option group for SQL Server EE 2022`"
```

## Adding the `RESOURCE_GOVERNOR` option to the option group

Next, use the AWS Management Console or the AWS CLI to add the `RESOURCE_GOVERNOR` option to your option group.

###### To add the RESOURCE_GOVERNOR option

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group that you just created, **resource-governor-ee-2022** in this example.
4. Choose **Add option**.
5. Under **Option details**, choose **RESOURCE_GOVERNOR** for **Option name**.
6. Under **Scheduling**, choose whether to add the option immediately or at the next maintenance window.
7. Choose **Add option**.

###### To add the `RESOURCE_GOVERNOR` option

- Add the `RESOURCE_GOVERNOR` option to the option group.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name `resource-governor-ee-2022` \
    --options "OptionName=RESOURCE_GOVERNOR" \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name `resource-governor-ee-2022` ^
    --options "OptionName=RESOURCE_GOVERNOR" ^
    --apply-immediately
```

## Associating the option group with your DB instance

To associate the `RESOURCE_GOVERNOR` option group with your DB instance, use the AWS Management Console or the AWS CLI.

To finish activating resource governor, associate your `RESOURCE_GOVERNOR` option group with a new or existing DB instance:

- For a new DB instance, associate them when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, associate them by modifying the instance. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
  You can associate the `RESOURCE_GOVERNOR` option group with a new or existing DB instance.

###### To create an instance with the `RESOURCE_GOVERNOR` option group

- Specify the same DB engine type and major version that you used when creating the option group.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mytestsqlserverresourcegovernorinstance` \
    --db-instance-class `db.m5.2xlarge` \
    --engine `sqlserver-ee` \
    --engine-version `16.00` \
    --license-model `license-included` \
    --allocated-storage `100` \
    --master-username `admin` \
    --master-user-password `password` \
    --storage-type `gp2` \
    --option-group-name `resource-governor-ee-2022`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mytestsqlserverresourcegovernorinstance` ^
    --db-instance-class `db.m5.2xlarge` ^
    --engine `sqlserver-ee` ^
    --engine-version `16.00` ^
    --license-model `license-included` ^
    --allocated-storage `100` ^
    --master-username `admin` ^
    --master-user-password `password` ^
    --storage-type `gp2` ^
    --option-group-name `resource-governor-ee-2022`
```

###### To modify an instance and associate the `RESOURCE_GOVERNOR` option group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mytestinstance` \
    --option-group-name `resource-governor-ee-2022` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mytestinstance` ^
    --option-group-name `resource-governor-ee-2022` ^
    --apply-immediately
```
