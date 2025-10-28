# Creating an access point

You can create and manage S3 access point that attach to Amazon FSx volumes
using the Amazon FSx console, CLI, API, and supported SDKs.

The maximum number of S3 access points that can be attached to an FSx for OpenZFS (HA) file system is dependent on the file system's throughput. For more information,
see [Resource quotas for each file
system](limits.md#limits-openzfs-resources-file-system "limits.md#limits-openzfs-resources-file-system").

###### Note

Because you might want to publicize your S3 access point name so that other users can use the
access point, avoid including sensitive information in the S3 access point name. Access point names are
published in a publicly accessible database known as the Domain Name System
(DNS). For more information about access point names, see
[Access points naming rules](access-point-restrictions-limitations-naming-rules.md#access-points-naming-rules "access-point-restrictions-limitations-naming-rules.md#access-points-naming-rules").

## Required permissions

The following permissions are required to create an S3 access point attached to an Amazon FSx volume:

- `fsx:CreateAndAttachS3AccessPoint`
- `s3:CreateAccessPoint`
- `s3:GetAccessPoint`

The `s3:PutAccessPointPolicy` permission is required to create an optional Access Point policy using either the Amazon FSx or S3 console. For more information, see
[IAM access point policies](s3-ap-manage-access-fsx.md#access-points-policies "s3-ap-manage-access-fsx.md#access-points-policies").

To create an access point, see the following topics.

###### Topics

- [Creating access points](create-access-points.md "create-access-points.md")
- [Creating access points restricted to a virtual private cloud](access-points-vpc.md "access-points-vpc.md")
