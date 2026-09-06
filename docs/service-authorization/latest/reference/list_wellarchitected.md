

# Actions, resources, and condition keys for AWS Well-Architected Tool
<a name="list_wellarchitected"></a>

AWS Well-Architected Tool (service prefix: `wellarchitected`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/wellarchitected/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/wellarchitected/latest/userguide/iam-auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/wellarchitected/wellarchitected.json) for this service.

**Topics**
+ [API operations defined by AWS Well-Architected Tool](#list_wellarchitected-operations)
+ [Actions defined by AWS Well-Architected Tool](#list_wellarchitected-actions-as-permissions)
+ [Permission-only actions for AWS Well-Architected Tool](#list_wellarchitected-permission-only-actions)
+ [Resource types defined by AWS Well-Architected Tool](#list_wellarchitected-resources-for-iam-policies)
+ [Condition keys for AWS Well-Architected Tool](#list_wellarchitected-policy-keys)

## API operations defined by AWS Well-Architected Tool
<a name="list_wellarchitected-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_wellarchitected-actions-as-permissions).




- **   AssociateLenses  **
  - **IAM action:**  [wellarchitected:AssociateLenses](#list_wellarchitected-action-AssociateLenses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateProfiles  **
  - **IAM action:**  [wellarchitected:AssociateProfiles](#list_wellarchitected-action-AssociateProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgentContext  **
  - **IAM action:**  [wellarchitected:CreateAgentContext](#list_wellarchitected-action-CreateAgentContext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgentGoal  **
  - **IAM action:**  [wellarchitected:CreateAgentGoal](#list_wellarchitected-action-CreateAgentGoal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgentProfile  **
  - **IAM action:**  [wellarchitected:CreateAgentProfile](#list_wellarchitected-action-CreateAgentProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wellarchitected:TagResource](#list_wellarchitected-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** wellarchitected.amazonaws.com / **Access level:** Write

- **   CreateLensShare  **
  - **IAM action:**  [wellarchitected:CreateLensShare](#list_wellarchitected-action-CreateLensShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLensVersion  **
  - **IAM action:**  [wellarchitected:CreateLensVersion](#list_wellarchitected-action-CreateLensVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMilestone  **
  - **IAM action:**  [wellarchitected:CreateMilestone](#list_wellarchitected-action-CreateMilestone) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProfile  **
  - **IAM action:**  [wellarchitected:CreateProfile](#list_wellarchitected-action-CreateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wellarchitected:TagResource](#list_wellarchitected-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProfileShare  **
  - **IAM action:**  [wellarchitected:CreateProfileShare](#list_wellarchitected-action-CreateProfileShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateReviewTemplate  **
  - **IAM action:**  [wellarchitected:CreateReviewTemplate](#list_wellarchitected-action-CreateReviewTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wellarchitected:TagResource](#list_wellarchitected-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTemplateShare  **
  - **IAM action:**  [wellarchitected:CreateTemplateShare](#list_wellarchitected-action-CreateTemplateShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkload  **
  - **IAM action:**  [wellarchitected:CreateWorkload](#list_wellarchitected-action-CreateWorkload)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wellarchitected:GetReviewTemplate](#list_wellarchitected-action-GetReviewTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [wellarchitected:GetReviewTemplateAnswer](#list_wellarchitected-action-GetReviewTemplateAnswer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [wellarchitected:GetReviewTemplateLensReview](#list_wellarchitected-action-GetReviewTemplateLensReview)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [wellarchitected:ListReviewTemplateAnswers](#list_wellarchitected-action-ListReviewTemplateAnswers)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [wellarchitected:TagResource](#list_wellarchitected-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWorkloadShare  **
  - **IAM action:**  [wellarchitected:CreateWorkloadShare](#list_wellarchitected-action-CreateWorkloadShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgentContext  **
  - **IAM action:**  [wellarchitected:DeleteAgentContext](#list_wellarchitected-action-DeleteAgentContext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgentGoal  **
  - **IAM action:**  [wellarchitected:DeleteAgentGoal](#list_wellarchitected-action-DeleteAgentGoal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgentProfile  **
  - **IAM action:**  [wellarchitected:DeleteAgentProfile](#list_wellarchitected-action-DeleteAgentProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLens  **
  - **IAM action:**  [wellarchitected:DeleteLens](#list_wellarchitected-action-DeleteLens) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLensShare  **
  - **IAM action:**  [wellarchitected:DeleteLensShare](#list_wellarchitected-action-DeleteLensShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfile  **
  - **IAM action:**  [wellarchitected:DeleteProfile](#list_wellarchitected-action-DeleteProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfileShare  **
  - **IAM action:**  [wellarchitected:DeleteProfileShare](#list_wellarchitected-action-DeleteProfileShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReviewTemplate  **
  - **IAM action:**  [wellarchitected:DeleteReviewTemplate](#list_wellarchitected-action-DeleteReviewTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplateShare  **
  - **IAM action:**  [wellarchitected:DeleteTemplateShare](#list_wellarchitected-action-DeleteTemplateShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkload  **
  - **IAM action:**  [wellarchitected:DeleteWorkload](#list_wellarchitected-action-DeleteWorkload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkloadShare  **
  - **IAM action:**  [wellarchitected:DeleteWorkloadShare](#list_wellarchitected-action-DeleteWorkloadShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateLenses  **
  - **IAM action:**  [wellarchitected:DisassociateLenses](#list_wellarchitected-action-DisassociateLenses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateProfiles  **
  - **IAM action:**  [wellarchitected:DisassociateProfiles](#list_wellarchitected-action-DisassociateProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportLens  **
  - **IAM action:**  [wellarchitected:ExportLens](#list_wellarchitected-action-ExportLens) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentContext  **
  - **IAM action:**  [wellarchitected:GetAgentContext](#list_wellarchitected-action-GetAgentContext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentGoal  **
  - **IAM action:**  [wellarchitected:GetAgentGoal](#list_wellarchitected-action-GetAgentGoal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentProfile  **
  - **IAM action:**  [wellarchitected:GetAgentProfile](#list_wellarchitected-action-GetAgentProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentRecommendation  **
  - **IAM action:**  [wellarchitected:GetAgentRecommendation](#list_wellarchitected-action-GetAgentRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentRecommendationGeneration  **
  - **IAM action:**  [wellarchitected:GetAgentRecommendationGeneration](#list_wellarchitected-action-GetAgentRecommendationGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnswer  **
  - **IAM action:**  [wellarchitected:GetAnswer](#list_wellarchitected-action-GetAnswer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConsolidatedReport  **
  - **IAM action:**  [wellarchitected:GetConsolidatedReport](#list_wellarchitected-action-GetConsolidatedReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGlobalSettings  **
  - **IAM action:**  [wellarchitected:GetGlobalSettings](#list_wellarchitected-action-GetGlobalSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLens  **
  - **IAM action:**  [wellarchitected:GetLens](#list_wellarchitected-action-GetLens) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLensReview  **
  - **IAM action:**  [wellarchitected:GetLensReview](#list_wellarchitected-action-GetLensReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLensReviewReport  **
  - **IAM action:**  [wellarchitected:GetLensReviewReport](#list_wellarchitected-action-GetLensReviewReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLensVersionDifference  **
  - **IAM action:**  [wellarchitected:GetLensVersionDifference](#list_wellarchitected-action-GetLensVersionDifference) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMilestone  **
  - **IAM action:**  [wellarchitected:GetMilestone](#list_wellarchitected-action-GetMilestone) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfile  **
  - **IAM action:**  [wellarchitected:GetProfile](#list_wellarchitected-action-GetProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileTemplate  **
  - **IAM action:**  [wellarchitected:GetProfileTemplate](#list_wellarchitected-action-GetProfileTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReviewTemplate  **
  - **IAM action:**  [wellarchitected:GetReviewTemplate](#list_wellarchitected-action-GetReviewTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReviewTemplateAnswer  **
  - **IAM action:**  [wellarchitected:GetReviewTemplateAnswer](#list_wellarchitected-action-GetReviewTemplateAnswer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReviewTemplateLensReview  **
  - **IAM action:**  [wellarchitected:GetReviewTemplateLensReview](#list_wellarchitected-action-GetReviewTemplateLensReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkload  **
  - **IAM action:**  [wellarchitected:GetWorkload](#list_wellarchitected-action-GetWorkload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportLens  **
  - **IAM action:**  [wellarchitected:ImportLens](#list_wellarchitected-action-ImportLens)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wellarchitected:TagResource](#list_wellarchitected-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListAgentContexts  **
  - **IAM action:**  [wellarchitected:ListAgentContexts](#list_wellarchitected-action-ListAgentContexts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgentGoals  **
  - **IAM action:**  [wellarchitected:ListAgentGoals](#list_wellarchitected-action-ListAgentGoals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgentProfiles  **
  - **IAM action:**  [wellarchitected:ListAgentProfiles](#list_wellarchitected-action-ListAgentProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgentRecommendationGenerations  **
  - **IAM action:**  [wellarchitected:ListAgentRecommendationGenerations](#list_wellarchitected-action-ListAgentRecommendationGenerations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgentRecommendationItems  **
  - **IAM action:**  [wellarchitected:ListAgentRecommendationItems](#list_wellarchitected-action-ListAgentRecommendationItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgentRecommendations  **
  - **IAM action:**  [wellarchitected:ListAgentRecommendations](#list_wellarchitected-action-ListAgentRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnswers  **
  - **IAM action:**  [wellarchitected:ListAnswers](#list_wellarchitected-action-ListAnswers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCheckDetails  **
  - **IAM action:**  [wellarchitected:ListCheckDetails](#list_wellarchitected-action-ListCheckDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCheckSummaries  **
  - **IAM action:**  [wellarchitected:ListCheckSummaries](#list_wellarchitected-action-ListCheckSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLensReviewImprovements  **
  - **IAM action:**  [wellarchitected:ListLensReviewImprovements](#list_wellarchitected-action-ListLensReviewImprovements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLensReviews  **
  - **IAM action:**  [wellarchitected:ListLensReviews](#list_wellarchitected-action-ListLensReviews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLensShares  **
  - **IAM action:**  [wellarchitected:ListLensShares](#list_wellarchitected-action-ListLensShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLenses  **
  - **IAM action:**  [wellarchitected:ListLenses](#list_wellarchitected-action-ListLenses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMilestones  **
  - **IAM action:**  [wellarchitected:ListMilestones](#list_wellarchitected-action-ListMilestones) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotifications  **
  - **IAM action:**  [wellarchitected:ListNotifications](#list_wellarchitected-action-ListNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileNotifications  **
  - **IAM action:**  [wellarchitected:ListProfileNotifications](#list_wellarchitected-action-ListProfileNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileShares  **
  - **IAM action:**  [wellarchitected:ListProfileShares](#list_wellarchitected-action-ListProfileShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfiles  **
  - **IAM action:**  [wellarchitected:ListProfiles](#list_wellarchitected-action-ListProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReviewTemplateAnswers  **
  - **IAM action:**  [wellarchitected:ListReviewTemplateAnswers](#list_wellarchitected-action-ListReviewTemplateAnswers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReviewTemplates  **
  - **IAM action:**  [wellarchitected:ListReviewTemplates](#list_wellarchitected-action-ListReviewTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListShareInvitations  **
  - **IAM action:**  [wellarchitected:ListShareInvitations](#list_wellarchitected-action-ListShareInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [wellarchitected:ListTagsForResource](#list_wellarchitected-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTemplateShares  **
  - **IAM action:**  [wellarchitected:ListTemplateShares](#list_wellarchitected-action-ListTemplateShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkloadShares  **
  - **IAM action:**  [wellarchitected:ListWorkloadShares](#list_wellarchitected-action-ListWorkloadShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkloads  **
  - **IAM action:**  [wellarchitected:ListWorkloads](#list_wellarchitected-action-ListWorkloads) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAgentRecommendationFeedback  **
  - **IAM action:**  [wellarchitected:PutAgentRecommendationFeedback](#list_wellarchitected-action-PutAgentRecommendationFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAgentRecommendationGeneration  **
  - **IAM action:**  [wellarchitected:StartAgentRecommendationGeneration](#list_wellarchitected-action-StartAgentRecommendationGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [wellarchitected:TagResource](#list_wellarchitected-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [wellarchitected:UntagResource](#list_wellarchitected-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAgentContext  **
  - **IAM action:**  [wellarchitected:UpdateAgentContext](#list_wellarchitected-action-UpdateAgentContext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAgentGoal  **
  - **IAM action:**  [wellarchitected:UpdateAgentGoal](#list_wellarchitected-action-UpdateAgentGoal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAgentProfile  **
  - **IAM action:**  [wellarchitected:UpdateAgentProfile](#list_wellarchitected-action-UpdateAgentProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** wellarchitected.amazonaws.com / **Access level:** Write

- **   UpdateAgentRecommendationStatus  **
  - **IAM action:**  [wellarchitected:UpdateAgentRecommendationStatus](#list_wellarchitected-action-UpdateAgentRecommendationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAnswer  **
  - **IAM action:**  [wellarchitected:UpdateAnswer](#list_wellarchitected-action-UpdateAnswer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlobalSettings  **
  - **IAM action:**  [wellarchitected:UpdateGlobalSettings](#list_wellarchitected-action-UpdateGlobalSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIntegration  **
  - **IAM action:**  [wellarchitected:UpdateIntegration](#list_wellarchitected-action-UpdateIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLensReview  **
  - **IAM action:**  [wellarchitected:UpdateLensReview](#list_wellarchitected-action-UpdateLensReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProfile  **
  - **IAM action:**  [wellarchitected:UpdateProfile](#list_wellarchitected-action-UpdateProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReviewTemplate  **
  - **IAM action:**  [wellarchitected:UpdateReviewTemplate](#list_wellarchitected-action-UpdateReviewTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReviewTemplateAnswer  **
  - **IAM action:**  [wellarchitected:UpdateReviewTemplateAnswer](#list_wellarchitected-action-UpdateReviewTemplateAnswer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReviewTemplateLensReview  **
  - **IAM action:**  [wellarchitected:UpdateReviewTemplateLensReview](#list_wellarchitected-action-UpdateReviewTemplateLensReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateShareInvitation  **
  - **IAM action:**  [wellarchitected:UpdateShareInvitation](#list_wellarchitected-action-UpdateShareInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkload  **
  - **IAM action:**  [wellarchitected:UpdateWorkload](#list_wellarchitected-action-UpdateWorkload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkloadShare  **
  - **IAM action:**  [wellarchitected:UpdateWorkloadShare](#list_wellarchitected-action-UpdateWorkloadShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpgradeLensReview  **
  - **IAM action:**  [wellarchitected:UpgradeLensReview](#list_wellarchitected-action-UpgradeLensReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpgradeProfileVersion  **
  - **IAM action:**  [wellarchitected:UpgradeProfileVersion](#list_wellarchitected-action-UpgradeProfileVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpgradeReviewTemplateLensReview  **
  - **IAM action:**  [wellarchitected:UpgradeReviewTemplateLensReview](#list_wellarchitected-action-UpgradeReviewTemplateLensReview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Well-Architected Tool
<a name="list_wellarchitected-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AssociateLenses.html)  **
  - **Description:** Grants permission to associate a lens to the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AssociateProfiles.html)  **
  - **Description:** Grants permission to associate a profile to the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentContext.html)  **
  - **Description:** Grants permission to create a context associated with a profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentGoal.html)  **
  - **Description:** Grants permission to create a goal associated with a profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentProfile.html)  **
  - **Description:** Grants permission to create an agent profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLensShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateLensShare.html)  **
  - **Description:** Grants permission to an owner of a lens to share with other AWS accounts and IAM users
  - **Resource types (\*required):** [lens\*](#list_wellarchitected-resource-lens)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLensVersion](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateLensVersion.html)  **
  - **Description:** Grants permission to create a new lens version
  - **Resource types (\*required):** [lens\*](#list_wellarchitected-resource-lens)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMilestone](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateMilestone.html)  **
  - **Description:** Grants permission to create a new milestone for the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfile.html)  **
  - **Description:** Grants permission to create a new profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProfileShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfileShare.html)  **
  - **Description:** Grants permission to an owner of a profile to share with other AWS accounts and IAM users
  - **Resource types (\*required):** [profile\*](#list_wellarchitected-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateReviewTemplate.html)  **
  - **Description:** Grants permission to create a new review template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTemplateShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateTemplateShare.html)  **
  - **Description:** Grants permission to an owner of a review template to share with other AWS accounts and IAM users
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateWorkload.html)  **
  - **Description:** Grants permission to create a new workload
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)<br />[wellarchitected:JiraProjectKey](#list_wellarchitected-wellarchitected_JiraProjectKey)
  - **Access level:** Write

- **   [CreateWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateWorkloadShare.html)  **
  - **Description:** Grants permission to share a workload with another account
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentContext.html)  **
  - **Description:** Grants permission to delete a context associated with a profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentGoal.html)  **
  - **Description:** Grants permission to delete a goal associated with a profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentProfile.html)  **
  - **Description:** Grants permission to delete an agent profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteLens.html)  **
  - **Description:** Grants permission to delete a lens
  - **Resource types (\*required):** [lens\*](#list_wellarchitected-resource-lens)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLensShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteLensShare.html)  **
  - **Description:** Grants permission to delete an existing lens share
  - **Resource types (\*required):** [lens\*](#list_wellarchitected-resource-lens)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteProfile.html)  **
  - **Description:** Grants permission to delete a profile
  - **Resource types (\*required):** [profile\*](#list_wellarchitected-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfileShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteProfileShare.html)  **
  - **Description:** Grants permission to delete an existing profile share
  - **Resource types (\*required):** [profile\*](#list_wellarchitected-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteReviewTemplate.html)  **
  - **Description:** Grants permission to delete an existing review template
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTemplateShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteTemplateShare.html)  **
  - **Description:** Grants permission to delete an existing review template share
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteWorkload.html)  **
  - **Description:** Grants permission to delete an existing workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteWorkloadShare.html)  **
  - **Description:** Grants permission to delete an existing workload share
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DisassociateLenses.html)  **
  - **Description:** Grants permission to disassociate a lens from the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DisassociateProfiles.html)  **
  - **Description:** Grants permission to disassociate a profile from the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ExportLens.html)  **
  - **Description:** Grants permission to export an existing lens
  - **Resource types (\*required):** [lens\*](#list_wellarchitected-resource-lens)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentContext.html)  **
  - **Description:** Grants permission to get context associated with a profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentGoal.html)  **
  - **Description:** Grants permission to get goal associated with a profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentProfile.html)  **
  - **Description:** Grants permission to get agent profile by profile arn
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentRecommendation](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentRecommendation.html)  **
  - **Description:** Grants permission to get a recommendation by recommendation ARN
  - **Resource types (\*required):** [agent-recommendation\*](#list_wellarchitected-resource-agent-recommendation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentRecommendationGeneration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentRecommendationGeneration.html)  **
  - **Description:** Grants permission to get a recommendation generation
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAnswer.html)  **
  - **Description:** Grants permission to retrieve the specified answer from the specified lens review
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConsolidatedReport](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetConsolidatedReport.html)  **
  - **Description:** Grants permission to get consolidated report metrics or to generate the consolidated report PDF in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGlobalSettings](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetGlobalSettings.html)  **
  - **Description:** Grants permission to get all settings for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteLensShare.html)  **
  - **Description:** Grants permission to get an existing lens
  - **Resource types (\*required):** [lens\*](#list_wellarchitected-resource-lens)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensReview.html)  **
  - **Description:** Grants permission to retrieve the specified lens review of the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLensReviewReport](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensReviewReport.html)  **
  - **Description:** Grants permission to retrieve the report for the specified lens review
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLensVersionDifference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensVersionDifference.html)  **
  - **Description:** Grants permission to get the difference between the specified lens version and latest available lens version
  - **Resource types (\*required):** [lens\*](#list_wellarchitected-resource-lens)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMilestone](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetMilestone.html)  **
  - **Description:** Grants permission to retrieve the specified milestone of the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetProfile.html)  **
  - **Description:** Grants permission to retrieve the specified profile
  - **Resource types (\*required):** [profile\*](#list_wellarchitected-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfileTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetProfileTemplate.html)  **
  - **Description:** Grants permission to retrieve the specified profile template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplate.html)  **
  - **Description:** Grants permission to retrieve the specified review template
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReviewTemplateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplateAnswer.html)  **
  - **Description:** Grants permission to retrieve the specified answer from the specified review template lens review
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplateLensReview.html)  **
  - **Description:** Grants permission to retrieve the specified lens review of the specified review template
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetWorkload.html)  **
  - **Description:** Grants permission to retrieve the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ImportLens.html)  **
  - **Description:** Grants permission to import a new lens
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Access level:** Write

- **   [ListAgentContexts](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentContexts.html)  **
  - **Description:** Grants permission to list contexts associated with a profile by filters on the fields
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAgentGoals](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentGoals.html)  **
  - **Description:** Grants permission to list goals associated with a profile by filters on the fields
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAgentProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentProfiles.html)  **
  - **Description:** Grants permission to list agent profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAgentRecommendationGenerations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendationGenerations.html)  **
  - **Description:** Grants permission to list recommendation generations
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAgentRecommendationItems](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendationItems.html)  **
  - **Description:** Grants permission to list recommendation items associated with a recommendation
  - **Resource types (\*required):** [agent-recommendation\*](#list_wellarchitected-resource-agent-recommendation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAgentRecommendations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendations.html)  **
  - **Description:** Grants permission to list recommendations by profile ARN
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAnswers](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAnswers.html)  **
  - **Description:** Grants permission to list the answers from the specified lens review
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCheckDetails](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListCheckDetails.html)  **
  - **Description:** Grants permission to list the check-details for the workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCheckSummaries](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListCheckSummaries.html)  **
  - **Description:** Grants permission to list the check-summaries for the workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLensReviewImprovements](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensReviewImprovements.html)  **
  - **Description:** Grants permission to list the improvements of the specified lens review
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLensReviews](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensReviews.html)  **
  - **Description:** Grants permission to list the lens reviews of the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLensShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensShares.html)  **
  - **Description:** Grants permission to list all shares created for a lens
  - **Resource types (\*required):** [lens\*](#list_wellarchitected-resource-lens)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLenses.html)  **
  - **Description:** Grants permission to list the lenses available to this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMilestones](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListMilestones.html)  **
  - **Description:** Grants permission to list the milestones of the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNotifications](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListNotifications.html)  **
  - **Description:** Grants permission to list notifications related to the account or specified resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProfileNotifications](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfileNotifications.html)  **
  - **Description:** Grants permission to list profile notifications related to specified resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProfileShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfileShares.html)  **
  - **Description:** Grants permission to list all shares created for a profile
  - **Resource types (\*required):** [profile\*](#list_wellarchitected-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfiles.html)  **
  - **Description:** Grants permission to list the profiles available to this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReviewTemplateAnswers](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListReviewTemplateAnswers.html)  **
  - **Description:** Grants permission to list the answers from the specified review template lens review
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReviewTemplates](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListReviewTemplates.html)  **
  - **Description:** Grants permission to list the review templates available to this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListShareInvitations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListShareInvitations.html)  **
  - **Description:** Grants permission to list the workload share invitations of the specified account or user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a Well-Architected resource
  - **Resource types (\*required):** [agent-profile](#list_wellarchitected-resource-agent-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [agent-recommendation](#list_wellarchitected-resource-agent-recommendation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [lens](#list_wellarchitected-resource-lens) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [profile](#list_wellarchitected-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [review-template](#list_wellarchitected-resource-review-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload](#list_wellarchitected-resource-workload) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTemplateShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListTemplateShares.html)  **
  - **Description:** Grants permission to list all shares created for a review template
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkloadShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListWorkloadShares.html)  **
  - **Description:** Grants permission to list the workload shares of the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkloads](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListWorkloads.html)  **
  - **Description:** Grants permission to list the workloads in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutAgentRecommendationFeedback](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PutAgentRecommendationFeedback.html)  **
  - **Description:** Grants permission to put feedback on a recommendation
  - **Resource types (\*required):** [agent-recommendation\*](#list_wellarchitected-resource-agent-recommendation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAgentRecommendationGeneration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_StartAgentRecommendationGeneration.html)  **
  - **Description:** Grants permission to start a recommendation generation process
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a Well-Architected resource
  - **Resource types (\*required):** [agent-profile](#list_wellarchitected-resource-agent-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [agent-recommendation](#list_wellarchitected-resource-agent-recommendation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [lens](#list_wellarchitected-resource-lens) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_wellarchitected-resource-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [review-template](#list_wellarchitected-resource-review-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [workload](#list_wellarchitected-resource-workload) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_wellarchitected-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a Well-Architected resource
  - **Resource types (\*required):** [agent-profile](#list_wellarchitected-resource-agent-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [agent-recommendation](#list_wellarchitected-resource-agent-recommendation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [lens](#list_wellarchitected-resource-lens) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_wellarchitected-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [review-template](#list_wellarchitected-resource-review-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Resource types (\*required):** [workload](#list_wellarchitected-resource-workload) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wellarchitected-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentContext.html)  **
  - **Description:** Grants permission to update a context associated with a profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentGoal.html)  **
  - **Description:** Grants permission to update a goal associated with a profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentProfile.html)  **
  - **Description:** Grants permission to update an agent profile
  - **Resource types (\*required):** [agent-profile\*](#list_wellarchitected-resource-agent-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentRecommendationStatus](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentRecommendationStatus.html)  **
  - **Description:** Grants permission to update the status of a recommendation
  - **Resource types (\*required):** [agent-recommendation\*](#list_wellarchitected-resource-agent-recommendation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAnswer.html)  **
  - **Description:** Grants permission to update properties of the specified answer
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGlobalSettings](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateGlobalSettings.html)  **
  - **Description:** Grants permission to manage all settings for the account
  - **Resource types (\*required):** 
  - **Condition keys:** [wellarchitected:JiraProjectKey](#list_wellarchitected-wellarchitected_JiraProjectKey)
  - **Access level:** Write

- **   [UpdateIntegration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateIntegration.html)  **
  - **Description:** Grants permission to update properties of the integration
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateLensReview.html)  **
  - **Description:** Grants permission to update properties of the specified lens review
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateProfile.html)  **
  - **Description:** Grants permission to update properties of the specified profile
  - **Resource types (\*required):** [profile\*](#list_wellarchitected-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplate.html)  **
  - **Description:** Grants permission to update properties of the specified review template
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReviewTemplateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplateAnswer.html)  **
  - **Description:** Grants permission to update properties of the specified review template answer
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplateLensReview.html)  **
  - **Description:** Grants permission to update properties of the specified review template lens review
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateShareInvitation](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateShareInvitation.html)  **
  - **Description:** Grants permission to update status of the specified workload share invitation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateWorkload.html)  **
  - **Description:** Grants permission to update properties of the specified workload
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)<br />[wellarchitected:JiraProjectKey](#list_wellarchitected-wellarchitected_JiraProjectKey)
  - **Access level:** Write

- **   [UpdateWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateWorkloadShare.html)  **
  - **Description:** Grants permission to update properties of the specified workload share
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpgradeLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeLensReview.html)  **
  - **Description:** Grants permission to upgrade the specified lens review to use the latest version of the associated lens
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpgradeProfileVersion](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeProfileVersion.html)  **
  - **Description:** Grants permission to upgrade the specified workload to use the latest version of the associated profile
  - **Resource types (\*required):** [profile\*](#list_wellarchitected-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload\*](#list_wellarchitected-resource-workload) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpgradeReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeReviewTemplateLensReview.html)  **
  - **Description:** Grants permission to upgrade the specified lens review of the specified review template
  - **Resource types (\*required):** [review-template\*](#list_wellarchitected-resource-review-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Well-Architected Tool
<a name="list_wellarchitected-permission-only-actions"></a>

The following actions are defined by AWS Well-Architected Tool but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [ConfigureIntegration](https://docs.aws.amazon.com/wellarchitected/latest/userguide/setting-up-jira.html)  | Grants permission to configure the integration |  |   | Write | 

## Resource types defined by AWS Well-Architected Tool
<a name="list_wellarchitected-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [agent-profile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AgentProfileSummary.html)  | arn:${Partition}:wellarchitected:${Region}:${Account}:agent-profile/${ProfileName} | [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_) | 
|  [agent-recommendation](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AgentRecommendationSummary.html)  | arn:${Partition}:wellarchitected:${Region}:${Account}:agent-recommendation/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_) | 
|  [lens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Lens.html)  | arn:${Partition}:wellarchitected:${Region}:${Account}:lens/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_) | 
|  [profile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Profile.html)  | arn:${Partition}:wellarchitected:${Region}:${Account}:profile/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_) | 
|  [review-template](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ReviewTemplate.html)  | arn:${Partition}:wellarchitected:${Region}:${Account}:review-template/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_) | 
|  [workload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Workload.html)  | arn:${Partition}:wellarchitected:${Region}:${Account}:workload/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_wellarchitected-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Well-Architected Tool
<a name="list_wellarchitected-policy-keys"></a>

AWS Well-Architected Tool defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys in the request | ArrayOfString | 
|   [wellarchitected:JiraProjectKey](https://docs.aws.amazon.com/wellarchitected/latest/userguide/security_iam_id-based-policy-examples.html)  | Filters access by project key | String | 