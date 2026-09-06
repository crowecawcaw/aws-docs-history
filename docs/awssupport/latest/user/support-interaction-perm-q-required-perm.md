

# Required permissions for Amazon Q integration
<a name="support-interaction-perm-q-required-perm"></a>

To use the Amazon Q conversation import feature in Support Center, IAM identities need permissions for the following Amazon Q Developer actions:
+ `q:StartConversation`: Start a new conversation with Amazon Q.
+ `q:SendMessage`: Send messages within a conversation.
+ `q:GetConversation`: Retrieve conversation details. This action is required for console access.
+ `q:ListConversations`: List available conversations. This action is required for console access and Support Center integration.

Amazon Q integration with Support Center Console specifically requires the `q:ListConversations` permission to display your recent conversations for import. For detailed guidance on configuring Amazon Q Developer permissions, see [Amazon Q Developer permissions reference](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html) and [Manage access to Amazon Q Developer with policies](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html).