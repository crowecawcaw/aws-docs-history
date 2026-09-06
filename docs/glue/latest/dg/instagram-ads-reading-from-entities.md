

# Reading from Instagram Ads entities
<a name="instagram-ads-reading-from-entities"></a>

**Prerequisite**

A Instagram Ads object you would like to read from. You will need the object name. The following tables shows the supported entities.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Campaign | Yes | Yes | No | Yes | Yes | 
| Ad Set | Yes | Yes | No | Yes | Yes | 
| Ads | Yes | Yes | No | Yes | Yes | 
| Ad Creative | No | Yes | No | Yes | No | 
| Insights - Account | No | Yes | No | Yes | No | 
| Ad Image | Yes | Yes | No | Yes | No | 
| Insights - Ad | Yes | Yes | No | Yes | Yes | 
| Insights - AdSet | Yes | Yes | No | Yes | Yes | 
| Insights - Campaign | Yes | Yes | No | Yes | Yes | 

**Example**:

```
instagramAds_read = glueContext.create_dynamic_frame.from_options(
    connection_type="instagramads",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v20.0"
    }
```

## Instagram Ads entity and field details
<a name="instagram-ads-reading-entity-and-field-details"></a>

For more information about the entities and field details see:
+ [Campaign](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group)
+ [Ad Set](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign)
+ [Ad](https://developers.facebook.com/docs/marketing-api/reference/adgroup)
+ [Ad Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative)
+ [Ad Account Insight](https://developers.facebook.com/docs/marketing-api/reference/ad-account/insights)
+ [Ad Image](https://developers.facebook.com/docs/marketing-api/reference/ad-image)
+ [Ad Insights](https://developers.facebook.com/docs/marketing-api/reference/adgroup/insights/)
+ [AdSets Insights](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/insights)
+ [Campaigns Insights](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/insights)

For more information, see [Marketing API](https://developers.facebook.com/docs/marketing-api/reference/v21.0).

**Note**  
Struct and List data types are converted to String data type in the response of the connectors.

## Partitioning queries
<a name="instagram-ads-reading-partitioning-queries"></a>

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `PARTITION_FIELD`: the name of the field to be used to partition the query.
+ `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

  For the DateTime field, we accept the Spark timestamp format used in Spark SQL queries.

  Example of valid value:

  ```
  "2022-01-01T00:00:00.000Z"
  ```
+ `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.

  Example of valid value:

  ```
  "2024-01-02T00:00:00.000Z"
  ```
+ `NUM_PARTITIONS`: the number of partitions.

Example:

```
instagramADs_read = glueContext.create_dynamic_frame.from_options(
    connection_type="instagramads",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v20.0",
        "PARTITION_FIELD": "created_time"
        "LOWER_BOUND": "2022-01-01T00:00:00.000Z"
        "UPPER_BOUND": "2024-01-02T00:00:00.000Z"
        "NUM_PARTITIONS": "10"
    }
```