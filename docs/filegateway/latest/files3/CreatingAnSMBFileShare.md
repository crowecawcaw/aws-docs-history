# Create an SMB file share with a custom

configuration

Use the following procedure to create a Server Message Block (SMB) file share with a
custom configuration. To create an SMB file share using default configuration settings,
see [Create an SMB
file share using the default configuration](smb-fileshare-quickstart-settings.md "smb-fileshare-quickstart-settings.md").

###### Important

Using S3 Versioning, Cross-Region Replication, or the Rsync utility when uploading data from a File Gateway can
have significant cost implications. For more information, see [Avoiding unanticipated costs when uploading data from File Gateway](avoid-unanticipated-costs.md "avoid-unanticipated-costs.md").

###### Prerequisites

Before you create your file share, do the following:

- Configure SMB security settings for your File Gateway. For instructions, see
  [Setting a security
  level for your gateway](security-strategy.md "security-strategy.md").
- Configure either Microsoft Active Directory or guest access for
  authentication. For instructions, see [Using Active
  Directory to authenticate users](enable-ad-settings.md "enable-ad-settings.md") or [Providing guest access to
  your file share](guest-access.md "guest-access.md").
- Make sure that the required ports are open in your security group. For more
  information, see [Port
  Requirements](Resource_Ports.md "Resource_Ports.md").

###### To create an SMB file share with customized settings

1.  Open the AWS Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/")
    and choose **File shares** from the left navigation
    pane.
2.  Choose **Create file share**.
3.  Choose **Customize configuration**. You can ignore the other
    fields on this page for now. You will be prompted to configure gateway,
    protocol, and storage settings in subsequent steps.
4.  For **Gateway**, choose the Amazon S3 File Gateway from the dropdown
    list.
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
    **Value** for your file share. A tag is a case-sensitive
    key-value pair that helps you to categorize your Storage Gateway resources. Adding tags
    can make filtering and searching for your file share easier. You can repeat this
    step to add up to 50 tags.

Choose **Next** when finished. 7. For **S3 bucket**, do one of the following to specify where
to store and retrieve files:

    * To connect the file share directly to an existing S3 bucket in your
     Amazon Web Services account, choose the bucket name from the dropdown list.
    * To connect the file share to an existing S3 bucket that's owned by an
     Amazon Web Services account other than the one that you're using to create the
     file share, choose **A bucket in another account** from
     the dropdown list, then enter the **Cross-account bucket
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
    access to an Amazon S3bucket](add-file-share.md#grant-access-s3 "add-file-share.md#grant-access-s3").

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

13. For **Encryption**, choose the type of encryption keys to use
    to encrypt objects that your File Gateway stores in Amazon S3:
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
    information, see [CreateSMBFileShare](../../../storagegateway/latest/APIReference/API_CreateSMBFileShare.md "../../../storagegateway/latest/APIReference/API_CreateSMBFileShare.md") in the _AWS Storage Gateway API
    Reference_.

###### Important

Make sure that your file share uses the same encryption type as the Amazon S3
bucket where it stores your data. 14. For **Guess MIME types**, select **Guess media MIME
type** to allow Storage Gateway to guess the Multipurpose Internet Mail
Extension (MIME) type for uploaded objects based on their file
extensions. 15. For **File share name**, enter a name for your file
share.

###### Note

A valid SMB file share name cannot contain the following characters:
`[`,`]`,`#`,`;`,`<`,`>`,`:`,`"`,`\`,`/`,`|`,`?`,`*`,`+`,
or ASCII control characters `1-31`. 16. For **Upload events**, select **Log an event when a
file is successfully uploaded by the gateway** if you want your
gateway to record CloudWatch log events when it successfully uploads files to Amazon S3.
Notification delay controls the delay between the most recent client write
operation and generation of the `ObjectUploaded` log notification.
Because clients can make many small writes to files in a short time, we
recommend setting this parameter for as long as possible to avoid generating
multiple notifications for the same file in rapid succession. For more
information, see [Getting file upload notification](monitoring-file-gateway.md#get-file-upload-notification "monitoring-file-gateway.md#get-file-upload-notification").

###### Note

This setting has no effect on the timing of the object uploading to S3,
only on the timing of the notification.

This setting is not meant to specify an exact time at which the
notification will be sent. In some cases, the gateway might require more
than the specified delay time to generate and send notifications.

Choose **Next** when finished. 17. For **File share protocol**, choose
**SMB**. 18. For **User authentication**, choose the authentication method
that you want to use from the dropdown list:

    * To use your corporate Microsoft Active Directory or AWS Managed Microsoft AD to
     authenticate user access to your SMB file share, choose **Active
     Directory**. Your gateway must be joined to a domain to use
     this method. For more information, see [Using Active
     Directory to authenticate users](enable-ad-settings.md "enable-ad-settings.md").


    ###### Note

    To use AWS Managed Microsoft AD with an Amazon EC2 gateway, you must create the
     Amazon EC2 instance in the same VPC as the AWS Managed Microsoft AD, add the
     `_workspaceMembers` security group to the Amazon EC2
     instance, and join the AD domain using the Admin credentials from
     the AWS Managed Microsoft AD.

    For more information about AWS Managed Microsoft AD, see the [*AWS Directory Service Administration
     Guide*](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md").

    For more information about Amazon EC2, see the [*Amazon Elastic Compute Cloud
     Documentation*](../../../ec2.md "../../../ec2.md").


    If **Join status** indicates that your gateway is
     already joined to an Active Directory domain, proceed to the next step.
     Otherwise, do the following:




    	1. Choose **Configure**.
    	2. For **Domain**, enter the name of the Active
    	 Directory domain that you want your gateway to join.
    	3. Enter the **Username** and
    	 **Password** that the gateway will use to
    	 join the domain.
    	4. (Optional) For **Organization unit (OU)**,
    	 enter the designated OU that your Active Directory uses for new
    	 computer objects.
    	5. (Optional) For **Domain controller(s) (DC)**,
    	 enter the name of the DC through which your gateway will connect
    	 to Active Directory. You can leave this field blank to allow DNS
    	 to automatically select a DC.
    	6. Choose **Join Active Directory**.
    ###### Note

    Joining a domain creates an Active Directory account in the
     default container (which isn't an organizational unit), using the
     gateway's Gateway ID as the account name (for example, SGW-1234ADE).
     It is not possible to customize the name of this account.

    If your Active Directory environment requires that you pre-stage
     accounts to facilitate the domain join process, you need to create
     this account ahead of time.

    If your Active Directory environment has a designated OU for new
     computer objects, you must specify that OU when joining the
     domain.
    * To grant password-protected access to anyone who provides the guest
     password that you configure, choose **Guest access**.
     Your File Gateway doesn't need to be part of a Microsoft Active
     Directory domain to use this method. Choose
     **Configure** to specify your **Guest
     password**, then choose **Save**.

19. For **User access**, do one of the following to specify which
    SMB clients can access your file share:
    - To grant access to all users that successfully authenticate through
      Active Directory, select **All AD-authenticated
      users**.
    - To allow or deny access to specific users or groups, choose
      **Specific AD-authenticated users or groups**, then
      do the following:
      - For **Allowed users and groups**, choose
        **Add allowed user** or **Add
        allowed group** and enter an Active Directory user
        or group that you want to allow file share access. Repeat this
        process to allow as many users and groups as necessary
      - For **Denied users and groups**, choose
        **Add denied user** or **Add denied
        group** and enter an Active Directory user or group
        that you want to deny file share access. Repeat this process to
        deny as many users and groups as necessary.

###### Note

The **User and group file share access** section appears
only if User authentication is set to **Active
Directory**.

When specifying users or groups, do not include the domain. The domain
name is implied by the membership of the gateway in the specific Active
Directory to which it is joined. 20. (Optional) For **Admin users**, enter a comma-separated list
of Active Directory users and groups. Admin users receive privileges to update
access control lists (ACLs) on all files and folders in the file share. Groups
must be prefixed with the `@` character, for example,
`@group1`. 21. For **Access type**, select one of the following:

    * To allow clients to read and write files on the file share, select
     **Read/Write**.
    * To allow clients to read files but not write to the file share, select
     **Read-only**.


    ###### Note

    For file shares that are mounted on a Microsoft Windows client, if
     you choose **Read-only**, you might see a message
     about an unexpected error keeping you from creating the folder. You
     can ignore this message.

22. For **File and directory access control**, select one of the
    following:
    - To set fine-grained permissions on files and folders in your SMB file
      share, select **Windows Access Control List**. For more
      information, see [Using Microsoft Windows
      ACLs to Control Access to an SMB File Share](smb-acl.md "smb-acl.md").
    - To use POSIX permissions to control access to files and directories
      that are stored through your SMB file share, choose **POSIX
      permissions**.

23. For **Access based enumeration**, do one of the
    following:
    - To make the files and folders on the share visible only to users who
      have read access, select **Hide files and directories where user
      doesn't have permission**.
    - To make the files and folders on the share visible to all users during
      directory enumeration, don't select the check box.

###### Note

Access-based enumeration is a system that filters the enumeration of files
and folders on an SMB file share based on the share's access control lists
(ACLs). 24. For File access options, select one of the following:

    * To optimize the file share’s file buffering strategy using
     opportunistic locking, select **Opportunistic lock**.
     In most cases, activating opportunistic locking improves performance,
     particularly with regard to Windows context menus.
    * To allow the gateway - rather than the SMB client - to control file
     name case sensitivity, select **Force case
     sensitivity**.
    * To deactivate both settings, select
     **Neither**.

###### Note

To avoid file access conflicts, these settings are mutually exclusive and
cannot be activated at the same time. 25. (Optional) For **Automated cache refresh from S3**, choose
**Set cache refresh interval**, then set the time in
**Minutes** or **Days** to refresh the
file share's cache using Time To Live (TTL). TTL is the length of time since the
last refresh. After the TTL interval has elapsed, accessing a directory causes
the File Gateway to refresh that directory's contents from the Amazon S3 bucket.

###### Note

Setting this value shorter than 30 minutes can negatively impact gateway
performance in situations where large numbers of Amazon S3 objects are frequently
created or deleted. 26. For **File ownership and permissions**, select **Give
the S3 bucket owner full ownership of files created by the gateway,
including read, write, edit, and delete permissions** if you want
the AWS account that owns the S3 bucket to have full control of all objects
written to the bucket by your file share.

Choose **Next** when finished. 27. Review the file share configuration. Choose **Edit** to
modify the settings for any section that you want to change. When finished,
choose **Create**.
After your SMB file share is created, you can view its configuration settings in the
AWS Storage Gateway console on the file share's **Details** tab. For
instructions to mount your file share, see [Mount your SMB file share
on your client](using-smb-fileshare.md "using-smb-fileshare.md").
