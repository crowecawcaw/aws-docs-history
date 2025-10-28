# Backing up in Oracle Database@AWS

Oracle Database@AWS provides multiple backup options to protect your Oracle databases. You can use Oracle
managed backups that integrate seamlessly with Amazon S3 or create your own user-managed backups using
Oracle Recovery Manager (RMAN).

## Oracle managed backups to Amazon S3

When you create an ODB network, Oracle Database@AWS automatically configures network access for Oracle
managed backups to Amazon S3. OCI configures necessary DNS entries and security lists. These
configurations allow traffic between the OCI Virtual Cloud Network (VCN) and Amazon S3. The ODB network
doesn't enable or control automatic backups.

Oracle managed backups are fully managed by OCI. When you create your Oracle Exadata
database, you can enable automatic backups by choosing **Enable automatic
backups** in the OCI console. Choose one of the following backup destinations:

- **Amazon S3**
- **OCI Object Storage**
- **Autonomous Recovery Service**

For more information, see [Backup Exadata Database](https://docs.oracle.com/en-us/iaas/Content/database-at-aws-exadata-awscr/awscr-create-exadata-database.html "https://docs.oracle.com/en-us/iaas/Content/database-at-aws-exadata-awscr/awscr-create-exadata-database.html") in the OCI documentation.

## User-managed backups to Amazon S3 in Oracle Database@AWS

With Oracle Database@AWS, you can create user-managed backups of your database using the Exadata Database
Service on Dedicated Infrastructure. You back up your data with Oracle Recovery Manager (RMAN)
and store it in your Amazon S3 buckets. You have full control over backup scheduling, retention
policies, and storage costs while maintaining the managed service benefits of Oracle Database@AWS.

###### Note

Oracle Database@AWS doesn't support user-managed backups for Autonomous Database on Dedicated
Infrastructure.

User-managed backups complement the AWS managed backup solutions provided by Oracle Database@AWS. You
can use manual backups for compliance requirements, cross-Region disaster recovery, or
integration with existing backup management workflows.

You can use the following user-managed backup techniques:

**Oracle Secure Backup**

Stream backups directly to Amazon S3 with optimal performance.

**Storage Gateway**

Use Storage Gateway for file-based backups that use an NFS share.

**S3 mount point**

Use a file client to mount an Amazon S3 bucket as a local file system.

### Prerequisites for user-managed backups to Amazon S3 in

Oracle Database@AWS

Before you can back up your Oracle Exadata databases to Amazon S3, do the following:

1. Enable direct access to Amazon S3 from your ODB network.
2. Configure network connectivity and routing between Oracle Database@AWS and Amazon S3.

#### Enabling access from your ODB network to Amazon S3

To back up your database manually to Amazon S3, enable direct access to S3 from your ODB network. This
technique allows your databases to access Amazon S3 for your business needs, such as data import/export
or user-managed backups. You have full control over the target destination of backup storage and
can use policies to restrict access to Amazon S3 using VPC Lattice.

Direct access to Amazon S3 from your ODB network isn't enabled by default. You can enable S3 access
when you create or modify your ODB network.

###### To enable direct access to Amazon S3 from your ODB network

1. Open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. In the navigation pane, choose **ODB networks**.
3. Select the ODB network for which you want to enable Amazon S3 access.
4. Choose **Modify**.
5. Select **Amazon S3**.
6. (Optional) Configure an Amazon S3 policy document to control access to Amazon S3. If you don't
   specify a policy, the default policy grants full access.
7. Choose **Continue** and then **Modify**.
   To enable direct Amazon S3 access from your ODB network, use the `update-odb-network`
   command with the `s3-access` parameter:

```
aws odb update-odb-network \
  --odb-network-id `odb-network-id` \
  --s3-access ENABLED
```

To configure an Amazon S3 policy document, use the `--s3-policy-document`
parameter:

```
aws odb update-odb-network \
  --odb-network-id `odb-network-id` \
  --s3-policy-document file://s3-policy.json
```

When Amazon S3 access is enabled, you can access Amazon S3 from your ODB network by using the regional DNS
`s3.`region`.amazonaws.com`. OCI configures this DNS name
by default. To use a custom DNS name, modify your VCN DNS to ensure the custom DNS resolves to
the IP address of the service network endpoint.

#### Configuring network connectivity between Oracle Database@AWS and

Amazon S3

To allow user-managed backups to Amazon S3, your VM must be able to access the S3 Amazon VPC
endpoint. In the OCI console, you can edit the security rules in a network security group (NSG)
to control the ingress and egress traffic. For user-managed backups, traffic flows over the
client subnet rather than the backup subnet. In the following steps, you update the NSGs for
the client subnet to add the egress rule for the VPC endpoint IP address.

###### To allow VM access to the Amazon S3 endpoint

1. Open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. Choose **ODB networks**.
3. Choose the name of the ODB network.
4. Choose **OCI resources**.
5. Choose the **Service integrations** tab.
6. Under **Amazon S3**, note the following pieces of information:
   - The IPv4 address of the Amazon VPC S3 endpoint. You need this information later. For
     example, the IP address might be `192.168.12.223`.
   - The domain name of the Amazon VPC S3 endpoint. You need this information later. For
     example, the domain name might be `s3.us-east-1.amazonaws.com`.

7. In the left navigation pane, choose Exadata VM clusters and then choose your VM cluster
   name.
8. At the top of the page, choose the **Summary** tab.
9. Choose **Virtual machines** and then choose the name of your VM.
10. Note the value in **DNS Name**. This is the host name that you specify
    when you connect to your VM using `ssh`.
11. In the top right, choose **Manage in OCI**. This opens the OCI
    console.
12. On the **Virtual Cloud Networks** list page, choose the VCN that
    contains the network security group (NSG) for the ODB network client subnet
    (`exa_static_nsg`). For more information, see [Managing Security Rules for an NSG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-security-rules.htm "https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-security-rules.htm") in the OCI documentation.
13. On the details page, perform one of the following actions depending on the option that
    you see:
    - On the **Security** tab, go to **Network Security
      Groups**.
    - Under **Resources**, choose **Network Security
      Groups**.

14. Choose the NSG for the client subnet (`exa_static_nsg`).
15. Add an egress rule for the VPC endpoint address that you noted earlier.

###### To test connectivity to S3 from your VM

1. Use `ssh` to connect as `root` to the VM whose DNS name you
   obtained previously. When you connect, specify a `.pem` file with your SSH
   keys.
2. Run the following commands to make sure that the VM can access the Amazon S3 Amazon VPC endpoint.
   Use the S3 domain name that you noted down previously.

```
# nslookup `s3.us-east-1.amazonaws.com`
# curl -v https://`s3.us-east-1.amazonaws.com`/
# aws s3 ls --endpoint-url https://`s3.us-east-1.amazonaws.com`
```

### Backing up to Amazon S3 using Oracle Secure Backup

Oracle Secure Backup acts as an SBT interface for use with Recovery Manager (RMAN). You can
use RMAN with Oracle Secure Backup to back up your Oracle Database@AWS databases directly to Amazon S3. Oracle
Secure Backup offers the following benefits:

- Oracle Secure Backup optimizes the data transfer between RMAN and S3.
- No intermediate backup storage is necessary.
- Oracle Secure Backup manages the lifecycle of your backup media.

###### To back up to Amazon S3 using Oracle Secure Backup

1. Install the Oracle Secure Backup module on your Exadata VM server. Replace the
   placeholder values with your AWS access key and secret access key. For more information, see
   the Oracle documentation at [Backup to Cloud with Oracle Secure Backup Cloud Module](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/backup-cloud-osb.html#GUID-EE4F48D8-61FA-4DAF-8169-FC42F15D828A "https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/backup-cloud-osb.html#GUID-EE4F48D8-61FA-4DAF-8169-FC42F15D828A").

```
cd $ORACLE_HOME/lib
java -jar osbws_install.jar -AWSID `aws-access-key-id` -AWSKey `aws-secret-access-key` -walletDir $ORACLE_HOME/dbs/osbws_wallet -location `us-west-2` -useHttps -awsEndPoint s3.`us-west-2`.amazonaws.com
```

2. Connect to RMAN and configure the backup channel and default device type.

```
RMAN target /
RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS 'SBT_LIBRARY=/u02/app/oracle/product/19.0.0.0/dbhome_2/lib/libosbws.so, ENV=(OSB_WS_PFILE=/u02/app/oracle/product/19.0.0.0/dbhome_2/dbs/osbwssmalikdb1.ora)';
RMAN> CONFIGURE DEFAULT DEVICE TYPE TO 'SBT_TAPE';
```

3. Verify the configuration.

```
RMAN> SHOW ALL;
```

4. Back up the database.

```
RMAN> BACKUP DATABASE;
```

5. Verify that the backup completed successfully.

```
RMAN> LIST BACKUP OF DATABASE SUMMARY;
```

### Backing up to Amazon S3 using AWS Storage Gateway on

Amazon EC2

AWS Storage Gateway is a hybrid service that connects your on-premises environment to AWS Cloud
storage services. For Oracle Database@AWS backups, you can use Storage Gateway to create a file-based backup workflow
that writes directly to Amazon S3. Unlike in the Oracle Secure Backup technique, you manage the
lifecycle of the backups.

In this solution, you create a separate Amazon EC2 instance for configuring Storage Gateway. You also
add an Amazon EBS volume to cache the reads and writes to Amazon S3.

This technique offers the following benefits:

- You don't require a media manager such as Oracle Secure Backup.
- No intermediate backup storage is necessary.

###### To deploy your Storage Gateway and create a file share

1. Open the AWS Management Console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/"), and choose the
   AWS Region where you want to create your gateway.
2. Deploy and activate an Amazon S3 file gateway, using an Amazon EC2 instance as the hub. Follow the
   instructions in [Deploy a customized Amazon EC2 host for
   S3 File Gateway](../../../filegateway/latest/files3/ec2-gateway-file.md "../../../filegateway/latest/files3/ec2-gateway-file.md") in the _Storage Gateway User Guide_.

When you configure your file gateway, make sure that you do the following:

    * Add at least one Amazon EBS volume for cache storage, with a size of at least 150
     GiB.
    * Open TCP/UDP port 2049 for NFS access in your security group. This allows you to create
     NFS file shares.
    * Open TCP port 80 for inbound traffic to allow one-time HTTP access during gateway
     activation. After activation, you can close this port.

3. Create a Amazon VPC endpoint for private connectivity between your ODB network and the Storage Gateway. For
   more information, see [Access an AWS service using an
   interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md").
4. Create a file share for your Amazon S3 bucket through the Storage Gateway console. For more
   information, see [Creating a file
   share](../../../filegateway/latest/files3/GettingStartedCreateFileShare.md "../../../filegateway/latest/files3/GettingStartedCreateFileShare.md").

###### To back up your database to Amazon S3 using Storage Gateway

1. In a terminal, use `ssh` to connect to the DNS name of the Exadata VM. To find
   the DNS name, see [Prerequisites for user-managed backups to Amazon S3 in
   Oracle Database@AWS](#manual-backups-prerequisites "#manual-backups-prerequisites").
2. Create a directory on the Exadata VM cluster server for the NFS mount. The following example creates
   the directory `/home/oracle/sgw_mount/`.

```
mkdir /home/oracle/sgw_mount/
```

3. Mount the NFS share on the directory that you just created. The following example creates
   the share on the directory `/home/oracle/sgw_mount/`. Replace
   `SG-IP-address` with your Storage Gateway IP address and
   `your-bucket-name` with the name of your S3 bucket.

```
sudo mount -t nfs -o nolock,hard `SG-IP-address`:/`your-bucket-name` /home/oracle/sgw_mount/
```

4. Connect to RMAN and back up the database to the mounted directory. The following example
   creates the channel `rman_local_bkp` and uses the mount point path to format the
   backup pieces.

```
$ rman TARGET /
RMAN> ALLOCATE CHANNEL rman_local_bkp DEVICE TYPE DISK;
RMAN> BACKUP FORMAT '/home/oracle/sgw_mount/%U' DATABASE;
```

5. Verify that the backup files are created in the mount directory. The following example
   shows two backup pieces.

```
$ ls -lart /home/oracle/sgw_mount/
total 8569632
-rw-r----- 1 oracle asmdba 1112223334 Jul 10 20:51 1a2b34cd_1234_1_1
drwxrwxrwx 1 nobody nobody 0 Jul 10 20:56 .
-rw-r----- 1 oracle asmdba 5556667778 Jul 10 20:56 1a2b34cd_1235_1_1
```

### Backing up to Amazon S3 using an S3 mount point

You can use Amazon S3 mount point to create backups locally first and then copy them to Amazon S3.
This technique creates backups on local storage and then transfers them to Amazon S3 using the mount
point interface. The backup time is longer than in other techniques because you need to back up
data twice.

###### Note

Direct backup to Amazon S3 using the mount point, without staging, isn't supported. RMAN
requires specific file system permissions that aren't compatible with the Amazon S3 mount point
interface.

This technique doesn't require you to license a media manager such as Oracle Secure Backup.
You manage the lifecycle of your backups.

###### To back up to Amazon S3 using an S3 mount point

1. In a terminal, use `ssh` to connect to the DNS name of the Exadata VM. To find
   the DNS name, see [Prerequisites for user-managed backups to Amazon S3 in
   Oracle Database@AWS](#manual-backups-prerequisites "#manual-backups-prerequisites").
2. Install the Amazon S3 mount point on the Exadata VM cluster server. For more information about installation and configuration, see [Mountpoint for Amazon S3](../../../AmazonS3/latest/userguide/mountpoint.md "../../../AmazonS3/latest/userguide/mountpoint.md") in the _Amazon S3 User Guide_.

```
$ sudo yum install ./mount-s3.rpm
```

3. Verify the installation by running the `mount-s3` command.

```
$ mount-s3 --version
mount-s3 1.19.0
```

4. Create an intermediate backup directory on the Exadata VM cluster server local storage. You will
   back up your database to this local directory and then copy the backup to your S3 bucket. The
   following example creates directory `/u02/rman_bkp_local`.

```
mkdir /u02/rman_bkp_local
```

5. Create a directory for the Amazon S3 mount point. The following example creates directory
   `/home/oracle/s3mount`.

```
$ mkdir /home/oracle/s3mount
```

6. Mount your Amazon S3 bucket using the mount point. The following example mounts an S3 bucket
   on directory `/home/oracle/s3mount`. Replace
   `your-s3-bucket-name` with your actual Amazon S3 bucket name.

```
$ mount-s3 s3://`your-s3-bucket-name` /home/oracle/s3mount
```

7. Verify that you can access the Amazon S3 bucket contents.

```
$ ls -lart /home/oracle/s3mount
```

8. Connect RMAN to your target database and back it up to your local staging directory. The
   following example creates the channel `rman_local_bkp` and uses the path
   `/u02/rman_bkp_local/` to format the backup pieces.

```
$ rman TARGET /

RMAN> ALLOCATE CHANNEL rman_local_bkp DEVICE TYPE DISK;
RMAN> BACKUP FORMAT '/u02/rman_bkp_local/%U' DATABASE;
```

9. Verify that the backups are created in the local directory:

```
$ cd /u02/rman_bkp_local/
$ ls -lart
total 4252128
drwxr-xr-x 8 oracle oinstall 4096 Jul 10 02:13 ..
-rw-r----- 1 oracle asmdba 1112223334 Jul 10 02:13 abcd1234_1921_1_1
drwxr-xr-x 2 oracle oinstall 4096 Jul 10 02:13 .
-rw-r----- 1 oracle asmdba 5556667778 Jul 10 02:14 abcd1234_1922_1_1
```

10. Copy the backup files from the local staging directory to the Amazon S3 mount point.

```
cp /u02/rman_bkp_local/* /home/oracle/s3mount/
```

11. Verify that you copied the files successfully to Amazon S3.

```
$ ls -lart /home/oracle/s3mount/
total 4252112
drwx------ 6 oracle oinstall 225 Jul 10 02:09 ..
drwxr-xr-x 2 oracle oinstall 0 Jul 10 02:24 .
-rw-r--r-- 1 oracle oinstall 1112223334 Jul 10 02:24 abcd1234_1921_1_1
-rw-r--r-- 1 oracle oinstall 5556667778 Jul 10 02:24 abcd1234_1922_1_1
```

### Disabling direct access to Amazon S3

If you no longer need direct access to Amazon S3 from your ODB network, you can disable it. Enabling
or disabling direct network access to S3 doesn't affect network access to Oracle managed backups
to Amazon S3.

###### To disable direct access to Amazon S3

1. Open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/ "https://console.aws.amazon.com/odb/").
2. In the navigation pane, choose **ODB networks**.
3. Select the ODB network for which you want to disable Amazon S3 access.
4. Choose **Modify**.
5. Clear the **Enable S3 access** checkbox.
6. Choose **Modify ODB network**.
   Use the `update-odb-network` command with the `s3-access`
   parameter.

```
aws odb update-odb-network \
  --odb-network-id `odb-network-id` \
  --s3-access DISABLED
```

## Troubleshooting the Amazon S3 integration

If you encounter issues with Oracle managed backups to Amazon S3 or direct access to Amazon S3,
consider the following troubleshooting steps:

**Cannot access Amazon S3 from your database**

Check the following:

- Verify that Amazon S3 access is enabled for your ODB network. Use the `GetOdbNetwork`
  action to check whether the `s3Access` status is `Enabled`.
- Ensure you are using the correct regional DNS name:
  `s3.`region`.amazonaws.com`.
- Check that your Oracle database has the necessary permissions to access Amazon S3.

**Oracle managed backups failing**

Check the following:

- Oracle managed backups to Amazon S3 are enabled by default and cannot be disabled. If
  backups are failing, check the Oracle database logs for specific error messages.
- Verify that the Amazon VPC Lattice resources are properly configured by viewing the service
  integration resources.
- Contact Oracle Support for assistance with Oracle managed automatic backup issues. For
  more information, see [Getting support for Oracle Database@AWS](odb-troubleshooting-overview.md#oracle-database-aws-support "odb-troubleshooting-overview.md#oracle-database-aws-support").
