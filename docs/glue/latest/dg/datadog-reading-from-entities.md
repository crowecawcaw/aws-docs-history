

# Reading from Datadog entities
<a name="datadog-reading-from-entities"></a>

 **Prerequisites** 

A Datadog Object you would like to read from. Refer the supported entities table below to check the available entities. 

 **Supported entities** 


| Entity | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Metrics Timeseries | Yes | No | No | Yes | No | 
| Log Queries | Yes | Yes | Yes | Yes | No | 

 **Example** 

```
Datadog_read = glueContext.create_dynamic_frame.from_options(
    connection_type="datadog",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "log-queries",
        "API_VERSION": "v2",
        "INSTANCE_URL": "https://api.datadoghq.com",
        "FILTER_PREDICATE": "from = `2023-10-03T09:00:26Z`"
    }
```

 **Datadog entity and field details** 



- **Metrics Timeseries**
  - **Field:** error / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** aggr / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** attributes / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** display\_name / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** end / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** expression / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** interval / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** length / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** metric / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** pointlist / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** query\_index / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** scope / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** start / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** tag\_set / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** unit / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** from\_to\_date / **Data Type:** DateTime / ****Supported Operators**:** BETWEEN
  - **Field:** query / **Data Type:** String / ****Supported Operators**:** EQUAL\_TO
  - **Field:** status / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** type / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** host / **Data Type:** String / ****Supported Operators**:** NA

- **Log Queries**
  - **Field:** id / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** attributes / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** timestamp / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** type / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** from / **Data Type:** DateTime / ****Supported Operators**:** BETWEEN,EQUAL\_TO
  - **Field:** indexes / **Data Type:** List / ****Supported Operators**:** EQUAL\_TO
  - **Field:** storage\_tier / **Data Type:** String / ****Supported Operators**:** EQUAL\_TO
  - **Field:** query / **Data Type:** String / ****Supported Operators**:** EQUAL\_TO

