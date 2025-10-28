# Using cost allocation S3 bucket tags

To track the storage cost or other criteria for individual projects or groups of projects,
label your Amazon S3 buckets using cost allocation tags. A _cost allocation
tag_ is a key-value pair that you associate with an S3 bucket. After you
activate cost allocation tags, AWS uses the tags to organize your resource costs on your
cost allocation report. Cost allocation tags can only be used to label buckets. For
information about tags used for labeling objects, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").

The _cost allocation report_ lists the AWS usage for your account by
product category and linked account user. The report contains the same line items as the
detailed billing report (see [Understanding your AWS billing and usage
reports for Amazon S3](aws-usage-report-understand.md "aws-usage-report-understand.md")) and additional columns for your tag
keys.

AWS provides two types of cost allocation tags, an AWS-generated tag and user-defined
tags. AWS defines, creates, and applies the AWS-generated `createdBy` tag for
you after an Amazon S3 CreateBucket event. You define, create, and apply
_user-defined_ tags to your S3 bucket.

You must activate both types of tags separately in the Billing and Cost Management console
before they can appear in your billing reports. For more information about AWS-generated
tags, see [AWS-Generated Cost Allocation
Tags](../../../awsaccountbilling/latest/aboutv2/aws-tags.md "../../../awsaccountbilling/latest/aboutv2/aws-tags.md").

For more information about activating tags, see [Using cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
in the _AWS Billing User Guide_.

###### User-defined cost allocation tags

A user-defined cost allocation tag has the following components:

- The tag key. The tag key is the name of the tag. For example, in the tag
  project/Trinity, project is the key. The tag key is a case-sensitive string that
  can contain 1 to 128 Unicode characters.

- The tag value. The tag value is a required string. For example, in the tag
  project/Trinity, Trinity is the value. The tag value is a case-sensitive string
  that can contain from 0 to 256 Unicode characters.
  For details on the allowed characters for user-defined tags and other restrictions, see
  [User-Defined Tag
  Restrictions](../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md "../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md") in the _AWS Billing User Guide_. For more
  information about user-defined tags, see [User-Defined Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/custom-tags.md "../../../awsaccountbilling/latest/aboutv2/custom-tags.md") in the
  _AWS Billing User Guide_.

###### S3 bucket tags

Each S3 bucket has a tag set. A _tag set_ contains all of the tags that
are assigned to that bucket. A tag set can contain as many as 50 tags, or it can be
empty. Keys must be unique within a tag set, but values in a tag set don't have to be
unique. For example, you can have the same value in tag sets named project/Trinity and
cost-center/Trinity.

Within a bucket, if you add a tag that has the same key as an existing tag, the new
value overwrites the old value.

AWS doesn't apply any semantic meaning to your tags. We interpret tags strictly as
character strings.

To add, list, edit, or delete tags, you can use the Amazon S3 console, the AWS Command Line Interface (AWS CLI), or
the Amazon S3 API.

## Managing tags for general purpose buckets

You can add or manage tags for general purpose buckets using the Amazon S3 Console, the AWS Command Line Interface (CLI), the AWS SDKs, or using the S3 APIs. For more information, see the following.

###### Using the Amazon S3 Console

To create tags in the console, see:

- [Viewing the properties for an S3 general purpose bucket](view-bucket-properties.md "view-bucket-properties.md").

###### Using the API

To manage tags using the Amazon S3 API, see the following API pages in the _Amazon Simple Storage Service API Reference_.

- [PutBucketTagging](../API/API_PutBucketTagging.md "../API/API_PutBucketTagging.md")
- [GetBucketTagging](../API/API_GetBucketTagging.md "../API/API_GetBucketTagging.md")
- [DeleteBucketTagging](../API/API_DeleteBucketTagging.md "../API/API_DeleteBucketTagging.md")

###### Using the CLI

To manage tags using the AWS CLI, see the following pages
in the AWS CLI Command Reference.

- [put-bucket-tagging](../../../cli/latest/reference/s3api/put-bucket-tagging.md "../../../cli/latest/reference/s3api/put-bucket-tagging.md")
- [get-bucket-tagging](../../../cli/latest/reference/s3api/get-bucket-tagging.md "../../../cli/latest/reference/s3api/get-bucket-tagging.md")
- [delete-bucket-tagging](../../../cli/latest/reference/s3api/delete-bucket-tagging.md "../../../cli/latest/reference/s3api/delete-bucket-tagging.md")

## More Info

- [Using Cost Allocation
  Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_
- [Understanding your AWS billing and usage
  reports for Amazon S3](aws-usage-report-understand.md "aws-usage-report-understand.md")
- [AWS Billing reports for Amazon S3](aws-billing-reports.md "aws-billing-reports.md")
