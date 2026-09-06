# API Reference

All operations follow the Command pattern. Import the client and the command, then
call client.send(command).

```
import { AgenticCXDesignerClient, <CommandName> } from "amazon-connect-acxd-sdk";

const client = new AgenticCXDesignerClient({
  apiKey: 'acxd_live_...',
  workspaceId: 'your-workspace-uuid',
});

const response = await client.send(new <CommandName>({ ... }));
```

Most List operations use token-based pagination:

```
const response = await client.send(new ListApplicationsCommand({
    maxResults: 50,
    nextToken: '...',
}));
```

**API Operations**

The following section lists the API operations by resource.

**API Token Operations**

- `ListApiTokens`
- `CreateApiToken`
- `DeleteApiToken`
  **Application Operations**

- `ListApplications`
- `CreateApplication`
- `GetApplication`
- `UpdateApplication`
- `DeleteApplication`
  **Application Build Operations**

- `ListApplicationBuilds`
- `CreateApplicationBuild`
- `GetApplicationBuild`
- `GetApplicationBuildDiff`
  **Application Deployment Operations**

- `ListApplicationDeployments`
- `CreateApplicationDeployment`
- `GetApplicationDeployment`
- `UpdateApplicationDeployment`
- `DeleteApplicationDeployment`
  **Analytics Tag Operations**

- `ListAnalyticsTags`
- `CreateAnalyticsTag`
- `UpdateAnalyticsTag`
- `DeleteAnalyticsTag`
  **Context Variables Operations**

- `ListContextVariables`
- `CreateContextVariable`
- `UpdateContextVariable`
- `DeleteContextVariable`
  **Conversation Operations**

- `ListConversations`
- `GetConversation`
  **Data Request Operations**

- `ListDataRequests`
- `CreateDataRequest`
- `GetDataRequest`
- `UpdateDataRequest`
- `DeleteDataRequest`
  **Downloads Operations**

- `GetDownload`
  **Flow Operations**

- `ListFlows`
- `CreateFlow`
- `GetFlow`
- `UpdateFlow`
- `DeleteFlow`
  **Guardrail Operations**

- `ListGuardrails`
- `CreateGuardrail`
- `GetGuardrail`
- `UpdateGuardrail`
- `DeleteGuardrail`
- `TestGuardrail`
- `ListGuardrailEvents`
  **Knowledge Base Operations**

- `ListKnowledgeBases`
- `CreateKnowledgeBase`
- `GetKnowledgeBase`
- `UpdateKnowledgeBase`
- `DeleteKnowledgeBase`
- `CloneKnowledgeBase`
- `PublishKnowledgeBase`
- `GetKnowledgeBasePublication`
- `ListKnowledgeBasePublications`
  **Knowledge Base Article Operations**

- `ListKnowledgeBaseArticles`
- `CreateKnowledgeBaseArticle`
- `GetKnowledgeBaseArticle`
- `UpdateKnowledgeBaseArticle`
- `DeleteKnowledgeBaseArticle`
  **Knowledge Base Document Operations**

- `ListKnowledgeBaseDocuments`
- `GetKnowledgeBaseDocument`
- `PutKnowledgeBaseDocument`
- `DeleteKnowledgeBaseDocument`
  **Live Sync Script Operations**

- `ListLiveSyncScripts`
- `CreateLiveSyncScript`
- `GetLiveSyncScript`
- `UpdateLiveSyncScript`
- `DeleteLiveSyncScript`
- `ListLiveSyncScriptBuilds`
- `CreateLiveSyncScriptBuild`
- `GetLiveSyncScriptBuild`
- `ListLiveSyncScriptDeployments`
- `CreateLiveSyncScriptDeployment`
- `GetLiveSyncScriptDeployment`
- `UpdateLiveSyncScriptDeployment`
- `DeleteLiveSyncScriptDeployment`
  **Log Operations**

- `QueryLogs`
  **Modality Operations**

- `ListModalities`
- `CreateModality`
- `GetModality`
- `UpdateModality`
- `DeleteModality`
  **Programmatic User Operations**

- `ListProgrammaticUsers`
- `CreateProgrammaticUser`
- `GetProgrammaticUser`
- `UpdateProgrammaticUser`
- `DeleteProgrammaticUser`
  **Role Operations**

- `ListRoles`
- `CreateRole`
- `GetRole`
- `UpdateRole`
- `DeleteRole`
- `GetRolePermissions`
  **Secret Operations**

- `ListSecrets`
- `CreateSecret`
- `GetSecret`
- `UpdateSecret`
- `DeleteSecret`
  **Slot Type Operations**

- `ListSlotTypes`
- `CreateSlotType`
- `GetSlotType`
- `UpdateSlotType`
- `DeleteSlotType`
  **Team Operations**

- `GetTeam`
  **Trail Operations**

- `StartTrailQuery`
- `GetTrailQueryResults`
  **User Operations**

- `ListUsers`
- `CreateUser`
- `GetUser`
- `UpdateUser`
- `DeleteUser`
  **Version Operations**

- `ListResourceVersions`
- `GetResourceVersion`
  **Workspace Operations**

- `ListWorkspaces`
- `CreateWorkspace`
- `GetWorkspace`
- `UpdateWorkspace`
- `DeleteWorkspace`

###### Contents

- [Analytics Tags](acxd-analytics-tags.md "acxd-analytics-tags.md")
- [API Tokens](acxd-api-tokens.md "acxd-api-tokens.md")
- [Applications](acxd-applications.md "acxd-applications.md")
- [Application Builds](acxd-application-builds.md "acxd-application-builds.md")
- [Application Deployments](acxd-application-deployments.md "acxd-application-deployments.md")
- [Context Variables](acxd-context-variables.md "acxd-context-variables.md")
- [Conversations](acxd-conversations.md "acxd-conversations.md")
- [Data Requests](acxd-data-requests.md "acxd-data-requests.md")
- [Downloads](acxd-downloads.md "acxd-downloads.md")
- [Flows](acxd-flows.md "acxd-flows.md")
- [Guardrails](acxd-guardrails.md "acxd-guardrails.md")
- [Knowledge Bases](acxd-knowledge-bases.md "acxd-knowledge-bases.md")
- [Knowledge Base Articles](acxd-knowledge-base-articles.md "acxd-knowledge-base-articles.md")
- [KnowledgeBase Documents](acxd-knowledge-base-documents.md "acxd-knowledge-base-documents.md")
- [Live Sync Scripts](acxd-live-sync-scripts.md "acxd-live-sync-scripts.md")
- [Logs](acxd-logs.md "acxd-logs.md")
- [Modalities](acxd-modalities.md "acxd-modalities.md")
- [Programmatic Users](acxd-programmatic-users.md "acxd-programmatic-users.md")
- [Roles](acxd-roles.md "acxd-roles.md")
- [Secrets](acxd-secrets.md "acxd-secrets.md")
- [Slot Types](acxd-slot-types.md "acxd-slot-types.md")
- [Team](acxd-team.md "acxd-team.md")
- [Trails](acxd-trails.md "acxd-trails.md")
- [Users](acxd-users.md "acxd-users.md")
- [Versions](acxd-versions.md "acxd-versions.md")
- [Workspaces](acxd-workspaces.md "acxd-workspaces.md")
- [Common Types](acxd-common-types.md "acxd-common-types.md")
