# Reading from Docusign Monitor entities

**Prerequisite**

A Docusign Monitor object you would like to read from.

**Supported entities for source**:

| Entity          | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| --------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Monitoring Data | Yes             | Yes            | No                | Yes                | No                    |

**Example**:

```
docusignmonitor_read = glueContext.create_dynamic_frame.from_options(
    connection_type="docusign_monitor",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "monitoring-data",
        "API_VERSION": "v2.0"
    }
```

## Docusign Monitor entity and field details

Entities with static metadata:

| Entity                       | Field     | Data type | Supported operators |
| ---------------------------- | --------- | --------- | ------------------- |
| Monitoring Data              | timestamp | DateTime  | N/A                 |
| eventId                      | String    | N/A       |
| application                  | String    | N/A       |
| environment                  | String    | N/A       |
| site                         | String    | N/A       |
| traceToken                   | String    | N/A       |
| organizationId               | String    | N/A       |
| accountId                    | String    | N/A       |
| userId                       | String    | N/A       |
| object                       | String    | N/A       |
| action                       | String    | N/A       |
| property                     | String    | N/A       |
| field                        | String    | N/A       |
| result                       | String    | N/A       |
| IntegratorKey                | String    | N/A       |
| customerVisible              | String    | N/A       |
| version                      | String    | N/A       |
| userAgent                    | String    | N/A       |
| userAgentClientInfo          | Struct    | N/A       |
| ipAddress                    | String    | N/A       |
| ipAddressLocation            | Struct    | N/A       |
| data                         | String    | N/A       |
| source                       | String    | N/A       |
| latitude                     | Double    | N/A       |
| longitude                    | Double    | N/A       |
| city                         | String    | N/A       |
| state                        | String    | N/A       |
| country                      | String    | N/A       |
| usUserMemberOfDomain         | Boolean   | N/A       |
| affectedUserIsMemberOfDomain | Boolean   | N/A       |
| proxyStatus                  | String    | N/A       |
| proxyType                    | String    | N/A       |
| proxyLevel                   | String    | N/A       |
| referencedUserId             | String    | N/A       |
| device                       | String    | N/A       |
| browser                      | String    | N/A       |
| cursor                       | DateTime  | EQUAL_TO  |

**Partitioning queries**

Docusign Monitor doesn’t support either field-based or record-based partitioning.
