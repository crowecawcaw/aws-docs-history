# Tagging Amazon Braket resources

A _tag_ is a custom attribute label that you assign or that AWS assigns to an AWS resource. A tag is _metadata_ that tells more about your resource. Each tag consists of a _key_ and a _value_. Together these are known as _key-value pairs_. For tags that you assign, you define the key and value.

In the Amazon Braket console, you can navigate to a quantum task or a notebook and view the list of tags associated with it. You can add a tag, remove a tag, or modify a tag. You can tag a quantum task or notebook upon creation, and then manage associated tags through the console, AWS CLI, or API.

**More about AWS and tags**

- For general information on tagging, including naming and usage conventions, see [What is Tag Editor?](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in the _Tagging AWS Resources and Tag Editor_ User Guide.
- For information about restrictions on tagging, see [Tag naming limits and requirements](../../../tag-editor/latest/userguide/best-practices-and-strats.md#id_tags_naming_best_practices "../../../tag-editor/latest/userguide/best-practices-and-strats.md#id_tags_naming_best_practices") in the _Tagging AWS Resources and Tag Editor_ User Guide.
- For best practices and tagging strategies, see [Best Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").
- For a list of services that support using tags, see the [_Resource Groups Tagging API Reference_](../../../resourcegroupstagging/latest/APIReference/overview.md "../../../resourcegroupstagging/latest/APIReference/overview.md").
  The following sections provide more specific information about tags for Amazon Braket.

###### In this section:

- [Using tags](#tags "#tags")
- [Supported resources for tagging in Amazon Braket](#tag-supported-resources "#tag-supported-resources")
- [Tagging with the Amazon Braket API](#braket-cli-tagging "#braket-cli-tagging")
- [Tagging restrictions](tag-restrictions.md "tag-restrictions.md")
- [Managing tags in Amazon Braket](tag-managing.md "tag-managing.md")
- [Example of AWS CLI tagging in Amazon Braket](braket-tags-example.md "braket-tags-example.md")

## Using tags

Tags can organize your resources into categories that are useful to you. For example, you can assign a "Department" tag to specify the department that owns this resource.

Each tag has two parts:

- A tag key (for example, _CostCenter_, _Environment_, or _Project_). Tag keys are case sensitive.
- An optional field known as a tag value (for example, _111122223333_ or _Production_). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

Tags help you do the following things:

- **Identify and organize your AWS resources.** Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related.
- **Track your AWS costs.** You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs and deliver a monthly cost allocation report to you. For more information, see [Use cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the [_AWS Billing and Cost Management User Guide_](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").
- **Control access to your AWS resources.** For more information, see [Controlling access using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

## Supported resources for tagging in Amazon Braket

The following resource type in Amazon Braket supports tagging:

- [`quantum-task`](braket-manage-access.md#resources "braket-manage-access.md#resources") resource
- **Resource Name:**
  `AWS::Service::Braket`
- **ARN Regex:**
  `arn:${Partition}:braket:${Region}:${Account}:quantum-task/${RandomId}`

**Note:** You can apply and manage tags for your Amazon
Braket notebooks in the Amazon
Braket console, by using the console to navigate to the notebook resource, although the notebooks actually are Amazon SageMaker AI resources. For more information, see [Notebook Instance Metadata](../../../sagemaker/latest/dg/nbi-metadata.md "../../../sagemaker/latest/dg/nbi-metadata.md") in the SageMaker documentation.

## Tagging with the Amazon Braket API

- If you're using the Amazon Braket API to set up tags on a
  resource, call the [`TagResource`API](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

`aws braket tag-resource --resource-arn $YOUR_TASK_ARN --tags {\"city\":\"Seattle\"}`

- To remove tags from a resource, call the [`UntagResource`API](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

`aws braket list-tags-for-resource --resource-arn $YOUR_TASK_ARN`

- To list all tags that are attached to a particular resource, call the [`ListTagsForResource`API](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

`aws braket tag-resource --resource-arn $YOUR_TASK_ARN --tag-keys "[\"city\",\"state\"]"`
