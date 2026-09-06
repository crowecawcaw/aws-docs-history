

# Reading from Salesforce Marketing Cloud entities
<a name="salesforce-marketing-cloud-reading-from-entities"></a>

**Prerequisite**

A Salesforce Marketing Cloud object you would like to read from. You will need the object name such as `Activity` or `Campaigns`. The following table shows the supported entities.

**Supported entities for source**:


| Entity | Interface | Can be filtered | Supports limit | Supports Order by | Supports SELECT \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | --- | 
| Event Notification Callback | REST | No | No | No | Yes | No | 
| Seed-List | REST | No | Yes | No | Yes | No | 
| Setup | REST | Yes | Yes | No | Yes | No | 
| Domain Verification | REST | Yes | Yes | Yes | Yes | No | 
| Objects Nested Tags | REST | Yes | No | No | Yes | No | 
| Contact | REST | No | Yes | No | Yes | No | 
| Event Notification Subscription | REST | No | No | No | Yes | No | 
| Messaging | REST | No | Yes | No | Yes | No | 
| Activity | SOAP | No | No | No | Yes | Yes | 
| Bounce Event | SOAP | No | No | No | Yes | Yes | 
| Click Event | SOAP | No | No | No | Yes | Yes | 
| Content Area | SOAP | No | No | No | Yes | Yes | 
| Data Extension | SOAP | No | Yes | No | Yes | Yes | 
| Email | SOAP | No | Yes | No | Yes | Yes | 
| Forwarded Email Event | SOAP | No | Yes | No | Yes | Yes | 
| Forward Email OptInEvent | SOAP | No | Yes | No | Yes | Yes | 
| Link | SOAP | No | Yes | No | Yes | Yes | 
| Link Send | SOAP | No | Yes | No | Yes | Yes | 
| List | SOAP | No | Yes | No | Yes | Yes | 
| List Subscriber | SOAP | No | Yes | No | Yes | Yes | 
| Not Sent Event | SOAP | No | Yes | No | Yes | Yes | 
| Open Event | SOAP | No | Yes | No | Yes | Yes | 
| Send | SOAP | No | Yes | No | Yes | Yes | 
| Sent Event | SOAP | No | Yes | No | Yes | Yes | 
| Subscriber | SOAP | No | Yes | No | Yes | Yes | 
| Survey Event | SOAP | No | Yes | No | Yes | Yes | 
| Unsub Event | SOAP | No | Yes | No | Yes | Yes | 
| Audit Events | REST | No | Yes | Yes | Yes | No | 
| Campaigns | REST | No | Yes | Yes | Yes | No | 
| Interactions | REST | No | Yes | Yes | Yes | No | 
| Content Assets | REST | No | Yes | Yes | Yes | No | 

**Example for REST**:

```
salesforcemarketingcloud_read = glueContext.create_dynamic_frame.from_options(
    connection_type="salesforcemarketingcloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Campaigns",
        "API_VERSION": "v1",
        "INSTANCE_URL": "https://**********************.rest.marketingcloudapis.com"
    }
)
```

**Example for SOAP**:

```
salesforcemarketingcloud_read = glueContext.create_dynamic_frame.from_options(
    connection_type="salesforcemarketingcloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Activity",
        "API_VERSION": "v1",
        "INSTANCE_URL": "https://**********************.soap.marketingcloudapis.com"
    }
)
```

**Salesforce Marketing Cloud entity and field details**:

The following tables describe the Salesforce Marketing Cloud entities. There are REST entities with static metadata and SOAP entities with dynamic metadata.

**REST entities with static metadata**:



- **Event Notification Callback**
  - **Field:** callbackId / **Data type:** String / **Supported operators:** 
  - **Field:** callbackName / **Data type:** String / **Supported operators:** 
  - **Field:** url / **Data type:** String / **Supported operators:** 
  - **Field:** maxBatchSize / **Data type:** Integer / **Supported operators:** 
  - **Field:** status / **Data type:** String / **Supported operators:** 
  - **Field:** statusReason / **Data type:** String / **Supported operators:** 

- **Seed-List**
  - **Field:** id / **Data type:** String / **Supported operators:** 
  - **Field:** name / **Data type:** String / **Supported operators:** 
  - **Field:** description / **Data type:** String / **Supported operators:** 
  - **Field:** activeSeedCount / **Data type:** Integer / **Supported operators:** 

- **Setup**
  - **Field:** customerKey / **Data type:** String / **Supported operators:** 
  - **Field:** name / **Data type:** String / **Supported operators:** 
  - **Field:** description / **Data type:** String / **Supported operators:** 
  - **Field:** locationType / **Data type:** String / **Supported operators:** '='
  - **Field:** awsFileTransferLocation / **Data type:** Struct / **Supported operators:** 

- **Domain verification**
  - **Field:** enterpriseId / **Data type:** Integer / **Supported operators:** 
  - **Field:** status / **Data type:** String / **Supported operators:** '='
  - **Field:** domainType / **Data type:** String / **Supported operators:** '='
  - **Field:** memberId / **Data type:** Integer / **Supported operators:** 
  - **Field:** emailSendTime / **Data type:** DateTime / **Supported operators:** 
  - **Field:** domain / **Data type:** String / **Supported operators:** 
  - **Field:** isSendable / **Data type:** Boolean / **Supported operators:** 

- **Objects Nested Tags**
  - **Field:** id / **Data type:** Integer / **Supported operators:** 
  - **Field:** modifiedDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** tags / **Data type:** List / **Supported operators:** 
  - **Field:** name / **Data type:** String / **Supported operators:** 
  - **Field:** description / **Data type:** String / **Supported operators:** 
  - **Field:** parentId / **Data type:** Integer / **Supported operators:** 

- **Contact**
  - **Field:** values
  - **Data type:** List
  - **Supported operators:** 

- **Event Notification Subscription**
  - **Field:** subscriptionName / **Data type:** String / **Supported operators:** 
  - **Field:** callbackId / **Data type:** String / **Supported operators:** 
  - **Field:** callbackName / **Data type:** String / **Supported operators:** 
  - **Field:** eventCategoryTypes / **Data type:** List / **Supported operators:** 
  - **Field:** filters / **Data type:** List / **Supported operators:** 
  - **Field:** url / **Data type:** String / **Supported operators:** 
  - **Field:** maxBatchSize / **Data type:** Integer / **Supported operators:** 
  - **Field:** subscriptionId / **Data type:** String / **Supported operators:** 
  - **Field:** status / **Data type:** String / **Supported operators:** 
  - **Field:** statusReason / **Data type:** String / **Supported operators:** 

- **Messaging**
  - **Field:** deliveryTime / **Data type:** DateTime / **Supported operators:** 
  - **Field:** id / **Data type:** String / **Supported operators:** 
  - **Field:** messageId / **Data type:** String / **Supported operators:** 
  - **Field:** status / **Data type:** String / **Supported operators:** 
  - **Field:** to / **Data type:** Struct / **Supported operators:** 

- **Interactions**
  - **Field:** status / **Data type:** String / **Supported operators:** '='
  - **Field:** id / **Data type:** String / **Supported operators:** 
  - **Field:** key / **Data type:** String / **Supported operators:** 
  - **Field:** name / **Data type:** String / **Supported operators:** 
  - **Field:** lastPublishedDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** description / **Data type:** String / **Supported operators:** 
  - **Field:** version / **Data type:** Integer / **Supported operators:** 
  - **Field:** workflowApiVersion / **Data type:** Integer / **Supported operators:** 
  - **Field:** createdDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** modifiedDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** goals / **Data type:** Struct / **Supported operators:** 
  - **Field:** stats / **Data type:** Struct / **Supported operators:** 
  - **Field:** entryMode / **Data type:** String / **Supported operators:** 
  - **Field:** defaults / **Data type:** Struct / **Supported operators:** 
  - **Field:** executionMode / **Data type:** Struct / **Supported operators:** 
  - **Field:** definitionId / **Data type:** String / **Supported operators:** 

- **Content Assets**
  - **Field:** id / **Data type:** Integer / **Supported operators:** 
  - **Field:** customerKey / **Data type:** String / **Supported operators:** 
  - **Field:** objectId / **Data type:** String / **Supported operators:** 
  - **Field:** contentType / **Data type:** String / **Supported operators:** 
  - **Field:** assetType / **Data type:** Struct / **Supported operators:** 
  - **Field:** name / **Data type:** String / **Supported operators:** 
  - **Field:** description / **Data type:** String / **Supported operators:** 
  - **Field:** owner / **Data type:** Struct / **Supported operators:** 
  - **Field:** createdDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** createdBy / **Data type:** Struct / **Supported operators:** 
  - **Field:** modifiedDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** modifiedBy / **Data type:** Struct / **Supported operators:** 
  - **Field:** thumbnail / **Data type:** Struct / **Supported operators:** 
  - **Field:** category / **Data type:** Struct / **Supported operators:** 
  - **Field:** meta / **Data type:** Struct / **Supported operators:** 
  - **Field:** views / **Data type:** Struct / **Supported operators:** 
  - **Field:** availableViews / **Data type:** Struct / **Supported operators:** 
  - **Field:** data / **Data type:** Struct / **Supported operators:** 
  - **Field:** legacyData / **Data type:** Struct / **Supported operators:** 
  - **Field:** modelVersion / **Data type:** Integer / **Supported operators:** 
  - **Field:** Version / **Data type:** Integer / **Supported operators:** 
  - **Field:** Locked / **Data type:** Boolean / **Supported operators:** 
  - **Field:** FileProperties / **Data type:** Struct / **Supported operators:** 
  - **Field:** Tags / **Data type:** List / **Supported operators:** 
  - **Field:** Content / **Data type:** String / **Supported operators:** 
  - **Field:** Design / **Data type:** String / **Supported operators:** 
  - **Field:** SuperContent / **Data type:** String / **Supported operators:** 
  - **Field:** CustomFields / **Data type:** Struct / **Supported operators:** 
  - **Field:** Blocks / **Data type:** Struct / **Supported operators:** 
  - **Field:** MinBlocks / **Data type:** Integer / **Supported operators:** 
  - **Field:** MaxBlocks / **Data type:** Integer / **Supported operators:** 
  - **Field:** Channels / **Data type:** Struct / **Supported operators:** 
  - **Field:** AllowedBlocks / **Data type:** List / **Supported operators:** 
  - **Field:** Slots / **Data type:** Struct / **Supported operators:** 
  - **Field:** BusinessUnitAvailability / **Data type:** Struct / **Supported operators:** 
  - **Field:** sharingProperties / **Data type:** Struct / **Supported operators:** 
  - **Field:** sharingProperties.sharedWith / **Data type:** Struct / **Supported operators:** 
  - **Field:** sharingProperties.sharingType / **Data type:** String / **Supported operators:** 
  - **Field:** Template / **Data type:** Struct / **Supported operators:** 
  - **Field:** File / **Data type:** String / **Supported operators:** 
  - **Field:** GenerateFrom / **Data type:** String / **Supported operators:** 

- **Audit Events**
  - **Field:** id / **Data type:** Integer / **Supported operators:** 
  - **Field:** createdDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** memberId / **Data type:** Integer / **Supported operators:** 
  - **Field:** enterpriseId / **Data type:** Integer / **Supported operators:** 
  - **Field:** employee / **Data type:** Struct / **Supported operators:** 
  - **Field:** objectType / **Data type:** Struct / **Supported operators:** 
  - **Field:** operation / **Data type:** Struct / **Supported operators:** 
  - **Field:** object / **Data type:** Struct / **Supported operators:** 
  - **Field:** transactionId / **Data type:** String / **Supported operators:** 

- **Campaigns**
  - **Field:** id / **Data type:** Integer / **Supported operators:** 
  - **Field:** createdDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** modifiedDate / **Data type:** DateTime / **Supported operators:** 
  - **Field:** name / **Data type:** String / **Supported operators:** 
  - **Field:** description / **Data type:** String / **Supported operators:** 
  - **Field:** campaignCode / **Data type:** String / **Supported operators:** 
  - **Field:** color / **Data type:** String / **Supported operators:** 
  - **Field:** favorite / **Data type:** Boolean / **Supported operators:** 



**SOAP entities with dynamic metadata**:



- **Activity**
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** Struct / **Supported operators:** 
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** Double / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** Boolean / **Supported operators:** \!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN

- **Bounce Event**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** Struct / **Supported operators:** 

- **Click Event**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** Struct / **Supported operators:** 

- **Content Area**
  - **Data type:** Struct / **Supported operators:** 
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Boolean / **Supported operators:** \!=,=

- **Data Extension**
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** String / **Supported operators:** LIKE,\!=,=

- **Email**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Boolean / **Supported operators:** \!=,=
  - **Data type:** Struct / **Supported operators:** 

- **Forwarded Email Event**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **Forwarded Email OptInEvent**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **Link**
  - **Data type:** Integer
  - **Supported operators:** \!=,=,>=,<=,<,>

- **Link Send**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** Double / **Supported operators:** \!=,=,>=,<=,<,>

- **List**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **List Subscriber**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **Not Sent Event**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **Open Event**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **Send**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Boolean / **Supported operators:** \!=,=
  - **Data type:** Struct / **Supported operators:** 

- **Sent Event**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **Subscriber**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **Survey Event**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Struct / **Supported operators:** 

- **Unsub Event**
  - **Data type:** Integer / **Supported operators:** \!=,=,>=,<=,<,>
  - **Data type:** String / **Supported operators:** LIKE,\!=,=
  - **Data type:** DateTime / **Supported operators:** >=,<=,<,>,=,BETWEEN
  - **Data type:** Boolean / **Supported operators:** \!=,=
  - **Data type:** Struct / **Supported operators:** 



## Partitioning queries
<a name="salesforce-marketing-cloud-reading-partitioning-queries"></a>

In Salesforce Marketing Cloud, the Integer and DateTime datatype fields support field-based partitioning.

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `PARTITION_FIELD`: the name of the field to be used to partition the query.
+ `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

  For the timestamp field, we accept the Spark timestamp format used in Spark SQL queries.

  Examples of valid value:

  ```
  “2024-05-07T02:03:00.00Z"
  ```
+ `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
+ `NUM_PARTITIONS`: the number of partitions.

Example:

```
salesforcemarketingcloud_read = glueContext.create_dynamic_frame.from_options(
    connection_type="salesforcemarketingcloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "ListSubscriber",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "CreatedDate",
        "LOWER_BOUND": "2023-09-07T02:03:00.000Z",
        "UPPER_BOUND": "2024-05-07T02:03:00.000Z",
        "NUM_PARTITIONS": "10"
    }
)
```