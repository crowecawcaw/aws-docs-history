

# Query current asset property values in AWS IoT SiteWise
<a name="current-values"></a>

This tutorial shows two ways to get the current value of an asset property. You can use the AWS IoT SiteWise console or use API in the AWS Command Line Interface (AWS CLI).

**Topics**
+ [Query an asset property's current value (console)](#query-current-value-console)
+ [Query an asset property's current value (AWS CLI)](#query-current-value-cli)

## Query an asset property's current value (console)
<a name="query-current-value-console"></a>

You can use the AWS IoT SiteWise console to view the current value of an asset property.

**To get the current value of an asset property (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. <a name="sitewise-choose-assets"></a>In the navigation pane, choose **Assets**.

1. Choose the asset with the property to query.

1. Choose the arrow icon to expand an asset hierarchy to find your asset.

1. Choose the tab for the type of property. For example, choose **Measurements** to view the current value of a measurement property.

1. Find the property to view. The current value appears in the **Latest value** column.

## Query an asset property's current value (AWS CLI)
<a name="query-current-value-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to query the current value of an asset property.

Use the [GetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html) operation to query an asset property's current value.

To identify an asset property, specify one of the following:
+ The `assetId` and `propertyId` of the asset property that data is sent to.
+ The `propertyAlias`, which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature`). To use this option, you must first set your asset property's alias. To set property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md).

**To get the current value of an asset property (AWS CLI)**
+ Run the following command to get the current value of the asset property. Replace {{asset-id}} with the ID of the asset and {{property-id}} with the ID of the property.

  ```
  aws iotsitewise get-asset-property-value \
    --asset-id {{asset-id}} \
    --property-id {{property-id}}
  ```

  The operation returns a response that contains the current TQV of the property in the following format.

  ```
  {
    "propertyValue": {
      "value": {
        "booleanValue": {{Boolean}},
        "doubleValue": {{Number}},
        "integerValue": {{Number}},
        "stringValue": "{{String}}",
        "nullValue": {
            "valueType": "{{String}}"
        }
      },
      "timestamp": {
        "timeInSeconds": {{Number}},
        "offsetInNanos": {{Number}}
      },
      "quality": "{{String}}"
    }
  }
  ```