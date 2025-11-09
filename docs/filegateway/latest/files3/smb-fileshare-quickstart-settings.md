# Create an SMB file share using the

default configuration

This section explains how to create a new Server Message Block (SMB) file share using
preconfigured default settings. Use this method for basic deployments, personal use,
testing, or as a way to quickly deploy multiple file shares that you plan to edit and
customize later. For a list of the default settings for file shares that you create using
this procedure, see [Default configuration settings for SMB file shares](smb-fileshare-quickstart-settings.md#quickstart-default-settings "smb-fileshare-quickstart-settings.md#quickstart-default-settings"). If you need more granular
control or want to use advanced settings for your file share, see [Create
an SMB file share with a custom configuration](CreatingAnSMBFileShare.md "CreatingAnSMBFileShare.md").

###### Note

If you need to connect your file share to Amazon S3 through a Virtual Private Cloud (VPC),
you must follow the custom configuration procedure. You can’t edit VPC settings for a
file share after you create it.

###### Important

Using S3 Versioning, Cross-Region Replication, or the Rsync utility when uploading data from a File Gateway can
have significant cost implications. For more information, see [Avoiding unanticipated costs when uploading data from File Gateway](avoid-unanticipated-costs.md "avoid-unanticipated-costs.md").

###### Prerequisites

Before you create your file share, do the following:

- Configure SMB security settings for your File Gateway. For instructions, see
  [Setting a security level
  for your gateway](security-strategy.md "security-strategy.md").
- Configure either Microsoft Active Directory or guest access for authentication.
  For instructions, see [Using Active Directory
  to authenticate users](enable-ad-settings.md "enable-ad-settings.md") or [Providing guest access to your
  file share](guest-access.md "guest-access.md").
- Make sure that the required ports are open in your security group. For more
  information, see [Port
  Requirements](Resource_Ports.md "Resource_Ports.md").

###### To create an SMB file share using the default

configuration:

1. Open the AWS Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/") and choose **File
   shares** from the left navigation pane.
2. Choose **Create file share**.
3. For **Gateway**, choose the Amazon S3 File Gateway from the dropdown
   list.
4. For **File share protocol**, choose
   **SMB**.
5. For **S3 bucket**, do one of the following:
   - Choose an existing Amazon S3 bucket in your account from the dropdown
     list.
   - Choose **A bucket in another account** from the dropdown
     list, then enter the name of the bucket in **Cross-account bucket
     name**.
   - Choose **Create new S3 bucket**, then choose the
     AWS Region where the Amazon S3 endpoint for your new bucket is located, and
     enter a unique **S3 bucket name**. Choose **Create
     S3 bucket** when finished.

   For information about creating a new bucket, see [How do I create an S3 bucket?](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md") in the Amazon S3 User Guide.

###### Note

S3 File Gateway does not support support Amazon S3 buckets with periods
(`.`) in the bucket name.

Make sure your bucket name complies with the rules for
bucket naming in Amazon S3. For more information, see [Rules
for bucket naming](../../../AmazonS3/latest/dev/BucketRestrictions.md#bucketnamingrules "../../../AmazonS3/latest/dev/BucketRestrictions.md#bucketnamingrules") in the _Amazon Simple Storage Service User Guide_. 6. **User authentication**, choose the authentication method you want
to use from the dropdown list:

    * To use your corporate Microsoft Active Directory or AWS Managed Microsoft AD to
     authenticate user access to your SMB file share, choose **Active
     Directory**. Your gateway must be joined to a domain to use
     this method. For more information, see [Using Active
     Directory to authenticate users](enable-ad-settings.md "enable-ad-settings.md").


    ###### Note

    To use AWS Managed Microsoft AD with an Amazon EC2 gateway, you must create the Amazon EC2
     instance in the same VPC as the AWS Managed Microsoft AD, add the
     `_workspaceMembers` security group to the Amazon EC2 instance,
     and join the AD domain using the Admin credentials from the
     AWS Managed Microsoft AD.

    For more information about AWS Managed Microsoft AD, see the [*AWS Directory Service Administration
     Guide*](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md").

    For more information about Amazon EC2, see the [*Amazon Elastic Compute Cloud
     Documentation*](../../../ec2.md "../../../ec2.md").


    If **Join status** indicates that your gateway is already
     joined to an Active Directory domain, proceed to the next step. Otherwise,
     do the following:




    	1. Choose **Configure**.
    	2. For **Domain**, enter the name of the Active
    	 Directory domain you want your gateway to join.
    	3. Enter the **Username** and
    	 **Password** that the gateway will use to join
    	 the domain.
    	4. (Optional) For **Organization unit (OU)**, enter
    	 the designated OU that your Active Directory uses for new computer
    	 objects.
    	5. (Optional) For **Domain controller(s) (DC)**,
    	 enter the name of the DC through which your gateway will connect to
    	 Active Directory. You can leave this field blank to allow DNS to
    	 automatically select a DC.
    	6. Choose **Join Active Directory**.
    ###### Note

    Joining a domain creates an Active Directory account in the default
     container (which isn't an organizational unit) using the Gateway ID as
     the account name (for example, SGW-1234ADE). It is not possible to
     customize the name of this account.

    If your Active Directory environment requires that you pre-stage
     accounts to facilitate the domain join process, you need to create this
     account ahead of time.

    If your Active Directory environment has a designated OU for new
     computer objects, you must specify that OU when joining the
     domain.
    * To grant password-protected access to anyone who provides the guest
     password that you configure, choose **Guest access**. Your
     File Gateway doesn't need to be part of a Microsoft Active Directory domain
     to use this method. Choose **Configure** to specify your
     **Guest password**, then choose
     **Save**.

7. Review the settings under **Default configuration**, then choose
   **Create file share** to create your new SMB file share using
   the default configuration.
   After your SMB file share is created, you can view its configuration settings in the AWS
   Storage Gateway console on the file share's **Details** tab. For information about
   mounting your file share, see [Mount your SMB file share on
   your client](using-smb-fileshare.md "using-smb-fileshare.md").

## Default configuration settings for SMB file

shares

The following settings apply to all new SMB file shares that you create using the
default configuration. After you create a file share, you can select it from the
**File shares** page in the AWS Storage Gateway console to view details
about its configuration.

###### Important

The default SMB file share configuration provides full file control and access
permissions to the owner of the S3 bucket that's mapped to the file share, even if
the bucket is owned by a different Amazon Web Services account. For more information about
using your file share to access objects in a bucket that's owned by another account,
see [Using a
file share for cross-account access](add-file-share.md#cross-account-access "add-file-share.md#cross-account-access").

| Setting                           | Default value                                                                                                                                                  | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon S3 location**            | The file share connects directly to the Amazon S3 bucket and has the<br>same name as the bucket. Your gateway uses this bucket to store and<br>retrieve files. | The name doesn't include a prefix.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **AWS PrivateLink for S3**        | The file share doesn't connect to Amazon S3 through an interface<br>endpoint in your virtual private cloud (VPC).                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **File upload notification**      | Off                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Storage class for new objects** | Amazon S3 Standard                                                                                                                                             | This lets you store your frequently accessed object data<br>redundantly in multiple Availability Zones that are geographically<br>separated. For more information about the Amazon S3<br>Standard storage class, see [Storage classes for frequently accessed objects](../../../AmazonS3/latest/dev/storage-class-intro.md#sc-freq-data-access "../../../AmazonS3/latest/dev/storage-class-intro.md#sc-freq-data-access") in the<br>_Amazon Simple Storage Service User Guide_. |
| **Encryption**                    | Server-side encryption with S3 managed keys (SSE-S3)                                                                                                           | All Amazon S3 objects that your S3 File Gateway uploads, updates, or<br>modifies are encrypted by default with server-side encryption using<br>Amazon S3 managed keys.                                                                                                                                                                                                                                                                                                          |
| **Object metadata**               | Guess MIME type                                                                                                                                                | This allows Storage Gateway to guess the Multipurpose Internet Mail<br>Extension (MIME) type for uploaded objects based on file<br>extensions.<br>This option requires that Access Control Lists (ACLs) are turned<br>on for the Amazon S3 bucket that's associated with your file<br>share. If ACLs are  turned off, the file share can't access the Amazon S3<br>bucket, and remains in the \*_Unavailable_<br>• state<br>indefinitely.                                       |
| **Access based enumeration**      | Not activated                                                                                                                                                  | The files and folders on the file share are visible to all users<br>during directory enumeration. Access-based enumeration is a system<br>that filters the enumeration of  files and folders on an SMB file<br>share based on the share's access  control lists (ACLs).                                                                                                                                                                                                         |
| **Enable requester pays**         | Off                                                                                                                                                            | For more information, see [Requester<br>Pays buckets](../../../AmazonS3/latest/dev/RequesterPaysBuckets.md "../../../AmazonS3/latest/dev/RequesterPaysBuckets.md").                                                                                                                                                                                                                                                                                                             |
| **Opportunistic locking**         | On                                                                                                                                                             | This allows the file share to use opportunistic locking to<br>optimize  the file buffering strategy.  In most cases, activating<br>opportunistic locking improves  performance, particularly with<br>regard to Windows context  menus.                                                                                                                                                                                                                                          |
| **Audit logs**                    | Off                                                                                                                                                            | Logging to an Amazon CloudWatch group is turned off by<br>default.                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Force case sensitivity**        | Off                                                                                                                                                            | This allows the client to control the case sensitivity.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Access to your S3 bucket**      | Create a new IAM role                                                                                                                                          | The default option allows the File Gateway to create a new IAM<br>role and access  policy on your behalf.                                                                                                                                                                                                                                                                                                                                                                       |
