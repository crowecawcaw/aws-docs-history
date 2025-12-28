# Required permissions for Amazon Q integration

To use the Amazon Q conversation import feature in Support Center, IAM identities need permissions for the following Amazon Q Developer actions:

- `q:StartConversation`: Start a new conversation with Amazon Q.
- `q:SendMessage`: Send messages within a conversation.
- `q:GetConversation`: Retrieve conversation details. This action is required for console access.
- `q:ListConversations`: List available conversations. This action is required for console access and Support Center integration.
  Amazon Q integration with Support Center Console specifically requires the `q:ListConversations` permission to display your recent conversations for import. For detailed guidance on configuring Amazon Q Developer permissions, see [Amazon Q Developer permissions reference](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md") and [Manage access to Amazon Q Developer with policies](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md").
