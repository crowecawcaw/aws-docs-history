# Turning on SSRS

Use the following process to turn on SSRS for your DB instance:

1. Create a new option group, or choose an existing option group.
2. Add the `SSRS` option to the option group.
3. Associate the option group with the DB instance.
4. Allow inbound access to the virtual private cloud (VPC) security group for the SSRS
   listener port.

## Creating an option group for

SSRS

To work with SSRS, create an option group that corresponds to the SQL Server engine and
version of the DB instance that you plan to use. To do this, use the AWS Management Console or
the AWS CLI.

###### Note

You can also use an existing option group if it's for the correct SQL
Server engine and version.

The following procedure creates an option group for SQL Server Standard Edition 2017.

###### To create the option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose **Create group**.
4. In the **Create option group** pane, do the following:
   1. For **Name**, enter a name for the option group that is unique within your AWS account, such as
      `ssrs-se-2017`. The name can contain only letters, digits, and
      hyphens.
   2. For **Description**, enter a brief description of the option group, such as `SSRS option group for SQL Server SE 
2017`. The description is used for display purposes.
   3. For **Engine**, choose **sqlserver-se**.
   4. For **Major engine version**, choose
      **14.00**.

5. Choose **Create**.
   The following procedure creates an option group for SQL Server Standard Edition
6.

###### To create the option group

- Run one of the following commands.
  For Linux, macOS, or Unix:

```
aws rds create-option-group \
    --option-group-name `ssrs-se-2017` \
    --engine-name `sqlserver-se` \
    --major-engine-version `14.00` \
    --option-group-description "`SSRS option group for SQL Server SE 2017`"
```

For Windows:

```
aws rds create-option-group ^
    --option-group-name `ssrs-se-2017` ^
    --engine-name `sqlserver-se` ^
    --major-engine-version `14.00` ^
    --option-group-description "`SSRS option group for SQL Server SE 2017`"
```

## Adding the SSRS option to your option group

Next, use the AWS Management Console or the AWS CLI to add the `SSRS` option to your option group.

###### To add the SSRS option

1.  Sign in to the AWS Management Console and open the Amazon RDS console at
    [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  In the navigation pane, choose **Option groups**.
3.  Choose the option group that you just created, then choose **Add option**.
4.  Under **Option details**, choose **SSRS** for **Option
    name**.
5.  Under **Option settings**, do the following:
    1. Enter the port for the SSRS service to listen on. The default is 8443. For a list of allowed
       values, see [Limitations and recommendations](Appendix.SQLServer.Options.md#SSRS.Limitations "Appendix.SQLServer.Options.md#SSRS.Limitations").
    2. Enter a value for **Max memory**.

    **Max memory** specifies the upper threshold above which no new memory allocation
    requests are granted to report server applications. The number is a percentage of the total memory
    of the DB instance. The allowed values are 10–80. 3. For **Security groups**, choose the VPC security group to associate with the
    option. Use the same security group that is associated with your DB instance.

6.  To use SSRS Email to send reports, choose the **Configure email delivery options** check
    box under **Email delivery in reporting services**, and then do the following:
    1. For **Sender email address**, enter the
       email address to use in the **From** field
       of messages sent by SSRS Email.

    Specify a user account that has permission to send mail from the SMTP server. 2. For **SMTP server**, specify the SMTP server or gateway to use.

    It can be an IP address, the NetBIOS name of a computer on your corporate intranet, or a fully
    qualified domain name. 3. For **SMTP port**, enter the port to use to connect to the mail server. The
    default is 25. 4. To use authentication:

        1. Select the **Use authentication** check box.
        2. For **Secret Amazon Resource Name (ARN)** enter the AWS Secrets Manager ARN for the
         user credentials.


        Use the following format:


        `arn:aws:secretsmanager:`Region`:`AccountId`:secret:`SecretName`-`6RandomCharacters``


        For example:


        `arn:aws:secretsmanager:`us-west-2`:`123456789012`:secret:`MySecret-a1b2c3``


        For more information on creating the secret, see [Using SSRS Email to send reports](SSRS.md "SSRS.md").

    5. Select the **Use Secure Sockets Layer (SSL)** check box to encrypt email messages
       using SSL.

7.  Under **Scheduling**, choose whether to add the option immediately or at the next
    maintenance window.
8.  Choose **Add option**.

###### To add the SSRS option

1. Create a JSON file, for example `ssrs-option.json`.
   1. Set the following required parameters:
      - `OptionGroupName` – The name of option group that you created or chose
        previously (`ssrs-se-2017` in the following example).
      - `Port` – The port for the SSRS service to listen on. The default is
      8443. For a list of allowed values, see [Limitations and recommendations](Appendix.SQLServer.Options.md#SSRS.Limitations "Appendix.SQLServer.Options.md#SSRS.Limitations").
      - `VpcSecurityGroupMemberships` – VPC security group memberships for your
        RDS DB instance.
      - `MAX_MEMORY` – The upper threshold above which no new memory allocation
        requests are granted to report server applications. The number is a percentage of the total
        memory of the DB instance. The allowed values are 10–80.

   2. (Optional) Set the following parameters to use SSRS Email:
      - `SMTP_ENABLE_EMAIL` – Set to `true` to use SSRS Email. The
        default is `false`.
      - `SMTP_SENDER_EMAIL_ADDRESS` –
        The email address to use in the
        **From** field of messages sent
        by SSRS Email. Specify a user account that has
        permission to send mail from the SMTP server.
      - `SMTP_SERVER` – The SMTP server or gateway to use. It can be an IP
        address, the NetBIOS name of a computer on your corporate intranet, or a fully qualified
        domain name.
      - `SMTP_PORT` – The port to use to connect to the mail server. The default
        is 25.
      - `SMTP_USE_SSL` – Set to `true` to encrypt email messages
        using SSL. The default is `true`.
      - `SMTP_EMAIL_CREDENTIALS_SECRET_ARN` – The Secrets Manager ARN that holds the
        user credentials. Use the following format:

      `arn:aws:secretsmanager:`Region`:`AccountId`:secret:`SecretName`-`6RandomCharacters``

      For more information on creating the secret, see [Using SSRS Email to send reports](SSRS.md "SSRS.md").
      - `SMTP_USE_ANONYMOUS_AUTHENTICATION` – Set to `true` and
        don't include `SMTP_EMAIL_CREDENTIALS_SECRET_ARN` if you don't want to
        use authentication.

      The default is `false` when `SMTP_ENABLE_EMAIL` is
      `true`.The following example includes the SSRS Email parameters, using the secret ARN.

```
{
"OptionGroupName": "`ssrs-se-2017`",
"OptionsToInclude": [
	{
	"OptionName": "SSRS",
	"Port": `8443`,
	"VpcSecurityGroupMemberships": ["`sg-0abcdef123`"],
	"OptionSettings": [
            {"Name": "MAX_MEMORY","Value": "`60`"},
            {"Name": "SMTP_ENABLE_EMAIL","Value": "`true`"}
            {"Name": "SMTP_SENDER_EMAIL_ADDRESS","Value": "`nobody@example.com`"},
            {"Name": "SMTP_SERVER","Value": "email-smtp.`us-west-2`.amazonaws.com"},
            {"Name": "SMTP_PORT","Value": "`25`"},
            {"Name": "SMTP_USE_SSL","Value": "`true`"},
            {"Name": "SMTP_EMAIL_CREDENTIALS_SECRET_ARN","Value": "arn:aws:secretsmanager:`us-west-2`:`123456789012`:secret:`MySecret-a1b2c3`"}
            ]
	}],
"ApplyImmediately": true
}
```

2. Add the `SSRS` option to the option group.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --cli-input-json file://`ssrs-option.json` \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --cli-input-json file://`ssrs-option.json` ^
    --apply-immediately
```

## Associating your option group with your

DB instance

Use the AWS Management Console or the AWS CLI to associate your option group with your DB instance.

If you use an existing DB instance, it must already have an Active Directory domain and
AWS Identity and Access Management (IAM) role associated with it. If you create a new instance, specify an existing
Active Directory domain and IAM role. For more information, see [Working with Active Directory with RDS for SQL Server](User.SQLServer.md "User.SQLServer.md").

You can associate your option group with a new or existing DB instance:

- For a new DB instance, associate the option group when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- For an existing DB instance, modify the instance and associate the new option group.
  For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
  You can associate your option group with a new or existing DB instance.

###### To create a DB instance that uses your option group

- Specify the same DB engine type and major version as you used when
  creating the option group.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `myssrsinstance` \
    --db-instance-class `db.m5.2xlarge` \
    --engine `sqlserver-se` \
    --engine-version `14.00.3223.3.v1` \
    --allocated-storage `100` \
    --manage-master-user-password  \
    --master-username `admin` \
    --storage-type `gp2` \
    --license-model `li` \
    --domain-iam-role-name `my-directory-iam-role` \
    --domain `my-domain-id` \
    --option-group-name `ssrs-se-2017`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `myssrsinstance` ^
    --db-instance-class `db.m5.2xlarge` ^
    --engine `sqlserver-se` ^
    --engine-version `14.00.3223.3.v1` ^
    --allocated-storage `100` ^
    --manage-master-user-password ^
    --master-username `admin` ^
    --storage-type `gp2` ^
    --license-model `li` ^
    --domain-iam-role-name `my-directory-iam-role` ^
    --domain `my-domain-id` ^
    --option-group-name `ssrs-se-2017`
```

###### To modify a DB instance to use your option group

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `myssrsinstance` \
    --option-group-name `ssrs-se-2017` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `myssrsinstance` ^
    --option-group-name `ssrs-se-2017` ^
    --apply-immediately
```

## Allowing inbound access to your VPC

security group

To allow inbound access to the VPC security group associated with your DB instance, create
an inbound rule for the specified SSRS listener port. For more information about
setting up security groups, see [Provide access to your DB instance in your VPC by
creating a security group](CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup "CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup").
