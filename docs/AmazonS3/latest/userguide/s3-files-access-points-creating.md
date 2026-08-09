# Creating access points for an S3 file system

Access points are application-specific entry points to a file system that simplify
managing data access at scale for shared datasets. You can use access points to enforce user
identities and permissions for all file system requests that are made through the access
point. Additionally, access points can restrict clients to only access data within a
specified root directory and its subdirectories. When you create a file system using the
AWS Management Console, S3 Files automatically creates one access point for the file
system.

A file system can have a maximum of 25,000 access points. For more information, see
[Unsupported features, limits, and quotas](s3-files-quotas.md "s3-files-quotas.md"). You can create access
points using the Amazon S3 console, AWS CLI, or AWS SDK.

Access points for an S3 file system cannot be edited after creation. If you want to make
updates, you have to delete the existing access point and create a new one.

This section explains how to use the Amazon S3 console to create an access point
for an S3 file system.

1. Sign in to the AWS Management Console and open the Amazon S3
   console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar, verify you are in the
   AWS Region of the file system for which you want to create an access
   point.
3. In the left navigation pane, choose **File
   systems**.
4. Choose your desired file system.
5. Select the **Access points** tab and
   select **Create access
   point**.
6. On the Create page, enter a **Name**
   for the access point.
7. (Optional) Specify a root directory path for the access point.
   Clients using this access point will be limited to this directory and its
   subdirectories. By default, S3 Files assumes the root directory for the
   access point to be the root directory of the file system.
8. (Optional) In the **POSIX user** panel, you
   can specify the full POSIX identity to use to enforce user and group
   information for all file operations by clients that are using the access
   point.

   - **User ID** – Enter a numeric
     POSIX user ID for the user.
   - **Group ID** – Enter a numeric
     POSIX group ID for the user.
   - **Secondary group IDs** – Enter
     an optional comma-separated list of secondary group
     IDs.

9. (Optional) For **Root directory creation
   permissions**, you can specify the permissions to use when S3
   Files creates the root directory path, if specified and the root directory
   doesn't already exist.

###### Note

If you don't specify any root directory ownership and permissions, and
the root directory does not already exist, S3 Files will not create the
root directory. Any attempts to mount the file system by using the access
point will fail.

    * **Owner user ID** – Enter the
     numeric POSIX user ID to use as the root directory
     owner.
    * **Owner group ID** – Enter the
     numeric POSIX group ID to use as the root directory owner
     group.
    * **Permissions** – Enter the Unix
     mode of the directory. A common configuration is 755. Ensure that the
     execute bit is set for the access point user so that they are able to
     mount.

10. (Optional) Under **Tags**, you can
choose to add tags to your access point. 11. Choose **Create access
point**.
The following `create-access-point` example command shows how you can
use the AWS CLI to create an access point for an S3 file system.

```
aws s3files create-access-point --file-system-id `file-system-id` --root-directory `root-directory` --posix-user `posix-user`
```

For example:

```
aws s3files create-access-point --file-system-id fs-abcdef0123456789a --client-token 010102020-3 \
  --root-directory "Path=/s3files/mobileapp/east,CreationInfo={OwnerUid=0,OwnerGid=11,Permissions=775}" \
  --posix-user "Uid=22,Gid=4" \
  --tags Key=Name,Value=east-users
```

###### Note

If multiple requests to create access points on the same file system are sent
in quick succession, and the file system is nearing the access points limit, you
may experience a throttling response for these requests. This is to ensure that
the file system does not exceed the access point quota.
