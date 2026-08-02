# Denying AI-enhanced troubleshooting operations

You can explicitly deny AI-enhanced troubleshooting operations by removing the following operations from your custom managed policy. Denying these operations prevents users from accessing the AI-powered interaction workflow and Amazon Q conversations in Support Center.

**Support interaction operations**

The following operations enable the interaction-based workflow in Support Center:

- `support:GetInteraction`
- `support:ListInteractions`
- `support:ResolveInteraction`
- `support:StartInteraction`
- `support:UpdateInteraction`
  **Amazon Q Developer conversation operations**

The following operations enable Amazon Q conversations in Support Center:

- `q:StartConversation` – Start a new conversation with Amazon Q.
- `q:SendMessage` – Send messages within a conversation.
- `q:GetConversation` – Retrieve conversation details. This action is required for console access.
- `q:ListConversations` – List available conversations. This action is required for console access and Support Center integration.
  The following example policy explicitly denies all AI-enhanced troubleshooting operations:

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "support:GetInteraction",
        "support:ListInteractions",
        "support:ResolveInteraction",
        "support:StartInteraction",
        "support:UpdateInteraction",
        "q:StartConversation",
        "q:SendMessage",
        "q:GetConversation",
        "q:ListConversations"
      ],
      "Resource": "*"
    }
  ]
}

```

###### Note

Denying these operations doesn't affect access to traditional support case management. You can continue creating and managing support cases using the standard workflow.
