

AWS Well-Architected Agent is in preview release and is subject to change.

# API actions
<a name="wa-api-actions"></a>

The following API actions are available for AWS Well-Architected services. All actions use the `wellarchitected` service namespace. For complete API reference documentation, see the [AWS Well-Architected API Reference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/Welcome.html).

## AWS Well-Architected Agent actions
<a name="agent-api-agent-actions"></a>

The following actions are for AWS Well-Architected Agent.

### Profiles
<a name="agent-api-profiles"></a>
+ [CreateAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentProfile.html)
+ [DeleteAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentProfile.html)
+ [GetAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentProfile.html)
+ [ListAgentProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentProfiles.html)
+ [UpdateAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentProfile.html)

### Goals
<a name="agent-api-goals"></a>
+ [CreateAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentGoal.html)
+ [DeleteAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentGoal.html)
+ [GetAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentGoal.html)
+ [ListAgentGoals](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentGoals.html)
+ [UpdateAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentGoal.html)

### Application context
<a name="agent-api-context"></a>
+ [CreateAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentContext.html)
+ [DeleteAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentContext.html)
+ [GetAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentContext.html)
+ [ListAgentContexts](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentContexts.html)
+ [UpdateAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentContext.html)

### Recommendations
<a name="agent-api-recommendations"></a>
+ [GetAgentRecommendation](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentRecommendation.html)
+ [ListAgentRecommendations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendations.html)
+ [ListAgentRecommendationItems](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendationItems.html)
+ [UpdateAgentRecommendationStatus](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentRecommendationStatus.html)
+ [PutAgentRecommendationFeedback](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PutAgentRecommendationFeedback.html)

### Recommendation generation
<a name="agent-api-recommendation-generation"></a>
+ [StartAgentRecommendationGeneration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_StartAgentRecommendationGeneration.html)
+ [GetAgentRecommendationGeneration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentRecommendationGeneration.html)
+ [ListAgentRecommendationGenerations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendationGenerations.html)

## AWS Well-Architected Tool actions
<a name="agent-api-tool-actions"></a>

The following actions are for the AWS Well-Architected Tool.

### Workloads
<a name="wa-tool-api-workloads"></a>
+ [CreateWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateWorkload.html)
+ [DeleteWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteWorkload.html)
+ [GetWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetWorkload.html)
+ [ListWorkloads](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListWorkloads.html)
+ [UpdateWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateWorkload.html)

### Workload sharing
<a name="wa-tool-api-workload-sharing"></a>
+ [CreateWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateWorkloadShare.html)
+ [DeleteWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteWorkloadShare.html)
+ [ListWorkloadShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListWorkloadShares.html)
+ [UpdateWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateWorkloadShare.html)
+ [ListShareInvitations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListShareInvitations.html)
+ [UpdateShareInvitation](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateShareInvitation.html)

### Lenses
<a name="wa-tool-api-lenses"></a>
+ [AssociateLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AssociateLenses.html)
+ [CreateLensShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateLensShare.html)
+ [CreateLensVersion](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateLensVersion.html)
+ [DeleteLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteLens.html)
+ [DeleteLensShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteLensShare.html)
+ [DisassociateLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DisassociateLenses.html)
+ [ExportLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ExportLens.html)
+ [GetLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLens.html)
+ [GetLensVersionDifference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensVersionDifference.html)
+ [ImportLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ImportLens.html)
+ [ListLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLenses.html)
+ [ListLensShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensShares.html)
+ [UpgradeLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeLensReview.html)

### Lens reviews
<a name="wa-tool-api-lens-reviews"></a>
+ [GetAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAnswer.html)
+ [GetLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensReview.html)
+ [GetLensReviewReport](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensReviewReport.html)
+ [ListAnswers](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAnswers.html)
+ [ListLensReviewImprovements](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensReviewImprovements.html)
+ [ListLensReviews](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensReviews.html)
+ [UpdateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAnswer.html)
+ [UpdateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateLensReview.html)

### Milestones
<a name="wa-tool-api-milestones"></a>
+ [CreateMilestone](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateMilestone.html)
+ [GetMilestone](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetMilestone.html)
+ [ListMilestones](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListMilestones.html)

### Profiles
<a name="wa-tool-api-profiles"></a>
+ [AssociateProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AssociateProfiles.html)
+ [CreateProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfile.html)
+ [CreateProfileShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfileShare.html)
+ [DeleteProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteProfile.html)
+ [DeleteProfileShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteProfileShare.html)
+ [DisassociateProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DisassociateProfiles.html)
+ [GetProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetProfile.html)
+ [GetProfileTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetProfileTemplate.html)
+ [ListProfileNotifications](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfileNotifications.html)
+ [ListProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfiles.html)
+ [ListProfileShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfileShares.html)
+ [UpdateProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateProfile.html)
+ [UpgradeProfileVersion](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeProfileVersion.html)

### Review templates
<a name="wa-tool-api-review-templates"></a>
+ [CreateReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateReviewTemplate.html)
+ [CreateTemplateShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateTemplateShare.html)
+ [DeleteReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteReviewTemplate.html)
+ [DeleteTemplateShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteTemplateShare.html)
+ [GetReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplate.html)
+ [GetReviewTemplateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplateAnswer.html)
+ [GetReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplateLensReview.html)
+ [ListReviewTemplateAnswers](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListReviewTemplateAnswers.html)
+ [ListReviewTemplates](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListReviewTemplates.html)
+ [ListTemplateShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListTemplateShares.html)
+ [UpdateReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplate.html)
+ [UpdateReviewTemplateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplateAnswer.html)
+ [UpdateReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplateLensReview.html)
+ [UpgradeReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeReviewTemplateLensReview.html)

### AWS Trusted Advisor checks
<a name="wa-tool-api-checks"></a>
+ [ListCheckDetails](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListCheckDetails.html)
+ [ListCheckSummaries](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListCheckSummaries.html)

### Notifications and settings
<a name="wa-tool-api-notifications-settings"></a>
+ [GetConsolidatedReport](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetConsolidatedReport.html)
+ [GetGlobalSettings](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetGlobalSettings.html)
+ [ListNotifications](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListNotifications.html)
+ [UpdateGlobalSettings](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateGlobalSettings.html)
+ [UpdateIntegration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateIntegration.html)

### Tagging
<a name="wa-tool-api-tagging"></a>
+ [ListTagsForResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListTagsForResource.html)
+ [TagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UntagResource.html)