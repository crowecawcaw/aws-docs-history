# Edit settings for your SMB file

share

You can edit the following settings for an existing SMB file share:

- **File share name** - choose a name for the file share
- **Audit logs** - turn audit logs on or off
- **Existing log group list** - choose an existing log group
  for audit logs
- **Non-gateway file cache refresh time** - specify the
  interval at which to refresh the file share's cache

###### Note

Setting this value shorter than 30 minutes can negatively impact gateway
performance in situations where large numbers of Amazon S3 objects are frequently
created or deleted.

- **Upload events settling time** - specify the number of
  seconds to wait after the last point in time that a client wrote to a file
  before generating an `ObjectUploaded` notification
- **Storage class for new objects** - choose a storage class to
  use for new objects created in your Amazon S3 bucket
- **Guess MIME type** - choose whether you want Storage Gateway to
  guess the MIME type for uploaded objects based on file extensions
- **Gateway files acccessible to S3 bucket owner** - choose
  whether to make files on the gateway accessible to the AWS account that owns
  the Amazon S3 bucket that is linked to the file share
- **Enable requester pays** - choose whether to require
  accounts that read or request data from the file share to to pay for access
  charges, rather than the bucket owner
- **Export as** - choose whether files are exported in
  read-write or read-only state
- **File and directory access controlled by** - choose whether
  to use Windows ACLs or POSIX permissions to control file and directory
  access
- **Opportunistic lock (oplock)** - choose whether allow the
  file share to use opportunistic locking to optimize the file buffering
  strategy
- **Force case sensitivity** - choose whether the client or the
  gateway controls case sensitivity for file and directory names

###### Note

If the file share currently has Force case sensitivity activated, deactivating
it may make files with identical names but different cases (e.g., file.txt, File.txt)
inaccessible. Only one version will remain accessible to case-insensitive clients.

- **Access based enumeration for files and directories** -
  choose whether to make the files and folders on the share visible to all users
  during directory enumeration, or only to users who have read access

###### Note

You cannot edit an existing file share to point to a new bucket or access point,
or modify the VPC endpoint settings. You can configure those settings only when
creating a new file share.

###### To edit the file share settings

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **File shares**, and then choose the file share that
   you want to update.
3. For **Actions**, choose **Edit file share
   settings**.
4. Edit any settings that you want to change.
5. Choose **Save**.
