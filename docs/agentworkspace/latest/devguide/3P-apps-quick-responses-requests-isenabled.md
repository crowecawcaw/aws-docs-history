# Determine if the Quick Responses feature is enabled in Amazon Connect Agent Workspace

Returns the QuickResponsesEnabledState object, which indicates if the quick
responses feature is enabled for the Connect instance. Quick responses is considered
enabled if there is a knowledge base for quick responses configured for the
instance. The object contains the following fields:

- `isEnabled`: A boolean indicating if the feature is enabled
- `knowledgeBaseId`: The id of the Quick Responses Knowledge Base (if
  the feature is enabled)

**Signature**

```
isEnabled(): Promise<QuickResponsesEnabledState>
```
