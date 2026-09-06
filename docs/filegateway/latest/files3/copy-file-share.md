

# Copy a file share
<a name="copy-file-share"></a>

**Note**  
The copy file share feature is available only through the Storage Gateway console. There is no corresponding AWS CLI command or API action for this feature.

You can use the Storage Gateway console to copy an existing NFS or SMB file share to a different gateway. Copying a file share creates a new file share on the destination gateway that points to the same Amazon S3 bucket as the source file share, while preserving most of the original share's configuration settings. This is primarily intended to assist with gateway migrations, allowing you to move a file share to a replacement gateway without manually recreating its configuration. After you verify that the copied file share is working correctly on the new gateway, you should delete the original file share from the source gateway.

## Considerations
<a name="copy-file-share-considerations"></a>

Before you copy a file share, consider the following:
+ The destination gateway must be in an **Active** state.
+ Both the source and destination gateways must be Amazon S3 File Gateway gateways. You cannot copy file shares between different gateway types.
+ The copied file share points to the same Amazon S3 bucket as the source. We do not recommend maintaining both file shares actively for an extended period. Writing to the same Amazon S3 bucket from multiple gateways simultaneously can lead to data inconsistencies, cache conflicts, and unexpected behavior. After confirming that the copied file share is functioning correctly, delete the source file share.
+ The copy operation preserves the file share protocol (NFS or SMB). You cannot change the protocol type during the copy.
+ If the source file share uses an IAM role for Amazon S3 bucket access, you can choose to use the same role for the copied file share, select a different existing role, or have the console create a new role automatically.
+ If the source file share has CloudWatch log group monitoring configured, you can choose to use the same log group, select a different log group, or have the console create a new log group automatically.
+ If you are copying an SMB file share between gateways that are joined to different Active Directory domains, or between a gateway using Active Directory authentication and one using guest access, review your SMB access settings after the copy completes to ensure that access permissions are configured correctly.
+ If the source and destination gateways have different VPC configurations (for example, one gateway is activated in a VPC and the other is not), the copied file share uses the network configuration of the destination gateway.

**Important**  
When copying an SMB file share, root-level access control lists (ACLs) are not copied to the new file share. The copied file share is created with default root ACLs. If you have configured custom root ACLs on the source file share, you must manually reconfigure them on the copied file share after the copy completes.

## Copy a file share to another gateway
<a name="copy-file-share-procedure"></a>

**To copy a file share using the Storage Gateway console**

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/).

1. In the navigation pane, choose **File shares**.

1. Select the file share that you want to copy.

1. From the **Actions** menu, choose **Copy file share to another gateway**.

1. For **Gateway**, select the destination gateway where you want to create the copy.

1. For **IAM role**, choose one of the following options:
   + **Use the same IAM role** – Uses the same IAM role as the source file share. Choose this option if the destination gateway should use the same permissions to access the Amazon S3 bucket.
   + **Select an existing IAM role** – Choose a different IAM role from the list. Make sure the role grants the required Amazon S3 permissions.
   + **Auto-generate a new IAM role** – The console creates a new IAM role with the required permissions for the Amazon S3 bucket.

1. For **Log group**, choose one of the following options:
   + **Use the same log group** – Sends health logs to the same CloudWatch log group as the source file share.
   + **Select an existing log group** – Choose a different CloudWatch log group from the list.
   + **Auto-generate a new log group** – The console creates a new CloudWatch log group for the copied file share.

1. Choose **Copy file share**.

The new file share appears in the **File shares** list with a status of **Creating**. After the share becomes **Available**, you can mount it on your clients using the same protocol as the source share.

## Settings preserved during copy
<a name="copy-file-share-settings"></a>

When you copy a file share, the following settings are carried over from the source file share to the new copy:
+ Amazon S3 bucket name and prefix
+ Storage class
+ Object encryption settings (SSE-S3, SSE-KMS, or DSSE-KMS)
+ File share protocol (NFS or SMB)
+ Cache refresh settings
+ Squash settings and client access (NFS file shares)
+ SMB access settings including authentication method, file share visibility, and access-based enumeration (SMB file shares)
+ Allowed and denied users and groups (SMB file shares)

The following settings are *not* copied and use the destination gateway's configuration or defaults:
+ Gateway network configuration (VPC endpoint, public endpoint)
+ Active Directory domain membership (uses the destination gateway's AD configuration)
+ Bandwidth rate limits (uses the destination gateway's limits)
+ Root-level ACLs (SMB file shares – the copied share is created with default root ACLs)