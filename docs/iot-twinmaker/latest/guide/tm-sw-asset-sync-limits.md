

# Asset sync limits
<a name="tm-sw-asset-sync-limits"></a>

**Important**  
See [Differences between custom and default workspaces](tm-sw-default-ws-diffs.md) for information about the differences between the custom and default workspaces.

Because the [AWS IoT SiteWise quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) are higher than the default [AWS IoT TwinMaker quotas](https://docs.aws.amazon.com/general/latest/gr/iot-twinmaker.html), we are increasing the following limits for entities and component types synced from AWS IoT SiteWise.
+ 1000 synced component types in a workspace, since it can only sync 1000 asset models from AWS IoT SiteWise.
+ 100,000 synced entities in a workspace, since it can only sync 100,000 assets from AWS IoT SiteWise.
+ 2000 maximum child entities per parent entity. It syncs 2000 child assets per single parent asset.
**Note**  
The [GetEntity](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetEntity.html) API only returns the first 50 child entities for a hierarchy property, but you can use the [GetPropertyValue](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetPropertyValue.html) API to paginate and retrieve the list of all child entities.
+ 600 properties per synced component from AWS IoT SiteWise, which can sync asset models with 600 total properties and hierarchies.

**Note**  
These limits are only applicable for the synced entities. Request a quota increase if you need these limits increased for non-synced resources.