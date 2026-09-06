

# Tagging Amazon Braket resources
<a name="braket-tagging-resources"></a>

A *tag* is a custom attribute label that you assign or that AWS assigns to an AWS resource. A tag is *metadata* that tells more about your resource. Each tag consists of a *key* and a *value*. Together these are known as *key-value pairs*. For tags that you assign, you define the key and value.

In the Amazon Braket console, you can navigate to a quantum task or a notebook and view the list of tags associated with it. You can add a tag, remove a tag, or modify a tag. You can tag a quantum task or notebook upon creation, and then manage associated tags through the console, AWS CLI, or API.

**More about AWS and tags**
+ For general information on tagging, including naming and usage conventions, see [What is Tag Editor?](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) in the *Tagging AWS Resources and Tag Editor* User Guide.
+ For information about restrictions on tagging, see [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#id_tags_naming_best_practices) in the *Tagging AWS Resources and Tag Editor* User Guide.
+ For best practices and tagging strategies, see [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html).
+ For a list of services that support using tags, see the [*Resource Groups Tagging API Reference*](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html).

The following sections provide more specific information about tags for Amazon Braket.

**Topics**
+ [Using tags](#tags)
+ [Supported resources for tagging in Amazon Braket](#tag-supported-resources)
+ [Tagging with the Amazon Braket API](#braket-cli-tagging)
+ [Tagging restrictions](tag-restrictions.md)
+ [Managing tags in Amazon Braket](tag-managing.md)
+ [Example of AWS CLI tagging in Amazon Braket](braket-tags-example.md)

## Using tags
<a name="tags"></a>

Tags can organize your resources into categories that are useful to you. For example, you can assign a "Department" tag to specify the department that owns this resource.

Each tag has two parts:
+ A tag key (for example, *CostCenter*, *Environment*, or *Project*). Tag keys are case sensitive.
+ An optional field known as a tag value (for example, *111122223333* or *Production*). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

Tags help you do the following things:
+  **Identify and organize your AWS resources.** Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related.
+  **Track your AWS costs.** You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs and deliver a monthly cost allocation report to you. For more information, see [Use cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the [*AWS Billing and Cost Management User Guide*](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html).
+  **Control access to your AWS resources.** For more information, see [Controlling access using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html).

## Supported resources for tagging in Amazon Braket
<a name="tag-supported-resources"></a>

The following resource type in Amazon Braket supports tagging:
+  [`quantum-task`](https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#resources) resource
+  **Resource Name:** `AWS::Service::Braket` 
+  **ARN Regex:** `arn:${Partition}:braket:${Region}:${Account}:quantum-task/${RandomId}` 

 **Note:** You can apply and manage tags for your Amazon Braket notebooks in the Amazon Braket console, by using the console to navigate to the notebook resource, although the notebooks actually are Amazon SageMaker AI resources. For more information, see [Notebook Instance Metadata](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-metadata.html) in the SageMaker documentation.

## Tagging with the Amazon Braket API
<a name="braket-cli-tagging"></a>
+ If you're using the Amazon Braket API to set up tags on a resource, call the [`TagResource`API](https://docs.aws.amazon.com/braket/latest/APIReference/API_Operations.html).

 `aws braket tag-resource --resource-arn $YOUR_TASK_ARN --tags {\"city\":\"Seattle\"}` 
+ To remove tags from a resource, call the [`UntagResource`API](https://docs.aws.amazon.com/braket/latest/APIReference/API_Operations.html).

 `aws braket list-tags-for-resource --resource-arn $YOUR_TASK_ARN` 
+ To list all tags that are attached to a particular resource, call the [`ListTagsForResource`API](https://docs.aws.amazon.com/braket/latest/APIReference/API_Operations.html).

 `aws braket tag-resource --resource-arn $YOUR_TASK_ARN --tag-keys "[\"city\",\"state\"]"` 