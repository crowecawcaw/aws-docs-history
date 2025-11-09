End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Data exploration

After your AWS IoT SiteWise data is created and loaded into a data store, you can create an
AWS IoT Analytics dataset and run SQL queries in AWS IoT Analytics to discover insights about your assets. The
following queries demonstrate how you can explore your data before running statistical
queries.

###### To explore your data with SQL queries

1. View a sample of columns and values in each table, such as in the raw table.

```
SELECT * FROM my_iotsitewise_datastore.raw LIMIT 5
```

| seriesid                                                                  | timeinseconds | offsetinnanos | quality | doublevalue | stringvalue | integervalue | booleanvalue | jsonvalue | recordversion  | startyear | startmonth | startday |
| ------------------------------------------------------------------------- | ------------- | ------------- | ------- | ----------- | ----------- | ------------ | ------------ | --------- | -------------- | --------- | ---------- | -------- |
| 5be0e702-7cdf-4d94-9726-9211d92d9e5a_ec5b0ebe-a396-43ae-b63c-f36fcce297f2 | 1625700900.0  | 0             | GOOD    | 112         |             |              |              |           | 117592000000.0 | 2021      | 7          | 7        |
| 5be0e702-7cdf-4d94-9726-9211d92d9e5a_ec5b0ebe-a396-43ae-b63c-f36fcce297f2 | 1625701200.0  | 0             | GOOD    | 279         |             |              |              |           | 121134000000.0 | 2021      | 7          | 7        |
| 5be0e702-7cdf-4d94-9726-9211d92d9e5a_ec5b0ebe-a396-43ae-b63c-f36fcce297f2 | 1625701500.0  | 0             | GOOD    | 300         |             |              |              |           | 122508000000.0 | 2021      | 7          | 7        |
| 5be0e702-7cdf-4d94-9726-9211d92d9e5a_ec5b0ebe-a396-43ae-b63c-f36fcce297f2 | 1625701800.0  | 0             | GOOD    | 300         |             |              |              |           | 122978000000.0 | 2021      | 7          | 7        |
| 5be0e702-7cdf-4d94-9726-9211d92d9e5a_ec5b0ebe-a396-43ae-b63c-f36fcce297f2 | 1625702100.0  | 0             | GOOD    | 300         |             |              |              |           | 122696000000.0 | 2021      | 7          | 7        |

2. Use `SELECT DISTINCT` to query your `asset_metadata`
   table and list the (unique) names of your AWS IoT SiteWise assets.

```
SELECT DISTINCT assetname FROM my_iotsitewise_datastore.asset_metadata ORDER BY assetname
```

| assetname            |
| -------------------- |
| Demo Turbine Asset 1 |
| Demo Turbine Asset 2 |
| Demo Turbine Asset 3 |
| Demo Turbine Asset 4 |
| Demo Wind Farm Asset |

3. To list information about properties for a particular AWS IoT SiteWise asset, use the
   `WHERE` clause.

```
SELECT assetpropertyname,
     assetpropertyunit,
     assetpropertydatatype
FROM my_iotsitewise_datastore.asset_metadata
WHERE assetname = 'Demo Turbine Asset 2'
```

| assetpropertyname              | assetpropertyunit | assetpropertydatatype |
| ------------------------------ | ----------------- | --------------------- |
| Make                           |                   | STRING                |
| Model                          |                   | INTEGER               |
| Location                       |                   | STRING                |
| RPM Alarm Threshold            |                   | DOUBLE                |
| AVG Wind Speed Alarm Threshold |                   | DOUBLE                |
| Torque (KiloNewton Meter)      | kNm               | DOUBLE                |
| Wind Direction                 | Degrees           | DOUBLE                |
| RotationsPerMinute             | RPM               | DOUBLE                |
| Wind Speed                     | m/s               | DOUBLE                |
| Torque (Newton Meter)          | Nm                | DOUBLE                |
| RotationsPerSecond             | RPS               | DOUBLE                |
| Overdrive State                |                   | DOUBLE                |
| Overdrive State String         |                   | STRING                |
| Average Wind Speed             | m/s               | DOUBLE                |
| Overdrive State Time           | Seconds           | DOUBLE                |
| Average Power                  | Watts             | DOUBLE                |
| AWS/ALARM_TYPE                 | none              | STRING                |
| AWS/ALARM_STATE                | none              | STRUCT                |
| AWS/ALARM_SOURCE               | none              | STRING                |
| AWS/ALARM_TYPE                 | none              | STRING                |
| AWS/ALARM_STATE                | none              | STRUCT                |
| AWS/ALARM_SOURCE               | none              | STRING                |

4. With AWS IoT Analytics, you can join data from two or more tables in your data store, such
   as in the following example.

```
SELECT * FROM my_iotsitewise_datastore.raw AS raw
JOIN my_iotsitewise_datastore.asset_metadata AS asset_metadata
ON raw.seriesId = asset_metadata.timeseriesId
```

To view all relationships between your assets, use the `JOIN`
functionality in the following query.

```
SELECT DISTINCT parent.assetName as "Parent name",
    child.assetName AS "Child name"
FROM (
    SELECT sourceAssetId AS parent,
            targetAssetId AS child
    FROM my_iotsitewise_datastore.asset_hierarchy_metadata
    WHERE associationType = 'CHILD'
)
AS relations
JOIN my_iotsitewise_datastore.asset_metadata AS child
    ON relations.child = child.assetId
JOIN my_iotsitewise_datastore.asset_metadata AS parent
    ON relations.parent = parent.assetId
```

| Parent name          | Child name           |
| -------------------- | -------------------- |
| Demo Wind Farm Asset | Demo Turbine Asset 3 |
| Demo Wind Farm Asset | Demo Turbine Asset 2 |
| Demo Wind Farm Asset | Demo Turbine Asset 4 |
| Demo Wind Farm Asset | Demo Turbine Asset 1 |

## Next step

[Run statistical queries](tutorial-step3.md "tutorial-step3.md")
