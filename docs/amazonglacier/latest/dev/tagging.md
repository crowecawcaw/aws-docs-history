**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Tagging Amazon Glacier Resources

A _tag_ is a label that you assign to an AWS resource. Each tag
consists of a _key_ and a _value_, both of which you
define. You can assign the tags that you define to Amazon Glacier (Amazon Glacier) vault resources. Using
tags is a simple yet powerful way to manage AWS resources and organize data, including billing
data.

###### Topics

- [Tagging Basics](#tagging-basics "#tagging-basics")
- [Tag Restrictions](#tagging-restrictions "#tagging-restrictions")
- [Tracking Costs Using Tagging](#tagging-billing "#tagging-billing")
- [Managing Access Control with Tagging](#tagging-access-control "#tagging-access-control")
- [Related Sections](#related-sections-tagging "#related-sections-tagging")

## Tagging Basics

You use the Amazon Glacier console, AWS Command Line Interface (AWS CLI), or Amazon Glacier API to complete the
following tasks:

- Adding tags to a vault
- Listing the tags for a vault
- Removing tags from a vault

For information about how to add, list, and remove tags, see [Tagging Your Amazon Glacier Vaults](tagging-vaults.md "tagging-vaults.md").

You can use tags to categorize your vaults. For example, you can categorize vaults by
purpose, owner, or environment. Because you define the key and value for each tag, you can
create a custom set of categories to meet your specific needs. For example, you might define a
set of tags that helps you track vaults by owner and purpose for the vault. Following are a
few examples of tags:

- Owner: Name
- Purpose: Video archives
- Environment: Production

## Tag Restrictions

Basic tag restrictions are as follows:

- The maximum number of tags for a resource (vault) is 50.
- Tag keys and values are case-sensitive.

Tag key restrictions are as follows:

- Within a set of tags for a vault, each tag key must be unique. If you add a tag with a
  key that's already in use, your new tag overwrites the existing key-value pair.
- Tag keys cannot start with `aws:` because this prefix is reserved for use
  by AWS. AWS can create tags that begin with this prefix on your behalf, but you can't
  edit or delete them.
- Tag keys must be from 1 to 128 Unicode characters in length.
- Tag keys must consist of the following characters: Unicode letters, digits, spaces,
  and the following special characters: `_ . / = + - @`.

Tag value restrictions are as follows:

- Tag values must be from 0 to 255 Unicode characters in length.
- Tag values can be blank. Otherwise, they must consist of the following characters:
  Unicode letters, digits, spaces, and any of the following special characters: `_ . /
= + - @`.

## Tracking Costs Using Tagging

You can use tags to categorize and track your AWS costs. When you apply tags to any
AWS resources, including vaults, your AWS cost allocation report includes usage and costs
aggregated by tags. You can apply tags that represent business categories (such as cost
centers, application names, and owners) to organize your costs across multiple services. For
more information, see [Use Cost Allocation Tags
for Custom Billing Reports](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.

## Managing Access Control with Tagging

You can use tags as a condition in an access policy statement. For example, you can set up
a legal hold tag and include it as a condition in a data retention policy that states that
“archive deletion from everyone will be denied if the legal hold tag value is set to
`True`.” You can deploy the data retention policy and set the legal hold tag to
`False` under normal conditions. If your data must be put on hold to assist an
investigation, you can easily turn on the legal hold by setting the tag value to
`True` and removing the hold in a similar way later on. For more information, see
[Controlling Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
_IAM User Guide_.

## Related Sections

- [Tagging Your Amazon Glacier Vaults](tagging-vaults.md "tagging-vaults.md")
