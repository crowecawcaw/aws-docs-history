# Enabling Database Mail

Use the following process to enable Database Mail for your DB instance:

1. Create a new parameter group.
2. Modify the parameter group to set the `database mail xps` parameter to 1.
3. Associate the parameter group with the DB instance.

## Creating the parameter group for Database Mail

Create a parameter group for the `database mail xps` parameter that corresponds to the SQL Server edition and
version of your DB instance.

###### Note

You can also modify an existing parameter group. Follow the procedure in [Modifying the parameter that enables
Database Mail](#DBMail.ModifyParamGroup "#DBMail.ModifyParamGroup").

The following example creates a parameter group for SQL Server Standard Edition 2016.

###### To create the parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose **Create parameter group**.
4. In the **Create parameter group** pane, do the following:
   1. For **Parameter group family**, choose
      **sqlserver-se-13.0**.
   2. For **Group name**, enter an identifier for the parameter group, such as
      `dbmail-sqlserver-se-13`.
   3. For **Description**, enter `Database Mail XPs`.

5. Choose **Create**.
   The following example creates a parameter group for SQL Server Standard Edition 2016.

###### To create the parameter group

- Use one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
    --db-parameter-group-name `dbmail-sqlserver-se-13` \
    --db-parameter-group-family "`sqlserver-se-13.0`" \
    --description "`Database Mail XPs`"
```

For Windows:

```
aws rds create-db-parameter-group ^
    --db-parameter-group-name `dbmail-sqlserver-se-13` ^
    --db-parameter-group-family "`sqlserver-se-13.0`" ^
    --description "`Database Mail XPs`"
```

## Modifying the parameter that enables

Database Mail

Modify the `database mail xps` parameter in the parameter group that corresponds to the SQL Server edition and
version of your DB instance.

To enable Database Mail, set the `database mail xps` parameter to 1.

The following example modifies the parameter group that you created for SQL Server Standard Edition 2016.

###### To modify the parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose the parameter group, such as **dbmail-sqlserver-se-13**.
4. Under **Parameters**, filter the parameter list for `mail`.
5. Choose **database mail xps**.
6. Choose **Edit parameters**.
7. Enter `1`.
8. Choose **Save changes**.
   The following example modifies the parameter group that you created for SQL Server Standard Edition 2016.

###### To modify the parameter group

- Use one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name `dbmail-sqlserver-se-13` \
    --parameters "ParameterName='database mail xps',ParameterValue=`1`,ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-parameter-group ^
    --db-parameter-group-name `dbmail-sqlserver-se-13` ^
    --parameters "ParameterName='database mail xps',ParameterValue=`1`,ApplyMethod=immediate"
```

## Associating the parameter group with the DB instance

You can use the AWS Management Console or the AWS CLI to associate the Database Mail parameter group with the DB instance.

You can associate the Database Mail parameter group with a new or existing DB instance.

- For a new DB instance, associate it when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, associate it by modifying the instance. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
  You can associate the Database Mail parameter group with a new or existing DB instance.

###### To create a DB instance with the Database Mail parameter group

- Specify the same DB engine type and major version as you used when creating the parameter group.

###### Example

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
    --license-model `li`
    --db-parameter-group-name `dbmail-sqlserver-se-13`
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
    --db-parameter-group-name `dbmail-sqlserver-se-13`
```

###### To modify a DB instance and associate the Database Mail parameter group

- Use one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --db-parameter-group-name `dbmail-sqlserver-se-13` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --db-parameter-group-name `dbmail-sqlserver-se-13` ^
    --apply-immediately
```
