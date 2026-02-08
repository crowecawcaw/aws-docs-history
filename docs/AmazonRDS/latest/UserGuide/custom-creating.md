# Configuring a DB instance for Amazon RDS Custom for Oracle

You can create an RDS Custom DB instance, and then connect to it using Secure Shell (SSH) or
AWS Systems Manager.

For more information about connecting and logging in to a RDS Custom for Oracle DB instance, see the following topics.

- [Connecting to your RDS Custom DB instance using Session Manager](custom-creating.md "custom-creating.md")
- [Connecting to your RDS Custom DB instance using SSH](#custom-creating.ssh "#custom-creating.ssh")
- [Logging in to your RDS Custom for Oracle database as
  SYS](custom-creating.md "custom-creating.md")

## Creating an RDS Custom for Oracle DB instance

Create an Amazon RDS Custom for Oracle DB instance using either the AWS Management Console or the AWS CLI. The procedure is
similar to the procedure for creating an Amazon RDS DB instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

If you included installation parameters in your CEV manifest, then your DB instance uses the
Oracle base, Oracle home, and the ID and name of the UNIX/Linux user and group that you specified. The
`oratab` file, which is created by Oracle Database during
installation, points to the real installation location rather than to a symbolic link. When
RDS Custom for Oracle runs commands, it runs as the configured OS user rather than the default user
`rdsdb`. For more information, see [Step 5: Prepare the CEV
manifest](custom-cev.md#custom-cev.preparing.manifest "custom-cev.md#custom-cev.preparing.manifest").

Before you attempt to create or connect to an RDS Custom DB instance, complete the tasks in [Setting up your environment for Amazon RDS Custom for Oracle](custom-setup-orcl.md "custom-setup-orcl.md").

###### To create an RDS Custom for Oracle DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose **Create database**.
4. In **Choose a database creation method**, select
   **Standard create**.
5. In the **Engine options** section, do the
   following:
   1. For **Engine type**, choose
      **Oracle**.
   2. For **Database management type**, choose
      **Amazon RDS Custom**.
   3. For **Architecture settings**, do one of the
      following:
      - Select **Multitenant architecture** to
        create a container database (CDB). At creation, your CDB
        contains one PDB seed and one initial PDB.

      ###### Note

      The **Multitenant architecture**
      setting is supported only for Oracle Database
      19c.
      - Clear **Multitenant architecture** to
        create a non-CDB. A non-CDB can't contain PDBs.

   4. For **Edition**, choose **Oracle
      Enterprise Edition** or **Oracle Standard
      Edition 2**.
   5. For **Custom engine version**, choose an existing
      RDS Custom custom engine version (CEV). A CEV has the following format:
      ``major-engine-version`.`customized_string``.
      An example identifier is `19.cdb_cev1`.

   If you chose **Multitenant architecture** in the
   previous step, you can only specify a CEV that uses the
   `custom-oracle-ee-cdb` or
   `custom-oracle-se2-cdb` engine type. The console
   filters out CEVs that were created with different engine
   types.

6. In **Templates**, choose
   **Production**.
7. In the **Settings** section, do the following:
   1. For **DB instance identifier**, enter a unique name for
      your DB instance.
   2. For **Master username**, enter a username. You
      can retrieve this value from the console later.

   When you connect to a non-CDB, the master user is the user for the non-CDB. When you connect to a CDB, the master user is the user for the PDB. To connect to the CDB root,
   log in to the host, start a SQL client, and create an administrative user with SQL commands. 3. Clear **Auto generate a password**.

8. Choose a **DB instance class**.

For supported classes, see [DB instance class support for RDS Custom for Oracle](custom-oracle-feature-support.md#custom-reqs-limits.instances "custom-oracle-feature-support.md#custom-reqs-limits.instances"). 9. In the **Storage** section, do the following:

    1. For **Storage type**, choose an SSD type: io1,
     io2, gp2, or gp3. You have the following additional options:




    	* For io1, io2, or gp3, choose a rate for
    	 **Provisioned IOPS**. The default is
    	 1000 for io1 and io2 and 12000 for gp3.
    	* For gp3, choose a rate for **Storage
    	 throughput**. The default is 500 MiBps.
    2. For **Allocated storage**, choose a storage size.
     The default is 40 GiB.

10. For **Connectivity**, specify your **Virtual
    private cloud (VPC)**, **DB subnet group**,
    and **VPC security group (firewall)**.
11. For **RDS Custom security**, do the following:
    1.  For **IAM instance profile**, choose the
        instance profile for your RDS Custom for Oracle DB instance.

    The IAM instance profile must begin with
    `AWSRDSCustom`, for example
    `AWSRDSCustomInstanceProfileForRdsCustomInstance`. 2. For **Encryption**, choose **Enter a key
    ARN** to list the available AWS KMS keys. Then choose
    your key from the list.

    An AWS KMS key is required for RDS Custom. For more information, see
    [Step 1: Create or reuse a symmetric encryption
    AWS KMS key](custom-setup-orcl.md#custom-setup-orcl.cmk "custom-setup-orcl.md#custom-setup-orcl.cmk").

12. For **Database options**, do the following:
    1.  (Optional) For **System ID (SID)**, enter a value
        for the Oracle SID, which is also the name of your CDB. The SID is
        the name of the Oracle database instance that manages your database
        files. In this context, the term "Oracle database instance" refers
        exclusively to the system global area (SGA) and Oracle background
        processes. If you don't specify a SID, the value defaults to
        `RDSCDB`.
    2.  (Optional) For **Initial database name**, enter a
        name. The default value is `ORCL`. In the
        multitenant architecture, the initial database name is the PDB
        name.

    ###### Note

    The SID and PDB name must be different. 3. For **Option group**, choose an option group or
    accept the default.

    ###### Note

    The only supported option for RDS Custom for Oracle is
    `Timezone`. For more information, see [Oracle time zone](custom-managing.md "custom-managing.md"). 4. For **Backup retention period** choose a value.
    You can't choose **0 days**. 5. For the remaining sections, specify your preferred RDS Custom DB
    instance settings. For information about each setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md"). The following
    settings don't appear in the console and aren't supported:

        * **Processor features**
        * **Storage autoscaling**
        * **Password and Kerberos authentication**
         option in **Database authentication** (only
         **Password authentication** is
         supported)
        * **Performance Insights**
        * **Log exports**
        * **Enable auto minor version
         upgrade**
        * **Deletion protection**

13. Choose **Create database**.

###### Important

When you create an RDS Custom for Oracle DB instance, you might receive the following
error: **`The service-linked role is in the process of being
 created. Try again later.`** If you do, wait a few minutes
and then try again to create the DB instance.

The **View credential details** button appears on the
**Databases** page.

To view the master user name and password for the RDS Custom DB instance, choose
**View credential details**.

To connect to the DB instance as the master user, use the user name and password
that appear.

###### Important

You can't view the master user password again in the console. If
you don't record it, you might have to change it. To change the
master user password after the RDS Custom DB instance is available, log in to the
database and run an `ALTER USER` command. You can't reset the
password using the **Modify** option in the
console. 14. Choose **Databases** to view the list of RDS Custom
DB instances. 15. Choose the RDS Custom DB instance that you just created.

On the RDS console, the details for the new RDS Custom DB instance appear:

    * The DB instance has a status of **creating** until the
     RDS Custom DB instance is created and ready for use. When the state changes to
     **available**, you can connect to the DB instance.
     Depending on the instance class and storage allocated, it can take
     several minutes for the new DB instance to be available.
    * **Role** has the value **Instance
     (RDS Custom)**.
    * **RDS Custom automation mode** has the value
     **Full automation**. This setting means that
     the DB instance provides automatic monitoring and instance
     recovery.

You create an RDS Custom DB instance by using the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") AWS CLI
command.

The following options are required:

- `--db-instance-identifier`
- `--db-instance-class` (for a list of supported instance
  classes, see [DB instance class support for RDS Custom for Oracle](custom-oracle-feature-support.md#custom-reqs-limits.instances "custom-oracle-feature-support.md#custom-reqs-limits.instances"))
- `--engine `engine-type``, where
`engine-type`is`custom-oracle-ee`,
`custom-oracle-se2`, `custom-oracle-ee-cdb`, or
`custom-oracle-se2-cdb`
- `--engine-version `cev`(where`cev`` is the name of the
  custom engine version that you specified in [Creating a CEV](custom-cev.md "custom-cev.md"))
- `--kms-key-id `my-kms-key``
- `--backup-retention-period `days`(where`days``is a value greater than`0`)
- `--no-auto-minor-version-upgrade`
- `--custom-iam-instance-profile
 AWSRDSCustomInstanceProfile-`us-east-1` (where`region``is the AWS Region
 where you are creating your DB instance)
The following example creates an RDS Custom DB instance named
`my-cfo-cdb-instance`. The database is a CDB with the nondefault name
 `MYCDB`. The nondefault PDB name is
 `MYPDB`. The backup retention period is three
  days.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --engine `custom-oracle-ee-cdb` \
    --db-instance-identifier `my-cfo-cdb-instance` \
    --engine-version `19.cdb_cev1` \
    --db-name `MYPDB` \
    --db-system-id `MYCDB` \
    --allocated-storage `250` \
    --db-instance-class `db.m5.xlarge` \
    --db-subnet-group `mydbsubnetgroup` \
    --master-username `myuser` \
    --master-user-password `mypassword` \
    --backup-retention-period `3` \
    --port `8200` \
    --kms-key-id `my-kms-key` \
    --no-auto-minor-version-upgrade \
    --custom-iam-instance-profile AWSRDSCustomInstanceProfile-`us-east-1`
```

For Windows:

```
aws rds create-db-instance ^
    --engine custom-oracle-ee-cdb ^
    --db-instance-identifier `my-cfo-cdb-instance` ^
    --engine-version `19.cdb_cev1` ^
    --db-name `MYPDB` ^
    --db-system-id `MYCDB` ^
    --allocated-storage `250` ^
    --db-instance-class `db.m5.xlarge` ^
    --db-subnet-group `mydbsubnetgroup` ^
    --master-username `myuser` ^
    --master-user-password `mypassword` ^
    --backup-retention-period `3` ^
    --port `8200` ^
    --kms-key-id `my-kms-key` ^
    --no-auto-minor-version-upgrade ^
    --custom-iam-instance-profile AWSRDSCustomInstanceProfile-`us-east-1`
```

###### Note

Specify a password other than the prompt shown here as a security best practice.

Get details about your instance by using the `describe-db-instances`
command.

```
aws rds describe-db-instances --db-instance-identifier `my-cfo-cdb-instance`
```

The following partial output shows the engine, parameter groups, and other
information.

```
        {
            "DBInstanceIdentifier": "my-cfo-cdb-instance",
            "DBInstanceClass": "db.m5.xlarge",
            "Engine": "custom-oracle-ee-cdb",
            "DBInstanceStatus": "available",
            "MasterUsername": "admin",
            "DBName": "MYPDB",
            "DBSystemID": "MYCDB",
            "Endpoint": {
                "Address": "my-cfo-cdb-instance.abcdefghijkl.us-east-1.rds.amazonaws.com",
                "Port": 1521,
                "HostedZoneId": "A1B2CDEFGH34IJ"
            },
            "AllocatedStorage": 100,
            "InstanceCreateTime": "2023-04-12T18:52:16.353000+00:00",
            "PreferredBackupWindow": "08:46-09:16",
            "BackupRetentionPeriod": 7,
            "DBSecurityGroups": [],
            "VpcSecurityGroups": [
                {
                    "VpcSecurityGroupId": "sg-0a1bcd2e",
                    "Status": "active"
                }
            ],
            "DBParameterGroups": [
                {
                    "DBParameterGroupName": "default.custom-oracle-ee-cdb-19",
                    "ParameterApplyStatus": "in-sync"
                }
            ],
...
```

## Multitenant architecture considerations

If you create an Amazon RDS Custom for Oracle DB instance with the Oracle multitenant architecture
(`custom-oracle-ee-cdb` or `custom-oracle-se2-cdb` engine type),
your database is a container database (CDB). If you don't specify the Oracle multitenant
architecture, your database is a traditional non-CDB that uses the
`custom-oracle-ee` or `custom-oracle-se2` engine type. A non-CDB
can't contain pluggable databases (PDBs). For more information, see [Database architecture for
Amazon RDS Custom for Oracle](custom-oracle.md "custom-oracle.md").

When you create an RDS Custom for Oracle CDB instance, consider the following:

- You can create a multitenant database only from an Oracle Database 19c CEV.
- You can create a CDB instance only if the CEV uses the
  `custom-oracle-ee-cdb` or `custom-oracle-se2-cdb` engine
  type.
- If you create a CDB instance using Standard Edition 2, the CDB can contain a
  maximum of 3 PDBs.
- By default, your CDB is named `RDSCDB`, which is also the name of the
  Oracle System ID (Oracle SID). You can choose a different name.
- You CDB contains only one initial PDB. The PDB name defaults to `ORCL`.
  You can choose a different name for your initial PDB, but the Oracle SID and the PDB
  name can’t be the same.
- RDS Custom for Oracle doesn't supply APIs for PDBs. To create additional PDBs, use the Oracle
  SQL command `CREATE PLUGGABLE DATABASE`. RDS Custom for Oracle doesn't restrict the
  number of PDBs that you can create. In general, you are responsible for creating and
  managing PDBs, as in an on-premises deployment.
- You can't use RDS APIs to create, modify, and delete PDBs: you must use Oracle SQL
  statements. When you create a PDB using Oracle SQL, we recommend that you take a
  manual snapshot afterward in case you need to perform point-in-time recovery
  (PITR).
- You can't rename existing PDBs using Amazon RDS APIs. You also can't rename the CDB using the
  `modify-db-instance` command.
- The open mode for the CDB root is `READ WRITE` on the primary and
  `MOUNTED` on a mounted standby database. RDS Custom for Oracle attempts to open
  all PDBs when opening the CDB. If RDS Custom for Oracle can’t open all PDBs, it issues the event
  `tenant database shutdown`.

## RDS Custom service-linked role

A _service-linked role_ gives Amazon RDS Custom access to
resources in your AWS account. It makes using RDS Custom easier because you don't have to
manually add the necessary permissions. RDS Custom defines the permissions of its service-linked
roles, and unless defined otherwise, only RDS Custom can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that permissions policy
can't be attached to any other IAM entity.

When you create an RDS Custom DB instance, both the Amazon RDS and RDS Custom service-linked roles are
created (if they don't already exist) and used. For more information, see [Using service-linked roles for
Amazon RDS](UsingWithRDS.IAM.md "UsingWithRDS.IAM.md").

The first time that you create an RDS Custom for Oracle DB instance, you might receive the following error:
**`The service-linked role is in the process of being created. Try again
 later.`** If you do, wait a few minutes and then try again to create the
DB instance.

## Installing additional software components on

your RDS Custom for Oracle DB instance

In a newly created DB instance, your database environment includes Oracle binaries, a database,
and a database listener. You might want to install additional software on the host operating
system of the DB instance. For example, you might want to install Oracle Application Express
(APEX), the Oracle Enterprise Manager (OEM) agent, or the Guardium S-TAP agent. For
guidelines and high-level instructions, see the detailed AWS blog post [Install additional software components on Amazon RDS Custom for Oracle](https://aws.amazon.com//blogs/database/install-additional-software-components-on-amazon-rds-custom-for-oracle/ "https://aws.amazon.com//blogs/database/install-additional-software-components-on-amazon-rds-custom-for-oracle/").

## Connecting to your RDS Custom DB instance using SSH

The Secure Shell Protocol (SSH) is a network protocol that supports encrypted
communication over an unsecured network. After you create your RDS Custom DB instance, you can connect
to it using an ssh client. For more information, see [Connecting to your Linux instance using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md").

Your SSH connection technique depends on whether your DB instance is private, meaning that it
doesn't accept connections from the public internet. In this case, you must use SSH
tunneling to connect the ssh utility to your instance. This technique transports data with a
dedicated data stream (tunnel) inside an existing SSH session. You can configure SSH
tunneling using AWS Systems Manager.

###### Note

Various strategies are supported for accessing private instances. To learn how to
connect an ssh client to private instances using bastion hosts, see [Linux Bastion Hosts
on AWS](https://aws.amazon.com/solutions/implementations/linux-bastion/ "https://aws.amazon.com/solutions/implementations/linux-bastion/"). To learn how to configure port forwarding, see [Port
Forwarding Using AWS Systems Manager Session Manager](https://aws.amazon.com/blogs/aws/new-port-forwarding-using-aws-system-manager-sessions-manager/ "https://aws.amazon.com/blogs/aws/new-port-forwarding-using-aws-system-manager-sessions-manager/").

If your DB instance is in a public subnet and has the publicly available setting, then no SSH
tunneling is required. You can connect with SSH just as would to a public Amazon EC2
instance.

To connect an ssh client to your DB instance, complete the following steps:

1. [Step 1: Configure your DB instance to allow SSH
   connections](#custom-managing.ssh.port-22 "#custom-managing.ssh.port-22")
2. [Step 2: Retrieve your SSH secret key
   and EC2 instance ID](#custom-managing.ssh.obtaining-key "#custom-managing.ssh.obtaining-key")
3. [Step 3: Connect to your EC2 instance
   using the ssh utility](#custom-managing.ssh.connecting "#custom-managing.ssh.connecting")

### Step 1: Configure your DB instance to allow SSH

connections

To make sure that your DB instance can accept SSH connections, do the following:

- Make sure that your DB instance security group permits inbound connections on port
  22 for TCP.

To learn how to configure the security group for your DB instance, see [Controlling access with security
groups](Overview.md "Overview.md").

- If you don't plan to use SSH tunneling, make sure your DB instance resides in a
  public subnet and is publicly accessible.

In the console, the relevant field is **Publicly accessible**
on the **Connectivity & security** tab of the database
details page. To check your settings in the CLI, run the following
command:

```
aws rds describe-db-instances \
--query 'DBInstances[*].{DBInstanceIdentifier:DBInstanceIdentifier,PubliclyAccessible:PubliclyAccessible}' \
--output table
```

To change the accessibility settings for your DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

### Step 2: Retrieve your SSH secret key

and EC2 instance ID

To connect to the DB instance using SSH, you need the SSH key pair associated with the
instance. RDS Custom creates the SSH key pair on your behalf, using the naming convention
`do-not-delete-rds-custom-ssh-privatekey-`resource_id`-`uuid``  or
 `rds-custom!oracle-do-not-delete-`resource_id`-`uuid`-ssh-privatekey`.
AWS Secrets Manager stores your SSH private key as a secret.

Retrieve your SSH secret key using either AWS Management Console or the AWS CLI. If your instance has
a public DNS, and you don't intend to use SSH tunneling, then also retrieve the DNS
name. You specify the DNS name for public connections.

###### To retrieve the secret SSH key

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and
   then choose the RDS Custom DB instance to which you want to connect.
3. Choose **Configuration**.
4. Note the **Resource ID** value. For example, the
   DB instance resource ID might be
   `db-ABCDEFGHIJKLMNOPQRS0123456`.
5. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
6. In the navigation pane, choose **Instances**.
7. Find the name of your EC2 instance, and choose the instance ID
   associated with it. For example, the EC2 instance ID might be
   `i-abcdefghijklm01234`.
8. In **Details**, find **Key pair
   name**. The pair name includes the DB instance resource ID. For
   example, the pair name might be
   `do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c`
   or
   `rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey`.
9. If your EC2 instance is public, note the **Public IPv4
   DNS**. For the example, the public Domain Name System (DNS)
   address might be
   `ec2-12-345-678-901.us-east-2.compute.amazonaws.com`.
10. Open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
11. Choose the secret that has the same name as your key pair.
12. Choose **Retrieve secret value**.
13. Copy the SSH private key into a text file, and then save the file with
    the `.pem` extension. For example, save the file as
    `/tmp/do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c.pem`
    or
    `/tmp/rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey.pem`.
    To retrieve the SSH private key and save it in a .pem file, you can use the
    AWS CLI.

14. Find the DB resource ID of your RDS Custom DB instance using `aws rds
describe-db-instances`.

```
aws rds describe-db-instances \
    --query 'DBInstances[*].[DBInstanceIdentifier,DbiResourceId]' \
    --output text
```

The following sample output shows the resource ID for your RDS Custom
instance. The prefix is `db-`.

```
db-ABCDEFGHIJKLMNOPQRS0123456
```

2. Find the EC2 instance ID of your DB instance using `aws ec2
describe-instances`. The following example uses
   `db-ABCDEFGHIJKLMNOPQRS0123456` for the resource
   ID.

```
aws ec2 describe-instances \
    --filters "Name=tag:Name,Values=db-ABCDEFGHIJKLMNOPQRS0123456" \
    --output text \
    --query 'Reservations[*].Instances[*].InstanceId'
```

The following sample output shows the EC2 instance ID.

```
i-abcdefghijklm01234
```

3. To find the key name, specify the EC2 instance ID. The following
   example describes EC2 instance `i-0bdc4219e66944afa`.

```
aws ec2 describe-instances \
    --instance-ids i-0bdc4219e66944afa \
    --output text \
    --query 'Reservations[*].Instances[*].KeyName'
```

The following sample output shows the key name, which uses the naming
format
`do-not-delete-rds-custom-ssh-privatekey-`resource_id`-`uuid``  or
 `rds-custom!oracle-do-not-delete-`resource_id`-`uuid`-ssh-privatekey`.

```
do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c
rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey
```

4. Save the private key in a .pem file named after the key using
   `aws secretsmanager`.

The following example saves the key
`do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c`
to a file in your `/tmp` directory.

```
aws secretsmanager get-secret-value \
    --secret-id do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c \
    --query SecretString \
    --output text >/tmp/do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c.pem
```

The following example saves the key
`rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey`
to a file in your `/tmp` directory.

```
aws secretsmanager get-secret-value \
    --secret-id rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey \
    --query SecretString \
    --output text >/tmp/rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey.pem
```

### Step 3: Connect to your EC2 instance

using the ssh utility

Your connection technique depends on whether you are connecting to a private DB instance or
connecting to a public instance. A private connection requires you to configure SSH
tunneling through AWS Systems Manager.

###### To connect to an EC2 instance using the ssh utility

1. For private connections, modify your SSH configuration file to proxy commands
   to AWS Systems Manager Session Manager. For public connections, skip to Step 2.

Add the following lines to `~/.ssh/config`. These lines proxy SSH
commands for hosts whose names begin with `i-` or
`mi-`.

```
Host i-* mi-*
    ProxyCommand sh -c "aws ssm start-session --target %h --document-name AWS-StartSSHSession --parameters 'portNumber=%p'"
```

2. Change to the directory that contains your .pem file. Using
   `chmod`, set the permissions to `400`.

The following example changes to the `/tmp` directory and sets
permissions for .pem file
`do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c.pem`.

```
cd /tmp
chmod 400 do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c.pem
```

The following example changes to the `/tmp` directory and sets
permissions for .pem file
`rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey.pem`.

```
cd /tmp
chmod 400 rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey.pem
```

3. Run the ssh utility, specifying the .pem file and either the public DNS name
   (for public connections) or the EC2 instance ID (for private connections). Log
   in as user `ec2-user`.

The following example connects to a public instance using the DNS name
`ec2-12-345-678-901.us-east-2.compute.amazonaws.com`.

```
# .pem file using naming prefix do-not-delete
ssh -i \
  "do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c.pem" \
  ec2-user@ec2-12-345-678-901.us-east-2.compute.amazonaws.com

# .pem file using naming prefix rds-custom!oracle-do-not-delete
ssh -i \
  "rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey.pem" \
  ec2-user@ec2-12-345-678-901.us-east-2.compute.amazonaws.com
```

The following example connects to a private instance using the EC2 instance ID
`i-0bdc4219e66944afa`.

```
# .pem file using naming prefix do-not-delete
ssh -i \
  "do-not-delete-rds-custom-ssh-privatekey-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c.pem" \
  ec2-user@i-0bdc4219e66944afa

# .pem file using naming prefix rds-custom!oracle-do-not-delete
ssh -i \
  "rds-custom!oracle-do-not-delete-db-ABCDEFGHIJKLMNOPQRS0123456-0d726c-ssh-privatekey.pem" \
  ec2-user@i-0bdc4219e66944afa
```
