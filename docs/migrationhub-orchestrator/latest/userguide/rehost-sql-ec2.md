AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Rehost SQL Server on Amazon EC2 template

With **Rehost SQL server on Amazon EC2** template, you
can rehost your SQL Server databases on an instance to Amazon EC2 using automated SQL
Server backup and restore. You can also migrate databases that are encrypted with
transparent data encryption (TDE). This template migrates User database items,
Certificates, Logins and Agent Jobs that are associated with your SQL Server.

###### Topics

- [Prerequisites](#rehost-sql-ec2 "#rehost-sql-ec2")
- [Creating the migration workflow](#w32aac16c15b9 "#w32aac16c15b9")
- [Running the migration workflow](#w32aac16c15c11 "#w32aac16c15c11")
- [FAQ](#w32aac16c15c13 "#w32aac16c15c13")

## Prerequisites

You must set up the source environment before creating a migration
workflow.

###### Topics

- [Source environment setup](#w32aac16c15b7b7 "#w32aac16c15b7b7")

### Source environment setup

- Ensure that PowerShell is enabled on the server that contains your SQL
  server instance.
- Install AWS.Tools on the server that contains your SQL server
  instance, with the following command.

```
Install-Module -Name AWS.Tools.Installer
```

- Install the `DBA.Tools` module on your Windows machine, with the following command.

```
Cmd: Install-Module dbatools
```

## Creating the migration workflow

1. Go to
   [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/")
2. Select
   **Create migration workflow**
   .
3. On Choose a workflow template page, select
   **Rehost SQL server on Amazon EC2**
   template.
4. Configure and submit your workflow to begin migration.

###### Note

You can customize the migration workflow once it has been created. For more information, see
[Migration workflows for Migration Hub Orchestrator](migration-workflows.md "migration-workflows.md").

###### Topics

- [Application](#w32aac16c15b9b7b3 "#w32aac16c15b9b7b3")
- [ServerId](#w32aac16c15b9b7b5 "#w32aac16c15b9b7b5")
- [Source Environment Configuration](#w32aac16c15b9b7b7 "#w32aac16c15b9b7b7")
- [Target Environment Configuration](#w32aac16c15b9b7b9 "#w32aac16c15b9b7b9")

#### Application

Select the application you want to migrate. If you do not see the application
in the list, you must define it in [AWS Application
Discovery Service](https://console.aws.amazon.com/discovery/home "https://console.aws.amazon.com/discovery/home"). An Application in this context is considered as a
group of servers, and does not refer to applications running on top of your SQL
server.

#### ServerId

Within the Application you defined in the [AWS Application
Discovery Service](https://console.aws.amazon.com/discovery/home "https://console.aws.amazon.com/discovery/home"), select the serverId of the server which hosts
your SQL server.

#### Source Environment Configuration

The details here help us to identify the details of your source SQL
Server.

1. **TDE**

- Check this checkbox if you have TDE enabled on your Databases. If
  you select this option, your certificates will be migrated to the target
  server.

2. **Migration Mode**

- This template offers 3 distinct migrations depending on your
  use-case.
  1.  “
      _Use only Full backup_
      ” - The template will only create a full backup of your
      databases and restore it on your target.
  2.  “
      _Use Full backup and Differential backup for
      Cutover_
      ” - A full backup of your databases will be created and
      restored on the target, after which you can mark the databases
      readonly, and a differential backup and restore will be used to
      migrate the remainder of the data.
  3.  “
      _Use Full backup, Differential backup for
      pre-cutover and T-Log backup for cutover_
      ” - A full backup of your databases will be created and
      restored on the target. When you are getting ready for cutover,
      a differential backup and restore will be used to migrate the
      remainder of the data. Lastly, after you mark your databases
      readonly, Tail-Log backups will be used to migrate the remainder
      of the data.

3. **Allow Migration Without Direct Connect**

- This template uploads backup files from your source instance to S3
  using the AWS CLI. The database files are transmitted over an HTTPS to
  AWS S3. However, if you are not comfortable with the backup files
  travelling over the public Internet, we recommend using AWS Direct
  Connect with a Public VIF setup. If you are comfortable with this,
  please select this checkbox. The migration workflow will not create
  unless you check this checkbox or have the setup mentioned above.

4. **Source SQL Server database names**

- The names of the SQL Databases that you would like to
  migrate.

5. **AWS ADS server ID for your application**

- See “ServerId” section above.

6. **Source SQL Server instance name**

- The name of your SQL server instance.

7. **Backup location**

- As a part of the migration, this template needs to take backups of
  your SQL Server. The path specified here is where the backup files will
  be stored. Please ensure this is an absolute path and has enough space
  for a Full and Differential backup of your databases.

#### Target Environment Configuration

The details here help us to identify the details of your migration to your
target server.

1. **Restore Logins**

- Select this checkbox if you would like to migrate your SQL Server
  Logins to your target instance.

2. **Restore Agent Jobs**

- Select this checkbox if you would like to migrate your SQL Server
  Agent Jobs to your target instance.

## Running the migration workflow

- When configuring the Migration Hub Orchestrator plugin, ensure that the
  username that is provided to connect to your Windows machine has the

`SYSAdmin`
permission on the source SQL server instance.

### Create AWS Profile on Source Server

- Create an IAM policy with the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "kms:GenerateDataKey",
 "kms:CreateKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

- Create an IAM user with the above policy attached.
- Configure a named profile for AWS Command Line Interface that uses the
  preceding IAM user. For more information, see
  [Using AWS credentials](../../../powershell/latest/userguide/specifying-your-aws-credentials.md "../../../powershell/latest/userguide/specifying-your-aws-credentials.md")
  . The credentials stored in the profile are used to upload your
  backups to a S3 bucket located in your account. (You will need the name
  of this profile when creating the workflow)

### Create Target EC2 Instance

This template does not create your EC2 instance for you. To create this
instance based on your requirements, we recommend one of the following:

- (
  _Optional_
  ) If you want to use BYOL for SQL server, use AWS VM Import/Export to
  import your VM image.
- (
  _Optional_
  ) Use AWS Launch Wizard to deploy your target SQL server.
  - Launch Wizard attaches the

  `AmazonEC2RoleForLaunchWizard`
  instance role by default when creating the target
  environment.
  - After creating the target environment with Launch Wizard,
    attach the
    `AWSMigrationHubOrchestratorInstanceRolePolicy`
    managed policy to
    `AmazonEC2RoleForLaunchWizard`
    . For more information, see
    [AWS managed policies for Migration Hub Orchestrator](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubOrchestratorInstanceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubOrchestratorInstanceRolePolicy")
    .

- Connect to the target EC2 instance and note the following:
  - Name of the SQL Server
  - Path to store data for the SQL Server
  - Path to store logs for the SQL Server
  - Path to store the downloaded backup files for the restore
    procedure. Please ensure this is large enough to hold the backup
    files of your database.

### Configure Target Permissions

Once your EC2 instance is configured and your target SQL server is deployed,
follow these steps:

- If you are not using Launch Wizard to create your target environment,
  attach the
  `AWSMigrationHubOrchestratorInstanceRolePolicy`
  managed policy to your instance role.
- Add the following permissions to your instance role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "kms:Decrypt",
 "s3:ListAllMyBuckets",
 "s3:ListBucket"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Create Target SQL Server User

- Create a username in your target SQL server with
  `SYSAdmin`
  permission.
- Provide credentials in AWS Secrets Manager for the username created in
  your target SQL server.
  1.  Sign in to
      [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/")
  2.  On the AWS Secrets Manager page, select
      **Store a new secret**
      .
  3.  For Secret type, select
      **Other type of secret**
      and enter the following keys.
      1. `username`
      - enter your username
      2. `password`
      - enter your password

  4.  Select
      **Next**
      and enter a name for the key pair beginning with
      `migrationhub-orchestrator-`secretname123``
      .
      1. The Secret ID must begin with the prefix
         `migrationhub-orchestrator-`
         and must only be followed by an alphanumeric
         value.

  5.  Select
      **Next**
      and then, select
      **Store**
      .
  6.  Copy the name of this secret and put the value into the manual
      step in the workflow.

## FAQ

Q. **What does this template do?**

A. This template migrates User Database Items, Certificates, Agent Jobs and Logins
from a source SQL server to a target SQL Server environment on Amazon EC2 .

Q. **Do I need to create the target SQL
Server?**

A. Yes. This template focuses on data migration. You need to setup the target SQL
server before using this template. Based on your requirements, we recommend using
AWS Launch Wizard or AWS VM Import/Export Service to accomplish this.

Q. **What kind of backups do you use for
migration?**

A. Based on your input, we use either only a full backup, a combination of full
and differential backups or a combination of full, differential and tail-log backups
for migration.

Q. **When do I need to put my databases in ‘readonly’
mode?**

A. Based on the type of migration selected there are different points to do this

-

1. For full backup only migrations set the databases to readonly before
   begging the migration workflow.
2. For full and differential backup migrations, set the databases to read
   only when instructed to do so on Step 4.1 in the workflow.
3. For full, differential and tail-log backups, set the databases to read
   only when instructed to do so on Step 4.4 in the workflow.

These different configurations help us ensure we capture all the changes in your
SQL server when migrating, to create parity between your source and target.

Q. **What security measures do you take while migrating
data?**

A. Our goal is to handle data securely at all times. Backup files are transferred
over an HTTPS connection to AWS S3, and then to your target EC2 instance.
Certificate files are handled specially, as the workflow creates a KMS key in your
account, which is used to encrypt the certificate before transport, and de-crypt the
certificate in your target environment.

Q. **What are the limitations of this
template?**

A. This template will not do the following:

1. This template does not migrate System Databases or SQL Server
   properties.
2. This template can only migrate SQL logins. Any Windows level logins are
   not guaranteed to be migrated.
3. This template expects that while the workflow is running, you will not
   initiate a full-backup of the database yourself. If a full-backup is taken,
   it breaks the chain of backups used to restore your databases on the target
   server.

Q. **I ran into an error during a database connection step.
What do I do?**

A. An error here indicates a problem with connecting to your SQL Server.

1. If this occurs on the source, ensure the user that was given to the plugin
   to connect to the machine has SYSADMIN permissions on your source SQL
   server.
2. If this happens on the target, ensure that the EC2 Instance ID provided
   during workflow creation is correct, and ensure the SQL credentials stored
   in your Secrets Manager Secret are correct.

Q. **I ran into an error during a database validation step.
What do I do?**

A. An error here indicates an incompatibility between the inputs provided during
workflow creation and the target environment. Look at the step logs located inside
the S3 bucket shown in the error message to diagnose the issue and re-create the
workflow with the appropriate inputs.

Q. **I ran into an error while a backup step was running. What
do I do?**

A. If you run into an error during the backup steps, look at the step logs located
inside the S3 bucket shown in the error message. Once you diagnose and fix the
issue, please clean the appropriate backup directory on the source machine before
re-trying this step.

Q. **I ran into an error while a restore step was running.
What do I do?**

A. If you run into an error during the restore steps, look at the step logs
located inside the S3 bucket shown in the error message. If you have taken a full
backup after the workflow started, the backup chain is broken and hence this
workflow cannot be recovered. You will have to delete the workflow, wipe your target
SQL server and re-create the workflow.
