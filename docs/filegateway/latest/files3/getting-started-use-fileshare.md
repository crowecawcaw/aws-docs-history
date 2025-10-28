# Mounting and using your file

share

The topics in this section provide instructions about how to mount your file share on your
client, use your file share, test your File Gateway, and clean up resources that are no
longer needed, such as the gateways, Amazon EC2 instances, or and on-premises VMs that you might
create for testing purposes. For more information about supported Network File System (NFS)
and Service Message Block (SMB) clients, see [Supported NFS and SMB clients for
File Gateway](Requirements.md#requirements-s3-fgw-clients "Requirements.md#requirements-s3-fgw-clients").

###### Note

The AWS Management Console also provides example commands that you can use to mount your file
share.

**Topics**

- [Mount your NFS file share on your
  client](GettingStartedAccessFileShare.md "GettingStartedAccessFileShare.md") - Learn how to mount your NFS
  file share on a drive on your client and map it to your Amazon S3 bucket.
- [Mount your SMB file share on your client](using-smb-fileshare.md "using-smb-fileshare.md") - Learn
  how to mount your SMB file share and map to a drive accessible to your
  client.
- [Using file shares on buckets with
  pre-existing objects](FileSharePrexistingObjects.md "FileSharePrexistingObjects.md") - Learn how to export a file share
  on an Amazon S3 bucket with objects created outside of the File Gateway using either NFS
  or SMB.
- [Test your S3 File Gateway](GettingStartedTestFileShare.md "GettingStartedTestFileShare.md") - Learn how to test your gateway
  by copying files and folders to your mapped drive and verifying that they appear in
  your Amazon S3 bucket automatically.
