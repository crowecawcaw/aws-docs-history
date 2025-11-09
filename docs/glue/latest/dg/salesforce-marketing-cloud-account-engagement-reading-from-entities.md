# Reading from Salesforce Marketing Cloud Account Engagement entities

**Prerequisite**

A Salesforce Marketing Cloud Account Engagement object you would like to read from. You will need the object name.

**Supported entities for Sync source**:

| Entity                    | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ------------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Campaign                  | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Dynamic Content           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Email                     | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Email Template            | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Engagement Studio Program | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Folder Contents           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Landing Page              | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Lifecycle History         | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Lifecycle Stage           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| List                      | Yes             | Yes            | Yes               | Yes                | Yes                   |
| List Email                | Yes             | Yes            | Yes               | Yes                | Yes                   |
| List Membership           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Opportunity               | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Prospect                  | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Prospect Account          | Yes             | Yes            | Yes               | Yes                | Yes                   |
| User                      | Yes             | Yes            | Yes               | Yes                | Yes                   |

**Example**:

```
salesforcepardot_read = glueContext.create_dynamic_frame.from_options(
    connection_type="SalesforcePardot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v5"
    }
   )
```

**Supported entities for Async source**:

| Entity            | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ----------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Campaign          | Yes             | No             | No                | Yes                | No                    |
| Dynamic Content   | Yes             | No             | No                | Yes                | No                    |
| Email Template    | Yes             | No             | No                | Yes                | No                    |
| Landing Page      | Yes             | No             | No                | Yes                | No                    |
| Lifecycle History | Yes             | No             | No                | Yes                | No                    |
| Lifecycle Stage   | Yes             | No             | No                | Yes                | No                    |
| List              | Yes             | No             | No                | Yes                | No                    |
| List Email        | Yes             | No             | No                | Yes                | No                    |
| List Membership   | Yes             | No             | No                | Yes                | No                    |
| Opportunity       | Yes             | No             | No                | Yes                | No                    |
| Prospect          | Yes             | No             | No                | Yes                | No                    |
| Prospect Account  | Yes             | No             | No                | Yes                | No                    |
| User              | Yes             | No             | No                | Yes                | No                    |

**Example**:

```
salesforcepardot_read = glueContext.create_dynamic_frame.from_options(
    connection_type="SalesforcePardot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v5",
        "TRANSFER_MODE": "ASYNC"
    }
   )
```

**Salesforce Marketing Cloud Account Engagement entity and field details**:

To view the field details for thhe following entities, navigate to [Salesforce Marketing Cloud Account Engagement API](https://developer.salesforce.com/docs/marketing/pardot "https://developer.salesforce.com/docs/marketing/pardot"), choose **Guides**, scroll down to **Open Source API Wrappers**, expand **Version 5 Docs** from the menu and choose an entity.

Entities list:

- Campaign
- Dynamic Content
- Email
- Email Template
- Engagement Studio Program
- Folder Content
- Landing Page
- Lifecycle History
- Lifecycle Stage
- List
- List Email
- List Membership
- Opportunity
- Prospect
- Prospect Account
- User
  In addition to the fields mentioned above, the Async mode supports specific filterable fields for each entity, as shown in the table below.

| Entity                    | Additional filterable fields supported in Async                                |
| ------------------------- | ------------------------------------------------------------------------------ |
| Campaign                  | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| Dynamic Content           | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| Email Template            | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| Engagement Studio Program | -                                                                              |
| Landing Page              | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| Lifecycle History         | `createdAfter`, `createdBefore`                                                |
| Lifecycle Stage           | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| List                      | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| List Email                | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| List Membership           | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| Opportunity               | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| Prospect                  | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |
| Prospect Account          | `createdAfter`, `createdBefore`, `deleted`                                     |
| User                      | `createdAfter`, `createdBefore`, `deleted`,<br>`updatedAfter`, `updatedBefore` |

For more information about the additional fields, refer to [Salesforce Export API](https://developer.salesforce.com/docs/marketing/pardot/guide/export-v5.html#procedures "https://developer.salesforce.com/docs/marketing/pardot/guide/export-v5.html#procedures")

Note the following considerations for the connector:

- The value of the `delete` field in the entities can be `false` (default), `true`, or `all`.

## Partitioning queries

**Filter-based partitioning**:

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and
`NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
these parameters, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks
concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the Datetime field, we accept the Spark timestamp format used in SPark SQL queries.

Examples of valid value:

```
"2022-01-01T01:01:01.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.
- `PARTITION_BY`: the type of partitioning to be performed. "FIELD" is to be passed in case of field-based partitioning.

Example:

```
salesforcepardot_read = glueContext.create_dynamic_frame.from_options(
    connection_type="salesforcepardot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v5",
        "PARTITION_FIELD": "createdAt"
        "LOWER_BOUND": "2022-01-01T01:01:01.000Z"
        "UPPER_BOUND": "2024-01-01T01:01:01.000Z"
        "NUM_PARTITIONS": "10",
        "PARTITION_BY": "FIELD"
    }
   )
```
