# Update asset models, component models, and interfaces

Use the AWS IoT SiteWise console or API to update an asset model, component model, or interface.

You can't change the type or data type of an existing property, or the window of an
existing metric. You also can't change the type of the model from asset model to component
model or interface, or the other way around.

###### Important

- If you remove a property from an asset model or component model, AWS IoT SiteWise deletes
  all previous data for that property. For component models, this affects **all asset models using that component model**, so be especially
  careful to understand how widely your change may apply.
- If you remove a hierarchy definition from an asset model, AWS IoT SiteWise disassociates all
  assets in that hierarchy.
  When you update an asset model, every asset based on that model reflects any changes
  that you make to the underlying model. Until the changes propagate, each asset has the
  `UPDATING` state. You must wait until those assets return to the
  `ACTIVE` state before you interact with them. During this time, the updated
  asset model's status will be `PROPAGATING`.

When you update a component model, every asset model that incorporates that component
model reflects the changes. Until the component model changes propagate, each affected asset
model has the `UPDATING` state, followed by `PROPAGATING` as it
updates its associated assets, as described in the preceding paragraph.
You must wait until those asset models return to the `ACTIVE`
state before you interact with them. During this time, the updated component model's status
will be `PROPAGATING`.

For more information, see [Asset and model states](asset-and-model-states.md "asset-and-model-states.md").

###### Topics

- [Updating an asset model, component model, or interface (console)](#update-asset-model-console "#update-asset-model-console")
- [Update an asset model, component model, or interface
  (AWS CLI)](#update-asset-model-cli "#update-asset-model-cli")

## Updating an asset model, component model, or interface (console)

You can use the AWS IoT SiteWise console to update an asset model, component model, or interface.

###### To update an asset model, component model, or interface (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose the asset model, component model, or interface to update.
4. Choose **Edit**.
5. On the **Edit model** page, do any of the following:
   - In **Model details**, change the **Name** of
     the model.
   - Change any of the **Attribute definitions**. You can't change
     the **Data type** of existing attributes. For more information,
     see [Define static data (attributes)](attributes.md "attributes.md").
   - Change any of the **Measurement definitions**. You can't
     change the **Data type** of existing measurements. For more
     information, see [Define data streams from equipment (measurements)](measurements.md "measurements.md").
   - Change any of the **Transform definitions**. For more
     information, see [Transform data (transforms)](transforms.md "transforms.md").
   - Change any of the **Metric definitions**. You can't change
     the **Time interval** of existing metrics. For more information,
     see [Aggregate data from properties and other assets (metrics)](metrics.md "metrics.md").
   - (Asset models only) Change any of the **Hierarchy
     definitions**. You can't change the **Hierarchy
     model** of existing hierarchies. For more information, see [Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md").

6. Choose **Save**.

###### Note

Update requests made in the console are rejected, if another user successfully updates the
asset model since you last opened the **Edit model** page. The console
prompts the user to **Refresh** the **Edit model** page, to
fetch the updated model. You must make your updates again, and retry your save.
See [Optimistic locking for asset model writes](opt-locking-for-model.md "opt-locking-for-model.md") for more details.

## Update an asset model, component model, or interface

(AWS CLI)

Use the AWS Command Line Interface (AWS CLI) to update an asset model, component model, or interface.

Use the [UpdateAssetModel](../APIReference/API_UpdateAssetModel.md "../APIReference/API_UpdateAssetModel.md") API to update the name, description, and properties of an
asset model, component model, or interface. For asset models only, you can update hierarchies. For interfaces, you can update properties and hierarchies. Specify
the following parameters:

- `assetModelId` – The ID of the asset. This is the actual ID in UUID format, or the `externalId:myExternalId` if it has one.
  For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.

Specify the updated model in the payload. To learn about the expected format of an
asset model or component model, see [Create asset models in AWS IoT SiteWise](create-asset-models.md "create-asset-models.md").

###### Warning

The [UpdateAssetModel](../APIReference/API_UpdateAssetModel.md "../APIReference/API_UpdateAssetModel.md")
API overwrites the existing model with the model that you
provide in the payload. To avoid deleting your model's properties or hierarchies, you
must include their IDs and definitions in the updated model payload. To learn how to
query your model's existing structure, see the [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md") operation.

###### Note

The following procedure can only update composite models of type
`AWS/ALARM`. If you want to update `CUSTOM` composite models,
use [UpdateAssetModelCompositeModel](../APIReference/API_UpdateAssetModelCompositeModel.md "../APIReference/API_UpdateAssetModelCompositeModel.md") instead. For more information, see [Update custom composite models
(components)](update-custom-composite-models.md "update-custom-composite-models.md").

###### To update an asset model or component model (AWS CLI)

1. Run the following command to retrieve the existing model definition. Replace
   `asset-model-id` with the ID or the external ID of the asset
   model or component model to update.

```
aws iotsitewise describe-asset-model --asset-model-id `asset-model-id`
```

The above command returns the model definition corresponding to model’s latest version.

For an use case where an asset model is in a `FAILED` state, retrieve
the valid model definition corresponding to its active version to build your update request. See
[Asset model versions](model-active-version.md "model-active-version.md") for details.
Run the following command to retrieve the active model definition:

```
aws iotsitewise describe-asset-model --asset-model-id `asset-model-id` --asset-model-version ACTIVE
```

The operation returns a response that contains the model's details. The response has the following structure.

```
{
    "assetModelId": "`String`",
    "assetModelArn": "`String`",
    "assetModelName": "`String`",
    "assetModelDescription": "`String`",
    "assetModelProperties": `Array of AssetModelProperty`,
    "assetModelHierarchies": `Array of AssetModelHierarchyDefinition`,
    "assetModelCompositeModels": `Array of AssetModelCompositeModel`,
    "assetModelCompositeModelSummaries": `Array of AssetModelCompositeModelSummary`,
    "assetModelCreationDate": "`String`",
    "assetModelLastUpdateDate": "`String`",
    "assetModelStatus": {
      "state": "`String`",
      "error": {
        "code": "`String`",
        "message": "`String`"
      },
    "assetModelType": "`String`"
    },
    "assetModelVersion": "`String`",
    "eTag": "`String`"
}
```

For more information, see the [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md")
operation. 2. Create a file called `update-asset-model.json` and copy the
previous command's response into the file. 3. Remove the following key-value pairs from the JSON object in
`update-asset-model.json`:

    * `assetModelId`
    * `assetModelArn`
    * `assetModelCompositeModelSummaries`
    * `assetModelCreationDate`
    * `assetModelLastUpdateDate`
    * `assetModelStatus`
    * `assetModelType`
    * `assetModelVersion`
    * `eTag`

The [UpdateAssetModel](../APIReference/API_UpdateAssetModel.md "../APIReference/API_UpdateAssetModel.md") operation expects a payload with the following
structure:

```
{
  "assetModelName": "`String`",
  "assetModelDescription": "`String`",
  "assetModelProperties": `Array of AssetModelProperty`,
  "assetModelHierarchies": `Array of AssetModelHierarchyDefinition`,
  "assetModelCompositeModels": `Array of AssetModelCompositeModel`
}
```

4. In `update-asset-model.json`, do any of the following:
   - Change the asset model's name (`assetModelName`).
   - Change, add, or remove the asset model's description
     (`assetModelDescription`).
   - Change, add, or remove any of the asset model's properties
     (`assetModelProperties`). You can't change the `dataType`
     of existing properties or the `window` of existing metrics. For more
     information, see [Define data properties](asset-properties.md "asset-properties.md").
   - Change, add, or remove any of the asset model's hierarchies
     (`assetModelHierarchies`). You can't change the
     `childAssetModelId` of existing hierarchies. For more information,
     see [Define asset model hierarchies](define-asset-hierarchies.md "define-asset-hierarchies.md").
   - Change, add, or remove any of the asset model's composite models of type
     `AWS/ALARM` (`assetModelCompositeModels`). Alarms monitor
     other properties so that you can identify when equipment or processes require
     attention. Each alarm definition is a composite model that standardizes the set of
     properties that the alarm uses. For more information, see [Monitor data with alarms in AWS IoT SiteWise](industrial-alarms.md "industrial-alarms.md")

   and [Define alarms on asset models in AWS IoT SiteWise](define-alarms.md "define-alarms.md").

5. Run the following command to update the asset model with the definition stored in
   `update-asset-model.json`. Replace
   `asset-model-id` with the ID of the asset model:

```
aws iotsitewise update-asset-model \
  --asset-model-id `asset-model-id` \
  --cli-input-json file://model-payload.json
```

###### Important

When multiple users update an asset model at the same time, an user's changes may be
inadvertently overwritten by another user. To prevent this, you must define a conditional update request. See
[Optimistic locking for asset model writes](opt-locking-for-model.md "opt-locking-for-model.md").
