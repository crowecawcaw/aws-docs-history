# Tagging Amazon Bedrock resources

To help you manage your Amazon Bedrock resources, you can assign metadata to each resource as
tags. A tag is a label that you assign to an AWS resource. Each tag consists of a key and
a value.

Tags enable you to categorize your AWS resources in different ways, for example, by
purpose, owner, or application. For best practices and restrictions on tagging, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

Tags help you to do the following:

- Identify and organize your AWS resources. Many AWS resources support tagging, so you can assign the same tag to resources in different services to indicate that the resources are the same.
- Allocate costs. You activate tags on the AWS Billing and Cost Management dashboard.
  AWS uses the tags to categorize your costs and deliver a
  monthly cost allocation report to you. For more information, see
  [Use cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing and Cost Management
  User Guide_.
- Control access to your resources. You can use tags with Amazon Bedrock
  to create policies to control access to Amazon Bedrock resources. These
  policies can be attached to an IAM role or user to enable
  tag-based access control.

###### Topics

- [Use the console](#tagging-console "#tagging-console")
- [Use the API](#tagging-api "#tagging-api")

## Use the console

You can add, modify, and remove tags at any time while creating or editing a supported resource.

## Use the API

To carry out tagging operations, you need the Amazon Resource Name (ARN) of the resource on which you want to carry out a tagging operation. There are two sets of tagging operations, depending on the resource for which you are adding or managing tags.

The following table summarizes the different use cases and the tagging operations to use for them:

| Use case                 | Resource created with [Amazon Bedrock](../APIReference/API_Operations_Amazon_Bedrock.md "../APIReference/API_Operations_Amazon_Bedrock.md") API operation                                                                                                                                                                                                                          | Resource created with [Amazon Bedrock Agents](../APIReference/API_Operations_Agents_for_Amazon_Bedrock.md "../APIReference/API_Operations_Agents_for_Amazon_Bedrock.md") API operation                                                                                                                                                                                                                   | Resource created with Amazon Bedrock Data Automation API                                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tag a resource           | • If the resource wasn't created yet, use the `tags` field when creating the resource.<br>• If the resource was already created, make a [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp"). | • If the resource wasn't created yet, use the `tags` field when creating the resource.<br>• If the resource was already created, make a [TagResource](../APIReference/API_agent_TagResource.md "../APIReference/API_agent_TagResource.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). | • If the resource wasn't created yet, use the `tags` field when creating the resource.<br>• If the resource was already created, make a TagResource request with an Amazon Bedrock Data Automation Build time Endpoint. |
| Untag a resource         | Make an [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp").                                                                                                                           | Make an [UntagResource](../APIReference/API_agent_UntagResource.md "../APIReference/API_agent_UntagResource.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt").                                                                                                                           | Make an UntagResource request with an Amazon Bedrock Data Automation Build time Endpoint.                                                                                                                               |
| List tags for a resource | Make a [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp").                                                                                                          | Make a [ListTagsForResource](../APIReference/API_agent_ListTagsForResource.md "../APIReference/API_agent_ListTagsForResource.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt").                                                                                                          | Make a ListTagsForResource request with an Amazon Bedrock Data Automation Build time Endpoint.                                                                                                                          |

###### Note

When viewing these operations in CloudTrail, you can identify the specific resource being
tagged by checking the request parameters in the event details.

Choose a tab to see code examples in an interface or language.

AWS CLI
Add two tags to an agent. Separate key/value pairs with a space.

```
aws bedrock-agent tag-resource \
    --resource-arn "arn:aws:bedrock:us-east-1:123456789012:agent/AGENT12345" \
    --tags key=department,value=billing key=facing,value=internal
```

Remove the tags from the agent. Separate keys with a space.

```
aws bedrock-agent untag-resource \
    --resource-arn "arn:aws:bedrock:us-east-1:123456789012:agent/AGENT12345" \
    --tag-keys key=department facing
```

List the tags for the agent.

```
aws bedrock-agent list-tags-for-resource \
    --resource-arn "arn:aws:bedrock:us-east-1:123456789012:agent/AGENT12345"
```

Python (Boto)
Add two tags to an agent.

```
import boto3

bedrock = boto3.client(service_name='bedrock-agent')

tags = [
    {
        'key': 'department',
        'value': 'billing'
    },
    {
        'key': 'facing',
        'value': 'internal'
    }
]

bedrock.tag_resource(resourceArn='arn:aws:bedrock:us-east-1:123456789012:agent/AGENT12345', tags=tags)
```

Remove the tags from the agent.

```
bedrock.untag_resource(
    resourceArn='arn:aws:bedrock:us-east-1:123456789012:agent/AGENT12345',
    tagKeys=['department', 'facing']
)
```

List the tags for the agent.

```
bedrock.list_tags_for_resource(resourceArn='arn:aws:bedrock:us-east-1:123456789012:agent/AGENT12345')
```
