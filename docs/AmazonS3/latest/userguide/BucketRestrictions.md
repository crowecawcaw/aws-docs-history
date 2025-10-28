# General purpose bucket quotas, limitations, and restrictions

An Amazon S3 general purpose bucket is owned by the AWS account that created it. Bucket ownership is not
transferable to another account.

## Bucket quotas

By default, you can create up to 10,000 general purpose buckets
per AWS account. To request a quota increase for general purpose buckets,
visit the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/home/services/s3/quotas/ "https://console.aws.amazon.com/servicequotas/home/services/s3/quotas/").

###### Important

We strongly recommend using only paginated `ListBuckets` requests. Unpaginated `ListBuckets` requests are only supported for
AWS accounts set to the default general purpose bucket quota of 10,000. If you have an approved
general purpose bucket quota above 10,000, you must send paginated `ListBuckets` requests to list your account’s buckets.
All unpaginated `ListBuckets` requests will be rejected for AWS accounts with a general purpose bucket quota
greater than 10,000.

###### Note

You must use the following AWS Regions to view your quota, bucket utilization, or request an increase for your general purpose buckets in your AWS account.

- General purpose bucket quotas for commercial Regions can only be viewed and managed
  from US East (N. Virginia).
- General purpose bucket quotas for AWS GovCloud (US) can only be viewed and managed from
  AWS GovCloud (US-West).

For information about service quotas, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the
_Amazon Web Services General Reference_.

## Objects and bucket limitations

There is no max bucket size or limit to the number of objects that you can store in a bucket. You can
store all of your objects in a single bucket, or you can organize them across several
buckets. However, you can't create a bucket from within another bucket.

## Bucket naming rules

When you create a bucket, you choose its name and the AWS Region to create it in.
After you create a bucket, you can't change its name or Region. For more information
about bucket naming, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").
