

# Actions, resources, and condition keys for AWS Database Migration Service
<a name="list_dms"></a>

AWS Database Migration Service (service prefix: `dms`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/dms/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/dms/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/dms/dms.json) for this service.

**Topics**
+ [API operations defined by AWS Database Migration Service](#list_dms-operations)
+ [Actions defined by AWS Database Migration Service](#list_dms-actions-as-permissions)
+ [Permission-only actions for AWS Database Migration Service](#list_dms-permission-only-actions)
+ [Resource types defined by AWS Database Migration Service](#list_dms-resources-for-iam-policies)
+ [Condition keys for AWS Database Migration Service](#list_dms-policy-keys)

## API operations defined by AWS Database Migration Service
<a name="list_dms-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_dms-actions-as-permissions).




- **   AddTagsToResource  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ApplyPendingMaintenanceAction  **
  - **IAM action:**  [dms:ApplyPendingMaintenanceAction](#list_dms-action-ApplyPendingMaintenanceAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchStartRecommendations  **
  - **IAM action:**  [dms:BatchStartRecommendations](#list_dms-action-BatchStartRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelMetadataModelConversion  **
  - **IAM action:**  [dms:CancelMetadataModelConversion](#list_dms-action-CancelMetadataModelConversion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelMetadataModelCreation  **
  - **IAM action:**  [dms:CancelMetadataModelCreation](#list_dms-action-CancelMetadataModelCreation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelReplicationTaskAssessmentRun  **
  - **IAM action:**  [dms:CancelReplicationTaskAssessmentRun](#list_dms-action-CancelReplicationTaskAssessmentRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataMigration  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateDataMigration](#list_dms-action-CreateDataMigration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   CreateDataProvider  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateDataProvider](#list_dms-action-CreateDataProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   CreateEndpoint  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateEndpoint](#list_dms-action-CreateEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   CreateEventSubscription  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateEventSubscription](#list_dms-action-CreateEventSubscription)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateFleetAdvisorCollector  **
  - **IAM action:**  [dms:CreateFleetAdvisorCollector](#list_dms-action-CreateFleetAdvisorCollector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   CreateInstanceProfile  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateInstanceProfile](#list_dms-action-CreateInstanceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateMigrationProject  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateMigrationProject](#list_dms-action-CreateMigrationProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   CreateReplicationConfig  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateReplicationConfig](#list_dms-action-CreateReplicationConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateReplicationInstance  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateReplicationInstance](#list_dms-action-CreateReplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   CreateReplicationSubnetGroup  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateReplicationSubnetGroup](#list_dms-action-CreateReplicationSubnetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateReplicationTask  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:CreateReplicationTask](#list_dms-action-CreateReplicationTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteCertificate  **
  - **IAM action:**  [dms:DeleteCertificate](#list_dms-action-DeleteCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnection  **
  - **IAM action:**  [dms:DeleteConnection](#list_dms-action-DeleteConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataMigration  **
  - **IAM action:**  [dms:DeleteDataMigration](#list_dms-action-DeleteDataMigration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataProvider  **
  - **IAM action:**  [dms:DeleteDataProvider](#list_dms-action-DeleteDataProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpoint  **
  - **IAM action:**  [dms:DeleteEndpoint](#list_dms-action-DeleteEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventSubscription  **
  - **IAM action:**  [dms:DeleteEventSubscription](#list_dms-action-DeleteEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleetAdvisorCollector  **
  - **IAM action:**  [dms:DeleteFleetAdvisorCollector](#list_dms-action-DeleteFleetAdvisorCollector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleetAdvisorDatabases  **
  - **IAM action:**  [dms:DeleteFleetAdvisorDatabases](#list_dms-action-DeleteFleetAdvisorDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInstanceProfile  **
  - **IAM action:**  [dms:DeleteInstanceProfile](#list_dms-action-DeleteInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMigrationProject  **
  - **IAM action:**  [dms:DeleteMigrationProject](#list_dms-action-DeleteMigrationProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationConfig  **
  - **IAM action:**  [dms:DeleteReplicationConfig](#list_dms-action-DeleteReplicationConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationInstance  **
  - **IAM action:**  [dms:DeleteReplicationInstance](#list_dms-action-DeleteReplicationInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationSubnetGroup  **
  - **IAM action:**  [dms:DeleteReplicationSubnetGroup](#list_dms-action-DeleteReplicationSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationTask  **
  - **IAM action:**  [dms:DeleteReplicationTask](#list_dms-action-DeleteReplicationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationTaskAssessmentRun  **
  - **IAM action:**  [dms:DeleteReplicationTaskAssessmentRun](#list_dms-action-DeleteReplicationTaskAssessmentRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountAttributes  **
  - **IAM action:**  [dms:DescribeAccountAttributes](#list_dms-action-DescribeAccountAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApplicableIndividualAssessments  **
  - **IAM action:**  [dms:DescribeApplicableIndividualAssessments](#list_dms-action-DescribeApplicableIndividualAssessments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCertificates  **
  - **IAM action:**  [dms:DescribeCertificates](#list_dms-action-DescribeCertificates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnections  **
  - **IAM action:**  [dms:DescribeConnections](#list_dms-action-DescribeConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConversionConfiguration  **
  - **IAM action:**  [dms:DescribeConversionConfiguration](#list_dms-action-DescribeConversionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataMigrations  **
  - **IAM action:**  [dms:DescribeDataMigrations](#list_dms-action-DescribeDataMigrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataProviders  **
  - **IAM action:**  [dms:ListDataProviders](#list_dms-action-ListDataProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpointSettings  **
  - **IAM action:**  [dms:DescribeEndpointSettings](#list_dms-action-DescribeEndpointSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpointTypes  **
  - **IAM action:**  [dms:DescribeEndpointTypes](#list_dms-action-DescribeEndpointTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoints  **
  - **IAM action:**  [dms:DescribeEndpoints](#list_dms-action-DescribeEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEngineVersions  **
  - **IAM action:**  [dms:DescribeEngineVersions](#list_dms-action-DescribeEngineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventCategories  **
  - **IAM action:**  [dms:DescribeEventCategories](#list_dms-action-DescribeEventCategories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventSubscriptions  **
  - **IAM action:**  [dms:DescribeEventSubscriptions](#list_dms-action-DescribeEventSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEvents  **
  - **IAM action:**  [dms:DescribeEvents](#list_dms-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExtensionPackAssociations  **
  - **IAM action:**  [dms:ListExtensionPacks](#list_dms-action-ListExtensionPacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetAdvisorCollectors  **
  - **IAM action:**  [dms:DescribeFleetAdvisorCollectors](#list_dms-action-DescribeFleetAdvisorCollectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetAdvisorDatabases  **
  - **IAM action:**  [dms:DescribeFleetAdvisorDatabases](#list_dms-action-DescribeFleetAdvisorDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetAdvisorLsaAnalysis  **
  - **IAM action:**  [dms:DescribeFleetAdvisorLsaAnalysis](#list_dms-action-DescribeFleetAdvisorLsaAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetAdvisorSchemaObjectSummary  **
  - **IAM action:**  [dms:DescribeFleetAdvisorSchemaObjectSummary](#list_dms-action-DescribeFleetAdvisorSchemaObjectSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFleetAdvisorSchemas  **
  - **IAM action:**  [dms:DescribeFleetAdvisorSchemas](#list_dms-action-DescribeFleetAdvisorSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstanceProfiles  **
  - **IAM action:**  [dms:ListInstanceProfiles](#list_dms-action-ListInstanceProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetadataModel  **
  - **IAM action:**  [dms:DescribeMetadataModel](#list_dms-action-DescribeMetadataModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetadataModelAssessments  **
  - **IAM action:**  [dms:ListMetadataModelAssessments](#list_dms-action-ListMetadataModelAssessments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetadataModelChildren  **
  - **IAM action:**  [dms:DescribeMetadataModelChildren](#list_dms-action-DescribeMetadataModelChildren) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetadataModelConversions  **
  - **IAM action:**  [dms:ListMetadataModelConversions](#list_dms-action-ListMetadataModelConversions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetadataModelCreations  **
  - **IAM action:**  [dms:DescribeMetadataModelCreations](#list_dms-action-DescribeMetadataModelCreations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetadataModelExportsAsScript  **
  - **IAM action:**  [dms:ListMetadataModelExports](#list_dms-action-ListMetadataModelExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetadataModelExportsToTarget  **
  - **IAM action:**  [dms:ListMetadataModelExports](#list_dms-action-ListMetadataModelExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMetadataModelImports  **
  - **IAM action:**  [dms:DescribeMetadataModelImports](#list_dms-action-DescribeMetadataModelImports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMigrationProjects  **
  - **IAM action:**  [dms:ListMigrationProjects](#list_dms-action-ListMigrationProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrderableReplicationInstances  **
  - **IAM action:**  [dms:DescribeOrderableReplicationInstances](#list_dms-action-DescribeOrderableReplicationInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePendingMaintenanceActions  **
  - **IAM action:**  [dms:DescribePendingMaintenanceActions](#list_dms-action-DescribePendingMaintenanceActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecommendationLimitations  **
  - **IAM action:**  [dms:DescribeRecommendationLimitations](#list_dms-action-DescribeRecommendationLimitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecommendations  **
  - **IAM action:**  [dms:DescribeRecommendations](#list_dms-action-DescribeRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRefreshSchemasStatus  **
  - **IAM action:**  [dms:DescribeRefreshSchemasStatus](#list_dms-action-DescribeRefreshSchemasStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationConfigs  **
  - **IAM action:**  [dms:DescribeReplicationConfigs](#list_dms-action-DescribeReplicationConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationInstanceTaskLogs  **
  - **IAM action:**  [dms:DescribeReplicationInstanceTaskLogs](#list_dms-action-DescribeReplicationInstanceTaskLogs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationInstances  **
  - **IAM action:**  [dms:DescribeReplicationInstances](#list_dms-action-DescribeReplicationInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationSubnetGroups  **
  - **IAM action:**  [dms:DescribeReplicationSubnetGroups](#list_dms-action-DescribeReplicationSubnetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationTableStatistics  **
  - **IAM action:**  [dms:DescribeReplicationTableStatistics](#list_dms-action-DescribeReplicationTableStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationTaskAssessmentResults  **
  - **IAM action:**  [dms:DescribeReplicationTaskAssessmentResults](#list_dms-action-DescribeReplicationTaskAssessmentResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationTaskAssessmentRuns  **
  - **IAM action:**  [dms:DescribeReplicationTaskAssessmentRuns](#list_dms-action-DescribeReplicationTaskAssessmentRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationTaskIndividualAssessments  **
  - **IAM action:**  [dms:DescribeReplicationTaskIndividualAssessments](#list_dms-action-DescribeReplicationTaskIndividualAssessments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationTasks  **
  - **IAM action:**  [dms:DescribeReplicationTasks](#list_dms-action-DescribeReplicationTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplications  **
  - **IAM action:**  [dms:DescribeReplications](#list_dms-action-DescribeReplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSchemas  **
  - **IAM action:**  [dms:DescribeSchemas](#list_dms-action-DescribeSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTableStatistics  **
  - **IAM action:**  [dms:DescribeTableStatistics](#list_dms-action-DescribeTableStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ExportMetadataModelAssessment  **
  - **IAM action:**  [dms:ExportMetadataModelAssessment](#list_dms-action-ExportMetadataModelAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetTargetSelectionRules  **
  - **IAM action:**  [dms:GetTargetSelectionRules](#list_dms-action-GetTargetSelectionRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportCertificate  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:ImportCertificate](#list_dms-action-ImportCertificate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ListTagsForResource  **
  - **IAM action:**  [dms:ListTagsForResource](#list_dms-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyConversionConfiguration  **
  - **IAM action:**  [dms:UpdateConversionConfiguration](#list_dms-action-UpdateConversionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyDataMigration  **
  - **IAM action:**  [dms:ModifyDataMigration](#list_dms-action-ModifyDataMigration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   ModifyDataProvider  **
  - **IAM action:**  [dms:UpdateDataProvider](#list_dms-action-UpdateDataProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   ModifyEndpoint  **
  - **IAM action:**  [dms:ModifyEndpoint](#list_dms-action-ModifyEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   ModifyEventSubscription  **
  - **IAM action:**  [dms:ModifyEventSubscription](#list_dms-action-ModifyEventSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyInstanceProfile  **
  - **IAM action:**  [dms:UpdateInstanceProfile](#list_dms-action-UpdateInstanceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyMigrationProject  **
  - **IAM action:**  [dms:UpdateMigrationProject](#list_dms-action-UpdateMigrationProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   ModifyReplicationConfig  **
  - **IAM action:**  [dms:ModifyReplicationConfig](#list_dms-action-ModifyReplicationConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyReplicationInstance  **
  - **IAM action:**  [dms:ModifyReplicationInstance](#list_dms-action-ModifyReplicationInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   ModifyReplicationSubnetGroup  **
  - **IAM action:**  [dms:ModifyReplicationSubnetGroup](#list_dms-action-ModifyReplicationSubnetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyReplicationTask  **
  - **IAM action:**  [dms:ModifyReplicationTask](#list_dms-action-ModifyReplicationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   MoveReplicationTask  **
  - **IAM action:**  [dms:MoveReplicationTask](#list_dms-action-MoveReplicationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootReplicationInstance  **
  - **IAM action:**  [dms:RebootReplicationInstance](#list_dms-action-RebootReplicationInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RefreshSchemas  **
  - **IAM action:**  [dms:RefreshSchemas](#list_dms-action-RefreshSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReloadReplicationTables  **
  - **IAM action:**  [dms:ReloadReplicationTables](#list_dms-action-ReloadReplicationTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReloadTables  **
  - **IAM action:**  [dms:ReloadTables](#list_dms-action-ReloadTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromResource  **
  - **IAM action:**  [dms:RemoveTagsFromResource](#list_dms-action-RemoveTagsFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   RunFleetAdvisorLsaAnalysis  **
  - **IAM action:**  [dms:RunFleetAdvisorLsaAnalysis](#list_dms-action-RunFleetAdvisorLsaAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDataMigration  **
  - **IAM action:**  [dms:StartDataMigration](#list_dms-action-StartDataMigration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartExtensionPackAssociation  **
  - **IAM action:**  [dms:AssociateExtensionPack](#list_dms-action-AssociateExtensionPack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetadataModelAssessment  **
  - **IAM action:**  [dms:StartMetadataModelAssessment](#list_dms-action-StartMetadataModelAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetadataModelConversion  **
  - **IAM action:**  [dms:StartMetadataModelConversion](#list_dms-action-StartMetadataModelConversion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetadataModelCreation  **
  - **IAM action:**  [dms:StartMetadataModelCreation](#list_dms-action-StartMetadataModelCreation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetadataModelExportAsScript  **
  - **IAM action:**  [dms:StartMetadataModelExportAsScripts](#list_dms-action-StartMetadataModelExportAsScripts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetadataModelExportToTarget  **
  - **IAM action:**  [dms:StartMetadataModelExportToTarget](#list_dms-action-StartMetadataModelExportToTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMetadataModelImport  **
  - **IAM action:**  [dms:StartMetadataModelImport](#list_dms-action-StartMetadataModelImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRecommendations  **
  - **IAM action:**  [dms:StartRecommendations](#list_dms-action-StartRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartReplication  **
  - **IAM action:**  [dms:StartReplication](#list_dms-action-StartReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartReplicationTask  **
  - **IAM action:**  [dms:StartReplicationTask](#list_dms-action-StartReplicationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartReplicationTaskAssessment  **
  - **IAM action:**  [dms:StartReplicationTaskAssessment](#list_dms-action-StartReplicationTaskAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartReplicationTaskAssessmentRun  **
  - **IAM action:**  [dms:AddTagsToResource](#list_dms-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [dms:StartReplicationTaskAssessmentRun](#list_dms-action-StartReplicationTaskAssessmentRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dms.amazonaws.com / **Access level:** Write

- **   StopDataMigration  **
  - **IAM action:**  [dms:StopDataMigration](#list_dms-action-StopDataMigration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopReplication  **
  - **IAM action:**  [dms:StopReplication](#list_dms-action-StopReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopReplicationTask  **
  - **IAM action:**  [dms:StopReplicationTask](#list_dms-action-StopReplicationTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestConnection  **
  - **IAM action:**  [dms:TestConnection](#list_dms-action-TestConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UpdateSubscriptionsToEventBridge  **
  - **IAM action:**  [dms:UpdateSubscriptionsToEventBridge](#list_dms-action-UpdateSubscriptionsToEventBridge) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Database Migration Service
<a name="list_dms-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTagsToResource](https://docs.aws.amazon.com/dms/latest/APIReference/API_AddTagsToResource.html)  **
  - **Description:** Grants permission to add metadata tags to DMS resources, including replication instances, endpoints, security groups, and migration tasks
  - **Resource types (\*required):** [Certificate](#list_dms-resource-Certificate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:cert-tag/${TagKey}](#list_dms-dms_cert-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [DataMigration](#list_dms-resource-DataMigration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:data-migration-tag/${TagKey}](#list_dms-dms_data-migration-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [DataProvider](#list_dms-resource-DataProvider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:data-provider-tag/${TagKey}](#list_dms-dms_data-provider-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [Endpoint](#list_dms-resource-Endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [EventSubscription](#list_dms-resource-EventSubscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:es-tag/${TagKey}](#list_dms-dms_es-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [InstanceProfile](#list_dms-resource-InstanceProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [MigrationProject](#list_dms-resource-MigrationProject) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationConfig](#list_dms-resource-ReplicationConfig) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationInstance](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationSubnetGroup](#list_dms-resource-ReplicationSubnetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)<br />[dms:subgrp-tag/${TagKey}](#list_dms-dms_subgrp-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTask](#list_dms-resource-ReplicationTask) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTaskAssessmentRun](#list_dms-resource-ReplicationTaskAssessmentRun) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:assessment-run-tag/${TagKey}](#list_dms-dms_assessment-run-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTaskIndividualAssessment](#list_dms-resource-ReplicationTaskIndividualAssessment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:individual-assessment-tag/${TagKey}](#list_dms-dms_individual-assessment-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Tagging, Write

- **   [ApplyPendingMaintenanceAction](https://docs.aws.amazon.com/dms/latest/APIReference/API_ApplyPendingMaintenanceAction.html)  **
  - **Description:** Grants permission to apply a pending maintenance action to a resource (for example, to a replication instance)
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Access level:** Write

- **   [AssociateExtensionPack](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartExtensionPackAssociation.html)  **
  - **Description:** Grants permission to associate a extension pack
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [BatchStartRecommendations](https://docs.aws.amazon.com/dms/latest/APIReference/API_BatchStartRecommendations.html)  **
  - **Description:** Grants permission to start the analysis of up to 20 source databases to recommend target engines for each source database
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelMetadataModelConversion](https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelConversion.html)  **
  - **Description:** Grants permission to cancel a single metadata model conversion operation that was started with StartMetadataModelConversion
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [CancelMetadataModelCreation](https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelCreation.html)  **
  - **Description:** Grants permission to cancel a single metadata model creation operation that was started with StartMetadataModelCreation
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [CancelReplicationTaskAssessmentRun](https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelReplicationTaskAssessmentRun.html)  **
  - **Description:** Grants permission to cancel a single premigration assessment run
  - **Resource types (\*required):** [ReplicationTaskAssessmentRun\*](#list_dms-resource-ReplicationTaskAssessmentRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:assessment-run-tag/${TagKey}](#list_dms-dms_assessment-run-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDataMigration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to create a database migration using the provided settings
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateDataProvider](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateDataProvider.html)  **
  - **Description:** Grants permission to create a data provider using the provided settings
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateEndpoint](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateEndpoint.html)  **
  - **Description:** Grants permission to create an endpoint using the provided settings
  - **Resource types (\*required):** [Certificate](#list_dms-resource-Certificate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:cert-tag/${TagKey}](#list_dms-dms_cert-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateEventSubscription](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateEventSubscription.html)  **
  - **Description:** Grants permission to create an AWS DMS event notification subscription
  - **Resource types (\*required):** [EventSubscription\*](#list_dms-resource-EventSubscription)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:es-tag/${TagKey}](#list_dms-dms_es-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateFleetAdvisorCollector](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateFleetAdvisorCollector.html)  **
  - **Description:** Grants permission to create a Fleet Advisor collector using the specified parameters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateInstanceProfile](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateInstanceProfile.html)  **
  - **Description:** Grants permission to create an instance profile using the provided settings
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateMigrationProject](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateMigrationProject.html)  **
  - **Description:** Grants permission to create a migration project using the provided settings
  - **Resource types (\*required):** [DataProvider\*](#list_dms-resource-DataProvider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:data-provider-tag/${TagKey}](#list_dms-dms_data-provider-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [InstanceProfile\*](#list_dms-resource-InstanceProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateReplicationConfig](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to create a replication config using the provided settings
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [CreateReplicationInstance](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationInstance.html)  **
  - **Description:** Grants permission to create a replication instance using the specified parameters
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationSubnetGroup](#list_dms-resource-ReplicationSubnetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)<br />[dms:subgrp-tag/${TagKey}](#list_dms-dms_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [CreateReplicationSubnetGroup](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationSubnetGroup.html)  **
  - **Description:** Grants permission to create a replication subnet group given a list of the subnet IDs in a VPC
  - **Resource types (\*required):** [ReplicationSubnetGroup\*](#list_dms-resource-ReplicationSubnetGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)<br />[dms:subgrp-tag/${TagKey}](#list_dms-dms_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [CreateReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html)  **
  - **Description:** Grants permission to create a replication task using the specified parameters
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteCertificate](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteCertificate.html)  **
  - **Description:** Grants permission to delete the specified certificate
  - **Resource types (\*required):** [Certificate\*](#list_dms-resource-Certificate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:cert-tag/${TagKey}](#list_dms-dms_cert-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteConnection.html)  **
  - **Description:** Grants permission to delete the specified connection between a replication instance and an endpoint
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataMigration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to delete the specified database migration
  - **Resource types (\*required):** [DataMigration\*](#list_dms-resource-DataMigration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-migration-tag/${TagKey}](#list_dms-dms_data-migration-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataProvider](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteDataProvider.html)  **
  - **Description:** Grants permission to delete the specified data provider
  - **Resource types (\*required):** [DataProvider\*](#list_dms-resource-DataProvider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-provider-tag/${TagKey}](#list_dms-dms_data-provider-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteEndpoint](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteEndpoint.html)  **
  - **Description:** Grants permission to delete the specified endpoint
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventSubscription](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteEventSubscription.html)  **
  - **Description:** Grants permission to delete an AWS DMS event subscription
  - **Resource types (\*required):** [EventSubscription\*](#list_dms-resource-EventSubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:es-tag/${TagKey}](#list_dms-dms_es-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteFleetAdvisorCollector](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteFleetAdvisorCollector.html)  **
  - **Description:** Grants permission to delete the specified Fleet Advisor collector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFleetAdvisorDatabases](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteFleetAdvisorDatabases.html)  **
  - **Description:** Grants permission to delete the specified Fleet Advisor databases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInstanceProfile](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteInstanceProfile.html)  **
  - **Description:** Grants permission to delete the specified instance profile
  - **Resource types (\*required):** [InstanceProfile\*](#list_dms-resource-InstanceProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteMigrationProject](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteMigrationProject.html)  **
  - **Description:** Grants permission to delete the specified migration project
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationConfig](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to delete the specified replication config
  - **Resource types (\*required):** [ReplicationConfig\*](#list_dms-resource-ReplicationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationInstance](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationInstance.html)  **
  - **Description:** Grants permission to delete the specified replication instance
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationSubnetGroup](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationSubnetGroup.html)  **
  - **Description:** Grants permission to delete a subnet group
  - **Resource types (\*required):** [ReplicationSubnetGroup\*](#list_dms-resource-ReplicationSubnetGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:subgrp-tag/${TagKey}](#list_dms-dms_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask.html)  **
  - **Description:** Grants permission to delete the specified replication task
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationTaskAssessmentRun](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTaskAssessmentRun.html)  **
  - **Description:** Grants permission to delete the record of a single premigration assessment run
  - **Resource types (\*required):** [ReplicationTaskAssessmentRun\*](#list_dms-resource-ReplicationTaskAssessmentRun)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:assessment-run-tag/${TagKey}](#list_dms-dms_assessment-run-tag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccountAttributes](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeAccountAttributes.html)  **
  - **Description:** Grants permission to list all of the AWS DMS attributes for a customer account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeApplicableIndividualAssessments](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeApplicableIndividualAssessments.html)  **
  - **Description:** Grants permission to list individual assessments that you can specify for a new premigration assessment run
  - **Resource types (\*required):** [ReplicationInstance](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTask](#list_dms-resource-ReplicationTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeCertificates](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeCertificates.html)  **
  - **Description:** Grants permission to provide a description of the certificate
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConnections](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConnections.html)  **
  - **Description:** Grants permission to describe the status of the connections that have been made between the replication instance and an endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html)  **
  - **Description:** Grants permission to return information about DMS Schema Conversion project configuration
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataMigrations](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to return information about database migrations for your account in the specified region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEndpointSettings](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEndpointSettings.html)  **
  - **Description:** Grants permission to return the possible endpoint settings available when you create an endpoint for a specific database engine
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEndpointTypes](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEndpointTypes.html)  **
  - **Description:** Grants permission to return information about the type of endpoints available
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEndpoints](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEndpoints.html)  **
  - **Description:** Grants permission to return information about the endpoints for your account in the current region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEngineVersions](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEngineVersions.html)  **
  - **Description:** Grants permission to return information about the available versions for DMS replication instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventCategories](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEventCategories.html)  **
  - **Description:** Grants permission to list categories for all event source types, or, if specified, for a specified source type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventSubscriptions](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEventSubscriptions.html)  **
  - **Description:** Grants permission to list all the event subscriptions for a customer account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEvents](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEvents.html)  **
  - **Description:** Grants permission to list events for a given source identifier and source type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetAdvisorCollectors](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorCollectors.html)  **
  - **Description:** Grants permission to return a paginated list of Fleet Advisor collectors in your account based on filter settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetAdvisorDatabases](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorDatabases.html)  **
  - **Description:** Grants permission to return a paginated list of Fleet Advisor databases in your account based on filter settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetAdvisorLsaAnalysis](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorLsaAnalysis.html)  **
  - **Description:** Grants permission to return a paginated list of descriptions of large-scale assessment (LSA) analyses produced by your Fleet Advisor collectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetAdvisorSchemaObjectSummary](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorSchemaObjectSummary.html)  **
  - **Description:** Grants permission to return a paginated list of descriptions of schemas discovered by your Fleet Advisor collectors based on filter settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFleetAdvisorSchemas](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorSchemas.html)  **
  - **Description:** Grants permission to return a paginated list of schemas discovered by your Fleet Advisor collectors based on filter settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMetadataModel](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModel.html)  **
  - **Description:** Grants permission to get detailed information about the specified metadata model, including its definition and corresponding converted objects in the target database if applicable
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeMetadataModelChildren](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelChildren.html)  **
  - **Description:** Grants permission to get a list of child metadata models for the specified metadata model in the database hierarchy
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeMetadataModelCreations](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelCreations.html)  **
  - **Description:** Grants permission to return a paginated list of metadata model creation requests for a migration project
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeMetadataModelImports](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelImports.html)  **
  - **Description:** Grants permission to return information about start metadata model import operations for a migration project
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeOrderableReplicationInstances](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeOrderableReplicationInstances.html)  **
  - **Description:** Grants permission to return information about the replication instance types that can be created in the specified region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePendingMaintenanceActions](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribePendingMaintenanceActions.html)  **
  - **Description:** Grants permission to return information about pending maintenance actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRecommendationLimitations](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorLsaAnalysis.html)  **
  - **Description:** Grants permission to return a paginated list of descriptions of limitations for recommendations of target AWS engines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRecommendations](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeRecommendations.html)  **
  - **Description:** Grants permission to return a paginated list of descriptions of target engine recommendations for your source databases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRefreshSchemasStatus](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeRefreshSchemasStatus.html)  **
  - **Description:** Grants permission to return the status of the RefreshSchemas operation
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeReplicationConfigs](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to describe replication configs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReplicationInstanceTaskLogs](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationInstanceTaskLogs.html)  **
  - **Description:** Grants permission to return information about the task logs for the specified task
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeReplicationInstances](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationInstances.html)  **
  - **Description:** Grants permission to return information about replication instances for your account in the current region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReplicationSubnetGroups](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationSubnetGroups.html)  **
  - **Description:** Grants permission to return information about the replication subnet groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReplicationTableStatistics](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to describe replication table statistics
  - **Resource types (\*required):** [ReplicationConfig\*](#list_dms-resource-ReplicationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeReplicationTaskAssessmentResults](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTaskAssessmentResults.html)  **
  - **Description:** Grants permission to return the latest task assessment results from Amazon S3
  - **Resource types (\*required):** [ReplicationTask](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeReplicationTaskAssessmentRuns](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTaskAssessmentRuns.html)  **
  - **Description:** Grants permission to return a paginated list of premigration assessment runs based on filter settings
  - **Resource types (\*required):** [ReplicationInstance](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTask](#list_dms-resource-ReplicationTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTaskAssessmentRun](#list_dms-resource-ReplicationTaskAssessmentRun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:assessment-run-tag/${TagKey}](#list_dms-dms_assessment-run-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeReplicationTaskIndividualAssessments](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTaskIndividualAssessments.html)  **
  - **Description:** Grants permission to return a paginated list of individual assessments based on filter settings
  - **Resource types (\*required):** [ReplicationTask](#list_dms-resource-ReplicationTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTaskAssessmentRun](#list_dms-resource-ReplicationTaskAssessmentRun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:assessment-run-tag/${TagKey}](#list_dms-dms_assessment-run-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeReplicationTasks](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTasks.html)  **
  - **Description:** Grants permission to return information about replication tasks for your account in the current region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReplications](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to describe replications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSchemas](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeSchemas.html)  **
  - **Description:** Grants permission to return information about the schema for the specified endpoint
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Access level:** Read

- **   [DescribeTableStatistics](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeTableStatistics.html)  **
  - **Description:** Grants permission to return table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Read

- **   [ExportMetadataModelAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_ExportMetadataModelAssessment.html)  **
  - **Description:** Grants permission to export the specified metadata model assessment
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [GetTargetSelectionRules](https://docs.aws.amazon.com/dms/latest/APIReference/API_GetTargetSelectionRules.html)  **
  - **Description:** Grants permission to convert source selection rules into their target counterparts for schema conversion operations
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [ImportCertificate](https://docs.aws.amazon.com/dms/latest/APIReference/API_ImportCertificate.html)  **
  - **Description:** Grants permission to upload the specified certificate
  - **Resource types (\*required):** [Certificate\*](#list_dms-resource-Certificate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:cert-tag/${TagKey}](#list_dms-dms_cert-tag___TagKey_)
  - **Access level:** Write

- **   [ListDataProviders](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeDataProviders.html)  **
  - **Description:** Grants permission to list the AWS DMS attributes for data providers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExtensionPacks](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeExtensionPackAssociations.html)  **
  - **Description:** Grants permission to list the AWS DMS attributes for extension packs
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [ListInstanceProfiles](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeInstanceProfiles.html)  **
  - **Description:** Grants permission to list the AWS DMS attributes for instance profiles
  - **Resource types (\*required):** [InstanceProfile](#list_dms-resource-InstanceProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_)
  - **Access level:** Read

- **   [ListMetadataModelAssessments](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelAssessments.html)  **
  - **Description:** Grants permission to list the AWS DMS attributes for a metadata model assessments
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [ListMetadataModelConversions](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelConversions.html)  **
  - **Description:** Grants permission to list the AWS DMS attributes for a metadata model conversions
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [ListMetadataModelExports](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to list the AWS DMS attributes for a metadata model exports
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [ListMigrationProjects](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to list the AWS DMS attributes for a migration projects
  - **Resource types (\*required):** [DataProvider](#list_dms-resource-DataProvider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-provider-tag/${TagKey}](#list_dms-dms_data-provider-tag___TagKey_)
  - **Resource types (\*required):** [InstanceProfile](#list_dms-resource-InstanceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_)
  - **Resource types (\*required):** [MigrationProject](#list_dms-resource-MigrationProject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/dms/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for an AWS DMS resource
  - **Resource types (\*required):** [Certificate](#list_dms-resource-Certificate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:cert-tag/${TagKey}](#list_dms-dms_cert-tag___TagKey_)
  - **Resource types (\*required):** [DataMigration](#list_dms-resource-DataMigration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-migration-tag/${TagKey}](#list_dms-dms_data-migration-tag___TagKey_)
  - **Resource types (\*required):** [DataProvider](#list_dms-resource-DataProvider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-provider-tag/${TagKey}](#list_dms-dms_data-provider-tag___TagKey_)
  - **Resource types (\*required):** [Endpoint](#list_dms-resource-Endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Resource types (\*required):** [EventSubscription](#list_dms-resource-EventSubscription) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:es-tag/${TagKey}](#list_dms-dms_es-tag___TagKey_)
  - **Resource types (\*required):** [InstanceProfile](#list_dms-resource-InstanceProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_)
  - **Resource types (\*required):** [MigrationProject](#list_dms-resource-MigrationProject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationConfig](#list_dms-resource-ReplicationConfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationInstance](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationSubnetGroup](#list_dms-resource-ReplicationSubnetGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:subgrp-tag/${TagKey}](#list_dms-dms_subgrp-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTask](#list_dms-resource-ReplicationTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTaskAssessmentRun](#list_dms-resource-ReplicationTaskAssessmentRun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:assessment-run-tag/${TagKey}](#list_dms-dms_assessment-run-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTaskIndividualAssessment](#list_dms-resource-ReplicationTaskIndividualAssessment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:individual-assessment-tag/${TagKey}](#list_dms-dms_individual-assessment-tag___TagKey_)
  - **Access level:** Read

- **   [ModifyDataMigration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to modify the specified database migration
  - **Resource types (\*required):** [DataMigration\*](#list_dms-resource-DataMigration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-migration-tag/${TagKey}](#list_dms-dms_data-migration-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyEndpoint](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyEndpoint.html)  **
  - **Description:** Grants permission to modify the specified endpoint
  - **Resource types (\*required):** [Certificate](#list_dms-resource-Certificate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:cert-tag/${TagKey}](#list_dms-dms_cert-tag___TagKey_)
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyEventSubscription](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyEventSubscription.html)  **
  - **Description:** Grants permission to modify an existing AWS DMS event notification subscription
  - **Resource types (\*required):** [EventSubscription\*](#list_dms-resource-EventSubscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:es-tag/${TagKey}](#list_dms-dms_es-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyReplicationConfig](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to modify the specified replication config
  - **Resource types (\*required):** [ReplicationConfig\*](#list_dms-resource-ReplicationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyReplicationInstance](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationInstance.html)  **
  - **Description:** Grants permission to modify the replication instance to apply new settings
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyReplicationSubnetGroup](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationSubnetGroup.html)  **
  - **Description:** Grants permission to modify the settings for the specified replication subnet group
  - **Resource types (\*required):** [ReplicationSubnetGroup\*](#list_dms-resource-ReplicationSubnetGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:subgrp-tag/${TagKey}](#list_dms-dms_subgrp-tag___TagKey_)
  - **Access level:** Write

- **   [ModifyReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html)  **
  - **Description:** Grants permission to modify the specified replication task
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Write

- **   [MoveReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask.html)  **
  - **Description:** Grants permission to move the specified replication task to a different replication instance
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Write

- **   [RebootReplicationInstance](https://docs.aws.amazon.com/dms/latest/APIReference/API_RebootReplicationInstance.html)  **
  - **Description:** Grants permission to reboot a replication instance. Rebooting results in a momentary outage, until the replication instance becomes available again
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Access level:** Write

- **   [RefreshSchemas](https://docs.aws.amazon.com/dms/latest/APIReference/API_RefreshSchemas.html)  **
  - **Description:** Grants permission to populate the schema for the specified endpoint
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Access level:** Write

- **   [ReloadReplicationTables](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to reload the target database table with the source for a replication
  - **Resource types (\*required):** [ReplicationConfig\*](#list_dms-resource-ReplicationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)
  - **Access level:** Write

- **   [ReloadTables](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReloadTables.html)  **
  - **Description:** Grants permission to reload the target database table with the source data
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Write

- **   [RemoveTagsFromResource](https://docs.aws.amazon.com/dms/latest/APIReference/API_RemoveTagsFromResource.html)  **
  - **Description:** Grants permission to remove metadata tags from a DMS resource
  - **Resource types (\*required):** [Certificate](#list_dms-resource-Certificate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:cert-tag/${TagKey}](#list_dms-dms_cert-tag___TagKey_)
  - **Resource types (\*required):** [DataMigration](#list_dms-resource-DataMigration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:data-migration-tag/${TagKey}](#list_dms-dms_data-migration-tag___TagKey_)
  - **Resource types (\*required):** [DataProvider](#list_dms-resource-DataProvider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:data-provider-tag/${TagKey}](#list_dms-dms_data-provider-tag___TagKey_)
  - **Resource types (\*required):** [Endpoint](#list_dms-resource-Endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Resource types (\*required):** [EventSubscription](#list_dms-resource-EventSubscription) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:es-tag/${TagKey}](#list_dms-dms_es-tag___TagKey_)
  - **Resource types (\*required):** [InstanceProfile](#list_dms-resource-InstanceProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_)
  - **Resource types (\*required):** [MigrationProject](#list_dms-resource-MigrationProject) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationConfig](#list_dms-resource-ReplicationConfig) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationInstance](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationSubnetGroup](#list_dms-resource-ReplicationSubnetGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:subgrp-tag/${TagKey}](#list_dms-dms_subgrp-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTask](#list_dms-resource-ReplicationTask) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTaskAssessmentRun](#list_dms-resource-ReplicationTaskAssessmentRun) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:assessment-run-tag/${TagKey}](#list_dms-dms_assessment-run-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationTaskIndividualAssessment](#list_dms-resource-ReplicationTaskIndividualAssessment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:individual-assessment-tag/${TagKey}](#list_dms-dms_individual-assessment-tag___TagKey_)
  - **Access level:** Tagging, Write

- **   [RunFleetAdvisorLsaAnalysis](https://docs.aws.amazon.com/dms/latest/APIReference/API_RunFleetAdvisorLsaAnalysis.html)  **
  - **Description:** Grants permission to run a large-scale assessment (LSA) analysis on every Fleet Advisor collector in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartDataMigration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to start the database migration
  - **Resource types (\*required):** [DataMigration\*](#list_dms-resource-DataMigration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-migration-tag/${TagKey}](#list_dms-dms_data-migration-tag___TagKey_)
  - **Access level:** Write

- **   [StartMetadataModelAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelAssessment.html)  **
  - **Description:** Grants permission to start a new assessment of metadata model
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [StartMetadataModelConversion](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelConversion.html)  **
  - **Description:** Grants permission to start a new conversion of metadata model
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [StartMetadataModelCreation](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelCreation.html)  **
  - **Description:** Grants permission to create source metadata model of the given type with the specified properties for schema conversion operations
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [StartMetadataModelExportAsScripts](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportAsScript.html)  **
  - **Description:** Grants permission to start a new export of metadata model as script
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [StartMetadataModelExportToTarget](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportToTarget.html)  **
  - **Description:** Grants permission to start a new export of metadata model to target
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [StartMetadataModelImport](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html)  **
  - **Description:** Grants permission to start a new import of metadata model
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [StartRecommendations](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartRecommendations.html)  **
  - **Description:** Grants permission to start the analysis of your source database to provide recommendations of target engines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartReplication](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to start a replication
  - **Resource types (\*required):** [ReplicationConfig\*](#list_dms-resource-ReplicationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)
  - **Access level:** Write

- **   [StartReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html)  **
  - **Description:** Grants permission to start the replication task
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Write

- **   [StartReplicationTaskAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment.html)  **
  - **Description:** Grants permission to start the replication task assessment for unsupported data types in the source database
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Write

- **   [StartReplicationTaskAssessmentRun](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html)  **
  - **Description:** Grants permission to start a new premigration assessment run for one or more individual assessments of a migration task
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Write

- **   [StopDataMigration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to stop the database migration
  - **Resource types (\*required):** [DataMigration\*](#list_dms-resource-DataMigration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-migration-tag/${TagKey}](#list_dms-dms_data-migration-tag___TagKey_)
  - **Access level:** Write

- **   [StopReplication](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to stop a replication
  - **Resource types (\*required):** [ReplicationConfig\*](#list_dms-resource-ReplicationConfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_)
  - **Access level:** Write

- **   [StopReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask.html)  **
  - **Description:** Grants permission to stop the replication task
  - **Resource types (\*required):** [ReplicationTask\*](#list_dms-resource-ReplicationTask)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_)
  - **Access level:** Write

- **   [TestConnection](https://docs.aws.amazon.com/dms/latest/APIReference/API_TestConnection.html)  **
  - **Description:** Grants permission to test the connection between the replication instance and the endpoint
  - **Resource types (\*required):** [Endpoint\*](#list_dms-resource-Endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_)
  - **Resource types (\*required):** [ReplicationInstance\*](#list_dms-resource-ReplicationInstance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_)
  - **Access level:** Read

- **   [UpdateConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html)  **
  - **Description:** Grants permission to update a conversion configuration
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataProvider](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyDataProvider.html)  **
  - **Description:** Grants permission to update the specified data provider
  - **Resource types (\*required):** [DataProvider\*](#list_dms-resource-DataProvider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-provider-tag/${TagKey}](#list_dms-dms_data-provider-tag___TagKey_)
  - **Access level:** Write

- **   [UpdateInstanceProfile](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyInstanceProfile.html)  **
  - **Description:** Grants permission to update the specified instance profile
  - **Resource types (\*required):** [InstanceProfile\*](#list_dms-resource-InstanceProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_)
  - **Access level:** Write

- **   [UpdateMigrationProject](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyMigrationProject.html)  **
  - **Description:** Grants permission to update the specified migration project
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Write

- **   [UpdateSubscriptionsToEventBridge](https://docs.aws.amazon.com/dms/latest/APIReference/API_UpdateSubscriptionsToEventBridge.html)  **
  - **Description:** Grants permission to migrate DMS subcriptions to Eventbridge
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for AWS Database Migration Service
<a name="list_dms-permission-only-actions"></a>

The following actions are defined by AWS Database Migration Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateOutboundIntegration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to DMS to create resources for zero-ETL integrations with self managed databases
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dms-aws_TagKeys)<br />[dms:req-tag/${TagKey}](#list_dms-dms_req-tag___TagKey_)
  - **Access level:** Write

- **   [GetMetadataModel](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to list all of the AWS DMS attributes for a metadata model
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [ListMetadataModelAssessmentActionItems](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to list the AWS DMS attributes for a metadata model assessment action items
  - **Resource types (\*required):** [MigrationProject\*](#list_dms-resource-MigrationProject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_)
  - **Access level:** Read

- **   [ModifyFleetAdvisorCollector](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to modify the name and description of the specified Fleet Advisor collector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifyFleetAdvisorCollectorStatuses](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to modify the status of the specified Fleet Advisor collector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifyOutboundIntegration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to DMS to modify resources for zero-ETL integrations with self managed databases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UploadFileMetadataList](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to upload files to your Amazon S3 bucket
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Database Migration Service
<a name="list_dms-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Certificate](https://docs.aws.amazon.com/dms/latest/APIReference/API_Certificate.html)  | arn:${Partition}:dms:${Region}:${Account}:cert:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:cert-tag/${TagKey}](#list_dms-dms_cert-tag___TagKey_) | 
|  [DataMigration](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  | arn:${Partition}:dms:${Region}:${Account}:data-migration:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-migration-tag/${TagKey}](#list_dms-dms_data-migration-tag___TagKey_) | 
|  [DataProvider](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  | arn:${Partition}:dms:${Region}:${Account}:data-provider:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:data-provider-tag/${TagKey}](#list_dms-dms_data-provider-tag___TagKey_) | 
|  [Endpoint](https://docs.aws.amazon.com/dms/latest/APIReference/API_Endpoint.html)  | arn:${Partition}:dms:${Region}:${Account}:endpoint:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:endpoint-tag/${TagKey}](#list_dms-dms_endpoint-tag___TagKey_) | 
|  [EventSubscription](https://docs.aws.amazon.com/dms/latest/APIReference/API_EventSubscription.html)  | arn:${Partition}:dms:${Region}:${Account}:es:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:es-tag/${TagKey}](#list_dms-dms_es-tag___TagKey_) | 
|  [InstanceProfile](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  | arn:${Partition}:dms:${Region}:${Account}:instance-profile:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:instance-profile-tag/${TagKey}](#list_dms-dms_instance-profile-tag___TagKey_) | 
|  [MigrationProject](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  | arn:${Partition}:dms:${Region}:${Account}:migration-project:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:migration-project-tag/${TagKey}](#list_dms-dms_migration-project-tag___TagKey_) | 
|  [ReplicationConfig](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html)  | arn:${Partition}:dms:${Region}:${Account}:replication-config:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:replication-config-tag/${TagKey}](#list_dms-dms_replication-config-tag___TagKey_) | 
|  [ReplicationInstance](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationInstance.html)  | arn:${Partition}:dms:${Region}:${Account}:rep:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:rep-tag/${TagKey}](#list_dms-dms_rep-tag___TagKey_) | 
|  [ReplicationSubnetGroup](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationSubnetGroup.html)  | arn:${Partition}:dms:${Region}:${Account}:subgrp:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:subgrp-tag/${TagKey}](#list_dms-dms_subgrp-tag___TagKey_) | 
|  [ReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTask.html)  | arn:${Partition}:dms:${Region}:${Account}:task:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:task-tag/${TagKey}](#list_dms-dms_task-tag___TagKey_) | 
|  [ReplicationTaskAssessmentRun](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskAssessmentRun.html)  | arn:${Partition}:dms:${Region}:${Account}:assessment-run:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:assessment-run-tag/${TagKey}](#list_dms-dms_assessment-run-tag___TagKey_) | 
|  [ReplicationTaskIndividualAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskIndividualAssessment.html)  | arn:${Partition}:dms:${Region}:${Account}:individual-assessment:\* | [aws:ResourceTag/${TagKey}](#list_dms-aws_ResourceTag___TagKey_)<br />[dms:individual-assessment-tag/${TagKey}](#list_dms-dms_individual-assessment-tag___TagKey_) | 

## Condition keys for AWS Database Migration Service
<a name="list_dms-policy-keys"></a>

AWS Database Migration Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [dms:assessment-run-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_assessment-run-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for AssessmentRun | String | 
|   [dms:cert-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice--dms_cert-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for Certificate | String | 
|   [dms:data-migration-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice--dms_data-migration-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for DataMigration | String | 
|   [dms:data-provider-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice--dms_dp-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for DataProvider | String | 
|   [dms:endpoint-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_endpoint-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for Endpoint | String | 
|   [dms:es-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_es-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for EventSubscription | String | 
|   [dms:individual-assessment-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_individual-assessment-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for IndividualAssessment | String | 
|   [dms:instance-profile-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice--dms_ip-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for InstanceProfile | String | 
|   [dms:migration-project-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice--dms_mp-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for MigrationProject | String | 
|   [dms:rep-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_rep-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for ReplicationInstance | String | 
|   [dms:replication-config-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_replication-config-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for ReplicationConfig | String | 
|   [dms:req-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_req-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the given request | String | 
|   [dms:subgrp-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_subgrp-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for ReplicationSubnetGroup | String | 
|   [dms:task-tag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html#awsdatabasemigrationservice-dms_task-tag___TagKey_)  | Filters access by the presence of tag key-value pairs in the request for ReplicationTask | String | 