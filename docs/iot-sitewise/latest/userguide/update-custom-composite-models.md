# Update custom composite models

(components)

You can use the AWS IoT SiteWise API to update a custom composite model, or the AWS IoT SiteWise console to update components.

###### Topics

- [Update a component
  (console)](#update-custom-composite-model-console "#update-custom-composite-model-console")
- [Update a custom composite model
  (AWS CLI)](#update-custom-composite-model-cli "#update-custom-composite-model-cli")

## Update a component

(console)

You can use the AWS IoT SiteWise console to update a component.

###### To update a component (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose the asset model where the component is.
4. On the **Properties** tab, choose **Components**.
5. Choose the component that you want to update.
6. Choose **Edit**.
7. On the **Edit component** page, do any of the following:
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

8. Choose **Save**.

## Update a custom composite model

(AWS CLI)

Use the AWS Command Line Interface (AWS CLI) to update a custom composite model.

To update the name or description, use the [UpdateAssetModelCompositeModel](../APIReference/API_UpdateAssetModelCompositeModel.md "../APIReference/API_UpdateAssetModelCompositeModel.md") operation. For
inline custom composite models only, you can also update the properties. You can't update the properties of a
component-model-based custom composite model, because its referenced component model provides its associated
properties.

###### Important

If you remove a property from a custom composite model, AWS IoT SiteWise deletes all previous data for
that property. You can’t change the type or data type of an existing property.

To replace an existing composite model property with a new one with the same `name`, do the following:

1. Submit an `UpdateAssetModelCompositeModel` request with the entire existing property removed.
2. Submit a second `UpdateAssetModelCompositeModel` request that includes the new property. The new asset property will have the same
   `name` as the previous one and AWS IoT SiteWise will generate a new unique `id`.

###### To update a custom composite model (AWS CLI)

1.  To retrieve the existing composite model definition, run the following command. Replace
    `composite-model-id` with the ID or the external ID of the custom composite model to update, and
    `asset-model-id` with the asset model that the custom composite model is
    associated with. For more information, see the _AWS IoT SiteWise User Guide_.
    1. Run the command below:

    ```
    aws iotsitewise describe-asset-model-composite-model \
    --asset-model-composite-model-id `composite-model-id` \
    --asset-model-id `asset-model-id`
    ```

    2. The above command returns the composite model definition corresponding to associated model’s latest version.
       For an use case where an asset model is in a `FAILED` state, retrieve
       the valid model definition corresponding to its active version to build your update request. See
       [Asset model versions](model-active-version.md "model-active-version.md") for details.
    3. Run the following command to retrieve the active model definition:

    ```
    aws iotsitewise describe-asset-model-composite-model \
    --asset-model-composite-model-id `composite-model-id` \
    --asset-model-id `asset-model-id` \
    --asset-model-version ACTIVE
    ```

    4. For more information, see the [DescribeAssetModelCompositeModel](../APIReference/API_DescribeAssetModelCompositeModel.md "../APIReference/API_DescribeAssetModelCompositeModel.md") operation.

2.  Create a file called `update-custom-composite-model.json`, and then copy the
    previous command's response into the file.
3.  Remove every key-value pair from the JSON object in `update-custom-composite-model.json`
    except for the following fields:
    - `assetModelCompositeModelName`
    - `assetModelCompositeModelDescription` (if present)
    - `assetModelCompositeModelProperties` (if present)

4.  In `update-custom-composite-model.json`, do any of the following:

        * Change the value of `assetModelCompositeModelName`.
        * Add or remove `assetModelCompositeModelDescription`, or change its value.
        * For inline custom composite models only: Change, add, or remove any of the asset model's
         properties in `assetModelCompositeModelProperties`.

    For more information about the required format for this file, see the request syntax for [UpdateAssetModelCompositeModel](../APIReference/API_UpdateAssetModelCompositeModel.md "../APIReference/API_UpdateAssetModelCompositeModel.md").

5.  Run the following command to update the custom composite model with the definition stored in
    `update-custom-composite-model.json`. Replace `composite-model-id`
    with the ID of the composite model, and `asset-model-id` with the ID of the asset model it's in.

```
aws iotsitewise update-asset-model-composite-model \
--asset-model-composite-model-id `composite-model-id` \
--asset-model-id `asset-model-id` \
--cli-input-json file://update-custom-composite-model.json
```

###### Important

When multiple users update an asset model at the same time, an user's changes may be
inadvertently overwritten by another user. To prevent this, you must define a conditional update request. See
[Optimistic locking for asset model writes](opt-locking-for-model.md "opt-locking-for-model.md").
