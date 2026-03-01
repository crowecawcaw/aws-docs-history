# Tag a distribution

Tags are words or phrases that you can use to identify and organize your AWS resources.
You can add multiple tags to each resource, and each tag includes a key and a value that you
define. For example, the key might be "domain" and the value might be "example.com". You can
search and filter your resources based on the tags you add.

You can use tags with CloudFront, such as the following examples:

- Enforce tag-based permissions on CloudFront distributions. For more information, see
  [ABAC with CloudFront](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").
- Track billing information in different categories. When you apply tags to CloudFront
  distributions or other AWS resources (such as Amazon EC2 instances or Amazon S3 buckets) and
  activate the tags, AWS generates a cost allocation report as a comma-separated
  value (CSV file) with your usage and costs aggregated by your active tags.

You can apply tags that represent business categories (such as cost centers,
application names, or owners) to organize your costs across multiple services. For
more information about using tags for cost allocation, see [Using cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing User Guide_.

###### Notes

- You can tag distributions, but you can't tag origin access identities or
  invalidations.
- [Tag
  Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") and [Resource groups](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md") aren't currently supported for
  CloudFront.
- For the current maximum number of tags that you can add to a distribution, see
  [General quotas](cloudfront-limits.md#limits-general "cloudfront-limits.md#limits-general").

###### Contents

- [Tag restrictions](tagging.md#tagging-restrictions "tagging.md#tagging-restrictions")
- [Add, edit, and delete tags for distributions](tagging.md#tagging-add-edit-delete "tagging.md#tagging-add-edit-delete")
- [Programmatic tagging](tagging.md#tagging-related-information "tagging.md#tagging-related-information")

## Tag restrictions

The following basic restrictions apply to tags:

- For the maximum number of tags per distribution, see [General quotas](cloudfront-limits.md#limits-general "cloudfront-limits.md#limits-general").
- Maximum key length – 128 Unicode characters
- Maximum value length – 256 Unicode characters
- Valid values for key and value – a-z, A-Z, 0-9, space, and the
  following characters: \_ . : / = + - and @
- Tag keys and values are case sensitive
- Don't use `aws:` as a prefix for keys. This prefix is reserved for
  AWS use.

## Add, edit, and delete tags for distributions

You can use the CloudFront console to manage tags for your distributions.

###### To add tags, edit, or delete tags for a distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose the ID for the distribution that you want to update.
3. Choose the **Tags** tab.
4. Choose **Manage tags**.
5. On the **Manage tags** page, you can do the following:
   - To add a tag, enter a key and, optionally, a value for the tag. Choose
     **Add new tag** to add more tags.
   - To edit a tag, change the tag’s key or its value, or both. You can
     delete the value for a tag, but the key is required.
   - To delete a tag, choose **Remove**.

6. Choose **Save changes**.

## Programmatic tagging

You can also use the CloudFront API, AWS Command Line Interface (AWS CLI), AWS SDKs, and AWS Tools for Windows PowerShell to apply
tags. For more information, see the following topics:

- CloudFront API operations:
  - [ListTagsForResource](../../../cloudfront/latest/APIReference/API_ListTagsForResource.md "../../../cloudfront/latest/APIReference/API_ListTagsForResource.md")
  - [TagResource](../../../cloudfront/latest/APIReference/API_TagResource.md "../../../cloudfront/latest/APIReference/API_TagResource.md")
  - [UntagResource](../../../cloudfront/latest/APIReference/API_UntagResource.md "../../../cloudfront/latest/APIReference/API_UntagResource.md")

- AWS CLI – See [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html") in the _AWS CLI Command Reference_
- AWS SDKs – See the applicable SDK documentation on the [AWS Documentation](../../../index.md "../../../index.md")
  page
- Tools for Windows PowerShell – See [Amazon CloudFront](../../../powershell/latest/reference/items/CloudFront_cmdlets.md "../../../powershell/latest/reference/items/CloudFront_cmdlets.md") in the [AWS Tools for PowerShell Cmdlet Reference](../../../powershell/latest/reference.md "../../../powershell/latest/reference.md")
