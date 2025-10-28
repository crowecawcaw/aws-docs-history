# Tagging resources in Amazon Q Business

Manage your Amazon Q Business data sources, retrievers, and indexes by
assigning tags. You can use tags to categorize your Amazon Q Business
resources in various ways. For example, you could categorize by purpose, owner, or
application, or any combination. Each tag consists of a _key_ and
a _value_, both of which you define.

Tags help you to do the following:

- **Identify and organize your AWS
  resources** – Many AWS services support tagging, so
  you can assign the same tag to resources in different services to indicate
  that the resources are related. For example, you can tag an Amazon Kendra retriever and the Amazon Q Business web experience that uses the
  retriever with the same tag.
- **Allocate costs** – You activate tags
  on the AWS Billing and Cost Management dashboard. AWS uses tags to
  categorize your costs and deliver a monthly cost allocation report to you.
  For more information, see [Cost
  Allocation and Tagging](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.
- **Control access to your resources** –
  You can use tags in AWS Identity and Access Management (IAM) policies
  that control access to Amazon Q Business resources. To activate
  tag-based access control, you can attach these policies to an IAM role or IAM user. For more information, see [Authorization based on tags](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").
  You can create and manage tags using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon Q Business API.

###### Topics

- [Using tags](#tagging-resources-ds "#tagging-resources-ds")
- [Tag restrictions](#tag-restrictions-ds "#tag-restrictions-ds")

## Using tags

If you're using the console, you can tag resources when you create them or add
them later. You can also use the console to update or remove tags in the
following ways:

Adding tags
**To add Amazon Q Business
tags**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. From **Applications**, select the
   application whose resources you want to tag.
3. From the application summary page, scroll down and select
   **Tags**.
4. In **Tags**, from the resource you want
   to add tags to, select **Manage
   tags**.
5. In **Tags –
   _optional_**, select
   **Add new tag** to add tags to your
   Amazon Q Business resource. Then, enter the
   following information for each tag:
   - **Key** – Add a key for
     your tag.
   - **Value -
     _optional_** –
     An optional value for your tag.

6. Select **Save**.

Removing tags
**To remove tags**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. From **Applications**, select the
   application you want to delete tags from.
3. From the application summary page, scroll down and select
   **Tags**.
4. In **Tags**, from the resource you want
   to add tags to, select **Manage
   tags**.
5. In **Tags –
   _optional_**, select
   **Remove**.
6. Select **Save**.

Listing tags
**To view a list of tags**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.
2. From **Applications**, select the
   application you want to delete tags from.
3. From the application summary page, scroll down and select
   **Tags**.
4. In **Tags**, each tagged resource will
   display a list of tags associated with it.

If you're using the AWS CLI or the Amazon Q Business API, use
the following operations to manage tags for your resources:

- [CreateApplication](../api-reference/API_CreateApplication.md "../api-reference/API_CreateApplication.md") – Apply tags when you create an
  Amazon Q Business application.
- [CreateWebExperience](../api-reference/API_CreateWebExperience.md "../api-reference/API_CreateWebExperience.md") – Apply tags when you create an
  Amazon Q Business web experience.
- [ListTagsForResource](../api-reference/API_ListTagsForResource.md "../api-reference/API_ListTagsForResource.md") – View the tags associated with
  a resource.
- [TagResource](../api-reference/API_TagResource.md "../api-reference/API_TagResource.md") – Add and modify tags for a
  resource.
- [UntagResource](../api-reference/API_UntagResource.md "../api-reference/API_UntagResource.md") – Remove tags from a resource.

## Tag restrictions

The following restrictions apply to tags on Amazon Q Business
resources:

- Maximum number of tags – 50
- Maximum key length – 128 characters
- Maximum value length – 256 characters
- Valid characters for key and value – a–z, A–Z,
  space, and the following characters: \_ . : / = + - and @
- Keys and values are case sensitive
- Don't use `aws:` as a prefix for keys; it's reserved for
  AWS use
