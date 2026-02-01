# Access your FSx for NetApp ONTAP file systems with Transfer Family

###### Contents

- [Overview](fsx-s3-access-points.md#fsx-overview "fsx-s3-access-points.md#fsx-overview")
- [Prerequisites](fsx-s3-access-points.md#fsx-prerequisites "fsx-s3-access-points.md#fsx-prerequisites")
  - [FSx for NetApp ONTAP requirements](fsx-s3-access-points.md#fsx-ontap-requirements "fsx-s3-access-points.md#fsx-ontap-requirements")
  - [Required IAM permissions](fsx-s3-access-points.md#required-iam-permissions "fsx-s3-access-points.md#required-iam-permissions")

- [How FSx storage works with Transfer Family](fsx-s3-access-points.md#how-fsx-storage-works "fsx-s3-access-points.md#how-fsx-storage-works")
  - [File system user identity](fsx-s3-access-points.md#file-system-user-identity "fsx-s3-access-points.md#file-system-user-identity")

- [Creating an S3 access point for FSx](fsx-s3-access-points.md#creating-s3-access-point "fsx-s3-access-points.md#creating-s3-access-point")
  - [Access point naming](fsx-s3-access-points.md#access-point-naming "fsx-s3-access-points.md#access-point-naming")
  - [Creating an access point for FSx for NetApp ONTAP](fsx-s3-access-points.md#creating-access-point-ontap "fsx-s3-access-points.md#creating-access-point-ontap")
  - [Configuring file system permissions](fsx-s3-access-points.md#configuring-file-system-permissions "fsx-s3-access-points.md#configuring-file-system-permissions")

- [Using S3 access point aliases with FSx](fsx-s3-access-points.md#using-s3-access-point-aliases "fsx-s3-access-points.md#using-s3-access-point-aliases")
  - [About access point aliases](fsx-s3-access-points.md#about-access-point-aliases "fsx-s3-access-points.md#about-access-point-aliases")
  - [Finding your access point alias](fsx-s3-access-points.md#finding-access-point-alias "fsx-s3-access-points.md#finding-access-point-alias")

- [Configuring Transfer Family for FSx storage](fsx-s3-access-points.md#configuring-transfer-family-fsx "fsx-s3-access-points.md#configuring-transfer-family-fsx")
  - [Creating an IAM role](fsx-s3-access-points.md#creating-iam-role-fsx "fsx-s3-access-points.md#creating-iam-role-fsx")

- [Managing users for FSx storage](fsx-s3-access-points.md#managing-users-fsx "fsx-s3-access-points.md#managing-users-fsx")
  - [Creating a user](fsx-s3-access-points.md#creating-user-fsx "fsx-s3-access-points.md#creating-user-fsx")
  - [Configuring multiple directory mappings](fsx-s3-access-points.md#multiple-directory-mappings "fsx-s3-access-points.md#multiple-directory-mappings")

- [Configuring file transfer clients](fsx-s3-access-points.md#configuring-file-transfer-clients "fsx-s3-access-points.md#configuring-file-transfer-clients")
  - [WinSCP configuration](fsx-s3-access-points.md#winscp-configuration "fsx-s3-access-points.md#winscp-configuration")
  - [Other SFTP clients](fsx-s3-access-points.md#other-sftp-clients "fsx-s3-access-points.md#other-sftp-clients")

- [Troubleshooting FSx storage](fsx-s3-access-points.md#troubleshooting-fsx-storage "fsx-s3-access-points.md#troubleshooting-fsx-storage")
  - [File operation issues](fsx-s3-access-points.md#file-operation-issues "fsx-s3-access-points.md#file-operation-issues")

## Overview

Transfer Family supports Amazon FSx for NetApp ONTAP through S3 access points. Amazon FSx for NetApp ONTAP is a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp's popular ONTAP file system. When you configure Transfer Family with an FSx file system, your users connect to Transfer Family endpoints using standard file transfer clients. Transfer Family routes file operations through an S3 access point attached to your FSx volume, while your data remains on the FSx file system. To learn more about FSx for NetApp ONTAP, see [What is Amazon FSx for NetApp ONTAP?](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md")

This integration enables you to:

- Transfer files using SFTP, FTPS, or FTP protocols to enterprise-grade file storage
- Access the same data through multiple protocols (SFTP, NFS, SMB)
- Use FSx features such as snapshots, backups, and data tiering

###### Important

Some file operations are not supported when using FSx file systems with Transfer Family, including rename and append operations. For upload operations, file sizes are limited to 5 GB. For a complete list of limitations, see [Access point compatibility](../../../fsx/latest/ONTAPGuide/access-points-for-fsxn-object-api-support.md "../../../fsx/latest/ONTAPGuide/access-points-for-fsxn-object-api-support.md").

## Prerequisites

Before you configure Transfer Family with Amazon FSx, you must meet the following requirements.

### FSx for NetApp ONTAP requirements

To use FSx for NetApp ONTAP with Transfer Family, you need:

- An FSx for NetApp ONTAP file system running ONTAP version 9.17.1 or later
- The file system and S3 access point in the same AWS Region
- The same AWS account owning both the file system and access point

To learn more, see [Getting started with Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/getting-started.md "../../../fsx/latest/ONTAPGuide/getting-started.md").

### Required IAM permissions

You can configure each S3 access point with distinct permissions and network controls that S3 applies for any request that is made using that access point. S3 access points support IAM resource policies that you can use to control the use of the access point by resource, user, or other conditions. For an application or user to access files through an access point, both the access point and the underlying volume must permit the request. For more information, see [IAM access point policies](../../../fsx/latest/ONTAPGuide/s3-ap-manage-access-fsxn.md "../../../fsx/latest/ONTAPGuide/s3-ap-manage-access-fsxn.md").

Amazon S3 access points for FSx use a dual-layer authorization model that combines IAM permissions with file system-level permissions. This approach ensures that data access requests are properly authorized at both the AWS service level and the underlying file system level.

For an application or user to successfully access data through an access point, both the S3 access point policy and the underlying FSx volume must permit the request.

To create and configure this integration, you need the following permissions:

- `fsx:CreateAndAttachS3AccessPoint`
- `s3:CreateAccessPoint`
- `s3:GetAccessPoint`
- `s3:PutAccessPointPolicy` (if creating an optional access point policy)

## How FSx storage works with Transfer Family

When you configure Transfer Family with an FSx file system, the following components work together to enable file transfers:

1. A user connects to the Transfer Family server using an SFTP, FTPS, or FTP client.
2. Transfer Family authenticates the user using service-managed identities, a custom identity provider, or AWS Directory Service for Microsoft Active Directory. Once authenticated, Transfer Family assumes the IAM role associated with the user.
3. For each file operation, Transfer Family acts as a standard S3 API client, making requests to the S3 Access Point using the assumed IAM role of the user and verifies permissions against the S3 access point policy.
4. The FSx file system verifies that the file system user associated with the access point has permission to perform the requested operation. The file operation is then performed on the FSx volume.

For a file operation to succeed, both authorization layers must permit the request.

###### Note

Attaching an S3 access point to an FSx volume does not change how the volume behaves when accessed directly through NFS or SMB. Existing file protocol access continues to work unchanged.

### File system user identity

Each access point uses a file system user identity that you specify when creating the access point. This identity authorizes all file access requests made through that access point. The file system user is a user account on the underlying Amazon FSx file system. If the file system user has read-only access, then only read requests made using the access point are authorized, and write requests are blocked. If the file system user has read-write access, then both read and write requests to the attached volume made using the access point are authorized.

## Creating an S3 access point for FSx

Before you configure Transfer Family, you must create an S3 access point attached to your FSx volume. S3 access points are named network endpoints that are attached to a data source such as a bucket or Amazon FSx for ONTAP volume. You can create and attach an access point to an FSx for NetApp ONTAP using the Amazon FSx console, AWS CLI, or API. Once attached, you can use the S3 object APIs to access your file data. Your data continues to reside on the Amazon FSx file system and continues to be directly accessible for your existing workloads. You continue to manage your storage using all the FSx for NetApp ONTAP storage management capabilities, including backups, snapshots, user and group quotas, and compression.

For more information, see [Creating access points](../../../fsx/latest/ONTAPGuide/create-access-points.md "../../../fsx/latest/ONTAPGuide/create-access-points.md").

### Access point naming

When you name your access point, follow these guidelines:

- Access point names must be unique within your AWS account and Region.
- Names cannot end with `-ext-s3alias` (reserved for aliases).
- Avoid including sensitive information in names because they are published in DNS.

For a full list of naming rules, see [Access points naming rules, restrictions, and limitations](../../../fsx/latest/ONTAPGuide/access-point-for-fsxn-restrictions-limitations-naming-rules.md "../../../fsx/latest/ONTAPGuide/access-point-for-fsxn-restrictions-limitations-naming-rules.md").

### Creating an access point for FSx for NetApp ONTAP

Use the following procedure to create an S3 access point for an FSx for NetApp ONTAP volume.

###### To create an access point (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the navigation pane, choose **File systems**.
3. Choose your FSx for NetApp ONTAP file system.
4. Choose the **Volumes** tab.
5. Select the volume that you want to attach.
6. For **Actions**, choose **Create S3 access point**.
7. For **Access point name**, enter a descriptive name (for example, `transfer-family-ap`).
8. For **File system user identity type**, choose one of the following:
   - **UNIX identity** - For volumes with UNIX security style
   - **Windows identity** - For volumes with NTFS security style

9. (Optional) For **Access point policy**, enter an IAM policy that defines which IAM principals can perform which operations on objects accessed through this access point. For more information, see [Managing access point access](../../../fsx/latest/ONTAPGuide/s3-ap-manage-access-fsxn.md "../../../fsx/latest/ONTAPGuide/s3-ap-manage-access-fsxn.md").
10. Choose **Create**.
11. After creation, note the access point alias for use in Transfer Family configuration.

###### Note

When AWS Transfer Family accesses S3 resources on behalf of your connected SFTP/FTPS users, requests originate from AWS Transfer Family infrastructure, not from your VPC. Because of this, S3 Access Points configured with a VPC network origin will deny these requests. However, even if you use an Access Point configured with an Internet network origin, all traffic between Transfer Family and the Access Point remains private and travels over the AWS backbone network - it does not traverse the public internet.

### Configuring file system permissions

The file system user that you specify determines what operations Transfer Family users can perform. You must configure appropriate permissions on your FSx volume.

**UNIX example:**

```
# Create a directory for Transfer Family users
mkdir -p /vol1/transfer-users

# Set ownership to match the access point user
chown 1001:1001 /vol1/transfer-users

# Set permissions
chmod 755 /vol1/transfer-users
```

**Windows example:**

```
# Create a directory for Transfer Family users
New-Item -Path "D:\vol1\transfer-users" -ItemType Directory

# Set permissions for the file system user associated with the access point
# Replace DOMAIN\TransferUser with your Windows user identity
icacls "D:\vol1\transfer-users" /grant "DOMAIN\TransferUser:(OI)(CI)M" /T

# Verify permissions
icacls "D:\vol1\transfer-users"
```

## Using S3 access point aliases with FSx

When you use FSx file systems with Transfer Family, you must use S3 access point aliases. Transfer Family does not support using access point ARNs or other reference methods for FSx storage.

###### Important

AWS Transfer Family only supports S3 access point aliases when using FSx file systems. You cannot use access point ARNs or virtual-hosted-style URIs.

###### Important

The access point must be in the same Region as the volume.

### About access point aliases

When you create an S3 access point attached to an FSx volume, Amazon S3 automatically generates an access point alias. This alias is a unique identifier that you can use anywhere you use an S3 bucket name.

For access points attached to FSx volumes, the alias uses the following format:

```
access-point-name-metadata-ext-s3alias
```

**Example alias:**

```
my-fsx-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias
```

###### Note

The `-ext-s3alias` suffix is reserved for FSx access point aliases. You cannot use this suffix in access point names.

### Finding your access point alias

You can find the access point alias after creating the access point.

###### To find the access point alias (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the navigation pane, choose **File systems**.
3. Choose your file system.
4. Choose the **Volumes** tab and select the volume you created the access point for.
5. Go to **S3 access point details** column.
6. The alias is displayed in the **Alias** column.

**To find the access point alias (CLI)**

Use the `describe-s3-access-point-attachments` command.

```
aws fsx describe-s3-access-point-attachments \
    --filters Name=file-system-id,Values=fs-0123456789abcdef0
```

The response includes the alias:

```
{
    "S3AccessPointAttachments": [
        {
            "S3AccessPoint": {
                "ResourceARN": "arn:aws:s3:us-east-1:111122223333:accesspoint/my-fsx-ap",
                "Alias": "my-fsx-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias"
            }
        }
    ]
}
```

When you configure Transfer Family users, use the access point alias in home directory mappings.

**Home directory format:**

```
/access-point-alias/path/to/directory
```

**Example:**

```
/my-fsx-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias/users/jsmith
```

## Configuring Transfer Family for FSx storage

After you create the S3 access point, configure a Transfer Family server to use it.

### Creating an IAM role

You must create an IAM role that grants Transfer Family access to the S3 access point.

###### Note

In the IAM policy, use the access point alias where you would normally specify a bucket name.

###### To create the IAM role

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, then choose **Create role**.
3. For **Trusted entity type**, choose **AWS service**.
4. For **Use case**, choose **Transfer**.
5. Choose **Next**.
6. Choose **Create policy** and enter your policy (see sample policy below).
7. Attach the policy to the role and choose **Create role**.

**Example IAM policy:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowFileOperations",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:GetObjectTagging",
                "s3:PutObjectTagging"
            ],
            "Resource": "arn:aws:s3:us-east-2:111122223333:accesspoint/my-fsx-ap/object/*"
        },
        {
            "Sid": "AllowDirectoryOperations",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:us-east-2:111122223333:accesspoint/my-fsx-ap"
        }
    ]
}
```

## Managing users for FSx storage

Create Transfer Family users with home directory mappings that use the S3 access point alias.

### Creating a user

When you create a user for FSx storage, use the access point alias in home directory mappings.

###### To create a Service Managed user (console)

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the navigation pane, choose **Servers**.
3. Choose your server.
4. In the Users section, choose **Add user**.
5. For **Username**, enter a username.
6. For **Role**, choose the IAM role that you created.
7. For **Home directory**, choose **Restricted**.
8. For **Home directory mappings**, add a mapping using the access point alias:

```
[{"Entry": "/", "Target": "/my-fsx-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias/users/jsmith"}]
```

**To create a user (CLI)**

Use the `create-user` command. Replace the access point alias with your alias.

```
aws transfer create-user \
    --server-id s-0123456789abcdef0 \
    --user-name jsmith \
    --role arn:aws:iam::111122223333:role/TransferFamilyFSxRole \
    --home-directory-type LOGICAL \
    --home-directory-mappings '[
        {
            "Entry": "/",
            "Target": "/my-fsx-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias/users/jsmith"
        }
    ]'
```

### Configuring multiple directory mappings

You can map multiple virtual directories to different paths on the FSx volume.

**Example: Separate upload and download directories**

```
aws transfer create-user \
    --server-id s-0123456789abcdef0 \
    --user-name jsmith \
    --role arn:aws:iam::111122223333:role/TransferFamilyFSxRole \
    --home-directory-type LOGICAL \
    --home-directory-mappings '[
        {
            "Entry": "/inbox",
            "Target": "/my-fsx-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias/users/jsmith/inbox"
        },
        {
            "Entry": "/outbox",
            "Target": "/my-fsx-ap-aqfqprnstn7aefdfbarligizwgyfouse1a-ext-s3alias/users/jsmith/outbox"
        }
    ]'
```

## Configuring file transfer clients

When using FSx file systems with Transfer Family, you must configure your file transfer clients to disable features that are not supported.

### WinSCP configuration

WinSCP uses a temporary rename feature by default that is not supported with S3 access points for FSx.

###### Warning

If you do not disable the temporary rename feature in WinSCP, file uploads will fail.

###### To disable temporary rename in WinSCP

1. Open WinSCP.
2. On the Login dialog, choose **Edit** to modify your session settings.
3. Choose **Advanced**.
4. In the left navigation, under **Transfer**, choose **Endurance**.
5. For **Enable transfer resume/transfer to temporary filename**, choose **Disable**.
6. Choose **OK** to save the settings.

Alternatively, you can disable this setting for an existing session:

1. Connect to your Transfer Family server.
2. Choose **Options**, then **Preferences**.
3. Choose **Transfer**, then **Endurance**.
4. For **Enable transfer resume/transfer to temporary filename**, choose **Disable**.
5. Choose **OK**.

### Other SFTP clients

For other SFTP clients, disable the following features if available:

- Temporary file uploads (upload to temp file, then rename)
- Resume transfers using temporary files
- Atomic uploads using rename operations
- Append mode for uploads

Consult your client documentation for specific configuration steps.

## Troubleshooting FSx storage

This section describes how to identify and resolve common issues when using Transfer Family with FSx file systems.

### File operation issues

**Permission denied**

If you receive permission denied errors:

1. Verify the IAM role has the correct permissions for the access point alias. You can do this by testing directly with S3 APIs.
2. Check that the access point policy allows the IAM role.
3. Verify the file system user has permissions on the target path.
4. Confirm the home directory mapping uses the correct access point alias.

**Upload fails with WinSCP**

If file uploads fail with WinSCP, disable temporary rename:

1. In WinSCP, choose **Options**, then **Preferences**.
2. Choose **Transfer**, then **Endurance**.
3. For **Enable transfer resume/transfer to temporary filename**, choose **Disable**.

For more information, see [Configuring file transfer clients](#configuring-file-transfer-clients "#configuring-file-transfer-clients").

**File upload fails**

If file uploads fail:

1. Verify the file size is under 5 GB.
2. Check that the FSx volume has sufficient available storage.
3. Monitor CloudWatch metrics for throttling.
