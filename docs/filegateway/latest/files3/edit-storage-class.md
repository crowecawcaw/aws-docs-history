# Edit settings for your NFS file share

Use the following procedure to edit settings for an existing NFS file share after you
create it.

###### Note

You cannot edit an existing file share to point to a new bucket or access point,
or modify the VPC endpoint settings. You can configure those settings only when
creating a new file share.

###### To edit the file share settings

1.  Open the Storage Gateway console at
    [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2.  Choose **File shares**, and then choose the file share that
    you want to update.
3.  For **Actions**, choose **Edit file share
    settings**.
4.  For **File share name**, enter a name for the file
    share.
5.  For **Audit logs**, select one of the following:

        * To create a new log group for this file share, choose **Create
         a new log group**.
        * To send health and resource notifications for this file share to an
         existing log group, choose **Use and existing log**
         group, and then choose the desired group from the list.
        * To turn off logging for this file share, choose **Deactivate
         logging**.

    For more information about audit logs, see [Understanding S3 File Gateway audit logs](monitoring-file-gateway.md#audit-logs "monitoring-file-gateway.md#audit-logs").

6.  For **Non-gateway file cache refresh time**, choose
    **Set refresh interval**, and then set the time in
    **Minutes** or **Days** to refresh the
    file share's cache using Time To Live (TTL). TTL is the length of time since the
    last refresh. After the TTL interval has elapsed, accessing a directory causes
    the File Gateway to refresh that directory's contents from the Amazon S3
    bucket.

###### Note

Setting this value shorter than 30 minutes can negatively impact gateway
performance in situations where large numbers of Amazon S3 objects are frequently
created or deleted. 7. For **Upload events settling time**, choose **Set
settling time**, and then enter the settling time in seconds.
**Settling time** controls the minimum delay between the
most recent client write operation and generation of the
`ObjectUploaded` log notification. Because clients can make many
small writes to files in a short time, we recommend setting this parameter for
as long as possible to avoid generating multiple notifications for the same file
in rapid succession. For more information, see [Getting file upload notification](monitoring-file-gateway.md#get-file-upload-notification "monitoring-file-gateway.md#get-file-upload-notification"). 8. For **Storage class for new objects**, choose a storage class
from the dropdown list. For more information about storage classes, see [Using
storage classes with a File Gateway](storage-classes.md#ia-file-gateway "storage-classes.md#ia-file-gateway"). 9. Under **Object metadata**, do the following:

    1. Select **Guess MIME type** if you want to allow
     Storage Gateway to guess the media type for uploaded objects based on their file
     extensions.
    2. Select **Gateway files accessible to S3 bucket
     owner**, if you want the AWS account that owns the S3
     bucket to have full ownership of files created by the gateway, including
     read, write, edit, and delete permissions.

10. Select **Enable requester pays** if you want the file
    requester rather than the bucket owner to pay the cost of the data request and
    download from the S3 bucket.
11.
12. For **Access level**, choose one of the following:
    - **Root squash (default)**: Access for the remote
      superuser (root) is mapped to UID (65534) and GID (65534).
    - **All squash**: All user access is mapped to User ID
      (UID) (65534) and Group ID (GID) (65534).
    - **No root squash**: The remote superuser (root)
      receives access as root.

13. For **Export as**, select one of the following:
    - To allow clients to read and write files on the file share, select
      **Read/Write**.
    - To allow clients to read files but not write to the file share, select
      **Read-only**.

    ###### Note

    For file shares that are mounted on a Microsoft Windows client, if
    you choose **Read-only**, you might see a message
    about an unexpected error keeping you from creating the folder. You
    can ignore this message.

14. When you are done editing settings, choose **Save
    changes**.
