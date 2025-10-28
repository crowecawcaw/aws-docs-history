# Delete asset models, component models, and interfaces in AWS IoT SiteWise

You can use the AWS IoT SiteWise console or API to delete an asset model, component model, or interface.

Before you can delete an asset model, you must first delete all assets that were created
from the asset model. Before you can delete an interface, you must first unlink it from all asset models that implement it.

When you delete an asset model or interface, its status is `DELETING` until the changes
propagate. For more information, see [Asset and model states](asset-and-model-states.md "asset-and-model-states.md"). After the asset model or interface is deleted, you can't query that
asset model or interface. If you do, the API returns an HTTP 404 response.

###### Topics

- [Delete an asset model, component model, or interface (console)](#delete-asset-model-console "#delete-asset-model-console")
- [Delete an asset model, component model, or interface (AWS CLI)](#delete-asset-model-cli "#delete-asset-model-cli")

## Delete an asset model, component model, or interface (console)

You can use the AWS IoT SiteWise console to delete an asset model, component model, or interface.

###### Topics

###### To delete an asset model, component model, or interface (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose the asset model, component model, or interface to delete.
4. If deleting an asset model and it has any **Assets**, delete each asset. Choose an
   asset's name to navigate to its page, where you can delete it. For more information,
   see [Delete an asset (console)](delete-assets.md#delete-asset-console "delete-assets.md#delete-asset-console").
5. On the model's page, choose **Delete**.
6. In the **Delete model** dialog box, do the following:
   1. Enter `Delete` to confirm deletion.
   2. Choose **Delete**.

## Delete an asset model, component model, or interface (AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to delete an asset model, component model, or interface.

Use the [DeleteAssetModel](../APIReference/API_DeleteAssetModel.md "../APIReference/API_DeleteAssetModel.md") operation to delete an asset model, component model, or interface. Specify the following
parameter:

- `assetModelId` – The ID of the asset. This is the actual ID in UUID format, or the `externalId:myExternalId` if it has one.
  For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.

###### To delete an asset model (AWS CLI)

1. Run the following command to list all assets created from the model. Replace
   `asset-model-id` with the ID or the external ID of the asset
   model.

```
aws iotsitewise list-assets --asset-model-id `asset-model-id`
```

For more information, see the [ListAssets](../APIReference/API_ListAssets.md "../APIReference/API_ListAssets.md") operation. 2. If the previous command returns any assets from the model, delete each asset. For
more information, see [Delete an asset (AWS CLI)](delete-assets.md#delete-asset-cli "delete-assets.md#delete-asset-cli"). 3. Run the following command to delete the asset model. Replace
`asset-model-id` with the ID or external ID of the asset
model.

```
aws iotsitewise delete-asset-model --asset-model-id `asset-model-id`
```

###### Important

To avoid deleting an asset model that was concurrently updated since the last read operation, you
must define a conditional delete request. See [Optimistic locking for asset model writes](opt-locking-for-model.md "opt-locking-for-model.md").
