

# Troubleshooting: file share issues
<a name="troubleshooting-file-share-issues"></a>

You can find information following about actions to take if you experience unexpected issues with your file share.

**Topics**
+ [File share stuck in CREATING, UPDATING, or DELETING state](#troubleshooting-file-share-stuck-states)
+ [You can't create a file share](#create-file-troubleshoot)
+ [SMB file shares don't allow multiple different access methods](#smb-fileshare-troubleshoot)
+ [Multiple file shares can't write to the mapped S3 bucket](#multiwrite)
+ [Notification for deleted log group when using audit logs](#multiwrite)
+ [Can't upload files into your S3 bucket](#access-s3bucket)
+ [Can't change the default encryption to use SSE-KMS to encrypt objects stored in my S3 bucket](#encryption-issues)
+ [Changes made directly in an S3 bucket with object versioning turned on may affect what you see in your file share](#s3-object-versioning-file-share-issue)
+ [When writing to an S3 bucket with versioning turned on, the Amazon S3 File Gateway may create multiple versions of Amazon S3 objects](#s3-object-versioning-file-gateway-issue)
+ [Changes to an S3 bucket are not reflected in Storage Gateway](#s3-changes-issue)
+ [ACL permissions aren't working as expected](#smb-acl-issues)
+ [Your gateway performance declined after you performed a recursive operation](#recursive-operation-issues)

## File share stuck in CREATING, UPDATING, or DELETING state
<a name="troubleshooting-file-share-stuck-states"></a>

The file share status summarizes the health of your file share. If your S3 File Gateway file share is stuck in the `CREATING`, `UPDATING`, or `DELETING` state, use the following troubleshooting steps to identify and resolve the issue.

**Note**  
When you create a file share, Storage Gateway doesn't verify that the IAM role and the Amazon S3 bucket that you specify already exist. This is intentional, because a newly created IAM role can take time to become available for Storage Gateway to assume. As a result, a `CreateNFSFileShare` or `CreateSMBFileShare` request that specifies a role or a bucket that doesn't exist still succeeds and returns a file share ARN, but the file share remains in the `CREATING` state instead of changing to `AVAILABLE`. Before you continue troubleshooting, confirm that both the IAM role and the Amazon S3 bucket that you specified exist.

### Confirm IAM role permissions and trust relationship
<a name="w2ab1c55c43b9b7"></a>

The AWS Identity and Access Management (IAM) role associated with your file share must exist, and it must have sufficient permissions to access the Amazon S3 bucket. Additionally, the role's trust policy must grant the Storage Gateway service permissions to assume the role.

**To verify IAM role permissions:**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Confirm that the IAM role that you specified for your file share appears in the list of roles. If the role doesn't exist, create it, and then create the file share again. For more information, see [Granting access to an Amazon S3 bucket](grant-access-s3.md).

1. Choose the IAM role that's associated with your file share.

1. Choose the **Trust relationships** tab.

1. Confirm that Storage Gateway is listed as a trusted entity. If Storage Gateway isn't a trusted entity, choose **Edit trust relationship**, and then add the following policy:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "",
         "Effect": "Allow",
         "Principal": {
           "Service": "storagegateway.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

1. Verify that the IAM role has the correct permissions and that the Amazon S3 bucket is listed as a resource in the IAM policy. For more information, see [Granting access to an Amazon S3 bucket](grant-access-s3.md).

**Note**  
To avoid cross-service confused deputy prevention issues, use a trust relationship policy that includes condition context keys. For more information, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md).

### Verify AWS STS is activated in your Region
<a name="w2ab1c55c43b9b9"></a>

File shares can become stuck in the `CREATING` or `UPDATING` state if AWS Security Token Service (AWS STS) is deactivated in your AWS Region.

**To verify AWS STS status:**

1. Open the AWS Identity and Access Management console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Account settings**.

1. In the **Security Token Service (STS)** section, verify that the **Status** is **Active** for the AWS Region where you want to create the file share.

1. If the status is **Inactive**, choose **Activate** to enable AWS STS in that Region.

### Verify S3 bucket exists and follows naming rules
<a name="w2ab1c55c43b9c11"></a>

Your file share requires an existing Amazon S3 bucket that follows Amazon S3 naming conventions. Storage Gateway doesn't verify that the bucket exists when you create the file share, so a file share that points to a bucket that was deleted or never created remains in the `CREATING` state.

**To verify your S3 bucket:**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Confirm that the Amazon S3 bucket mapped to your file share exists. If the bucket doesn't exist, create it. After you create the bucket, the file share status should change to `AVAILABLE`. For more information, see [Create a bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) in the *Amazon Simple Storage Service User Guide*.

1. Verify that your bucket name complies with the [rules for bucket naming](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html#bucketnamingrules) in the *Amazon Simple Storage Service User Guide*.
**Note**  
S3 File Gateway does not support Amazon S3 buckets with periods (`.`) in the bucket name.

### Force delete a file share stuck in DELETING state
<a name="w2ab1c55c43b9c13"></a>

When you delete a file share, the gateway removes the share from the associated Amazon S3 bucket. However, data that's currently uploading continues to upload before the deletion completes. During this process, the file share shows a `DELETING` status.

**Important**  
Check the Amazon CloudWatch metric `CachePercentDirty` for your gateway to determine how much data is pending upload. For more information about Storage Gateway metrics, see [Monitoring your S3 File Gateway](monitoring-file-gateway.md).

If you don't want to wait for all in-progress uploads to finish, you can force delete the file share.

**To force delete a file share:**

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/](https://console.aws.amazon.com/storagegateway/).

1. In the navigation pane, choose **File shares**.

1. Select the file share that you want to delete.

1. Choose the **Details** tab, and review the **This file share is being deleted** message.

1. Verify the ID of the file share in the message, and then select the confirmation box.
**Note**  
You can't undo the force delete operation.

1. Choose **Force delete now**.

Alternatively, you can use the AWS CLI [delete-file-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-file-share.html) command with the `--force-delete` parameter set to `true`.

**Important**  
Before force deleting a file share, confirm that your gateway isn't in an `OFFLINE` state. If the gateway is offline, first resolve the offline issue. For more information, see [Troubleshooting: gateway offline in the Storage Gateway console](troubleshooting-gateway-offline.md).

If the gateway virtual machine (VM) is already deleted, you must delete the gateway from the Storage Gateway console to remove all associated file shares, including those stuck in the `DELETING` state. For more information, see [Deleting your gateway and removing associated resources](deleting-gateway-common.md).

### Troubleshoot network connectivity issues
<a name="w2ab1c55c43b9c15"></a>

Network issues can prevent your file share from transitioning out of the `CREATING`, `UPDATING`, or `DELETING` state. Common network issues include:
+ Your gateway is offline or the gateway VM is deleted.
+ Network access between Storage Gateway and the Amazon S3 service endpoint is blocked.
+ The Amazon S3 Amazon VPC endpoint that the gateway uses to communicate with Amazon S3 was deleted.
+ Required network ports aren't open or network routing is improperly configured.

#### Test S3 connectivity from the gateway local console
<a name="w2ab1c55c43b9c15b7"></a>

**To test S3 connectivity:**

1. Log in to your gateway's local console. For more information, see [Logging in to the File Gateway local console](LocalConsole-login-fgw.md).

1. In the **Storage Gateway - Configuration** main menu, enter the number corresponding to **Test S3 Connectivity**.

1. Choose the Amazon S3 endpoint type:
   + For Amazon S3 traffic that flows through an Internet Gateway, NAT Gateway, Transit Gateway, or Amazon S3 Gateway Amazon VPC endpoint, choose **Public**.
   + For Amazon S3 traffic that flows through an Amazon S3 interface Amazon VPC endpoint, choose **VPC (PrivateLink)**.
   + For a FIPS endpoint, choose the FIPS option.

1. Enter the Amazon S3 bucket Region.

1. If using a Amazon VPC endpoint, enter the Amazon S3 Amazon VPC endpoint DNS name (for example, `vpce-0329c2790456f2d01-0at85l34`).

The gateway automatically performs a connectivity test that validates both the network connection and SSL connection. If the test fails:
+ **Network Test failure** - Usually caused by firewall rules, security group configurations, or improper network routing. Verify that required ports are open and network routing is configured correctly.
+ **SSL Test failure** - Indicates that SSL inspection or deep packet inspection is occurring between your gateway VM and Amazon S3 service endpoints. Disable SSL and deep packet inspection for Storage Gateway traffic.

#### Verify proxy configuration
<a name="w2ab1c55c43b9c15b9"></a>

If your gateway uses a proxy server, verify that the proxy isn't blocking network communication.

**To check proxy configuration:**

1. In the **Storage Gateway - Configuration** main menu, enter the number corresponding to **HTTP/SOCKS Proxy Configuration**.

1. Select the option to view the current network proxy configuration.

1. If a proxy is configured, verify that Amazon S3 traffic can flow from Storage Gateway to the proxy server over port 3128 (or your configured listener port), and then to the Amazon S3 endpoint over port 443.

1. Confirm that the proxy or firewall allows traffic to and from the network ports and service endpoints required by Storage Gateway. For more information, see the required network ports.

If issues persist, you can temporarily remove the proxy configuration to determine if the proxy is causing the problem.

#### Verify security groups and network routing
<a name="w2ab1c55c43b9c15c11"></a>
+ **For gateways on Amazon EC2** - Confirm that the security group has port 443 open to Amazon S3 endpoints. Verify that the Amazon EC2 subnet's route table properly routes Amazon S3 traffic to Amazon S3 endpoints. For more information, see the required network ports.
+ **For on-premises gateways** - Confirm that firewall rules allow the required ports and that local route tables properly route Amazon S3 traffic to Amazon S3 endpoints. For more information, see the required network ports.
+ **VPC endpoints** - Verify that the Amazon S3 Amazon VPC endpoint used by the gateway hasn't been deleted. If the Amazon VPC endpoint is deleted and the gateway has no public IP address, the gateway can't communicate with Amazon S3.

## You can't create a file share
<a name="create-file-troubleshoot"></a>

1. If you can't create a file share because your file share is stuck in CREATING status, verify that the S3 bucket you mapped your file share to exists. For information on how to do so, see [File share stuck in CREATING, UPDATING, or DELETING state](#troubleshooting-file-share-stuck-states), preceding.

1. If the S3 bucket exists, then verify that AWS Security Token Service is activated in the region where you are creating the file share. If a security token is not active, you should activate it. For information about how to activate a token using AWS Security Token Service, see [Activating and deactivating AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the *IAM User Guide*.

## SMB file shares don't allow multiple different access methods
<a name="smb-fileshare-troubleshoot"></a>

SMB file shares have the following restrictions:

1. When the same client attempts to mount both an Active Directory and Guest access SMB file share the following error message is displayed: `Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.`

1. A Windows user cannot remain connected to two Guest Access SMB file shares, and may be disconnected when a new Guest Access connection is established.

1. A Windows client can't mount both a Guest Access and an Active Directory SMB file share that is exported by the same gateway.

## Multiple file shares can't write to the mapped S3 bucket
<a name="multiwrite"></a>

We don't recommend configuring your S3 bucket to allow multiple file shares to write to one S3 bucket. This approach can cause unpredictable results. 

Instead, we recommend that you allow only one file share to write to each S3 bucket. You create a bucket policy to allow only the role associated with your file share to write to the bucket. For more information, see [Best Practices for File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/best-practices.html).

## Notification for deleted log group when using audit logs
<a name="multiwrite"></a>

If the log group does not exist, the user could select the log group link below that message to go either create a new log group or use an existing log group to use as the target for audit logs

## Can't upload files into your S3 bucket
<a name="access-s3bucket"></a>

If you can't upload files into your S3 bucket, do the following:

1. Make sure you have granted the required access for the Amazon S3 File Gateway to upload files into your S3 bucket. For more information, see [Granting access to an Amazon S3 bucket](grant-access-s3.md).

1. Make sure the role that created the bucket has permission to write to the S3 bucket. For more information, see [Best Practices for File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/best-practices.html).

1. If your File Gateway uses SSE-KMS or DSSE-KMS for encryption, make sure the IAM role associated with the file share includes *kms:Encrypt*, *kms:Decrypt*, *kms:ReEncrypt\**, *kms:GenerateDataKey*, and *kms:DescribeKey* permissions. For more information, see [Using Identity-Based Policies (IAM Policies) for Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/using-identity-based-policies.html).

## Can't change the default encryption to use SSE-KMS to encrypt objects stored in my S3 bucket
<a name="encryption-issues"></a>

If you change the default encryption and make SSE-KMS (server-side encryption with AWS KMS–managed keys) the default for your S3 bucket, objects that a Amazon S3 File Gateway stores in the bucket are not encrypted with SSE-KMS. By default, a S3 File Gateway uses server-side encryption managed with Amazon S3 (SSE-S3) when it writes data to an S3 bucket. Changing the default won't automatically change your encryption.

To change the encryption to use SSE-KMS with your own AWS KMS key, you must turn on SSE-KMS encryption. To do so, you provide the Amazon Resource Name (ARN) of the KMS key when you create your file share. You can also update KMS settings for your file share by using the `UpdateNFSFileShare` or `UpdateSMBFileShare` API operation. This update applies to objects stored in the S3 buckets after the update. For more information, see [Data encryption using AWS KMS](encryption.md).

## Changes made directly in an S3 bucket with object versioning turned on may affect what you see in your file share
<a name="s3-object-versioning-file-share-issue"></a>

If your S3 bucket has objects written to it by another client, your view of the S3 bucket might not be up-to-date as a result of S3 bucket object versioning. You should always refresh your cache before examining files of interest.

*Object versioning *is an optional S3 bucket feature that helps protect data by storing multiple copies of the same-named object. Each copy has a separate ID value, for example `file1.jpg`: `ID="xxx"` and `file1.jpg`: `ID="yyy"`. The number of identically named objects and their lifetimes is controlled by Amazon S3 lifecycle policies. For more details on these Amazon S3 concepts, see [Using versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) and [Object lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) in the *Amazon S3 Developer Guide. * 

When you delete a versioned object, that object is flagged with a delete marker but retained. Only an S3 bucket owner can permanently delete an object with versioning turned on.

In your S3 File Gateway, files shown are the most recent versions of objects in an S3 bucket at the time the object was fetched or the cache was refreshed. S3 File Gateways ignore any older versions or any objects marked for deletion. When reading a file, you read data from the latest version. When you write a file in your file share, your S3 File Gateway creates a new version of a named object with your changes, and that version becomes the latest version.

Your S3 File Gateway continues to read from the earlier version, and updates that you make are based on the earlier version should a new version be added to the S3 bucket outside of your application. To read the latest version of an object, use the [RefreshCache](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RefreshCache.html) API action or refresh from the console as described in [Refreshing Amazon S3 bucket object cache](refresh-cache.md).

**Important**  
We don't recommend that objects or files be written to your S3 File Gateway S3 bucket from outside of the file share.

## When writing to an S3 bucket with versioning turned on, the Amazon S3 File Gateway may create multiple versions of Amazon S3 objects
<a name="s3-object-versioning-file-gateway-issue"></a>

With object versioning turned on, you may have multiple versions of an object created in Amazon S3 on every update to a file from your NFS or SMB client. Here are scenarios that can result in multiple versions of an object being created in your S3 bucket:
+ When a file is modified in the Amazon S3 File Gateway by an NFS or SMB client after it has been uploaded to Amazon S3, the S3 File Gateway uploads the new or modified data instead of uploading the whole file. The file modification results in a new version of the Amazon S3 object being created.
+ When a file is written to the S3 File Gateway by an NFS or SMB client, the S3 File Gateway uploads the file's data to Amazon S3 followed by its metadata, (ownerships, timestamps, etc.). Uploading the file data creates an Amazon S3 object, and uploading the metadata for the file updates the metadata for the Amazon S3 object. This process creates another version of the object, resulting in two versions of an object.
+ When the S3 File Gateway is uploading larger files, it might need to upload smaller chunks of the file before the client is done writing to the File Gateway. Some reasons for this include to free up cache space or a high rate of writes to a file. This can result in multiple versions of an object in the S3 bucket.

You should monitor your S3 bucket to determine how many versions of an object exist before setting up lifecycle policies to move objects to different storage classes. You should configure lifecycle expiration for previous versions to minimize the number of versions you have for an object in your S3 bucket. The use of Same-Region replication (SRR) or Cross-Region replication (CRR) between S3 buckets will increase the storage used. For more information about replication, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html).

**Important**  
Do not configure replication between S3 buckets until you understand how much storage is being used when object versioning is turned on.

Use of versioned S3 buckets can greatly increase the amount of storage in Amazon S3 because each modification to a file creates a new version of the S3 object. By default, Amazon S3 continues to store all of these versions unless you specifically create a policy to override this behavior and limit the number of versions that are kept. If you notice unusually large storage usage with object versioning turned on, check that you have your storage policies set appropriately. An increase in the number of `HTTP 503-slow down` responses for browser requests can also be the result of problems with object versioning.

If you turn on object versioning after installing a S3 File Gateway, all unique objects are retained (`ID=”NULL”`) and you can see them all in the file system. New versions of objects are assigned a unique ID (older versions are retained). Based on the object's timestamp only the newest versioned object is viewable in the NFS file system.

After you turn on object versioning, your S3 bucket can't be returned to a nonversioned state. You can, however, suspend versioning. When you suspend versioning, a new object is assigned an ID. If the same named object exists with an `ID=”NULL”` value, the older version is overwritten. However, any version that contains a non-`NULL` ID is retained. Timestamps identify the new object as the current one, and that is the one that appears in the NFS file system.

## Changes to an S3 bucket are not reflected in Storage Gateway
<a name="s3-changes-issue"></a>

Storage Gateway updates the file share cache automatically when you write files to the cache locally using the file share. However, Storage Gateway doesn't automatically update the cache when you upload a file directly to Amazon S3. When you do this, you must perform a `RefreshCache` operation to see the changes on the file share. If you have more than one file share, then you must run the `RefreshCache` operation on each file share.

You can refresh the cache using the Storage Gateway console and the AWS Command Line Interface (AWS CLI):
+  To refresh the cache using the Storage Gateway console, see Refreshing objects in your Amazon S3 bucket. 
+  To refresh the cache using the AWS CLI: 

  1. Run the command `aws storagegateway list-file-shares`

  1. Copy the Amazon Resource Number (ARN) of the file share with the cache that you want to refresh.

  1. Run the `refresh-cache` command with your ARN as the value for `--file-share-arn`:

     `aws storagegateway refresh-cache --file-share-arn arn:aws:storagegateway:eu-west-1:12345678910:share/share-FFDEE12`

 To automate the `RefreshCache` operation, see [ How can I automate the RefreshCache operation on Storage Gateway?](https://aws.amazon.com/premiumsupport/knowledge-center/storage-gateway-automate-refreshcache/) 

## ACL permissions aren't working as expected
<a name="smb-acl-issues"></a>

If access control list (ACL) permissions aren't working as you expect with your SMB file share, you can perform a test. 

To do this, first test the permissions on a Microsoft Windows file server or a local Windows file share. Then compare the behavior to your gateway's file share.

## Your gateway performance declined after you performed a recursive operation
<a name="recursive-operation-issues"></a>

In some cases, you might perform a recursive operation, such as renaming a directory or turning on inheritance for an ACL, and force it down the tree. If you do this, your S3 File Gateway recursively applies the operation to all objects in the file share. 

For example, suppose that you apply inheritance to existing objects in an S3 bucket. Your S3 File Gateway recursively applies inheritance to all objects in the bucket. Such operations can cause your gateway performance to decline.