

# Tag your Amazon Kinesis Data Streams resources
<a name="tagging"></a>

You can assign your own metadata to streams and enhanced fan-out consumers you create in Amazon Kinesis Data Streams in the form of *tags*. A tag is a key-value pair that you define for a stream. Using tags is a simple yet powerful way to manage AWS resources and organize data, including billing data.

**Topics**
+ [Review tag basics](#tagging-basics)
+ [Track costs using tagging](#tagging-billing)
+ [Understand tag restrictions](#tagging-restrictions)
+ [Tag streams using the Kinesis Data Streams console](#tagging-console)
+ [Tag streams using the AWS CLI](#tagging-cli)
+ [Tag streams using the Kinesis Data Streams APIs](#tagging-api)
+ [Tag consumers using the AWS CLI](#tagging-consumers-cli)
+ [Tag consumers using the Kinesis Data Streams APIs](#tagging-consumers-api)

## Review tag basics
<a name="tagging-basics"></a>

The Kinesis Data Streams resources you can tag include data streams and enhanced fan-out consumers. You use the Kinesis Data Streams console, AWS CLI, or Kinesis Data Streams API to complete the following tasks:
+ Create a resource with tags
+ Add tags to a resource
+ List the tags for your resources
+ Remove tags from a resource

**Note**  
You can't apply tags to enhanced fan-out consumers using the Kinesis Data Streams console. For applying tags to consumers, use AWS CLI or Kinesis Data Streams API. 

You can use tags to categorize your resources. For example, you can categorize resources by purpose, owner, or environment. Because you define the key and value for each tag, you can create a custom set of categories to meet your specific needs. For example, you might define a set of tags that helps you track resources by owner and associated application. Here are several examples of tags:
+ Project: Project name
+ Owner: Name
+ Purpose: Load testing 
+ Application: Application name
+ Environment: Production 

**Important**  
To add tags while creating a stream, you must include the `kinesis:CreateStream` and `kinesis:AddTagsToStream` permissions for that stream. You **can't use** the `kinesis:TagResource` permission to tag streams while creating them.
To add tags during consumer registration, you must include the `kinesis:TagResource` and `kinesis:RegisterStreamConsumer` permissions.

## Track costs using tagging
<a name="tagging-billing"></a>

You can use tags to categorize and track your AWS costs. When you apply tags to your Kinesis Data Streams resources, your AWS cost allocation report includes usage and costs aggregated by tags. You can apply tags that represent business categories, such as cost centers, application names, or owners, to organize your costs across multiple services. For more information, see [Use Cost Allocation Tags for Custom Billing Reports](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.

## Understand tag restrictions
<a name="tagging-restrictions"></a>

The following restrictions apply to tags:

**Basic restrictions**
+ The maximum number of tags for each resource is 50.
+ Tag keys and values are case-sensitive.
+ You can't change or edit tags for a deleted resource.

**Tag key restrictions**
+ Each tag key must be unique. If you add a tag with a key that's already in use, your new tag overwrites the existing key-value pair. 
+ You can't start a tag key with `aws:` because this prefix is reserved for use by AWS. AWS creates tags that begin with this prefix on your behalf, but you can't edit or delete them.
+ Tag keys must be between 1 and 128 Unicode characters in length.
+ Tag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: `_ . / = + - @`.

**Tag value restrictions**
+ Tag values must be between 0 and 255 Unicode characters in length.
+ Tag values can be blank. Otherwise, they must consist of the following characters: Unicode letters, digits, white space, and any of the following special characters: `_ . / = + - @`.

## Tag streams using the Kinesis Data Streams console
<a name="tagging-console"></a>

You can add, update, list, and remove tags on your streams using the Kinesis Data Streams console.

**To view the tags for a stream**

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. On the left navigation pane, choose **Data streams**.

1. On the **Data streams** page, choose the stream that you want to tag.

1. On the Stream details page, choose **Configuration**.

1. In the **Tags** section, view the tags applied to the stream.

**To create a data stream with a tag**

1. Open the Kinesis Data Streams console.

1. On the left navigation pane, choose **Data streams**.

1. Choose **Create data stream**.

1. On the **Create data stream** page, enter a name for your data stream.

1. For **Data stream capacity**, choose either the **On-demand** or the **Provisioned** capacity mode.

   For more information about capacity modes, see [Choose the right mode to stream in](how-do-i-size-a-stream.md).

1. In the **Tags** section, do the following:

   1. Choose **Add new tag**.

   1. For **Key**, enter the tag and optionally specify a value in the **Value** field.

      If you see an error, either the tag key or value that you specified doesn't meet the tag restrictions. For more information, see [Understand tag restrictions](#tagging-restrictions).

1. Choose **Create data stream**.

**To add or update a tag on a stream**

1. Open the Kinesis Data Streams console.

1. On the left navigation pane, choose **Data streams**.

1. On the **Data streams** page, choose the stream to which you want to add or update tags.

1. On the Stream details page, choose **Configuration**.

1. In the **Tags** section, choose **Manage tags**.

1. Under **Tags**, do one of the following:
   + To add a new tag, choose **Add new tag**, and then enter the tag's **Key** and **Value** data. Repeat this step as many times as necessary.

     The maximum number of tags you can add for each stream is 50.
   + To update an existing tag, enter a new tag value in the **Value** field of that tag's **Key**.

   If you see an error, either the tag key or value that you specified doesn't meet the tag restrictions. For more information, see [Understand tag restrictions](#tagging-restrictions).

1. Choose **Save changes**.

**To remove a tag from a stream**

1. Open the Kinesis Data Streams console.

1. On the left navigation pane, choose **Data streams**.

1. On the **Data streams** page, choose the stream from which you want to remove tags.

1. On the Stream details page, choose **Configuration**.

1. In the **Tags** section, choose **Manage tags**.

1. Find the tag **Key** and **Value** pair that you want to remove. Then, choose **Remove**.

1. Choose **Save changes**.

## Tag streams using the AWS CLI
<a name="tagging-cli"></a>

You can add, list, and remove tags on your streams using the AWS CLI. For examples, see the following documentation.

 [create-stream](https://docs.aws.amazon.com/cli/latest/reference/kinesis/create-stream.html)   
Creates a stream with tags.

 [add-tags-to-stream](https://docs.aws.amazon.com/cli/latest/reference/kinesis/add-tags-to-stream.html)   
Adds or updates tags for the specified stream.

 [list-tags-for-stream](https://docs.aws.amazon.com/cli/latest/reference/kinesis/list-tags-for-stream.html)  
Lists the tags for the specified stream.

 [remove-tags-from-stream](https://docs.aws.amazon.com/cli/latest/reference/kinesis/remove-tags-from-stream.html)  
Removes tags from the specified stream.

## Tag streams using the Kinesis Data Streams APIs
<a name="tagging-api"></a>

You can add, list, and remove tags on your streams using the Kinesis Data Streams APIs. For examples, see the following documentation:

 [CreateStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html)   
Creates a stream with tags.

 [AddTagsToStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_AddTagsToStream.html)   
Adds or updates tags for the specified stream.

 [ListTagsForStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForStream.html)  
Lists the tags for the specified stream.

 [RemoveTagsFromStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RemoveTagsFromStream.html)  
Removes tags from the specified stream.

## Tag consumers using the AWS CLI
<a name="tagging-consumers-cli"></a>

You can add, list, and remove tags on your consumers using the AWS CLI. For examples, see the following documentation:

[register-stream-consumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/register-stream-consumer.html)  
Registers a consumer for a Kinesis data stream with tags. 

[tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/tag-resource.html)  
Adds or updates tags for the specified Kinesis resource.

[list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-tags-for-resource.html)  
Lists the tags for the specified Kinesis resource.

[untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/untag-resource.html)  
Removes tags from the specified Kinesis resource.

## Tag consumers using the Kinesis Data Streams APIs
<a name="tagging-consumers-api"></a>

You can add, list, and remove tags on your consumers using the Kinesis Data Streams APIs. For examples, see the following documentation:

[RegisterStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RegisterStreamConsumer.html)  
Registers a consumer for a Kinesis data stream with tags.

[TagResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_TagResource.html)  
Adds or updates tags for the specified Kinesis resource.

[ListTagsForResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListTagsForResource.html)  
Lists the tags for the specified Kinesis resource.

[UntagResource](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UntagResource.html)  
Removes tags from the specified Kinesis resource.