

# API operations for VPC endpoints in AWS IoT SiteWise
<a name="vpc-endpoint-considerations"></a>

AWS IoT SiteWise supports making calls to the following AWS IoT SiteWise API operations from your VPC:
+ For all the **data plane** API operations, use the following endpoint: Replace `{{region}}` with your AWS Region

  ```
  data.iotsitewise.{{region}}.amazonaws.com
  ```

  The data plane API operations include the following:
  + [BatchGetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValue.html)
  + [BatchGetAssetPropertyValueHistory](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueHistory.html)
  + [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html)
  + [GetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyAggregates.html)
  + [GetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html)
  + [GetAssetPropertyValueHistory](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValueHistory.html)
  + [GetInterpolatedAssetPropertyValues](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetInterpolatedAssetPropertyValues.html)
+ For the **control plane** API operations that you use to manage asset models, assets, SiteWise Edge gateways, tags, and account configurations, use the following endpoint. Replace `{{region}}` with your AWS Region.

  ```
  api.iotsitewise.{{region}}.amazonaws.com
  ```

  The supported control plane API operations include the following:
  + [AssociateAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssociateAssets.html)
  + [CreateAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAsset.html)
  + [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html)
  + [DeleteAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAsset.html)
  + [DeleteAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAssetModel.html)
  + [DeleteDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteDashboard.html)
  + [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html)
  + [DescribeAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html)
  +  [DescribeAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html)
  + [DescribeDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDashboard.html)
  + [DescribeLoggingOptions](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeLoggingOptions.html)
  + [DisassociateAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateAssets.html)
  + [ListAssetModels](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html)
  + [ListAssetRelationships](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetRelationships.html)
  + [ListAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssets.html)
  + [ListAssociatedAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssociatedAssets.html)
  + [PutLoggingOptions](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutLoggingOptions.html)
  + [UpdateAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAsset.html)
  + [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html)
  + [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html)
  + [CreateGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateGateway.html)
  + [DeleteGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteGateway.html)
  + [DescribeDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDefaultEncryptionConfiguration.html)
  + [DescribeGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html)
  + [DescribeGatewayCapabilityConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html)
  + [DescribeStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeStorageConfiguration.html)
  + [ListGateways](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListGateways.html)
  + [ListTagsForResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListTagsForResource.html)
  +  [UpdateGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateGateway.html)
  + [UpdateGatewayCapabilityConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateGatewayCapabilityConfiguration.html)
  + [PutDefaultEncryptionConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutDefaultEncryptionConfiguration.html)
  +  [PutStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html)
  + [TagResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TagResource.html)
  + [UntagResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UntagResource.html)
**Note**  
The interface VPC endpoint for the **control plane** API operations currently doesn't support making calls to the following SiteWise Monitor API operations:  
[BatchAssociateProjectAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchAssociateProjectAssets.html)
[BatchDisassociateProjectAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchDisassociateProjectAssets.html)
[CreateAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAccessPolicy.html)
[CreateDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDashboard.html)
[CreatePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePortal.html)
[CreateProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateProject.html)
[DeleteAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAccessPolicy.html)
[DeletePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeletePortal.html)
[DeleteProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteProject.html)
[DescribeAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAccessPolicy.html)
[DescribePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePortal.html) 
[DescribeProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeProject.html)
[ListAccessPolicies](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAccessPolicies.html)
[ListDashboards](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListDashboards.html) 
[ListPortals](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListPortals.html)
[ListProjects](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListProjects.html) 
[ListProjectAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListProjectAssets.html)
[UpdateAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAccessPolicy.html)
[UpdateDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateDashboard.html)
[UpdatePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdatePortal.html)
[UpdateProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateProject.html)