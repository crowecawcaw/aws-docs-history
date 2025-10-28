# Store Application Icon, Setup Script, Session Script,

and VHD in an S3 Bucket

You must store the application icons, setup scripts, session scripts, and VHDs that
you use for your applications and app blocks in an Amazon Simple Storage Service (Amazon S3) bucket in your AWS
account. AppStream 2.0 Elastic fleets download the application icon, setup script, and VHD from
the S3 bucket when your user starts their streaming session. The S3 bucket must reside
in the AWS Region that you intend to create AppStream 2.0 Elastic fleets within.

We recommend that you create a new S3 bucket that is used to store only the
application icons, setup scripts, session scripts, and VHDs that you intend to use with
Elastic fleets. We also recommend enabling versioning on the S3 bucket. This allows
reverting to previous object versions if necessary. For more information about how to
create a new S3 bucket, see [Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"). For more information about how to manage object versioning, see
[Using
versioning in S3 buckets](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md").

###### Note

AppStream 2.0 uses your VPC to access the S3 bucket you select. The VPC you choose for
your fleet must provide sufficient network access to the S3 bucket.

Make sure that your S3 bucket content is not encrypted using keys that you manage
(Customer Managed Keys).

Currently, S3 buckets configured to use server-side encryption with
customer-provided encryption keys (SSE-C) are not supported for Elastic fleets. If
you require encryption at rest for your S3 objects, server-side encryption with
Amazon S3-managed encryption keys (SSE-S3) is an option that will work for Elastic
fleets.

###### Topics

- [Amazon S3 Bucket Permissions](s3-permissions.md "s3-permissions.md")
