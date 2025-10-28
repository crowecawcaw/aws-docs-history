# Asset model versions

AWS IoT SiteWise supports asynchronous processing of create and update operations on asset models and component models. It also
updates the status of the model.

AWS IoT SiteWise propagates a valid model's changes in the create and update requests to its dependent resources (from asset model to assets,
or from component model to asset models). It then places the model in `ACTIVE` state.

If the provided model definition is invalid, AWS IoT SiteWise places the model in a `FAILED` state. The changes are not propagated
to the dependent resources. The dependent resources refer to the last model definition propagated when the model was in an `ACTIVE` state.

Based on the information above, model definitions have two types of model versions:

1. **Latest version –** The latest definition accepted as part of a create or update request.
2. **Active version –** The latest definition successfully processed, and the model state is `ACTIVE`.

By default, details of the model's latest version is returned when describe APIs are called on an asset model or component model.
There are scenarios where the active version of the asset model or component model is needed. See example scenarios below:

- An update operation with an invalid definition places your asset model in a `FAILED` state. You must
  revert your changes by retrieving the active version of the asset model, and creating another update request
  referring to this valid definition.
- An application on AWS IoT SiteWise exists where customers can view assets and their corresponding asset models.
  When a user refers the asset model definition corresponding to a particular asset, and the asset model
  is in a transitory `UPDATING`, `PROPAGATING`, or `FAILED` state,
  the latest version returns the asset model definition that is not yet propagated to its assets.
  In this case, you must retrieve the active version of the asset model to customers.

###### Topics

- [Retrieve the active version of an asset model or component model (console)](#active-console "#active-console")
- [Retrieve the active version of an asset model or component model (AWS CLI)](#active-cli "#active-cli")

## Retrieve the active version of an asset model or component model (console)

Follow this procedure to retrieve the active version of an asset model or component model in the AWS IoT SiteWise console.

###### Tip

Asset models and component models are both listed under **Models**
in the navigation pane. The **Details** panel of the selected asset
model or component model indicates which type it is.

###### To retrieve the active version of an asset model or component model (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose the model to retrieve its active version.
   1. If the model is in an `ACTIVE` state, you are viewing its active version.
   2. If the model is in a transitory `UPDATING`, `PROPAGATING`, or `FAILED` state,
      find the **See active version** under **Status** in the
      **Details** panel.

## Retrieve the active version of an asset model or component model (AWS CLI)

Use the AWS CLI to retrieve the active version of an asset model or component model.

To retrieve the active version of an asset model or component model, use the [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md") operation with the `assetModelVersion`
parameter.

###### Tip

The AWS CLI defines component models as a type of asset model. Therefore, you use the
same [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md") operation for both types of model. The
`assetModelType` field in the response indicates whether it's an
`ASSET_MODEL` or a `COMPONENT_MODEL`.

###### To retrieve the active version of an asset model or component model (AWS CLI)

- Run the following command to describe the model. Replace
  `asset-model-id` with the ID or the external ID of the asset model or component model.
  The external ID is a user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references "object-ids.md#external-id-references") in the _AWS IoT SiteWise User Guide_.

```
aws iotsitewise describe-asset-model --asset-model-id `asset-model-id` --asset-model-version ACTIVE
```

The operation returns a response with the model's details. The response
contains an `assetModelStatus` object with the following
structure.

```
{
    `...`
    "assetModelName": "`string`",
    "assetModelProperties": [ ... ],
    ...,
    "assetModelVersion": "`string`"
}
```
