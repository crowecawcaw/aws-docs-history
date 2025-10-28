# Tags

Manage your indices, data sources, and FAQs by assigning tags or labels. You can use
tags to categorize your Amazon Kendra resources in various ways. For example, by
purpose, owner, or application, or any combination. Each tag consists of a
_key_ and a _value_, both of which you
define.

Tags help you to:

- Identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources in
  different services to indicate that the resources are related. For example, you
  can tag an index and the Amazon Lex bot that uses the index with the
  same tag.
- Allocate costs. You activate tags on the AWS Billing and Cost Management dashboard.
  AWS uses tags to categorize your costs and deliver a monthly
  cost allocation report to you. For more information, see [Cost Allocation
  and Tagging](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in _About AWS Billing and Cost
  Management_.
- Control access to your resources. You can use tags in AWS Identity and Access Management
  (IAM) policies that control access to Amazon Kendra
  resources. You can attach these policies to an IAM role or user
  to activate tag-based access control. For more information, see [Authorization based on tags](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").
  You can create and manage tags using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon Kendra API.

## Tagging resources

If you're using the Amazon Kendra console, you can tag resources when you
create them or add them later. You can also use the console to update or remove
tags.

If you're using the AWS Command Line Interface (AWS CLI) or the Amazon Kendra API, use the following operations to manage tags for your
resources:

- [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md")—Apply tags when you create a data
  source.
- [CreateFaq](../APIReference/API_CreateFaq.md "../APIReference/API_CreateFaq.md")—Apply tags when you create an FAQ.
- [CreateIndex](../APIReference/API_CreateIndex.md "../APIReference/API_CreateIndex.md")—Apply tags when you create an index.
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")—View the tags associated with a
  resource.
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")—Add and modify tags for a resource.
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")—Remove tags from a resource.

## Tag restrictions

The following restrictions apply to tags on Amazon Kendra resources:

- Maximum number of tags—50
- Maximum key length—128 characters
- Maximum value length—256 characters
- Valid characters for key and value—a–z, A–Z, space, and
  the following characters: \_ . : / = + - and @
- Keys and values are case sensitive
- Don't use `aws:` as a prefix for keys; it's reserved for
  AWS use
