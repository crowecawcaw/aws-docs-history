# Support for file attributes in

Amazon S3 File Gateway

Amazon S3 File Gateway supports DOS or Windows file attributes by default. Using S3 File Gateway, you can
preserve file data and metadata and update settings — such as marking items as
archived when they are placed in Amazon S3. For more information about DOS and Windows file
attributes, see the [File Attribute Constants](https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants "https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants") article on the Windows app development documentation
website.

S3 File Gateway supports the following attributes:

- _ReadOnly_ – The S3 File Gateway prevents changes to files that
  have the ReadOnly attribute set.
- _Archive_ – The S3 File Gateway sets this attribute when files
  are first added to the gateway.

###### Note

Backup applications commonly backup files that have the Archive bit set and
then clear the bit after successful backup.

- _Hidden_ – Server Message Block (SMB) clients hide files
  that use this bit set.
- _System_ – This attribute persists once you have set
  it.
  When you copy a file to the S3 File Gateway with the attributes set, the file's DOS or Windows
  attributes are preserved on the S3 File Gateway and in Amazon S3. You can update these attributes for
  files on the gateway, and those updates also apply to the object in Amazon S3. If a file is
  evicted from the gateway the gateway pull the file, its metadata, and its persistent
  attributes from Amazon S3 when you request.

###### Note

DOS attributes are only supported on SMB shares and if access is controlled by Windows
Access Control Lists.
