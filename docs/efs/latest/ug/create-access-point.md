# Creating access points

You can create and delete Amazon EFS access points using the AWS Management Console, the AWS Command Line Interface (AWS CLI),
and the Amazon EFS API and SDKs. You cannot modify an access point once it is created. A file
system can have a maximum of 10,000 access points unless you request an increase.

###### Note

If multiple requests to create access points on the same file system are sent in quick
succession, and the file system is nearing the access points limit, you may experience a
throttling response for these requests. This is to ensure that the file system does not
exceed the stated access point quota.

For more information about EFS access points, see [Working with access points](efs-access-points.md "efs-access-points.md").

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Choose **Access points** to open the **Access points**
   window.
3. Choose **Create access point** to display the **Create access
   point** page.

You can also open the **Create access point** page by choosing
**File Systems**. Choose a file system **Name** or
**File system ID** and then choose **Access
points** and **Create access point** to create an access point
for that file system.

    1. Enter the following information in the **Details** panel:




    	* **File system** – Enter a file system name or ID and choose the
    	 matching file system. You can also choose the file system from the list that
    	 appears when you choose the input field.
    	* (Optional) **Name** – Enter a name for the access point.
    	* (Optional) **Root directory path** – You can specify a root directory
    	 for the access point; the default access point root is /. To enter a root
    	 directory path, use the format `/foo/bar`. For more
    	 information, see [Enforcing a root directory with an access point](enforce-root-directory-access-point.md "enforce-root-directory-access-point.md").
    2. (Optional) In the **POSIX user** panel, you can specify the full
     POSIX identity to use to enforce user and group information for all file
     operations by NFS clients that are using the access point. For more information,
     see [Enforcing a user identity using an access point](enforce-identity-access-points.md "enforce-identity-access-points.md").




    	* **User ID** – Enter a numeric POSIX user ID for the user.
    	* **Group ID** – Enter a numeric POSIX group ID for the user.
    	* **Secondary group IDs** – Enter an optional comma-separated list of
    	 secondary group IDs.
    3. (Optional) For **Root directory creation permissions**, you can
     specify the permissions to use when Amazon EFS creates the root directory path, if
     specified and the root directory doesn't already exist. For more information,
     see [Enforcing a root directory with an access point](enforce-root-directory-access-point.md "enforce-root-directory-access-point.md").


    ###### Note

    If you don't specify any root directory ownership and permissions, and the root directory does
     not already exist, EFS will not create the root directory. Any
     attempts to mount the file system by using the access point will fail.




    	* **Owner user ID** – Enter the numeric POSIX user ID to use as the root
    	 directory owner.
    	* **Owner group ID** – Enter the numeric POSIX group ID to use as the
    	 root directory owner group.
    	* **Permissions** – Enter the Unix mode of the directory. A common
    	 configuration is 755. Ensure that the execute bit is set for the access point
    	 user so that they are able to mount.

4. Choose **Create access point** to create the access point by
   using this configuration.
   In the following example, the `create-access-point` CLI command creates an
   access point for an EFS file system. The equivalent API command is [CreateAccessPoint](API_CreateAccessPoint.md "API_CreateAccessPoint.md").

```
aws efs create-access-point --file-system-id fs-abcdef0123456789a --client-token 010102020-3 \
--root-directory “Path=/efs/mobileapp/east,CreationInfo={OwnerUid=0,OwnerGid=11,Permissions=775}” \
--posix-user “Uid=22,Gid=4” \
--tags Key=Name,Value=east-users
```

If the request is successful, the CLI responds with the access point description.

```
`{
 "ClientToken": "010102020-3",
 "Name": "east-users",
 "AccessPointId": "fsap-abcd1234ef5678901",
 "AccessPointArn": "arn:aws:elasticfilesystem:us-east-2:111122223333:access-point/fsap-abcd1234ef5678901",
 "FileSystemId": "fs-01234567",
 "LifeCycleState": "creating",
 "OwnerId": "111122223333",
 "PosixUser": {
 "Gid": 4,
 "Uid": 22
 },
 "RootDirectory": {
 "CreationInfo": {
 "OwnerGid": 0,
 "OwnerUid": 11,
 "Permissions": "775"
 },
 "Path": "/efs/mobileapp/east",
 },
 "Tags": []
}`
```

###### Note

If multiple requests to create access points on the same file system are sent in quick
succession, and the file system is nearing the access points limit, you may
experience a throttling response for these requests. This is to ensure that the file
system does not exceed the stated access point quota.
