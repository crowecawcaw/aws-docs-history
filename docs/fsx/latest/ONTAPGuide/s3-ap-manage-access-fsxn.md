# Managing access point access

You can configure each S3 access point with distinct permissions and network controls that S3 applies for any request that
is made using that access point. S3 access points support AWS Identity and Access Management (IAM) resource policies that you can use to control the use of the access point by resource, user, or other conditions.
For an application or user to access files through an access point, both the access point and the underlying volume must permit the request.
For more information, see [IAM access point policies](#access-points-for-fsxn-policies "#access-points-for-fsxn-policies").

Amazon S3 access points for FSx for ONTAP use a dual-layer authorization model that combines AWS IAM permissions with file system-level permissions. This approach ensures that data access requests are properly authorized at both the AWS service level and the underlying file system level.

For an application or user to successfully access data through an access point, both the S3 access point policy and the underlying FSx for ONTAP volume must permit the request.

###### Topics

- [File system user identity and authorization](#fsxn-file-system-user-identity "#fsxn-file-system-user-identity")
- [S3 API request authorization](#access-points-for-fsxn-s3-iam-auth "#access-points-for-fsxn-s3-iam-auth")
- [S3 Block Public Access](#access-points-for-fsxn-bpa "#access-points-for-fsxn-bpa")
- [IAM access point policies](#access-points-for-fsxn-policies "#access-points-for-fsxn-policies")

## File system user identity and authorization

When you create an S3 access point for an FSx for ONTAP volume, you specify a file system identity that will be used to authorize all file system requests made through that access point. This file system identity determines what level of access is granted to the underlying files and directories based on the file system's permission model. The file system user is a user account on the underlying Amazon FSx file system. If the file system user has
_read-only_ access, then only read requests made using the access point are authorized, and write requests are blocked.
If the file system user has read-write access, then both read and write requests to the attached volume made using the access point are authorized.

The file system identity can be one of two types:

- **UNIX identity** – Use a UNIX identity (username) when accessing volumes with UNIX security style
- **Windows Identity** – Use a Windows identity (domain and username) when accessing volumes with NTFS security style.

When you specify a UNIX or Windows identity, all S3 API operations performed through the access point are authorized using that user's permissions on the file system.

The file system identity you associate with the access point determines the level of access to files and directories. For example, if you associate the access point with the root UNIX identity (UID 0), which typically has full file access permissions on the file system, then all file operations would be authorized. Conversely, if you associate the access point with a restricted user identity, file operations would be limited to what that user can access based on the file system's permission model.

You should use the UNIX file system identity type for volumes with UNIX security style and the Windows identity type for volumes with NTFS security style. This alignment ensures that the authorization model matches the volume's security configuration.

For UNIX security style volumes, the file system uses mode-bits or NFSv4 ACLs to control access. For NTFS security style volumes, the file system uses Windows ACLs to control access.

###### Important

Attaching an S3 access point to an FSx for ONTAP volume doesn't change the volume's behavior when the volume is
accessed directly via NFS or SMB. All existing operations against the volume will continue to work as before. Restrictions that you
include in an S3 access point policy apply only to requests made using the access point.

## S3 API request authorization

When you make an S3 API request through an access point attached to an FSx for NetApp ONTAP volume, Amazon S3 evaluates the IAM permissions of the calling principal against the access point's IAM resource policy. The IAM principal caller must have the necessary permissions granted through their identity-based policies, and the access point's resource policy must also permit the requested action.

Amazon S3 evaluates all relevant policies—including user policies, the access point policy, VPC endpoint policies, and service control policies—to determine whether to authorize the request.

You can also configure an S3 access point to only accept requests from a specific virtual private
cloud (VPC) to restrict data access. For more information, see [Creating access points restricted to a virtual private cloud](access-points-for-fsxn-vpc.md "access-points-for-fsxn-vpc.md").

## S3 Block Public Access

Amazon S3 access points attached to an FSx for ONTAP volume are automatically configured with block
public access enabled, which you cannot change.

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

You can configure an access point policy when you create an access point attached to an FSx for ONTAP volume using the Amazon FSx console.
To add, modify, or delete an access point policy on an existing S3 access point, you can use the S3 console, CLI, or API.
