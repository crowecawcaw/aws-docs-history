

# Create assets for asset models in AWS IoT SiteWise
<a name="create-assets"></a>

You can create an asset from an asset model. You must have an asset model before you can create an asset. If you haven't created an asset model, see [Create asset models in AWS IoT SiteWise](create-asset-models.md). 

**Note**  
You can only create assets from `ACTIVE` models. If your model's state isn't `ACTIVE`, you may need to wait for up to a few minutes before you can create assets from that model. For more information, see [Asset and model states](asset-and-model-states.md).

**Topics**
+ [Create an asset (console)](#create-asset-console)
+ [Create an asset (AWS CLI)](#create-asset-cli)
+ [Configure a new asset](create-asset-next-steps.md)

## Create an asset (console)
<a name="create-asset-console"></a>

You can use the AWS IoT SiteWise console to create an asset.

**To create an asset (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. <a name="sitewise-choose-assets"></a>In the navigation pane, choose **Assets**.

1. Choose **Create asset**.

1. On the **Create asset** page, do the following:

   1. For **Model**, choose the asset model from which to create an asset.
**Note**  
If your model isn't **ACTIVE**, you must wait until it's active, or resolve issues if it's **FAILED**.

   1. Enter a **Name** for your asset.

   1. (Optional) Add tags for your asset. For more information, see [Tag your AWS IoT SiteWise resources](tag-resources.md).

   1. Choose **Create asset**.

   When you create an asset, the AWS IoT SiteWise console navigates to the new asset's page. On this page, you can see the asset's **Status**, which is initially **CREATING**. This page automatically updates, so you can wait for the asset's status to update.
**Note**  
The asset creation process can take up to a minute. After the **Status** is **ACTIVE**, you can perform update operations on your asset. For more information, see [Asset and model states](asset-and-model-states.md).

After you create an asset, see [Configure a new asset](create-asset-next-steps.md).

## Create an asset (AWS CLI)
<a name="create-asset-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to create an asset from an asset model.

You must have an `assetModelId` to create an asset. If you created an asset model, but don't know its `assetModelId`, use the [ListAssetModels](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html) API to view all of your asset models.

To create an asset from an asset model, use the [CreateAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAsset.html) API with the following parameters:
+ `assetName` – The new asset's name. Give your asset a name to help you identify it.
+ `assetModelId` – The ID of the asset. This is the actual ID in UUID format, or the `externalId:myExternalId` if it has one. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references) in the *AWS IoT SiteWise User Guide*.

**To create an asset (AWS CLI)**
+ Run the following command to create an asset. Replace {{asset-name}} with a name for the asset and {{asset-model-id}} with the ID or the external ID of the asset model. 

  ```
  aws iotsitewise create-asset \
    --asset-name {{asset-name}} \
    --asset-model-id {{asset-model-id}}
  ```

  The operation returns a response that contains your new asset's details and status in the following format.

  ```
  {
    "assetId": "{{String}}",
    "assetArn": "{{String}}",
    "assetStatus": {
      "state": "{{String}}",
      "error": {
        "code": "{{String}}",
        "message": "{{String}}"
      }
    }
  }
  ```

  The asset's `state` is `CREATING` until the asset creates.
**Note**  
The asset creation process can take up to a minute. To check your asset's status, use the [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html) operation with your asset's ID as the `assetId` parameter. After the asset's `state` is `ACTIVE`, you can perform update operations on your asset. For more information, see [Asset and model states](asset-and-model-states.md).

After you create an asset, see [Configure a new asset](create-asset-next-steps.md).