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

| Entity             | Field            | Data type         | Supported operators |
| ------------------ | ---------------- | ----------------- | ------------------- |
| Problem            | affectedEntities | List              | EQUAL_TO            |
| displayId          | String           | EQUAL_TO          |
| endTime            | DateTime         |                   |
| entityTags         | List             |                   |
| evidenceDetails    | Struct           |                   |
| impactAnalysis     | Struct           |                   |
| impactLevel        | String           | EQUAL_TO          |
| impactedEntities   | List             | EQUAL_TO          |
| linkedProblemInfo  | Struct           |                   |
| managementZones    | List             | EQUAL_TO          |
| problemFilters     | List             |                   |
| recentComments     | Struct           |                   |
| rootCauseEntity    | Struct           | EQUAL_TO          |
| problemId          | String           | EQUAL_TO          |
| severityLevel      | String           | EQUAL_TO          |
| startTime          | DateTime         | BETWEEN           |
| status             | String           | EQUAL_TO          |
| title              | String           |                   |
| from               | DateTime         | EQUAL_TO, BETWEEN |
| problemFilterIds   | String           | EQUAL_TO          |
| problemFilterNames | String           | EQUAL_TO          |
| managementZoneIds  | String           | EQUAL_TO          |
| text               | String           | EQUAL_TO          |
| underMaintenance   | Boolean          | EQUAL_TO          |
| message            | String           |                   |

## Partitioning queries

Dynatrace doesn’t support field based or record based partitioning.
