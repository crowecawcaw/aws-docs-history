# Tagging AgentCore resources

A _tag_ is a label that you assign to an AWS resource. Each tag consists of a _key_ and an optional _value_, both of which you define.

Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags you've assigned to it.

## Tagging overview

Each tag consists of a key and an optional value. For example, you could define a set of tags for your account's AgentCore resources that helps you track each resource's owner and stack level.

We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add.

Tags don't have any semantic meaning to AgentCore and are interpreted strictly as a string of characters. Also, tags are not automatically assigned to your resources. You can edit tag keys and values, and you can remove tags from a resource at any time. You can set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value. If you delete a resource, any tags for the resource are also deleted.

## Resources that support tagging

The following AgentCore resources support tagging:

- Agent runtime
- Agent runtime endpoint
- Code interpreter
- Browser
- Gateway
- Workload identity
- OAuth2 credential provider
- API key credential provider
- Workload identity directory
- Token vault
- AgentCore Memory

## Tag restrictions

The following basic restrictions apply to tags:

- Maximum number of tags per resource – 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length – 128 Unicode characters in UTF-8
- Maximum value length – 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . \_ : / @.
- Tag keys and values are case-sensitive.
- Don't use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You can't edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

## Working with tags

You can add, edit, or delete tags for AgentCore resources using the console, API, or CLI.

### Adding tags

Console
You can add tags when you create the following AgentCore resources:

- Agent runtime
- Agent runtime endpoint
- Code interpreter
- Browser
- Gateway
- Workload identity
- OAuth2 credential provider
- API key credential provider

###### To add tags when creating a resource

1. Open the AgentCore console.
2. Navigate to the resource type you want to create.
3. Follow the steps to create the resource. When you reach the **Tags** section, choose **Add tag**.
4. Enter a tag key and optionally a tag value.
5. To add more tags, choose **Add tag** again.
6. Complete the resource creation process.

###### To add tags to an existing resource

1. Open the AgentCore console.
2. Navigate to the resource type and select the specific resource.
3. Choose the **Tags** tab.
4. Choose **Add tag**, then enter a key and optionally a value.
5. Choose **Save changes**.

API
You can add tags when you create resources or to existing resources using the AgentCore API.

###### Adding tags when creating resources

You can add tags when you create resources using the following API operations:

- [CreateAgentRuntime](../../../bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntime.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntime.md") – Include tags in the `tags` parameter.
- [CreateAgentRuntimeEndpoint](../../../bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntimeEndpoint.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntimeEndpoint.md") – Include tags in the `tags` parameter.
- [CreateCodeInterpreter](../../../bedrock-agentcore-control/latest/APIReference/API_CreateCodeInterpreter.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateCodeInterpreter.md") – Include tags in the `tags` parameter.
- [CreateBrowser](../../../bedrock-agentcore-control/latest/APIReference/API_CreateBrowser.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateBrowser.md") – Include tags in the `tags` parameter.
- [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") – Include tags in the `tags` parameter.
- [CreateWorkloadIdentity](../../../bedrock-agentcore-control/latest/APIReference/API_CreateWorkloadIdentity.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateWorkloadIdentity.md") – Include tags in the `tags` parameter.
- [CreateOAuth2CredentialProvider](../../../bedrock-agentcore-control/latest/APIReference/API_CreateOAuth2CredentialProvider.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateOAuth2CredentialProvider.md") – Include tags in the `tags` parameter.
- [CreateAPIKeyCredentialProvider](../../../bedrock-agentcore-control/latest/APIReference/API_CreateAPIKeyCredentialProvider.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateAPIKeyCredentialProvider.md") – Include tags in the `tags` parameter.

###### Adding tags to existing resources

Use the [TagResource](../../../bedrock-agentcore-control/latest/APIReference/API_TagResource.md "../../../bedrock-agentcore-control/latest/APIReference/API_TagResource.md") operation to add tags to existing resources.

CLI
You can use the CLI to add tags to AgentCore resources.

###### To add tags to a resource

Use the `tag-resource` command:

```
aws bedrock-agentcore tag-resource \
    --resource-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:agent-runtime/example-runtime \
    --tags Key=Environment,Value=Production Key=Team,Value=AI
```

### Managing tags

Console
You can edit tag values for existing resources in the console.

###### To edit tags for an existing resource

1. Open the AgentCore console.
2. Navigate to the resource type and select the specific resource.
3. Choose the **Tags** tab.
4. To edit a tag, modify the key or value directly.
5. Choose **Save changes**.

API
You can use the AgentCore API to list and manage tags for resources.

###### Listing tags

Use the [ListTagsForResource](../../../bedrock-agentcore-control/latest/APIReference/API_ListTagsForResource.md "../../../bedrock-agentcore-control/latest/APIReference/API_ListTagsForResource.md") operation to list the tags for a resource.

###### Updating tags

Use the [TagResource](../../../bedrock-agentcore-control/latest/APIReference/API_TagResource.md "../../../bedrock-agentcore-control/latest/APIReference/API_TagResource.md") operation to update existing tags by adding new values for existing keys.

CLI
You can use the CLI to list and manage tags for AgentCore resources.

###### To list tags for a resource

Use the `list-tags-for-resource` command:

```
aws bedrock-agentcore list-tags-for-resource \
    --resource-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:agent-runtime/example-runtime
```

###### To update tags for a resource

Use the `tag-resource` command to update existing tags:

```
aws bedrock-agentcore tag-resource \
    --resource-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:agent-runtime/example-runtime \
    --tags Key=Environment,Value=Staging
```

### Deleting tags

Console
You can remove tags from resources in the console.

###### To delete tags from a resource

1. Open the AgentCore console.
2. Navigate to the resource type and select the specific resource.
3. Choose the **Tags** tab.
4. To delete a tag, choose **Remove** next to the tag.
5. Choose **Save changes**.

API
You can use the AgentCore API to remove tags from resources.

###### Removing tags

Use the [UntagResource](../../../bedrock-agentcore-control/latest/APIReference/API_UntagResource.md "../../../bedrock-agentcore-control/latest/APIReference/API_UntagResource.md") operation to remove tags from a resource.

CLI
You can use the CLI to remove tags from AgentCore resources.

###### To remove tags from a resource

Use the `untag-resource` command:

```
aws bedrock-agentcore untag-resource \
    --resource-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:agent-runtime/example-runtime \
    --tag-keys Environment Team
```
