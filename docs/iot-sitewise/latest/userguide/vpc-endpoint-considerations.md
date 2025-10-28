# API operations for VPC endpoints in

AWS IoT SiteWise

AWS IoT SiteWise supports making calls to the following AWS IoT SiteWise API operations from your VPC:

- For all the **data plane** API operations, use the
  following endpoint: Replace
  `region` with your
  AWS Region

```
data.iotsitewise.`region`.amazonaws.com
```

The data plane API operations include the following:

    + [BatchGetAssetPropertyValue](../APIReference/API_BatchGetAssetPropertyValue.md "../APIReference/API_BatchGetAssetPropertyValue.md")
    + [BatchGetAssetPropertyValueHistory](../APIReference/API_BatchGetAssetPropertyValueHistory.md "../APIReference/API_BatchGetAssetPropertyValueHistory.md")
    + [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md")
    + [GetAssetPropertyAggregates](../APIReference/API_GetAssetPropertyAggregates.md "../APIReference/API_GetAssetPropertyAggregates.md")
    + [GetAssetPropertyValue](../APIReference/API_GetAssetPropertyValue.md "../APIReference/API_GetAssetPropertyValue.md")
    + [GetAssetPropertyValueHistory](../APIReference/API_GetAssetPropertyValueHistory.md "../APIReference/API_GetAssetPropertyValueHistory.md")
    + [GetInterpolatedAssetPropertyValues](../APIReference/API_GetInterpolatedAssetPropertyValues.md "../APIReference/API_GetInterpolatedAssetPropertyValues.md")

- For the **control plane** API operations that you use to
  manage asset models, assets, SiteWise Edge gateways, tags, and account configurations, use the
  following endpoint. Replace
  `region` with your
  AWS Region.

```
api.iotsitewise.`region`.amazonaws.com
```

The supported control plane API operations include the following:

    + [AssociateAssets](../APIReference/API_AssociateAssets.md "../APIReference/API_AssociateAssets.md")
    + [CreateAsset](../APIReference/API_CreateAsset.md "../APIReference/API_CreateAsset.md")
    + [CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md")
    + [DeleteAsset](../APIReference/API_DeleteAsset.md "../APIReference/API_DeleteAsset.md")
    + [DeleteAssetModel](../APIReference/API_DeleteAssetModel.md "../APIReference/API_DeleteAssetModel.md")
    + [DeleteDashboard](../APIReference/API_DeleteDashboard.md "../APIReference/API_DeleteDashboard.md")
    + [DescribeAsset](../APIReference/API_DescribeAsset.md "../APIReference/API_DescribeAsset.md")
    + [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md")
    + [DescribeAssetProperty](../APIReference/API_DescribeAssetProperty.md "../APIReference/API_DescribeAssetProperty.md")
    + [DescribeDashboard](../APIReference/API_DescribeDashboard.md "../APIReference/API_DescribeDashboard.md")
    + [DescribeLoggingOptions](../APIReference/API_DescribeLoggingOptions.md "../APIReference/API_DescribeLoggingOptions.md")
    + [DisassociateAssets](../APIReference/API_DisassociateAssets.md "../APIReference/API_DisassociateAssets.md")
    + [ListAssetModels](../APIReference/API_ListAssetModels.md "../APIReference/API_ListAssetModels.md")
    + [ListAssetRelationships](../APIReference/API_ListAssetRelationships.md "../APIReference/API_ListAssetRelationships.md")
    + [ListAssets](../APIReference/API_ListAssets.md "../APIReference/API_ListAssets.md")
    + [ListAssociatedAssets](../APIReference/API_ListAssociatedAssets.md "../APIReference/API_ListAssociatedAssets.md")
    + [PutLoggingOptions](../APIReference/API_PutLoggingOptions.md "../APIReference/API_PutLoggingOptions.md")
    + [UpdateAsset](../APIReference/API_UpdateAsset.md "../APIReference/API_UpdateAsset.md")
    + [UpdateAssetModel](../APIReference/API_UpdateAssetModel.md "../APIReference/API_UpdateAssetModel.md")
    + [UpdateAssetProperty](../APIReference/API_UpdateAssetProperty.md "../APIReference/API_UpdateAssetProperty.md")
    + [CreateGateway](../APIReference/API_CreateGateway.md "../APIReference/API_CreateGateway.md")
    + [DeleteGateway](../APIReference/API_DeleteGateway.md "../APIReference/API_DeleteGateway.md")
    + [DescribeDefaultEncryptionConfiguration](../APIReference/API_DescribeDefaultEncryptionConfiguration.md "../APIReference/API_DescribeDefaultEncryptionConfiguration.md")
    + [DescribeGateway](../APIReference/API_DescribeGateway.md "../APIReference/API_DescribeGateway.md")
    + [DescribeGatewayCapabilityConfiguration](../APIReference/API_DescribeGatewayCapabilityConfiguration.md "../APIReference/API_DescribeGatewayCapabilityConfiguration.md")
    + [DescribeStorageConfiguration](../APIReference/API_DescribeStorageConfiguration.md "../APIReference/API_DescribeStorageConfiguration.md")
    + [ListGateways](../APIReference/API_ListGateways.md "../APIReference/API_ListGateways.md")
    + [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
    + [UpdateGateway](../APIReference/API_UpdateGateway.md "../APIReference/API_UpdateGateway.md")
    + [UpdateGatewayCapabilityConfiguration](../APIReference/API_UpdateGatewayCapabilityConfiguration.md "../APIReference/API_UpdateGatewayCapabilityConfiguration.md")
    + [PutDefaultEncryptionConfiguration](../APIReference/API_PutDefaultEncryptionConfiguration.md "../APIReference/API_PutDefaultEncryptionConfiguration.md")
    + [PutStorageConfiguration](../APIReference/API_PutStorageConfiguration.md "../APIReference/API_PutStorageConfiguration.md")
    + [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
    + [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

###### Note

The interface VPC endpoint for the **control plane**
API operations currently doesn't support making calls to the following SiteWise Monitor API
operations:

    + [BatchAssociateProjectAssets](../APIReference/API_BatchAssociateProjectAssets.md "../APIReference/API_BatchAssociateProjectAssets.md")
    + [BatchDisassociateProjectAssets](../APIReference/API_BatchDisassociateProjectAssets.md "../APIReference/API_BatchDisassociateProjectAssets.md")
    + [CreateAccessPolicy](../APIReference/API_CreateAccessPolicy.md "../APIReference/API_CreateAccessPolicy.md")
    + [CreateDashboard](../APIReference/API_CreateDashboard.md "../APIReference/API_CreateDashboard.md")
    + [CreatePortal](../APIReference/API_CreatePortal.md "../APIReference/API_CreatePortal.md")
    + [CreateProject](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md")
    + [DeleteAccessPolicy](../APIReference/API_DeleteAccessPolicy.md "../APIReference/API_DeleteAccessPolicy.md")
    + [DeletePortal](../APIReference/API_DeletePortal.md "../APIReference/API_DeletePortal.md")
    + [DeleteProject](../APIReference/API_DeleteProject.md "../APIReference/API_DeleteProject.md")
    + [DescribeAccessPolicy](../APIReference/API_DescribeAccessPolicy.md "../APIReference/API_DescribeAccessPolicy.md")
    + [DescribePortal](../APIReference/API_DescribePortal.md "../APIReference/API_DescribePortal.md")
    + [DescribeProject](../APIReference/API_DescribeProject.md "../APIReference/API_DescribeProject.md")
    + [ListAccessPolicies](../APIReference/API_ListAccessPolicies.md "../APIReference/API_ListAccessPolicies.md")
    + [ListDashboards](../APIReference/API_ListDashboards.md "../APIReference/API_ListDashboards.md")
    + [ListPortals](../APIReference/API_ListPortals.md "../APIReference/API_ListPortals.md")
    + [ListProjects](../APIReference/API_ListProjects.md "../APIReference/API_ListProjects.md")
    + [ListProjectAssets](../APIReference/API_ListProjectAssets.md "../APIReference/API_ListProjectAssets.md")
    + [UpdateAccessPolicy](../APIReference/API_UpdateAccessPolicy.md "../APIReference/API_UpdateAccessPolicy.md")
    + [UpdateDashboard](../APIReference/API_UpdateDashboard.md "../APIReference/API_UpdateDashboard.md")
    + [UpdatePortal](../APIReference/API_UpdatePortal.md "../APIReference/API_UpdatePortal.md")
    + [UpdateProject](../APIReference/API_UpdateProject.md "../APIReference/API_UpdateProject.md")
