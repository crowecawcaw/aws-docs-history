# Query asset property aggregates in AWS IoT SiteWise

AWS IoT SiteWise automatically computes aggregated asset property values, which are a set of basic
metrics calculated over multiple time intervals. AWS IoT SiteWise computes the following aggregates
every minute, hour, and day for your asset properties:

- **average** – The average (mean) of a property's
  values over a time interval.
- **count** – The number of data points for a property over
  a time interval.
- **maximum** – The maximum of a property's values
  over a time interval.
- **minimum** – The minimum of a property's values
  over a time interval.
- **standard deviation** – The standard deviation of
  a property's values over a time interval.
- **sum** – The sum of a property's values over a
  time interval.
  For non-numeric properties, such as strings and Booleans, AWS IoT SiteWise computes only the count
  aggregate.

You can also compute custom metrics for your asset data. With metric properties, you
define aggregations that are specific to your operation. Metric properties offer additional
aggregation functions and time intervals that aren't precomputed for the AWS IoT SiteWise API. For more
information, see [Aggregate data from properties and other assets (metrics)](metrics.md "metrics.md").

###### Topics

- [Aggregates for an asset property (API)](#aggregates-api "#aggregates-api")
- [Aggregates for an asset property (AWS CLI)](#aggregates-cli "#aggregates-cli")

## Aggregates for an asset property (API)

Use the AWS IoT SiteWise API to get aggregates for an asset property.

Use the [GetAssetPropertyAggregates](../APIReference/API_GetAssetPropertyAggregates.md "../APIReference/API_GetAssetPropertyAggregates.md") operation to query aggregates of an asset
property.

To identify an asset property, specify one of the following:

- The `assetId` and `propertyId` of the asset property that data is sent to.
- The `propertyAlias`, which is a data stream alias (for example,
  `/company/windfarm/3/turbine/7/temperature`). To use this option, you must first set your asset property's alias.
  To set property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").

You must pass the following required parameters:

- `aggregateTypes` – The list of aggregates to retrieve. You can
  specify any of `AVERAGE`, `COUNT`, `MAXIMUM`,
  `MINIMUM`, `STANDARD_DEVIATION`, and `SUM`.
- `resolution` – The time interval for which to retrieve the metric:
  `1m` (1 minute), `15m` (15 minutes), `1h` (1 hour), or `1d` (1 day).
- `startDate` – The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
- `endDate` – The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.

You can also pass any of the following parameters to refine your results:

- `maxResults` – The maximum number of results to return in one request. Defaults to `20` results.
- `nextToken` – A pagination token returned from a previous call of this operation.
- `timeOrdering` – The ordering to apply to the returned values:
  `ASCENDING` or `DESCENDING`.
- `qualities` – The quality to filter results by: `GOOD`,
  `BAD`, or `UNCERTAIN`.

###### Note

The [GetAssetPropertyAggregates](../APIReference/API_GetAssetPropertyAggregates.md "../APIReference/API_GetAssetPropertyAggregates.md") operation returns a TQV with a different format than other operations
described in this section. The `value` structure contains a field for each of the
`aggregateTypes` in the request. The `timestamp` contains the time that the aggregation
occurred, in seconds in Unix epoch time.

## Aggregates for an asset property (AWS CLI)

###### To query aggregates for an asset property (AWS CLI)

1. Run the following command to get aggregates for the asset property. This command queries the average and
   sum with a 1 hour resolution for a specific 1 hour interval. Replace `asset-id` with
   the ID of the asset and `property-id` with the ID of the property. Replace the
   parameters with the aggregates and interval to query.

```
aws iotsitewise get-asset-property-aggregates \
  --asset-id `asset-id` \
  --property-id `property-id` \
  --start-date `1575216000` \
  --end-date `1575219600` \
  --aggregate-types `AVERAGE SUM` \
  --resolution `1h`
```

The operation returns a response that contains the historical TQVs of the property in the following
format. The response includes only the requested aggregates.

```
{
  "aggregatedValues": [
    {
      "timestamp": `Number`,
      "quality": "`String`",
      "value": {
        "average": `Number`,
        "count": `Number`,
        "maximum": `Number`,
        "minimum": `Number`,
        "standardDeviation": `Number`,
        "sum": `Number`
      }
    }
  ],
  "nextToken": "`String`"
}
```

2. If more value entries exist, you can pass the pagination token from the `nextToken` field to a subsequent call to the [GetAssetPropertyAggregates](../APIReference/API_GetAssetPropertyAggregates.md "../APIReference/API_GetAssetPropertyAggregates.md") operation.

###### Note

If your query range contains a `null` value TQVs, see [AssetPropertyValue](../APIReference/API_AssetPropertyValue.md "../APIReference/API_AssetPropertyValue.md") API.
All statistics except count, results in a `null` response, similar to statistics for String TQVs.
If your query range contains `Double.NaN` for double type TQVs, all calculations except count will result in a `Double.NaN`.
