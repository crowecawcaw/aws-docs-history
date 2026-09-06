

# Actions, resources, and condition keys for AWS Application Migration Service
<a name="list_mgn"></a>

AWS Application Migration Service (service prefix: `mgn`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mgn/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mgn/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mgn/latest/ug/security_iam_authentication.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mgn/mgn.json) for this service.

**Topics**
+ [API operations defined by AWS Application Migration Service](#list_mgn-operations)
+ [Actions defined by AWS Application Migration Service](#list_mgn-actions-as-permissions)
+ [Permission-only actions for AWS Application Migration Service](#list_mgn-permission-only-actions)
+ [Resource types defined by AWS Application Migration Service](#list_mgn-resources-for-iam-policies)
+ [Condition keys for AWS Application Migration Service](#list_mgn-policy-keys)

## API operations defined by AWS Application Migration Service
<a name="list_mgn-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mgn-actions-as-permissions).




- **   ArchiveApplication  **
  - **IAM action:**  [mgn:ArchiveApplication](#list_mgn-action-ArchiveApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ArchiveWave  **
  - **IAM action:**  [mgn:ArchiveWave](#list_mgn-action-ArchiveWave) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateApplications  **
  - **IAM action:**  [mgn:AssociateApplications](#list_mgn-action-AssociateApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateSourceServers  **
  - **IAM action:**  [mgn:AssociateSourceServers](#list_mgn-action-AssociateSourceServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ChangeServerLifeCycleState  **
  - **IAM action:**  [mgn:ChangeServerLifeCycleState](#list_mgn-action-ChangeServerLifeCycleState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [mgn:CreateApplication](#list_mgn-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnector  **
  - **IAM action:**  [mgn:CreateConnector](#list_mgn-action-CreateConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLaunchConfigurationTemplate  **
  - **IAM action:**  [mgn:CreateLaunchConfigurationTemplate](#list_mgn-action-CreateLaunchConfigurationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateNetworkMigrationDefinition  **
  - **IAM action:**  [mgn:CreateNetworkMigrationDefinition](#list_mgn-action-CreateNetworkMigrationDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateReplicationConfigurationTemplate  **
  - **IAM action:**  [mgn:CreateReplicationConfigurationTemplate](#list_mgn-action-CreateReplicationConfigurationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWave  **
  - **IAM action:**  [mgn:CreateWave](#list_mgn-action-CreateWave)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteApplication  **
  - **IAM action:**  [mgn:DeleteApplication](#list_mgn-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnector  **
  - **IAM action:**  [mgn:DeleteConnector](#list_mgn-action-DeleteConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJob  **
  - **IAM action:**  [mgn:DeleteJob](#list_mgn-action-DeleteJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLaunchConfigurationTemplate  **
  - **IAM action:**  [mgn:DeleteLaunchConfigurationTemplate](#list_mgn-action-DeleteLaunchConfigurationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNetworkMigrationDefinition  **
  - **IAM action:**  [mgn:DeleteNetworkMigrationDefinition](#list_mgn-action-DeleteNetworkMigrationDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationConfigurationTemplate  **
  - **IAM action:**  [mgn:DeleteReplicationConfigurationTemplate](#list_mgn-action-DeleteReplicationConfigurationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSourceServer  **
  - **IAM action:**  [mgn:DeleteSourceServer](#list_mgn-action-DeleteSourceServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVcenterClient  **
  - **IAM action:**  [mgn:DeleteVcenterClient](#list_mgn-action-DeleteVcenterClient) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWave  **
  - **IAM action:**  [mgn:DeleteWave](#list_mgn-action-DeleteWave) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeJobLogItems  **
  - **IAM action:**  [mgn:DescribeJobLogItems](#list_mgn-action-DescribeJobLogItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobs  **
  - **IAM action:**  [mgn:DescribeJobs](#list_mgn-action-DescribeJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLaunchConfigurationTemplates  **
  - **IAM action:**  [mgn:DescribeLaunchConfigurationTemplates](#list_mgn-action-DescribeLaunchConfigurationTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeReplicationConfigurationTemplates  **
  - **IAM action:**  [mgn:DescribeReplicationConfigurationTemplates](#list_mgn-action-DescribeReplicationConfigurationTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeSourceServers  **
  - **IAM action:**  [mgn:DescribeSourceServers](#list_mgn-action-DescribeSourceServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeVcenterClients  **
  - **IAM action:**  [mgn:DescribeVcenterClients](#list_mgn-action-DescribeVcenterClients) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisassociateApplications  **
  - **IAM action:**  [mgn:DisassociateApplications](#list_mgn-action-DisassociateApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateSourceServers  **
  - **IAM action:**  [mgn:DisassociateSourceServers](#list_mgn-action-DisassociateSourceServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisconnectFromService  **
  - **IAM action:**  [mgn:DisconnectFromService](#list_mgn-action-DisconnectFromService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   FinalizeCutover  **
  - **IAM action:**  [mgn:FinalizeCutover](#list_mgn-action-FinalizeCutover) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetLaunchConfiguration  **
  - **IAM action:**  [mgn:GetLaunchConfiguration](#list_mgn-action-GetLaunchConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkMigrationDefinition  **
  - **IAM action:**  [mgn:GetNetworkMigrationDefinition](#list_mgn-action-GetNetworkMigrationDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkMigrationMapperSegmentConstruct  **
  - **IAM action:**  [mgn:GetNetworkMigrationMapperSegmentConstruct](#list_mgn-action-GetNetworkMigrationMapperSegmentConstruct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReplicationConfiguration  **
  - **IAM action:**  [mgn:GetReplicationConfiguration](#list_mgn-action-GetReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InitializeService  **
  - **IAM action:**  [mgn:InitializeService](#list_mgn-action-InitializeService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListApplications  **
  - **IAM action:**  [mgn:ListApplications](#list_mgn-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectors  **
  - **IAM action:**  [mgn:ListConnectors](#list_mgn-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListExportErrors  **
  - **IAM action:**  [mgn:ListExportErrors](#list_mgn-action-ListExportErrors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExports  **
  - **IAM action:**  [mgn:ListExports](#list_mgn-action-ListExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImportErrors  **
  - **IAM action:**  [mgn:ListImportErrors](#list_mgn-action-ListImportErrors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImportFileEnrichments  **
  - **IAM action:**  [mgn:ListImportFileEnrichments](#list_mgn-action-ListImportFileEnrichments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImports  **
  - **IAM action:**  [mgn:ListImports](#list_mgn-action-ListImports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedAccounts  **
  - **IAM action:**  [mgn:ListManagedAccounts](#list_mgn-action-ListManagedAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationAnalyses  **
  - **IAM action:**  [mgn:ListNetworkMigrationAnalyses](#list_mgn-action-ListNetworkMigrationAnalyses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationAnalysisResults  **
  - **IAM action:**  [mgn:ListNetworkMigrationAnalysisResults](#list_mgn-action-ListNetworkMigrationAnalysisResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationCodeGenerationSegments  **
  - **IAM action:**  [mgn:ListNetworkMigrationCodeGenerationSegments](#list_mgn-action-ListNetworkMigrationCodeGenerationSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationCodeGenerations  **
  - **IAM action:**  [mgn:ListNetworkMigrationCodeGenerations](#list_mgn-action-ListNetworkMigrationCodeGenerations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationDefinitions  **
  - **IAM action:**  [mgn:ListNetworkMigrationDefinitions](#list_mgn-action-ListNetworkMigrationDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationDeployedStacks  **
  - **IAM action:**  [mgn:ListNetworkMigrationDeployedStacks](#list_mgn-action-ListNetworkMigrationDeployedStacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationDeployments  **
  - **IAM action:**  [mgn:ListNetworkMigrationDeployments](#list_mgn-action-ListNetworkMigrationDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationExecutions  **
  - **IAM action:**  [mgn:ListNetworkMigrationExecutions](#list_mgn-action-ListNetworkMigrationExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationMapperSegmentConstructs  **
  - **IAM action:**  [mgn:ListNetworkMigrationMapperSegmentConstructs](#list_mgn-action-ListNetworkMigrationMapperSegmentConstructs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationMapperSegments  **
  - **IAM action:**  [mgn:ListNetworkMigrationMapperSegments](#list_mgn-action-ListNetworkMigrationMapperSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationMappingUpdates  **
  - **IAM action:**  [mgn:ListNetworkMigrationMappingUpdates](#list_mgn-action-ListNetworkMigrationMappingUpdates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNetworkMigrationMappings  **
  - **IAM action:**  [mgn:ListNetworkMigrationMappings](#list_mgn-action-ListNetworkMigrationMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSourceServerActions  **
  - **IAM action:**  [mgn:ListSourceServerActions](#list_mgn-action-ListSourceServerActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [mgn:ListTagsForResource](#list_mgn-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTemplateActions  **
  - **IAM action:**  [mgn:ListTemplateActions](#list_mgn-action-ListTemplateActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWaves  **
  - **IAM action:**  [mgn:ListWaves](#list_mgn-action-ListWaves) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   MarkAsArchived  **
  - **IAM action:**  [mgn:MarkAsArchived](#list_mgn-action-MarkAsArchived) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PauseReplication  **
  - **IAM action:**  [mgn:PauseReplication](#list_mgn-action-PauseReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSourceServerAction  **
  - **IAM action:**  [mgn:PutSourceServerAction](#list_mgn-action-PutSourceServerAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTemplateAction  **
  - **IAM action:**  [mgn:PutTemplateAction](#list_mgn-action-PutTemplateAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveSourceServerAction  **
  - **IAM action:**  [mgn:RemoveSourceServerAction](#list_mgn-action-RemoveSourceServerAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTemplateAction  **
  - **IAM action:**  [mgn:RemoveTemplateAction](#list_mgn-action-RemoveTemplateAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResumeReplication  **
  - **IAM action:**  [mgn:ResumeReplication](#list_mgn-action-ResumeReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetryDataReplication  **
  - **IAM action:**  [mgn:RetryDataReplication](#list_mgn-action-RetryDataReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCutover  **
  - **IAM action:**  [mgn:StartCutover](#list_mgn-action-StartCutover)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartExport  **
  - **IAM action:**  [mgn:StartExport](#list_mgn-action-StartExport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartImport  **
  - **IAM action:**  [mgn:StartImport](#list_mgn-action-StartImport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartImportFileEnrichment  **
  - **IAM action:**  [mgn:StartImportFileEnrichment](#list_mgn-action-StartImportFileEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNetworkMigrationAnalysis  **
  - **IAM action:**  [mgn:StartNetworkMigrationAnalysis](#list_mgn-action-StartNetworkMigrationAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNetworkMigrationCodeGeneration  **
  - **IAM action:**  [mgn:StartNetworkMigrationCodeGeneration](#list_mgn-action-StartNetworkMigrationCodeGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNetworkMigrationDeployment  **
  - **IAM action:**  [mgn:StartNetworkMigrationDeployment](#list_mgn-action-StartNetworkMigrationDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNetworkMigrationMapping  **
  - **IAM action:**  [mgn:StartNetworkMigrationMapping](#list_mgn-action-StartNetworkMigrationMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNetworkMigrationMappingUpdate  **
  - **IAM action:**  [mgn:StartNetworkMigrationMappingUpdate](#list_mgn-action-StartNetworkMigrationMappingUpdate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartReplication  **
  - **IAM action:**  [mgn:StartReplication](#list_mgn-action-StartReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTest  **
  - **IAM action:**  [mgn:StartTest](#list_mgn-action-StartTest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StopReplication  **
  - **IAM action:**  [mgn:StopReplication](#list_mgn-action-StopReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateTargetInstances  **
  - **IAM action:**  [mgn:TagResource](#list_mgn-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [mgn:TerminateTargetInstances](#list_mgn-action-TerminateTargetInstances)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UnarchiveApplication  **
  - **IAM action:**  [mgn:UnarchiveApplication](#list_mgn-action-UnarchiveApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UnarchiveWave  **
  - **IAM action:**  [mgn:UnarchiveWave](#list_mgn-action-UnarchiveWave) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [mgn:UntagResource](#list_mgn-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [mgn:UpdateApplication](#list_mgn-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnector  **
  - **IAM action:**  [mgn:UpdateConnector](#list_mgn-action-UpdateConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLaunchConfiguration  **
  - **IAM action:**  [mgn:UpdateLaunchConfiguration](#list_mgn-action-UpdateLaunchConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLaunchConfigurationTemplate  **
  - **IAM action:**  [mgn:UpdateLaunchConfigurationTemplate](#list_mgn-action-UpdateLaunchConfigurationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNetworkMigrationDefinition  **
  - **IAM action:**  [mgn:UpdateNetworkMigrationDefinition](#list_mgn-action-UpdateNetworkMigrationDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNetworkMigrationMapperSegment  **
  - **IAM action:**  [mgn:UpdateNetworkMigrationMapperSegment](#list_mgn-action-UpdateNetworkMigrationMapperSegment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReplicationConfiguration  **
  - **IAM action:**  [mgn:UpdateReplicationConfiguration](#list_mgn-action-UpdateReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReplicationConfigurationTemplate  **
  - **IAM action:**  [mgn:UpdateReplicationConfigurationTemplate](#list_mgn-action-UpdateReplicationConfigurationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSourceServer  **
  - **IAM action:**  [mgn:UpdateSourceServer](#list_mgn-action-UpdateSourceServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSourceServerReplicationType  **
  - **IAM action:**  [mgn:UpdateSourceServerReplicationType](#list_mgn-action-UpdateSourceServerReplicationType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWave  **
  - **IAM action:**  [mgn:UpdateWave](#list_mgn-action-UpdateWave) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Application Migration Service
<a name="list_mgn-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ArchiveApplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ArchiveApplication.html)  **
  - **Description:** Grants permission to archive an application
  - **Resource types (\*required):** [ApplicationResource\*](#list_mgn-resource-ApplicationResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ArchiveWave](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ArchiveWave.html)  **
  - **Description:** Grants permission to archive a wave
  - **Resource types (\*required):** [WaveResource\*](#list_mgn-resource-WaveResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateApplications](https://docs.aws.amazon.com/mgn/latest/APIReference/API_AssociateApplications.html)  **
  - **Description:** Grants permission to associate applications to a wave
  - **Resource types (\*required):** [ApplicationResource\*](#list_mgn-resource-ApplicationResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WaveResource\*](#list_mgn-resource-WaveResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateSourceServers](https://docs.aws.amazon.com/mgn/latest/APIReference/API_AssociateSourceServers.html)  **
  - **Description:** Grants permission to associate source servers to an application
  - **Resource types (\*required):** [ApplicationResource\*](#list_mgn-resource-ApplicationResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ChangeServerLifeCycleState](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ChangeServerLifeCycleState.html)  **
  - **Description:** Grants permission to change source server life cycle state
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnector](https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateConnector.html)  **
  - **Description:** Grants permission to create connector
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLaunchConfigurationTemplate](https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateLaunchConfigurationTemplate.html)  **
  - **Description:** Grants permission to create launch configuration template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [CreateNetworkMigrationDefinition](https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateNetworkMigrationDefinition.html)  **
  - **Description:** Grants permission to create a network migration definition
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [CreateReplicationConfigurationTemplate](https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateReplicationConfigurationTemplate.html)  **
  - **Description:** Grants permission to create replication configuration template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWave](https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateWave.html)  **
  - **Description:** Grants permission to create a wave
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [ApplicationResource\*](#list_mgn-resource-ApplicationResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteConnector.html)  **
  - **Description:** Grants permission to delete connector
  - **Resource types (\*required):** [ConnectorResource\*](#list_mgn-resource-ConnectorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJob](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteJob.html)  **
  - **Description:** Grants permission to delete job
  - **Resource types (\*required):** [JobResource\*](#list_mgn-resource-JobResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLaunchConfigurationTemplate](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteLaunchConfigurationTemplate.html)  **
  - **Description:** Grants permission to delete launch configuration template
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource\*](#list_mgn-resource-LaunchConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetworkMigrationDefinition](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteNetworkMigrationDefinition.html)  **
  - **Description:** Grants permission to delete a network migration definition
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationConfigurationTemplate](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteReplicationConfigurationTemplate.html)  **
  - **Description:** Grants permission to delete replication configuration template
  - **Resource types (\*required):** [ReplicationConfigurationTemplateResource\*](#list_mgn-resource-ReplicationConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSourceServer](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteSourceServer.html)  **
  - **Description:** Grants permission to delete source server
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVcenterClient](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteVcenterClient.html)  **
  - **Description:** Grants permission to delete vcenter client
  - **Resource types (\*required):** [VcenterClientResource\*](#list_mgn-resource-VcenterClientResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWave](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteWave.html)  **
  - **Description:** Grants permission to delete a wave
  - **Resource types (\*required):** [WaveResource\*](#list_mgn-resource-WaveResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeJobLogItems](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeJobLogItems.html)  **
  - **Description:** Grants permission to describe job log items
  - **Resource types (\*required):** [JobResource\*](#list_mgn-resource-JobResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJobs](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeJobs.html)  **
  - **Description:** Grants permission to describe jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeLaunchConfigurationTemplates](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeLaunchConfigurationTemplates.html)  **
  - **Description:** Grants permission to describe launch configuration template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeReplicationConfigurationTemplates](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeReplicationConfigurationTemplates.html)  **
  - **Description:** Grants permission to describe replication configuration template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeSourceServers](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeSourceServers.html)  **
  - **Description:** Grants permission to describe source servers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeVcenterClients](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeVcenterClients.html)  **
  - **Description:** Grants permission to describe vcenter clients
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DisassociateApplications](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DisassociateApplications.html)  **
  - **Description:** Grants permission to disassociate applications from a wave
  - **Resource types (\*required):** [ApplicationResource\*](#list_mgn-resource-ApplicationResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [WaveResource\*](#list_mgn-resource-WaveResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateSourceServers](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DisassociateSourceServers.html)  **
  - **Description:** Grants permission to disassociate source servers from an application
  - **Resource types (\*required):** [ApplicationResource\*](#list_mgn-resource-ApplicationResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisconnectFromService](https://docs.aws.amazon.com/mgn/latest/APIReference/API_DisconnectFromService.html)  **
  - **Description:** Grants permission to disconnect source server from service
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [FinalizeCutover](https://docs.aws.amazon.com/mgn/latest/APIReference/API_FinalizeCutover.html)  **
  - **Description:** Grants permission to finalize cutover
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountSettings](https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to get account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLaunchConfiguration](https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetLaunchConfiguration.html)  **
  - **Description:** Grants permission to get launch configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkMigrationDefinition](https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetNetworkMigrationDefinition.html)  **
  - **Description:** Grants permission to get a network migration definition
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkMigrationMapperSegmentConstruct](https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetNetworkMigrationMapperSegmentConstruct.html)  **
  - **Description:** Grants permission to get a network migration mapper segment construct
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReplicationConfiguration](https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetReplicationConfiguration.html)  **
  - **Description:** Grants permission to get replication configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InitializeService](https://docs.aws.amazon.com/mgn/latest/APIReference/API_InitializeService.html)  **
  - **Description:** Grants permission to initialize service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListApplications](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to list application summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectors](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListConnectors.html)  **
  - **Description:** Grants permission to list connectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExportErrors](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListExportErrors.html)  **
  - **Description:** Grants permission to list the errors of an export task
  - **Resource types (\*required):** [ExportResource\*](#list_mgn-resource-ExportResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExports](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListExports.html)  **
  - **Description:** Grants permission to list export tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImportErrors](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListImportErrors.html)  **
  - **Description:** Grants permission to list the errors of an import task
  - **Resource types (\*required):** [ImportResource\*](#list_mgn-resource-ImportResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListImportFileEnrichments](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListImportFileEnrichments.html)  **
  - **Description:** Grants permission to list the import file enrichment tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImports](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListImports.html)  **
  - **Description:** Grants permission to list the import tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedAccounts](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListManagedAccounts.html)  **
  - **Description:** Grants permission to list managed accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNetworkMigrationAnalyses](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationAnalyses.html)  **
  - **Description:** Grants permission to list network migration analyses
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationAnalysisResults](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationAnalysisResults.html)  **
  - **Description:** Grants permission to list network migration analysis results
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationCodeGenerationSegments](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationCodeGenerationSegments.html)  **
  - **Description:** Grants permission to list network migration code generation segments
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationCodeGenerations](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationCodeGenerations.html)  **
  - **Description:** Grants permission to list network migration code generations
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationDefinitions](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationDefinitions.html)  **
  - **Description:** Grants permission to list network migration definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNetworkMigrationDeployedStacks](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationDeployedStacks.html)  **
  - **Description:** Grants permission to list network migration deployed stacks
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationDeployedStacksDeletions](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationDeployedStacksDeletions.html)  **
  - **Description:** Grants permission to list network migration deployed stacks deletions
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationDeployments](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationDeployments.html)  **
  - **Description:** Grants permission to list network migration deployments
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationExecutionArtifacts](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationExecutionArtifacts.html)  **
  - **Description:** Grants permission to list network migration execution artifacts
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationExecutions](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationExecutions.html)  **
  - **Description:** Grants permission to list network migration executions
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationMapperSegmentConstructs](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationMapperSegmentConstructs.html)  **
  - **Description:** Grants permission to list network migration mapper segment constructs
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationMapperSegments](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationMapperSegments.html)  **
  - **Description:** Grants permission to list network migration mapper segments
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationMappingUpdates](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationMappingUpdates.html)  **
  - **Description:** Grants permission to list network migration mapping updates
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListNetworkMigrationMappings](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListNetworkMigrationMappings.html)  **
  - **Description:** Grants permission to list network migration mappings
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSourceServerActions](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListSourceServerActions.html)  **
  - **Description:** Grants permission to list source server action documents
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTemplateActions](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListTemplateActions.html)  **
  - **Description:** Grants permission to list launch configuration template action documents
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource\*](#list_mgn-resource-LaunchConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWaves](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListWaves.html)  **
  - **Description:** Grants permission to list wave summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [MarkAsArchived](https://docs.aws.amazon.com/mgn/latest/APIReference/API_MarkAsArchived.html)  **
  - **Description:** Grants permission to mark source server as archived
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PauseReplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_PauseReplication.html)  **
  - **Description:** Grants permission to pause replication
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutSourceServerAction](https://docs.aws.amazon.com/mgn/latest/APIReference/API_PutSourceServerAction.html)  **
  - **Description:** Grants permission to put source server action document
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutTemplateAction](https://docs.aws.amazon.com/mgn/latest/APIReference/API_PutTemplateAction.html)  **
  - **Description:** Grants permission to put launch configuration template action document
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource\*](#list_mgn-resource-LaunchConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveSourceServerAction](https://docs.aws.amazon.com/mgn/latest/APIReference/API_RemoveSourceServerAction.html)  **
  - **Description:** Grants permission to remove source server action document
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveTemplateAction](https://docs.aws.amazon.com/mgn/latest/APIReference/API_RemoveTemplateAction.html)  **
  - **Description:** Grants permission to remove launch configuration template action document
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource\*](#list_mgn-resource-LaunchConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResumeReplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_ResumeReplication.html)  **
  - **Description:** Grants permission to resume replication
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetryDataReplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_RetryDataReplication.html)  **
  - **Description:** Grants permission to retry replication
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCutover](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartCutover.html)  **
  - **Description:** Grants permission to start cutover
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [StartExport](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartExport.html)  **
  - **Description:** Grants permission to start an export task
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [StartImport](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartImport.html)  **
  - **Description:** Grants permission to create an import task
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [StartImportFileEnrichment](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartImportFileEnrichment.html)  **
  - **Description:** Grants permission to start import file enrichment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartNetworkMigrationAnalysis](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationAnalysis.html)  **
  - **Description:** Grants permission to start a network migration analysis
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNetworkMigrationCodeGeneration](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationCodeGeneration.html)  **
  - **Description:** Grants permission to start network migration code generation
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNetworkMigrationDeployedStacksDeletion](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationDeployedStacksDeletion.html)  **
  - **Description:** Grants permission to start deletion of network migration deployed stacks
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNetworkMigrationDeployment](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationDeployment.html)  **
  - **Description:** Grants permission to start a network migration deployment
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNetworkMigrationMapping](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationMapping.html)  **
  - **Description:** Grants permission to start a network migration mapping
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNetworkMigrationMappingUpdate](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationMappingUpdate.html)  **
  - **Description:** Grants permission to start a network migration mapping update
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartReplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartReplication.html)  **
  - **Description:** Grants permission to start replication
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTest](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartTest.html)  **
  - **Description:** Grants permission to start test
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [StopReplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_StopReplication.html)  **
  - **Description:** Grants permission to stop replication
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mgn/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to assign a resource tag
  - **Resource types (\*required):** [ApplicationResource](#list_mgn-resource-ApplicationResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [ConnectorResource](#list_mgn-resource-ConnectorResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [ExportResource](#list_mgn-resource-ExportResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [ImportResource](#list_mgn-resource-ImportResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [JobResource](#list_mgn-resource-JobResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource](#list_mgn-resource-LaunchConfigurationTemplateResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [ReplicationConfigurationTemplateResource](#list_mgn-resource-ReplicationConfigurationTemplateResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [SourceServerResource](#list_mgn-resource-SourceServerResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [VcenterClientResource](#list_mgn-resource-VcenterClientResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Resource types (\*required):** [WaveResource](#list_mgn-resource-WaveResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)<br />[mgn:CreateAction](#list_mgn-mgn_CreateAction)
  - **Access level:** Tagging, Write

- **   [TerminateTargetInstances](https://docs.aws.amazon.com/mgn/latest/APIReference/API_TerminateTargetInstances.html)  **
  - **Description:** Grants permission to terminate target instances
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [UnarchiveApplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UnarchiveApplication.html)  **
  - **Description:** Grants permission to unarchive an application
  - **Resource types (\*required):** [ApplicationResource\*](#list_mgn-resource-ApplicationResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UnarchiveWave](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UnarchiveWave.html)  **
  - **Description:** Grants permission to unarchive a wave
  - **Resource types (\*required):** [WaveResource\*](#list_mgn-resource-WaveResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [ApplicationResource](#list_mgn-resource-ApplicationResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Resource types (\*required):** [ConnectorResource](#list_mgn-resource-ConnectorResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Resource types (\*required):** [JobResource](#list_mgn-resource-JobResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource](#list_mgn-resource-LaunchConfigurationTemplateResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Resource types (\*required):** [ReplicationConfigurationTemplateResource](#list_mgn-resource-ReplicationConfigurationTemplateResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Resource types (\*required):** [SourceServerResource](#list_mgn-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Resource types (\*required):** [VcenterClientResource](#list_mgn-resource-VcenterClientResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Resource types (\*required):** [WaveResource](#list_mgn-resource-WaveResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateAccountSettings.html)  **
  - **Description:** Grants permission to update account settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplication](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update an application
  - **Resource types (\*required):** [ApplicationResource\*](#list_mgn-resource-ApplicationResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConnector](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateConnector.html)  **
  - **Description:** Grants permission to update connector
  - **Resource types (\*required):** [ConnectorResource\*](#list_mgn-resource-ConnectorResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLaunchConfiguration](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateLaunchConfiguration.html)  **
  - **Description:** Grants permission to update launch configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLaunchConfigurationTemplate](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateLaunchConfigurationTemplate.html)  **
  - **Description:** Grants permission to update launch configuration
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource\*](#list_mgn-resource-LaunchConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkMigrationDefinition](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateNetworkMigrationDefinition.html)  **
  - **Description:** Grants permission to update a network migration definition
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkMigrationMapperSegment](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateNetworkMigrationMapperSegment.html)  **
  - **Description:** Grants permission to update a network migration mapper segment
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkMigrationMapperSegmentConstruct](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateNetworkMigrationMapperSegmentConstruct.html)  **
  - **Description:** Grants permission to update a network migration mapper segment construct
  - **Resource types (\*required):** [NetworkMigrationDefinitionResource\*](#list_mgn-resource-NetworkMigrationDefinitionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReplicationConfiguration](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateReplicationConfiguration.html)  **
  - **Description:** Grants permission to update replication configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReplicationConfigurationTemplate](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateReplicationConfigurationTemplate.html)  **
  - **Description:** Grants permission to update replication configuration template
  - **Resource types (\*required):** [ReplicationConfigurationTemplateResource\*](#list_mgn-resource-ReplicationConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSourceServer](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateSourceServer.html)  **
  - **Description:** Grants permission to update source server
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSourceServerReplicationType](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateSourceServerReplicationType.html)  **
  - **Description:** Grants permission to update source server replication type
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWave](https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateWave.html)  **
  - **Description:** Grants permission to update a wave
  - **Resource types (\*required):** [WaveResource\*](#list_mgn-resource-WaveResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Application Migration Service
<a name="list_mgn-permission-only-actions"></a>

The following actions are defined by AWS Application Migration Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [BatchCreateVolumeSnapshotGroupForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to create volume snapshot group
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteSnapshotRequestForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to batch delete snapshot request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateVcenterClientForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to create vcenter client
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeReplicationServerAssociationsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to describe replication server associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSnapshotRequestsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to describe snapshots requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgentCommandForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to get agent command
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentConfirmedResumeInfoForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to get agent confirmed resume info
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentInstallationAssetsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to get agent installation assets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgentReplicationInfoForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to get agent replication info
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentRuntimeConfigurationForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to get agent runtime configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentSnapshotCreditsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to get agent snapshots credits
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChannelCommandsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to get channel commands
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVcenterClientCommandsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to get vcenter client commands
  - **Resource types (\*required):** [VcenterClientResource\*](#list_mgn-resource-VcenterClientResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [IssueClientCertificateForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to issue a client certificate
  - **Resource types (\*required):** [SourceServerResource](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyAgentAuthenticationForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to notify agent authentication
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyAgentConnectedForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to notify agent is connected
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyAgentDisconnectedForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to notify agent is disconnected
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyAgentReplicationProgressForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to notify agent replication progress
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyVcenterClientStartedForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to notify vcenter client started
  - **Resource types (\*required):** [VcenterClientResource\*](#list_mgn-resource-VcenterClientResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterAgentForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to register agent
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mgn-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mgn-aws_TagKeys)
  - **Access level:** Write

- **   [SendAgentLogsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to send agent logs
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendAgentMetricsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to send agent metrics
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendChannelCommandResultForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to send channel command result
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendClientLogsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to send client logs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendClientMetricsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to send client metrics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendVcenterClientCommandResultForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to send vcenter client command result
  - **Resource types (\*required):** [VcenterClientResource\*](#list_mgn-resource-VcenterClientResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendVcenterClientLogsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to send vcenter client logs
  - **Resource types (\*required):** [VcenterClientResource\*](#list_mgn-resource-VcenterClientResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendVcenterClientMetricsForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to send vcenter client metrics
  - **Resource types (\*required):** [VcenterClientResource\*](#list_mgn-resource-VcenterClientResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSnapshotGroupForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to start snapshot group requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAgentBacklogForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to update agent backlog
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentConversionInfoForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to update agent conversion info
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentReplicationInfoForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to update agent replication info
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentReplicationProcessStateForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to update agent replication process state
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentSourcePropertiesForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to update agent source properties
  - **Resource types (\*required):** [SourceServerResource\*](#list_mgn-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifyClientRoleForMgn](https://docs.aws.amazon.com/mgn/latest/ug/mgn-apis.html)  **
  - **Description:** Grants permission to verify client role
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by AWS Application Migration Service
<a name="list_mgn-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ApplicationResource](https://docs.aws.amazon.com/mgn/latest/ug/applications.html)  | arn:${Partition}:mgn:${Region}:${Account}:application/${ApplicationID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [ConnectorResource](https://docs.aws.amazon.com/mgn/latest/ug/connectors.html)  | arn:${Partition}:mgn:${Region}:${Account}:connector/${ConnectorID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [ExportResource](https://docs.aws.amazon.com/mgn/latest/ug/exports.html)  | arn:${Partition}:mgn:${Region}:${Account}:export/${ExportID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [ImportResource](https://docs.aws.amazon.com/mgn/latest/ug/imports.html)  | arn:${Partition}:mgn:${Region}:${Account}:import/${ImportID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [JobResource](https://docs.aws.amazon.com/mgn/latest/ug/launching-target-servers.html)  | arn:${Partition}:mgn:${Region}:${Account}:job/${JobID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [LaunchConfigurationTemplateResource](https://docs.aws.amazon.com/mgn/latest/ug/post-launch-settings.html)  | arn:${Partition}:mgn:${Region}:${Account}:launch-configuration-template/${LaunchConfigurationTemplateID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [NetworkMigrationDefinitionResource](https://docs.aws.amazon.com/mgn/latest/ug/network-migration-definition.html)  | arn:${Partition}:mgn:${Region}:${Account}:network-migration-definition/${NetworkMigrationDefinitionID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [ReplicationConfigurationTemplateResource](https://docs.aws.amazon.com/mgn/latest/ug/replication-settings-template.html)  | arn:${Partition}:mgn:${Region}:${Account}:replication-configuration-template/${ReplicationConfigurationTemplateID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [SourceServerResource](https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html)  | arn:${Partition}:mgn:${Region}:${Account}:source-server/${SourceServerID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [VcenterClientResource](https://docs.aws.amazon.com/mgn/latest/ug/agentless-mgn.html)  | arn:${Partition}:mgn:${Region}:${Account}:vcenter-client/${VcenterClientID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 
|  [WaveResource](https://docs.aws.amazon.com/mgn/latest/ug/waves.html)  | arn:${Partition}:mgn:${Region}:${Account}:wave/${WaveID} | [aws:ResourceTag/${TagKey}](#list_mgn-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Application Migration Service
<a name="list_mgn-policy-keys"></a>

AWS Application Migration Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by presence of tag keys in the request | ArrayOfString | 
|   [mgn:CreateAction](https://docs.aws.amazon.com/mgn/latest/ug/supported-iam-actions-tagging.html)  | Filters access by the name of a resource-creating API action | String | 