# Lustre root squash

Root squash is an administrative feature that adds an additional layer of
file access control on top of the current network-based access control and POSIX
file permissions. Using the root squash feature, you can restrict root level access
from clients that try to access your FSx for Lustre file system as root.

Root user permissions are required to perform administrative actions,
such as managing permissions on FSx for Lustre file systems. However, root access provides
unrestricted access to the users, allowing them to bypass permission checks to access,
modify, or delete file system objects. Using the root squash feature, you can prevent
unauthorized access or deletion of data by specifying a non-root user ID (UID) and group ID
(GID) for your file system. Root users accessing the file system will automatically be
converted to the specified less-privileged user/group with limited permissions that are
set by the storage administrator.

The root squash feature also optionally allows you to provide a list of clients who are not
affected by the root squash setting. These clients can access the file system as root,
with unrestricted privileges.

###### Topics

- [How root squash works](#root-squash-overview "#root-squash-overview")
- [Managing root squash](#manage-root-squash "#manage-root-squash")

## How root squash works

The root squash feature works by re-mapping the user ID (UID) and group ID (GID)
of the root user to a UID and GID specified by the Lustre system administrator. The root
squash feature also lets you optionally specify a set of clients for which UID/GID
re-mapping does not apply.

When you create a new FSx for Lustre file system, root squash is disabled by default.
You enable root squash by configuring a UID and GID root squash setting for your
FSx for Lustre file system. The UID and GID values are integers that can range from
`0` to `4294967294`:

- A non-zero value for UID and GID enables root squash. The UID and GID
  values can be different, but each must be a non-zero value.
- A value of `0` (zero) for UID and GID indicates root,
  and therefore disables root squash.

During file system creation, you can use the Amazon FSx console to provide the
root squash UID and GID values in the **Root Squash** property, as shown
in [To enable root squash when creating a file system (console)](#create-root-squash-console "#create-root-squash-console").
You can also use the `RootSquash` parameter with the AWS CLI or API to provide
the UID and GID values, as shown
in [To enable root squash when creating a file system (CLI)](#create-root-squash-cli "#create-root-squash-cli").

Optionally, you can also specify a list of NIDs of clients for which root squash
doesn't apply. A client NID is a Lustre Network Identifier used to uniquely identify
a client. You can specify the NID as either a single address or a range of addresses:

- A single address is described in standard Lustre NID format by specifying
  the client’s IP address followed by the Lustre network ID (for example,
  `10.0.1.6@tcp`).
- An address range is described using a dash to separate the range (for example,
  `10.0.[2-10].[1-255]@tcp`).
- If you don't specify any client NIDs, there will be no exceptions to
  root squash.

When creating or updating your file system, you can use the
**Exceptions to Root Squash** property in the Amazon FSx console to provide
the list of client NIDs. In the AWS CLI or API, use the `NoSquashNids` parameter.
For more information, see the procedures
in [Managing root squash](#manage-root-squash "#manage-root-squash").

## Managing root squash

During file system creation, root squash is disabled by default. You can enable
root squash when creating a new Amazon FSx for Lustre file system from the Amazon FSx console,
AWS CLI, or API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Follow the procedure for creating a new file system described in [Step 1: Create your FSx for Lustre file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1") in the
   _Getting started_ section.
3. Open the **Root Squash - _optional_**
   section.
4. For **Root Squash**, provide the user and group IDs with which the
   root user can access the file system. You can specify any whole number in the range of
   `1`–`4294967294`:
   1. For **User ID**, specify the user ID for the
      root user to use.
   2. For **Group ID**, specify the group ID for the
      root user to use.

5. (Optional) For **Exceptions to Root Squash**, do the following:
   1. Choose **Add client address**.
   2. In the **Client addresses** field, specify the
      IP address of a client to which root squash doesn't apply, For information on the IP
      address format, see [How root squash works](#root-squash-overview "#root-squash-overview").
   3. Repeat as needed to add more client IP addresses.

6. Complete the wizard as you do when you create a new file system.
7. Choose **Review and create**.
8. Review the settings you chose for your Amazon FSx for Lustre file system, and then choose **Create
   file system**.
   When the file system is **Available**, root squash is enabled.

- To create an FSx for Lustre file system with root squash enabled, use
  the Amazon FSx CLI command [`create-file-system`](../../../cli/latest/reference/fsx/create-file-system.md "../../../cli/latest/reference/fsx/create-file-system.md") with the `RootSquashConfiguration`
  parameter. The corresponding API operation is
  [CreateFileSystem](../APIReference/API_CreateFileSystem.md "../APIReference/API_CreateFileSystem.md").

For the `RootSquashConfiguration` parameter, set the following options:

    + `RootSquash` – The colon-separated UID:GID values that specify
     the user ID and group ID for the root user to use. You can specify any whole number in the range
     of `0`–`4294967294` (0 is root) for each ID (for example,
     `65534:65534`).
    + `NoSquashNids` – Specify the Lustre Network Identifiers (NIDs)
     of clients to which root squash doesn't apply. For information on the client NID format,
     see [How root squash works](#root-squash-overview "#root-squash-overview").

The following example creates an FSx for Lustre file system with root squash enabled:

```
`$` aws fsx create-file-system \
      --client-request-token CRT1234 \
      --file-system-type LUSTRE \
      --file-system-type-version 2.15 \
      --lustre-configuration "DeploymentType=PERSISTENT_2,PerUnitStorageThroughput=250,DataCompressionType=LZ4,\
          RootSquashConfiguration={RootSquash="65534:65534",\
          NoSquashNids=["10.216.123.47@tcp", "10.216.12.176@tcp"]}" \
      --storage-capacity 2400 \
      --subnet-ids subnet-123456 \
      --tags Key=Name,Value=Lustre-TEST-1 \
      --region us-east-2
```

After successfully creating the file system, Amazon FSx returns the file system description
as JSON, as shown in the following example.

```
{

    "FileSystems": [
        {
            "OwnerId": "111122223333",
            "CreationTime": 1549310341.483,
            "FileSystemId": "fs-0123456789abcdef0",
            "FileSystemType": "LUSTRE",
            "FileSystemTypeVersion": "2.15",
            "Lifecycle": "CREATING",
            "StorageCapacity": 2400,
            "VpcId": "vpc-123456",
            "SubnetIds": [
                "subnet-123456"
            ],
            "NetworkInterfaceIds": [
                "eni-039fcf55123456789"
            ],
            "DNSName": "fs-0123456789abcdef0.fsx.us-east-2.amazonaws.com",
            "ResourceARN": "arn:aws:fsx:us-east-2:123456:file-system/fs-0123456789abcdef0",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Lustre-TEST-1"
                }
            ],
            "LustreConfiguration": {
                "DeploymentType": "PERSISTENT_2",
                "DataCompressionType": "LZ4",
                "PerUnitStorageThroughput": 250,
                "RootSquashConfiguration": {
                    "RootSquash": "65534:65534",
                    "NoSquashNids": "10.216.123.47@tcp 10.216.29.176@tcp"
            }
        }
    ]
}
```

You can also update the root squash settings of your existing file system
using the Amazon FSx console, AWS CLI, or API. For example, you can change the
root squash UID and GID values, add or remove client NIDs, or disable root squash.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems**, and choose the Lustre file system that you want
   to manage root squash for.
3. For **Actions**, choose **Update root squash**.
   Or, in the **Summary** panel, choose **Update** next to the file
   system's **Root Squash** field to display the **Update Root Squash Settings**
   dialog box.
4. For **Root Squash**, update the user and group IDs with which the
   root user can access the file system. You can specify any whole number in the range of
   `0`–`4294967294`. To disable root squash, specify
   `0` (zero) for both IDs.
   1. For **User ID**, specify the user ID for the
      root user to use.
   2. For **Group ID**, specify the group ID for the
      root user to use.

5. For **Exceptions to Root Squash**, do the following:
   1. Choose **Add client address**.
   2. In the **Client addresses** field, specify the
      IP address of a client to which root squash doesn't apply,
   3. Repeat as needed to add more client IP addresses.

6. Choose **Update**.

###### Note

If root squash is enabled and you want to disable it, choose
**Disable** instead of performing steps 4-6.
You can monitor the update progress on the file systems detail page in
the **Updates** tab.

To update the root squash settings for an existing FSx for Lustre file system, use the AWS CLI command
[update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md").
The corresponding API operation is
[UpdateFileSystem](../APIReference/API_UdateFileSystem.md "../APIReference/API_UdateFileSystem.md").

Set the following parameters:

- Set `--file-system-id` to the ID of the file system that you are
  updating.
- Set the `--lustre-configuration RootSquashConfiguration` options
  as follows:

      + `RootSquash` – Set the colon-separated UID:GID values that specify
       the user ID and group ID for the root user to use. You can specify any whole number in the range
       of `0`–`4294967294` (0 is root) for each ID. To disable root
       squash, specify `0:0` for the UID:GID values.
      + `NoSquashNids` – Specify the Lustre Network Identifiers (NIDs)
       of clients to which root squash doesn't apply. Use `[]` to remove all client NIDs,
       which means there will be no exceptions to root squash.

  This command specifies that root squash is enabled using `65534` as the value
  for the root user's user ID and group ID.

```
$ aws fsx update-file-system \
    --file-system-id fs-0123456789abcdef0 \
    --lustre-configuration RootSquashConfiguration={RootSquash="65534:65534", \
          NoSquashNids=["10.216.123.47@tcp", "10.216.12.176@tcp"]}
```

If the command is successful, Amazon FSx for Lustre returns the response in JSON format.

You can view the root squash settings of your file system in the **Summary**
panel of the file system details page on the Amazon FSx console or in the response of a
[`describe-file-systems`](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") CLI command
(the equivalent API action is [`DescribeFileSystems`](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md")).
