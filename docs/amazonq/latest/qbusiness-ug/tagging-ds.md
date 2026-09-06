

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Tagging resources in Amazon Q Business
<a name="tagging-ds"></a>

Manage your Amazon Q Business data sources, retrievers, and indexes by assigning tags. You can use tags to categorize your Amazon Q Business resources in various ways. For example, you could categorize by purpose, owner, or application, or any combination. Each tag consists of a *key* and a *value*, both of which you define.

Tags help you to do the following:
+ **Identify and organize your AWS resources** – Many AWS services support tagging, so you can assign the same tag to resources in different services to indicate that the resources are related. For example, you can tag an Amazon Kendra retriever and the Amazon Q Business web experience that uses the retriever with the same tag.
+ **Allocate costs** – You activate tags on the AWS Billing and Cost Management dashboard. AWS uses tags to categorize your costs and deliver a monthly cost allocation report to you. For more information, see [Cost Allocation and Tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.
+ **Control access to your resources** – You can use tags in AWS Identity and Access Management (IAM) policies that control access to Amazon Q Business resources. To activate tag-based access control, you can attach these policies to an IAM role or IAM user. For more information, see [Authorization based on tags](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security_iam_service-with-iam.html#security_iam_service-with-iam-tags).

You can create and manage tags using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon Q Business API.

**Topics**
+ [Using tags](#tagging-resources-ds)
+ [Tag restrictions](#tag-restrictions-ds)

## Using tags
<a name="tagging-resources-ds"></a>

If you're using the console, you can tag resources when you create them or add them later. You can also use the console to update or remove tags in the following ways:

------
#### [ Adding tags ]

**To add Amazon Q Business tags**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From **Applications**, select the application whose resources you want to tag.

1. From the application summary page, scroll down and select **Tags**.

1. In **Tags**, from the resource you want to add tags to, select **Manage tags**.

1. In **Tags – *optional***, select **Add new tag** to add tags to your Amazon Q Business resource. Then, enter the following information for each tag:
   + **Key** – Add a key for your tag.
   + **Value - *optional*** – An optional value for your tag.

1. Select **Save**.

------
#### [ Removing tags ]

**To remove tags**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From **Applications**, select the application you want to delete tags from.

1. From the application summary page, scroll down and select **Tags**.

1. In **Tags**, from the resource you want to add tags to, select **Manage tags**.

1. In **Tags – *optional***, select **Remove**.

1. Select **Save**.

------
#### [ Listing tags ]

**To view a list of tags**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From **Applications**, select the application you want to delete tags from.

1. From the application summary page, scroll down and select **Tags**.

1. In **Tags**, each tagged resource will display a list of tags associated with it.

------

If you're using the AWS CLI or the Amazon Q Business API, use the following operations to manage tags for your resources:
+ [CreateApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateApplication.html) – Apply tags when you create an Amazon Q Business application.
+ [CreateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateWebExperience.html) – Apply tags when you create an Amazon Q Business web experience.
+ [ListTagsForResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListTagsForResource.html) – View the tags associated with a resource.
+ [TagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TagResource.html) – Add and modify tags for a resource.
+ [UntagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UntagResource.html) – Remove tags from a resource.

## Tag restrictions
<a name="tag-restrictions-ds"></a>

The following restrictions apply to tags on Amazon Q Business resources:
+ Maximum number of tags – 50
+ Maximum key length – 128 characters
+ Maximum value length – 256 characters
+ Valid characters for key and value – a–z, A–Z, space, and the following characters: \_ . : / = \+ - and @
+ Keys and values are case sensitive
+ Don't use `aws:` as a prefix for keys; it's reserved for AWS use