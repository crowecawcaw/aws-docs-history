

# Understanding how DataSync handles file and object metadata
<a name="metadata-copied"></a>

AWS DataSync can preserve your file or object metadata during a data transfer. How your metadata gets copied depends on your transfer locations and if those locations use similar types of metadata.

## System-level metadata
<a name="metadata-copied-system-level"></a>

In general, DataSync doesn't copy system-level metadata. For example, when transferring from an SMB file server, the permissions you configured at the file system level aren't copied to the destination storage system.

There are exceptions. When transferring between Amazon S3 and other object storage, DataSync does copy some [system-defined object metadata](#metadata-copied-between-object-s3).

## Metadata copied in Amazon S3 transfers
<a name="metadata-copied-amazon-s3"></a>

The following tables describe what metadata DataSync can copy when a transfer involves an Amazon S3 location.

**Topics**
+ [To Amazon S3](#metadata-copied-to-s3)
+ [Between Amazon S3 and other object storage](#metadata-copied-between-object-s3)
+ [Between Amazon S3 and HDFS](#metadata-copied-between-hdfs-s3)

### To Amazon S3
<a name="metadata-copied-to-s3"></a>


| When copying from one of these locations | To this location | DataSync can copy | 
| --- | --- | --- | 
|  +  NFS <br />+  Amazon EFS <br />+  FSx for Lustre <br />+  FSx for OpenZFS <br />+  FSx for ONTAP (using NFS)   |  +  Amazon S3   | The following as Amazon S3 user metadata:+  File and folder modification timestamps <br />+  File and folder access timestamps (DataSync can only do this on a best-effort basis) <br />+  User ID and group ID <br />+  POSIX permissions <br />The file metadata stored in Amazon S3 user metadata is interoperable with NFS shares on file gateways using AWS Storage Gateway. A file gateway enables low-latency access from on-premises networks to data that was copied to Amazon S3 by DataSync. This metadata is also interoperable with FSx for Lustre.<br />When DataSync copies objects that contain this metadata back to an NFS server, the file metadata is restored. Restoring metadata requires granting elevated permissions to the NFS server. For more information, see [Configuring AWS DataSync transfers with an NFS file server](create-nfs-location.md). | 

### Between Amazon S3 and other object storage
<a name="metadata-copied-between-object-s3"></a>


<table>
<thead>
  <tr><th>When copying between these locations</th><th>DataSync can copy</th></tr>
</thead>
<tbody>
  <tr><td> <ul><li> Object storage </li><li> Amazon S3 </li></ul> </td><td rowspan="2"><ul><li> User-defined object metadata </li><li> Object tags </li><li> The following system-defined object metadata: <ul><li> Content-Disposition </li><li> Content-Encoding </li><li> Content-Language </li><li> Content-Type </li></ul> <br /><b>Note</b>: DataSync copies system-level metadata for all objects during an initial transfer. If you <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html">configure your task to transfer only data that has changed</a>, DataSync won't copy system metadata in subsequent transfers unless an object's content or user metadata has also been modified. </li></ul>DataSync doesn't copy other object metadata, such as object access control lists (ACLs), prior object versions, or the Last-Modified key.</td></tr>
  <tr><td> <ul><li> Microsoft Azure Blob Storage </li><li> Amazon S3 </li></ul> </td></tr>
</tbody>
</table>


### Between Amazon S3 and HDFS
<a name="metadata-copied-between-hdfs-s3"></a>


| When copying between these locations | DataSync can copy | 
| --- | --- | 
|  +  Hadoop Distributed File System (HDFS) <br />+  Amazon S3   | The following as Amazon S3 user metadata:+  File and folder modification timestamps <br />+  File and folder access timestamps (DataSync can only do this on a best-effort basis) <br />+  User ID and group ID <br />+  POSIX permissions HDFS uses strings to store file and folder user and group ownership, rather than numeric identifiers, such as UIDs and GIDs. | 

## Metadata copied in NFS transfers
<a name="metadata-copied-nfs"></a>

The following table describes what metadata DataSync can copy between locations that use Network File System (NFS).


| When copying between these locations | DataSync can copy | 
| --- | --- | 
|  +  NFS <br />+  Amazon EFS <br />+  Amazon FSx for Lustre <br />+  Amazon FSx for OpenZFS <br />+  Amazon FSx for NetApp ONTAP (using NFS)   |  +  File and folder modification timestamps <br />+  File and folder access timestamps (DataSync can only do this on a best-effort basis) <br />+  User ID (UID) and group ID (GID) <br />+  POSIX permissions   | 

## Metadata copied in SMB transfers
<a name="metadata-copied-smb"></a>

The following table describes what metadata DataSync can copy between locations that use Server Message Block (SMB).


| When copying between these locations | DataSync can copy | 
| --- | --- | 
|  +  SMB <br />+  Amazon FSx for Windows File Server <br />+  FSx for ONTAP (using SMB)   |  +  File timestamps: access time, modification time, and creation time <br />+  File owner security identifier (SID) <br />+  Standard file attributes: read-only (R), archive (A), system (S), hidden (H), compressed (C), not content indexed (I), encrypted (E), temporary (T), offline (O), and sparse (P) <br />DataSync attempts to copy the archive (A), compressed (C), not context indexed (I), sparse (P), and temporary (T) attributes on a best-effort basis. If these attributes aren't applied on the destination, they're ignored during task verification. <br />+  NTFS discretionary access lists (DACLs), which determine whether to grant access to an object. <br />+  NTFS system access control lists (SACLs), which are used by administrators to log attempts to access a secured object.  <br />**Note**: SACLs are not copied if you use SMB version 1.0. <br />Copying DACLs and SACLs requires granting specific permissions to the Windows user that DataSync uses to access your location using SMB. For more information, see creating a location for [SMB](create-smb-location.md#configuring-smb), [FSx for Windows File Server](create-fsx-location.md), or [FSx for ONTAP](create-ontap-location.md) (depending on the type of location in your transfer).    | 

## Metadata copied in other transfer scenarios
<a name="metadata-copied-different"></a>

DataSync handles metadata the following ways when copying between these storage systems (most of which have different metadata structures).


<table>
<thead>
  <tr><th>When copying from one of these locations</th><th>To one of these locations</th><th>DataSync can copy</th></tr>
</thead>
<tbody>
  <tr><td> <ul><li> SMB </li><li> FSx for Windows File Server </li><li> FSx for ONTAP (using SMB) </li></ul> </td><td> <ul><li> Amazon EFS </li><li> FSx for Lustre </li><li> FSx for OpenZFS </li><li> FSx for ONTAP (using NFS) </li><li> Amazon S3 </li><li> Object storage </li><li> Azure Blob Storage </li><li> NFS </li></ul> </td><td><a href="#POSIX-metadata">Default POSIX metadata</a> for all files and folders on the destination file system or objects in the destination S3 bucket. This approach includes using the default POSIX user ID and group ID values.<br />Windows-based metadata (such as ACLs) is not preserved.</td></tr>
  <tr><td> <ul><li> Object storage </li><li> Amazon S3 </li><li> Azure Blob Storage </li></ul> </td><td> <ul><li> Amazon EFS </li><li> FSx for Lustre </li><li> FSx for OpenZFS </li><li> FSx for ONTAP (using NFS) </li></ul> </td><td><a href="#POSIX-metadata">Default POSIX metadata</a> on the destination files and folders. This approach includes using the default POSIX user ID and group ID values.</td></tr>
  <tr><td> <ul><li> Amazon EFS </li><li> FSx for Lustre </li><li> FSx for OpenZFS </li><li> FSx for ONTAP (using NFS) </li></ul> </td><td> <ul><li> Azure Blob Storage </li></ul> </td><td>The following as user-defined metadata:<ul><li> File and folder modification timestamps </li><li> File and folder access timestamps (DataSync can only do this on a best-effort basis) </li><li> User ID and group ID </li><li> POSIX permissions </li></ul></td></tr>
  <tr><td> <ul><li> HDFS </li></ul> </td><td> <ul><li> Amazon EFS </li><li> FSx for Lustre </li><li> FSx for OpenZFS </li><li> FSx for ONTAP (using NFS) </li></ul> </td><td><ul><li> File and folder modification timestamps </li><li> File and folder access timestamps (DataSync can only do this on a best-effort basis) </li><li> POSIX permissions </li></ul>HDFS stores file and folder user and group ownership as strings rather than numeric identifiers (such as UIDs and GIDs). Default values for UIDs and GIDs are applied on the destination file system. For more information, see <a href="#POSIX-metadata">Understanding when and how DataSync applies default POSIX metadata</a>.</td></tr>
  <tr><td> <ul><li> Amazon S3 </li><li> Amazon EFS </li><li> FSx for Lustre </li><li> FSx for OpenZFS </li><li> FSx for Windows File Server </li><li> FSx for ONTAP </li></ul> </td><td> <ul><li> HDFS </li></ul> </td><td>File and folder timestamps from the source location. The file or folder owner is set based on the HDFS user or Kerberos principal you specified when creating the <a href="create-hdfs-location.md">HDFS transfer location</a>. The Groups Mapping configuration on the Hadoop cluster determines the group.</td></tr>
  <tr><td> <ul><li> Amazon S3 </li><li> Amazon EFS </li><li> FSx for Lustre </li><li> FSx for OpenZFS </li><li> FSx for ONTAP (using NFS) </li><li> Object storage </li><li> NFS </li><li> HDFS </li></ul> </td><td> <ul><li> SMB </li><li> FSx for Windows File Server </li><li> FSx for ONTAP (using SMB) </li></ul> </td><td rowspan="2">File and folder timestamps from the source location. Ownership is set based on the Windows user that was specified in DataSync to access the Amazon FSx or SMB share. Permissions are inherited from the parent directory.</td></tr>
  <tr><td> <ul><li> Azure Blob Storage </li></ul> </td><td> <ul><li> FSx for Windows File Server </li><li> FSx for ONTAP (using SMB) </li></ul> </td></tr>
</tbody>
</table>


## Understanding when and how DataSync applies default POSIX metadata
<a name="POSIX-metadata"></a>

DataSync applies default POSIX metadata in the following situations:
+ When your transfer's source and destination locations don't have similar metadata structures
+ When metadata is missing from the source location

The following table describes how DataSync applies default POSIX metadata during these types of transfers:


| Source | Destination | File permissions | Folder permissions | UID | GID | 
| --- | --- | --- | --- | --- | --- | 
|  +  Amazon S31 <br />+  Object storage1 <br />+  Microsoft Azure Blob Storage1   |  +  Amazon EFS <br />+  FSx for Lustre <br />+  FSx for OpenZFS <br />+  FSx for ONTAP (using NFS) <br />+  NFS   | 0755 | 0755 | 65534 | 65534 | 
|  +  SMB   |  +  Amazon S3 <br />+  Object storage <br />+  Amazon EFS <br />+  FSx for Lustre <br />+  FSx for OpenZFS <br />+  FSx for ONTAP (using NFS) <br />+  NFS   | 0644 | 0755 | 65534 | 65534 | 
|  +  HDFS   |  +  Amazon EFS <br />+  FSx for Lustre <br />+  FSx for OpenZFS <br />+  FSx for ONTAP (using NFS) <br />+  NFS   | 0644 | 0755 | 65534 | 65534 | 

1 In cases where the objects don't have metadata that was previously applied by DataSync.