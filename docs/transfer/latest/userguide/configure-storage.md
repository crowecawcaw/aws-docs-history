# Configure storage to use with AWS Transfer Family

servers

This topic describes the storage options that you can use with AWS Transfer Family. You can use
either Amazon S3 or Amazon EFS as storage for your Transfer Family servers.

###### Contents

- [Configure an Amazon S3 bucket](configure-storage.md#requirements-S3 "configure-storage.md#requirements-S3")
  - [Amazon S3 access points](configure-storage.md#access-points "configure-storage.md#access-points")
  - [Amazon S3 HeadObject behavior](configure-storage.md#head-object-behavior "configure-storage.md#head-object-behavior")
    - [Grant ability to only write and
      list files](configure-storage.md#headobject-access-denied "configure-storage.md#headobject-access-denied")
    - [Large number of zero-byte objects
      causing latency issues](configure-storage.md#headobject-latency "configure-storage.md#headobject-latency")

- [Configure an Amazon EFS file system](configure-storage.md#requirements-efs "configure-storage.md#requirements-efs")
  - [Amazon EFS file ownership](configure-storage.md#efs-file-ownership "configure-storage.md#efs-file-ownership")
  - [Set up Amazon EFS users for
    Transfer Family](configure-storage.md#configure-efs-users-permissions "configure-storage.md#configure-efs-users-permissions")
    - [Configure Transfer Family users on
      Amazon EFS](configure-storage.md#set-up-efs-home-folders "configure-storage.md#set-up-efs-home-folders")
    - [Create an Amazon EFS root user](configure-storage.md#create-root-user-efs "configure-storage.md#create-root-user-efs")

  - [Supported Amazon EFS commands](configure-storage.md#efs-commands "configure-storage.md#efs-commands")

## Configure an Amazon S3 bucket

AWS Transfer Family accesses your Amazon S3 bucket to service your users' transfer requests,
so you need to provide an Amazon S3 bucket as part of setting up your file transfer
protocol-enabled server. You can use an existing bucket, or you can create a new
one.

###### Note

You don't have to use a server and Amazon S3 bucket that are in the same AWS
Region, but we recommend this as a best practice.

When you set up your users, you assign them each an IAM role. This role
determines the level of access that they have to your Amazon S3 bucket.

For information on creating a new bucket, see [How do I create an
S3 bucket?](../../../AmazonS3/latest/user-guide/create-bucket-overview.md "../../../AmazonS3/latest/user-guide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_.

###### Note

You can use Amazon S3 Object Lock to prevent objects from being overwritten for a
fixed amount of time or indefinitely. This works the same way with Transfer Family as with
other services. If an object exists and is protected, writing to that file or
deleting it is not allowed. For more details on Amazon S3 Object Lock, see [Using
Amazon S3 Object Lock](../../../AmazonS3/latest/user-guide/object-lock.md "../../../AmazonS3/latest/user-guide/object-lock.md") in the _Amazon Simple Storage Service User Guide_.

### Amazon S3 access points

AWS Transfer Family supports [Amazon S3 Access Points](https://aws.amazon.com/s3/features/access-points/ "https://aws.amazon.com/s3/features/access-points/"), a feature of Amazon S3 that allows you to easily
manage granular access to shared data sets. You can use S3 Access Point aliases
anywhere you use an S3 bucket name. You can create hundreds of access points in
Amazon S3 for users who have different permissions to access shared data in an Amazon S3
bucket.

For example, you can use access points to allow three different teams to have
access to the same shared dataset where one team can read data from S3, a second
team can write data to S3, and the third team can read, write, and delete data
from S3. To implement a granular access control as mentioned above, you can
create an S3 access point that contains a policy that gives asymmetrical access
to different teams. You can use S3 access points with your Transfer Family server to
achieve a fine-grained access control, without creating a complex S3 bucket
policy that spans hundreds of use cases. To learn more about how to use S3
access points with a Transfer Family server, refer to the [Enhance data access control with AWS Transfer Family and Amazon S3](https://aws.amazon.com/blogs/storage/enhance-data-access-control-with-aws-transfer-family-and-amazon-s3-access-points/ "https://aws.amazon.com/blogs/storage/enhance-data-access-control-with-aws-transfer-family-and-amazon-s3-access-points/") blog
post.

###### Note

AWS Transfer Family does not currently support Amazon S3 Multi-Region Access
Points.

### Amazon S3 HeadObject behavior

###### Note

When you create or update a Transfer Family server, you can optimize performance for
your Amazon S3 directories, which eliminates `HeadObject`
calls.

In Amazon S3, buckets and objects are the primary resources, and objects are stored
in buckets. Amazon S3 can mimic a hierarchical file system, but can sometimes behave
differently than a typical file system. For example, directories are not a
first-class concept in Amazon S3 but instead are based on object keys. AWS Transfer Family
infers a directory path by splitting an object's key by the forward slash
character (**/**), treating the last element as the file name,
then grouping file names which have the same prefix together under the same
path. Zero-byte objects are created to represent a folder's path when you create
an empty directory using `mkdir` or by using the Amazon S3 console. The
key for these objects ends in a trailing forward slash. These zero-byte objects
are described in [Organizing objects in the
Amazon S3 console using folders](../../../AmazonS3/latest/userguide/using-folders.md "../../../AmazonS3/latest/userguide/using-folders.md") in the
_Amazon S3 User Guide_.

When you run an `ls` command, and some results are Amazon S3 zero-byte
objects (these objects have keys that end in the forward slash character), Transfer Family
issues a `HeadObject` request for each of these objects (see [HeadObject](../../../AmazonS3/latest/API/API_HeadObject.md "../../../AmazonS3/latest/API/API_HeadObject.md") in the _Amazon Simple Storage Service API Reference_ for details).
This can result in the following problems when using Amazon S3 as your storage with
Transfer Family.

#### Grant ability to only write and

list files

In some cases, you might want to offer only write access to your Amazon S3 objects. For example, you might want to provide
access to write (or upload) and list objects in a bucket, but not to read (download) objects. To perform `ls`
and `mkdir` commands by using file transfer clients, you must have the Amazon S3 `ListObjects`
and `PutObject` permissions. However, when Transfer Family needs to make a `HeadObject`
call to either write or list files, the call fails with an error of **Access denied**, because this
call requires the `GetObject` permission.

###### Note

When you create or update a Transfer Family server, you can optimize performance for your Amazon S3 directories, which eliminates
`HeadObject` calls.

In this case, you can grant access by adding an AWS Identity and Access Management (IAM) policy condition that adds the
`GetObject` permission only for objects that end in a slash
(`/`). This condition prevents `GetObject` calls on files (so that they can't be read),
but allows the user to list and traverse folders. The following example policy offers
only write and list access to your Amazon S3 buckets. To use this policy, replace
`amzn-s3-demo-bucket` with the name of your bucket.

###### Note

To address WinSCP's upload behavior, make sure to add the
`"arn:aws:s3:::amzn-s3-demo-bucket/*.filepart"` line as listed in the following example policy.
This line ensures proper handling of .filepart objects to prevent failures.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowListing",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
        },
        {
            "Sid": "AllowReadWrite",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ]
         },
      {
            "Sid": "DenyIfNotFolder",
            "Effect": "Deny",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "NotResource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/*/",
                "arn:aws:s3:::amzn-s3-demo-bucket/*.filepart"
            ]
         }
      ]
}
```

###### Note

This policy doesn't allow users to append files. In other words, a user who
is assigned this policy can't open files to add content to them, or to
modify them. Additionally, if your use case requires a `HeadObject`
call before uploading a file, this policy won't
work for you.

#### Large number of zero-byte objects

causing latency issues

If your Amazon S3 buckets contain a large number of these zero-byte objects,
Transfer Family issues a lot of `HeadObject` calls, which can result in
processing delays. The recommended solution for this issue is to enable
**Optimized Directories** to reduce latency.

For example, suppose that you go into your home directory, and you have
10,000 subdirectories. In other words, your Amazon S3 bucket has 10,000 folders.
In this scenario, if you run the `ls` (list) command, the list
operation takes between six and eight minutes. However, if you optimize your
directories, this operation takes only a few seconds. You set this option in
the **Configure additional details** screen during the
server creation or update procedure. These procedures are detailed under the
[Configuring an SFTP, FTPS, or FTP server
endpoint](sftp-for-transfer-family.md "sftp-for-transfer-family.md") topic.

###### Note

GUI clients may issue an `ls` command outside your control,
so it is important to enable this setting if you can.

If you don't or can't optimize your directories, an alternate solution to
this problem is to delete all of your zero-byte objects. Note the
following:

- Empty directories will no longer exist. Directories only exist as
  a result of their names being in the key of an object.
- Doesn’t prevent someone from calling `mkdir` and
  breaking things all over again. You could mitigate this by crafting
  a policy which prevents directory creation.
- Some scenarios make use of these 0-byte objects. For example, you
  have a structure like **/inboxes/customer1000** and
  the inbox directory gets cleaned every day.

Finally, one more possible solution is to limit the number of objects
visible through a policy condition to reduce the number of
`HeadObject` calls. For this to be a workable solution, you
need to accept that you might only be able to view a limited set of all of
your sub-directories.

## Configure an Amazon EFS file system

AWS Transfer Family accesses Amazon Elastic File System (Amazon EFS) to service your users' transfer requests.
So you must provide an Amazon EFS file system as part of setting up your file transfer
protocol-enabled server. You can use an existing file system, or you can create a
new one.

Note the following:

- When you use a Transfer Family server and an Amazon EFS file system, the server and the
  file system must be in the same AWS Region.
- The server and the file system don't need to be in the same account. If
  the server and file system are not in the same account, the file system
  policy must give explicit permission to the user role.

For information about how to set up multiple accounts, see [Managing
the AWS accounts in your organization](../../../organizations/latest/userguide/orgs_manage_accounts.md "../../../organizations/latest/userguide/orgs_manage_accounts.md") in the
_AWS Organizations User Guide_.

- When you set up your users, you assign them each an IAM role. This role
  determines the level of access that they have to your Amazon EFS file
  system.
- For details on mounting an Amazon EFS file system, see [Mounting
  Amazon EFS file systems](../../../efs/latest/ug/mounting-fs.md "../../../efs/latest/ug/mounting-fs.md").

For more details on how AWS Transfer Family and Amazon EFS work together, see [Using AWS Transfer Family to access files in your Amazon EFS file system](../../../efs/latest/ug/using-aws-transfer-integration.md "../../../efs/latest/ug/using-aws-transfer-integration.md") in the
_Amazon Elastic File System User Guide_.

### Amazon EFS file ownership

Amazon EFS uses the Portable Operating System Interface (POSIX) file permission
model to represent file ownership.

In POSIX, users in the system are categorized into three distinct permission
classes: When you allow a user to access files stored in an Amazon EFS file
system using AWS Transfer Family, you must assign them a “POSIX profile.” This profile is
used to determine their access to files and directories in the Amazon EFS file
system.

- User (u): Owner of the file or directory. Usually, the creator of a
  file or directory is also the owner.
- Group (g): Set of users that need identical access to files and
  directories that they share.
- Others (o): All other users that have access to the system except for
  the owner and group members. This permission class is also referred to
  as "Public."

In the POSIX permission model, every file system object (files, directories,
symbolic links, named pipes, and sockets) is associated with the previously
mentioned three sets of permissions. Amazon EFS objects have a Unix-style mode
associated with them. This mode value defines the permissions for performing
actions on that object.

Additionally, on Unix-style systems, users and groups are mapped to numeric
identifiers, which Amazon EFS uses to represent file ownership. For Amazon EFS, objects
are owned by a single owner and a single group. Amazon EFS uses the mapped numeric
IDs to check permissions when a user attempts to access a file system
object.

### Set up Amazon EFS users for

Transfer Family

Before you set up your Amazon EFS users, you can do either of the following:

- You can create users and set up their home folders in Amazon EFS. See [Configure Transfer Family users on
  Amazon EFS](#set-up-efs-home-folders "#set-up-efs-home-folders") for details.
- If you are comfortable adding a root user, you can [Create an Amazon EFS root user](#create-root-user-efs "#create-root-user-efs").

###### Note

Transfer Family servers do not support Amazon EFS access points to set POSIX permissions.
Transfer Family users' POSIX profiles (described in the preceding section) offer the
ability to set POSIX permissions. These permissions are set at a user level,
for granular access, based on UID, GID, and secondary GIDs.

#### Configure Transfer Family users on

Amazon EFS

Transfer Family maps the users to the UID/GID and directories you specify. If the
UID/GID/directories do not already exist in EFS, then you should create them
before assigning them in Transfer to a user. The details for creating Amazon EFS
users is described in [Working with
users, groups, and permissions at the Network File System (NFS)
Level](../../../efs/latest/ug/accessing-fs-nfs-permissions.md "../../../efs/latest/ug/accessing-fs-nfs-permissions.md") in the _Amazon Elastic File System User Guide_.

###### Steps to set up Amazon EFS users in Transfer Family

1. Map the EFS UID and GID for your user in Transfer Family using the [`PosixProfile`](../APIReference/API_PosixProfile.md "../APIReference/API_PosixProfile.md") fields.
2. If you want the user to start in a specific folder upon login, you
   can specify the EFS directory under the [`HomeDirectory`](../APIReference/API_CreateUser.md#TransferFamily-CreateUser-request-HomeDirectory "../APIReference/API_CreateUser.md#TransferFamily-CreateUser-request-HomeDirectory") field.

You can automate the process, by using a CloudWatch rule and Lambda function. For
an example Lambda function that interacts with EFS, see [Using Amazon EFS for AWS Lambda in your serverless
applications](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications "https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications").

Additionally, you can configure logical directories for your Transfer Family users.
For details, see the [Configure logical directories for Amazon EFS](logical-dir-mappings.md#logical-dir-efs "logical-dir-mappings.md#logical-dir-efs") section in the [Using logical directories to simplify your Transfer Family
directory structures](logical-dir-mappings.md "logical-dir-mappings.md")
topic.

#### Create an Amazon EFS root user

If your organization is comfortable for you to enable root user access via
SFTP/FTPS for the configuration of your users, you can create a user who's
UID and GID are 0 (root user), then use that root user to create folders and
assign POSIX ID owners for rest of the users. The advantage of this option
is that there is no need to mount the Amazon EFS file system.

Perform the steps described in [Adding Amazon EFS service-managed users](service-managed-users.md#add-efs-user "service-managed-users.md#add-efs-user"), and for both the User ID and Group ID,
enter 0 (zero).

###### Tip

Don't let this superuser account exist for longer than necessary. Or,
if you do keep the root user account, make sure that you keep it well
protected.

### Supported Amazon EFS commands

The following commands are supported for Amazon EFS for AWS Transfer Family.

- `cd`
- `ls`/`dir`
- `pwd`
- `put`
- `get`
- `rename`
- `chown`: Only root (that is, users with uid=0) can change
  ownership and permissions of files and directories.
- `chmod`: Only root can change ownership and permissions of
  files and directories.
- `chgrp`: Supported either for root or for the file's
  owner who can only change a file's group to be one of their
  secondary groups.
- `ln -s`/`symlink`
- `mkdir`
- `rm`/`delete`
- `rmdir`
- `chmtime`
