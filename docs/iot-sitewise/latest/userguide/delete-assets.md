

# Delete assets in AWS IoT SiteWise
<a name="delete-assets"></a>

You can use the AWS IoT SiteWise console or API to delete an asset no longer needed in your environment. Deleting an asset model also deletes all associated assets and component models. However, it's important to note that deleting an asset or model is a permanent action, and any data associated with the deleted resources is also be removed. Before deleting assets or models, it's recommended to review any dependencies or integrations that might be impacted and ensure that you have a backup of any important data.

Before you can delete an asset, you must first disassociate its child assets and disassociate it from its parent asset. For more information, see [Associate and disassociate assets](add-associated-assets.md). If you use the AWS Command Line Interface (AWS CLI), you can use the [ListAssociatedAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssociatedAssets.html) operation to list an asset's children.

When you delete an asset, its status is `DELETING` until the changes propagate. For more information, see [Asset and model states](asset-and-model-states.md). After the asset is deleted, you can't query that asset. If you do, the API returns an HTTP 404 response.

**Important**  
AWS IoT SiteWise deletes all property data for deleted assets.

**Topics**
+ [Delete an asset (console)](#delete-asset-console)
+ [Delete an asset (AWS CLI)](#delete-asset-cli)

## Delete an asset (console)
<a name="delete-asset-console"></a>

You can use the AWS IoT SiteWise console to delete an asset.

**To delete an asset (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. <a name="sitewise-choose-assets"></a>In the navigation pane, choose **Assets**.

1. Choose the asset to delete.
**Tip**  <a name="sitewise-expand-asset-hierarchy"></a>
You can choose the arrow icon to expand an asset hierarchy to find your asset.

1. If the asset has any **Associated assets**, delete each asset. You can choose an asset's name to navigate to its page, where you can delete it.

1. On the asset's page, choose **Delete**.

1. In the **Delete asset** dialog box, do the following:

   1. Enter **Delete** to confirm deletion.

   1. Choose **Delete**.

## Delete an asset (AWS CLI)
<a name="delete-asset-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to delete an asset.

Use the [DeleteAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAsset.html) operation to delete an asset. Specify the following parameter:
+ `assetId` – The ID of the asset. This is the actual ID in UUID format, or the `externalId:myExternalId` if it has one. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references) in the *AWS IoT SiteWise User Guide*.

**To delete an asset (AWS CLI)**

1. Run the following command to list the asset's hierarchies. Replace {{asset-id}} with the ID or the external ID of the asset:

   ```
   aws iotsitewise describe-asset --asset-id {{asset-id}}
   ```

   The operation returns a response that contains the asset's details. The response contains an `assetHierarchies` list that has the following structure:

   ```
   {
     {{...}}
     "assetHierarchies": [
       {
         "id": "{{String}}",
         "name": "{{String}}"
       }
     ],
     {{...}}
   }
   ```

   For more information, see the [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html) operation.

1. For each hierarchy, run the following command to list the asset's children that are associated with that hierarchy. Replace {{asset-id}} with the ID or external ID of the asset and {{hierarchy-id}} with the ID or external ID of the hierarchy.

   ```
   aws iotsitewise list-associated-assets \
     --asset-id {{asset-id}} \
     --hierarchy-id {{hierarchy-id}}
   ```

   For more information, see the [ListAssociatedAssets](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssociatedAssets.html) operation.

1. Run the following command to delete each associated asset and then to delete the asset. Replace {{asset-id}} with the ID or external ID of the asset.

   ```
   aws iotsitewise delete-asset --asset-id {{asset-id}}
   ```