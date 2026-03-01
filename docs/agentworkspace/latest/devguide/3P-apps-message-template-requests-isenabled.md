# Determine if the Message Template feature is enabled in Amazon Connect Agent Workspace

Returns the MessageTemplateEnabledState object, which indicates if the message
template feature is enabled for the Connect instance. The Message Template feature
is considered enabled if there is a knowledge base for message templates configured
for the instance. The object contains the following fields:

- `isEnabled`: A boolean indicating if the feature is enabled
- `knowledgeBaseId`: The id of the Message Template Knowledge Base
  (if the feature is enabled)

**Signature**

```
isEnabled(): Promise<MessageTemplateEnabledState>
```
