# Managing access point access

You can configure each S3 access point with distinct permissions and network controls that S3 applies for any request that
is made using that access point. S3 access points support AWS Identity and Access Management (IAM) resource policies that you can use to control the use of the access point by resource, user, or other conditions.
For an application or user to access files through an access point, both the access point and the underlying volume must permit the request.
For more information, see [IAM access point policies](#access-points-policies "#access-points-policies").

###### Topics

- [File system user identity](#file-system-user-identity "#file-system-user-identity")
- [Server-side encryption with Amazon FSx (SSE-FSX)](#data-encryption "#data-encryption")
- [IAM access point policies](#access-points-policies "#access-points-policies")

## File system user identity

Each access point attached to an FSx for OpenZFS volume uses a file system user identity that you specify for authorizing all file access requests
that are made using the access point. The file system user is a user account on the underlying Amazon FSx file system. If the file system user has
_read-only_ access, then only read requests made using the access point are authorized, and write requests are blocked.
If the file system user has read-write access, then both read and write requests to the attached volume made using the access point are authorized.

You can also configure an S3 access point to only accept requests from a specific virtual private
cloud (VPC) to restrict data access. For more information, see [Creating access points restricted to a virtual private cloud](access-points-vpc.md "access-points-vpc.md").

Amazon S3 access points attached to an FSx for OpenZFS volume are automatically configured with block
public access enabled, which you cannot change.

###### Important

Attaching an S3 access point to an FSx for OpenZFS volume doesn't change the volume's behavior when the volume is
accessed directly via NFS. All existing operations against the volume will continue to work as before. Restrictions that you
include in an S3 access point policy apply only to requests made using the access point.

## Server-side encryption with Amazon FSx (SSE-FSX)

All Amazon FSx file systems have encryption configured by default and are encrypted at rest with keys managed
using AWS Key Management Service. Data is automatically encrypted and decrypted by on the file system as data is being written
to and read from the file system. These processes are handled transparently by Amazon FSx.

## IAM access point policies

Amazon S3 access points support AWS Identity and Access Management (IAM) resource policies that allow you to control the use
of the access point by resource, user, or other conditions. For an application or user to be able to
access objects through an access point, both the access point and the underlying data source must permit the
request.

The `s3:PutAccessPointPolicy` permission is required to create an optional access point policy.

After you attach an S3 access point to an Amazon FSx volume, all existing operations against the volume will continue
to work as before. Restrictions that you include in an access point policy apply only to requests made through that
access point. For more information, see
[Configuring IAM policies for using access points](../../../AmazonS3/latest/userguide/access-points-policies.md "../../../AmazonS3/latest/userguide/access-points-policies.md")
in the _Amazon Simple Storage Service User Guide_.

You can configure an access point policy when you create an access point attached to an FSx for OpenZFS volume using the Amazon FSx console.
To add, modify, or delete an access point policy on an existing S3 access point, you can use the S3 console, CLI, or API.
