# Create an NFS file share with a custom

configuration

Use the following procedure to create a Network File System (NFS) file share with a
custom configuration. To create an NFS file share using default configuration settings,
see [Create an NFS
file share using the default configuration](nfs-fileshare-quickstart-settings.md "nfs-fileshare-quickstart-settings.md").

###### Important

Using S3 Versioning, Cross-Region Replication, or the Rsync utility when uploading data from a File Gateway can
have significant cost implications. For more information, see [Avoiding unanticipated costs when uploading data from File Gateway](avoid-unanticipated-costs.md "avoid-unanticipated-costs.md").

###### To create an NFS file share with customized settings

1.  Open the AWS Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/")
    and choose **File shares** from the left navigation
    pane.
2.  Choose **Create file share**.
3.  Choose **Customize configuration**. You can ignore the other
    fields on this page for now. You will be prompted to configure gateway,
    protocol, and storage settings in subsequent steps.
4.  For **Gateway**, choose the Amazon S3 File Gateway for your new file
    share for from the dropdown list.
5.  For **CloudWatch log group**, choose one of the following
    from the dropdown list:

        * To turn off logging for this file share, choose **Disable
         logging**.
        * To automatically create a new log group for this file share, choose
         **Created by Storage Gateway**.
        * To send health and resource notifications for this file share to an
         existing log group, choose the desired group from the list.

    For more information about audit logs, see [Understanding S3 File Gateway audit logs](monitoring-file-gateway.md#audit-logs "monitoring-file-gateway.md#audit-logs").

6.  (Optional) Under **Tags - Optional**, choose **Add
    new tag**, then enter a **Key** and
    **Value** for your file share.

A tag is a case-sensitive key-value pair that helps you categorize your
Storage Gateway resources. Adding tags can make filtering and searching for your file
share easier. You can repeat this step to add up to 50 tags.

Choose **Next** when finished. 7. For **S3 bucket**, do one of the following to specify where
your file share will store and retrieve files:

    * To connect the file share directly to an existing S3 bucket in your
     Amazon Web Services account, choose the bucket name from the dropdown list.
    * To connect the file share to an existing S3 bucket that is owned by an
     Amazon Web Services account other than the one that you use to create the file
     share, choose **A bucket in another account** from the
     dropdown list, then enter the **Cross-account bucket
     name**.
    * To connect the file share to a new S3 bucket, choose **Create
     a new S3 bucket**, then choose the
     **Region** where the Amazon S3 endpoint for your new
     bucket is located, and enter a unique **S3 bucket
     name**. Choose **Create S3 bucket** when
     finished. For more information about creating new buckets, see [How do I create
     an S3 bucket?](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md") in the Amazon S3 User Guide.
    * To connect the file share to an S3 bucket using an access point name,
     choose **Amazon S3 access point name** from the dropdown
     list, then enter the **Access point name**. If you need
     to create a new access point, you can choose **Create an S3
     access point**. For further instructions, see [Creating
     an access point](../../../AmazonS3/latest/userguide/create-access-points.md "../../../AmazonS3/latest/userguide/create-access-points.md") in the Amazon S3 User Guide. For more information
     about access points, see [Managing data
     access with Amazon S3 access points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md") and [Delegating access control to access points](../../../AmazonS3/latest/userguide/access-points-policies.md#access-points-delegating-control "../../../AmazonS3/latest/userguide/access-points-policies.md#access-points-delegating-control") in the Amazon S3 User
     Guide.
    * To connect the file share to an S3 bucket using an access point alias,
     choose **Amazon S3 access point alias** from the dropdown
     list, then enter the **Access point alias**. If you
     need to create a new access point, you can choose **Create an S3
     access point**. For further instructions, see [Creating
     an access point](../../../AmazonS3/latest/userguide/create-access-points.md "../../../AmazonS3/latest/userguide/create-access-points.md") in the Amazon S3 User Guide. For more information
     about access point aliases, see [Using a
     bucket-style alias for your access point](../../../AmazonS3/latest/userguide/access-points-alias.md "../../../AmazonS3/latest/userguide/access-points-alias.md") in the Amazon S3 User
     Guide.

###### Note

Each file share can only connect to one S3 bucket, but multiple file
shares can connect to the same bucket. If you connect more than one file
share to the same bucket, you must configure each file share to use a
unique, non-overlapping **S3 bucket prefix** to prevent
read/write conflicts.

S3 File Gateway does not support support Amazon S3 buckets with
periods (`.`) in the bucket name.

Make sure your bucket name complies with the rules for
bucket naming in Amazon S3. For more information, see [Rules for bucket naming](../../../AmazonS3/latest/dev/BucketRestrictions.md#bucketnamingrules "../../../AmazonS3/latest/dev/BucketRestrictions.md#bucketnamingrules") in the
_Amazon Simple Storage Service User Guide_. 8. (Optional) For **S3 bucket prefix**, enter a prefix for your
file share to apply to the objects it creates in Amazon S3. Prefixes are a way to
organize your data in S3, similar to directories in traditional file structures.
For more information, see [Organizing objects using
prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the Amazon S3 User Guide.

###### Note

    * If you connect more than one file share to the same bucket, you
     must configure each file share to use a unique, non-overlapping
     prefix to prevent read/write conflicts.
    * The prefix must end with a forward slash (/).
    * After the file share is created, the prefix can't be modified or
     deleted.

9.  For **Region**, choose the AWS Region where the S3 endpoint
    for your bucket is located from the dropdown list. This field appears only when
    you specify an access point or a bucket in another account for **S3
    bucket**.
10. For **Storage class for new objects**, choose a storage class
    from the dropdown list. For more information about storage classes, see [Using
    storage classes with a File Gateway](storage-classes.md#ia-file-gateway "storage-classes.md#ia-file-gateway").
11. For **IAM Role**, do one of the following to configure an IAM
    role for your file share:

        * To automatically create a new IAM role with the necessary permissions
         for your file share to work properly, choose **Created by
         Storage Gateway** from the dropdown list.
        * To use an existing IAM role, choose the role name from the dropdown
         list.
        * To create a new IAM role, choose **Create a role**.
         For further instructions, see [Creating
         a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
         AWS Identity and Access Management User Guide.

    For more information about how IAM roles control access between your file
    share and S3 bucket, see [Granting
    access to an Amazon S3 bucket](add-file-share.md#grant-access-s3 "add-file-share.md#grant-access-s3").

12. For **Private link**, do the following only if you need to
    configure your file share to communicate with AWS using a private endpoint in
    a Virtual Private Cloud (VPC). Otherwise, skip this step. For more information,
    see [What is AWS
    PrivateLink?](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") in the AWS PrivateLink Guide.
    1. Select **Use VPC endpoint**.
    2. For **Identify VPC endpoint by**, do one of the
       following:
       - Select **VPC endpoint ID**, then choose the
         endpoint that you want to use from the **VPC
         endpoint** dropdown list.
       - Select **DNS name**, then enter the
         **DNS name** for the endpoint that you want
         to use.

13. For **Encryption**, choose the type of server-side encryption
    that the file share will use for the data that it stores in Amazon S3:
    - To use server-side encryption managed with Amazon S3 (SSE-S3), choose
      **S3-Managed Keys (SSE-S3)**.

    For more information, see [Using
    server-side encryption with Amazon S3 managed keys](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") in the
    _Amazon Simple Storage Service User Guide_.
    - To use server-side encryption managed with AWS Key Management
      Service (SSE-KMS), choose **KMS-Managed Keys
      (SSE-KMS)**. For **Primary KMS key**,
      choose an existing AWS KMS key, or choose **Create a new KMS
      key** to create a new KMS key in the AWS Key Management
      Service (AWS KMS) console.

    For more information about AWS KMS, see [What is AWS Key
    Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer
    Guide_.
    - To use dual-layer server-side encryption managed with AWS Key
      Management Service (DSSE-KMS), choose **Dual-layer server-side
      encryption with AWS Key Management Service keys (DSSE-KMS)**. For
      **Primary KMS key**, choose an existing AWS KMS
      key, or choose **Create a new KMS key** to create a new
      KMS key in the AWS Key Management Service (AWS KMS) console.

    For more information about DSSE-KMS, see [Using
    dual-layer server-side encryption with AWS KMS keys](../../../AmazonS3/latest/userguide/UsingDSSEncryption.md "../../../AmazonS3/latest/userguide/UsingDSSEncryption.md") in the
    _Amazon Simple Storage Service User Guide_.

    ###### Note

    There are additional charges for using DSSE-KMS and AWS KMS keys.
    For more information, see [AWS KMS
    pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

    To specify an AWS KMS key with an alias that is not listed or to use
    an AWS KMS key from a different AWS account, you must use the
    AWS Command Line Interface. Asymmetric KMS keys are not supported. For more
    information, see [CreateNFSFileShare](../../../storagegateway/latest/APIReference/API_CreateMFSFileShare.md "../../../storagegateway/latest/APIReference/API_CreateMFSFileShare.md") in the _AWS Storage Gateway API
    Reference_.

###### Important

Make sure that your file share uses the same encryption type as the Amazon S3
bucket where it stores your data. 14. For **Guess MIME types**, select **Guess media MIME
type** to allow Storage Gateway to guess the media type for uploaded
objects based on their file extensions. 15. For **File share name**, enter a name for your file
share.

###### Note

A valid NFS file share name can only contain the following characters:
`a`-`z`, `A`-`Z`,
`0`-`9`, `-`, `.`, and
`_`. 16. For **Upload events**, select **Log an event when a
file is successfully uploaded by the gateway** if you want your
gateway to record CloudWatch log events when it successfully uploads files to Amazon S3.
Notification delay controls the minimum delay between the most recent client
write operation and generation of the `ObjectUploaded` log
notification. Because clients can make many small writes to files in a short
time, we recommend setting this parameter for as long as possible to avoid
generating multiple notifications for the same file in rapid succession. For
more information, see [Getting file upload notification](monitoring-file-gateway.md#get-file-upload-notification "monitoring-file-gateway.md#get-file-upload-notification").

###### Note

This setting has no effect on the timing of the object uploading to S3,
only on the timing of the notification.

This setting is not meant to specify an exact time at which the
notification will be sent. In some cases, the gateway might require more
than the specified delay time to generate and send notifications.

Choose **Next** when finished. 17. 18. For **File share protocol**, choose
**NFS**. 19. For **Client access**, do one of the following to specify
which NFS clients can access your file share:

    * To accept all incoming client connections, select **All NFS
     clients**.
    * To accept incoming client connections only from specific IP addresses,
     select **Specific NFS clients**, then choose
     **Add a client**. For **Allowed
     clients**, specify a valid IP address or CIDR block from
     which to accept connections. If you need to specify additional IP
     addresses, choose **Add another client**.

###### Note

We recommend configuring limiting access to your file share using the
**Specific NFS clients** option. If you don't, any
client on your network can mount to the file share. 20. For **Access type**, select one of the following:

    * To allow clients to read and write files on the file share, select
     **Read/Write**.
    * To allow clients to read files but not write to the file share, select
     **Read-only**.


    ###### Note

    For file shares that are mounted on a Microsoft Windows client, if
     you choose **Read-only**, you might see a message
     about an unexpected error keeping you from creating the folder. You
     can ignore this message.

21. For **Access level**, choose one of the following:
    - **Root squash (default)**: Access for the remote
      superuser (root) is mapped to UID (65534) and GID (65534).
    - **All squash**: All user access is mapped to User ID
      (UID) (65534) and Group ID (GID) (65534).
    - **No root squash**: The remote superuser (root)
      receives access as root.

22. (Optional) For **Automated cache refresh from S3**, choose
    **Set cache refresh interval**, then set the time in
    **Minutes** or **Days** to refresh the
    file share's cache using Time To Live (TTL). TTL is the length of time since the
    last refresh. After the TTL interval has elapsed, accessing a directory causes
    the File Gateway to refresh that directory's contents from the Amazon S3 bucket.

###### Note

Setting this value shorter than 30 minutes can negatively impact gateway
performance in situations where large numbers of Amazon S3 objects are frequently
created or deleted. 23. For **File metadata defaults**, select **Change
default metadata for S3 objects that were not created or modified by your
gateway** if you want your gateway to apply file metadata
(including Unix permissions) to preexisting objects that it discovers in your S3
bucket. Specify the **Directory permissions**, **File
permissions**, **User ID**, and **Group
ID** that you want to apply in the corresponding fields. 24. For **File ownership and permissions**, select **Give
the S3 bucket owner full ownership of files created by the gateway,
including read, write, edit, and delete permissions** if you want
the AWS account that owns the S3 bucket to have full control of all objects
written to the bucket by your file share.

Choose **Next** when finished. 25. Review the file share configuration. Choose **Edit** to
modify the settings for any section that you want to change. When finished,
choose **Create**.
After your NFS file share is created, you can view its configuration settings in the
AWS Storage Gateway console on the file share's **Details** tab. For
instructions to mount your file share, see [Mount your NFS
file share on your client](GettingStartedAccessFileShare.md "GettingStartedAccessFileShare.md").
