# Managing your Amazon S3 File Gateway

The topics in this section provide information about how to manage your Amazon S3 File Gateway
resources. Gateway management includes granting permissions for your gateway to access file
shares and Amazon S3 buckets, editing information and settings for gateways and file shares,
deleting file shares, refreshing cached objects, and understanding operational status
indicators for gateways and file shares.

**Topics**

- [Edit basic gateway
  information](edit-gateway-information.md "edit-gateway-information.md") - Learn how to use the Storage Gateway
  console to edit basic information for an existing gateway, including the gateway
  name, time zone, and CloudWatch log group.
- [Granting access and
  permissions](add-file-share.md "add-file-share.md") - Learn how
  use IAM roles to provide your gateway with access permissions for Amazon S3 buckets and
  Amazon VPC endpoints, prevent certain security issues, and connect file shares to buckets
  across AWS accounts.
- [Delete a file share](remove-file-share.md "remove-file-share.md") - Learn how
  to delete a file share using the Storage Gateway console.
- [Editing gateway SMB
  settings](edit-smb-access-settings.md "edit-smb-access-settings.md") - Learn how to edit
  gateway-level SMB settings that control security strategy, Active Directory
  authentication, guest access, local group permissions, and file share visibility for
  the SMB file shares on a gateway.
- [Edit SMB file share
  settings](edit-smbfileshare-settings.md "edit-smbfileshare-settings.md") - Learn how to edit settings
  to configure name, logging, cache refresh, storage class, file export, and more for
  an SMB file share.
- [Limit SMB file share
  access](edit-file-share-access-smb.md "edit-file-share-access-smb.md") - Learn how to add allowed or
  denied users or groups to limit access to your SMB file share.
- [Edit NFS file share
  settings](edit-storage-class.md "edit-storage-class.md") -
  Learn how to edit settings to configure name, logging, cache refresh, storage class,
  file export, and more for an NFS file share.
- [Edit NFS file share metadata
  defaults](edit-metadata-defaults.md "edit-metadata-defaults.md") - Learn how to edit default
  metadata values that include Unix permissions for files and folders on NFS files
  shares.
- [Limit NFS file share access](edit-nfs-client.md "edit-nfs-client.md") - Learn
  how to to limit access to clients from specific IP addresses or IP ranges for your
  NFS fileshare.
- [Refreshing Amazon S3 bucket object
  cache](refresh-cache.md "refresh-cache.md") - Learn how to
  refresh the S3 bucket object cache for a file share and configure a schedule to
  refresh the cache automatically.
- [Using S3 Object Lock](s3-object-lock.md "s3-object-lock.md") - Learn
  about how Amazon S3 File Gateway works with the S3 Object Lock feature.
- [File share status](understand-file-share.md "understand-file-share.md") - Learn how to view and interpret file share status.
- [Gateway status](understand-gateway-status.md "understand-gateway-status.md") - Learn how to view and
  interpret gateway status.
- [Managing bandwidth for your
  Amazon S3 File Gateway](MaintenanceUpdateBandwidth-common.md "MaintenanceUpdateBandwidth-common.md") - Learn how to limit the
  upload throughput from your gateway to AWS to control the amount of network
  bandwidth the gateway uses.
