# All available AWS IoT SiteWise Edge device APIs

AWS IoT SiteWise provides a variety of APIs to use on edge devices so that you can complete
tasks locally on the device. Some of the available edge APIs include retrieving
asset models, creating and updating asset properties, and sending data streams to
the cloud. By leveraging these APIs, you can build solutions that can operate in
environments with intermittent or limited network connectivity.

## Available AWS IoT SiteWise APIs

The following AWS IoT SiteWise APIs are available on edge devices:

- [ListAssetModels](../APIReference/API_ListAssetModels.md "../APIReference/API_ListAssetModels.md")
- [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md")
- [ListAssets](../APIReference/API_ListAssets.md "../APIReference/API_ListAssets.md")
- [DescribeAsset](../APIReference/API_DescribeAsset.md "../APIReference/API_DescribeAsset.md")
- [DescribeAssetProperty](../APIReference/API_DescribeAssetProperty.md "../APIReference/API_DescribeAssetProperty.md")
- [ListAssociatedAssets](../APIReference/API_ListAssociatedAssets.md "../APIReference/API_ListAssociatedAssets.md")
- [GetAssetPropertyAggregates](../APIReference/API_GetAssetPropertyAggregates.md "../APIReference/API_GetAssetPropertyAggregates.md")
- [GetAssetPropertyValue](../APIReference/API_GetAssetPropertyValue.md "../APIReference/API_GetAssetPropertyValue.md")
- [GetAssetPropertyValueHistory](../APIReference/API_GetAssetPropertyValueHistory.md "../APIReference/API_GetAssetPropertyValueHistory.md")
- [ListDashboards](../APIReference/API_ListDashboards.md "../APIReference/API_ListDashboards.md")
- [ListPortals](../APIReference/API_ListPortals.md "../APIReference/API_ListPortals.md")
- [ListProjectAssets](../APIReference/API_ListProjectAssets.md "../APIReference/API_ListProjectAssets.md")
- [ListProjects](../APIReference/API_ListProjects.md "../APIReference/API_ListProjects.md")
- [DescribeDashboard](../APIReference/API_DescribeDashboard.md "../APIReference/API_DescribeDashboard.md")
- [DescribePortal](../APIReference/API_DescribePortal.md "../APIReference/API_DescribePortal.md")
- [DescribeProject](../APIReference/API_DescribeProject.md "../APIReference/API_DescribeProject.md")

## Available edge-only APIs

The following APIs are used locally on devices on the edge:

- [Authenticate](edge-local-apis.md#edge-local-apis-authenticate "edge-local-apis.md#edge-local-apis-authenticate") – Use this API
  to get the SigV4 temporary credentials that you'll use to make API
  calls.
