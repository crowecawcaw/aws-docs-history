# Network File System (NFS) level users, groups, and permissions

After creating a file system, by default only the root user (UID 0) has read, write, and
execute permissions. For other users to modify the file system, the root user must explicitly
grant them access. You can use access points to automate the creation of directories that a
nonroot user can write from. For more information, see [Working with access points](efs-access-points.md "efs-access-points.md").

EFS file system objects have a Unix-style mode associated with them. This mode value
defines the permissions for performing actions on that object. Users familiar with Unix-style
systems can easily understand how Amazon EFS behaves with respect to these permissions.

Additionally, on Unix-style systems, users and groups are mapped to numeric identifiers,
which Amazon EFS uses to represent file ownership. For Amazon EFS, file system objects (that is, files,
directories, and so on) are owned by a single owner and a single group. Amazon EFS uses the mapped
numeric IDs to check permissions when a user attempts to access a file system object.

###### Note

The NFS protocol supports a maximum of 16 group IDs (GIDs) per user and any additional GIDs are
truncated from NFS client requests. For more information, see [Access denied to allowed files on NFS file system](troubleshooting-efs-general.md#nfs-16-group-limit "troubleshooting-efs-general.md#nfs-16-group-limit").

Following, you can find examples of permissions and a discussion about NFS permissions
considerations for Amazon EFS.

###### Topics

- [File and directory permissions](user-and-group-permissions.md "user-and-group-permissions.md")
- [Example EFS file system use cases
  and permissions](#accessing-fs-nfs-permissions-ex-scenarios "#accessing-fs-nfs-permissions-ex-scenarios")
- [User and group ID permissions for files
  and directories within a file system](#accessing-fs-nfs-permissions-uid-gid "#accessing-fs-nfs-permissions-uid-gid")
- [No root squashing](#accessing-fs-nfs-permissions-root-user "#accessing-fs-nfs-permissions-root-user")
- [Permissions caching](#accessing-fs-nfs-permissions-caching "#accessing-fs-nfs-permissions-caching")
- [Changing file system object
  ownership](#accessing-fs-nfs-permissions-chown-restricted "#accessing-fs-nfs-permissions-chown-restricted")
- [EFS access points](#accessing-fs-nfs-permissions-access-points "#accessing-fs-nfs-permissions-access-points")

## Example EFS file system use cases

and permissions

After you create an EFS file system and mount targets for the file system in your VPC,
you can mount the remote file system locally on your Amazon EC2 instance. The `mount`
command can mount any directory in the file system. However, when you first create the file
system, there is only one root directory at `/`. The root user and root group
own the mounted directory.

The following `mount` command mounts the root directory of an Amazon EFS file
system, identified by the file system DNS name, on the `/efs-mount-point` local
directory.

```
sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport `file-system-id`.efs.aws-region.amazonaws.com:/ efs-mount-point
```

The initial permissions mode allows:

- `read-write-execute` permissions to the owner
  _root_
- `read-execute` permissions to the group _root_
- `read-execute` permissions to others

Only the root user can modify this directory. The root user can also grant other users
permissions to write to this directory, for example:

- Create writable per-user subdirectories. For step-by-step instructions, see [Tutorial: Creating writable
  per-user subdirectories](accessing-fs-nfs-permissions-per-user-subdirs.md "accessing-fs-nfs-permissions-per-user-subdirs.md").
- Allow users to write to the EFS file system root. A user with root privileges can
  grant other users access to the file system.
  - To change the EFS file system ownership to a non-_root_
    user and group, use the following:

  ```
  $ sudo chown `user`:`group` /`EFSroot`
  ```

  - To change permissions of the file system to something more permissive, use the
    following:

  ```
  $ sudo chmod 777 /`EFSroot`
  ```

  This command grants read-write-execute privileges to all users on all EC2
  instances that have the file system mounted.

## User and group ID permissions for files

and directories within a file system

Files and directories in an EFS file system support standard Unix-style read, write,
and execute permissions based on the user ID and group IDs. When an NFS client mounts an EFS
file system without using an access point, the user ID and group ID provided by the client
is trusted. You can use EFS access points to override user ID and group IDs used by the NFS
client. When users attempt to access files and directories, Amazon EFS checks their user IDs and
group IDs to verify that each user has permission to access the objects. Amazon EFS also uses
these IDs to indicate the owner and group owner for new files and directories that the user
creates. Amazon EFS doesn't examine user or group names—it only uses the numeric
identifiers.

###### Note

When you create a user on an EC2 instance, you can assign any numeric user ID (UID)
and group ID (GID) to the user. The numeric user IDs are set in the
`/etc/passwd` file on Linux systems. The numeric group IDs are in the
`/etc/group` file. These files define the mappings between names and IDs.
Outside of the EC2 instance, Amazon EFS doesn't perform any authentication of these IDs,
including the root ID of 0.

If a user accesses an EFS file system from two different EC2 instances, depending on
whether the UID for the user is the same or different on those instances you see different
behavior, as follows:

- If the user IDs are the same on both EC2 instances, Amazon EFS considers them to indicate
  the same user, regardless of the EC2 instance used. The user experience when accessing
  the file system is the same from both EC2 instances.
- If the user IDs aren't the same on both EC2 instances, Amazon EFS considers the
  users to be different users. The user experience isn't the same when accessing the
  EFS file system from the two different EC2 instances.
- If two different users on different EC2 instances share an ID, Amazon EFS considers them
  to be the same user.

You might consider managing user ID mappings across EC2 instances consistently. Users
can check their numeric ID using the `id` command.

```
$ id

uid=502(joe) gid=502(joe) groups=502(joe)
```

### Turn Off the ID Mapper

The NFS utilities in the operating system include a daemon called an ID Mapper that
manages mapping between user names and IDs. In Amazon Linux, the daemon is called
`rpc.idmapd` and on Ubuntu is called `idmapd`. It translates user
and group IDs into names, and vice versa. However, Amazon EFS deals only with numeric IDs. We
recommend that you turn this process off on your EC2 instances. On Amazon Linux, the ID
mapper is usually disabled, and if it is don't enable it. To turn off the ID mapper, use
the commands shown following.

```
$  service rpcidmapd status
$  sudo service rpcidmapd stop
```

## No root squashing

By default, root squashing is disabled on EFS file systems. Amazon EFS behaves like a
Linux NFS server with `no_root_squash`. If a user or
group ID is 0, Amazon EFS treats that user as the `root` user, and bypasses
permissions checks (allowing access and modification to all file system objects).
Root squashing can be enabled on a client connection when the AWS Identity and Access Management (AWS IAM)
identity or resource policy does not allow access to the `ClientRootAccess` action.
When root squashing is enabled, the root user is converted to a user with limited permissions on the NFS server.

For more information, see [Using IAM to control access to file
systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md").

### Enable root squashing using IAM authorization for NFS clients

You can configure Amazon EFS to prevent root access to your EFS file system for
all AWS principals except for a single management workstation. You do this by configuring
AWS Identity and Access Management (IAM) authorization for Network File System (NFS) clients.

To do this requires configuring two IAM permissions policies, as follows:

- Create an EFS file system policy that explicitly allows read and write access to the
  file system, and implicitly denies root access.
- Assign an IAM identity to the Amazon EC2 management workstation that requires root access
  to the file system by using an EC2 instance profile. For more information about Amazon EC2
  instance profiles, see [Use
  instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") in the _AWS Identity and Access Management User Guide_.
- Assign the `AmazonElasticFileSystemClientFullAccess` AWS managed policy to
  the IAM role of the management workstation. For more information about AWS managed policies
  for Amazon EFS, see [Identity and access management for Amazon EFS](security-iam.md "security-iam.md").

To enable root squashing using IAM authorization for NFS clients, use the following
procedures.

###### To prevent root access to the file system

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Choose **File systems**.
3. Choose the file system that you want to enable
   root squashing on.
4. On the file system details page, choose **File system policy**, and
   then choose **Edit**. The **File system policy** page
   appears.
5. Choose **Prevent root access by default\*** under **Policy
   options**. The policy JSON object appears in the **Policy
   editor**.
6. Choose **Save** to save the file system policy.

Clients that aren't anonymous can get root access to the file system through an
identity-based policy. When you attach the `AmazonElasticFileSystemClientFullAccess`
managed policy to the workstation's role, IAM grants root access to the workstation based
on its identity policy.

###### To enable root access from the management workstation

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Create a role for Amazon EC2 called `EFS-client-root-access`. IAM creates an instance profile with the same name as the EC2 role you created.
3. Assign the AWS managed policy `AmazonElasticFileSystemClientFullAccess` to the EC2 role you created. The contents of this policy is shown following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:ClientMount",
 "elasticfilesystem:ClientRootAccess",
 "elasticfilesystem:ClientWrite",
 "elasticfilesystem:DescribeMountTargets"
 ],
 "Resource": "*"
 }
 ]
}`

```

4. Attach the instance profile to the EC2 instance that you are using as the management
   workstation, as described following. For more information, see [Attaching an
   IAM Role to an Instance](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role") in the _Amazon EC2 User Guide for Linux
   Instances_.
   1. Open the Amazon EC2 console at
      [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
   2. In the navigation pane, choose **Instances**.
   3. Choose the instance. For **Actions**, choose **Instance
      Settings**, and then choose **Attach/Replace IAM
      role**.
   4. Choose the IAM role that you created in the first step, `EFS-client-root-access`,
      and choose **Apply**.

5. Install the EFS mount helper on the management workstation. For more information about the EFS mount helper
   mount helper and the amazon-efs-utils package, see [Installing the Amazon EFS client](using-amazon-efs-utils.md "using-amazon-efs-utils.md").
6. Mount the EFS file system on the management workstation by using the following command with
   the `iam` mount option.

```
`$` sudo mount -t efs -o tls,iam `file-system-id`:/ `efs-mount-point`
```

You can configure the Amazon EC2 instance to automatically mount the file system with IAM
authorization. For more information about mounting an EFS file system with IAM
authorization, see [Mounting with IAM authorization](mounting-IAM-option.md "mounting-IAM-option.md").

## Permissions caching

Amazon EFS caches file permissions for a small time period. As a result, there might be a
brief window where a user whose access was revoked recently can still access that object.

## Changing file system object

ownership

Amazon EFS enforces the POSIX `chown_restricted` attribute. This means only the
root user can change the owner of a file system object. The root or the owner user can
change the owner group of a file system object. However, unless the user is root, the group
can only be changed to one that the owner user is a member of.

## EFS access points

An _access point_ applies an operating system user,
group, and file system path to any file system request made using the access point. The
access point's operating system user and group override any identity information provided by
the NFS client. The file system path is exposed to the client as the access point's root
directory. This approach ensures that each application always uses the correct operating
system identity and the correct directory when accessing shared file-based datasets.
Applications using the access point can only access data in its own directory and below. For
more information about access points, see [Working with access points](efs-access-points.md "efs-access-points.md").
