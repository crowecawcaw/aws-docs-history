

# Actions, resources, and condition keys for AWS Clean Rooms
<a name="list_cleanrooms"></a>

AWS Clean Rooms (service prefix: `cleanrooms`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/clean-rooms/latest/apireference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cleanrooms/cleanrooms.json) for this service.

**Topics**
+ [API operations defined by AWS Clean Rooms](#list_cleanrooms-operations)
+ [Actions defined by AWS Clean Rooms](#list_cleanrooms-actions-as-permissions)
+ [Permission-only actions for AWS Clean Rooms](#list_cleanrooms-permission-only-actions)
+ [Resource types defined by AWS Clean Rooms](#list_cleanrooms-resources-for-iam-policies)
+ [Condition keys for AWS Clean Rooms](#list_cleanrooms-policy-keys)

## API operations defined by AWS Clean Rooms
<a name="list_cleanrooms-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cleanrooms-actions-as-permissions).




- **   BatchGetCollaborationAnalysisTemplate  **
  - **IAM action:**  [cleanrooms:BatchGetCollaborationAnalysisTemplate](#list_cleanrooms-action-BatchGetCollaborationAnalysisTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetSchema  **
  - **IAM action:**  [cleanrooms:BatchGetSchema](#list_cleanrooms-action-BatchGetSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetSchemaAnalysisRule  **
  - **IAM action:**  [cleanrooms:BatchGetSchemaAnalysisRule](#list_cleanrooms-action-BatchGetSchemaAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateAnalysisTemplate  **
  - **IAM action:**  [cleanrooms:CreateAnalysisTemplate](#list_cleanrooms-action-CreateAnalysisTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms.amazonaws.com / **Access level:** Write

- **   CreateCollaboration  **
  - **IAM action:**  [cleanrooms:CreateCollaboration](#list_cleanrooms-action-CreateCollaboration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCollaborationChangeRequest  **
  - **IAM action:**  [cleanrooms:CreateCollaborationChangeRequest](#list_cleanrooms-action-CreateCollaborationChangeRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConfiguredAudienceModelAssociation  **
  - **IAM action:**  [cleanrooms:CreateConfiguredAudienceModelAssociation](#list_cleanrooms-action-CreateConfiguredAudienceModelAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfiguredTable  **
  - **IAM action:**  [cleanrooms:CreateConfiguredTable](#list_cleanrooms-action-CreateConfiguredTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfiguredTableAnalysisRule  **
  - **IAM action:**  [cleanrooms:CreateConfiguredTableAnalysisRule](#list_cleanrooms-action-CreateConfiguredTableAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConfiguredTableAssociation  **
  - **IAM action:**  [cleanrooms:CreateConfiguredTableAssociation](#list_cleanrooms-action-CreateConfiguredTableAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms.amazonaws.com / **Access level:** Write

- **   CreateConfiguredTableAssociationAnalysisRule  **
  - **IAM action:**  [cleanrooms:CreateConfiguredTableAssociationAnalysisRule](#list_cleanrooms-action-CreateConfiguredTableAssociationAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIdMappingTable  **
  - **IAM action:**  [cleanrooms:CreateIdMappingTable](#list_cleanrooms-action-CreateIdMappingTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIdNamespaceAssociation  **
  - **IAM action:**  [cleanrooms:CreateIdNamespaceAssociation](#list_cleanrooms-action-CreateIdNamespaceAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIntermediateTable  **
  - **IAM action:**  [cleanrooms:CreateIntermediateTable](#list_cleanrooms-action-CreateIntermediateTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIntermediateTableAnalysisRule  **
  - **IAM action:**  [cleanrooms:CreateIntermediateTableAnalysisRule](#list_cleanrooms-action-CreateIntermediateTableAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMembership  **
  - **IAM action:**  [cleanrooms:CreateMembership](#list_cleanrooms-action-CreateMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms.amazonaws.com / **Access level:** Write

- **   CreatePrivacyBudgetTemplate  **
  - **IAM action:**  [cleanrooms:CreatePrivacyBudgetTemplate](#list_cleanrooms-action-CreatePrivacyBudgetTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAnalysisTemplate  **
  - **IAM action:**  [cleanrooms:DeleteAnalysisTemplate](#list_cleanrooms-action-DeleteAnalysisTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCollaboration  **
  - **IAM action:**  [cleanrooms:DeleteCollaboration](#list_cleanrooms-action-DeleteCollaboration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredAudienceModelAssociation  **
  - **IAM action:**  [cleanrooms:DeleteConfiguredAudienceModelAssociation](#list_cleanrooms-action-DeleteConfiguredAudienceModelAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredTable  **
  - **IAM action:**  [cleanrooms:DeleteConfiguredTable](#list_cleanrooms-action-DeleteConfiguredTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredTableAnalysisRule  **
  - **IAM action:**  [cleanrooms:DeleteConfiguredTableAnalysisRule](#list_cleanrooms-action-DeleteConfiguredTableAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredTableAssociation  **
  - **IAM action:**  [cleanrooms:DeleteConfiguredTableAssociation](#list_cleanrooms-action-DeleteConfiguredTableAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredTableAssociationAnalysisRule  **
  - **IAM action:**  [cleanrooms:DeleteConfiguredTableAssociationAnalysisRule](#list_cleanrooms-action-DeleteConfiguredTableAssociationAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIdMappingTable  **
  - **IAM action:**  [cleanrooms:DeleteIdMappingTable](#list_cleanrooms-action-DeleteIdMappingTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIdNamespaceAssociation  **
  - **IAM action:**  [cleanrooms:DeleteIdNamespaceAssociation](#list_cleanrooms-action-DeleteIdNamespaceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntermediateTable  **
  - **IAM action:**  [cleanrooms:DeleteIntermediateTable](#list_cleanrooms-action-DeleteIntermediateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntermediateTableAnalysisRule  **
  - **IAM action:**  [cleanrooms:DeleteIntermediateTableAnalysisRule](#list_cleanrooms-action-DeleteIntermediateTableAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMember  **
  - **IAM action:**  [cleanrooms:DeleteMember](#list_cleanrooms-action-DeleteMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMembership  **
  - **IAM action:**  [cleanrooms:DeleteMembership](#list_cleanrooms-action-DeleteMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePrivacyBudgetTemplate  **
  - **IAM action:**  [cleanrooms:DeletePrivacyBudgetTemplate](#list_cleanrooms-action-DeletePrivacyBudgetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisallowIntermediateTable  **
  - **IAM action:**  [cleanrooms:DisallowIntermediateTable](#list_cleanrooms-action-DisallowIntermediateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAnalysisLogExport  **
  - **IAM action:**  [cleanrooms:GetAnalysisLogExport](#list_cleanrooms-action-GetAnalysisLogExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnalysisTemplate  **
  - **IAM action:**  [cleanrooms:GetAnalysisTemplate](#list_cleanrooms-action-GetAnalysisTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaboration  **
  - **IAM action:**  [cleanrooms:GetCollaboration](#list_cleanrooms-action-GetCollaboration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaborationAnalysisTemplate  **
  - **IAM action:**  [cleanrooms:GetCollaborationAnalysisTemplate](#list_cleanrooms-action-GetCollaborationAnalysisTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaborationChangeRequest  **
  - **IAM action:**  [cleanrooms:GetCollaborationChangeRequest](#list_cleanrooms-action-GetCollaborationChangeRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaborationConfiguredAudienceModelAssociation  **
  - **IAM action:**  [cleanrooms:GetCollaborationConfiguredAudienceModelAssociation](#list_cleanrooms-action-GetCollaborationConfiguredAudienceModelAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaborationIdNamespaceAssociation  **
  - **IAM action:**  [cleanrooms:GetCollaborationIdNamespaceAssociation](#list_cleanrooms-action-GetCollaborationIdNamespaceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaborationPrivacyBudgetTemplate  **
  - **IAM action:**  [cleanrooms:GetCollaborationPrivacyBudgetTemplate](#list_cleanrooms-action-GetCollaborationPrivacyBudgetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredAudienceModelAssociation  **
  - **IAM action:**  [cleanrooms:GetConfiguredAudienceModelAssociation](#list_cleanrooms-action-GetConfiguredAudienceModelAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredTable  **
  - **IAM action:**  [cleanrooms:GetConfiguredTable](#list_cleanrooms-action-GetConfiguredTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredTableAnalysisRule  **
  - **IAM action:**  [cleanrooms:GetConfiguredTableAnalysisRule](#list_cleanrooms-action-GetConfiguredTableAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredTableAssociation  **
  - **IAM action:**  [cleanrooms:GetConfiguredTableAssociation](#list_cleanrooms-action-GetConfiguredTableAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredTableAssociationAnalysisRule  **
  - **IAM action:**  [cleanrooms:GetConfiguredTableAssociationAnalysisRule](#list_cleanrooms-action-GetConfiguredTableAssociationAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdMappingTable  **
  - **IAM action:**  [cleanrooms:GetIdMappingTable](#list_cleanrooms-action-GetIdMappingTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdNamespaceAssociation  **
  - **IAM action:**  [cleanrooms:GetIdNamespaceAssociation](#list_cleanrooms-action-GetIdNamespaceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntermediateTable  **
  - **IAM action:**  [cleanrooms:GetIntermediateTable](#list_cleanrooms-action-GetIntermediateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntermediateTableAnalysisRule  **
  - **IAM action:**  [cleanrooms:GetIntermediateTableAnalysisRule](#list_cleanrooms-action-GetIntermediateTableAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMembership  **
  - **IAM action:**  [cleanrooms:GetMembership](#list_cleanrooms-action-GetMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPrivacyBudgetTemplate  **
  - **IAM action:**  [cleanrooms:GetPrivacyBudgetTemplate](#list_cleanrooms-action-GetPrivacyBudgetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProtectedJob  **
  - **IAM action:**  [cleanrooms:GetProtectedJob](#list_cleanrooms-action-GetProtectedJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProtectedQuery  **
  - **IAM action:**  [cleanrooms:GetProtectedQuery](#list_cleanrooms-action-GetProtectedQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchema  **
  - **IAM action:**  [cleanrooms:GetSchema](#list_cleanrooms-action-GetSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchemaAnalysisRule  **
  - **IAM action:**  [cleanrooms:GetSchemaAnalysisRule](#list_cleanrooms-action-GetSchemaAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnalysisLogExports  **
  - **IAM action:**  [cleanrooms:ListAnalysisLogExports](#list_cleanrooms-action-ListAnalysisLogExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAnalysisTemplates  **
  - **IAM action:**  [cleanrooms:ListAnalysisTemplates](#list_cleanrooms-action-ListAnalysisTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationAnalysisTemplates  **
  - **IAM action:**  [cleanrooms:ListCollaborationAnalysisTemplates](#list_cleanrooms-action-ListCollaborationAnalysisTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationChangeRequests  **
  - **IAM action:**  [cleanrooms:ListCollaborationChangeRequests](#list_cleanrooms-action-ListCollaborationChangeRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationConfiguredAudienceModelAssociations  **
  - **IAM action:**  [cleanrooms:ListCollaborationConfiguredAudienceModelAssociations](#list_cleanrooms-action-ListCollaborationConfiguredAudienceModelAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationIdNamespaceAssociations  **
  - **IAM action:**  [cleanrooms:ListCollaborationIdNamespaceAssociations](#list_cleanrooms-action-ListCollaborationIdNamespaceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationPrivacyBudgetTemplates  **
  - **IAM action:**  [cleanrooms:ListCollaborationPrivacyBudgetTemplates](#list_cleanrooms-action-ListCollaborationPrivacyBudgetTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationPrivacyBudgets  **
  - **IAM action:**  [cleanrooms:ListCollaborationPrivacyBudgets](#list_cleanrooms-action-ListCollaborationPrivacyBudgets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborations  **
  - **IAM action:**  [cleanrooms:ListCollaborations](#list_cleanrooms-action-ListCollaborations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfiguredAudienceModelAssociations  **
  - **IAM action:**  [cleanrooms:ListConfiguredAudienceModelAssociations](#list_cleanrooms-action-ListConfiguredAudienceModelAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfiguredTableAssociations  **
  - **IAM action:**  [cleanrooms:ListConfiguredTableAssociations](#list_cleanrooms-action-ListConfiguredTableAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfiguredTables  **
  - **IAM action:**  [cleanrooms:ListConfiguredTables](#list_cleanrooms-action-ListConfiguredTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdMappingTables  **
  - **IAM action:**  [cleanrooms:ListIdMappingTables](#list_cleanrooms-action-ListIdMappingTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdNamespaceAssociations  **
  - **IAM action:**  [cleanrooms:ListIdNamespaceAssociations](#list_cleanrooms-action-ListIdNamespaceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntermediateTableVersions  **
  - **IAM action:**  [cleanrooms:ListIntermediateTableVersions](#list_cleanrooms-action-ListIntermediateTableVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntermediateTables  **
  - **IAM action:**  [cleanrooms:ListIntermediateTables](#list_cleanrooms-action-ListIntermediateTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMembers  **
  - **IAM action:**  [cleanrooms:ListMembers](#list_cleanrooms-action-ListMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMemberships  **
  - **IAM action:**  [cleanrooms:ListMemberships](#list_cleanrooms-action-ListMemberships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrivacyBudgetTemplates  **
  - **IAM action:**  [cleanrooms:ListPrivacyBudgetTemplates](#list_cleanrooms-action-ListPrivacyBudgetTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrivacyBudgets  **
  - **IAM action:**  [cleanrooms:ListPrivacyBudgets](#list_cleanrooms-action-ListPrivacyBudgets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProtectedJobs  **
  - **IAM action:**  [cleanrooms:ListProtectedJobs](#list_cleanrooms-action-ListProtectedJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProtectedQueries  **
  - **IAM action:**  [cleanrooms:ListProtectedQueries](#list_cleanrooms-action-ListProtectedQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchemas  **
  - **IAM action:**  [cleanrooms:ListSchemas](#list_cleanrooms-action-ListSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [cleanrooms:ListTagsForResource](#list_cleanrooms-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PopulateIdMappingTable  **
  - **IAM action:**  [cleanrooms:PopulateIdMappingTable](#list_cleanrooms-action-PopulateIdMappingTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PopulateIntermediateTable  **
  - **IAM action:**  [cleanrooms:PopulateIntermediateTable](#list_cleanrooms-action-PopulateIntermediateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PreviewPrivacyImpact  **
  - **IAM action:**  [cleanrooms:PreviewPrivacyImpact](#list_cleanrooms-action-PreviewPrivacyImpact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartAnalysisLogExport  **
  - **IAM action:**  [cleanrooms:StartAnalysisLogExport](#list_cleanrooms-action-StartAnalysisLogExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartProtectedJob  **
  - **IAM action:**  [cleanrooms:StartProtectedJob](#list_cleanrooms-action-StartProtectedJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartProtectedQuery  **
  - **IAM action:**  [cleanrooms:StartProtectedQuery](#list_cleanrooms-action-StartProtectedQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [cleanrooms:TagResource](#list_cleanrooms-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [cleanrooms:UntagResource](#list_cleanrooms-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAnalysisTemplate  **
  - **IAM action:**  [cleanrooms:UpdateAnalysisTemplate](#list_cleanrooms-action-UpdateAnalysisTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCollaboration  **
  - **IAM action:**  [cleanrooms:UpdateCollaboration](#list_cleanrooms-action-UpdateCollaboration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCollaborationChangeRequest  **
  - **IAM action:**  [cleanrooms:UpdateCollaborationChangeRequest](#list_cleanrooms-action-UpdateCollaborationChangeRequest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfiguredAudienceModelAssociation  **
  - **IAM action:**  [cleanrooms:UpdateConfiguredAudienceModelAssociation](#list_cleanrooms-action-UpdateConfiguredAudienceModelAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfiguredTable  **
  - **IAM action:**  [cleanrooms:UpdateConfiguredTable](#list_cleanrooms-action-UpdateConfiguredTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:UpdateConfiguredTableAllowedColumns](#list_cleanrooms-action-UpdateConfiguredTableAllowedColumns)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms:UpdateConfiguredTableReference](#list_cleanrooms-action-UpdateConfiguredTableReference)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateConfiguredTableAnalysisRule  **
  - **IAM action:**  [cleanrooms:UpdateConfiguredTableAnalysisRule](#list_cleanrooms-action-UpdateConfiguredTableAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfiguredTableAssociation  **
  - **IAM action:**  [cleanrooms:UpdateConfiguredTableAssociation](#list_cleanrooms-action-UpdateConfiguredTableAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms.amazonaws.com / **Access level:** Write

- **   UpdateConfiguredTableAssociationAnalysisRule  **
  - **IAM action:**  [cleanrooms:UpdateConfiguredTableAssociationAnalysisRule](#list_cleanrooms-action-UpdateConfiguredTableAssociationAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIdMappingTable  **
  - **IAM action:**  [cleanrooms:UpdateIdMappingTable](#list_cleanrooms-action-UpdateIdMappingTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIdNamespaceAssociation  **
  - **IAM action:**  [cleanrooms:UpdateIdNamespaceAssociation](#list_cleanrooms-action-UpdateIdNamespaceAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIntermediateTable  **
  - **IAM action:**  [cleanrooms:UpdateIntermediateTable](#list_cleanrooms-action-UpdateIntermediateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIntermediateTableAnalysisRule  **
  - **IAM action:**  [cleanrooms:UpdateIntermediateTableAnalysisRule](#list_cleanrooms-action-UpdateIntermediateTableAnalysisRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMembership  **
  - **IAM action:**  [cleanrooms:UpdateMembership](#list_cleanrooms-action-UpdateMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms.amazonaws.com / **Access level:** Write

- **   UpdatePrivacyBudgetTemplate  **
  - **IAM action:**  [cleanrooms:UpdatePrivacyBudgetTemplate](#list_cleanrooms-action-UpdatePrivacyBudgetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProtectedJob  **
  - **IAM action:**  [cleanrooms:UpdateProtectedJob](#list_cleanrooms-action-UpdateProtectedJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProtectedQuery  **
  - **IAM action:**  [cleanrooms:UpdateProtectedQuery](#list_cleanrooms-action-UpdateProtectedQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Clean Rooms
<a name="list_cleanrooms-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetCollaborationAnalysisTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_BatchGetCollaborationAnalysisTemplate.html)  **
  - **Description:** Grants permission to view details of analysisTemplates associated to the collaboration
  - **Resource types (\*required):** [analysistemplate\*](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetSchema](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_BatchGetSchema.html)  **
  - **Description:** Grants permission to view details for schemas
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredtableassociation](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [idmappingtable](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [intermediatetable](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetSchemaAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_BatchGetSchemaAnalysisRule.html)  **
  - **Description:** Grants permission to view analysis rules associated with schemas
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredtableassociation](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [idmappingtable](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [intermediatetable](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateAnalysisTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateAnalysisTemplate.html)  **
  - **Description:** Grants permission to create a new analysis template
  - **Resource types (\*required):** [analysistemplate\*](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCollaboration](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateCollaboration.html)  **
  - **Description:** Grants permission to create a new collaboration, a shared data collaboration environment
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCollaborationChangeRequest](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateCollaborationChangeRequest.html)  **
  - **Description:** Grants permission to create a change request in a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguredAudienceModelAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredAudienceModelAssociation.html)  **
  - **Description:** Grants permission to link a Cleanrooms ML configured audience model with a collaboration by creating a new association
  - **Resource types (\*required):** [configuredaudiencemodelassociation\*](#list_cleanrooms-resource-configuredaudiencemodelassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguredTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTable.html)  **
  - **Description:** Grants permission to create a new configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguredTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTableAnalysisRule.html)  **
  - **Description:** Grants permission to create a analysis rule for a configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateConfiguredTableAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTableAssociation.html)  **
  - **Description:** Grants permission to link a configured table with a collaboration by creating a new association
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguredTableAssociationAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredTableAssociationAnalysisRule.html)  **
  - **Description:** Grants permission to create an analysis rule for a configured table association
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIdMappingTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateIdMappingTable.html)  **
  - **Description:** Grants permission to link an id mapping workflow with a collaboration by creating a new id mapping table
  - **Resource types (\*required):** [idmappingtable\*](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIdNamespaceAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateIdNamespaceAssociation.html)  **
  - **Description:** Grants permission to link an AWS Entity Resolution Id Namespace with a collaboration by creating a new association
  - **Resource types (\*required):** [idnamespaceassociation\*](#list_cleanrooms-resource-idnamespaceassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntermediateTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateIntermediateTable.html)  **
  - **Description:** Grants permission to create a new intermediate table in a membership
  - **Resource types (\*required):** [analysistemplate](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntermediateTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateIntermediateTableAnalysisRule.html)  **
  - **Description:** Grants permission to create an analysis rule for an intermediate table
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMembership](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateMembership.html)  **
  - **Description:** Grants permission to join collaborations by creating a membership
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePrivacyBudgetTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreatePrivacyBudgetTemplate.html)  **
  - **Description:** Grants permission to create a new privacy budget template
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [privacybudgettemplate\*](#list_cleanrooms-resource-privacybudgettemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAnalysisTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteAnalysisTemplate.html)  **
  - **Description:** Grants permission to delete an existing analysis template
  - **Resource types (\*required):** [analysistemplate\*](#list_cleanrooms-resource-analysistemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCollaboration](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteCollaboration.html)  **
  - **Description:** Grants permission to delete an existing collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfiguredAudienceModelAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteConfiguredAudienceModelAssociation.html)  **
  - **Description:** Grants permission to delete an existing configured audience model association
  - **Resource types (\*required):** [configuredaudiencemodelassociation\*](#list_cleanrooms-resource-configuredaudiencemodelassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfiguredTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteConfiguredTable.html)  **
  - **Description:** Grants permission to delete a configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfiguredTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteConfiguredTableAnalysisRule.html)  **
  - **Description:** Grants permission to delete an existing analysis rule
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfiguredTableAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteConfiguredTableAssociation.html)  **
  - **Description:** Grants permission to remove a configured table association from a collaboration
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfiguredTableAssociationAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteConfiguredTableAssociationAnalysisRule.html)  **
  - **Description:** Grants permission to delete an existing configured table association analysis rule
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIdMappingTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteIdMappingTable.html)  **
  - **Description:** Grants permission to remove an id mapping table from a collaboration
  - **Resource types (\*required):** [idmappingtable\*](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIdNamespaceAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteIdNamespaceAssociation.html)  **
  - **Description:** Grants permission to remove an Id Namespace Association from a collaboration
  - **Resource types (\*required):** [idnamespaceassociation\*](#list_cleanrooms-resource-idnamespaceassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntermediateTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteIntermediateTable.html)  **
  - **Description:** Grants permission to remove an intermediate table from a collaboration
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntermediateTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteIntermediateTableAnalysisRule.html)  **
  - **Description:** Grants permission to delete an existing analysis rule for an intermediate table
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMember](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteMember.html)  **
  - **Description:** Grants permission to delete members from a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMembership](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteMembership.html)  **
  - **Description:** Grants permission to leave collaborations by deleting a membership
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePrivacyBudgetTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeletePrivacyBudgetTemplate.html)  **
  - **Description:** Grants permission to delete an existing privacy budget template
  - **Resource types (\*required):** [privacybudgettemplate\*](#list_cleanrooms-resource-privacybudgettemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisallowIntermediateTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DisallowIntermediateTable.html)  **
  - **Description:** Grants permission to invalidate an intermediate table
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAnalysisLogExport](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetAnalysisLogExport.html)  **
  - **Description:** Grants permission to get an analysis log export
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnalysisTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetAnalysisTemplate.html)  **
  - **Description:** Grants permission to view details for an analysis template
  - **Resource types (\*required):** [analysistemplate\*](#list_cleanrooms-resource-analysistemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCollaboration](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetCollaboration.html)  **
  - **Description:** Grants permission to view details for a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCollaborationAnalysisTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetCollaborationAnalysisTemplate.html)  **
  - **Description:** Grants permission to view details for an analysis template within a collaboration
  - **Resource types (\*required):** [analysistemplate\*](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCollaborationChangeRequest](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetCollaborationChangeRequest.html)  **
  - **Description:** Grants permission to get a change request in a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCollaborationConfiguredAudienceModelAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetCollaborationConfiguredAudienceModelAssociation.html)  **
  - **Description:** Grants permission to view details for a configured audience model association within a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredaudiencemodelassociation\*](#list_cleanrooms-resource-configuredaudiencemodelassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCollaborationIdNamespaceAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetCollaborationIdNamespaceAssociation.html)  **
  - **Description:** Grants permission to get id namespace association within a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [idnamespaceassociation\*](#list_cleanrooms-resource-idnamespaceassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCollaborationPrivacyBudgetTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetCollaborationPrivacyBudgetTemplate.html)  **
  - **Description:** Grants permission to view details for a privacy budget template within a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [privacybudgettemplate\*](#list_cleanrooms-resource-privacybudgettemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfiguredAudienceModelAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetConfiguredAudienceModelAssociation.html)  **
  - **Description:** Grants permission to view details for a configured audience model association
  - **Resource types (\*required):** [configuredaudiencemodelassociation\*](#list_cleanrooms-resource-configuredaudiencemodelassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfiguredTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetConfiguredTable.html)  **
  - **Description:** Grants permission to view details for a configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfiguredTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetConfiguredTableAnalysisRule.html)  **
  - **Description:** Grants permission to view analysis rules for a configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfiguredTableAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetConfiguredTableAssociation.html)  **
  - **Description:** Grants permission to view details for a configured table association
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfiguredTableAssociationAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetConfiguredTableAssociationAnalysisRule.html)  **
  - **Description:** Grants permission to view analysis rules for a configured table association
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdMappingTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetIdMappingTable.html)  **
  - **Description:** Grants permission to view details of an id mapping table
  - **Resource types (\*required):** [idmappingtable\*](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdNamespaceAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetIdNamespaceAssociation.html)  **
  - **Description:** Grants permission to view details of an id namespace association
  - **Resource types (\*required):** [idnamespaceassociation\*](#list_cleanrooms-resource-idnamespaceassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntermediateTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetIntermediateTable.html)  **
  - **Description:** Grants permission to view details of an intermediate table
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntermediateTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetIntermediateTableAnalysisRule.html)  **
  - **Description:** Grants permission to view analysis rules for an intermediate table
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMembership](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetMembership.html)  **
  - **Description:** Grants permission to view details about a membership
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPrivacyBudgetTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetPrivacyBudgetTemplate.html)  **
  - **Description:** Grants permission to view details for a privacy budget template
  - **Resource types (\*required):** [privacybudgettemplate\*](#list_cleanrooms-resource-privacybudgettemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProtectedJob](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetProtectedJob.html)  **
  - **Description:** Grants permission to view a protected job
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProtectedQuery](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetProtectedQuery.html)  **
  - **Description:** Grants permission to view a protected query
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchema](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetSchema.html)  **
  - **Description:** Grants permission to view details for a schema
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchemaAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetSchemaAnalysisRule.html)  **
  - **Description:** Grants permission to view analysis rules associated with a schema
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAnalysisLogExports](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListAnalysisLogExports.html)  **
  - **Description:** Grants permission to list analysis log exports
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAnalysisTemplates](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListAnalysisTemplates.html)  **
  - **Description:** Grants permission to list available analysis templates
  - **Resource types (\*required):** [analysistemplate\*](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCollaborationAnalysisTemplates](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListCollaborationAnalysisTemplates.html)  **
  - **Description:** Grants permission to list available analysis templates within a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCollaborationChangeRequests](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListCollaborationChangeRequests.html)  **
  - **Description:** Grants permission to list change requests in a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCollaborationConfiguredAudienceModelAssociations](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListCollaborationConfiguredAudienceModelAssociations.html)  **
  - **Description:** Grants permission to list available configured audience model association within a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCollaborationIdNamespaceAssociations](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListCollaborationIdNamespaceAssociations.html)  **
  - **Description:** Grants permission to list id namespace within a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCollaborationPrivacyBudgetTemplates](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListCollaborationPrivacyBudgetTemplates.html)  **
  - **Description:** Grants permission to list available privacy budget templates within a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCollaborationPrivacyBudgets](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListCollaborationPrivacyBudgets.html)  **
  - **Description:** Grants permission to list privacy budgets within a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCollaborations](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListCollaborations.html)  **
  - **Description:** Grants permission to list available collaborations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfiguredAudienceModelAssociations](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListConfiguredAudienceModelAssociations.html)  **
  - **Description:** Grants permission to list available configured audience model associations for a membership
  - **Resource types (\*required):** [configuredaudiencemodelassociation\*](#list_cleanrooms-resource-configuredaudiencemodelassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConfiguredTableAssociations](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListConfiguredTableAssociations.html)  **
  - **Description:** Grants permission to list available configured table associations for a membership
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConfiguredTables](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListConfiguredTables.html)  **
  - **Description:** Grants permission to list available configured tables
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIdMappingTables](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListIdMappingTables.html)  **
  - **Description:** Grants permission to list available id mapping tables for a membership
  - **Resource types (\*required):** [idmappingtable\*](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIdNamespaceAssociations](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListIdNamespaceAssociations.html)  **
  - **Description:** Grants permission to list entity resolution data associations for a membership
  - **Resource types (\*required):** [idnamespaceassociation\*](#list_cleanrooms-resource-idnamespaceassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntermediateTableVersions](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListIntermediateTableVersions.html)  **
  - **Description:** Grants permission to list versions of an intermediate table
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntermediateTables](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListIntermediateTables.html)  **
  - **Description:** Grants permission to list intermediate tables for a membership
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMembers](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListMembers.html)  **
  - **Description:** Grants permission to list the members of a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMemberships](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListMemberships.html)  **
  - **Description:** Grants permission to list available memberships
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPrivacyBudgetTemplates](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListPrivacyBudgetTemplates.html)  **
  - **Description:** Grants permission to list available privacy budget templates
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [privacybudgettemplate\*](#list_cleanrooms-resource-privacybudgettemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPrivacyBudgets](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListPrivacyBudgets.html)  **
  - **Description:** Grants permission to list available privacy budgets
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProtectedJobs](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListProtectedJobs.html)  **
  - **Description:** Grants permission to list protected jobs
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProtectedQueries](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListProtectedQueries.html)  **
  - **Description:** Grants permission to list protected queries
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSchemas](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListSchemas.html)  **
  - **Description:** Grants permission to view available schemas for a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [analysistemplate](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [collaboration](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredaudiencemodelassociation](#list_cleanrooms-resource-configuredaudiencemodelassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredtable](#list_cleanrooms-resource-configuredtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredtableassociation](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [intermediatetable](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [privacybudgettemplate](#list_cleanrooms-resource-privacybudgettemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PopulateIdMappingTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PopulateIdMappingTable.html)  **
  - **Description:** Grants permission to start an Id Mapping Job in AWS Entity Resolution to generate id mapping results in cleanrooms collaboration. 
  - **Resource types (\*required):** [idmappingtable\*](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PopulateIntermediateTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PopulateIntermediateTable.html)  **
  - **Description:** Grants permission to populate an intermediate table by executing its stored analysis
  - **Resource types (\*required):** [configuredtableassociation](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [idmappingtable](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PreviewPrivacyImpact](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PreviewPrivacyImpact.html)  **
  - **Description:** Grants permission to preview privacy budget template settings
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartAnalysisLogExport](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_StartAnalysisLogExport.html)  **
  - **Description:** Grants permission to start an analysis log export
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartProtectedJob](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_StartProtectedJob.html)  **
  - **Description:** Grants permission to start protected jobs
  - **Resource types (\*required):** [analysistemplate](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredtableassociation](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [intermediatetable](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartProtectedQuery](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_StartProtectedQuery.html)  **
  - **Description:** Grants permission to start protected queries
  - **Resource types (\*required):** [analysistemplate](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configuredtableassociation](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [idmappingtable](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [intermediatetable](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [analysistemplate](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [collaboration](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [configuredaudiencemodelassociation](#list_cleanrooms-resource-configuredaudiencemodelassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [configuredtable](#list_cleanrooms-resource-configuredtable) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [configuredtableassociation](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [idmappingtable](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [idnamespaceassociation](#list_cleanrooms-resource-idnamespaceassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [intermediatetable](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [privacybudgettemplate](#list_cleanrooms-resource-privacybudgettemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanrooms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [analysistemplate](#list_cleanrooms-resource-analysistemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [collaboration](#list_cleanrooms-resource-collaboration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [configuredaudiencemodelassociation](#list_cleanrooms-resource-configuredaudiencemodelassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [configuredtable](#list_cleanrooms-resource-configuredtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [configuredtableassociation](#list_cleanrooms-resource-configuredtableassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [idmappingtable](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [idnamespaceassociation](#list_cleanrooms-resource-idnamespaceassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [intermediatetable](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [membership](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Resource types (\*required):** [privacybudgettemplate](#list_cleanrooms-resource-privacybudgettemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanrooms-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAnalysisTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateAnalysisTemplate.html)  **
  - **Description:** Grants permission to update details of the analysis template
  - **Resource types (\*required):** [analysistemplate\*](#list_cleanrooms-resource-analysistemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCollaboration](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateCollaboration.html)  **
  - **Description:** Grants permission to update details of the collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCollaborationChangeRequest](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateCollaborationChangeRequest.html)  **
  - **Description:** Grants permission to update a change request in a collaboration
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguredAudienceModelAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredAudienceModelAssociation.html)  **
  - **Description:** Grants permission to update a configured audience model association
  - **Resource types (\*required):** [configuredaudiencemodelassociation\*](#list_cleanrooms-resource-configuredaudiencemodelassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguredTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTable.html)  **
  - **Description:** Grants permission to update an existing configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguredTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTableAnalysisRule.html)  **
  - **Description:** Grants permission to update analysis rules for a configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguredTableAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTableAssociation.html)  **
  - **Description:** Grants permission to update a configured table association
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguredTableAssociationAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTableAssociationAnalysisRule.html)  **
  - **Description:** Grants permission to update analysis rules for a configured table association
  - **Resource types (\*required):** [configuredtableassociation\*](#list_cleanrooms-resource-configuredtableassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIdMappingTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateIdMappingTable.html)  **
  - **Description:** Grants permission to update an id mapping table
  - **Resource types (\*required):** [idmappingtable\*](#list_cleanrooms-resource-idmappingtable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIdNamespaceAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateIdNamespaceAssociation.html)  **
  - **Description:** Grants permission to update a entity resolution input association
  - **Resource types (\*required):** [idnamespaceassociation\*](#list_cleanrooms-resource-idnamespaceassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntermediateTable](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateIntermediateTable.html)  **
  - **Description:** Grants permission to update an intermediate table
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntermediateTableAnalysisRule](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateIntermediateTableAnalysisRule.html)  **
  - **Description:** Grants permission to update an analysis rule for an intermediate table
  - **Resource types (\*required):** [intermediatetable\*](#list_cleanrooms-resource-intermediatetable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMembership](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateMembership.html)  **
  - **Description:** Grants permission to update details of a membership
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePrivacyBudgetTemplate](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdatePrivacyBudgetTemplate.html)  **
  - **Description:** Grants permission to update details of the privacy budget template
  - **Resource types (\*required):** [privacybudgettemplate\*](#list_cleanrooms-resource-privacybudgettemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProtectedJob](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateProtectedJob.html)  **
  - **Description:** Grants permission to update protected jobs
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProtectedQuery](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateProtectedQuery.html)  **
  - **Description:** Grants permission to update protected queries
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Clean Rooms
<a name="list_cleanrooms-permission-only-actions"></a>

The following actions are defined by AWS Clean Rooms but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [PassCollaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-behaviors-byom.html#ml-behaviors-byom-membership-collaboration-access)  **
  - **Description:** Grants permission to access a collaboration in the context of Clean Rooms ML custom models
  - **Resource types (\*required):** [collaboration\*](#list_cleanrooms-resource-collaboration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PassMembership](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-behaviors-byom.html#ml-behaviors-byom-membership-collaboration-access)  **
  - **Description:** Grants permission to access a membership in the context of Clean Rooms ML custom models
  - **Resource types (\*required):** [membership\*](#list_cleanrooms-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [UpdateConfiguredTableAllowedColumns](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTable.html)  **
  - **Description:** Grants permission to update the allowed columns of an existing configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguredTableReference](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTable.html)  **
  - **Description:** Grants permission to update the table reference of an existing configured table
  - **Resource types (\*required):** [configuredtable\*](#list_cleanrooms-resource-configuredtable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Clean Rooms
<a name="list_cleanrooms-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [analysistemplate](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:membership/${MembershipId}/analysistemplate/${AnalysisTemplateId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:collaboration/${CollaborationId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [configuredaudiencemodelassociation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:membership/${MembershipId}/configuredaudiencemodelassociation/${ConfiguredAudienceModelAssociationId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [configuredtable](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:configuredtable/${ConfiguredTableId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [configuredtableassociation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:membership/${MembershipId}/configuredtableassociation/${ConfiguredTableAssociationId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [idmappingtable](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:membership/${MembershipId}/idmappingtable/${IdMappingTableId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [idnamespaceassociation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:membership/${MembershipId}/idnamespaceassociation/${IdNamespaceAssociationId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [intermediatetable](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:membership/${MembershipId}/intermediatetable/${IntermediateTableId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [membership](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:membership/${MembershipId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 
|  [privacybudgettemplate](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)  | arn:${Partition}:cleanrooms:${Region}:${Account}:membership/${MembershipId}/privacybudgettemplate/${PrivacyBudgetTemplateId} | [aws:ResourceTag/${TagKey}](#list_cleanrooms-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Clean Rooms
<a name="list_cleanrooms-policy-keys"></a>

AWS Clean Rooms defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 