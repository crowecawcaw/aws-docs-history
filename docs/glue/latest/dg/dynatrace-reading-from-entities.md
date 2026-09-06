

# Reading from Dynatrace entities
<a name="dynatrace-reading-from-entities"></a>

**Prerequisite**

A Dynatrace object you would like to read from. You will need the object name such as "problem".

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Problem | Yes | Yes | Yes | Yes | No | 

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



- **Problem**
  - **Field:** affectedEntities / **Data type:** List / **Supported operators:** EQUAL\_TO
  - **Field:** displayId / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** endTime / **Data type:** DateTime / **Supported operators:** 
  - **Field:** entityTags / **Data type:** List / **Supported operators:** 
  - **Field:** evidenceDetails / **Data type:** Struct / **Supported operators:** 
  - **Field:** impactAnalysis / **Data type:** Struct / **Supported operators:** 
  - **Field:** impactLevel / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** impactedEntities / **Data type:** List / **Supported operators:** EQUAL\_TO
  - **Field:** linkedProblemInfo / **Data type:** Struct / **Supported operators:** 
  - **Field:** managementZones / **Data type:** List / **Supported operators:** EQUAL\_TO
  - **Field:** problemFilters / **Data type:** List / **Supported operators:** 
  - **Field:** recentComments / **Data type:** Struct / **Supported operators:** 
  - **Field:** rootCauseEntity / **Data type:** Struct / **Supported operators:** EQUAL\_TO
  - **Field:** problemId / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** severityLevel / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** startTime / **Data type:** DateTime / **Supported operators:** BETWEEN
  - **Field:** status / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** title / **Data type:** String / **Supported operators:** 
  - **Field:** from / **Data type:** DateTime / **Supported operators:** EQUAL\_TO, BETWEEN
  - **Field:** problemFilterIds / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** problemFilterNames / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** managementZoneIds / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** text / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** underMaintenance / **Data type:** Boolean / **Supported operators:** EQUAL\_TO
  - **Field:** message / **Data type:** String / **Supported operators:** 



## Partitioning queries
<a name="dynatrace-reading-partitioning-queries"></a>

Dynatrace doesn’t support field based or record based partitioning.