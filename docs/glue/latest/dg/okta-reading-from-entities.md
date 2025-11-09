# Reading from Okta entities

**Prerequisites**

- A Okta Object you would like to read from. Refer the supported entities table below to check the available
  entities.

**Supported entities**

| Entity       | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| ------------ | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Applications | Yes             | Yes            | No                | Yes                | No                    |
| Devices      | Yes             | Yes            | No                | Yes                | Yes                   |
| Groups       | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Users        | Yes             | Yes            | Yes               | Yes                | Yes                   |
| User Types   | No              | No             | No                | Yes                | No                    |

**Example**

```
okta_read = glueContext.create_dynamic_frame.from_options(
    connection_type="Okta",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "applications",
        "API_VERSION": "v1"
    }
```

**Okta entity and field details**

Entities list:

- Application: [https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Application/](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Application/ "https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Application/")
- Device: [https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Device/](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Device/ "https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Device/")
- Group: [https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/ "https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/")
- User: [https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/ "https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/")
- User Type: [https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/ "https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/")

**Partitioning queries**

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
okta_read = glueContext.create_dynamic_frame.from_options(
    connection_type="okta",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "lastUpdated",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "lastMembershipUpdated"
        "LOWER_BOUND": "2022-08-10T10:28:46.000Z"
        "UPPER_BOUND": "2024-08-10T10:28:46.000Z"
        "NUM_PARTITIONS": "10"
    }
```
