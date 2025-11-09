End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Run statistical queries

Now that you've explored your AWS IoT SiteWise data, you can run statistical queries that
provide valuable insights to your industrial equipment. The following queries
demonstrate some of the information that you can retrieve.

###### To run statistical queries on AWS IoT SiteWise demo wind farm data

1. Run the following SQL command to find the latest values of all properties with
   numeric values for a particular asset (Demo Turbine Asset 4).

```
SELECT assetName,
    assetPropertyName,
    assetPropertyUnit,
    max_by(value, timeInSeconds) AS Latest
FROM (
    SELECT *,
        CASE assetPropertyDataType
        WHEN 'DOUBLE' THEN
        cast(doubleValue AS varchar)
        WHEN 'INTEGER' THEN
        cast(integerValue AS varchar)
        WHEN 'STRING' THEN
        stringValue
        WHEN 'BOOLEAN' THEN
        cast(booleanValue AS varchar)
        ELSE NULL
        END AS value
    FROM my_iotsitewise_datastore.asset_metadata AS asset_metadata
    JOIN my_iotsitewise_datastore.raw AS raw
        ON raw.seriesId = asset_metadata.timeSeriesId
    WHERE startYear=2021
        AND startMonth=7
        AND startDay=8
        AND assetName='Demo Turbine Asset 4'
)
GROUP BY assetName, assetPropertyName, assetPropertyUnit
```

| assetname            | assetpropertyname         | assetpropertyunit | Latest      |
| -------------------- | ------------------------- | ----------------- | ----------- |
| Demo Turbine Asset 4 | RotationsPerSecond        | RPS               | 0.48575     |
| Demo Turbine Asset 4 | Overdrive State           |                   | 1           |
| Demo Turbine Asset 4 | RotationsPerMinute        | RPM               | 29.14528    |
| Demo Turbine Asset 4 | Torque (Newton Meter)     | Nm                | 3545.35429  |
| Demo Turbine Asset 4 | Overdrive State String    |                   | overdrive   |
| Demo Turbine Asset 4 | Average Power             | Watts             | 10770.62132 |
| Demo Turbine Asset 4 | Average Wind Speed        | m/s               | 33.57922    |
| Demo Turbine Asset 4 | Torque (KiloNewton Meter) | kNm               | 3.54535     |
| Demo Turbine Asset 4 | Wind Direction            | Degrees           | 46.05476    |

2. Join both metadata tables and your raw table to identify the maximum wind
   speed properties for all assets, in addition to
   their
   parent assets.

```
SELECT child_assets_data_set.parentAssetId,
        child_assets_data_set.childAssetId,
        asset_metadata.assetPropertyId,
        asset_metadata.assetPropertyName,
        asset_metadata.timeSeriesId,
        raw_data_set.max_speed
FROM (
   SELECT sourceAssetId AS parentAssetId,
        targetAssetId AS childAssetId
    FROM my_iotsitewise_datastore.asset_hierarchy_metadata
    WHERE associationType = 'CHILD'
)
AS child_assets_data_set
JOIN mls_demo.asset_metadata AS asset_metadata
    ON asset_metadata.assetId = child_assets_data_set.childAssetId
JOIN (
    SELECT seriesId, MAX(doubleValue) AS max_speed
    FROM my_iotsitewise_datastore.raw
    GROUP BY seriesId
)
AS raw_data_set
ON raw_data_set.seriesId = asset_metadata.timeseriesid
WHERE assetPropertyName = 'Wind Speed'
ORDER BY max_speed DESC
```

| assetname                            | assetpropertyname                    | assetpropertyunit                    | Latest     | timeSeriesId                                                              | max_speed |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ---------- | ------------------------------------------------------------------------- | --------- |
| beec3903-2f94-437b-aa8f-235337810550 | fe066382-88e7-4fdd-84cf-321ff52d4c54 | cce0ccc8-e8f9-468d-88e4-139adcb0592f | Wind Speed | fe066382-88e7-4fdd-84cf-321ff52d4c54_cce0ccc8-e8f9-468d-88e4-139adcb0592f | 47.9813   |
| beec3903-2f94-437b-aa8f-235337810550 | c9e967ed-2416-49d4-af16-c231f8a7a72e | cce0ccc8-e8f9-468d-88e4-139adcb0592f | Wind Speed | c9e967ed-2416-49d4-af16-c231f8a7a72e_cce0ccc8-e8f9-468d-88e4-139adcb0592f | 47.97489  |
| beec3903-2f94-437b-aa8f-235337810550 | ee058b1a-570e-49b3-899e-0e3c9f750e59 | cce0ccc8-e8f9-468d-88e4-139adcb0592f | Wind Speed | ee058b1a-570e-49b3-899e-0e3c9f750e59_cce0ccc8-e8f9-468d-88e4-139adcb0592f | 47.97294  |
| beec3903-2f94-437b-aa8f-235337810550 | dc2cc045-1188-47cc-969f-eea93387c935 | cce0ccc8-e8f9-468d-88e4-139adcb0592f | Wind Speed | dc2cc045-1188-47cc-969f-eea93387c935_cce0ccc8-e8f9-468d-88e4-139adcb0592f | 41.46872  |

3. To find the average value of a particular property (Wind Speed) for an asset
   (Demo Turbine Asset 2), run the following SQL command. You must replace
   `my_bucket_id` with the ID of your bucket.

```
SELECT AVG(doubleValue) as "Average wind speed"
FROM my_iotsitewise_datastore.raw
WHERE seriesId =
    (SELECT timeseriesId
    FROM my_iotsitewise_datastore.asset_metadata as asset_metadata
    WHERE asset_metadata.assetname = 'Demo Turbine Asset 2'
            AND asset_metadata.assetpropertyname = 'Wind Speed')
```

| Average wind speed |
| ------------------ |
| 28.20818           |

## Next step

[Cleaning up your tutorial resources](tutorial-step4.md "tutorial-step4.md")
