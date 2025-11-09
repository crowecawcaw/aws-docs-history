# Reading from Pipedrive entities

**Prerequisites**

- A Pipedrive Object you would like to read from. Refer the supported entities table below to check the available
  entities.

**Supported entities**

| Entity          | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| --------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Activities      | Yes             | Yes            | No                | Yes                | Yes                   |
| Activity Type   | No              | No             | No                | Yes                | No                    |
| Call Logs       | No              | No             | No                | Yes                | No                    |
| Currencies      | Yes             | Yes            | No                | Yes                | No                    |
| Deals           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Leads           | Yes             | Yes            | Yes               | Yes                | No                    |
| Lead Sources    | No              | Yes            | No                | Yes                | No                    |
| Lead Labels     | No              | No             | No                | No                 | No                    |
| Notes           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Organization    | Yes             | Yes            | No                | Yes                | Yes                   |
| Permission Sets | Yes             | No             | No                | Yes                | No                    |
| Persons         | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Pipelines       | No              | Yes            | No                | Yes                | No                    |
| Products        | Yes             | Yes            | No                | Yes                | Yes                   |
| Roles           | No              | Yes            | No                | Yes                | No                    |
| Stages          | Yes             | Yes            | No                | Yes                | No                    |
| Users           | No              | No             | No                | Yes                | No                    |

**Example**

```
pipedrive_read= glueContext.create_dynamic_frame.from_options(
    connection_type="PIPEDRIVE",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "activites",
        "API_VERSION": "v1"
    }
```

**Pipedrive entity and field details**

Entities list:

- Activities: [https://developers.pipedrive.com/docs/api/v1/Activities](https://developers.pipedrive.com/docs/api/v1/Activities "https://developers.pipedrive.com/docs/api/v1/Activities")
- Activity Type: [https://developers.pipedrive.com/docs/api/v1/ActivityTypes](https://developers.pipedrive.com/docs/api/v1/ActivityTypes "https://developers.pipedrive.com/docs/api/v1/ActivityTypes")
- Call Logs: [https://developers.pipedrive.com/docs/api/v1/CallLogs](https://developers.pipedrive.com/docs/api/v1/CallLogs "https://developers.pipedrive.com/docs/api/v1/CallLogs")
- Currencies: [https://developers.pipedrive.com/docs/api/v1/Currencies](https://developers.pipedrive.com/docs/api/v1/Currencies "https://developers.pipedrive.com/docs/api/v1/Currencies")
- Deals: [https://developers.pipedrive.com/docs/api/v1/Deals](https://developers.pipedrive.com/docs/api/v1/Deals "https://developers.pipedrive.com/docs/api/v1/Deals")
- Leads: [https://developers.pipedrive.com/docs/api/v1/Leads](https://developers.pipedrive.com/docs/api/v1/Leads "https://developers.pipedrive.com/docs/api/v1/Leads")
- Lead Sources: [https://developers.pipedrive.com/docs/api/v1/LeadSources](https://developers.pipedrive.com/docs/api/v1/LeadSources "https://developers.pipedrive.com/docs/api/v1/LeadSources")
- Lead Labels: [https://developers.pipedrive.com/docs/api/v1/LeadLabels](https://developers.pipedrive.com/docs/api/v1/LeadLabels "https://developers.pipedrive.com/docs/api/v1/LeadLabels")
- Notes: [https://developers.pipedrive.com/docs/api/v1/Notes](https://developers.pipedrive.com/docs/api/v1/Notes "https://developers.pipedrive.com/docs/api/v1/Notes")
- Organizations: [https://developers.pipedrive.com/docs/api/v1/Organizations](https://developers.pipedrive.com/docs/api/v1/Organizations "https://developers.pipedrive.com/docs/api/v1/Organizations")
- Permission Sets: [https://developers.pipedrive.com/docs/api/v1/PermissionSets](https://developers.pipedrive.com/docs/api/v1/PermissionSets "https://developers.pipedrive.com/docs/api/v1/PermissionSets")
- Persons: [https://developers.pipedrive.com/docs/api/v1/Persons](https://developers.pipedrive.com/docs/api/v1/Persons "https://developers.pipedrive.com/docs/api/v1/Persons")
- Pipelines: [https://developers.pipedrive.com/docs/api/v1/Pipelines](https://developers.pipedrive.com/docs/api/v1/Pipelines "https://developers.pipedrive.com/docs/api/v1/Pipelines")
- Products: [https://developers.pipedrive.com/docs/api/v1/Products](https://developers.pipedrive.com/docs/api/v1/Products "https://developers.pipedrive.com/docs/api/v1/Products")
- Roles: [https://developers.pipedrive.com/docs/api/v1/Roles](https://developers.pipedrive.com/docs/api/v1/Roles "https://developers.pipedrive.com/docs/api/v1/Roles")
- Stages: [https://developers.pipedrive.com/docs/api/v1/Stages](https://developers.pipedrive.com/docs/api/v1/Stages "https://developers.pipedrive.com/docs/api/v1/Stages")
- Users: [https://developers.pipedrive.com/docs/api/v1/Users](https://developers.pipedrive.com/docs/api/v1/Users "https://developers.pipedrive.com/docs/api/v1/Users")

| Entity                                                        | Data Type | Supported Operators |
| ------------------------------------------------------------- | --------- | ------------------- |
| Activities, Deals, Notes, Organization, Persons and Products. | Date      | '='                 |
|                                                               | Integer   | '='                 |
|                                                               | String    | '='                 |
|                                                               | Boolean   | '='                 |

## Partitioning queries

In Pipedrive, only one field (due_date) from Activities entity supports field-based partitioning. It is a Date field.

Additional spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`,
`NUM_PARTITIONS` can be provided if you want to utilize concurrency in Spark. With these parameters,
the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by spark
tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition query.
- `LOWER_BOUND`: an inclusive lower bound value of the chosen partition field.

For date, we accept the Spark date format used in Spark SQL queries.
Example of valid values: `"2024-02-06"`.

- `UPPER_BOUND`: an exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: number of partitions.

**Example**

```
pipedrive_read = glueContext.create_dynamic_frame.from_options(
    connection_type="PIPEDRIVE",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "activites",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "due_date"
        "LOWER_BOUND": "2023-09-07T02:03:00.000Z"
        "UPPER_BOUND": "2024-05-07T02:03:00.000Z"
        "NUM_PARTITIONS": "10"
    }
```
