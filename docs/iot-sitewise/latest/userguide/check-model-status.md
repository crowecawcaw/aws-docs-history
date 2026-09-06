

# Check the status of an asset or component model
<a name="check-model-status"></a>

You can use the AWS IoT SiteWise console or API to check the status of an asset model or component model.

**Topics**
+ [Check the status of an asset model or component model (console)](#check-model-status-console)
+ [Check the status of an asset model or component model (AWS CLI)](#check-model-status-cli)

## Check the status of an asset model or component model (console)
<a name="check-model-status-console"></a>

Use the following procedure to check the status of an asset model or component model in the AWS IoT SiteWise console.

**Tip**  
Asset models and component models are both listed under **Models** in the navigation pane. The **Details** panel of the selected asset model or component model indicates which type it is.

**To check the status of an asset model or component model (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. <a name="sitewise-choose-models"></a>In the navigation pane, choose **Models**.

1. Choose the model to check.

1. Find **Status** in the **Details** panel.  
![AWS IoT SiteWise "Asset model" page screenshot with asset model status highlighted.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sitewise-view-model-status-console.png)

## Check the status of an asset model or component model (AWS CLI)
<a name="check-model-status-cli"></a>

You can use the AWS CLI to check the status of an asset model or component model.

To check the status of an asset model or component model, use the [DescribeAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html) operation with the `assetModelId` parameter.

**Tip**  
The AWS CLI defines component models as a type of asset model. Therefore, you use the same [DescribeAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html) operation for both types of model. The `assetModelType` field in the response indicates whether it's an `ASSET_MODEL` or a `COMPONENT_MODEL`. 

**To check the status of an asset model or component model (AWS CLI)**
+ Run the following command to describe the model. Replace {{asset-model-id}} with the ID or the external ID of the asset model or component model. The external ID is a user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references) in the *AWS IoT SiteWise User Guide*.

  ```
  aws iotsitewise describe-asset-model --asset-model-id {{asset-model-id}}
  ```

  The operation returns a response that contains the model's details. The response contains an `assetModelStatus` object that has the following structure.

  ```
  {
      {{...}}
      "assetModelStatus": {
        "state": "{{String}}",
        "error": {
           "code": "{{String}}",
           "message": "{{String}}"
        }
      }
    }
  ```

  The model's state is in `assetModelStatus.state` in the JSON object.