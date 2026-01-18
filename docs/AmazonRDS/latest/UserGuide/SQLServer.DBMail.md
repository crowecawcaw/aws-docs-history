# Configuring Database Mail

You perform the following tasks to configure Database Mail:

1. Create the Database Mail profile.
2. Create the Database Mail account.
3. Add the Database Mail account to the Database Mail profile.
4. Add users to the Database Mail profile.

###### Note

To configure Database Mail, make sure that you have `execute`
permission on the stored procedures in the `msdb` database.

## Creating the Database Mail profile

To create the Database Mail profile, you use the [sysmail_add_profile_sp](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profile-sp-transact-sql "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profile-sp-transact-sql") stored procedure. The following example creates a profile named
`Notifications`.

###### To create the profile

- Use the following SQL statement.

```
USE msdb
GO

EXECUTE msdb.dbo.sysmail_add_profile_sp
    @profile_name         = 'Notifications',
    @description          = 'Profile used for sending outgoing notifications using Amazon SES.';
GO
```

## Creating the Database Mail account

To create the Database Mail account, you use the [sysmail_add_account_sp](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-account-sp-transact-sql "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-account-sp-transact-sql") stored procedure. The following example creates an account named `SES` on an RDS for SQL Server DB instance
in a private VPC, using Amazon Simple Email Service.

Using Amazon SES requires the following parameters:

- `@email_address` – An Amazon SES verified identity. For more information, see [Verified identities in
  Amazon SES](../../../ses/latest/dg/verify-addresses-and-domains.md "../../../ses/latest/dg/verify-addresses-and-domains.md").
- `@mailserver_name` – An Amazon SES SMTP endpoint. For more information, see [Connecting to an Amazon SES SMTP endpoint](../../../ses/latest/dg/smtp-connect.md "../../../ses/latest/dg/smtp-connect.md").
- `@username` – An Amazon SES SMTP user name. For more information, see [Obtaining Amazon SES SMTP credentials](../../../ses/latest/dg/smtp-credentials.md "../../../ses/latest/dg/smtp-credentials.md").

Don't use an AWS Identity and Access Management user name.

- `@password` – An Amazon SES SMTP password. For more information, see [Obtaining Amazon SES SMTP credentials](../../../ses/latest/dg/smtp-credentials.md "../../../ses/latest/dg/smtp-credentials.md").

###### To create the account

- Use the following SQL statement.

```
USE msdb
GO

EXECUTE msdb.dbo.sysmail_add_account_sp
    @account_name        = 'SES',
    @description         = 'Mail account for sending outgoing notifications.',
    @email_address       = '`nobody@example.com`',
    @display_name        = 'Automated Mailer',
    @mailserver_name     = '`vpce-0a1b2c3d4e5f-01234567.email-smtp.us-west-2.vpce`.amazonaws.com',
    @port                = 587,
    @enable_ssl          = 1,
    @username            = '`Smtp_Username`',
    @password            = '`Smtp_Password`';
GO
```

###### Note

Specify credentials other than the prompts shown here as a security best practice.

## Adding the Database Mail account to the Database Mail

profile

To add the Database Mail account to the Database Mail profile, you use the [sysmail_add_profileaccount_sp](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profileaccount-sp-transact-sql "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profileaccount-sp-transact-sql") stored procedure. The following example adds the `SES` account to the
`Notifications` profile.

###### To add the account to the profile

- Use the following SQL statement.

```
USE msdb
GO

EXECUTE msdb.dbo.sysmail_add_profileaccount_sp
    @profile_name        = 'Notifications',
    @account_name        = 'SES',
    @sequence_number     = 1;
GO
```

## Adding users to the Database Mail profile

To grant permission for an `msdb` database principal to use a Database Mail profile, you use the [sysmail_add_principalprofile_sp](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-principalprofile-sp-transact-sql "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-principalprofile-sp-transact-sql") stored procedure. A _principal_ is an entity that can
request SQL Server resources. The database principal must map to a SQL Server authentication user, a Windows Authentication
user, or a Windows Authentication group.

The following example grants public access to the `Notifications` profile.

###### To add a user to the profile

- Use the following SQL statement.

```
USE msdb
GO

EXECUTE msdb.dbo.sysmail_add_principalprofile_sp
    @profile_name       = 'Notifications',
    @principal_name     = 'public',
    @is_default         = 1;
GO
```
