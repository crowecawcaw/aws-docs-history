

# Reading from HubSpot entities
<a name="hubspot-reading-from-entities"></a>

**Prerequisite**

A HubSpot object you would like to read from. You will need the object name such as contact or task. The following table shows the supported entities for Sync source.

## Supported entities for Sync source
<a name="sync-table"></a>


| Entity | API version | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partioning | 
| --- | --- | --- | --- | --- | --- | --- | 
| Campaigns | v1 | No | Yes | No | Yes | No | 
| Companies | v3 | Yes | Yes | Yes | Yes | Yes | 
| Contacts | v3 | Yes | Yes | Yes | Yes | Yes | 
| Contact Lists | v1 | No | Yes | No | Yes | No | 
| Deals | v3 | Yes | Yes | Yes | Yes | Yes | 
| CRM Pipeline (Deal Pipelines) | v1 | No | No | No | Yes | No | 
| Email Events | v1 | No | Yes | No | Yes | No | 
| Calls | v3 | Yes | Yes | Yes | Yes | Yes | 
| Notes | v3 | Yes | Yes | Yes | Yes | Yes | 
| Emails | v3 | Yes | Yes | Yes | Yes | Yes | 
| Meetings | v3 | Yes | Yes | Yes | Yes | Yes | 
| Tasks | v3 | Yes | Yes | Yes | Yes | Yes | 
| Postal Mails | v3 | Yes | Yes | Yes | Yes | Yes | 
| Custom Objects | v3 | Yes | Yes | Yes | Yes | Yes | 
| Forms | v2 | No | No | No | Yes | No | 
| Owners | v3 | No | Yes | No | Yes | No | 
| Products | v3 | Yes | Yes | Yes | Yes | Yes | 
| Tickets | v3 | Yes | Yes | Yes | Yes | Yes | 
| Workflows | v3 | No | No | No | Yes | No | 
| Associations | v4 | Yes | No | No | Yes | No | 
| Associations Labels | v4 | No | No | No | Yes | No | 

**Example**:

```
hubspot_read = glueContext.create_dynamic_frame.from_options(
    connection_type="hubspot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "contact",
        "API_VERSION": "v3"
    }
```

## Supported entities for Async source
<a name="async-table"></a>


| Entity | API version | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partioning | 
| --- | --- | --- | --- | --- | --- | --- | 
| Companies | v3 | Yes | No | Yes | Yes | No | 
| Contacts | v3 | Yes | No | Yes | Yes | No | 
| Deals | v3 | Yes | No | Yes | Yes | No | 
| Calls | v3 | Yes | No | Yes | Yes | No | 
| Notes | v3 | Yes | No | Yes | Yes | No | 
| Emails | v3 | Yes | No | Yes | Yes | No | 
| Meetings | v3 | Yes | No | Yes | Yes | No | 
| Tasks | v3 | Yes | No | Yes | Yes | No | 
| Postal Mails | v3 | Yes | No | Yes | Yes | No | 
| Custom Objects | v3 | Yes | No | Yes | Yes | No | 
| Products | v3 | Yes | No | Yes | Yes | No | 
| Tickets | v3 | Yes | No | Yes | Yes | No | 

**Example**:

```
hubspot_read = glueContext.create_dynamic_frame.from_options(
    connection_type="hubspot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "contact",
        "API_VERSION": "v3",
        "TRANSFER_MODE": "ASYNC"
    }
```

**HubSpot entity and field details**:

**HubSpot API v4**: 



- **Association Label**
  - **API version:** v4
  - **Field:** category / **Data type:** String / **Supported operators:** N/A
  - **Field:** typeId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** label / **Data type:** String / **Supported operators:** N/A

- **Associations**
  - **Field:** from / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** id / **Data type:** String / **Supported operators:** "="
  - **Field:** to / **Data type:** List / **Supported operators:** N/A



**Note**  
For the `Associations` object, to fetch associations between two objects, you need to provide the 'from Id' (the ID of the first object) via a mandatory filter while creating an AWS Glue job. If you want to fetch associations for multiple from IDs in that case, you have to provide multiple IDs in the `where` clause. For example: for fetching `Associations` for contact IDs '1' and '151', you need to provide a filter as `where id=1 AND id=151`.

**HubSpot API v3**:



- **Owner**
  - **Field:** firstName / **Data type:** String / **Supported operators:** N/A
  - **Field:** lastName / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** archived / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** teams / **Data type:** List / **Supported operators:** N/A
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** userId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** email / **Data type:** String / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A

- **Workflow**
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** N/A
  - **Field:** enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** insertedAt / **Data type:** Long / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** Long / **Supported operators:** N/A
  - **Field:** contactListIds / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** personaTagIds / **Data type:** List / **Supported operators:** N/A



For the following entities, HubSpot provides endpoints to fetch metadata dynamically, so that operator support is captured at the datatype level for each entity.

**Note**  
`DML_STATUS` is a virtual field added on every record at runtime to determine its status (CREATED/UPDATED) in the Sync mode. The `CONTAINS/LIKE` operator is not supported in the Async mode.



- **Contact**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Company**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Deal**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Ticket**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Product**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Custom Object**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Call**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Email**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Meeting**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Note**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Task**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A

- **Postal Mail**
  - **Data type:** Integer / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** Long / **Supported operators:** "=, \!=, <, >, >=, <="
  - **Data type:** String / **Supported operators:** "=, \!=, LIKE"
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** "between"
  - **Data type:** Boolean / **Supported operators:** "="
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A



**HubSpot API v2**:



- **Form**
  - **Field:** portalId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** guid / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** method / **Data type:** String / **Supported operators:** N/A
  - **Field:** cssClass / **Data type:** String / **Supported operators:** N/A
  - **Field:** redirect / **Data type:** String / **Supported operators:** N/A
  - **Field:** submitText / **Data type:** String / **Supported operators:** N/A
  - **Field:** notifyRecipients / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** Long / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** Long / **Supported operators:** N/A
  - **Field:** ignoreCurrentValues / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** deletable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** inlineMessage / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** captchaEnabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** cloneable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** formFieldGroups / **Data type:** List / **Supported operators:** N/A
  - **Field:** editable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** deletedAt / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** themeName / **Data type:** String / **Supported operators:** N/A
  - **Field:** parentId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** style / **Data type:** String / **Supported operators:** N/A
  - **Field:** isPublished / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** publishAt / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** unpublishAt / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** publishedAt / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** kickbackEmailWorkflowId / **Data type:** String / **Supported operators:** N/A
  - **Field:** kickbackEmailsJson / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** customUid / **Data type:** String / **Supported operators:** N/A
  - **Field:** createMarketableContact / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** editVersion / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** thankYouMessageJson / **Data type:** String / **Supported operators:** N/A
  - **Field:** themeColor / **Data type:** String / **Supported operators:** N/A
  - **Field:** alwaysCreateNewCompany / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** internalUpdatedAt / **Data type:** Long / **Supported operators:** N/A
  - **Field:** businessUnitId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** portableKey / **Data type:** String / **Supported operators:** N/A
  - **Field:** paymentSessionTemplateIds / **Data type:** List / **Supported operators:** N/A
  - **Field:** selectedExternalOptions / **Data type:** List / **Supported operators:** N/A



**HubSpot API v1**:



- **Campaign**
  - **Field:** id / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** appId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** appName / **Data type:** String / **Supported operators:** N/A
  - **Field:** lastUpdatedTime / **Data type:** Long / **Supported operators:** N/A

- **Contact\_List**
  - **Field:** dynamic / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** portalId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** Long / **Supported operators:** N/A
  - **Field:** listId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** Long / **Supported operators:** N/A
  - **Field:** ListType / **Data type:** String / **Supported operators:** N/A
  - **Field:** filters / **Data type:** List / **Supported operators:** N/A
  - **Field:** authorId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** metaData / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** archived / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** ilsFilterBranch / **Data type:** String / **Supported operators:** N/A
  - **Field:** filterIds / **Data type:** List / **Supported operators:** N/A
  - **Field:** limitExempt / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** internal / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** readOnly / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** parentId / **Data type:** Integer / **Supported operators:** N/A

- **Email\_Event**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** N/A
  - **Field:** recipient / **Data type:** String / **Supported operators:** N/A
  - **Field:** portalId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** appId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** appName / **Data type:** String / **Supported operators:** N/A
  - **Field:** emailCampaignId / **Data type:** Long / **Supported operators:** N/A
  - **Field:** attempt / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** created / **Data type:** Long / **Supported operators:** N/A
  - **Field:** sentBy / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** smtpId / **Data type:** String / **Supported operators:** N/A
  - **Field:** response / **Data type:** String / **Supported operators:** N/A
  - **Field:** subject / **Data type:** String / **Supported operators:** N/A
  - **Field:** cc / **Data type:** List / **Supported operators:** N/A
  - **Field:** bcc / **Data type:** List / **Supported operators:** N/A
  - **Field:** replyTo / **Data type:** List / **Supported operators:** N/A
  - **Field:** from / **Data type:** String / **Supported operators:** N/A
  - **Field:** dropReason / **Data type:** String / **Supported operators:** N/A
  - **Field:** dropMessage / **Data type:** String / **Supported operators:** N/A
  - **Field:** browser / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** userAgent / **Data type:** String / **Supported operators:** N/A
  - **Field:** duration / **Data type:** Long / **Supported operators:** N/A
  - **Field:** location / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** filteredEvent / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** deviceType / **Data type:** String / **Supported operators:** N/A
  - **Field:** suppressedReason / **Data type:** String / **Supported operators:** N/A
  - **Field:** suppressedMessage / **Data type:** String / **Supported operators:** N/A

- **CRM\_Pipeline**
  - **Field:** pipelineId
  - **Data type:** String
  - **Supported operators:** N/A

- ****
  - **Field:** createdAt
  - **Data type:** Long
  - **Supported operators:** N/A

- ****
  - **Field:** updatedAt
  - **Data type:** Long
  - **Supported operators:** N/A

- ****
  - **Field:** objectType
  - **Data type:** String
  - **Supported operators:** N/A

- ****
  - **Field:** label
  - **Data type:** String
  - **Supported operators:** N/A

- ****
  - **Field:** displayOrder
  - **Data type:** Integer
  - **Supported operators:** N/A

- ****
  - **Field:** active
  - **Data type:** Boolean
  - **Supported operators:** N/A

- ****
  - **Field:** stages
  - **Data type:** List
  - **Supported operators:** N/A

- ****
  - **Field:** objectTypeId
  - **Data type:** String
  - **Supported operators:** N/A

- ****
  - **Field:** default
  - **Data type:** Boolean
  - **Supported operators:** N/A



## Partitioning queries
<a name="hubspot-reading-partitioning-queries"></a>

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `PARTITION_FIELD`: the name of the field to be used to partition the query.
+ `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

  For the DateTime field, we accept the value in ISO format.

  Examples of valid value:

  ```
  “2024-01-01T10:00:00.115Z" 
  ```
+ `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
+ `NUM_PARTITIONS`: the number of partitions.

The following table describes the entity partitioning field support details:



- **contact**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, lastmodifieddate / **Data type:** DateTime

- **company**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **deal**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **ticket**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **product**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **custom\_object**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **call**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **email**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **meeting**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **note**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **task**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime

- **postal\_mail**
  - **Partitioning fields:** hs\_object\_id / **Data type:** Long
  - **Partitioning fields:** createdate, hs\_lastmodifieddate / **Data type:** DateTime



Example:

```
hubspot_read = glueContext.create_dynamic_frame.from_options(
    connection_type="hubspot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "company",
        "API_VERSION": "v3",
        "PARTITION_FIELD": "hs_object_id"
        "LOWER_BOUND": "50"
        "UPPER_BOUND": "16726619290"
        "NUM_PARTITIONS": "10"
    }
```