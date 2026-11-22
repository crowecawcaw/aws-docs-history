

# Required permissions for AWS assistant integration

To use the AWS assistant conversation import feature in Support Center, IAM identities need permissions for the following AWS assistant actions:
+ `q:StartConversation`: Start a new conversation with the AWS assistant.
+ `q:SendMessage`: Send messages within a conversation.
+ `q:GetConversation`: Retrieve conversation details. This action is required for console access.
+ `q:ListConversations`: List available conversations. This action is required for console access and Support Center integration.

The AWS assistant integration with Support Center Console specifically requires the `q:ListConversations` permission to display your recent conversations for import. For detailed guidance on configuring AWS assistant permissions, see [Identity and access management](https://docs.aws.amazon.com/assistant/latest/userguide/security.html#security-iam) and [Identity-based policy examples for AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/security-iam-examples.html).