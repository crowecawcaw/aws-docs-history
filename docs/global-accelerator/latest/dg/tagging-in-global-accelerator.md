# Tagging in AWS Global Accelerator

Tags are words or phrases (metadata) that you use to identify and organize your AWS resources.
You can add multiple tags to each resource, and each tag includes a key and a value that you
define. For example, the key might be `environment` and the value might be
`production`. You can search and filter your resources based on the tags you
add. In AWS Global Accelerator, you can tag accelerators.

The following are two examples of how it can be useful to work with tags in Global Accelerator:

- Use tags to track billing information in different categories. To do this, apply
  tags to accelerators or other AWS resources (such as Network Load Balancers, Application Load Balancers, or Amazon EC2 instances)
  and activate the tags. Then AWS generates a cost allocation report as a
  comma-separated value (CSV file) with your usage and costs aggregated by your active
  tags. You can apply tags that represent business categories (such as cost centers,
  application names, or owners) to organize your costs across multiple services. For
  more information, see [Using Cost
  Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.
- Use tags to enforce tag-based permissions for accelerators. To do this, create
  IAM policies that specify tags and tag values to allow or disallow actions. For more
  information, see [ABAC with Global Accelerator](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").
  For usage conventions and links to other resources about tagging, see [Tagging your AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the
  _AWS General Reference_. For tips on using tags, see [Tagging Best
  Practices: AWS Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf") in the _AWS
  Whitepapers_ blog.

For the maximum number of tags that you can add to a resource in Global Accelerator, see [Quotas for AWS Global Accelerator](limits-global-accelerator.md "limits-global-accelerator.md").

You can add and update tags by using the AWS console, AWS CLI, or Global Accelerator API. This
chapter includes steps for working with tagging in the console. For more information
about working with tags by using the AWS CLI and the Global Accelerator API, including CLI examples,
see the following operations in the _AWS Global Accelerator API Reference_:

- [CreateAccelerator](../api/CreateAccelerator.md "../api/CreateAccelerator.md")
- [CreateCrossAccountAttachment](../api/CreateCrossAccountAttachment.md "../api/CreateCrossAccountAttachment.md")
- [TagResource](../api/TagResource.md "../api/TagResource.md")
- [UntagResource](../api/UntagResource.md "../api/UntagResource.md")
- [ListTagsForResource](../api/ListTagsForResource.md "../api/ListTagsForResource.md")

## Tagging support in Global Accelerator

AWS Global Accelerator supports tagging for accelerators and cross-account attachments.

Global Accelerator supports the tag-based access control feature of AWS Identity and Access Management (IAM). For more
information, see [ABAC with Global Accelerator](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").

## Adding, editing, and deleting tags in

Global Accelerator

The following procedure explains how to add, edit, and delete tags for accelerators in
the Global Accelerator console.

You can add or remove tags using the console, the AWS CLI, or Global Accelerator API operations.
For more information, including CLI examples, see [TagResource](../api/API_TagResource.md "../api/API_TagResource.md") in the _AWS Global Accelerator API Reference_.

###### To add tags, edit, or delete tags in

Global Accelerator

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. Choose the accelerator that you want to add or update tags for.
3. In the **Tags** section, you can do the following:

**Add a tag**

Choose **Add tag**, then enter a key and,
optionally, a value for the tag.

**Edit a tag**

Update the text for a key, value, or both. You can also clear the
value for a tag, but the key is required.

**Delete a tag**

Choose **Remove** on the right side of the value
field. 4. Choose **Save changes**.
