

# Reading from Zoom Meetings entities
<a name="zoom-meetings-reading-from-entities"></a>

**Prerequisite**

A Zoom Meetings object you would like to read from. You will need the object namem such as `Group` or `Zoom Rooms`.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Zoom Rooms | No | Yes | No | Yes | No | 
| Group | No | No | No | Yes | No | 
| Group Member | Yes | Yes | No | Yes | No | 
| Group Admin | No | Yes | No | Yes | No | 
| Report (daily) | Yes | No | No | Yes | No | 
| Roles | No | No | No | Yes | No | 
| Users | Yes | Yes | No | Yes | No | 

**Example**:

```
zoom_read = glueContext.create_dynamic_frame.from_options(
    connection_type="zoom",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "organization",
        "API_VERSION": "v2"
    }
)
```

**Zoom Meetings entity and field details**:

Zoom Meetings dynamically loads the available fields under the selected entity. Depending on the data type of the field, it supports the following filter operators.



- **Zoom Room**
  - **Field:** status / **Data type:** String / **Supported operators:** =
  - **Field:** type / **Data type:** String / **Supported operators:** =
  - **Field:** unassigned\_rooms / **Data type:** Boolean / **Supported operators:** =
  - **Field:** location\_id / **Data type:** String / **Supported operators:** =
  - **Field:** room\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** activation\_code / **Data type:** String / **Supported operators:** N/A
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** tag\_ids / **Data type:** String / **Supported operators:** N/A
  - **Field:** query\_name / **Data type:** String / **Supported operators:** N/A

- **Daily Report**
  - **Field:** month / **Data type:** Date / **Supported operators:** =
  - **Field:** date / **Data type:** Date / **Supported operators:** N/A
  - **Field:** meeting\_minutes / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** meetings / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** new\_users / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** participants / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** group\_id / **Data type:** String / **Supported operators:** N/A

- **User**
  - **Field:** created\_at / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** dept / **Data type:** String / **Supported operators:** N/A
  - **Field:** email / **Data type:** String / **Supported operators:** N/A
  - **Field:** employee\_unique\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** first\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** group\_ids / **Data type:** List / **Supported operators:** N/A
  - **Field:** host\_key / **Data type:** String / **Supported operators:** N/A
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** im\_group\_ids / **Data type:** String / **Supported operators:** N/A
  - **Field:** last\_client\_version / **Data type:** String / **Supported operators:** N/A
  - **Field:** last\_login\_time / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** last\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** plan\_united\_type / **Data type:** String / **Supported operators:** N/A
  - **Field:** custom\_attributes / **Data type:** List / **Supported operators:** N/A
  - **Field:** pmi / **Data type:** BigInteger / **Supported operators:** N/A
  - **Field:** role\_id / **Data type:** String / **Supported operators:** =
  - **Field:** status / **Data type:** String / **Supported operators:** =
  - **Field:** timezone / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** verified / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** user\_created\_at / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** display\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** phone\_number / **Data type:** String / **Supported operators:** N/A
  - **Field:** language / **Data type:** String / **Supported operators:** N/A
  - **Field:** license / **Data type:** String / **Supported operators:** =

- **Group**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** total\_members / **Data type:** Integer / **Supported operators:** N/A

- **Group Member**
  - **Field:** email / **Data type:** String / **Supported operators:** N/A
  - **Field:** first\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** last\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** primary\_group / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** member\_id / **Data type:** String / **Supported operators:** N/A

- **Group Admin**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** email / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A

- **role**
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** total\_members / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** =



## Partitioning queries
<a name="zoom-meetings-reading-partitioning-queries"></a>

Zoom Meetings doesn't support filter-based partitioning or record-based partitioning.