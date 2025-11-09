# Reading from Snapchat Ads entities

**Prerequisites**

- A Snapchat Ads Object you would like to read from. Refer the supported entities table below to check the available
  entities.

**Supported entities**

| Entity              | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| ------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Organization        | No              | No             | No                | Yes                | No                    |
| Ad Account          | No              | No             | No                | Yes                | No                    |
| Creative            | No              | No             | No                | Yes                | No                    |
| Media               | No              | No             | No                | Yes                | No                    |
| Campaign            | Yes             | No             | No                | Yes                | No                    |
| Ad Under Ad Account | Yes             | No             | No                | Yes                | No                    |
| Ad Under Campaign   | No              | No             | No                | Yes                | No                    |
| Ad Squad            | Yes             | No             | No                | Yes                | No                    |
| Segment             | No              | No             | No                | Yes                | No                    |

**Example**

```
snapchatads_read = glueContext.create_dynamic_frame.from_options(
    connection_type="snapchatAds",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "organization",
        "API_VERSION": "v1"
    }
)
```

**Snapchat Ads entity and field details**

Snapchat Ads dynamically loads available fields under selected entity. Depending on the data type of the field,
it supports following filter operators.

| Field Data Type | Supported Filter Operators |
| --------------- | -------------------------- |
| Boolean         | =                          |

**Partitioning queries**

- Field-based partitioning: Not supported.
- Record-based partitioning: Not supported.
