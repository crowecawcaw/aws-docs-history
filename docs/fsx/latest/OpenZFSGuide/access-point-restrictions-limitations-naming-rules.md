# Access points naming rules, restrictions, and limitations

When creating an S3 access point you choose a name for it. The following topics provide information about S3 access point naming rules and restrictions and limitations.

###### Topics

- [Access points naming rules](#access-points-naming-rules "#access-points-naming-rules")
- [Access points restrictions and limitations](#access-points-restrictions-limitations "#access-points-restrictions-limitations")

## Access points naming rules

When you create an S3 access point you choose its name. Access point names do not need to be
unique across AWS accounts or AWS Regions. The same AWS account may create access points with the same name in different
AWS Regions or two different AWS accounts may use the same access point name. However, within a single AWS Region an
AWS account may not have two identically named access points.

S3 access point names can't end with the suffix `-ext-s3alias`, which is reserved for
access point alias. For a complete list of access point naming rules, see
[Naming rules for Amazon S3 access points](../../../AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.md#access-points-names "../../../AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.md#access-points-names")
in the _Amazon Simple Storage Service User Guide_.

## Access points restrictions and limitations

S3 access points attached to FSx for OpenZFS volumes have the following restrictions, which do not apply to access points attached to S3 buckets:

- S3 access points can only be attached to volumes that are hosted on high-availability (HA) Multi-AZ and Single-AZ FSx for OpenZFS file systems.
  For more information about the types of FSx for OpenZFS file systems, see [Availability and durability for Amazon FSx for OpenZFS](availability-durability.md "availability-durability.md").
- The maximum number of S3 access points that can be attached to an FSx for OpenZFS (HA) file system is dependent on the file system's throughput. For more information,
  see [Resource quotas for each file
  system](limits.md#limits-openzfs-resources-file-system "limits.md#limits-openzfs-resources-file-system").
- S3 access control lists (ACLs) are not supported.
- The same AWS account must own the FSx for OpenZFS file system and the S3 access point.

You can only create S3 access points that are attached to FSx for OpenZFS volumes that you own. You cannot create an S3 access point that is attached
to a volume owned by another AWS account.

For a complete list of all access point restrictions and limitations, see
[Restrictions and limitations for access points](../../../AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.md "../../../AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.md")
in the _Amazon Simple Storage Service User Guide_.
