

# Actions, resources, and condition keys for AWS Resilience Hub
<a name="list_resilience-hub"></a>

AWS Resilience Hub (service prefix: `resiliencehub`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/resilience-hub/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/resilience-hub/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/resiliencehub/resiliencehub.json) for this service.

**Topics**
+ [API operations defined by AWS Resilience Hub](#list_resilience-hub-operations)
+ [Actions defined by AWS Resilience Hub](#list_resilience-hub-actions-as-permissions)
+ [Resource types defined by AWS Resilience Hub](#list_resilience-hub-resources-for-iam-policies)
+ [Condition keys for AWS Resilience Hub](#list_resilience-hub-policy-keys)

## API operations defined by AWS Resilience Hub
<a name="list_resilience-hub-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_resilience-hub-actions-as-permissions).




- **   AcceptResourceGroupingRecommendations  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:AcceptResourceGroupingRecommendations](#list_resilience-hub-action-AcceptResourceGroupingRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddDraftAppVersionResourceMappings  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:AddDraftAppVersionResourceMappings](#list_resilience-hub-action-AddDraftAppVersionResourceMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateRecommendationStatus  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:BatchUpdateRecommendationStatus](#list_resilience-hub-action-BatchUpdateRecommendationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApp  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:CreateApp](#list_resilience-hub-action-CreateApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** resiliencehub.amazonaws.com / **Access level:** Write

- **   CreateAppVersionAppComponent  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:CreateAppVersionAppComponent](#list_resilience-hub-action-CreateAppVersionAppComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAppVersionResource  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:CreateAppVersionResource](#list_resilience-hub-action-CreateAppVersionResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRecommendationTemplate  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:CreateRecommendationTemplate](#list_resilience-hub-action-CreateRecommendationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateResiliencyPolicy  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:CreateResiliencyPolicy](#list_resilience-hub-action-CreateResiliencyPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteApp  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DeleteApp](#list_resilience-hub-action-DeleteApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAppAssessment  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DeleteAppAssessment](#list_resilience-hub-action-DeleteAppAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAppInputSource  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DeleteAppInputSource](#list_resilience-hub-action-DeleteAppInputSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAppVersionAppComponent  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DeleteAppVersionAppComponent](#list_resilience-hub-action-DeleteAppVersionAppComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAppVersionResource  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DeleteAppVersionResource](#list_resilience-hub-action-DeleteAppVersionResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecommendationTemplate  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DeleteRecommendationTemplate](#list_resilience-hub-action-DeleteRecommendationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResiliencyPolicy  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DeleteResiliencyPolicy](#list_resilience-hub-action-DeleteResiliencyPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeApp  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeApp](#list_resilience-hub-action-DescribeApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAppAssessment  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeAppAssessment](#list_resilience-hub-action-DescribeAppAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAppVersion  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeAppVersion](#list_resilience-hub-action-DescribeAppVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAppVersionAppComponent  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeAppVersionAppComponent](#list_resilience-hub-action-DescribeAppVersionAppComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAppVersionResource  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeAppVersionResource](#list_resilience-hub-action-DescribeAppVersionResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAppVersionResourcesResolutionStatus  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeAppVersionResourcesResolutionStatus](#list_resilience-hub-action-DescribeAppVersionResourcesResolutionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAppVersionTemplate  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeAppVersionTemplate](#list_resilience-hub-action-DescribeAppVersionTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDraftAppVersionResourcesImportStatus  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeDraftAppVersionResourcesImportStatus](#list_resilience-hub-action-DescribeDraftAppVersionResourcesImportStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetricsExport  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeMetricsExport](#list_resilience-hub-action-DescribeMetricsExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResiliencyPolicy  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeResiliencyPolicy](#list_resilience-hub-action-DescribeResiliencyPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourceGroupingRecommendationTask  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:DescribeResourceGroupingRecommendationTask](#list_resilience-hub-action-DescribeResourceGroupingRecommendationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportResourcesToDraftAppVersion  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ImportResourcesToDraftAppVersion](#list_resilience-hub-action-ImportResourcesToDraftAppVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAlarmRecommendations  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAlarmRecommendations](#list_resilience-hub-action-ListAlarmRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppAssessmentComplianceDrifts  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppAssessmentComplianceDrifts](#list_resilience-hub-action-ListAppAssessmentComplianceDrifts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppAssessmentResourceDrifts  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppAssessmentResourceDrifts](#list_resilience-hub-action-ListAppAssessmentResourceDrifts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppAssessments  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppAssessments](#list_resilience-hub-action-ListAppAssessments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppComponentCompliances  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppComponentCompliances](#list_resilience-hub-action-ListAppComponentCompliances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppComponentRecommendations  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppComponentRecommendations](#list_resilience-hub-action-ListAppComponentRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppInputSources  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppInputSources](#list_resilience-hub-action-ListAppInputSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppVersionAppComponents  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppVersionAppComponents](#list_resilience-hub-action-ListAppVersionAppComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppVersionResourceMappings  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppVersionResourceMappings](#list_resilience-hub-action-ListAppVersionResourceMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppVersionResources  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppVersionResources](#list_resilience-hub-action-ListAppVersionResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppVersions  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListAppVersions](#list_resilience-hub-action-ListAppVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApps  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListApps](#list_resilience-hub-action-ListApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMetrics  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListMetrics](#list_resilience-hub-action-ListMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendationTemplates  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListRecommendationTemplates](#list_resilience-hub-action-ListRecommendationTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResiliencyPolicies  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListResiliencyPolicies](#list_resilience-hub-action-ListResiliencyPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceGroupingRecommendations  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListResourceGroupingRecommendations](#list_resilience-hub-action-ListResourceGroupingRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSopRecommendations  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListSopRecommendations](#list_resilience-hub-action-ListSopRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSuggestedResiliencyPolicies  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListSuggestedResiliencyPolicies](#list_resilience-hub-action-ListSuggestedResiliencyPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListTagsForResource](#list_resilience-hub-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTestRecommendations  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListTestRecommendations](#list_resilience-hub-action-ListTestRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUnsupportedAppVersionResources  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ListUnsupportedAppVersionResources](#list_resilience-hub-action-ListUnsupportedAppVersionResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PublishAppVersion  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:PublishAppVersion](#list_resilience-hub-action-PublishAppVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDraftAppVersionTemplate  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:PutDraftAppVersionTemplate](#list_resilience-hub-action-PutDraftAppVersionTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectResourceGroupingRecommendations  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:RejectResourceGroupingRecommendations](#list_resilience-hub-action-RejectResourceGroupingRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveDraftAppVersionResourceMappings  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:RemoveDraftAppVersionResourceMappings](#list_resilience-hub-action-RemoveDraftAppVersionResourceMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResolveAppVersionResources  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:ResolveAppVersionResources](#list_resilience-hub-action-ResolveAppVersionResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAppAssessment  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:StartAppAssessment](#list_resilience-hub-action-StartAppAssessment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartMetricsExport  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:StartMetricsExport](#list_resilience-hub-action-StartMetricsExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartResourceGroupingRecommendationTask  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:StartResourceGroupingRecommendationTask](#list_resilience-hub-action-StartResourceGroupingRecommendationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:UntagResource](#list_resilience-hub-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApp  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:UpdateApp](#list_resilience-hub-action-UpdateApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** resiliencehub.amazonaws.com / **Access level:** Write

- **   UpdateAppVersion  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:UpdateAppVersion](#list_resilience-hub-action-UpdateAppVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAppVersionAppComponent  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:UpdateAppVersionAppComponent](#list_resilience-hub-action-UpdateAppVersionAppComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAppVersionResource  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:UpdateAppVersionResource](#list_resilience-hub-action-UpdateAppVersionResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResiliencyPolicy  **
  - **SDK client:** resiliencehub
  - **IAM action:**  [resiliencehub:UpdateResiliencyPolicy](#list_resilience-hub-action-UpdateResiliencyPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssertion  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateAssertion](#list_resilience-hub-action-CreateAssertion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInputSource  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateInputSource](#list_resilience-hub-action-CreateInputSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePolicy  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreatePolicy](#list_resilience-hub-action-CreatePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateReport  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateReport](#list_resilience-hub-action-CreateReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateService  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateService](#list_resilience-hub-action-CreateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** resiliencehub.amazonaws.com / **Access level:** Write

- **   CreateServiceFunction  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateServiceFunction](#list_resilience-hub-action-CreateServiceFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateServiceFunctionResources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateServiceFunctionResources](#list_resilience-hub-action-CreateServiceFunctionResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSystem  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateSystem](#list_resilience-hub-action-CreateSystem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTest  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateTest](#list_resilience-hub-action-CreateTest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** fis.amazonaws.com / **Access level:** Write

- **   CreateUserJourney  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:CreateUserJourney](#list_resilience-hub-action-CreateUserJourney) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssertion  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteAssertion](#list_resilience-hub-action-DeleteAssertion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInputSource  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteInputSource](#list_resilience-hub-action-DeleteInputSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicy  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeletePolicy](#list_resilience-hub-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteService  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteService](#list_resilience-hub-action-DeleteService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceFunction  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteServiceFunction](#list_resilience-hub-action-DeleteServiceFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceFunctionResources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteServiceFunctionResources](#list_resilience-hub-action-DeleteServiceFunctionResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSystem  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteSystem](#list_resilience-hub-action-DeleteSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTest  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteTest](#list_resilience-hub-action-DeleteTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTestSources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteTestSources](#list_resilience-hub-action-DeleteTestSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserJourney  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:DeleteUserJourney](#list_resilience-hub-action-DeleteUserJourney) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetFailureModeFinding  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:GetFailureModeFinding](#list_resilience-hub-action-GetFailureModeFinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:GetPolicy](#list_resilience-hub-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetService  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:GetService](#list_resilience-hub-action-GetService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSystem  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:GetSystem](#list_resilience-hub-action-GetSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTest  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:GetTest](#list_resilience-hub-action-GetTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTestRun  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:GetTestRun](#list_resilience-hub-action-GetTestRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTestTemplate  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:GetTestTemplate](#list_resilience-hub-action-GetTestTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUserJourney  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:GetUserJourney](#list_resilience-hub-action-GetUserJourney) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportApp  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ImportApp](#list_resilience-hub-action-ImportApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ImportPolicy  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ImportPolicy](#list_resilience-hub-action-ImportPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAssertions  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListAssertions](#list_resilience-hub-action-ListAssertions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDependencies  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListDependencies](#list_resilience-hub-action-ListDependencies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFailureModeAssessments  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListFailureModeAssessments](#list_resilience-hub-action-ListFailureModeAssessments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFailureModeFindings  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListFailureModeFindings](#list_resilience-hub-action-ListFailureModeFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInputSources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListInputSources](#list_resilience-hub-action-ListInputSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPolicies  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListPolicies](#list_resilience-hub-action-ListPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListReports  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListReports](#list_resilience-hub-action-ListReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListResolvedTestRunTargetResources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListResolvedTestRunTargetResources](#list_resilience-hub-action-ListResolvedTestRunTargetResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListResources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListResources](#list_resilience-hub-action-ListResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceEvents  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListServiceEvents](#list_resilience-hub-action-ListServiceEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceFunctions  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListServiceFunctions](#list_resilience-hub-action-ListServiceFunctions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceTopologyEdges  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListServiceTopologyEdges](#list_resilience-hub-action-ListServiceTopologyEdges) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServices  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListServices](#list_resilience-hub-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSystemEvents  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListSystemEvents](#list_resilience-hub-action-ListSystemEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSystems  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListSystems](#list_resilience-hub-action-ListSystems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListTagsForResource](#list_resilience-hub-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTestRunEvents  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListTestRunEvents](#list_resilience-hub-action-ListTestRunEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTestRunSources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListTestRunSources](#list_resilience-hub-action-ListTestRunSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTestRuns  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListTestRuns](#list_resilience-hub-action-ListTestRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTestSources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListTestSources](#list_resilience-hub-action-ListTestSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTestTemplates  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListTestTemplates](#list_resilience-hub-action-ListTestTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTests  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListTests](#list_resilience-hub-action-ListTests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListUserJourneys  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:ListUserJourneys](#list_resilience-hub-action-ListUserJourneys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutTestSources  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:PutTestSources](#list_resilience-hub-action-PutTestSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFailureModeAssessment  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:StartFailureModeAssessment](#list_resilience-hub-action-StartFailureModeAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTestRun  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:StartTestRun](#list_resilience-hub-action-StartTestRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTestRun  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:StopTestRun](#list_resilience-hub-action-StopTestRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:TagResource](#list_resilience-hub-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UntagResource](#list_resilience-hub-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAssertion  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdateAssertion](#list_resilience-hub-action-UpdateAssertion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDependency  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdateDependency](#list_resilience-hub-action-UpdateDependency) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFailureModeFinding  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdateFailureModeFinding](#list_resilience-hub-action-UpdateFailureModeFinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePolicy  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdatePolicy](#list_resilience-hub-action-UpdatePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateService  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdateService](#list_resilience-hub-action-UpdateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** resiliencehub.amazonaws.com / **Access level:** Write

- **   UpdateServiceFunction  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdateServiceFunction](#list_resilience-hub-action-UpdateServiceFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSystem  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdateSystem](#list_resilience-hub-action-UpdateSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTest  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdateTest](#list_resilience-hub-action-UpdateTest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** fis.amazonaws.com / **Access level:** Write

- **   UpdateUserJourney  **
  - **SDK client:** resiliencehubv2
  - **IAM action:**  [resiliencehub:UpdateUserJourney](#list_resilience-hub-action-UpdateUserJourney) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Resilience Hub
<a name="list_resilience-hub-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptResourceGroupingRecommendations](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AcceptResourceGroupingRecommendations.html)  **
  - **Description:** Grants permission to accept resource grouping recommendations
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddDraftAppVersionResourceMappings](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AddDraftAppVersionResourceMappings.html)  **
  - **Description:** Grants permission to add draft application version resource mappings
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchUpdateRecommendationStatus](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_BatchUpdateRecommendationStatus.html)  **
  - **Description:** Grants permission to include or exclude one or more operational recommendations
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApp](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateApp.html)  **
  - **Description:** Grants permission to create application
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAppVersionAppComponent](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateAppVersionAppComponent.html)  **
  - **Description:** Grants permission to create application app component
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAppVersionResource](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateAppVersionResource.html)  **
  - **Description:** Grants permission to create application resource
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAssertion](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateAssertion.html)  **
  - **Description:** Grants permission to create an assertion for a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInputSource](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateInputSource.html)  **
  - **Description:** Grants permission to create an input source for a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePolicy](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreatePolicy.html)  **
  - **Description:** Grants permission to create a resilience policy that defines availability and disaster recovery requirements
  - **Resource types (\*required):** [policy\*](#list_resilience-hub-resource-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecommendationTemplate](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateRecommendationTemplate.html)  **
  - **Description:** Grants permission to create recommendation template
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateReport](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateReport.html)  **
  - **Description:** Grants permission to create a report for a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateResiliencyPolicy](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_CreateResiliencyPolicy.html)  **
  - **Description:** Grants permission to create resiliency policy
  - **Resource types (\*required):** [resiliency-policy\*](#list_resilience-hub-resource-resiliency-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateService](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateService.html)  **
  - **Description:** Grants permission to create a service
  - **Resource types (\*required):** [policy](#list_resilience-hub-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [system](#list_resilience-hub-resource-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateServiceFunction](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateServiceFunction.html)  **
  - **Description:** Grants permission to create a service function
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateServiceFunctionResources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateServiceFunctionResources.html)  **
  - **Description:** Grants permission to create service function resources
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSystem](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateSystem.html)  **
  - **Description:** Grants permission to create a system that represents a logical grouping of services
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTest](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateTest.html)  **
  - **Description:** Grants permission to create a test instance
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUserJourney](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateUserJourney.html)  **
  - **Description:** Grants permission to create a user journey within a system
  - **Resource types (\*required):** [policy](#list_resilience-hub-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApp](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteApp.html)  **
  - **Description:** Grants permission to batch delete application
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAppAssessment](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteAppAssessment.html)  **
  - **Description:** Grants permission to batch delete application assessment
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAppInputSource](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteAppInputSource.html)  **
  - **Description:** Grants permission to remove application input source
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAppVersionAppComponent](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteAppVersionAppComponent.html)  **
  - **Description:** Grants permission to delete application app component
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAppVersionResource](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteAppVersionResource.html)  **
  - **Description:** Grants permission to delete application resource
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssertion](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteAssertion.html)  **
  - **Description:** Grants permission to delete an assertion
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInputSource](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteInputSource.html)  **
  - **Description:** Grants permission to delete an input source
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to delete a resilience policy
  - **Resource types (\*required):** [policy\*](#list_resilience-hub-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecommendationTemplate](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteRecommendationTemplate.html)  **
  - **Description:** Grants permission to batch delete recommendation template
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResiliencyPolicy](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteResiliencyPolicy.html)  **
  - **Description:** Grants permission to batch delete resiliency policy
  - **Resource types (\*required):** [resiliency-policy\*](#list_resilience-hub-resource-resiliency-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteService](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteService.html)  **
  - **Description:** Grants permission to delete a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceFunction](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteServiceFunction.html)  **
  - **Description:** Grants permission to delete a service function
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceFunctionResources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteServiceFunctionResources.html)  **
  - **Description:** Grants permission to delete service function resources
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSystem](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteSystem.html)  **
  - **Description:** Grants permission to delete a system
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTest](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteTest.html)  **
  - **Description:** Grants permission to delete a test
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTestSources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteTestSources.html)  **
  - **Description:** Grants permission to delete test sources from a test
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserJourney](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteUserJourney.html)  **
  - **Description:** Grants permission to delete a user journey
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeApp](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeApp.html)  **
  - **Description:** Grants permission to describe application
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAppAssessment](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeAppAssessment.html)  **
  - **Description:** Grants permission to describe application assessment
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAppVersion](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeAppVersion.html)  **
  - **Description:** Grants permission to describe application version
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAppVersionAppComponent](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeAppVersionAppComponent.html)  **
  - **Description:** Grants permission to describe application version app component
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAppVersionResource](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeAppVersionResource.html)  **
  - **Description:** Grants permission to describe application version resource
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAppVersionResourcesResolutionStatus](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeAppVersionResourcesResolutionStatus.html)  **
  - **Description:** Grants permission to describe application resolution
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAppVersionTemplate](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeAppVersionTemplate.html)  **
  - **Description:** Grants permission to describe application version template
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDraftAppVersionResourcesImportStatus](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeDraftAppVersionResourcesImportStatus.html)  **
  - **Description:** Grants permission to describe draft application version resources import status
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMetricsExport](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeMetricsExport.html)  **
  - **Description:** Grants permission to describe metrics export
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeResiliencyPolicy](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeResiliencyPolicy.html)  **
  - **Description:** Grants permission to describe resiliency policy
  - **Resource types (\*required):** [resiliency-policy\*](#list_resilience-hub-resource-resiliency-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeResourceGroupingRecommendationTask](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeResourceGroupingRecommendationTask.html)  **
  - **Description:** Grants permission to describe the latest status of the grouping recommendation process
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFailureModeFinding](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetFailureModeFinding.html)  **
  - **Description:** Grants permission to retrieve a failure mode finding
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetPolicy.html)  **
  - **Description:** Grants permission to retrieve a resilience policy
  - **Resource types (\*required):** [policy\*](#list_resilience-hub-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetService](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetService.html)  **
  - **Description:** Grants permission to retrieve a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSystem](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetSystem.html)  **
  - **Description:** Grants permission to retrieve a system
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTest](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetTest.html)  **
  - **Description:** Grants permission to retrieve a test
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTestRun](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetTestRun.html)  **
  - **Description:** Grants permission to retrieve a test run
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTestTemplate](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetTestTemplate.html)  **
  - **Description:** Grants permission to retrieve a test template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUserJourney](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetUserJourney.html)  **
  - **Description:** Grants permission to retrieve a user journey
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportApp](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ImportApp.html)  **
  - **Description:** Grants permission to import a V1 app into the V2 resource model
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Write

- **   [ImportPolicy](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ImportPolicy.html)  **
  - **Description:** Grants permission to import a V1 policy into V2
  - **Resource types (\*required):** [policy\*](#list_resilience-hub-resource-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [resiliency-policy\*](#list_resilience-hub-resource-resiliency-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ImportResourcesToDraftAppVersion](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ImportResourcesToDraftAppVersion.html)  **
  - **Description:** Grants permission to import resources to draft application version
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAlarmRecommendations](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAlarmRecommendations.html)  **
  - **Description:** Grants permission to list alarm recommendation
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppAssessmentComplianceDrifts](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppAssessmentComplianceDrifts.html)  **
  - **Description:** Grants permission to list compliance drifts that were detected while running an assessment
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppAssessmentResourceDrifts](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppAssessmentResourceDrifts.html)  **
  - **Description:** Grants permission to list resource drifts that were detected while running an assessment
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppAssessments](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppAssessments.html)  **
  - **Description:** Grants permission to list application assessment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAppComponentCompliances](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppComponentCompliances.html)  **
  - **Description:** Grants permission to list app component compliances
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppComponentRecommendations](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppComponentRecommendations.html)  **
  - **Description:** Grants permission to list app component recommendations
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppInputSources](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppInputSources.html)  **
  - **Description:** Grants permission to list application input sources
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppVersionAppComponents](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppVersionAppComponents.html)  **
  - **Description:** Grants permission to list application version app components
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppVersionResourceMappings](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppVersionResourceMappings.html)  **
  - **Description:** Grants permission to application version resource mappings
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppVersionResources](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppVersionResources.html)  **
  - **Description:** Grants permission to list application resources
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppVersions](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppVersions.html)  **
  - **Description:** Grants permission to list application version
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApps](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListApps.html)  **
  - **Description:** Grants permission to list applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssertions](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListAssertions.html)  **
  - **Description:** Grants permission to list assertions for a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDependencies](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListDependencies.html)  **
  - **Description:** Grants permission to list dependencies discovered for services
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListFailureModeAssessments](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListFailureModeAssessments.html)  **
  - **Description:** Grants permission to list failure mode assessments
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFailureModeFindings](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListFailureModeFindings.html)  **
  - **Description:** Grants permission to list failure mode findings
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInputSources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListInputSources.html)  **
  - **Description:** Grants permission to list input sources for a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListMetrics](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListMetrics.html)  **
  - **Description:** Grants permission to list metrics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicies](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListPolicies.html)  **
  - **Description:** Grants permission to list resilience policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRecommendationTemplates](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListRecommendationTemplates.html)  **
  - **Description:** Grants permission to list recommendation templates
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReports](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListReports.html)  **
  - **Description:** Grants permission to list reports
  - **Resource types (\*required):** [service](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListResiliencyPolicies](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListResiliencyPolicies.html)  **
  - **Description:** Grants permission to list resiliency policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResolvedTestRunTargetResources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListResolvedTestRunTargetResources.html)  **
  - **Description:** Grants permission to list resolved target resources for a test run
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListResourceGroupingRecommendations](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListResourceGroupingRecommendations.html)  **
  - **Description:** Grants permission to list resource grouping recommendations
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListResources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListResources.html)  **
  - **Description:** Grants permission to list resources for a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListServiceEvents](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListServiceEvents.html)  **
  - **Description:** Grants permission to list events for a service
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListServiceFunctions](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListServiceFunctions.html)  **
  - **Description:** Grants permission to list service functions
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListServiceTopologyEdges](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListServiceTopologyEdges.html)  **
  - **Description:** Grants permission to list service topology edges
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListServices](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListServices.html)  **
  - **Description:** Grants permission to list services
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSopRecommendations](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListSopRecommendations.html)  **
  - **Description:** Grants permission to list SOP recommendations
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSuggestedResiliencyPolicies](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListSuggestedResiliencyPolicies.html)  **
  - **Description:** Grants permission to list suggested resiliency policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSystemEvents](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListSystemEvents.html)  **
  - **Description:** Grants permission to list events for a system
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSystems](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListSystems.html)  **
  - **Description:** Grants permission to list systems
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [app-assessment](#list_resilience-hub-resource-app-assessment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [application](#list_resilience-hub-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy](#list_resilience-hub-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommendation-template](#list_resilience-hub-resource-recommendation-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [resiliency-policy](#list_resilience-hub-resource-resiliency-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service](#list_resilience-hub-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [system](#list_resilience-hub-resource-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestRecommendations](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListTestRecommendations.html)  **
  - **Description:** Grants permission to list test recommendations
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTestRunEvents](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTestRunEvents.html)  **
  - **Description:** Grants permission to list events for a test run
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestRunSources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTestRunSources.html)  **
  - **Description:** Grants permission to list test run source snapshots
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestRuns](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTestRuns.html)  **
  - **Description:** Grants permission to list test runs for a target
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestSources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTestSources.html)  **
  - **Description:** Grants permission to list test sources on a test
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestTemplates](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTestTemplates.html)  **
  - **Description:** Grants permission to list available test templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTests](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTests.html)  **
  - **Description:** Grants permission to list tests for a target
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUnsupportedAppVersionResources](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListUnsupportedAppVersionResources.html)  **
  - **Description:** Grants permission to list unsupported application version resources
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserJourneys](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListUserJourneys.html)  **
  - **Description:** Grants permission to list user journeys for a system
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PublishAppVersion](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PublishAppVersion.html)  **
  - **Description:** Grants permission to publish application version
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDraftAppVersionTemplate](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PutDraftAppVersionTemplate.html)  **
  - **Description:** Grants permission to put draft application version template
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutTestSources](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_PutTestSources.html)  **
  - **Description:** Grants permission to put test sources on a test
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RejectResourceGroupingRecommendations](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RejectResourceGroupingRecommendations.html)  **
  - **Description:** Grants permission to reject resource grouping recommendations
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveDraftAppVersionResourceMappings](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RemoveDraftAppVersionResourceMappings.html)  **
  - **Description:** Grants permission to remove draft application version mappings
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResolveAppVersionResources](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResolveAppVersionResources.html)  **
  - **Description:** Grants permission to resolve application version resources
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAppAssessment](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_StartAppAssessment.html)  **
  - **Description:** Grants permission to create application assessment
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Write

- **   [StartFailureModeAssessment](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_StartFailureModeAssessment.html)  **
  - **Description:** Grants permission to start a failure mode assessment
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMetricsExport](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_StartMetricsExport.html)  **
  - **Description:** Grants permission to start the metrics export
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartResourceGroupingRecommendationTask](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_StartResourceGroupingRecommendationTask.html)  **
  - **Description:** Grants permission to start the grouping recommendation generation process
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTestRun](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_StartTestRun.html)  **
  - **Description:** Grants permission to start a test run
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTestRun](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_StopTestRun.html)  **
  - **Description:** Grants permission to stop a test run
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to assign a resource tag
  - **Resource types (\*required):** [app-assessment](#list_resilience-hub-resource-app-assessment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [application](#list_resilience-hub-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [policy](#list_resilience-hub-resource-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [recommendation-template](#list_resilience-hub-resource-recommendation-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [resiliency-policy](#list_resilience-hub-resource-resiliency-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_resilience-hub-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [system](#list_resilience-hub-resource-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_resilience-hub-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [app-assessment](#list_resilience-hub-resource-app-assessment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [application](#list_resilience-hub-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [policy](#list_resilience-hub-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [recommendation-template](#list_resilience-hub-resource-recommendation-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [resiliency-policy](#list_resilience-hub-resource-resiliency-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_resilience-hub-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Resource types (\*required):** [system](#list_resilience-hub-resource-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resilience-hub-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApp](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateApp.html)  **
  - **Description:** Grants permission to update application
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAppVersion](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateAppVersion.html)  **
  - **Description:** Grants permission to update application version
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAppVersionAppComponent](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateAppVersionAppComponent.html)  **
  - **Description:** Grants permission to update application app component
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAppVersionResource](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateAppVersionResource.html)  **
  - **Description:** Grants permission to update application resource
  - **Resource types (\*required):** [application\*](#list_resilience-hub-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssertion](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateAssertion.html)  **
  - **Description:** Grants permission to update an assertion
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDependency](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateDependency.html)  **
  - **Description:** Grants permission to update a dependency classification
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFailureModeFinding](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateFailureModeFinding.html)  **
  - **Description:** Grants permission to update a failure mode finding
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePolicy](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdatePolicy.html)  **
  - **Description:** Grants permission to update a resilience policy
  - **Resource types (\*required):** [policy\*](#list_resilience-hub-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResiliencyPolicy](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateResiliencyPolicy.html)  **
  - **Description:** Grants permission to update resiliency policy
  - **Resource types (\*required):** [resiliency-policy\*](#list_resilience-hub-resource-resiliency-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateService](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateService.html)  **
  - **Description:** Grants permission to update a service
  - **Resource types (\*required):** [policy](#list_resilience-hub-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [system](#list_resilience-hub-resource-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceFunction](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateServiceFunction.html)  **
  - **Description:** Grants permission to update a service function
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSystem](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateSystem.html)  **
  - **Description:** Grants permission to update a system
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTest](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateTest.html)  **
  - **Description:** Grants permission to update a test
  - **Resource types (\*required):** [service\*](#list_resilience-hub-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserJourney](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateUserJourney.html)  **
  - **Description:** Grants permission to update a user journey
  - **Resource types (\*required):** [policy](#list_resilience-hub-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [system\*](#list_resilience-hub-resource-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Resilience Hub
<a name="list_resilience-hub-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [app-assessment](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppAssessment.html)  | arn:${Partition}:resiliencehub:${Region}:${Account}:app-assessment/${AppAssessmentId} | [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_) | 
|  [application](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_App.html)  | arn:${Partition}:resiliencehub:${Region}:${Account}:app/${AppId} | [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_) | 
|  [policy](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Policy.html)  | arn:${Partition}:resiliencehub:${Region}:${Account}:policy/${PolicyId} | [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_) | 
|  [recommendation-template](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RecommendationTemplate.html)  | arn:${Partition}:resiliencehub:${Region}:${Account}:recommendation-template/${RecommendationTemplateId} | [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_) | 
|  [resiliency-policy](https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ResiliencyPolicy.html)  | arn:${Partition}:resiliencehub:${Region}:${Account}:resiliency-policy/${ResiliencyPolicyId} | [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_) | 
|  [service](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Service.html)  | arn:${Partition}:resiliencehub:${Region}:${Account}:service/${ServiceId} | [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_) | 
|  [system](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_System.html)  | arn:${Partition}:resiliencehub:${Region}:${Account}:system/${SystemId} | [aws:ResourceTag/${TagKey}](#list_resilience-hub-aws_ResourceTag___TagKey_) | 
|  [test-template](https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_GetTestTemplate.html)  | arn:${Partition}:resiliencehub:${Region}:${Account}:test-template/${TestTemplateId} |   | 

## Condition keys for AWS Resilience Hub
<a name="list_resilience-hub-policy-keys"></a>

AWS Resilience Hub defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 