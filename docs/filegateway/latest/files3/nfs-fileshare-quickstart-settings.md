# Create an NFS file share using the

default configuration

This section explains how to create a new Network File System (NFS) file share using
preconfigured default settings. Use this method for basic deployments, personal use,
testing, or as a way to quickly deploy multiple file shares that you plan to edit and
customize later. For a list of the default settings for file shares that you create using
this procedure, see [Default configuration settings for NFS file shares](nfs-fileshare-quickstart-settings.md#quickstart-default-settings "nfs-fileshare-quickstart-settings.md#quickstart-default-settings"). If you need more granular
control or want to use advanced settings for your file share, see [Create
an NFS file share using a custom configuration](CreatingAnNFSFileShare.md "CreatingAnNFSFileShare.md").

###### Note

If you need to connect your file share to Amazon S3 through a Virtual Private Cloud (VPC),
you must follow the custom configuration procedure. You can’t edit VPC settings for a
file share after you create it.

###### Important

Using S3 Versioning, Cross-Region Replication, or the Rsync utility when uploading data from a File Gateway can
have significant cost implications. For more information, see [Avoiding unanticipated costs when uploading data from File Gateway](avoid-unanticipated-costs.md "avoid-unanticipated-costs.md").

###### To create an NFS file share using the default

configuration:

1. Open the AWS Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/") and choose **File
   shares** from the left navigation pane.
2. Choose **Create file share**.
3. For **Gateway**, choose your Amazon S3 File Gateway from the list.
4. For **File share protocol**, choose
   **NFS**.
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
for bucket naming](../../../AmazonS3/latest/dev/BucketRestrictions.md#bucketnamingrules "../../../AmazonS3/latest/dev/BucketRestrictions.md#bucketnamingrules") in the _Amazon Simple Storage Service User Guide_. 6. Review the settings under **Default configuration**, then choose
**Create file share** to create your new NFS file share using
the default configuration.
After your NFS file share is created, you can view its configuration settings in the AWS
Storage Gateway console on the file share's **Details** tab. For information about
mounting your file share, see [Mount your NFS file
share on your client](GettingStartedAccessFileShare.md "GettingStartedAccessFileShare.md").

## Default configuration settings for NFS file

shares

The following settings apply to all new NFS file shares that you create using the
default configuration. After you create a file share, you can select it from the
**File shares** page in the AWS Storage Gateway console to view details
about its configuration.

###### Important

The default NFS file share configuration provides full file control and access
permissions to the owner of the S3 bucket that's mapped to the file share, even if
the bucket is owned by a different AWS account. For more information about using
your file share to access objects in a bucket that's owned by another account, see
[Using a file share for cross-account access](cross-account-access.md "cross-account-access.md").

| Setting                           | Default value                                                                                                                                            | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon S3 location**            | The file share connects directly to the Amazon S3 bucket and has the same name as the bucket. Your gateway uses this bucket to store and retrieve files. | The name doesn't include a prefix.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **AWS PrivateLink for S3**        | The file share doesn't connect to Amazon S3 through an interface endpoint in your virtual private cloud (VPC).                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **File upload notification**      | Off                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Storage class for new objects** | Amazon S3 Standard                                                                                                                                       | This lets you store your frequently accessed object data redundantly in multiple Availability Zones that are geographically separated. For more information about the Amazon S3 Standard storage class, see [Storage classes for frequently accessed objects](../../../AmazonS3/latest/dev/storage-class-intro.md#sc-freq-data-access "../../../AmazonS3/latest/dev/storage-class-intro.md#sc-freq-data-access") in the _Amazon Simple Storage Service User Guide_. |
| **Encryption**                    | Server-side encryption with S3 managed keys (SSE-S3)                                                                                                     | All Amazon S3 objects that your S3 File Gateway uploads, updates, or modifies are encrypted by default with server-side encryption using Amazon S3 managed keys.                                                                                                                                                                                                                                                                                                    |
| **Object metadata**               | Guess MIME type                                                                                                                                          | This allows Storage Gateway to guess the Multipurpose Internet Mail Extension (MIME) type for uploaded objects based on file extensions. This option requires that Access Control Lists (ACLs) are turned on for the Amazon S3 bucket that's associated with your file share. If ACLs are turned off, the file share can't access the Amazon S3 bucket, and remains in the **Unavailable** state indefinitely.                                                      |
| **Enable requester pays**         | Off                                                                                                                                                      | For more information, see [Requester Pays buckets](../../../AmazonS3/latest/dev/RequesterPaysBuckets.md "../../../AmazonS3/latest/dev/RequesterPaysBuckets.md").                                                                                                                                                                                                                                                                                                    |
| **Audit logs**                    | Off                                                                                                                                                      | Logging to an Amazon CloudWatch group is turned off by default.                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Access to your S3 bucket**      | Create a new IAM role                                                                                                                                    | The default option allows the File Gateway to create a new IAM role and access policy on your behalf. All NFS clients are allowed access. For information about supported NFS clients, see [Supported NFS and SMB clients for File Gateway](Requirements.md#requirements-s3-fgw-clients "Requirements.md#requirements-s3-fgw-clients").                                                                                                                             |
| **Mount options**                 | <br>• Squash level – Root squash <br>• Export as – Read-write                                                                                            | The default value of **Squash level** means that access for the remote superuser (root) is mapped to User Identifier (UID) (65534) and Group Identifier (GID) (65534).                                                                                                                                                                                                                                                                                              |
| **File metadata defaults**        | <br>• Directory permissions – 0777 <br>• File permissions – 0666 <br>• User Identifier (UID) – 65534 <br>• Group Identifier (GID) – 65534                |
