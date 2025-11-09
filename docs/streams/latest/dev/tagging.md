# Tag your Amazon Kinesis Data Streams resources

You can assign your own metadata to streams and enhanced fan-out consumers you create in Amazon Kinesis Data Streams in the form of _tags_. A tag is a key-value pair that you define for a stream. Using tags is a simple yet powerful way to manage AWS resources and organize data, including billing data.

###### Contents

- [Review tag basics](#tagging-basics "#tagging-basics")
- [Track costs using tagging](#tagging-billing "#tagging-billing")
- [Understand tag restrictions](#tagging-restrictions "#tagging-restrictions")
- [Tag streams using the Kinesis Data Streams console](#tagging-console "#tagging-console")
- [Tag streams using the AWS CLI](#tagging-cli "#tagging-cli")
- [Tag streams using the Kinesis Data Streams APIs](#tagging-api "#tagging-api")
- [Tag consumers using the AWS CLI](#tagging-consumers-cli "#tagging-consumers-cli")
- [Tag consumers using the Kinesis Data Streams APIs](#tagging-consumers-api "#tagging-consumers-api")

## Review tag basics

The Kinesis Data Streams resources you can tag include data streams and enhanced fan-out consumers. You use the Kinesis Data Streams console, AWS CLI, or Kinesis Data Streams API to complete the following tasks:

- Create a resource with tags
- Add tags to a resource
- List the tags for your resources
- Remove tags from a resource

###### Note

You can't apply tags to enhanced fan-out consumers using the Kinesis Data Streams console. For applying tags to consumers, use AWS CLI or Kinesis Data Streams API.

You can use tags to categorize your resources. For example, you can categorize resources by purpose, owner, or environment. Because you define the key and value for each tag, you can create a custom set of categories to meet your specific needs. For example, you might define a set of tags that helps you track resources by owner and associated application. Here are several examples of tags:

- Project: Project name
- Owner: Name
- Purpose: Load testing
- Application: Application name
- Environment: Production

###### Important

- To add tags while creating a stream, you must include the `kinesis:CreateStream` and `kinesis:AddTagsToStream` permissions for that stream. You **can't use** the `kinesis:TagResource` permission to tag streams while creating them.
- To add tags during consumer registration, you must include the `kinesis:TagResource` and `kinesis:RegisterStreamConsumer` permissions.

## Track costs using tagging

You can use tags to categorize and track your AWS costs. When you apply tags to your Kinesis Data Streams resources, your AWS cost allocation report includes usage and costs aggregated by tags. You can apply tags that represent business categories, such as cost centers, application names, or owners, to organize your costs across multiple services. For more information, see [Use Cost Allocation Tags for Custom Billing Reports](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.

## Understand tag restrictions

The following restrictions apply to tags:

###### Basic restrictions

- The maximum number of tags for each resource is 50.
- Tag keys and values are case-sensitive.
- You can't change or edit tags for a deleted resource.

###### Tag key restrictions

- Each tag key must be unique. If you add a tag with a key that's already in use, your new tag overwrites the existing key-value pair.
- You can't start a tag key with `aws:` because this prefix is reserved for use by AWS. AWS creates tags that begin with this prefix on your behalf, but you can't edit or delete them.
- Tag keys must be between 1 and 128 Unicode characters in length.
- Tag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: `_ . / = + - @`.

###### Tag value restrictions

- Tag values must be between 0 and 255 Unicode characters in length.
- Tag values can be blank. Otherwise, they must consist of the following characters: Unicode letters, digits, white space, and any of the following special characters: `_ . / = + - @`.

## Tag streams using the Kinesis Data Streams console

You can add, update, list, and remove tags on your streams using the Kinesis Data Streams console.

###### To view the tags for a stream

1. Sign in to the AWS Management Console and open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. On the left navigation pane, choose **Data streams**.
3. On the **Data streams** page, choose the stream that you want to tag.
4. On the Stream details page, choose **Configuration**.
5. In the **Tags** section, view the tags applied to the stream.

###### To create a data stream with a tag

1. Open the Kinesis Data Streams console.
2. On the left navigation pane, choose **Data streams**.
3. Choose **Create data stream**.
4. On the **Create data stream** page, enter a name for your data stream.
5. For **Data stream capacity**, choose either the **On-demand** or the **Provisioned** capacity mode.

For more information about capacity modes, see [Choose the right mode to stream in](how-do-i-size-a-stream.md "how-do-i-size-a-stream.md"). 6. In the **Tags** section, do the following:

    1. Choose **Add new tag**.
    2. For **Key**, enter the tag and optionally specify a value in the **Value** field.


    If you see an error, either the tag key or value that you specified doesn't meet the tag restrictions. For more information, see [Understand tag restrictions](#tagging-restrictions "#tagging-restrictions").

7. Choose **Create data stream**.

###### To add or update a tag on a stream

1.  Open the Kinesis Data Streams console.
2.  On the left navigation pane, choose **Data streams**.
3.  On the **Data streams** page, choose the stream to which you want to add or update tags.
4.  On the Stream details page, choose **Configuration**.
5.  In the **Tags** section, choose **Manage tags**.
6.  Under **Tags**, do one of the following:

        * To add a new tag, choose **Add new tag**, and then enter the tag's **Key** and **Value** data. Repeat this step as many times as necessary.


        The maximum number of tags you can add for each stream is 50.
        * To update an existing tag, enter a new tag value in the **Value** field of that tag's **Key**.

    If you see an error, either the tag key or value that you specified doesn't meet the tag restrictions. For more information, see [Understand tag restrictions](#tagging-restrictions "#tagging-restrictions").

7.  Choose **Save changes**.

###### To remove a tag from a stream

1. Open the Kinesis Data Streams console.
2. On the left navigation pane, choose **Data streams**.
3. On the **Data streams** page, choose the stream from which you want to remove tags.
4. On the Stream details page, choose **Configuration**.
5. In the **Tags** section, choose **Manage tags**.
6. Find the tag **Key** and **Value** pair that you want to remove. Then, choose **Remove**.
7. Choose **Save changes**.

## Tag streams using the AWS CLI

You can add, list, and remove tags on your streams using the AWS CLI. For examples, see the following documentation.

[create-stream](../../../cli/latest/reference/kinesis/create-stream.md "../../../cli/latest/reference/kinesis/create-stream.md")

Creates a stream with tags.

[add-tags-to-stream](../../../cli/latest/reference/kinesis/add-tags-to-stream.md "../../../cli/latest/reference/kinesis/add-tags-to-stream.md")

Adds or updates tags for the specified stream.

[list-tags-for-stream](../../../cli/latest/reference/kinesis/list-tags-for-stream.md "../../../cli/latest/reference/kinesis/list-tags-for-stream.md")

Lists the tags for the specified stream.

[remove-tags-from-stream](../../../cli/latest/reference/kinesis/remove-tags-from-stream.md "../../../cli/latest/reference/kinesis/remove-tags-from-stream.md")

Removes tags from the specified stream.

## Tag streams using the Kinesis Data Streams APIs

You can add, list, and remove tags on your streams using the Kinesis Data Streams APIs. For examples, see the following documentation:

[CreateStream](../../../kinesis/latest/APIReference/API_CreateStream.md "../../../kinesis/latest/APIReference/API_CreateStream.md")

Creates a stream with tags.

[AddTagsToStream](../../../kinesis/latest/APIReference/API_AddTagsToStream.md "../../../kinesis/latest/APIReference/API_AddTagsToStream.md")

Adds or updates tags for the specified stream.

[ListTagsForStream](../../../kinesis/latest/APIReference/API_ListTagsForStream.md "../../../kinesis/latest/APIReference/API_ListTagsForStream.md")

Lists the tags for the specified stream.

[RemoveTagsFromStream](../../../kinesis/latest/APIReference/API_RemoveTagsFromStream.md "../../../kinesis/latest/APIReference/API_RemoveTagsFromStream.md")

Removes tags from the specified stream.

## Tag consumers using the AWS CLI

You can add, list, and remove tags on your consumers using the AWS CLI. For examples, see the following documentation:

[register-stream-consumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/register-stream-consumer.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/register-stream-consumer.html")

Registers a consumer for a Kinesis data stream with tags.

[tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/tag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/tag-resource.html")

Adds or updates tags for the specified Kinesis resource.

[list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-tags-for-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-tags-for-resource.html")

Lists the tags for the specified Kinesis resource.

[untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/untag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/untag-resource.html")

Removes tags from the specified Kinesis resource.

## Tag consumers using the Kinesis Data Streams APIs

You can add, list, and remove tags on your consumers using the Kinesis Data Streams APIs. For examples, see the following documentation:

[RegisterStreamConsumer](../../../kinesis/latest/APIReference/API_RegisterStreamConsumer.md "../../../kinesis/latest/APIReference/API_RegisterStreamConsumer.md")

Registers a consumer for a Kinesis data stream with tags.

[TagResource](../../../kinesis/latest/APIReference/API_TagResource.md "../../../kinesis/latest/APIReference/API_TagResource.md")

Adds or updates tags for the specified Kinesis resource.

[ListTagsForResource](../../../kinesis/latest/APIReference/API_ListTagsForResource.md "../../../kinesis/latest/APIReference/API_ListTagsForResource.md")

Lists the tags for the specified Kinesis resource.

[UntagResource](../../../kinesis/latest/APIReference/API_UntagResource.md "../../../kinesis/latest/APIReference/API_UntagResource.md")

Removes tags from the specified Kinesis resource.
