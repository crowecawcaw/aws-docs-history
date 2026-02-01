# Amazon RDS Custom architecture

Amazon RDS Custom architecture is based on Amazon RDS, with important differences. The following diagram
shows the key components of the RDS Custom architecture.

![RDS Custom architecture components](images/RDS_Custom_gen_architecture.png)

###### Topics

- [VPC](#custom-concept.components.VPC "#custom-concept.components.VPC")
- [RDS Custom automation and monitoring](#custom-concept.workflow.automation "#custom-concept.workflow.automation")
- [Amazon S3](#custom-concept.components.S3 "#custom-concept.components.S3")
- [AWS CloudTrail](#custom-concept.components.CloudTrail "#custom-concept.components.CloudTrail")

## VPC

As in Amazon RDS, your RDS Custom DB instance resides in a virtual private cloud (VPC).

![RDS Custom DB instance components](images/RDS_Custom_instance.png)

Your RDS Custom DB instance consists of the following main components:

- Amazon EC2 instance
- Instance endpoint
- Operating system installed on the Amazon EC2 instance
- Amazon EBS storage, which contains any additional file systems

## RDS Custom automation and monitoring

RDS Custom has automation software that runs outside of the DB instance. This software
communicates with agents on the DB instance and with other components within the overall
RDS Custom environment.

The RDS Custom monitoring and recovery features offer similar functionality to Amazon RDS. By
default, RDS Custom is in full automation mode. The automation software has the following
primary responsibilities:

- Collect metrics and send notifications
- Perform automatic instance recovery

An important responsibility of RDS Custom automation is responding to problems with your
Amazon EC2 instance. For various reasons, the host might become impaired or unreachable.
RDS Custom resolves these problems by either rebooting or replacing the Amazon EC2
instance.

###### Topics

- [Amazon RDS Custom host replacement](#custom-troubleshooting.host-problems "#custom-troubleshooting.host-problems")
- [RDS Custom support
  perimeter](#custom-troubleshooting.support-perimeter "#custom-troubleshooting.support-perimeter")

### Amazon RDS Custom host replacement

If the Amazon EC2 host becomes impaired, RDS Custom attempts to reboot it. If this effort fails,
RDS Custom uses the same stop and start feature included in Amazon EC2. The only customer-visible
change when a host is replaced is a new public IP address.

###### Topics

- [Stopping and starting the host](#custom-troubleshooting.host-problems.replacement.stop-start "#custom-troubleshooting.host-problems.replacement.stop-start")
- [Effects of host replacement](#custom-troubleshooting.host-problems.replacement.host-state "#custom-troubleshooting.host-problems.replacement.host-state")
- [Best practices for Amazon EC2 hosts](#custom-troubleshooting.host-problems.best-practices "#custom-troubleshooting.host-problems.best-practices")

#### Stopping and starting the host

RDS Custom automatically takes the following steps, with no user intervention required:

1. Stops the Amazon EC2 host.

The EC2 instance performs a normal shutdown and stops running. Any Amazon EBS volumes remain attached to the instance,
and their data persists. Any data stored in the instance store volumes (not supported on RDS Custom) or RAM of the host
computer is gone.

For more information, see [Stop
and start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md") in the _Amazon EC2 User Guide_. 2. Starts the Amazon EC2 host.

The EC2 instance migrates to a new underlying host hardware. In some cases, the RDS Custom DB instance remains on the
original host.

#### Effects of host replacement

In RDS Custom, you have full control over the root device volume and Amazon EBS storage volumes. The root volume can contain important
data and configurations that you don't want to lose.

RDS Custom for Oracle retains all database and customer data after the operation, including root
volume data. No user intervention is required. On RDS Custom for SQL Server, database data is retained,
but any data on the `C:` drive, including operating system and customer data,
is lost.

After the host replacement process, the Amazon EC2 host has a new public IP address. The
new host retains the data and metadata shown in the following table.

| Metadata or data         | RDS Custom for Oracle retention | RDS Custom for SQL Server retention |
| ------------------------ | ------------------------------- | ----------------------------------- |
| EC2 instance ID          | Yes                             | No                                  |
| EC2 instance metadata    | Yes                             | Yes                                 |
| Data storage volume data | Yes                             | Yes                                 |
| Root volume data         | Yes                             | No                                  |
| Private IP addresses     | Yes                             | Yes                                 |
| Elastic IP addresses     | Yes                             | Yes                                 |

#### Best practices for Amazon EC2 hosts

The Amazon EC2 host replacement feature covers the majority of Amazon EC2 impairment scenarios. We recommend that you adhere to the
following best practices:

- Before you change your configuration or the operating system, back up your data. If the root volume or operating
  system becomes corrupt, host replacement can't repair it. Your only options are restoring from a DB snapshot or
  point-in-time recovery.
- Don't manually stop or terminate the physical Amazon EC2 host. Both actions result in the instance being put outside
  the RDS Custom support perimeter.
- (RDS Custom for SQL Server) If you attach additional volumes to the Amazon EC2 host, configure them to remount upon restart. If the host
  is impaired, RDS Custom might stop and start the host automatically.

### RDS Custom support

perimeter

RDS Custom provides additional monitoring capability called the _support
perimeter_. This additional monitoring ensures that your RDS Custom DB instance
uses a supported AWS infrastructure, operating system, and database.

The support perimeter checks that your DB instance conforms to the requirements listed
in [Fixing unsupported configurations in RDS Custom for Oracle](custom-troubleshooting.md#custom-troubleshooting.fix-unsupported "custom-troubleshooting.md#custom-troubleshooting.fix-unsupported") and [Fixing unsupported
configurations in RDS Custom for SQL Server](custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.fix-unsupported "custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.fix-unsupported"). If any of
these requirements aren't met, RDS Custom considers your DB instance to be outside of the
support perimeter.

###### Topics

- [Unsupported configurations in RDS Custom](#custom-concept.support-perimeter.unsupported-config "#custom-concept.support-perimeter.unsupported-config")
- [Troubleshooting unsupported configurations](#custom-concept.support-perimeter.fix-unsupported-config "#custom-concept.support-perimeter.fix-unsupported-config")

#### Unsupported configurations in RDS Custom

When your DB instance is outside the support perimeter, RDS Custom changes the DB instance
status to `unsupported-configuration` and sends event notifications.
After you fix the configuration problems, RDS Custom changes the DB instance status back
to `available`.

While your DB instance is in the `unsupported-configuration` state, the
following is true:

- Your database is reachable. An exception is when the DB instance is in the
  `unsupported-configuration` because the database is
  shutting down unexpectedly.
- You can't modify your DB instance.
- You can't take DB snapshots.
- Automatic backups aren't created.
- For RDS Custom for SQL Server DB instances only, RDS Custom doesn't replace the underlying Amazon EC2
  instance if it becomes impaired. For more information about host
  replacement, see [Amazon RDS Custom host replacement](#custom-troubleshooting.host-problems "#custom-troubleshooting.host-problems").
- You can delete your DB instance, but most other RDS Custom API operations aren't
  available.
- RDS Custom continues to support point-in-time recovery (PITR) by archiving
  redo log files and uploading them to Amazon S3. PITR in an
  `unsupported-configuration` state differs in the
  following ways:
  - PITR can take a long time to completely restore to a new
    RDS Custom DB instance. This situation occurs because you can't take
    either automated or manual snapshots while the instance is in
    the `unsupported-configuration` state.
  - PITR has to replay more redo logs starting from the most
    recent snapshot taken before the instance entered the
    `unsupported-configuration` state.
  - In some cases, the DB instance is in the
    `unsupported-configuration` state because you
    made a change that prevented the uploading of archived redo log
    files. Examples include stopping the EC2 instance, stopping the
    RDS Custom agent, and detaching EBS volumes. In such cases, PITR
    can't restore the DB instance to the latest restorable time.

#### Troubleshooting unsupported configurations

RDS Custom provides troubleshooting guidance for the
`unsupported-configuration` state. Although some guidance applies
to both RDS Custom for Oracle and RDS Custom for SQL Server, other guidance depends on your DB engine. For
engine-specific troubleshooting information, see the following topics:

- [Fixing unsupported configurations in RDS Custom for Oracle](custom-troubleshooting.md#custom-troubleshooting.fix-unsupported "custom-troubleshooting.md#custom-troubleshooting.fix-unsupported")
- [Fixing unsupported
  configurations in RDS Custom for SQL Server](custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.fix-unsupported "custom-troubleshooting-sqlserver.md#custom-troubleshooting-sqlserver.fix-unsupported")

## Amazon S3

If you use RDS Custom for Oracle, you upload installation media to a user-created Amazon S3 bucket.
RDS Custom for Oracle uses the media in this bucket to create a custom engine version (CEV). A
_CEV_ is a binary volume snapshot of a database
version and Amazon Machine Image (AMI). From the CEV, you can create an RDS Custom DB
instance. For more information, see [Working with custom engine versions for Amazon RDS Custom for Oracle](custom-cev.md "custom-cev.md").

For both RDS Custom for Oracle and RDS Custom for SQL Server, RDS Custom automatically creates an Amazon S3 bucket prefixed with the string
`do-not-delete-rds-custom-`. RDS Custom uses the `do-not-delete-rds-custom-` S3 bucket to store
the following types of files:

- AWS CloudTrail logs for the trail created by RDS Custom
- Support perimeter artifacts (see [RDS Custom support
  perimeter](#custom-troubleshooting.support-perimeter "#custom-troubleshooting.support-perimeter"))
- Database redo log files (RDS Custom for Oracle only)
- Transaction logs (RDS Custom for SQL Server only)
- Custom engine version artifacts (RDS Custom for Oracle only)

RDS Custom creates the `do-not-delete-rds-custom-` S3 bucket when you create either of the following
resources:

- Your first CEV for RDS Custom for Oracle
- Your first DB instance for RDS Custom for SQL Server

RDS Custom creates one bucket for each combination of the following:

- AWS account ID
- Engine type (either RDS Custom for Oracle or RDS Custom for SQL Server)
- AWS Region

For example, if you create RDS Custom for Oracle CEVs in a single AWS Region, one `do-not-delete-rds-custom-` bucket
exists. If you create multiple RDS Custom for SQL Server instances, and they reside in different AWS Regions, one
`do-not-delete-rds-custom-` bucket exists in each AWS Region. If you create one RDS Custom for Oracle instance and two
RDS Custom for SQL Server instances in a single AWS Region, two `do-not-delete-rds-custom-` buckets exist.

## AWS CloudTrail

RDS Custom automatically creates an AWS CloudTrail trail whose name begins with `do-not-delete-rds-custom-`. The RDS Custom
support perimeter relies on the events from CloudTrail to determine whether your actions affect RDS Custom automation. For more information, see
[Troubleshooting unsupported configurations](#custom-concept.support-perimeter.fix-unsupported-config "#custom-concept.support-perimeter.fix-unsupported-config").

RDS Custom creates the trail when you create your first DB instance. RDS Custom creates one trail for each combination of the
following:

- AWS account ID
- Engine type (either RDS Custom for Oracle or RDS Custom for SQL Server)
- AWS Region

When you delete an RDS Custom DB instance, the CloudTrail for this instance isn't automatically
removed. In this case, your AWS account continues to be billed for the undeleted CloudTrail.
RDS Custom is not responsible for the deletion of this resource. To learn how to remove the
CloudTrail manually, see [Deleting a trail](../../../awscloudtrail/latest/userguide/cloudtrail-delete-trails-console.md "../../../awscloudtrail/latest/userguide/cloudtrail-delete-trails-console.md") in the _AWS CloudTrail User
Guide_.
