

# Reading from Microsoft Dynamics 365 CRM entities
<a name="microsoft-dynamics-365-reading-from-entities"></a>

 **Prerequisites** 
+  A Microsoft Dynamics 365 CRM object you would like to read from. You will need the object name such as contacts or accounts. The following table shows the supported entities. 

 **Supported entities** 


| Entity | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Dynamic entity | Yes | Yes | Yes | Yes | Yes | 

 **Example** 

```
dynamics365_read = glueContext.create_dynamic_frame.from_options(
    connection_type="microsoftdynamics365crm",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "dynamic_entity",
        "API_VERSION": "v9.2",
        "INSTANCE_URL": "https://{tenantID}.api.crm.dynamics.com"
    }
```

## Microsoft Dynamics 365 CRM Entity and Field Details
<a name="microsoft-dynamics-365-entity-and-field-details"></a>

 **Entities with dynamic metadata:** 

Microsoft Dynamics 365 CRM provides endpoints to fetch metadata dynamically. Therefore, for dynamic entities, the operator support is captured at datatype level.

<a name="microsoft-dynamics-365-metadata-table"></a>

- **Dynamic entity**
  - **Data Type:** DateTime / **Supported Operators:**  =, <, <=, >, >=, BETWEEN
  - **Data Type:** Date / **Supported Operators:**  =, <, <=, >, >=
  - **Data Type:** String / **Supported Operators:**  =, \!=
  - **Data Type:** Double / **Supported Operators:**  =, <, <=, >, >=
  - **Data Type:** Integer / **Supported Operators:**  =, <, <=, >, >=
  - **Data Type:** Decimal / **Supported Operators:**  =, <, <=, >, >=
  - **Data Type:** Long / **Supported Operators:**  =, <, <=, >, >=
  - **Data Type:** BigInteger / **Supported Operators:**  =, <, <=, >, >=
  - **Data Type:** List / **Supported Operators:** NA
  - **Data Type:** Struct / **Supported Operators:** NA
  - **Data Type:** Map / **Supported Operators:** NA



 **Partitioning queries** 

Microsoft Dynamics 365 CRM supports only field based partitioning.

 Additional spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, `NUM_PARTITIONS` can be provided if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by spark tasks concurrently. 
+  `PARTITION_FIELD`: the name of the field to be used to partition query. 
+  `LOWER_BOUND`: an inclusive lower bound value of the chosen partition field. 

   For Datetime, we accept the Spark timestamp format used in Spark SQL queries. Example of valid values: `"2024-01-30T06:47:51.000Z"`. 
+  `UPPER_BOUND`: an exclusive upper bound value of the chosen partition field. 
+  `NUM_PARTITIONS`: number of partitions. 

 Entity wise partitioning field support details are captured in below table: 


| Entity Name | Partitioning Fields | DataType | 
| --- | --- | --- | 
| Dynamic Entity (Standard entity) | Dynamic DateTime fields which are queryable | createdon, modifiedon | 
| Dynamic Entity (Custom entity) | createdon, modifiedon | createdon, modifiedon | 

 **Example** 

```
dynamics365_read = glueContext.create_dynamic_frame.from_options(
    connection_type="microsoftdynamics365crm",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "dynamic_entity",
        "API_VERSION": "v9.2",
        "instanceUrl": "https://{tenantID}.api.crm.dynamics.com"
        "PARTITION_FIELD": "createdon"
        "LOWER_BOUND": "2024-01-30T06:47:51.000Z"
        "UPPER_BOUND": "2024-06-30T06:47:51.000Z"
        "NUM_PARTITIONS": "10"
    }
```