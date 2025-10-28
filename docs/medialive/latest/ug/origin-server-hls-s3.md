# HLS output group to Amazon S3

Follow this procedure if you [determined](identify-downstream-system.md "identify-downstream-system.md") that you will create an HLS output group with Amazon S3 as the
destination. You and the operator of the downstream system must agree about the
destination for the output of the HLS output group.

###### To arrange setup of the destination

1. Decide if you need two destinations for the output:
   - You need two destinations in a [standard channel](plan-redundancy.md "plan-redundancy.md").
   - You need one destination in a single-pipeline channel.

2. We recommend that you design the full path of the destination — the
   Amazon S3 bucket and all the folders. See [Design the path for the
   output destination](hls-destinations-design-step.md "hls-destinations-design-step.md").
3. Ask the Amazon S3 user to create any buckets that don't already exist.

With MediaLive, the Amazon S3 bucket name must not use dot notation, which means it
mustn't use . (dot) between the words in the bucket name. 4. Discuss ownership with the Amazon S3 user. If the bucket belongs to another
AWS account, you typically want that account to become the owner of the
output. For more information, see [Controlling access to the
output](#setting-dss-hls-canned-acl "#setting-dss-hls-canned-acl"), after this procedure.
Note that you don't need user credentials to send to an S3 bucket. MediaLive has
permission to write to the S3 bucket via the trusted entity. Someone in your
organization should have already set up these permissions. For more information, see
[Access requirements for the trusted entity](trusted-entity-requirements.md "trusted-entity-requirements.md").

## Controlling access to the

output

You might be sending output files to an Amazon S3 bucket that is owned by another
AWS account. In this situation, you typically want the other account to become
the owner of the output files (the object being put in the bucket). If the
bucket owner doesn't become the object owner, you (MediaLive) will be the only agent
that can delete the files when the files are no longer required.

It is therefore in everyone's interest to transfer ownership of the output
files after they are in the Amazon S3 bucket.

To transfer object ownership, the following setup is required:

- The bucket owner must add a bucket permissions policy that grants you
  permission to add an Amazon S3 canned access control list (ACL) when MediaLive
  delivers the output files to the bucket. The bucket owner should read
  the information in [Managing access
  with ACLs](../../../AmazonS3/latest/userguide/acls.md "../../../AmazonS3/latest/userguide/acls.md") in the Amazon Simple Storage Service user guide. The bucket owner must
  set up ACL permissions for the bucket, not for the objects.
- The bucket owner should also set up object ownership. This feature
  effectively makes it mandatory (rather than optional) for the sender
  (MediaLive) to include the _Bucket owner full
  control_ ACL. The bucket owner should read the information
  in [Controlling object ownership](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") in the Amazon Simple Storage Service user
  guide.

If the bucket owner implements this feature, then you must set up
MediaLive to include the ACL. If you don't, delivery to the Amazon S3 bucket will
fail.

- You must set up MediaLive to include the *Bucket
  owner full control*ACL
  when it delivers to the bucket. You will perform this setup when you
  [create the
  channel](hls-destinations-s3-specify.md "hls-destinations-s3-specify.md").

The S3 canned ACL feature supports ACLs other than _Bucket owner full control_, but those other ACLs are typicallly
not applicable to the use case of delivering video from MediaLive.
