# Reading from Dynatrace entities

**Prerequisite**

A Dynatrace object you would like to read from. You will need the object name such as "problem".

**Supported entities for source**:

| Entity  | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Problem | Yes             | Yes            | Yes               | Yes                | No                    |

**Example**:

```
Dynatrace_read = glueContext.create_dynamic_frame.from_options(
    connection_type="Dynatrace",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "problem",
        "API_VERSION": "v2",
        "INSTANCE_URL": "https://[instanceName].live.dynatrace.com"
    }
```

**Dynatrace entity and field details**:

Dynatrace provides endpoints to fetch metadata dynamically for supported entities. Accordingly, operator support is captured at the datatype level.

| Entity             | Field            | Data type          | Supported operators |
| ------------------ | ---------------- | ------------------ | ------------------- |
| Problem            | affectedEntities | List               | EQUAL\_TO           |
| displayId          | String           | EQUAL\_TO          |
| endTime            | DateTime         |                    |
| entityTags         | List             |                    |
| evidenceDetails    | Struct           |                    |
| impactAnalysis     | Struct           |                    |
| impactLevel        | String           | EQUAL\_TO          |
| impactedEntities   | List             | EQUAL\_TO          |
| linkedProblemInfo  | Struct           |                    |
| managementZones    | List             | EQUAL\_TO          |
| problemFilters     | List             |                    |
| recentComments     | Struct           |                    |
| rootCauseEntity    | Struct           | EQUAL\_TO          |
| problemId          | String           | EQUAL\_TO          |
| severityLevel      | String           | EQUAL\_TO          |
| startTime          | DateTime         | BETWEEN            |
| status             | String           | EQUAL\_TO          |
| title              | String           |                    |
| from               | DateTime         | EQUAL\_TO, BETWEEN |
| problemFilterIds   | String           | EQUAL\_TO          |
| problemFilterNames | String           | EQUAL\_TO          |
| managementZoneIds  | String           | EQUAL\_TO          |
| text               | String           | EQUAL\_TO          |
| underMaintenance   | Boolean          | EQUAL\_TO          |
| message            | String           |                    |

## Partitioning queries

Dynatrace doesn’t support field based or record based partitioning.
