

# Actions, resources, and condition keys for AWS IoT SiteWise
<a name="list_iotsitewise"></a>

AWS IoT SiteWise (service prefix: `iotsitewise`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotsitewise/iotsitewise.json) for this service.

**Topics**
+ [API operations defined by AWS IoT SiteWise](#list_iotsitewise-operations)
+ [Actions defined by AWS IoT SiteWise](#list_iotsitewise-actions-as-permissions)
+ [Permission-only actions for AWS IoT SiteWise](#list_iotsitewise-permission-only-actions)
+ [Resource types defined by AWS IoT SiteWise](#list_iotsitewise-resources-for-iam-policies)
+ [Condition keys for AWS IoT SiteWise](#list_iotsitewise-policy-keys)

## API operations defined by AWS IoT SiteWise
<a name="list_iotsitewise-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_iotsitewise-actions-as-permissions).




- **   AssociateAssets  **
  - **IAM action:**  [iotsitewise:AssociateAssets](#list_iotsitewise-action-AssociateAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateTimeSeriesToAssetProperty  **
  - **IAM action:**  [iotsitewise:AssociateTimeSeriesToAssetProperty](#list_iotsitewise-action-AssociateTimeSeriesToAssetProperty) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateDataSegmentsToDataset  **
  - **IAM action:**  [iotsitewise:BatchAssociateDataSegmentsToDataset](#list_iotsitewise-action-BatchAssociateDataSegmentsToDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateProjectAssets  **
  - **IAM action:**  [iotsitewise:BatchAssociateProjectAssets](#list_iotsitewise-action-BatchAssociateProjectAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteDatasetDataSegments  **
  - **IAM action:**  [iotsitewise:BatchDeleteDatasetDataSegments](#list_iotsitewise-action-BatchDeleteDatasetDataSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateDataSegmentsFromDataset  **
  - **IAM action:**  [iotsitewise:BatchDisassociateDataSegmentsFromDataset](#list_iotsitewise-action-BatchDisassociateDataSegmentsFromDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateProjectAssets  **
  - **IAM action:**  [iotsitewise:BatchDisassociateProjectAssets](#list_iotsitewise-action-BatchDisassociateProjectAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetAssetPropertyAggregates  **
  - **IAM action:**  [iotsitewise:BatchGetAssetPropertyAggregates](#list_iotsitewise-action-BatchGetAssetPropertyAggregates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetAssetPropertyValue  **
  - **IAM action:**  [iotsitewise:BatchGetAssetPropertyValue](#list_iotsitewise-action-BatchGetAssetPropertyValue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetAssetPropertyValueHistory  **
  - **IAM action:**  [iotsitewise:BatchGetAssetPropertyValueHistory](#list_iotsitewise-action-BatchGetAssetPropertyValueHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchPutAssetPropertyValue  **
  - **IAM action:**  [iotsitewise:BatchPutAssetPropertyValue](#list_iotsitewise-action-BatchPutAssetPropertyValue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelEnrichmentJob  **
  - **IAM action:**  [iotsitewise:CancelEnrichmentJob](#list_iotsitewise-action-CancelEnrichmentJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelPipelineExecution  **
  - **IAM action:**  [iotsitewise:CancelPipelineExecution](#list_iotsitewise-action-CancelPipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelQuery  **
  - **IAM action:**  [iotsitewise:CancelQuery](#list_iotsitewise-action-CancelQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccessPolicy  **
  - **IAM action:**  [iotsitewise:CreateAccessPolicy](#list_iotsitewise-action-CreateAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [iotsitewise:CreateApplication](#list_iotsitewise-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAsset  **
  - **IAM action:**  [iotsitewise:CreateAsset](#list_iotsitewise-action-CreateAsset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAssetModel  **
  - **IAM action:**  [iotsitewise:CreateAssetModel](#list_iotsitewise-action-CreateAssetModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAssetModelCompositeModel  **
  - **IAM action:**  [iotsitewise:CreateAssetModelCompositeModel](#list_iotsitewise-action-CreateAssetModelCompositeModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   CreateBulkImportJob  **
  - **IAM action:**  [iotsitewise:CreateBulkImportJob](#list_iotsitewise-action-CreateBulkImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   CreateComputationModel  **
  - **IAM action:**  [iotsitewise:CreateComputationModel](#list_iotsitewise-action-CreateComputationModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDashboard  **
  - **IAM action:**  [iotsitewise:CreateDashboard](#list_iotsitewise-action-CreateDashboard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataset  **
  - **IAM action:**  [iotsitewise:CreateDataset](#list_iotsitewise-action-CreateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   CreateDatasetExportJob  **
  - **IAM action:**  [iotsitewise:CreateDatasetExportJob](#list_iotsitewise-action-CreateDatasetExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEnrichmentJob  **
  - **IAM action:**  [iotsitewise:CreateEnrichmentJob](#list_iotsitewise-action-CreateEnrichmentJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGateway  **
  - **IAM action:**  [iotsitewise:CreateGateway](#list_iotsitewise-action-CreateGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   CreatePipeline  **
  - **IAM action:**  [iotsitewise:CreatePipeline](#list_iotsitewise-action-CreatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePortal  **
  - **IAM action:**  [iotsitewise:CreatePortal](#list_iotsitewise-action-CreatePortal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   CreateProject  **
  - **IAM action:**  [iotsitewise:CreateProject](#list_iotsitewise-action-CreateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTask  **
  - **IAM action:**  [iotsitewise:CreateTask](#list_iotsitewise-action-CreateTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   CreateWorkspace  **
  - **IAM action:**  [iotsitewise:CreateWorkspace](#list_iotsitewise-action-CreateWorkspace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAccessPolicy  **
  - **IAM action:**  [iotsitewise:DeleteAccessPolicy](#list_iotsitewise-action-DeleteAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [iotsitewise:DeleteApplication](#list_iotsitewise-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAsset  **
  - **IAM action:**  [iotsitewise:DeleteAsset](#list_iotsitewise-action-DeleteAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssetModel  **
  - **IAM action:**  [iotsitewise:DeleteAssetModel](#list_iotsitewise-action-DeleteAssetModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssetModelCompositeModel  **
  - **IAM action:**  [iotsitewise:DeleteAssetModelCompositeModel](#list_iotsitewise-action-DeleteAssetModelCompositeModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssetModelInterfaceRelationship  **
  - **IAM action:**  [iotsitewise:DeleteAssetModelInterfaceRelationship](#list_iotsitewise-action-DeleteAssetModelInterfaceRelationship) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteComputationModel  **
  - **IAM action:**  [iotsitewise:DeleteComputationModel](#list_iotsitewise-action-DeleteComputationModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDashboard  **
  - **IAM action:**  [iotsitewise:DeleteDashboard](#list_iotsitewise-action-DeleteDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataset  **
  - **IAM action:**  [iotsitewise:DeleteDataset](#list_iotsitewise-action-DeleteDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGateway  **
  - **IAM action:**  [iotsitewise:DeleteGateway](#list_iotsitewise-action-DeleteGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePipeline  **
  - **IAM action:**  [iotsitewise:DeletePipeline](#list_iotsitewise-action-DeletePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePortal  **
  - **IAM action:**  [iotsitewise:DeletePortal](#list_iotsitewise-action-DeletePortal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProject  **
  - **IAM action:**  [iotsitewise:DeleteProject](#list_iotsitewise-action-DeleteProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTask  **
  - **IAM action:**  [iotsitewise:DeleteTask](#list_iotsitewise-action-DeleteTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTimeSeries  **
  - **IAM action:**  [iotsitewise:DeleteTimeSeries](#list_iotsitewise-action-DeleteTimeSeries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspace  **
  - **IAM action:**  [iotsitewise:DeleteWorkspace](#list_iotsitewise-action-DeleteWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccessPolicy  **
  - **IAM action:**  [iotsitewise:DescribeAccessPolicy](#list_iotsitewise-action-DescribeAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAction  **
  - **IAM action:**  [iotsitewise:DescribeAction](#list_iotsitewise-action-DescribeAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApplication  **
  - **IAM action:**  [iotsitewise:DescribeApplication](#list_iotsitewise-action-DescribeApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAsset  **
  - **IAM action:**  [iotsitewise:DescribeAsset](#list_iotsitewise-action-DescribeAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssetCompositeModel  **
  - **IAM action:**  [iotsitewise:DescribeAssetCompositeModel](#list_iotsitewise-action-DescribeAssetCompositeModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssetModel  **
  - **IAM action:**  [iotsitewise:DescribeAssetModel](#list_iotsitewise-action-DescribeAssetModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssetModelCompositeModel  **
  - **IAM action:**  [iotsitewise:DescribeAssetModelCompositeModel](#list_iotsitewise-action-DescribeAssetModelCompositeModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssetModelInterfaceRelationship  **
  - **IAM action:**  [iotsitewise:DescribeAssetModelInterfaceRelationship](#list_iotsitewise-action-DescribeAssetModelInterfaceRelationship) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssetProperty  **
  - **IAM action:**  [iotsitewise:DescribeAssetProperty](#list_iotsitewise-action-DescribeAssetProperty) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBulkImportJob  **
  - **IAM action:**  [iotsitewise:DescribeBulkImportJob](#list_iotsitewise-action-DescribeBulkImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeComputationModel  **
  - **IAM action:**  [iotsitewise:DescribeComputationModel](#list_iotsitewise-action-DescribeComputationModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeComputationModelExecutionSummary  **
  - **IAM action:**  [iotsitewise:DescribeComputationModelExecutionSummary](#list_iotsitewise-action-DescribeComputationModelExecutionSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDashboard  **
  - **IAM action:**  [iotsitewise:DescribeDashboard](#list_iotsitewise-action-DescribeDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataset  **
  - **IAM action:**  [iotsitewise:DescribeDataset](#list_iotsitewise-action-DescribeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDatasetExportJob  **
  - **IAM action:**  [iotsitewise:DescribeDatasetExportJob](#list_iotsitewise-action-DescribeDatasetExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDefaultEncryptionConfiguration  **
  - **IAM action:**  [iotsitewise:DescribeDefaultEncryptionConfiguration](#list_iotsitewise-action-DescribeDefaultEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEnrichmentJob  **
  - **IAM action:**  [iotsitewise:DescribeEnrichmentJob](#list_iotsitewise-action-DescribeEnrichmentJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExecution  **
  - **IAM action:**  [iotsitewise:DescribeExecution](#list_iotsitewise-action-DescribeExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGateway  **
  - **IAM action:**  [iotsitewise:DescribeGateway](#list_iotsitewise-action-DescribeGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGatewayCapabilityConfiguration  **
  - **IAM action:**  [iotsitewise:DescribeGatewayCapabilityConfiguration](#list_iotsitewise-action-DescribeGatewayCapabilityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLoggingOptions  **
  - **IAM action:**  [iotsitewise:DescribeLoggingOptions](#list_iotsitewise-action-DescribeLoggingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePipeline  **
  - **IAM action:**  [iotsitewise:DescribePipeline](#list_iotsitewise-action-DescribePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePipelineExecution  **
  - **IAM action:**  [iotsitewise:DescribePipelineExecution](#list_iotsitewise-action-DescribePipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePortal  **
  - **IAM action:**  [iotsitewise:DescribePortal](#list_iotsitewise-action-DescribePortal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProject  **
  - **IAM action:**  [iotsitewise:DescribeProject](#list_iotsitewise-action-DescribeProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeQuery  **
  - **IAM action:**  [iotsitewise:DescribeQuery](#list_iotsitewise-action-DescribeQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSearch  **
  - **IAM action:**  [iotsitewise:DescribeSearch](#list_iotsitewise-action-DescribeSearch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStorageConfiguration  **
  - **IAM action:**  [iotsitewise:DescribeStorageConfiguration](#list_iotsitewise-action-DescribeStorageConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTask  **
  - **IAM action:**  [iotsitewise:DescribeTask](#list_iotsitewise-action-DescribeTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTimeSeries  **
  - **IAM action:**  [iotsitewise:DescribeTimeSeries](#list_iotsitewise-action-DescribeTimeSeries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspace  **
  - **IAM action:**  [iotsitewise:DescribeWorkspace](#list_iotsitewise-action-DescribeWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateAssets  **
  - **IAM action:**  [iotsitewise:DisassociateAssets](#list_iotsitewise-action-DisassociateAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateTimeSeriesFromAssetProperty  **
  - **IAM action:**  [iotsitewise:DisassociateTimeSeriesFromAssetProperty](#list_iotsitewise-action-DisassociateTimeSeriesFromAssetProperty) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteAction  **
  - **IAM action:**  [iotsitewise:ExecuteAction](#list_iotsitewise-action-ExecuteAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteQuery  **
  - **IAM action:**  [iotsitewise:ExecuteQuery](#list_iotsitewise-action-ExecuteQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssetPropertyAggregates  **
  - **IAM action:**  [iotsitewise:GetAssetPropertyAggregates](#list_iotsitewise-action-GetAssetPropertyAggregates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssetPropertyValue  **
  - **IAM action:**  [iotsitewise:GetAssetPropertyValue](#list_iotsitewise-action-GetAssetPropertyValue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssetPropertyValueHistory  **
  - **IAM action:**  [iotsitewise:GetAssetPropertyValueHistory](#list_iotsitewise-action-GetAssetPropertyValueHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCaptureData  **
  - **IAM action:**  [iotsitewise:GetCaptureData](#list_iotsitewise-action-GetCaptureData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInterpolatedAssetPropertyValues  **
  - **IAM action:**  [iotsitewise:GetInterpolatedAssetPropertyValues](#list_iotsitewise-action-GetInterpolatedAssetPropertyValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryResults  **
  - **IAM action:**  [iotsitewise:GetQueryResults](#list_iotsitewise-action-GetQueryResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSearchResults  **
  - **IAM action:**  [iotsitewise:GetSearchResults](#list_iotsitewise-action-GetSearchResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeAssistant  **
  - **IAM action:**  [iotsitewise:InvokeAssistant](#list_iotsitewise-action-InvokeAssistant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessPolicies  **
  - **IAM action:**  [iotsitewise:ListAccessPolicies](#list_iotsitewise-action-ListAccessPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListActions  **
  - **IAM action:**  [iotsitewise:ListActions](#list_iotsitewise-action-ListActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplications  **
  - **IAM action:**  [iotsitewise:ListApplications](#list_iotsitewise-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetModelCompositeModels  **
  - **IAM action:**  [iotsitewise:ListAssetModelCompositeModels](#list_iotsitewise-action-ListAssetModelCompositeModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetModelProperties  **
  - **IAM action:**  [iotsitewise:ListAssetModelProperties](#list_iotsitewise-action-ListAssetModelProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetModels  **
  - **IAM action:**  [iotsitewise:ListAssetModels](#list_iotsitewise-action-ListAssetModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetProperties  **
  - **IAM action:**  [iotsitewise:ListAssetProperties](#list_iotsitewise-action-ListAssetProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetRelationships  **
  - **IAM action:**  [iotsitewise:ListAssetRelationships](#list_iotsitewise-action-ListAssetRelationships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssets  **
  - **IAM action:**  [iotsitewise:ListAssets](#list_iotsitewise-action-ListAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociatedAssets  **
  - **IAM action:**  [iotsitewise:ListAssociatedAssets](#list_iotsitewise-action-ListAssociatedAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBulkImportJobs  **
  - **IAM action:**  [iotsitewise:ListBulkImportJobs](#list_iotsitewise-action-ListBulkImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCompositionRelationships  **
  - **IAM action:**  [iotsitewise:ListCompositionRelationships](#list_iotsitewise-action-ListCompositionRelationships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComputationModelDataBindingUsages  **
  - **IAM action:**  [iotsitewise:ListComputationModelDataBindingUsages](#list_iotsitewise-action-ListComputationModelDataBindingUsages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComputationModelResolveToResources  **
  - **IAM action:**  [iotsitewise:ListComputationModelResolveToResources](#list_iotsitewise-action-ListComputationModelResolveToResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComputationModels  **
  - **IAM action:**  [iotsitewise:ListComputationModels](#list_iotsitewise-action-ListComputationModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDashboards  **
  - **IAM action:**  [iotsitewise:ListDashboards](#list_iotsitewise-action-ListDashboards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasetDataSegmentRelationships  **
  - **IAM action:**  [iotsitewise:ListDatasetDataSegmentRelationships](#list_iotsitewise-action-ListDatasetDataSegmentRelationships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasetDataSegments  **
  - **IAM action:**  [iotsitewise:ListDatasetDataSegments](#list_iotsitewise-action-ListDatasetDataSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasetExportJobs  **
  - **IAM action:**  [iotsitewise:ListDatasetExportJobs](#list_iotsitewise-action-ListDatasetExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasets  **
  - **IAM action:**  [iotsitewise:ListDatasets](#list_iotsitewise-action-ListDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnrichmentJobs  **
  - **IAM action:**  [iotsitewise:ListEnrichmentJobs](#list_iotsitewise-action-ListEnrichmentJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExecutions  **
  - **IAM action:**  [iotsitewise:ListExecutions](#list_iotsitewise-action-ListExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGateways  **
  - **IAM action:**  [iotsitewise:ListGateways](#list_iotsitewise-action-ListGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInterfaceRelationships  **
  - **IAM action:**  [iotsitewise:ListInterfaceRelationships](#list_iotsitewise-action-ListInterfaceRelationships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelineExecutions  **
  - **IAM action:**  [iotsitewise:ListPipelineExecutions](#list_iotsitewise-action-ListPipelineExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelines  **
  - **IAM action:**  [iotsitewise:ListPipelines](#list_iotsitewise-action-ListPipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPortals  **
  - **IAM action:**  [iotsitewise:ListPortals](#list_iotsitewise-action-ListPortals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProjectAssets  **
  - **IAM action:**  [iotsitewise:ListProjectAssets](#list_iotsitewise-action-ListProjectAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProjects  **
  - **IAM action:**  [iotsitewise:ListProjects](#list_iotsitewise-action-ListProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQueries  **
  - **IAM action:**  [iotsitewise:ListQueries](#list_iotsitewise-action-ListQueries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSearches  **
  - **IAM action:**  [iotsitewise:ListSearches](#list_iotsitewise-action-ListSearches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [iotsitewise:ListTagsForResource](#list_iotsitewise-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTasks  **
  - **IAM action:**  [iotsitewise:ListTasks](#list_iotsitewise-action-ListTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTimeSeries  **
  - **IAM action:**  [iotsitewise:ListTimeSeries](#list_iotsitewise-action-ListTimeSeries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkspaces  **
  - **IAM action:**  [iotsitewise:ListWorkspaces](#list_iotsitewise-action-ListWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAssetModelInterfaceRelationship  **
  - **IAM action:**  [iotsitewise:PutAssetModelInterfaceRelationship](#list_iotsitewise-action-PutAssetModelInterfaceRelationship) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDefaultEncryptionConfiguration  **
  - **IAM action:**  [iotsitewise:PutDefaultEncryptionConfiguration](#list_iotsitewise-action-PutDefaultEncryptionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutLoggingOptions  **
  - **IAM action:**  [iotsitewise:PutLoggingOptions](#list_iotsitewise-action-PutLoggingOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutStorageConfiguration  **
  - **IAM action:**  [iotsitewise:PutStorageConfiguration](#list_iotsitewise-action-PutStorageConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   StartPipelineExecution  **
  - **IAM action:**  [iotsitewise:StartPipelineExecution](#list_iotsitewise-action-StartPipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartQuery  **
  - **IAM action:**  [iotsitewise:StartQuery](#list_iotsitewise-action-StartQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSearch  **
  - **IAM action:**  [iotsitewise:StartSearch](#list_iotsitewise-action-StartSearch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [iotsitewise:TagResource](#list_iotsitewise-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [iotsitewise:UntagResource](#list_iotsitewise-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccessPolicy  **
  - **IAM action:**  [iotsitewise:UpdateAccessPolicy](#list_iotsitewise-action-UpdateAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAsset  **
  - **IAM action:**  [iotsitewise:UpdateAsset](#list_iotsitewise-action-UpdateAsset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssetModel  **
  - **IAM action:**  [iotsitewise:UpdateAssetModel](#list_iotsitewise-action-UpdateAssetModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssetModelCompositeModel  **
  - **IAM action:**  [iotsitewise:UpdateAssetModelCompositeModel](#list_iotsitewise-action-UpdateAssetModelCompositeModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   UpdateAssetProperty  **
  - **IAM action:**  [iotsitewise:UpdateAssetProperty](#list_iotsitewise-action-UpdateAssetProperty) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateComputationModel  **
  - **IAM action:**  [iotsitewise:UpdateComputationModel](#list_iotsitewise-action-UpdateComputationModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDashboard  **
  - **IAM action:**  [iotsitewise:UpdateDashboard](#list_iotsitewise-action-UpdateDashboard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataset  **
  - **IAM action:**  [iotsitewise:UpdateDataset](#list_iotsitewise-action-UpdateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   UpdateGateway  **
  - **IAM action:**  [iotsitewise:UpdateGateway](#list_iotsitewise-action-UpdateGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGatewayCapabilityConfiguration  **
  - **IAM action:**  [iotsitewise:UpdateGatewayCapabilityConfiguration](#list_iotsitewise-action-UpdateGatewayCapabilityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePipeline  **
  - **IAM action:**  [iotsitewise:UpdatePipeline](#list_iotsitewise-action-UpdatePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePortal  **
  - **IAM action:**  [iotsitewise:UpdatePortal](#list_iotsitewise-action-UpdatePortal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   UpdateProject  **
  - **IAM action:**  [iotsitewise:UpdateProject](#list_iotsitewise-action-UpdateProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTask  **
  - **IAM action:**  [iotsitewise:UpdateTask](#list_iotsitewise-action-UpdateTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** iotsitewise.amazonaws.com / **Access level:** Write

- **   UpdateWorkspace  **
  - **IAM action:**  [iotsitewise:UpdateWorkspace](#list_iotsitewise-action-UpdateWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS IoT SiteWise
<a name="list_iotsitewise-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssociateAssets.html)  **
  - **Description:** Grants permission to associate a child asset with a parent asset through a hierarchy
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateTimeSeriesToAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssociateTimeSeriesToAssetProperty.html)  **
  - **Description:** Grants permission to associate a time series with an asset property
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series\*](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAssociateDataSegmentsToDataset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchAssociateDataSegmentsToDataset.html)  **
  - **Description:** Grants permission to associate data segments to a dataset
  - **Resource types (\*required):** [dataset\*](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAssociateProjectAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchAssociateProjectAssets.html)  **
  - **Description:** Grants permission to associate assets to a project
  - **Resource types (\*required):** [project\*](#list_iotsitewise-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteDatasetDataSegments](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchDeleteDatasetDataSegments.html)  **
  - **Description:** Grants permission to batch delete data segments from a dataset
  - **Resource types (\*required):** [dataset\*](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisassociateDataSegmentsFromDataset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchDisassociateDataSegmentsFromDataset.html)  **
  - **Description:** Grants permission to disassociate data segments from a dataset
  - **Resource types (\*required):** [dataset\*](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisassociateProjectAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchDisassociateProjectAssets.html)  **
  - **Description:** Grants permission to disassociate assets from a project
  - **Resource types (\*required):** [project\*](#list_iotsitewise-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html)  **
  - **Description:** Grants permission to retrieve computed aggregates for multiple asset properties
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValue.html)  **
  - **Description:** Grants permission to retrieve the latest value for multiple asset properties
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetAssetPropertyValueHistory](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueHistory.html)  **
  - **Description:** Grants permission to retrieve the value history for multiple asset properties
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html)  **
  - **Description:** Grants permission to put property values for asset properties
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelEnrichmentJob](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CancelEnrichmentJob.html)  **
  - **Description:** Grants permission to cancel an enrichment job
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelPipelineExecution](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CancelPipelineExecution.html)  **
  - **Description:** Grants permission to cancel a pipeline execution in a workspace
  - **Resource types (\*required):** [pipeline\*](#list_iotsitewise-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelQuery](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CancelQuery.html)  **
  - **Description:** Grants permission to cancel a query
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAccessPolicy.html)  **
  - **Description:** Grants permission to create an access policy for a portal or a project
  - **Resource types (\*required):** [portal](#list_iotsitewise-resource-portal) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_iotsitewise-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAsset.html)  **
  - **Description:** Grants permission to create an asset from an asset model
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html)  **
  - **Description:** Grants permission to create an asset model
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html)  **
  - **Description:** Grants permission to create an asset model composite model inside an asset model
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBulkImportJob](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateBulkImportJob.html)  **
  - **Description:** Grants permission to create bulk import job
  - **Resource types (\*required):** [dataset](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateComputationModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateComputationModel.html)  **
  - **Description:** Grants permission to create a computation model
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [asset-model](#list_iotsitewise-resource-asset-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDashboard.html)  **
  - **Description:** Grants permission to create a dashboard in a project
  - **Resource types (\*required):** [project\*](#list_iotsitewise-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a dataset
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDatasetExportJob](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDatasetExportJob.html)  **
  - **Description:** Grants permission to create a dataset export job
  - **Resource types (\*required):** [dataset](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEnrichmentJob](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateEnrichmentJob.html)  **
  - **Description:** Grants permission to create an enrichment job
  - **Resource types (\*required):** [dataset](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateGateway.html)  **
  - **Description:** Grants permission to create a gateway
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePipeline](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePipeline.html)  **
  - **Description:** Grants permission to create a new pipeline definition in a workspace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)<br />[iotsitewise:taskArns](#list_iotsitewise-iotsitewise_taskArns)
  - **Access level:** Write

- **   [CreatePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePortal.html)  **
  - **Description:** Grants permission to create a portal
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create a project in a portal
  - **Resource types (\*required):** [portal\*](#list_iotsitewise-resource-portal)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTask](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateTask.html)  **
  - **Description:** Grants permission to create a new task definition in a workspace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkspace](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateWorkspace.html)  **
  - **Description:** Grants permission to create a workspace
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAccessPolicy.html)  **
  - **Description:** Grants permission to delete an access policy
  - **Resource types (\*required):** [access-policy\*](#list_iotsitewise-resource-access-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [application\*](#list_iotsitewise-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAsset.html)  **
  - **Description:** Grants permission to delete an asset
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAssetModel.html)  **
  - **Description:** Grants permission to delete an asset model
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAssetModelCompositeModel.html)  **
  - **Description:** Grants permission to delete an asset model composite model
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssetModelInterfaceRelationship](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAssetModelInterfaceRelationship.html)  **
  - **Description:** Grants permission to delete a relationship between asset model and interface
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteComputationModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteComputationModel.html)  **
  - **Description:** Grants permission to delete a computation model
  - **Resource types (\*required):** [computation-model\*](#list_iotsitewise-resource-computation-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteDashboard.html)  **
  - **Description:** Grants permission to delete a dashboard
  - **Resource types (\*required):** [dashboard\*](#list_iotsitewise-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** [dataset\*](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteGateway.html)  **
  - **Description:** Grants permission to delete a gateway
  - **Resource types (\*required):** [gateway\*](#list_iotsitewise-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePipeline](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeletePipeline.html)  **
  - **Description:** Grants permission to delete a pipeline definition from a workspace
  - **Resource types (\*required):** [pipeline\*](#list_iotsitewise-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeletePortal.html)  **
  - **Description:** Grants permission to delete a portal
  - **Resource types (\*required):** [portal\*](#list_iotsitewise-resource-portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a project
  - **Resource types (\*required):** [project\*](#list_iotsitewise-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTask](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteTask.html)  **
  - **Description:** Grants permission to delete a task definition from a workspace
  - **Resource types (\*required):** [task\*](#list_iotsitewise-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTimeSeries](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteTimeSeries.html)  **
  - **Description:** Grants permission to delete a time series
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkspace](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteWorkspace.html)  **
  - **Description:** Grants permission to delete a workspace
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAccessPolicy.html)  **
  - **Description:** Grants permission to describe an access policy
  - **Resource types (\*required):** [access-policy\*](#list_iotsitewise-resource-access-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAction](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAction.html)  **
  - **Description:** Grants permission to describe actions
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computation-model](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeApplication](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeApplication.html)  **
  - **Description:** Grants permission to describe an application
  - **Resource types (\*required):** [application\*](#list_iotsitewise-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html)  **
  - **Description:** Grants permission to describe an asset
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAssetCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetCompositeModel.html)  **
  - **Description:** Grants permission to describe an asset composite model
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html)  **
  - **Description:** Grants permission to describe an asset model
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModelCompositeModel.html)  **
  - **Description:** Grants permission to describe an asset model composite model
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAssetModelInterfaceRelationship](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModelInterfaceRelationship.html)  **
  - **Description:** Grants permission to describe a relationship between asset model and interface
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html)  **
  - **Description:** Grants permission to describe an asset property
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBulkImportJob](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeBulkImportJob.html)  **
  - **Description:** Grants permission to describe bulk import job
  - **Resource types (\*required):** [dataset](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeComputationModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeComputationModel.html)  **
  - **Description:** Grants permission to describe a computation model
  - **Resource types (\*required):** [computation-model\*](#list_iotsitewise-resource-computation-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeComputationModelExecutionSummary](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeComputationModelExecutionSummary.html)  **
  - **Description:** Grants permission to describe computation model execution summary
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computation-model\*](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDashboard.html)  **
  - **Description:** Grants permission to describe a dashboard
  - **Resource types (\*required):** [dashboard\*](#list_iotsitewise-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDataset.html)  **
  - **Description:** Grants permission to describe dataset
  - **Resource types (\*required):** [dataset\*](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDatasetExportJob](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDatasetExportJob.html)  **
  - **Description:** Grants permission to describe a dataset export job
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDefaultEncryptionConfiguration.html)  **
  - **Description:** Grants permission to describe the default encryption configuration for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEnrichmentJob](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeEnrichmentJob.html)  **
  - **Description:** Grants permission to describe an enrichment job
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExecution](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeExecution.html)  **
  - **Description:** Grants permission to describe an execution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html)  **
  - **Description:** Grants permission to describe a gateway
  - **Resource types (\*required):** [gateway\*](#list_iotsitewise-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGatewayCapabilityConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html)  **
  - **Description:** Grants permission to describe a capability configuration for a gateway
  - **Resource types (\*required):** [gateway\*](#list_iotsitewise-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLoggingOptions](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeLoggingOptions.html)  **
  - **Description:** Grants permission to describe logging options for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePipeline](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePipeline.html)  **
  - **Description:** Grants permission to retrieve detailed information about a pipeline in a workspace
  - **Resource types (\*required):** [pipeline\*](#list_iotsitewise-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePipelineExecution](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePipelineExecution.html)  **
  - **Description:** Grants permission to retrieve detailed information about a pipeline execution
  - **Resource types (\*required):** [pipeline\*](#list_iotsitewise-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePortal.html)  **
  - **Description:** Grants permission to describe a portal
  - **Resource types (\*required):** [portal\*](#list_iotsitewise-resource-portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeProject.html)  **
  - **Description:** Grants permission to describe a project
  - **Resource types (\*required):** [project\*](#list_iotsitewise-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeQuery](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeQuery.html)  **
  - **Description:** Grants permission to describe a query
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSearch](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeSearch.html)  **
  - **Description:** Grants permission to describe a search
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeStorageConfiguration.html)  **
  - **Description:** Grants permission to describe the storage configuration for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTask](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTask.html)  **
  - **Description:** Grants permission to retrieve detailed information about a task in a workspace
  - **Resource types (\*required):** [task\*](#list_iotsitewise-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTimeSeries](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTimeSeries.html)  **
  - **Description:** Grants permission to describe a time series
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeWorkspace](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeWorkspace.html)  **
  - **Description:** Grants permission to describe a workspace
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateAssets.html)  **
  - **Description:** Grants permission to disassociate a child asset from a parent asset by a hierarchy
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateTimeSeriesFromAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateTimeSeriesFromAssetProperty.html)  **
  - **Description:** Grants permission to disassociate a time series from an asset property
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series\*](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExecuteAction](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExecuteAction.html)  **
  - **Description:** Grants permission to execute actions
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computation-model](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExecuteQuery](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ExecuteQuery.html)  **
  - **Description:** Grants permission to execute query
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyAggregates.html)  **
  - **Description:** Grants permission to retrieve computed aggregates for an asset property
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html)  **
  - **Description:** Grants permission to retrieve the latest value for an asset property
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssetPropertyValueHistory](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValueHistory.html)  **
  - **Description:** Grants permission to retrieve the value history for an asset property
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCaptureData](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetCaptureData.html)  **
  - **Description:** Grants permission to retrieve captured data
  - **Resource types (\*required):** [time-series\*](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInterpolatedAssetPropertyValues](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetInterpolatedAssetPropertyValues.html)  **
  - **Description:** Grants permission to retrieve interpolated values for an asset property
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueryResults](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetQueryResults.html)  **
  - **Description:** Grants permission to retrieve query results
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSearchResults](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetSearchResults.html)  **
  - **Description:** Grants permission to retrieve search results
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeAssistant](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_InvokeAssistant.html)  **
  - **Description:** Grants permission to invoke an assistant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAccessPolicies](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAccessPolicies.html)  **
  - **Description:** Grants permission to list all access policies for an identity or a resource
  - **Resource types (\*required):** [portal](#list_iotsitewise-resource-portal) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [project](#list_iotsitewise-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListActions](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListActions.html)  **
  - **Description:** Grants permission to list all actions
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computation-model](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApplications](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to list all applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssetModelCompositeModels](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModelCompositeModels.html)  **
  - **Description:** Grants permission to list all asset model composite models
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssetModelProperties](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModelProperties.html)  **
  - **Description:** Grants permission to list asset model properties
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssetModels](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html)  **
  - **Description:** Grants permission to list all asset models
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssetProperties](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetProperties.html)  **
  - **Description:** Grants permission to list asset properties
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssetRelationships](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetRelationships.html)  **
  - **Description:** Grants permission to list the asset relationship graph for an asset
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssets.html)  **
  - **Description:** Grants permission to list all assets
  - **Resource types (\*required):** [asset-model](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssociatedAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssociatedAssets.html)  **
  - **Description:** Grants permission to list all assets associated with an asset through a hierarchy
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBulkImportJobs](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListBulkImportJobs.html)  **
  - **Description:** Grants permission to list bulk import jobs
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCompositionRelationships](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListCompositionRelationships.html)  **
  - **Description:** Grants permission to list all asset model composition relationships
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListComputationModelDataBindingUsages](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListComputationModelDataBindingUsages.html)  **
  - **Description:** Grants permission to list computation model data binding usages
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [asset-model](#list_iotsitewise-resource-asset-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListComputationModelResolveToResources](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListComputationModelResolveToResources.html)  **
  - **Description:** Grants permission to list computation model resolve to resources
  - **Resource types (\*required):** [computation-model\*](#list_iotsitewise-resource-computation-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListComputationModels](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListComputationModels.html)  **
  - **Description:** Grants permission to list all computation models
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDashboards](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListDashboards.html)  **
  - **Description:** Grants permission to list all dashboards in a project
  - **Resource types (\*required):** [project\*](#list_iotsitewise-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatasetDataSegmentRelationships](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListDatasetDataSegmentRelationships.html)  **
  - **Description:** Grants permission to list dataset data segment relationships
  - **Resource types (\*required):** [dataset\*](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatasetDataSegments](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListDatasetDataSegments.html)  **
  - **Description:** Grants permission to list data segments for a dataset
  - **Resource types (\*required):** [dataset\*](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatasetExportJobs](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListDatasetExportJobs.html)  **
  - **Description:** Grants permission to list dataset export jobs
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatasets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListDatasets.html)  **
  - **Description:** Grants permission to list all datasets
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnrichmentJobs](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListEnrichmentJobs.html)  **
  - **Description:** Grants permission to list enrichment jobs
  - **Resource types (\*required):** [dataset](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExecutions](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListExecutions.html)  **
  - **Description:** Grants permission to list executions
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computation-model](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGateways](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListGateways.html)  **
  - **Description:** Grants permission to list all gateways
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInterfaceRelationships](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListInterfaceRelationships.html)  **
  - **Description:** Grants permission to list all asset models that are enforced by an interface
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPipelineExecutions](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListPipelineExecutions.html)  **
  - **Description:** Grants permission to list pipeline executions for a pipeline in a workspace
  - **Resource types (\*required):** [pipeline\*](#list_iotsitewise-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPipelines](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListPipelines.html)  **
  - **Description:** Grants permission to list pipeline definitions in a workspace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPortals](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListPortals.html)  **
  - **Description:** Grants permission to list all portals
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProjectAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListProjectAssets.html)  **
  - **Description:** Grants permission to list all assets associated with a project
  - **Resource types (\*required):** [project\*](#list_iotsitewise-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProjects](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListProjects.html)  **
  - **Description:** Grants permission to list all projects in a portal
  - **Resource types (\*required):** [portal\*](#list_iotsitewise-resource-portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListQueries](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListQueries.html)  **
  - **Description:** Grants permission to list queries
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSearches](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListSearches.html)  **
  - **Description:** Grants permission to list searches
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for a resource
  - **Resource types (\*required):** [access-policy](#list_iotsitewise-resource-access-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [application](#list_iotsitewise-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [asset-model](#list_iotsitewise-resource-asset-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computation-model](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dashboard](#list_iotsitewise-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [gateway](#list_iotsitewise-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pipeline](#list_iotsitewise-resource-pipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [portal](#list_iotsitewise-resource-portal) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [project](#list_iotsitewise-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task](#list_iotsitewise-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTasks](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListTasks.html)  **
  - **Description:** Grants permission to list task definitions in a workspace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTimeSeries](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListTimeSeries.html)  **
  - **Description:** Grants permission to list time series
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkspaces](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListWorkspaces.html)  **
  - **Description:** Grants permission to list all workspaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutAssetModelInterfaceRelationship](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutAssetModelInterfaceRelationship.html)  **
  - **Description:** Grants permission to create a relationship between asset model and interface
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutDefaultEncryptionConfiguration.html)  **
  - **Description:** Grants permission to set the default encryption configuration for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutLoggingOptions](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutLoggingOptions.html)  **
  - **Description:** Grants permission to set logging options for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html)  **
  - **Description:** Grants permission to configure storage settings for the AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartPipelineExecution](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_StartPipelineExecution.html)  **
  - **Description:** Grants permission to start execution of a pipeline in a workspace
  - **Resource types (\*required):** [pipeline\*](#list_iotsitewise-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartQuery](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_StartQuery.html)  **
  - **Description:** Grants permission to start a query on sensor data
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSearch](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_StartSearch.html)  **
  - **Description:** Grants permission to start a search
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [access-policy](#list_iotsitewise-resource-access-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [application](#list_iotsitewise-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [asset-model](#list_iotsitewise-resource-asset-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [computation-model](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_iotsitewise-resource-dashboard) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [gateway](#list_iotsitewise-resource-gateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [pipeline](#list_iotsitewise-resource-pipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [portal](#list_iotsitewise-resource-portal) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_iotsitewise-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [task](#list_iotsitewise-resource-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotsitewise-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [access-policy](#list_iotsitewise-resource-access-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [application](#list_iotsitewise-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [asset-model](#list_iotsitewise-resource-asset-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [computation-model](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [dashboard](#list_iotsitewise-resource-dashboard) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [gateway](#list_iotsitewise-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [pipeline](#list_iotsitewise-resource-pipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [portal](#list_iotsitewise-resource-portal) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_iotsitewise-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [task](#list_iotsitewise-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [time-series](#list_iotsitewise-resource-time-series) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotsitewise-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAccessPolicy.html)  **
  - **Description:** Grants permission to update an access policy
  - **Resource types (\*required):** [access-policy\*](#list_iotsitewise-resource-access-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAsset.html)  **
  - **Description:** Grants permission to update an asset
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html)  **
  - **Description:** Grants permission to update an asset model
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModelCompositeModel.html)  **
  - **Description:** Grants permission to update asset model composite model
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html)  **
  - **Description:** Grants permission to update an asset property
  - **Resource types (\*required):** [asset\*](#list_iotsitewise-resource-asset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateComputationModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateComputationModel.html)  **
  - **Description:** Grants permission to update a computation model
  - **Resource types (\*required):** [asset](#list_iotsitewise-resource-asset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [asset-model](#list_iotsitewise-resource-asset-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [computation-model\*](#list_iotsitewise-resource-computation-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateDashboard.html)  **
  - **Description:** Grants permission to update a dashboard
  - **Resource types (\*required):** [dashboard\*](#list_iotsitewise-resource-dashboard)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateDataset.html)  **
  - **Description:** Grants permission to update a dataset
  - **Resource types (\*required):** [dataset\*](#list_iotsitewise-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspace](#list_iotsitewise-resource-workspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateGateway.html)  **
  - **Description:** Grants permission to update a gateway
  - **Resource types (\*required):** [gateway\*](#list_iotsitewise-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGatewayCapabilityConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateGatewayCapabilityConfiguration.html)  **
  - **Description:** Grants permission to update a capability configuration for a gateway
  - **Resource types (\*required):** [gateway\*](#list_iotsitewise-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePipeline](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdatePipeline.html)  **
  - **Description:** Grants permission to update an existing pipeline definition in a workspace
  - **Resource types (\*required):** [pipeline\*](#list_iotsitewise-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)<br />[iotsitewise:taskArns](#list_iotsitewise-iotsitewise_taskArns)
  - **Access level:** Write

- **   [UpdatePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdatePortal.html)  **
  - **Description:** Grants permission to update a portal
  - **Resource types (\*required):** [portal\*](#list_iotsitewise-resource-portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateProject.html)  **
  - **Description:** Grants permission to update a project
  - **Resource types (\*required):** [project\*](#list_iotsitewise-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTask](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateTask.html)  **
  - **Description:** Grants permission to update an existing task definition in a workspace
  - **Resource types (\*required):** [task\*](#list_iotsitewise-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkspace](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateWorkspace.html)  **
  - **Description:** Grants permission to update a workspace
  - **Resource types (\*required):** [workspace\*](#list_iotsitewise-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS IoT SiteWise
<a name="list_iotsitewise-permission-only-actions"></a>

The following actions are defined by AWS IoT SiteWise but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [EnableSiteWiseIntegration](${UserGuideDocPage}/integrate-tm.html)  **
  - **Description:** Grants permission to allow IoT SiteWise integrate with other services
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAssetModelPropertyRouting](${UserGuideDocPage}alarms-iam-permissions.html)  **
  - **Description:** Grants permission to update an AssetModel property routing
  - **Resource types (\*required):** [asset-model\*](#list_iotsitewise-resource-asset-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS IoT SiteWise
<a name="list_iotsitewise-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [access-policy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAccessPolicy.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [application](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateApplication.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:workspace/${WorkspaceName}/application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [asset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAsset.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [asset-model](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [computation-model](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateComputationModel.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [dashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDashboard.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [dataset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDataset.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [gateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateGateway.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [pipeline](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePipeline.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:workspace/${WorkspaceName}/pipeline/${PipelineName} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [portal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePortal.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [project](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateProject.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [task](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateTask.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:workspace/${WorkspaceName}/task/${TaskName} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [time-series](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTimeSeries.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:time-series/${TimeSeriesId} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 
|  [workspace](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateWorkspace.html)  | arn:${Partition}:iotsitewise:${Region}:${Account}:workspace/${WorkspaceName} | [aws:ResourceTag/${TagKey}](#list_iotsitewise-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT SiteWise
<a name="list_iotsitewise-policy-keys"></a>

AWS IoT SiteWise defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in the request | ArrayOfString | 
|   [iotsitewise:assetHierarchyPath](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by an asset hierarchy path, which is the string of asset IDs in the asset's hierarchy, each separated by a forward slash | String | 
|   [iotsitewise:childAssetId](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ID of a child asset being associated whith a parent asset | String | 
|   [iotsitewise:group](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ID of an AWS Single Sign-On group | String | 
|   [iotsitewise:iam](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ID of an AWS IAM identity | String | 
|   [iotsitewise:isAssociatedWithAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by data streams associated with or not associated with asset properties | String | 
|   [iotsitewise:portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ID of a portal | String | 
|   [iotsitewise:project](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ID of a project | String | 
|   [iotsitewise:propertyAlias](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the property alias | String | 
|   [iotsitewise:propertyId](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ID of an asset property | String | 
|   [iotsitewise:taskArns](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the task ARNs specified in the pipeline request | ArrayOfARN | 
|   [iotsitewise:user](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the ID of an AWS Single Sign-On user | String | 