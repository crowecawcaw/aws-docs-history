# CreateBulkImportJob API

Use the `CreateBulkImportJob` API to import large amounts of data from Amazon S3. Your
data must be saved in the CSV format in Amazon S3. Data files can have the following columns.

###### Note

Data older than 1 January 1970 00:00:00 UTC is not supported.

To identify an asset property, specify one of the following.

- The `ASSET_ID` and `PROPERTY_ID` of the asset property that you
  you're sending data to.
- The `ALIAS`, which is a data stream alias (for example,
  `/company/windfarm/3/turbine/7/temperature`). To use this option, you must
  first set your asset property's alias. To learn how to set property aliases, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").

- `ALIAS` – The alias that identifies the property, such as an OPC UA
  server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").
- `ASSET_ID` – The ID of the asset.
- `PROPERTY_ID` – The ID of the asset property.
- `DATA_TYPE` – The property's data type can be one of the
  following.
  - `STRING` – A string with up to 1024 bytes.
  - `INTEGER` – A signed 32-bit integer with range [-2,147,483,648,
    2,147,483,647].
  - `DOUBLE` – A floating point number with range [-10^100, 10^100]
    and IEEE 754 double precision.
  - `BOOLEAN` – `true` or `false`.

- `TIMESTAMP_SECONDS` – The timestamp of the data point, in Unix epoch
  time.
- `TIMESTAMP_NANO_OFFSET` – The nanosecond offset coverted from
  `TIMESTAMP_SECONDS`.
- `QUALITY` – (Optional) The quality of the asset property value. The
  value can be one of the following.

      + `GOOD` – (Default) The data isn't affected by any
       issues.
      + `BAD` – The data is affected by an issue such as sensor
       failure.
      + `UNCERTAIN` – The data is affected by an issue such as sensor
       inaccuracy.

  For more information about how AWS IoT SiteWise handles data quality in computations, see [Data quality in formula expressions](expression-tutorials.md#data-quality "expression-tutorials.md#data-quality").

- `VALUE` – The value of the asset property.

###### Example data file(s) in the .csv format

```
asset_id,property_id,DOUBLE,1635201373,0,GOOD,1.0
asset_id,property_id,DOUBLE,1635201374,0,GOOD,2.0
asset_id,property_id,DOUBLE,1635201375,0,GOOD,3.0
```

```
unmodeled_alias1,DOUBLE,1635201373,0,GOOD,1.0
unmodeled_alias1,DOUBLE,1635201374,0,GOOD,2.0
unmodeled_alias1,DOUBLE,1635201375,0,GOOD,3.0
unmodeled_alias1,DOUBLE,1635201376,0,GOOD,4.0
unmodeled_alias1,DOUBLE,1635201377,0,GOOD,5.0
unmodeled_alias1,DOUBLE,1635201378,0,GOOD,6.0
unmodeled_alias1,DOUBLE,1635201379,0,GOOD,7.0
unmodeled_alias1,DOUBLE,1635201380,0,GOOD,8.0
unmodeled_alias1,DOUBLE,1635201381,0,GOOD,9.0
unmodeled_alias1,DOUBLE,1635201382,0,GOOD,10.0
```

AWS IoT SiteWise provides the following API operations to create a bulk import job and get information
about an existing job.

- [CreateBulkImportJob](../APIReference/API_CreateBulkImportJob.md "../APIReference/API_CreateBulkImportJob.md")
  – Creates a new bulk import job.
- [DescribeBulkImportJob](../APIReference/API_DescribeBulkImportJob.md "../APIReference/API_DescribeBulkImportJob.md") – Retrieves information about a bulk import
  job.
- [ListBulkImportJob](../APIReference/API_ListBulkImportJobs.md "../APIReference/API_ListBulkImportJobs.md")
  – Retrieves a paginated list of summaries of all bulk import jobs.
