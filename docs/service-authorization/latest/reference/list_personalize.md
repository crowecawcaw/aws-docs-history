

# Actions, resources, and condition keys for Amazon Personalize
<a name="list_personalize"></a>

Amazon Personalize (service prefix: `personalize`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/personalize/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/personalize/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/personalize/latest/dg/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/personalize/personalize.json) for this service.

**Topics**
+ [API operations defined by Amazon Personalize](#list_personalize-operations)
+ [Actions defined by Amazon Personalize](#list_personalize-actions-as-permissions)
+ [Resource types defined by Amazon Personalize](#list_personalize-resources-for-iam-policies)
+ [Condition keys for Amazon Personalize](#list_personalize-policy-keys)

## API operations defined by Amazon Personalize
<a name="list_personalize-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_personalize-actions-as-permissions).




- **   CreateBatchInferenceJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateBatchInferenceJob](#list_personalize-action-CreateBatchInferenceJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** personalize.amazonaws.com / **Access level:** Write

- **   CreateBatchSegmentJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateBatchSegmentJob](#list_personalize-action-CreateBatchSegmentJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** personalize.amazonaws.com / **Access level:** Write

- **   CreateCampaign  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateCampaign](#list_personalize-action-CreateCampaign)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataDeletionJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateDataDeletionJob](#list_personalize-action-CreateDataDeletionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** personalize.amazonaws.com / **Access level:** Write

- **   CreateDataset  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateDataset](#list_personalize-action-CreateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDatasetExportJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateDatasetExportJob](#list_personalize-action-CreateDatasetExportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** personalize.amazonaws.com / **Access level:** Write

- **   CreateDatasetGroup  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateDatasetGroup](#list_personalize-action-CreateDatasetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** personalize.amazonaws.com / **Access level:** Write

- **   CreateDatasetImportJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateDatasetImportJob](#list_personalize-action-CreateDatasetImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** personalize.amazonaws.com / **Access level:** Write

- **   CreateEventTracker  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateEventTracker](#list_personalize-action-CreateEventTracker)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFilter  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateFilter](#list_personalize-action-CreateFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMetricAttribution  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateMetricAttribution](#list_personalize-action-CreateMetricAttribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** personalize.amazonaws.com / **Access level:** Write

- **   CreateRecommender  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateRecommender](#list_personalize-action-CreateRecommender)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSchema  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateSchema](#list_personalize-action-CreateSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSolution  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateSolution](#list_personalize-action-CreateSolution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSolutionVersion  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:CreateSolutionVersion](#list_personalize-action-CreateSolutionVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCampaign  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteCampaign](#list_personalize-action-DeleteCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataset  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteDataset](#list_personalize-action-DeleteDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDatasetGroup  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteDatasetGroup](#list_personalize-action-DeleteDatasetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventTracker  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteEventTracker](#list_personalize-action-DeleteEventTracker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFilter  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteFilter](#list_personalize-action-DeleteFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMetricAttribution  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteMetricAttribution](#list_personalize-action-DeleteMetricAttribution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecommender  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteRecommender](#list_personalize-action-DeleteRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchema  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteSchema](#list_personalize-action-DeleteSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSolution  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DeleteSolution](#list_personalize-action-DeleteSolution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAlgorithm  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeAlgorithm](#list_personalize-action-DescribeAlgorithm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBatchInferenceJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeBatchInferenceJob](#list_personalize-action-DescribeBatchInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBatchSegmentJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeBatchSegmentJob](#list_personalize-action-DescribeBatchSegmentJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCampaign  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeCampaign](#list_personalize-action-DescribeCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataDeletionJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeDataDeletionJob](#list_personalize-action-DescribeDataDeletionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataset  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeDataset](#list_personalize-action-DescribeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDatasetExportJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeDatasetExportJob](#list_personalize-action-DescribeDatasetExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDatasetGroup  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeDatasetGroup](#list_personalize-action-DescribeDatasetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDatasetImportJob  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeDatasetImportJob](#list_personalize-action-DescribeDatasetImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventTracker  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeEventTracker](#list_personalize-action-DescribeEventTracker) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFeatureTransformation  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeFeatureTransformation](#list_personalize-action-DescribeFeatureTransformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFilter  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeFilter](#list_personalize-action-DescribeFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetricAttribution  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeMetricAttribution](#list_personalize-action-DescribeMetricAttribution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecipe  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeRecipe](#list_personalize-action-DescribeRecipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecommender  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeRecommender](#list_personalize-action-DescribeRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSchema  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeSchema](#list_personalize-action-DescribeSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSolution  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeSolution](#list_personalize-action-DescribeSolution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSolutionVersion  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:DescribeSolutionVersion](#list_personalize-action-DescribeSolutionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolutionMetrics  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:GetSolutionMetrics](#list_personalize-action-GetSolutionMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBatchInferenceJobs  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListBatchInferenceJobs](#list_personalize-action-ListBatchInferenceJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBatchSegmentJobs  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListBatchSegmentJobs](#list_personalize-action-ListBatchSegmentJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCampaigns  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListCampaigns](#list_personalize-action-ListCampaigns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataDeletionJobs  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListDataDeletionJobs](#list_personalize-action-ListDataDeletionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasetExportJobs  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListDatasetExportJobs](#list_personalize-action-ListDatasetExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasetGroups  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListDatasetGroups](#list_personalize-action-ListDatasetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasetImportJobs  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListDatasetImportJobs](#list_personalize-action-ListDatasetImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasets  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListDatasets](#list_personalize-action-ListDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventTrackers  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListEventTrackers](#list_personalize-action-ListEventTrackers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFilters  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListFilters](#list_personalize-action-ListFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMetricAttributionMetrics  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListMetricAttributionMetrics](#list_personalize-action-ListMetricAttributionMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMetricAttributions  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListMetricAttributions](#list_personalize-action-ListMetricAttributions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecipes  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListRecipes](#list_personalize-action-ListRecipes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommenders  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListRecommenders](#list_personalize-action-ListRecommenders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchemas  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListSchemas](#list_personalize-action-ListSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSolutionVersions  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListSolutionVersions](#list_personalize-action-ListSolutionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSolutions  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListSolutions](#list_personalize-action-ListSolutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:ListTagsForResource](#list_personalize-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartRecommender  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:StartRecommender](#list_personalize-action-StartRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRecommender  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:StopRecommender](#list_personalize-action-StopRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopSolutionVersionCreation  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:StopSolutionVersionCreation](#list_personalize-action-StopSolutionVersionCreation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:TagResource](#list_personalize-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:UntagResource](#list_personalize-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCampaign  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:UpdateCampaign](#list_personalize-action-UpdateCampaign) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataset  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:UpdateDataset](#list_personalize-action-UpdateDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMetricAttribution  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:UpdateMetricAttribution](#list_personalize-action-UpdateMetricAttribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** personalize.amazonaws.com / **Access level:** Write

- **   UpdateRecommender  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:UpdateRecommender](#list_personalize-action-UpdateRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSolution  **
  - **SDK client:** personalize
  - **IAM action:**  [personalize:UpdateSolution](#list_personalize-action-UpdateSolution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutActionInteractions  **
  - **SDK client:** personalize-events
  - **IAM action:**  [personalize:PutActionInteractions](#list_personalize-action-PutActionInteractions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutActions  **
  - **SDK client:** personalize-events
  - **IAM action:**  [personalize:PutActions](#list_personalize-action-PutActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutEvents  **
  - **SDK client:** personalize-events
  - **IAM action:**  [personalize:PutEvents](#list_personalize-action-PutEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutItems  **
  - **SDK client:** personalize-events
  - **IAM action:**  [personalize:PutItems](#list_personalize-action-PutItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutUsers  **
  - **SDK client:** personalize-events
  - **IAM action:**  [personalize:PutUsers](#list_personalize-action-PutUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetActionRecommendations  **
  - **SDK client:** personalize-runtime
  - **IAM action:**  [personalize:GetActionRecommendations](#list_personalize-action-GetActionRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPersonalizedRanking  **
  - **SDK client:** personalize-runtime
  - **IAM action:**  [personalize:GetPersonalizedRanking](#list_personalize-action-GetPersonalizedRanking) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendations  **
  - **SDK client:** personalize-runtime
  - **IAM action:**  [personalize:GetRecommendations](#list_personalize-action-GetRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Personalize
<a name="list_personalize-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateBatchInferenceJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateBatchInferenceJob.html)  **
  - **Description:** Grants permission to create a batch inference job
  - **Resource types (\*required):** [batchInferenceJob\*](#list_personalize-resource-batchInferenceJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBatchSegmentJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateBatchSegmentJob.html)  **
  - **Description:** Grants permission to create a batch segment job
  - **Resource types (\*required):** [batchSegmentJob\*](#list_personalize-resource-batchSegmentJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html)  **
  - **Description:** Grants permission to create a campaign
  - **Resource types (\*required):** [campaign\*](#list_personalize-resource-campaign) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataDeletionJob.html)  **
  - **Description:** Grants permission to create a data deletion job
  - **Resource types (\*required):** [dataDeletionJob\*](#list_personalize-resource-dataDeletionJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataInsightsJob](https://docs.aws.amazon.com/personalize/latest/dg/analyzing-data.html)  **
  - **Description:** Grants permission to create a data insights job
  - **Resource types (\*required):** [dataInsightsJob\*](#list_personalize-resource-dataInsightsJob)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a dataset
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDatasetExportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetExportJob.html)  **
  - **Description:** Grants permission to create a dataset export job
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetExportJob\*](#list_personalize-resource-datasetExportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html)  **
  - **Description:** Grants permission to create a dataset group
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html)  **
  - **Description:** Grants permission to create a dataset import job
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetImportJob\*](#list_personalize-resource-datasetImportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateEventTracker.html)  **
  - **Description:** Grants permission to create an event tracker
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [eventTracker\*](#list_personalize-resource-eventTracker) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFilter](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateFilter.html)  **
  - **Description:** Grants permission to create a filter
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [filter\*](#list_personalize-resource-filter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateMetricAttribution.html)  **
  - **Description:** Grants permission to create a metric attribution
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [metricAttribution\*](#list_personalize-resource-metricAttribution) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateRecommender.html)  **
  - **Description:** Grants permission to create a recommender
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [recommender\*](#list_personalize-resource-recommender) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSchema](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSchema.html)  **
  - **Description:** Grants permission to create a schema
  - **Resource types (\*required):** [schema\*](#list_personalize-resource-schema)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html)  **
  - **Description:** Grants permission to create a solution
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolutionVersion.html)  **
  - **Description:** Grants permission to create a solution version
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteCampaign.html)  **
  - **Description:** Grants permission to delete a campaign
  - **Resource types (\*required):** [campaign\*](#list_personalize-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDatasetGroup.html)  **
  - **Description:** Grants permission to delete a dataset group
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteEventTracker.html)  **
  - **Description:** Grants permission to delete an event tracker
  - **Resource types (\*required):** [eventTracker\*](#list_personalize-resource-eventTracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFilter](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteFilter.html)  **
  - **Description:** Grants permission to delete a filter
  - **Resource types (\*required):** [filter\*](#list_personalize-resource-filter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteMetricAttribution.html)  **
  - **Description:** Grants permission to delete a metric attribution
  - **Resource types (\*required):** [metricAttribution\*](#list_personalize-resource-metricAttribution)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteRecommender.html)  **
  - **Description:** Grants permission to delete a recommender
  - **Resource types (\*required):** [recommender\*](#list_personalize-resource-recommender)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSchema](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSchema.html)  **
  - **Description:** Grants permission to delete a schema
  - **Resource types (\*required):** [schema\*](#list_personalize-resource-schema)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSolution.html)  **
  - **Description:** Grants permission to delete a solution including all versions of the solution
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAlgorithm](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeAlgorithm.html)  **
  - **Description:** Grants permission to describe an algorithm
  - **Resource types (\*required):** [algorithm\*](#list_personalize-resource-algorithm)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeBatchInferenceJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeBatchInferenceJob.html)  **
  - **Description:** Grants permission to describe a batch inference job
  - **Resource types (\*required):** [batchInferenceJob\*](#list_personalize-resource-batchInferenceJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBatchSegmentJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeBatchSegmentJob.html)  **
  - **Description:** Grants permission to describe a batch segment job
  - **Resource types (\*required):** [batchSegmentJob\*](#list_personalize-resource-batchSegmentJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html)  **
  - **Description:** Grants permission to describe a campaign
  - **Resource types (\*required):** [campaign\*](#list_personalize-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataDeletionJob.html)  **
  - **Description:** Grants permission to describe a data deletion job
  - **Resource types (\*required):** [dataDeletionJob\*](#list_personalize-resource-dataDeletionJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataInsightsJob](https://docs.aws.amazon.com/personalize/latest/dg/analyzing-data.html)  **
  - **Description:** Grants permission to describe a data insights job
  - **Resource types (\*required):** [dataInsightsJob\*](#list_personalize-resource-dataInsightsJob)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html)  **
  - **Description:** Grants permission to describe a dataset
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDatasetExportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetExportJob.html)  **
  - **Description:** Grants permission to describe a dataset export job
  - **Resource types (\*required):** [datasetExportJob\*](#list_personalize-resource-datasetExportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetGroup.html)  **
  - **Description:** Grants permission to describe a dataset group
  - **Resource types (\*required):** [datasetGroup\*](#list_personalize-resource-datasetGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetImportJob.html)  **
  - **Description:** Grants permission to describe a dataset import job
  - **Resource types (\*required):** [datasetImportJob\*](#list_personalize-resource-datasetImportJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeEventTracker.html)  **
  - **Description:** Grants permission to describe an event tracker
  - **Resource types (\*required):** [eventTracker\*](#list_personalize-resource-eventTracker)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFeatureTransformation](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeFeatureTransformation.html)  **
  - **Description:** Grants permission to describe a feature transformation
  - **Resource types (\*required):** [featureTransformation\*](#list_personalize-resource-featureTransformation)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFilter](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeFilter.html)  **
  - **Description:** Grants permission to describe a filter
  - **Resource types (\*required):** [filter\*](#list_personalize-resource-filter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeMetricAttribution.html)  **
  - **Description:** Grants permission to describe a metric attribution
  - **Resource types (\*required):** [metricAttribution\*](#list_personalize-resource-metricAttribution)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRecipe](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeRecipe.html)  **
  - **Description:** Grants permission to describe a recipe
  - **Resource types (\*required):** [recipe\*](#list_personalize-resource-recipe)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeRecommender.html)  **
  - **Description:** Grants permission to describe a recommender
  - **Resource types (\*required):** [recommender\*](#list_personalize-resource-recommender)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSchema](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSchema.html)  **
  - **Description:** Grants permission to describe a schema
  - **Resource types (\*required):** [schema\*](#list_personalize-resource-schema)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html)  **
  - **Description:** Grants permission to describe a solution
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html)  **
  - **Description:** Grants permission to describe a version of a solution
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetActionRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetActionRecommendations.html)  **
  - **Description:** Grants permission to get a list of recommended actions
  - **Resource types (\*required):** [campaign\*](#list_personalize-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataInsights](https://docs.aws.amazon.com/personalize/latest/dg/analyzing-data.html)  **
  - **Description:** Grants permission to get data insights from a data insights job
  - **Resource types (\*required):** [dataInsightsJob\*](#list_personalize-resource-dataInsightsJob)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPersonalizedRanking](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetPersonalizedRanking.html)  **
  - **Description:** Grants permission to get a re-ranked list of recommendations
  - **Resource types (\*required):** [campaign\*](#list_personalize-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html)  **
  - **Description:** Grants permission to get a list of recommendations from a campaign
  - **Resource types (\*required):** [campaign\*](#list_personalize-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolutionMetrics](https://docs.aws.amazon.com/personalize/latest/dg/API_GetSolutionMetrics.html)  **
  - **Description:** Grants permission to get metrics for a solution version
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBatchInferenceJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListBatchInferenceJobs.html)  **
  - **Description:** Grants permission to list batch inference jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBatchSegmentJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListBatchSegmentJobs.html)  **
  - **Description:** Grants permission to list batch segment jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCampaigns](https://docs.aws.amazon.com/personalize/latest/dg/API_ListCampaigns.html)  **
  - **Description:** Grants permission to list campaigns
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataDeletionJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDataDeletionJobs.html)  **
  - **Description:** Grants permission to list data deletion jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataInsightsJobs](https://docs.aws.amazon.com/personalize/latest/dg/analyzing-data.html)  **
  - **Description:** Grants permission to list data insights jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatasetExportJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetExportJobs.html)  **
  - **Description:** Grants permission to list dataset export jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatasetGroups](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetGroups.html)  **
  - **Description:** Grants permission to list dataset groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatasetImportJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetImportJobs.html)  **
  - **Description:** Grants permission to list dataset import jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatasets](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasets.html)  **
  - **Description:** Grants permission to list datasets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventTrackers](https://docs.aws.amazon.com/personalize/latest/dg/API_ListEventTrackers.html)  **
  - **Description:** Grants permission to list event trackers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFilters](https://docs.aws.amazon.com/personalize/latest/dg/API_ListFilters.html)  **
  - **Description:** Grants permission to list filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMetricAttributionMetrics](https://docs.aws.amazon.com/personalize/latest/dg/API_ListMetricAttributionMetrics.html)  **
  - **Description:** Grants permission to list metric attribution metrics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMetricAttributions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListMetricAttributions.html)  **
  - **Description:** Grants permission to list metric attributions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecipes](https://docs.aws.amazon.com/personalize/latest/dg/API_ListRecipes.html)  **
  - **Description:** Grants permission to list recipes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommenders](https://docs.aws.amazon.com/personalize/latest/dg/API_ListRecommenders.html)  **
  - **Description:** Grants permission to list recommenders
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSchemas](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSchemas.html)  **
  - **Description:** Grants permission to list schemas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html)  **
  - **Description:** Grants permission to list versions of a solution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSolutions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutions.html)  **
  - **Description:** Grants permission to list solutions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/personalize/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [batchInferenceJob](#list_personalize-resource-batchInferenceJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [batchSegmentJob](#list_personalize-resource-batchSegmentJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [campaign](#list_personalize-resource-campaign) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataDeletionJob](#list_personalize-resource-dataDeletionJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_personalize-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasetExportJob](#list_personalize-resource-datasetExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasetGroup](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasetImportJob](#list_personalize-resource-datasetImportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventTracker](#list_personalize-resource-eventTracker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [filter](#list_personalize-resource-filter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommender](#list_personalize-resource-recommender) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [solution](#list_personalize-resource-solution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutActionInteractions](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutActionInteractions.html)  **
  - **Description:** Grants permission to put real time action interaction data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutActions](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutActions.html)  **
  - **Description:** Grants permission to ingest Actions data
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutEvents](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html)  **
  - **Description:** Grants permission to put real time event data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutItems](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutItems.html)  **
  - **Description:** Grants permission to ingest Items data
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutUsers](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutUsers.html)  **
  - **Description:** Grants permission to ingest Users data
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_StartRecommender.html)  **
  - **Description:** Grants permission to start a recommender
  - **Resource types (\*required):** [recommender\*](#list_personalize-resource-recommender)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_StopRecommender.html)  **
  - **Description:** Grants permission to stop a recommender
  - **Resource types (\*required):** [recommender\*](#list_personalize-resource-recommender)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopSolutionVersionCreation](https://docs.aws.amazon.com/personalize/latest/dg/API_StopSolutionVersionCreation.html)  **
  - **Description:** Grants permission to stop a solution version creation
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/personalize/latest/dg/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [batchInferenceJob](#list_personalize-resource-batchInferenceJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [batchSegmentJob](#list_personalize-resource-batchSegmentJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [campaign](#list_personalize-resource-campaign) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [dataDeletionJob](#list_personalize-resource-dataDeletionJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_personalize-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetExportJob](#list_personalize-resource-datasetExportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetGroup](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetImportJob](#list_personalize-resource-datasetImportJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [eventTracker](#list_personalize-resource-eventTracker) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [filter](#list_personalize-resource-filter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [recommender](#list_personalize-resource-recommender) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [solution](#list_personalize-resource-solution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_personalize-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/personalize/latest/dg/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [batchInferenceJob](#list_personalize-resource-batchInferenceJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [batchSegmentJob](#list_personalize-resource-batchSegmentJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [campaign](#list_personalize-resource-campaign) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [dataDeletionJob](#list_personalize-resource-dataDeletionJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_personalize-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetExportJob](#list_personalize-resource-datasetExportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetGroup](#list_personalize-resource-datasetGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [datasetImportJob](#list_personalize-resource-datasetImportJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [eventTracker](#list_personalize-resource-eventTracker) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [filter](#list_personalize-resource-filter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [recommender](#list_personalize-resource-recommender) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Resource types (\*required):** [solution](#list_personalize-resource-solution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_personalize-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateCampaign.html)  **
  - **Description:** Grants permission to update a campaign
  - **Resource types (\*required):** [campaign\*](#list_personalize-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateDataset.html)  **
  - **Description:** Grants permission to update a dataset
  - **Resource types (\*required):** [dataset\*](#list_personalize-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateMetricAttribution.html)  **
  - **Description:** Grants permission to update a metric attribution
  - **Resource types (\*required):** [metricAttribution\*](#list_personalize-resource-metricAttribution)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateRecommender.html)  **
  - **Description:** Grants permission to update a recommender
  - **Resource types (\*required):** [recommender\*](#list_personalize-resource-recommender)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html)  **
  - **Description:** Grants permission to update a solution
  - **Resource types (\*required):** [solution\*](#list_personalize-resource-solution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Personalize
<a name="list_personalize-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [algorithm](https://docs.aws.amazon.com/personalize/latest/dg/API_Algorithm.html)  | arn:${Partition}:personalize:::algorithm/${ResourceId} |   | 
|  [batchInferenceJob](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchInferenceJob.html)  | arn:${Partition}:personalize:${Region}:${Account}:batch-inference-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [batchSegmentJob](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchSegmentJob.html)  | arn:${Partition}:personalize:${Region}:${Account}:batch-segment-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [campaign](https://docs.aws.amazon.com/personalize/latest/dg/API_Campaign.html)  | arn:${Partition}:personalize:${Region}:${Account}:campaign/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [dataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DataDeletionJob.html)  | arn:${Partition}:personalize:${Region}:${Account}:data-deletion-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [dataInsightsJob](https://docs.aws.amazon.com/personalize/latest/dg/analyzing-data.html)  | arn:${Partition}:personalize:${Region}:${Account}:data-insights-job/${ResourceId} |   | 
|  [dataset](https://docs.aws.amazon.com/personalize/latest/dg/API_Dataset.html)  | arn:${Partition}:personalize:${Region}:${Account}:dataset/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [datasetExportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetExportJob.html)  | arn:${Partition}:personalize:${Region}:${Account}:dataset-export-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [datasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetGroup.html)  | arn:${Partition}:personalize:${Region}:${Account}:dataset-group/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [datasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetImportJob.html)  | arn:${Partition}:personalize:${Region}:${Account}:dataset-import-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [eventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_EventTracker.html)  | arn:${Partition}:personalize:${Region}:${Account}:event-tracker/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [featureTransformation](https://docs.aws.amazon.com/personalize/latest/dg/API_FeatureTransformation.html)  | arn:${Partition}:personalize:::feature-transformation/${ResourceId} |   | 
|  [filter](https://docs.aws.amazon.com/personalize/latest/dg/API_Filter.html)  | arn:${Partition}:personalize:${Region}:${Account}:filter/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [metricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_MetricAttribution.html)  | arn:${Partition}:personalize:${Region}:${Account}:metric-attribution/${ResourceId} |   | 
|  [recipe](https://docs.aws.amazon.com/personalize/latest/dg/API_Recipe.html)  | arn:${Partition}:personalize:::recipe/${ResourceId} |   | 
|  [recommender](https://docs.aws.amazon.com/personalize/latest/dg/API_Recommender.html)  | arn:${Partition}:personalize:${Region}:${Account}:recommender/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 
|  [schema](https://docs.aws.amazon.com/personalize/latest/dg/how-it-works-dataset-schema.html#schema-examples)  | arn:${Partition}:personalize:${Region}:${Account}:schema/${ResourceId} |   | 
|  [solution](https://docs.aws.amazon.com/personalize/latest/dg/API_Solution.html)  | arn:${Partition}:personalize:${Region}:${Account}:solution/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_personalize-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Personalize
<a name="list_personalize-policy-keys"></a>

Amazon Personalize defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 