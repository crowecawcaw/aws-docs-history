# Activating linked servers with Teradata

Activate linked servers with Teradata by adding the `ODBC_TERADATA` option to your
RDS for SQL Server DB instance. Use the following process:

###### Topics

- [Creating the option group for ODBC_TERADATA](#USER_SQLServerTeradata.Activate.CreateOG "#USER_SQLServerTeradata.Activate.CreateOG")
- [Adding the ODBC_TERADATA option to the option group](#USER_SQLServerTeradata.Activate.AddOG "#USER_SQLServerTeradata.Activate.AddOG")
- [Associating the ODBC_TERADATA option with your DB instance](#USER_SQLServerTeradata.Activate.AssociateOG "#USER_SQLServerTeradata.Activate.AssociateOG")

## Creating the option group for `ODBC_TERADATA`

To work with linked servers with Teradata, create an option group or modify an option group that corresponds to the SQL Server eddition and
version of the DB instance that you plan to use. To complete this procedure, use the AWS Management Console or the AWS CLI.

Use the following procedure to create an option group for SQL Server Standard Edition 2019.

###### To create the option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose **Create group**.
4. In the **Create option group** window, do the following:
   1. For **Name**, enter a name for the option group that is unique within your AWS account,
      such as `teradata-odbc-se-2019`.
      The name can contain only letters, digits, and hyphens.
   2. For **Description**, enter a brief description of the option group.
   3. For **Engine**, choose **sqlserver-se**.
   4. For **Major engine version**, choose **15.00**.

5. Choose **Create**.

The following procedure creates an option group for SQL Server Standard Edition 2019.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-option-group \
    --option-group-name `teradata-odbc-se-2019` \
    --engine-name sqlserver-se \
    --major-engine-version 15.00 \
    --option-group-description "`ODBC_TERADATA option group for SQL Server SE 2019`"
```

###### Example

For Windows:

```
aws rds create-option-group ^
    --option-group-name `teradata-odbc-se-2019` ^
    --engine-name sqlserver-se ^
    --major-engine-version 15.00 ^
    --option-group-description "`ODBC_TERADATA option group for SQL Server SE 2019`"
```

## Adding the `ODBC_TERADATA` option to the option group

Next, use the AWS Management Console or the AWS CLI to add the `ODBC_Teradata` option to your option group.

Use the following procedure creates an option group for SQL Server Standard Edition 2019.

###### To add the `ODBC_TERADATA` option

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose your new option group.
4. Choose **Add option**.
5. Under **Option details**:
   1. Choose **ODBC_TERADATA** for **Option name**.
   2. For `17.20.33.00` for **Option version**.

6. Under scheduling, choose whether to add the option immediately or at the next maintenance window.
7. Choose **Add option**.

The following procedure adds the `ODBC_TERADATA` option to your option group.

###### Example

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name `teradata-odbc-se-2019` \
    --options "OptionName=ODBC_TERADATA,OptionVersion=17.20.33.00" \
    --apply-immediately
```

###### Example

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name `teradata-odbc-se-2019` ^
    --options "OptionName=ODBC_TERADATA,OptionVersion=17.20.33.00" ^
    --apply-immediately
```

## Associating the `ODBC_TERADATA` option with your DB instance

To associate the `ODBC_TERADATA` option group with your DB instance, use the AWS Management Console or AWS CLI.

To finish activating linked servers for Teradata, associate your option group with a new or existing DB instance:

- For a new DB instance, associate it when you launch the instance. For more information, see
  [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, associate it by modifying the instance. For more information, see
  [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

Specify the same DB engine type and major version that you used when creating the option group.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mytestsqlserverteradataodbcinstance` \
    --db-instance-class db.m5.2xlarge \
    --engine sqlserver-se \
    --engine-version 15.00 \
    --license-model license-included \
    --allocated-storage 100 \
    --master-username admin \
    --master-user-password password \
    --storage-type gp2 \
    --option-group-name teradata-odbc-se-2019
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mytestsqlserverteradataodbcinstance` ^
    --db-instance-class db.m5.2xlarge ^
    --engine sqlserver-se ^
    --engine-version 15.00 ^
    --license-model license-included ^
    --allocated-storage 100 ^
    --master-username admin ^
    --master-user-password password ^
    --storage-type gp2 ^
    --option-group-name teradata-odbc-se-2019
```

To modify an instance and associate the new option group:

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mytestsqlserverteradataodbcinstance` \
    --option-group-name teradata-odbc-se-2019 \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mytestsqlserverteradataodbcinstance` ^
    --option-group-name teradata-odbc-se-2019 ^
    --apply-immediately
```
