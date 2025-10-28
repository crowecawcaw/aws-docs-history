# Query historical asset property values in AWS IoT SiteWise

You can use the AWS IoT SiteWise API [GetAssetPropertyValueHistory](../APIReference/API_GetAssetPropertyValueHistory.md "../APIReference/API_GetAssetPropertyValueHistory.md") operation to query the historical values of an asset
property.

To identify an asset property, specify one of the following:

- The `assetId` and `propertyId` of the asset property that data is sent to.
- The `propertyAlias`, which is a data stream alias (for example,
  `/company/windfarm/3/turbine/7/temperature`). To use this option, you must first set your asset property's alias.
  To set property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").
  Pass the following parameters to refine your results:

- `startDate` – The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
- `endDate` – The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
- `maxResults` – The maximum number of results to return in one request. Defaults to `20` results.
- `nextToken` – A pagination token returned from a previous call of this operation.
- `timeOrdering` – The ordering to apply to the returned values:
  `ASCENDING` or `DESCENDING`.
- `qualities` – The quality to filter results by: `GOOD`,
  `BAD`, or `UNCERTAIN`.

###### To query the value history for an asset property (AWS CLI)

1. Run the following command to get the value history for the asset property. This command queries the
   property's history over a specific 10 minute interval. Replace `asset-id` with the ID
   of the asset and `property-id` with the ID of the property. Replace the date
   parameters with the interval to query.

```
aws iotsitewise get-asset-property-value-history \
  --asset-id `asset-id` \
  --property-id `property-id` \
  --start-date `1575216000` \
  --end-date `1575216600`
```

The operation returns a response that contains the historical TQVs of the property in the following
format:

```
{
  "assetPropertyValueHistory": [
    {
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
  ],
  "nextToken": "`String`"
}
```

2. If more value entries exist, you can pass the pagination token from the `nextToken` field to a subsequent call to the [GetAssetPropertyValueHistory](../APIReference/API_GetAssetPropertyValueHistory.md "../APIReference/API_GetAssetPropertyValueHistory.md") operation.
