# Best practices for using Amazon EFS volumes with Amazon ECS

Make note of the following best practice recommendations when you use Amazon EFS with Amazon ECS.

## Security and access controls for Amazon EFS volumes

Amazon EFS offers access control features that you can use to ensure that the data
stored in an Amazon EFS file system is secure and accessible only from applications that
need it. You can secure data by enabling encryption at rest and in-transit. For more
information, see [Data encryption in Amazon EFS](../../../efs/latest/ug/encryption.md "../../../efs/latest/ug/encryption.md") in the
_Amazon Elastic File System User Guide_.

In addition to data encryption, you can also use Amazon EFS to restrict access to a
file system. There are three ways to implement access control in EFS.

- **Security groups**—With Amazon EFS mount
  targets, you can configure a security group that's used to permit and deny
  network traffic. You can configure the security group attached to Amazon EFS to
  permit NFS traffic (port 2049) from the security group that's attached to
  your Amazon ECS instances or, when using the `awsvpc` network mode,
  the Amazon ECS task.
- **IAM**—You can restrict access to
  an Amazon EFS file system using IAM. When configured, Amazon ECS tasks require an
  IAM role for file system access to mount an EFS file system. For more
  information, see [Using IAM to
  control file system data access](../../../efs/latest/ug/iam-access-control-nfs-efs.md "../../../efs/latest/ug/iam-access-control-nfs-efs.md") in the
  _Amazon Elastic File System User Guide_.

IAM policies can also enforce predefined conditions such as requiring a
client to use TLS when connecting to an Amazon EFS file system. For more
information, see [Amazon EFS condition keys for clients](../../../efs/latest/ug/iam-access-control-nfs-efs.md#efs-condition-keys-for-nfs "../../../efs/latest/ug/iam-access-control-nfs-efs.md#efs-condition-keys-for-nfs") in the
_Amazon Elastic File System User Guide_.

- **Amazon EFS access points**—Amazon EFS access
  points are application-specific entry points into an Amazon EFS file system. You
  can use access points to enforce a user identity, including the user's POSIX
  groups, for all file system requests that are made through the access point.
  Access points can also enforce a different root directory for the file
  system. This is so that clients can only access data in the specified
  directory or its sub-directories.

### IAM policies

You can use IAM policies to control the access to the Amazon EFS file
system.

You can specify the following actions for clients accessing a file system using a file system policy.

| Action                               | Description                                                 |
| ------------------------------------ | ----------------------------------------------------------- |
| `elasticfilesystem:ClientMount`      | Provides read-only access to a file system.                 |
| `elasticfilesystem:ClientWrite`      | Provides write permissions on a file system.                |
| `elasticfilesystem:ClientRootAccess` | Provides use of the root user when accessing a file system. |

You need to specify each action in a policy. The policies can be defined in
the following ways:

- Client-based - Attach the policy to the task role

Set the **IAM authorization** option when you
create the task definition.

- Resource-based - Attach the policy to Amazon EFS file system

If the resource-based policy does not exist, by default at file system
creation access is granted to all principals (\*).

When you set the **IAM authorization** option, we merge the
the policy associated with the task role and the Amazon EFS resource-based. The
**IAM authorization** option passes the task identity
(the task role) with the policy to Amazon EFS. This allows the Amazon EFS resource-based
policy to have context for the IAM user or role specified in the policy. If
you do not set the option, the Amazon EFS resource-level policy identifies the
IAM user as ”anonymous".

Consider implementing all three access controls on an Amazon EFS file system for
maximum security. For example, you can configure the security group attached to an
Amazon EFS mount point to only permit ingress NFS traffic from a security group that's
associated with your container instance or Amazon ECS task. Additionally, you can
configure Amazon EFS to require an IAM role to access the file system, even if the
connection originates from a permitted security group. Last, you can use Amazon EFS
access points to enforce POSIX user permissions and specify root directories for
applications.

The following task definition snippet shows how to mount an Amazon EFS file system
using an access point.

```
"volumes": [
    {
      "efsVolumeConfiguration": {
        "fileSystemId": "`fs-1234`",
        "authorizationConfig": {
          "accessPointId": "`fsap-1234`",
          "iam": "ENABLED"
        },
        "transitEncryption": "ENABLED",
        "rootDirectory": ""
      },
      "name": "`my-filesystem`"
    }
]
```

## Amazon EFS volume performance

Amazon EFS offers two performance modes: General Purpose and Max I/O. General Purpose
is suitable for latency-sensitive applications such as content management systems
and CI/CD tools. In contrast, Max I/O file systems are suitable for workloads such
as data analytics, media processing, and machine learning. These workloads need to
perform parallel operations from hundreds or even thousands of containers and
require the highest possible aggregate throughput and IOPS. For more information,
see [Amazon EFS performance
modes](../../../efs/latest/ug/performance.md#performancemodes "../../../efs/latest/ug/performance.md#performancemodes") in the _Amazon Elastic File System User Guide_.

Some latency sensitive workloads require both the higher I/O levels that are
provided by Max I/O performance mode and the lower latency that are provided by
General Purpose performance mode. For this type of workload, we recommend creating
multiple General Purpose performance mode file systems. That way, you can spread
your application workload across all these file systems, as long as the workload and
applications can support it.

## Amazon EFS volume throughput

All Amazon EFS file systems have an associated metered throughput that's determined by
either the amount of provisioned throughput for file systems using
_Provisioned Throughput_ or the amount of data stored in the
EFS Standard or One Zone storage class for file systems using _Bursting
Throughput_. For more information, see [Understanding metered
throughput](../../../efs/latest/ug/performance.md#read-write-throughput "../../../efs/latest/ug/performance.md#read-write-throughput") in the _Amazon Elastic File System User Guide_.

The default throughput mode for Amazon EFS file systems is bursting mode. With bursting
mode, the throughput that's available to a file system scales in or out as a file
system grows. Because file-based workloads typically spike, requiring high levels of
throughput for periods of time and lower levels of throughput the rest of the time,
Amazon EFS is designed to burst to allow high throughput levels for periods of time.
Additionally, because many workloads are read-heavy, read operations are metered at
a 1:3 ratio to other NFS operations (like write).

All Amazon EFS file systems deliver a consistent baseline performance of 50 MB/s for
each TB of Amazon EFS Standard or Amazon EFS One Zone storage. All file systems (regardless of
size) can burst to 100 MB/s. File systems with more than 1TB of EFS Standard or EFS
One Zone storage can burst to 100 MB/s for each TB. Because read operations are
metered at a 1:3 ratio, you can drive up to 300 MiBs/s for each TiB of read
throughput. As you add data to your file system, the maximum throughput that's
available to the file system scales linearly and automatically with your storage in
the Amazon EFS Standard storage class. If you need more throughput than you can achieve
with your amount of data stored, you can configure Provisioned Throughput to the
specific amount your workload requires.

File system throughput is shared across all Amazon EC2 instances connected to a file
system. For example, a 1TB file system that can burst to 100 MB/s of throughput can
drive 100 MB/s from a single Amazon EC2 instance can each drive 10 MB/s. For more
information, see [Amazon EFS performance](../../../efs/latest/ug/performance.md "../../../efs/latest/ug/performance.md") in the
_Amazon Elastic File System User Guide_.

## Optimizing cost for Amazon EFS volumes

Amazon EFS simplifies scaling storage for you. Amazon EFS file systems grow automatically as
you add more data. Especially with Amazon EFS _Bursting Throughput_
mode, throughput on Amazon EFS scales as the size of your file system in the standard
storage class grows. To improve the throughput without paying an additional cost for
provisioned throughput on an EFS file system, you can share an Amazon EFS file system
with multiple applications. Using Amazon EFS access points, you can implement storage
isolation in shared Amazon EFS file systems. By doing so, even though the applications
still share the same file system, they can't access data unless you authorize
it.

As your data grows, Amazon EFS helps you automatically move infrequently accessed files
to a lower storage class. The Amazon EFS Standard-Infrequent Access (IA) storage class
reduces storage costs for files that aren't accessed every day. It does this without
sacrificing the high availability, high durability, elasticity, and the POSIX file
system access that Amazon EFS provides. For more information, see [EFS storage
classes](../../../efs/latest/ug/features.md "../../../efs/latest/ug/features.md") in the _Amazon Elastic File System User Guide_.

Consider using Amazon EFS lifecycle policies to automatically save money by moving
infrequently accessed files to Amazon EFS IA storage. For more information, see [Amazon EFS
lifecycle management](../../../efs/latest/ug/lifecycle-management-efs.md "../../../efs/latest/ug/lifecycle-management-efs.md") in the _Amazon Elastic File System User Guide_.

When creating an Amazon EFS file system, you can choose if Amazon EFS replicates your data
across multiple Availability Zones (Standard) or stores your data redundantly within
a single Availability Zone. The Amazon EFS One Zone storage class can reduce storage
costs by a significant margin compared to Amazon EFS Standard storage classes. Consider
using Amazon EFS One Zone storage class for workloads that don't require multi-AZ
resilience. You can further reduce the cost of Amazon EFS One Zone storage by moving
infrequently accessed files to Amazon EFS One Zone-Infrequent Access. For more
information, see [Amazon EFS
Infrequent Access](https://aws.amazon.com/efs/features/infrequent-access/ "https://aws.amazon.com/efs/features/infrequent-access/").

## Amazon EFS volume data protection

Amazon EFS stores your data redundantly across multiple Availability Zones for file
systems using Standard storage classes. If you select Amazon EFS One Zone storage
classes, your data is redundantly stored within a single Availability Zone.
Additionally, Amazon EFS is designed to provide 99.999999999% (11 9’s) of durability over
a given year.

As with any environment, it's a best practice to have a backup and to build
safeguards against accidental deletion. For Amazon EFS data, that best practice includes
a functioning, regularly tested backup using AWS Backup. File systems using Amazon EFS One
Zone storage classes are configured to automatically back up files by default at
file system creation unless you choose to disable this functionality. For more
information, see [Backing up EFS file systems](../../../efs/latest/ug/awsbackup.md "../../../efs/latest/ug/awsbackup.md")
in the _Amazon Elastic File System User Guide_.
