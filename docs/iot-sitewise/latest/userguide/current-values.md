# Query current asset property values in AWS IoT SiteWise

This tutorial shows two ways to get the current value of an asset property. You can use
the AWS IoT SiteWise console or use API in the AWS Command Line Interface (AWS CLI).

###### Topics

- [Query an asset property's current value (console)](#query-current-value-console "#query-current-value-console")
- [Query an asset property's current value (AWS CLI)](#query-current-value-cli "#query-current-value-cli")

## Query an asset property's current value (console)

You can use the AWS IoT SiteWise console to view the current value of an asset property.

###### To get the current value of an asset property (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset with the property to query.
4. Choose the arrow icon to expand an asset hierarchy to find your asset.
5. Choose the tab for the type of property. For example, choose
   **Measurements** to view the current value of a measurement
   property.
6. Find the property to view. The current value appears in the **Latest
   value** column.

## Query an asset property's current value (AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to query the current value of an asset
property.

Use the [GetAssetPropertyValue](../APIReference/API_GetAssetPropertyValue.md "../APIReference/API_GetAssetPropertyValue.md") operation to query an asset property's current
value.

To identify an asset property, specify one of the following:

- The `assetId` and `propertyId` of the asset property that data is sent to.
- The `propertyAlias`, which is a data stream alias (for example,
  `/company/windfarm/3/turbine/7/temperature`). To use this option, you must first set your asset property's alias.
  To set property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").

###### To get the current value of an asset property (AWS CLI)

- Run the following command to get the current value of the asset property. Replace
  `asset-id` with the ID of the asset and
  `property-id` with the ID of the property.

```
aws iotsitewise get-asset-property-value \
  --asset-id `asset-id` \
  --property-id `property-id`
```

The operation returns a response that contains the current TQV of the property in the
following format.

```
{
  "propertyValue": {
    "value": {
      "booleanValue": `Boolean`,
      "doubleValue": `Number`,
      "integerValue": `Number`,
      "stringValue": "`String`",
      "nullValue": {
          "valueType": "`String`"
      }
    },
    "timestamp": {
      "timeInSeconds": `Number`,
      "offsetInNanos": `Number`
    },
    "quality": "`String`"
  }
}
```
