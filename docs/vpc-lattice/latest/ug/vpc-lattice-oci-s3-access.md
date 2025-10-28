# Amazon S3 access

In addition to the OCI Managed Backup to Amazon S3, you can create a managed integration
that enables access to Amazon S3 from the ODB network. When you modify the Oracle Database@AWS network to
enable the Amazon S3 Access managed integration, VPC Lattice provisions a resource
configuration called `odb-s3-access` in the default service network. You can
use this integration to access Amazon S3 for your own needs including self-managed backups or
restores. You can establish perimeter control by providing an auth policy.

## Considerations

The following are considerations for the Amazon S3 Access managed integration:

- You can create only one Amazon S3 Access managed integration for the ODB network.
- This managed integration enables access to Amazon S3 from the ODB network
  only, and not from other VPC associations or service-network endpoints in
  the default service network.
- You can't access S3 buckets in different AWS Regions.

## Enable the Amazon S3 Access managed integration

Use the following command to enable the Amazon S3 Access managed integration:

```
aws odb update-odb-network \
  --odb-network-id odb-network-id \
  --s3-access ENABLED
```

## Secure access with an auth policy

You can secure access to S3 buckets by defining an auth policy using the ODB API. The following example policy grants access
to specific S3 buckets owned by a specific organization.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy1515115909152",
 "Statement": [
 {
 "Sid": "GrantAccessToMyOrgS3",
 "Principal": "*",
 "Action": "s3:*",
 "Effect": "Deny",
 "Resource": [
 "arn:aws:s3:::awsexamplebucket1",
 "arn:aws:s3:::awsexamplebucket1/*"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:ResourceOrgID": "o-abcd1234"
 }
 }
 }
 ]
}`

```

###### Note

The
`aws:SourceVpc`, `aws:SourceVpce`, and
`aws:VpcSourceIp` condition keys aren't supported for S3 bucket policies when using ODB managed integrations.
