

# Check the status of an asset
<a name="check-asset-status"></a>

You can use the AWS IoT SiteWise console or API to check the status of an asset.

**Topics**
+ [Check the status of an asset (console)](#check-asset-status-console)
+ [Check the status of an asset (AWS CLI)](#check-asset-status-cli)

## Check the status of an asset (console)
<a name="check-asset-status-console"></a>

Use the following procedure to check the status of an asset in the AWS IoT SiteWise console.

**To check the status of an asset (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. <a name="sitewise-choose-assets"></a>In the navigation pane, choose **Assets**.

1. Choose the asset to check.
**Tip**  <a name="sitewise-expand-asset-hierarchy"></a>
You can choose the arrow icon to expand an asset hierarchy to find your asset.

1. Find **Status** in the **Asset details** panel.  
![AWS IoT SiteWise Asset details panel with Status as Active.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sitewise-view-asset-status-console.png)

## Check the status of an asset (AWS CLI)
<a name="check-asset-status-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to check the status of an asset.

To check the status of an asset, use the [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html) operation with the `assetId` parameter.

**To check the status of an asset (AWS CLI)**
+ Run the following command to describe the asset. Replace {{asset-id}} with the asset's ID or external ID. The external ID is a user-defined ID. For more information, see [Reference objects with external IDs](object-ids.md#external-id-references) in the *AWS IoT SiteWise User Guide*.

  ```
  aws iotsitewise describe-asset --asset-id {{asset-id}}
  ```

  The operation returns a response that contains the asset's details. The response contains an `assetStatus` object that has the following structure:

  ```
  {
      {{...}}
      "assetStatus": {
        "state": "{{String}}",
        "error": {
           "code": "{{String}}",
           "message": "{{String}}"
        }
      }
    }
  ```

  The asset's state is in `assetStatus.state` in the JSON object.