

# Update assets in AWS IoT SiteWise
<a name="update-assets"></a>

You can use the AWS IoT SiteWise console or API to update an asset's name.

When you update an asset, the asset's status is `UPDATING` until the changes propagate. For more information, see [Asset and model states](asset-and-model-states.md).

**Topics**
+ [Update an asset (console)](#update-asset-console)
+ [Update an asset (AWS CLI)](#update-asset-cli)

## Update an asset (console)
<a name="update-asset-console"></a>

You can use the AWS IoT SiteWise console to update asset details.

**To update an asset (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. <a name="sitewise-choose-assets"></a>In the navigation pane, choose **Assets**.

1. Choose the asset to update.
**Tip**  <a name="sitewise-expand-asset-hierarchy"></a>
You can choose the arrow icon to expand an asset hierarchy to find your asset.

1. Choose **Edit**.

1. Update the asset's **Name**.

1. (Optional) On this page, update other information for the asset. For more information, see the following:
   + [Manage data streams for AWS IoT SiteWise](manage-data-streams.md)
   + [Update attribute values](update-attribute-values.md)
   + [Interact with other AWS services](interact-with-other-services.md)

1. Choose **Save**.

## Update an asset (AWS CLI)
<a name="update-asset-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to update an asset's name.

Use the [UpdateAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAsset.html) operation to update an asset. Specify the following parameters:
+ `assetId` – The ID of the asset. This is the actual ID in UUID format, or the `externalId:myExternalId` if it has one. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references) in the *AWS IoT SiteWise User Guide*.
+ `assetName` – The asset's new name.

**To update an asset's name (AWS CLI)**
+ Run the following command to update an asset's name. Replace {{asset-id}} with the ID or external ID of the asset. Update the {{asset-name}} with the new name for the asset.

  ```
  aws iotsitewise update-asset \
    --asset-id {{asset-id}} \
    --asset-name {{asset-name}}
  ```