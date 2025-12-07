# Access points naming rules, restrictions, and

limitations

Access points are named network endpoints attached to a bucket or a volume on an Amazon FSx file system that simplify managing data.
When you create an access point you choose a name and the AWS Region to create it in. The
following topics provide information about access point naming rules, restrictions and
limitations.

###### Topics

- [Naming rules for access points](#access-points-names "#access-points-names")
- [Restrictions and limitations for access points](#access-points-restrictions-limitations "#access-points-restrictions-limitations")
- [Restrictions and limitations for access points attached to a volume on an Amazon FSx file system](#access-points-restrictions-limitations-fsx "#access-points-restrictions-limitations-fsx")

## Naming rules for access points

When you create an access point, you choose its name and the AWS Region to create it in.
Unlike general purpose buckets access point names do not need to be unique across AWS accounts or
AWS Regions. The same AWS account may create access points with the same name in different
AWS Regions or two different AWS accounts may use the same access point name.
However, within a single AWS Region an AWS account may not have two identically
named access points.

###### Note

If you choose to publicize your access point name, avoid including sensitive information
in the access point name. Access point names are published in a publicly accessible database
known as the Domain Name System (DNS).

Access point names must be DNS-compliant and must meet the following conditions:

- Must be unique within a single AWS account and AWS Region
- Must begin with a number or lowercase letter
- Must be between 3 and 50 characters long
- Can't begin or end with a hyphen (`-`)
- Can't contain underscores (`_`), uppercase letters, spaces, or
  periods (`.`)
- Can't end with the suffix `-s3alias` or `-ext-s3alias`.
  These suffixes are reserved for access point alias names. For more information, see [Access point aliases](access-points-naming.md#access-points-alias "access-points-naming.md#access-points-alias").

## Restrictions and limitations for access points

Amazon S3 access points have the following restrictions and limitations:

- Each access point is associated with exactly one bucket or FSx for OpenZFS volume. You
  must specify this when you create the access point. After you create an access point, you can't
  associate it with a different bucket or FSx for OpenZFS volume. However, you can
  delete an access point, and then create another one with the same name.
- After you create an access point, you can't change its virtual private cloud (VPC)
  configuration.
- Access point policies are limited to 20 KB in size.
- You can create a maximum of 10,000 access points per AWS account per AWS Region.
  If you need more than 10,000 access points for a single account in a single Region, you
  can request a service quota increase. For more information about service quotas
  and requesting an increase, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
  in the _AWS General Reference_.
- You can't use an access point as a destination for S3 Replication. For more
  information about replication, see [Replicating objects within and across Regions](replication.md "replication.md").
- You can't use S3 access point aliases as the source or destination for **Move** operations in the Amazon S3 console.
- You can address access points only by using virtual-host-style URLs. For more
  information about virtual-host-style addressing, see [Accessing an Amazon S3 general purpose bucket](access-bucket-intro.md "access-bucket-intro.md").
- API operations that control access point functionality (for example,
  `PutAccessPoint` and `GetAccessPointPolicy`) don't
  support cross-account calls.
- You must use AWS Signature Version 4 when making requests to an access point by
  using the REST APIs. For more information about authenticating requests, see
  [Authenticating
  Requests (AWS Signature Version 4)](../API/sig-v4-authenticating-requests.md "../API/sig-v4-authenticating-requests.md") in the _Amazon Simple Storage Service API Reference_.
- Access points only support requests over HTTPS. Amazon S3 will automatically respond
  with an HTTP redirect for any requests made via HTTP, to upgrade the request to
  HTTPS.
- Access points don't support anonymous access.
- After you create an access point, you can't change its block public access
  settings.
- Cross-account access points don’t grant you access to data until you are granted
  permissions from the bucket owner. The bucket owner always retains ultimate
  control over access to the data and must update the bucket policy to authorize
  requests from the cross-account access point. To view a bucket policy example, see [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md").
- In AWS Regions where you have more than 1,000 access points, you can't search for an
  access point by name in the Amazon S3 console.
- When you're viewing a cross-account access point in the Amazon S3 console, the
  **Access** column displays **Unknown**. The Amazon S3 console can't determine if public access is
  granted for the associated bucket and objects. Unless you require a public
  configuration for a specific use case, we recommend that you and the bucket
  owner block all public access to the access point and the bucket. For more information,
  see [Blocking public access to your Amazon S3
  storage](access-control-block-public-access.md "access-control-block-public-access.md").

## Restrictions and limitations for access points attached to a volume on an Amazon FSx file system

The following are specific limitations when using access points attached to a volume on an Amazon FSx file system:

- When creating an access points you can only attach the access point to a volume on a Amazon FSx file systems that you own.
  You cannot attach to a volume owned by another AWS account.
- You cannot use the `CreateAccessPoint` API when creating and
  attaching an access point to a volume on a Amazon FSx file system. You must use the [CreateAndAttachS3AccessPoint](../../../fsx/latest/APIReference/API_CreateAndAttachS3AccessPoint.md "../../../fsx/latest/APIReference/API_CreateAndAttachS3AccessPoint.md") API.
- You can not turn off any block public access settings when creating or using an
  access point attached to a volume on an Amazon FSx file system.
- You can't list objects or use **Copy** or **Move**
  operations in the S3 console with access points attached to a volume on an Amazon FSx file system.
- `CopyObject` is supported for access points attached to an FSx for NetApp ONTAP or FSx for OpenZFS volume only if the source and destination are the same access point. For
  more information, about access point compatibility, see [Access point compatibility](access-points-service-api-support.md "access-points-service-api-support.md").
- Multipart uploads are limited to 5GB.
- FSx for OpenZFS deployment type and storage class support varies by AWS Region. For more information, see
  [Availability by AWS Region](../../../fsx/latest/OpenZFSGuide/available-aws-regions.md "../../../fsx/latest/OpenZFSGuide/available-aws-regions.md") in the _OpenZFS User
  Guide_.
