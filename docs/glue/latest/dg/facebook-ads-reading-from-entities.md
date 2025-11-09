# Reading from Facebook Ads entities

**Prerequisite**

A Facebook Ads object you would like to read from. You will need the object name. The following tables shows the supported entities.

**Supported entities for source**:

| Entity                 | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ---------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Campaign               | Yes             | Yes            | No                | Yes                | Yes                   |
| Ad Set                 | Yes             | Yes            | No                | Yes                | Yes                   |
| Ads                    | Yes             | Yes            | No                | Yes                | Yes                   |
| Ad Creative            | No              | Yes            | No                | Yes                | No                    |
| Insights<br>• Account  | No              | Yes            | No                | Yes                | No                    |
| Adaccounts             | Yes             | Yes            | No                | Yes                | No                    |
| Insights<br>• Ad       | Yes             | Yes            | No                | Yes                | Yes                   |
| Insights<br>• AdSet    | Yes             | Yes            | No                | Yes                | Yes                   |
| Insights<br>• Campaign | Yes             | Yes            | No                | Yes                | Yes                   |

**Example**:

```
FacebookAds_read = glueContext.create_dynamic_frame.from_options(
    connection_type="FacebookAds",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v20.0"
    }
```

## Facebook Ads entity and field details

For more information about the entities and field details see:

- [Ad Account](https://developers.facebook.com/docs/marketing-api/reference/ad-account "https://developers.facebook.com/docs/marketing-api/reference/ad-account")
- [Campaign](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group "https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group")
- [Ad Set](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign "https://developers.facebook.com/docs/marketing-api/reference/ad-campaign")
- [Ad](https://developers.facebook.com/docs/marketing-api/reference/adgroup "https://developers.facebook.com/docs/marketing-api/reference/adgroup")
- [Ad Creative](https://developers.facebook.com/docs/marketing-api/reference/ad-creative "https://developers.facebook.com/docs/marketing-api/reference/ad-creative")
- [Insight Ad Account](https://developers.facebook.com/docs/marketing-api/reference/ad-account/insights "https://developers.facebook.com/docs/marketing-api/reference/ad-account/insights")
- [Insights Ads](https://developers.facebook.com/docs/marketing-api/reference/adgroup/insights/ "https://developers.facebook.com/docs/marketing-api/reference/adgroup/insights/")
- [Insights AdSets](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/insights "https://developers.facebook.com/docs/marketing-api/reference/ad-campaign/insights")
- [Insights Campaigns](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/insights "https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/insights")

For more information, see [Marketing API](https://developers.facebook.com/docs/marketing-api/reference/v21.0 "https://developers.facebook.com/docs/marketing-api/reference/v21.0").

###### Note

Struct and List data types are converted to String data type in the response of the connectors.

## Partitioning queries

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the DateTime field, we accept the Spark timestamp format used in Spark SQL queries.

Example of valid value:

```
"2022-01-01"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

Example:

```
FacebookADs_read = glueContext.create_dynamic_frame.from_options(
    connection_type="FacebookAds",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v20.0",
        "PARTITION_FIELD": "created_time"
        "LOWER_BOUND": "2022-01-01"
        "UPPER_BOUND": "2024-01-02"
        "NUM_PARTITIONS": "10"
    }
```
