# Access points naming rules, restrictions, and limitations

When creating an S3 access point you choose a name for it. The following topics provide information about S3 access point naming rules and restrictions and limitations.

###### Topics

- [Access points naming rules](#access-points-for-fsxn-naming-rules "#access-points-for-fsxn-naming-rules")
- [Access points restrictions and limitations](#access-points-for-fsxn-restrictions-limitations "#access-points-for-fsxn-restrictions-limitations")

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

S3 access points attached to FSx for ONTAP volumes have the following restrictions, which do not apply to access points attached to S3 buckets:

- You can only create an S3 access point in the same AWS Region as the FSx for ONTAP volume that you are attaching it to.
- The same AWS account must own the FSx for ONTAP file system and the S3 access point. You can only create S3 access points that are attached to FSx for ONTAP volumes that you own. You cannot create an S3 access point that is attached
  to a volume owned by another AWS account.
- You can only create and attach S3 access points to FSx for ONTAP file systems running NetApp ONTAP version 9.17.1 and later.

For a complete list of all access point restrictions and limitations, see
[Restrictions and limitations for access points](../../../AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.md "../../../AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.md")
in the _Amazon Simple Storage Service User Guide_.
