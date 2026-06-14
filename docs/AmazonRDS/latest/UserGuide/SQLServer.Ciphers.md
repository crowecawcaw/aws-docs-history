# Configuring SQL Server security protocols and ciphers

You can turn certain security protocols and ciphers on and off using DB parameters. The security parameters that you can configure
(except for TLS version 1.2) are shown in the following table.

| DB parameter                          | Allowed values (default in bold)    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| rds.tls10                             | **default**, enabled, disabled      | TLS 1.0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| rds.tls11                             | **default**, enabled, disabled      | TLS 1.1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| rds.tls12                             | **default**                         | TLS 1.2. You can't modify this value.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| rds.fips                              | **0**, 1                            | When you set the parameter to 1, RDS forces the use of modules that are compliant with the Federal Information<br>Processing Standard (FIPS) 140-2 standard.<br>For more information, see [Use SQL<br>Server 2016 in FIPS 140-2-compliant mode](https://docs.microsoft.com/en-us/troubleshoot/sql/security/sql-2016-fips-140-2-compliant-mode "https://docs.microsoft.com/en-us/troubleshoot/sql/security/sql-2016-fips-140-2-compliant-mode") in the Microsoft documentation. |
| rds.rc4                               | **default**, enabled, disabled      | RC4 stream cipher.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| rds.diffie-hellman                    | **default**, enabled, disabled      | Diffie-Hellman key-exchange encryption.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| rds.diffie-hellman-min-key-bit-length | **default**, 1024, 2048, 3072, 4096 | Minimum bit length for Diffie-Hellman keys.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| rds.curve25519                        | **default**, enabled, disabled      | Curve25519 elliptic-curve encryption cipher. This parameter isn't supported for all<br>engine versions.                                                                                                                                                                                                                                                                                                                                                                        |
| rds.3des168                           | **default**, enabled, disabled      | Triple Data Encryption Standard (DES) encryption cipher with a 168-bit key<br>length.                                                                                                                                                                                                                                                                                                                                                                                          |

###### Note

For minor engine versions after 16.00.4120.1, 15.00.4365.2, 14.00.3465.1, 13.00.6435.1, and 12.00.6449.1,
the default setting for the DB parameters `rds.tls10`, `rds.tls11`, `rds.rc4`,
`rds.curve25519`, and `rds.3des168` is _disabled_.
Otherwise the default setting is _enabled_.

For minor engine versions after 16.00.4120.1, 15.00.4365.2, 14.00.3465.1, 13.00.6435.1, and 12.00.6449.1,
the default setting for `rds.diffie-hellman-min-key-bit-length`is 3072. Otherwise the default setting is 2048.

Use the following process to configure the security protocols and ciphers:

1. Create a custom DB parameter group.
2. Modify the parameters in the parameter group.
3. Associate the DB parameter group with your DB instance.
   For more information on DB parameter groups, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Creating the security-related parameter group

Create a parameter group for your security-related parameters that corresponds to the SQL
Server edition and version of your DB instance.

The following procedure creates a parameter group for SQL Server Standard Edition 2016.

###### To create the parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose **Create parameter group**.
4. In the **Create parameter group** pane, do the following:

   1. For **Parameter group family**, choose
      **sqlserver-se-13.0**.
   2. For **Group name**, enter an identifier for the parameter group, such
      as `sqlserver-ciphers-se-13`.
   3. For **Description**, enter `Parameter group for security
protocols and ciphers`.

5. Choose **Create**.
   The following procedure creates a parameter group for SQL Server Standard Edition 2016.

###### To create the parameter group

- Run one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-db-parameter-group \
    --db-parameter-group-name `sqlserver-ciphers-se-13` \
    --db-parameter-group-family "`sqlserver-se-13.0`" \
    --description "`Parameter group for security protocols and ciphers`"
```

For Windows:

```
aws rds create-db-parameter-group ^
    --db-parameter-group-name `sqlserver-ciphers-se-13` ^
    --db-parameter-group-family "`sqlserver-se-13.0`" ^
    --description "`Parameter group for security protocols and ciphers`"
```

## Modifying security-related parameters

Modify the security-related parameters in the parameter group that corresponds to the SQL
Server edition and version of your DB instance.

The following procedure modifies the parameter group that you created for SQL Server
Standard Edition 2016. This example turns off TLS version 1.0.

###### To modify the parameter group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose the parameter group, such as **sqlserver-ciphers-se-13**.
4. Under **Parameters**, filter the parameter list for
   `rds`.
5. Choose **Edit parameters**.
6. Choose **rds.tls10**.
7. For **Values**, choose **disabled**.
8. Choose **Save changes**.
   The following procedure modifies the parameter group that you created for SQL Server
   Standard Edition 2016. This example turns off TLS version 1.0.

###### To modify the parameter group

- Run one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
    --db-parameter-group-name `sqlserver-ciphers-se-13` \
    --parameters "ParameterName='`rds.tls10`',ParameterValue='`disabled`',ApplyMethod=pending-reboot"
```

For Windows:

```
aws rds modify-db-parameter-group ^
    --db-parameter-group-name `sqlserver-ciphers-se-13` ^
    --parameters "ParameterName='`rds.tls10`',ParameterValue='`disabled`',ApplyMethod=pending-reboot"
```

## Associating the security-related parameter group with your DB instance

To associate the parameter group with your DB instance, use the AWS Management Console or the AWS CLI.

You can associate the parameter group with a new or existing DB instance:

- For a new DB instance, associate it when you launch the instance.
  For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, associate it by modifying the instance.
  For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md "Overview.DBInstance.Modifying.md").
  You can associate the parameter group with a new or existing DB instance.

###### To create a DB instance with the parameter group

- Specify the same DB engine type and major version as you used when
  creating the parameter group.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mydbinstance` \
    --db-instance-class `db.m5.2xlarge` \
    --engine `sqlserver-se` \
    --engine-version `13.00.5426.0.v1` \
    --allocated-storage `100` \
    --master-user-password `secret123` \
    --master-username `admin` \
    --storage-type `gp2` \
    --license-model `li` \
    --db-parameter-group-name `sqlserver-ciphers-se-13`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --db-instance-class `db.m5.2xlarge` ^
    --engine `sqlserver-se` ^
    --engine-version `13.00.5426.0.v1` ^
    --allocated-storage `100` ^
    --master-user-password `secret123` ^
    --master-username `admin` ^
    --storage-type `gp2` ^
    --license-model `li` ^
    --db-parameter-group-name `sqlserver-ciphers-se-13`
```

###### Note

Specify a password other than the prompt shown here as a security best practice.

###### To modify a DB instance and associate the parameter group

- Run one of the following commands.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --db-parameter-group-name `sqlserver-ciphers-se-13` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --db-parameter-group-name `sqlserver-ciphers-se-13` ^
    --apply-immediately
```
