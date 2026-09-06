

# Actions, resources, and condition keys for Amazon Q in Connect
<a name="list_q-in-connect"></a>

Amazon Q in Connect (service prefix: `wisdom`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/connect/latest/adminguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/wisdom/wisdom.json) for this service.

**Topics**
+ [API operations defined by Amazon Q in Connect](#list_q-in-connect-operations)
+ [Actions defined by Amazon Q in Connect](#list_q-in-connect-actions-as-permissions)
+ [Permission-only actions for Amazon Q in Connect](#list_q-in-connect-permission-only-actions)
+ [Resource types defined by Amazon Q in Connect](#list_q-in-connect-resources-for-iam-policies)
+ [Condition keys for Amazon Q in Connect](#list_q-in-connect-policy-keys)

## API operations defined by Amazon Q in Connect
<a name="list_q-in-connect-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_q-in-connect-actions-as-permissions).




- **   ActivateMessageTemplate  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ActivateMessageTemplate](#list_q-in-connect-action-ActivateMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAIAgent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateAIAgent](#list_q-in-connect-action-CreateAIAgent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAIAgentVersion  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateAIAgentVersion](#list_q-in-connect-action-CreateAIAgentVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAIGuardrail  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateAIGuardrail](#list_q-in-connect-action-CreateAIGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAIGuardrailVersion  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateAIGuardrailVersion](#list_q-in-connect-action-CreateAIGuardrailVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAIPrompt  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateAIPrompt](#list_q-in-connect-action-CreateAIPrompt)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAIPromptVersion  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateAIPromptVersion](#list_q-in-connect-action-CreateAIPromptVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssistant  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateAssistant](#list_q-in-connect-action-CreateAssistant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAssistantAssociation  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateAssistantAssociation](#list_q-in-connect-action-CreateAssistantAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** wisdom.amazonaws.com / **Access level:** Write

- **   CreateContent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateContent](#list_q-in-connect-action-CreateContent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateContentAssociation  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateContentAssociation](#list_q-in-connect-action-CreateContentAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateKnowledgeBase  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateKnowledgeBase](#list_q-in-connect-action-CreateKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMessageTemplate  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateMessageTemplate](#list_q-in-connect-action-CreateMessageTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMessageTemplateAttachment  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateMessageTemplateAttachment](#list_q-in-connect-action-CreateMessageTemplateAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMessageTemplateVersion  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateMessageTemplateVersion](#list_q-in-connect-action-CreateMessageTemplateVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateQuickResponse  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateQuickResponse](#list_q-in-connect-action-CreateQuickResponse)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSession  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:CreateSession](#list_q-in-connect-action-CreateSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeactivateMessageTemplate  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeactivateMessageTemplate](#list_q-in-connect-action-DeactivateMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAIAgent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteAIAgent](#list_q-in-connect-action-DeleteAIAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAIAgentVersion  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteAIAgentVersion](#list_q-in-connect-action-DeleteAIAgentVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAIGuardrail  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteAIGuardrail](#list_q-in-connect-action-DeleteAIGuardrail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAIGuardrailVersion  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteAIGuardrailVersion](#list_q-in-connect-action-DeleteAIGuardrailVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAIPrompt  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteAIPrompt](#list_q-in-connect-action-DeleteAIPrompt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAIPromptVersion  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteAIPromptVersion](#list_q-in-connect-action-DeleteAIPromptVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssistant  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteAssistant](#list_q-in-connect-action-DeleteAssistant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssistantAssociation  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteAssistantAssociation](#list_q-in-connect-action-DeleteAssistantAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteContent](#list_q-in-connect-action-DeleteContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContentAssociation  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteContentAssociation](#list_q-in-connect-action-DeleteContentAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImportJob  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteImportJob](#list_q-in-connect-action-DeleteImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKnowledgeBase  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteKnowledgeBase](#list_q-in-connect-action-DeleteKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMessageTemplate  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteMessageTemplate](#list_q-in-connect-action-DeleteMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMessageTemplateAttachment  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteMessageTemplateAttachment](#list_q-in-connect-action-DeleteMessageTemplateAttachment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQuickResponse  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:DeleteQuickResponse](#list_q-in-connect-action-DeleteQuickResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAIAgent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetAIAgent](#list_q-in-connect-action-GetAIAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAIGuardrail  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetAIGuardrail](#list_q-in-connect-action-GetAIGuardrail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAIPrompt  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetAIPrompt](#list_q-in-connect-action-GetAIPrompt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssistant  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetAssistant](#list_q-in-connect-action-GetAssistant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssistantAssociation  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetAssistantAssociation](#list_q-in-connect-action-GetAssistantAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetContent](#list_q-in-connect-action-GetContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContentAssociation  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetContentAssociation](#list_q-in-connect-action-GetContentAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContentSummary  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetContentSummary](#list_q-in-connect-action-GetContentSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImportJob  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetImportJob](#list_q-in-connect-action-GetImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKnowledgeBase  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetKnowledgeBase](#list_q-in-connect-action-GetKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMessageTemplate  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetMessageTemplate](#list_q-in-connect-action-GetMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNextMessage  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetNextMessage](#list_q-in-connect-action-GetNextMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQuickResponse  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetQuickResponse](#list_q-in-connect-action-GetQuickResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendations  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetRecommendations](#list_q-in-connect-action-GetRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSession  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetSession](#list_q-in-connect-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAIAgentVersions  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListAIAgentVersions](#list_q-in-connect-action-ListAIAgentVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAIAgents  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListAIAgents](#list_q-in-connect-action-ListAIAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAIGuardrailVersions  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListAIGuardrailVersions](#list_q-in-connect-action-ListAIGuardrailVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAIGuardrails  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListAIGuardrails](#list_q-in-connect-action-ListAIGuardrails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAIPromptVersions  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListAIPromptVersions](#list_q-in-connect-action-ListAIPromptVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAIPrompts  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListAIPrompts](#list_q-in-connect-action-ListAIPrompts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssistantAssociations  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListAssistantAssociations](#list_q-in-connect-action-ListAssistantAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssistants  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListAssistants](#list_q-in-connect-action-ListAssistants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContentAssociations  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListContentAssociations](#list_q-in-connect-action-ListContentAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContents  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListContents](#list_q-in-connect-action-ListContents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImportJobs  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListImportJobs](#list_q-in-connect-action-ListImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKnowledgeBases  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListKnowledgeBases](#list_q-in-connect-action-ListKnowledgeBases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMessageTemplateVersions  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListMessageTemplateVersions](#list_q-in-connect-action-ListMessageTemplateVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMessageTemplates  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListMessageTemplates](#list_q-in-connect-action-ListMessageTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMessages  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListMessages](#list_q-in-connect-action-ListMessages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModels  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListModels](#list_q-in-connect-action-ListModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQuickResponses  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListQuickResponses](#list_q-in-connect-action-ListQuickResponses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpans  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListSpans](#list_q-in-connect-action-ListSpans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:ListTagsForResource](#list_q-in-connect-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   NotifyRecommendationsReceived  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:NotifyRecommendationsReceived](#list_q-in-connect-action-NotifyRecommendationsReceived) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFeedback  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:PutFeedback](#list_q-in-connect-action-PutFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   QueryAssistant  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:QueryAssistant](#list_q-in-connect-action-QueryAssistant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RemoveAssistantAIAgent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:RemoveAssistantAIAgent](#list_q-in-connect-action-RemoveAssistantAIAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveKnowledgeBaseTemplateUri  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:RemoveKnowledgeBaseTemplateUri](#list_q-in-connect-action-RemoveKnowledgeBaseTemplateUri) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RenderMessageTemplate  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetMessageTemplate](#list_q-in-connect-action-GetMessageTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [wisdom:RenderMessageTemplate](#list_q-in-connect-action-RenderMessageTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   Retrieve  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:Retrieve](#list_q-in-connect-action-Retrieve) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchContent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:SearchContent](#list_q-in-connect-action-SearchContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchMessageTemplates  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:SearchMessageTemplates](#list_q-in-connect-action-SearchMessageTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchQuickResponses  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:GetQuickResponse](#list_q-in-connect-action-GetQuickResponse)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [wisdom:SearchQuickResponses](#list_q-in-connect-action-SearchQuickResponses)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   SearchSessions  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:SearchSessions](#list_q-in-connect-action-SearchSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendMessage  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:SendMessage](#list_q-in-connect-action-SendMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartContentUpload  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:StartContentUpload](#list_q-in-connect-action-StartContentUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImportJob  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:StartImportJob](#list_q-in-connect-action-StartImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UntagResource](#list_q-in-connect-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAIAgent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateAIAgent](#list_q-in-connect-action-UpdateAIAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAIGuardrail  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateAIGuardrail](#list_q-in-connect-action-UpdateAIGuardrail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAIPrompt  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateAIPrompt](#list_q-in-connect-action-UpdateAIPrompt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssistantAIAgent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateAssistantAIAgent](#list_q-in-connect-action-UpdateAssistantAIAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContent  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateContent](#list_q-in-connect-action-UpdateContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKnowledgeBaseTemplateUri  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateKnowledgeBaseTemplateUri](#list_q-in-connect-action-UpdateKnowledgeBaseTemplateUri) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMessageTemplate  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateMessageTemplate](#list_q-in-connect-action-UpdateMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMessageTemplateMetadata  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateMessageTemplateMetadata](#list_q-in-connect-action-UpdateMessageTemplateMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQuickResponse  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateQuickResponse](#list_q-in-connect-action-UpdateQuickResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSession  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateSession](#list_q-in-connect-action-UpdateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSessionData  **
  - **SDK client:** qconnect
  - **IAM action:**  [wisdom:UpdateSessionData](#list_q-in-connect-action-UpdateSessionData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssistant  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:CreateAssistant](#list_q-in-connect-action-CreateAssistant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAssistantAssociation  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:CreateAssistantAssociation](#list_q-in-connect-action-CreateAssistantAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** wisdom.amazonaws.com / **Access level:** Write

- **   CreateContent  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:CreateContent](#list_q-in-connect-action-CreateContent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateKnowledgeBase  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:CreateKnowledgeBase](#list_q-in-connect-action-CreateKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateQuickResponse  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:CreateQuickResponse](#list_q-in-connect-action-CreateQuickResponse)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSession  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:CreateSession](#list_q-in-connect-action-CreateSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAssistant  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:DeleteAssistant](#list_q-in-connect-action-DeleteAssistant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssistantAssociation  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:DeleteAssistantAssociation](#list_q-in-connect-action-DeleteAssistantAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContent  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:DeleteContent](#list_q-in-connect-action-DeleteContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImportJob  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:DeleteImportJob](#list_q-in-connect-action-DeleteImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKnowledgeBase  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:DeleteKnowledgeBase](#list_q-in-connect-action-DeleteKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQuickResponse  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:DeleteQuickResponse](#list_q-in-connect-action-DeleteQuickResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAssistant  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetAssistant](#list_q-in-connect-action-GetAssistant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssistantAssociation  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetAssistantAssociation](#list_q-in-connect-action-GetAssistantAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContent  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetContent](#list_q-in-connect-action-GetContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContentSummary  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetContentSummary](#list_q-in-connect-action-GetContentSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImportJob  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetImportJob](#list_q-in-connect-action-GetImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKnowledgeBase  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetKnowledgeBase](#list_q-in-connect-action-GetKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQuickResponse  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetQuickResponse](#list_q-in-connect-action-GetQuickResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendations  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetRecommendations](#list_q-in-connect-action-GetRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSession  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetSession](#list_q-in-connect-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssistantAssociations  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:ListAssistantAssociations](#list_q-in-connect-action-ListAssistantAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssistants  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:ListAssistants](#list_q-in-connect-action-ListAssistants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContents  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:ListContents](#list_q-in-connect-action-ListContents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImportJobs  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:ListImportJobs](#list_q-in-connect-action-ListImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKnowledgeBases  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:ListKnowledgeBases](#list_q-in-connect-action-ListKnowledgeBases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQuickResponses  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:ListQuickResponses](#list_q-in-connect-action-ListQuickResponses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:ListTagsForResource](#list_q-in-connect-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   NotifyRecommendationsReceived  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:NotifyRecommendationsReceived](#list_q-in-connect-action-NotifyRecommendationsReceived) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   QueryAssistant  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:QueryAssistant](#list_q-in-connect-action-QueryAssistant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RemoveKnowledgeBaseTemplateUri  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:RemoveKnowledgeBaseTemplateUri](#list_q-in-connect-action-RemoveKnowledgeBaseTemplateUri) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchContent  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:SearchContent](#list_q-in-connect-action-SearchContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchQuickResponses  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:GetQuickResponse](#list_q-in-connect-action-GetQuickResponse)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [wisdom:SearchQuickResponses](#list_q-in-connect-action-SearchQuickResponses)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   SearchSessions  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:SearchSessions](#list_q-in-connect-action-SearchSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartContentUpload  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:StartContentUpload](#list_q-in-connect-action-StartContentUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImportJob  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:StartImportJob](#list_q-in-connect-action-StartImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:TagResource](#list_q-in-connect-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:UntagResource](#list_q-in-connect-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateContent  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:UpdateContent](#list_q-in-connect-action-UpdateContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKnowledgeBaseTemplateUri  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:UpdateKnowledgeBaseTemplateUri](#list_q-in-connect-action-UpdateKnowledgeBaseTemplateUri) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQuickResponse  **
  - **SDK client:** wisdom
  - **IAM action:**  [wisdom:UpdateQuickResponse](#list_q-in-connect-action-UpdateQuickResponse) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Q in Connect
<a name="list_q-in-connect-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateMessageTemplate](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ActivateMessageTemplate.html)  **
  - **Description:** Grants permission to activate a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Write

- **   [CreateAIAgent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateAIAgent.html)  **
  - **Description:** Grants permission to create an ai agent
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAIAgentVersion](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateAIAgentVersion.html)  **
  - **Description:** Grants permission to create an ai agent version
  - **Resource types (\*required):** [AIAgent\*](#list_q-in-connect-resource-AIAgent)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAIGuardrail](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateAIGuardrail.html)  **
  - **Description:** Grants permission to create an ai guardrail
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAIGuardrailVersion](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateAIGuardrailVersion.html)  **
  - **Description:** Grants permission to create an ai guardrail version
  - **Resource types (\*required):** [AIGuardrail\*](#list_q-in-connect-resource-AIGuardrail)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAIPrompt](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateAIPrompt.html)  **
  - **Description:** Grants permission to create an ai prompt
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAIPromptVersion](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateAIPromptVersion.html)  **
  - **Description:** Grants permission to create an ai prompt version
  - **Resource types (\*required):** [AIPrompt\*](#list_q-in-connect-resource-AIPrompt)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAssistant](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateAssistant.html)  **
  - **Description:** Grants permission to create an assistant
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAssistantAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateAssistantAssociation.html)  **
  - **Description:** Grants permission to create an association between an assistant and another resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateContent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateContent.html)  **
  - **Description:** Grants permission to create content
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateContentAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateContentAssociation.html)  **
  - **Description:** Grants permission to create a content association
  - **Resource types (\*required):** [Content\*](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKnowledgeBase](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateKnowledgeBase.html)  **
  - **Description:** Grants permission to create a knowledge base
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMessageTemplate](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateMessageTemplate.html)  **
  - **Description:** Grants permission to create a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMessageTemplateAttachment](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateMessageTemplateAttachment.html)  **
  - **Description:** Grants permission to create an attachment to a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Write

- **   [CreateMessageTemplateVersion](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateMessageTemplateVersion.html)  **
  - **Description:** Grants permission to create a version of a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Write

- **   [CreateQuickResponse](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateQuickResponse.html)  **
  - **Description:** Grants permission to create quick response
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSession](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateSession.html)  **
  - **Description:** Grants permission to create a session
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [DeactivateMessageTemplate](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeactivateMessageTemplate.html)  **
  - **Description:** Grants permission to deactivate a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Write

- **   [DeleteAIAgent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteAIAgent.html)  **
  - **Description:** Grants permission to delete an ai agent
  - **Resource types (\*required):** [AIAgent\*](#list_q-in-connect-resource-AIAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAIAgentVersion](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteAIAgentVersion.html)  **
  - **Description:** Grants permission to delete an ai agent version
  - **Resource types (\*required):** [AIAgent\*](#list_q-in-connect-resource-AIAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAIGuardrail](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteAIGuardrail.html)  **
  - **Description:** Grants permission to delete an ai guardrail
  - **Resource types (\*required):** [AIGuardrail\*](#list_q-in-connect-resource-AIGuardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAIGuardrailVersion](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteAIGuardrailVersion.html)  **
  - **Description:** Grants permission to delete an ai guardrail version
  - **Resource types (\*required):** [AIGuardrail\*](#list_q-in-connect-resource-AIGuardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAIPrompt](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteAIPrompt.html)  **
  - **Description:** Grants permission to delete an ai prompt
  - **Resource types (\*required):** [AIPrompt\*](#list_q-in-connect-resource-AIPrompt)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAIPromptVersion](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteAIPromptVersion.html)  **
  - **Description:** Grants permission to delete an ai prompt version
  - **Resource types (\*required):** [AIPrompt\*](#list_q-in-connect-resource-AIPrompt)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssistant](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteAssistant.html)  **
  - **Description:** Grants permission to delete an assistant
  - **Resource types (\*required):** [Assistant\*](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssistantAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteAssistantAssociation.html)  **
  - **Description:** Grants permission to delete an assistant association
  - **Resource types (\*required):** [AssistantAssociation\*](#list_q-in-connect-resource-AssistantAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteContent.html)  **
  - **Description:** Grants permission to delete content
  - **Resource types (\*required):** [Content\*](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContentAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteContentAssociation.html)  **
  - **Description:** Grants permission to delete a content association
  - **Resource types (\*required):** [Content\*](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ContentAssociation\*](#list_q-in-connect-resource-ContentAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImportJob](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteImportJob.html)  **
  - **Description:** Grants permission to delete a import job of a knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKnowledgeBase](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteKnowledgeBase.html)  **
  - **Description:** Grants permission to delete a knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMessageTemplate](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteMessageTemplate.html)  **
  - **Description:** Grants permission to delete a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Write

- **   [DeleteMessageTemplateAttachment](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteMessageTemplateAttachment.html)  **
  - **Description:** Grants permission to delete an attachment from a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Write

- **   [DeleteQuickResponse](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteQuickResponse.html)  **
  - **Description:** Grants permission to delete quick response
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [QuickResponse\*](#list_q-in-connect-resource-QuickResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAIAgent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetAIAgent.html)  **
  - **Description:** Grants permission to retrieve information about an ai agent
  - **Resource types (\*required):** [AIAgent\*](#list_q-in-connect-resource-AIAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAIGuardrail](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetAIGuardrail.html)  **
  - **Description:** Grants permission to retrieve information about an ai guardrail
  - **Resource types (\*required):** [AIGuardrail\*](#list_q-in-connect-resource-AIGuardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAIPrompt](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetAIPrompt.html)  **
  - **Description:** Grants permission to retrieve information about an ai prompt
  - **Resource types (\*required):** [AIPrompt\*](#list_q-in-connect-resource-AIPrompt)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssistant](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetAssistant.html)  **
  - **Description:** Grants permission to retrieve information about an assistant
  - **Resource types (\*required):** [Assistant\*](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssistantAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetAssistantAssociation.html)  **
  - **Description:** Grants permission to retrieve information about an assistant association
  - **Resource types (\*required):** [AssistantAssociation\*](#list_q-in-connect-resource-AssistantAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetContent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetContent.html)  **
  - **Description:** Grants permission to retrieve content, including a pre-signed URL to download the content
  - **Resource types (\*required):** [Content\*](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetContentAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetContentAssociation.html)  **
  - **Description:** Grants permission to retrieve information about a content association
  - **Resource types (\*required):** [Content\*](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ContentAssociation\*](#list_q-in-connect-resource-ContentAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetContentSummary](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetContentSummary.html)  **
  - **Description:** Grants permission to retrieve summary information about the content
  - **Resource types (\*required):** [Content\*](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImportJob](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetImportJob.html)  **
  - **Description:** Grants permission to retrieve information about the import job
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKnowledgeBase](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetKnowledgeBase.html)  **
  - **Description:** Grants permission to retrieve information about the knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMessageTemplate](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetMessageTemplate.html)  **
  - **Description:** Grants permission to retrieve a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Read

- **   [GetNextMessage](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetNextMessage.html)  **
  - **Description:** Grants permission to retrieve for next message in a session
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQuickResponse](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetQuickResponse.html)  **
  - **Description:** Grants permission to retrieve content
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [QuickResponse\*](#list_q-in-connect-resource-QuickResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommendations](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html)  **
  - **Description:** Grants permission to retrieve recommendations for the specified session
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetSession.html)  **
  - **Description:** Grants permission to retrieve information for a specified session
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAIAgentVersions](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListAIAgentVersions.html)  **
  - **Description:** Grants permission to list information about ai agent versions
  - **Resource types (\*required):** [AIAgent\*](#list_q-in-connect-resource-AIAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAIAgents](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListAIAgents.html)  **
  - **Description:** Grants permission to list information about ai agents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAIGuardrailVersions](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListAIGuardrailVersions.html)  **
  - **Description:** Grants permission to list information about ai guardrail versions
  - **Resource types (\*required):** [AIGuardrail\*](#list_q-in-connect-resource-AIGuardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAIGuardrails](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListAIGuardrails.html)  **
  - **Description:** Grants permission to list information about ai guardrails
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAIPromptVersions](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListAIPromptVersions.html)  **
  - **Description:** Grants permission to list information about ai prompt versions
  - **Resource types (\*required):** [AIPrompt\*](#list_q-in-connect-resource-AIPrompt)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAIPrompts](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListAIPrompts.html)  **
  - **Description:** Grants permission to list information about ai prompts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssistantAssociations](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListAssistantAssociations.html)  **
  - **Description:** Grants permission to list information about assistant associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssistants](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListAssistants.html)  **
  - **Description:** Grants permission to list information about assistants
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListContentAssociations](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListContentAssociations.html)  **
  - **Description:** Grants permission to list information about content associations
  - **Resource types (\*required):** [Content\*](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListContents](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListContents.html)  **
  - **Description:** Grants permission to list the content with a knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListImportJobs](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListImportJobs.html)  **
  - **Description:** Grants permission to list information about knowledge bases
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKnowledgeBases](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListKnowledgeBases.html)  **
  - **Description:** Grants permission to list information about knowledge bases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMessageTemplateVersions](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListMessageTemplateVersions.html)  **
  - **Description:** Grants permission to list message template versions for the specified message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** List

- **   [ListMessageTemplates](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListMessageTemplates.html)  **
  - **Description:** Grants permission to list the message templates for a knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMessages](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListMessages.html)  **
  - **Description:** Grants permission to list messages in a session
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModels](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListModels.html)  **
  - **Description:** Grants permission to list models available for an assistant
  - **Resource types (\*required):** [Assistant\*](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListQuickResponses](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListQuickResponses.html)  **
  - **Description:** Grants permission to list the quick response with a knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSpans](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListSpans.html)  **
  - **Description:** Grants permission to list AI agent traces for a session
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for the specified resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [NotifyRecommendationsReceived](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_NotifyRecommendationsReceived.html)  **
  - **Description:** Grants permission to remove the specified recommendations from the specified assistant's queue of newly available recommendations
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutFeedback](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_PutFeedback.html)  **
  - **Description:** Grants permission to submit feedback
  - **Resource types (\*required):** [Assistant\*](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [QueryAssistant](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QueryAssistant.html)  **
  - **Description:** Grants permission to perform a manual search against the specified assistant
  - **Resource types (\*required):** [Assistant\*](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RemoveAssistantAIAgent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_RemoveAssistantAIAgent.html)  **
  - **Description:** Grants permission to remove an ai agent from an assistant
  - **Resource types (\*required):** [Assistant\*](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveKnowledgeBaseTemplateUri](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_RemoveKnowledgeBaseTemplateUri.html)  **
  - **Description:** Grants permission to remove a URI template from a knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RenderMessageTemplate](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_RenderMessageTemplate.html)  **
  - **Description:** Grants permission to render a message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Read

- **   [Retrieve](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_Retrieve.html)  **
  - **Description:** Grants permission to retrieve knowledge content from specified assistant associations
  - **Resource types (\*required):** [Assistant\*](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchContent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SearchContent.html)  **
  - **Description:** Grants permission to search for content referencing a specified knowledge base. Can be used to get a specific content resource by its name
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchMessageTemplates](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SearchMessageTemplates.html)  **
  - **Description:** Grants permission to search for message templates referencing a specified knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:SearchFilter/Qualifier](#list_q-in-connect-wisdom_SearchFilter_Qualifier)<br />[wisdom:SearchFilter/RoutingProfileArn](#list_q-in-connect-wisdom_SearchFilter_RoutingProfileArn)
  - **Access level:** Read

- **   [SearchQuickResponses](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SearchQuickResponses.html)  **
  - **Description:** Grants permission to search for quick response referencing a specified knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:SearchFilter/RoutingProfileArn](#list_q-in-connect-wisdom_SearchFilter_RoutingProfileArn)
  - **Access level:** Read

- **   [SearchSessions](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SearchSessions.html)  **
  - **Description:** Grants permission to search for sessions referencing a specified assistant. Can be used to et a specific session resource by its name
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SendMessage](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SendMessage.html)  **
  - **Description:** Grants permission to send a message
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartContentUpload](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html)  **
  - **Description:** Grants permission to get a URL to upload content to a knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartImportJob](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartImportJob.html)  **
  - **Description:** Grants permission to create multiple quick responses
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add the specified tags to the specified resource
  - **Resource types (\*required):** [Assistant](#list_q-in-connect-resource-Assistant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [AssistantAssociation](#list_q-in-connect-resource-AssistantAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [Content](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [ContentAssociation](#list_q-in-connect-resource-ContentAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [KnowledgeBase](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [MessageTemplate](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Resource types (\*required):** [QuickResponse](#list_q-in-connect-resource-QuickResponse) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [Session](#list_q-in-connect-resource-Session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-in-connect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from the specified resource
  - **Resource types (\*required):** [Assistant](#list_q-in-connect-resource-Assistant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [AssistantAssociation](#list_q-in-connect-resource-AssistantAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [Content](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [ContentAssociation](#list_q-in-connect-resource-ContentAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [KnowledgeBase](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [MessageTemplate](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Resource types (\*required):** [QuickResponse](#list_q-in-connect-resource-QuickResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Resource types (\*required):** [Session](#list_q-in-connect-resource-Session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-in-connect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAIAgent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateAIAgent.html)  **
  - **Description:** Grants permission to update information about an ai agent
  - **Resource types (\*required):** [AIAgent\*](#list_q-in-connect-resource-AIAgent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAIGuardrail](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateAIGuardrail.html)  **
  - **Description:** Grants permission to update information about an ai guardrail
  - **Resource types (\*required):** [AIGuardrail\*](#list_q-in-connect-resource-AIGuardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAIPrompt](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateAIPrompt.html)  **
  - **Description:** Grants permission to update information about an ai prompt
  - **Resource types (\*required):** [AIPrompt\*](#list_q-in-connect-resource-AIPrompt)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssistantAIAgent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateAssistantAIAgent.html)  **
  - **Description:** Grants permission to update assistant information about an ai agent
  - **Resource types (\*required):** [Assistant\*](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateContent.html)  **
  - **Description:** Grants permission to update information about the content
  - **Resource types (\*required):** [Content\*](#list_q-in-connect-resource-Content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKnowledgeBaseTemplateUri](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateKnowledgeBaseTemplateUri.html)  **
  - **Description:** Grants permission to update the template URI of a knowledge base
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMessageTemplate](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateMessageTemplate.html)  **
  - **Description:** Grants permission to update content of the message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Write

- **   [UpdateMessageTemplateMetadata](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateMessageTemplateMetadata.html)  **
  - **Description:** Grants permission to update metadata of the message template
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [MessageTemplate\*](#list_q-in-connect-resource-MessageTemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn)
  - **Access level:** Write

- **   [UpdateQuickResponse](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateQuickResponse.html)  **
  - **Description:** Grants permission to update information or content of the quick response
  - **Resource types (\*required):** [KnowledgeBase\*](#list_q-in-connect-resource-KnowledgeBase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [QuickResponse\*](#list_q-in-connect-resource-QuickResponse) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSession](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateSession.html)  **
  - **Description:** Grants permission to update a session
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSessionData](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateSessionData.html)  **
  - **Description:** Grants permission to update data stored in a session
  - **Resource types (\*required):** [Session\*](#list_q-in-connect-resource-Session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Q in Connect
<a name="list_q-in-connect-permission-only-actions"></a>

The following actions are defined by Amazon Q in Connect but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](${UserGuideDocPage})  **
  - **Description:** Grants permission to configure vended log delivery for an assistant
  - **Resource types (\*required):** [Assistant](#list_q-in-connect-resource-Assistant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon Q in Connect
<a name="list_q-in-connect-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AIAgent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AIAgentData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:ai-agent/${AssistantId}/${AIAgentId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [AIGuardrail](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AIGuardrailData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:ai-guardrail/${AssistantId}/${AIGuardrailId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [AIPrompt](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AIPromptData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:ai-prompt/${AssistantId}/${AIPromptId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [Assistant](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AssistantData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:assistant/${AssistantId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [AssistantAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_AssistantAssociationData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:association/${AssistantId}/${AssistantAssociationId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [Content](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ContentData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:content/${KnowledgeBaseId}/${ContentId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [ContentAssociation](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_ContentAssociationData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:content-association/${KnowledgeBaseId}/${ContentId}/${ContentAssociationId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [KnowledgeBase](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_KnowledgeBaseData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:knowledge-base/${KnowledgeBaseId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [MessageTemplate](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_MessageTemplateData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:message-template/${KnowledgeBaseId}/${MessageTemplateId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_)<br />[wisdom:MessageTemplate/RoutingProfileArn](#list_q-in-connect-wisdom_MessageTemplate_RoutingProfileArn) | 
|  [QuickResponse](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QuickResponseData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:quick-response/${KnowledgeBaseId}/${QuickResponseId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 
|  [Session](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SessionData.html)  | arn:${Partition}:wisdom:${Region}:${Account}:session/${AssistantId}/${SessionId} | [aws:ResourceTag/${TagKey}](#list_q-in-connect-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Q in Connect
<a name="list_q-in-connect-policy-keys"></a>

Amazon Q in Connect defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [wisdom:MessageTemplate/RoutingProfileArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonconnectwisdom.html#amazonconnectwisdom-policy-keys)  | Filters access by the connect routing profile arns associated with the resource | ArrayOfARN | 
|   [wisdom:SearchFilter/Qualifier](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonconnectwisdom.html#amazonconnectwisdom-policy-keys)  | Filters access by the qualifiers that are passed in the request | ArrayOfString | 
|   [wisdom:SearchFilter/RoutingProfileArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonconnectwisdom.html#amazonconnectwisdom-policy-keys)  | Filters access by the connect routing profile arn that is passed in the request | ARN | 