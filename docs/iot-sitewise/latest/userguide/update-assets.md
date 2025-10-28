# Update assets in AWS IoT SiteWise

You can use the AWS IoT SiteWise console or API to update an asset's name.

When you update an asset, the asset's status is `UPDATING` until the changes
propagate. For more information, see [Asset and model states](asset-and-model-states.md "asset-and-model-states.md").

###### Topics

- [Update an asset (console)](#update-asset-console "#update-asset-console")
- [Update an asset (AWS CLI)](#update-asset-cli "#update-asset-cli")

## Update an asset (console)

You can use the AWS IoT SiteWise console to update asset details.

###### To update an asset (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset to update.

###### Tip

You can choose the arrow icon to expand an asset hierarchy to find your
asset. 4. Choose **Edit**. 5. Update the asset's **Name**. 6. (Optional) On this page, update other information for the asset. For more
information, see the following:

    * [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md")
    * [Update attribute values](update-attribute-values.md "update-attribute-values.md")
    * [Interact with other AWS services](interact-with-other-services.md "interact-with-other-services.md")

7. Choose **Save**.

## Update an asset (AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to update an asset's name.

Use the [UpdateAsset](../APIReference/API_UpdateAsset.md "../APIReference/API_UpdateAsset.md") operation to update an asset. Specify the following
parameters:

- `assetId` – The ID of the asset. This is the actual ID in UUID format, or the `externalId:myExternalId` if it has one.
  For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.
- `assetName` – The asset's new name.

###### To update an asset's name (AWS CLI)

- Run the following command to update an asset's name. Replace
  `asset-id` with the ID or external ID of the asset. Update the
  `asset-name` with the new name for the asset.

```
aws iotsitewise update-asset \
  --asset-id `asset-id` \
  --asset-name `asset-name`
```
