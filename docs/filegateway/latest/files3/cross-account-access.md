# Using a file share for cross-account access

_Cross-account_ access is when an Amazon Web Services account and users for that
account are granted access to resources that belong to another Amazon Web Services account. With
File Gateways, you can use a file share in one Amazon Web Services account to access objects in an
Amazon S3 bucket that belongs to a different Amazon Web Services account.

###### To use a file share owned by one Amazon Web Services account to access an S3 bucket in a

different Amazon Web Services account

1. Make sure that the S3 bucket owner has granted your Amazon Web Services account access to
   the S3 bucket that you need to access and the objects in that bucket. For
   information about how to grant this access, see [Example 2:
   Bucket owner granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md") in the
   _Amazon Simple Storage Service User Guide_. For a list of the required permissions, see
   [Granting access to an Amazon S3 bucket](grant-access-s3.md "grant-access-s3.md").
2. Make sure that the IAM role that your file share uses to access the S3 bucket
   includes permissions for operations such as `s3:GetObjectAcl` and
   `s3:PutObjectAcl`. In addition, make sure that the IAM role includes
   a trust policy that allows your account to assume that IAM role. For an example of
   such a trust policy, see [Granting access to an Amazon S3 bucket](grant-access-s3.md "grant-access-s3.md").

If your file share uses an existing role to access the S3 bucket, you should
include permissions for `s3:GetObjectAc`l and
`s3:PutObjectAcl` operations. The role also needs a trust policy that
allows your account to assume this role. For an example of such a trust policy, see
[Granting access to an Amazon S3 bucket](grant-access-s3.md "grant-access-s3.md"). 3. Choose **Gateway files acccessible to S3 bucket owner** when
creating your file share or editing file share settings in the
[https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
When you have created or updated your file share for cross-account access and mounted the
file share on-premises, we highly recommend that you test your setup. You can do this by
listing directory contents or writing test files and making sure the files show up as
objects in the S3 bucket.

###### Important

Make sure to set up the policies correctly to grant cross-account access to the
account used by your file share. If you don't, updates to files through your
on-premises applications don't propagate to the Amazon S3 bucket that you're
working with.

## Resources

For additional information about access policies and access control lists, see the
following:

[Guidelines for
using the available access policy options](../../../AmazonS3/latest/dev/access-policy-alternatives-guidelines.md "../../../AmazonS3/latest/dev/access-policy-alternatives-guidelines.md") in the
_Amazon Simple Storage Service User Guide_

[Access Control
List (ACL) overview](../../../AmazonS3/latest/dev/acl-overview.md "../../../AmazonS3/latest/dev/acl-overview.md") in the _Amazon Simple Storage Service User Guide_
