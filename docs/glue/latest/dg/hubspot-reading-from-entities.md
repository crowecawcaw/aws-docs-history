# Reading from HubSpot entities

**Prerequisite**

A HubSpot object you would like to read from. You will need the object name such as contact or task. The following table shows the supported entities for Sync source.

## Supported entities for Sync source

| Entity                        | API version | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partioning |
| ----------------------------- | ----------- | --------------- | -------------- | ----------------- | ------------------ | ------------------- |
| Campaigns                     | v1          | No              | Yes            | No                | Yes                | No                  |
| Companies                     | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Contacts                      | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Contact Lists                 | v1          | No              | Yes            | No                | Yes                | No                  |
| Deals                         | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| CRM Pipeline (Deal Pipelines) | v1          | No              | No             | No                | Yes                | No                  |
| Email Events                  | v1          | No              | Yes            | No                | Yes                | No                  |
| Calls                         | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Notes                         | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Emails                        | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Meetings                      | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Tasks                         | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Postal Mails                  | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Custom Objects                | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Forms                         | v2          | No              | No             | No                | Yes                | No                  |
| Owners                        | v3          | No              | Yes            | No                | Yes                | No                  |
| Products                      | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Tickets                       | v3          | Yes             | Yes            | Yes               | Yes                | Yes                 |
| Workflows                     | v3          | No              | No             | No                | Yes                | No                  |
| Associations                  | v4          | Yes             | No             | No                | Yes                | No                  |
| Associations Labels           | v4          | No              | No             | No                | Yes                | No                  |

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

| Entity         | API version | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partioning |
| -------------- | ----------- | --------------- | -------------- | ----------------- | ------------------ | ------------------- |
| Companies      | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Contacts       | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Deals          | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Calls          | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Notes          | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Emails         | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Meetings       | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Tasks          | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Postal Mails   | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Custom Objects | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Products       | v3          | Yes             | No             | Yes               | Yes                | No                  |
| Tickets        | v3          | Yes             | No             | Yes               | Yes                | No                  |

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

| Entity            | API version | Field    | Data type | Supported operators |
| ----------------- | ----------- | -------- | --------- | ------------------- |
| Association Label | v4          | category | String    | N/A                 |
| typeId            | Integer     | N/A      |
| label             | String      | N/A      |
| Associations      | from        | Struct   | N/A       |
| id                | String      | "="      |
| to                | List        | N/A      |

###### Note

For the `Associations` object, to fetch associations between two objects, you need to provide the 'from Id' (the ID of the first object) via a mandatory filter while creating an AWS Glue job. If you want to fetch associations for multiple from IDs in that case, you have to provide multiple IDs in the `where` clause. For example: for fetching `Associations` for contact IDs '1' and '151', you need to provide a filter as `where id=1 AND id=151`.

**HubSpot API v3**:

| Entity         | Field     | Data type | Supported operators |
| -------------- | --------- | --------- | ------------------- |
| Owner          | firstName | String    | N/A                 |
| lastName       | String    | N/A       |
| createdAt      | DateTime  | N/A       |
| archived       | Boolean   | N/A       |
| teams          | List      | N/A       |
| id             | String    | N/A       |
| userId         | Integer   | N/A       |
| email          | String    | N/A       |
| updatedAt      | DateTime  | N/A       |
| Workflow       | name      | String    | N/A                 |
| id             | Integer   | N/A       |
| type           | String    | N/A       |
| enabled        | Boolean   | N/A       |
| insertedAt     | Long      | N/A       |
| updatedAt      | Long      | N/A       |
| contactListIds | Struct    | N/A       |
| personaTagIds  | List      | N/A       |

For the following entities, HubSpot provides endpoints to fetch metadata dynamically, so that operator support is captured at the datatype level for each entity.

###### Note

`DML_STATUS` is a virtual field added on every record at runtime to determine its
status (CREATED/UPDATED) in the Sync mode. The `CONTAINS/LIKE` operator is not supported in the Async mode.

| Entity        | Data type             | Supported operators   |
| ------------- | --------------------- | --------------------- |
| Contact       | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Company       | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Deal          | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Ticket        | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Product       | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Custom Object | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Call          | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Email         | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Meeting       | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Note          | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Task          | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |
| Postal Mail   | Integer               | "=, !=, <, >, >=, <=" |
| Long          | "=, !=, <, >, >=, <=" |
| String        | "=, !=, LIKE"         |
| Date          | N/A                   |
| DateTime      | "between"             |
| Boolean       | "="                   |
| List          | N/A                   |
| Struct        | N/A                   |

**HubSpot API v2**:

| Entity                    | Field    | Data type | Supported operators |
| ------------------------- | -------- | --------- | ------------------- |
| Form                      | portalId | Integer   | N/A                 |
| guid                      | String   | N/A       |
| name                      | String   | N/A       |
| method                    | String   | N/A       |
| cssClass                  | String   | N/A       |
| redirect                  | String   | N/A       |
| submitText                | String   | N/A       |
| notifyRecipients          | String   | N/A       |
| createdAt                 | Long     | N/A       |
| updatedAt                 | Long     | N/A       |
| ignoreCurrentValues       | Boolean  | N/A       |
| deletable                 | Boolean  | N/A       |
| inlineMessage             | Boolean  | N/A       |
| captchaEnabled            | Boolean  | N/A       |
| cloneable                 | Boolean  | N/A       |
| formFieldGroups           | List     | N/A       |
| editable                  | Boolean  | N/A       |
| deletedAt                 | Integer  | N/A       |
| themeName                 | String   | N/A       |
| parentId                  | Integer  | N/A       |
| style                     | String   | N/A       |
| isPublished               | Boolean  | N/A       |
| publishAt                 | Integer  | N/A       |
| unpublishAt               | Integer  | N/A       |
| publishedAt               | Integer  | N/A       |
| kickbackEmailWorkflowId   | String   | N/A       |
| kickbackEmailsJson        | Integer  | N/A       |
| customUid                 | String   | N/A       |
| createMarketableContact   | Boolean  | N/A       |
| editVersion               | Integer  | N/A       |
| thankYouMessageJson       | String   | N/A       |
| themeColor                | String   | N/A       |
| alwaysCreateNewCompany    | Boolean  | N/A       |
| internalUpdatedAt         | Long     | N/A       |
| businessUnitId            | Integer  | N/A       |
| portableKey               | String   | N/A       |
| paymentSessionTemplateIds | List     | N/A       |
| selectedExternalOptions   | List     | N/A       |

**HubSpot API v1**:

| Entity            | Field        | Data type | Supported operators |
| ----------------- | ------------ | --------- | ------------------- |
| Campaign          | id           | Integer   | N/A                 |
| appId             | Integer      | N/A       |
| appName           | String       | N/A       |
| lastUpdatedTime   | Long         | N/A       |
| Contact_List      | dynamic      | Boolean   | N/A                 |
| name              | String       | N/A       |
| portalId          | Integer      | N/A       |
| createdAt         | Long         | N/A       |
| listId            | Integer      | N/A       |
| updatedAt         | Long         | N/A       |
| ListType          | String       | N/A       |
| filters           | List         | N/A       |
| authorId          | Integer      | N/A       |
| metaData          | Struct       | N/A       |
| archived          | Boolean      | N/A       |
| ilsFilterBranch   | String       | N/A       |
| filterIds         | List         | N/A       |
| limitExempt       | Boolean      | N/A       |
| internal          | Boolean      | N/A       |
| readOnly          | Boolean      | N/A       |
| parentId          | Integer      | N/A       |
| Email_Event       | id           | String    | N/A                 |
| type              | String       | N/A       |
| recipient         | String       | N/A       |
| portalId          | Integer      | N/A       |
| appId             | Integer      | N/A       |
| appName           | String       | N/A       |
| emailCampaignId   | Long         | N/A       |
| attempt           | Integer      | N/A       |
| created           | Long         | N/A       |
| sentBy            | Struct       | N/A       |
| smtpId            | String       | N/A       |
| response          | String       | N/A       |
| subject           | String       | N/A       |
| cc                | List         | N/A       |
| bcc               | List         | N/A       |
| replyTo           | List         | N/A       |
| from              | String       | N/A       |
| dropReason        | String       | N/A       |
| dropMessage       | String       | N/A       |
| browser           | Struct       | N/A       |
| userAgent         | String       | N/A       |
| duration          | Long         | N/A       |
| location          | Struct       | N/A       |
| filteredEvent     | Boolean      | N/A       |
| deviceType        | String       | N/A       |
| suppressedReason  | String       | N/A       |
| suppressedMessage | String       | N/A       |
| CRM_Pipeline      | pipelineId   | String    | N/A                 |
|                   | createdAt    | Long      | N/A                 |
|                   | updatedAt    | Long      | N/A                 |
|                   | objectType   | String    | N/A                 |
|                   | label        | String    | N/A                 |
|                   | displayOrder | Integer   | N/A                 |
|                   | active       | Boolean   | N/A                 |
|                   | stages       | List      | N/A                 |
|                   | objectTypeId | String    | N/A                 |
|                   | default      | Boolean   | N/A                 |

## Partitioning queries

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the DateTime field, we accept the value in ISO format.

Examples of valid value:

```
“2024-01-01T10:00:00.115Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

The following table describes the entity partitioning field support details:

| Entity name                                    | Partitioning fields | Data type |
| ---------------------------------------------- | ------------------- | --------- |
| contact                                        | hs_object_id        | Long      |
| createdate, lastmodifieddate                   | DateTime            |
| company                                        | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| deal                                           | hs_object_id        | Long      |
| createdate, hs_createdate, hs_lastmodifieddate | DateTime            |
| ticket                                         | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| product                                        | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| custom_object                                  | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| call                                           | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| email                                          | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| meeting                                        | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| note                                           | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| task                                           | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |
| postal_mail                                    | hs_object_id        | Long      |
| createdate, hs_lastmodifieddate                | DateTime            |

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
