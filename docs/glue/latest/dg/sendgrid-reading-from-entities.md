

# Reading from SendGrid entities
<a name="sendgrid-reading-from-entities"></a>

**Prerequisite**

A SendGrid object you would like to read from. You will need the object name such as `lists`, `singlesends` or `segments`.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Lists | No | Yes | No | Yes | No | 
| Single Sends | Yes | Yes | No | Yes | No | 
| Marketing Campaign Stats-Automations | Yes | Yes | No | Yes | No | 
| Marketing Campaign Stats-Single Sends | Yes | Yes | No | Yes | No | 
| Segments | Yes | No | No | Yes | No | 
| Contacts | Yes | No | No | Yes | No | 
| Category | No | No | No | Yes | No | 
| Stats | Yes | No | No | Yes | No | 
| Unsubscribe Groups | Yes | No | No | Yes | No | 

**Example**:

```
sendgrid_read = glueContext.create_dynamic_frame.from_options(
    connection_type="sendgrid",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "lists",
        "API_VERSION": "v3",
        "INSTANCE_URL": "instanceUrl"
    }
```

**SendGrid entity and field details**:

Entities with static metadata:



- **Lists**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** contact\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** \_metadata / **Data type:** Struct / **Supported operators:** N/A

- **Single Sends**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** abtest / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** categories / **Data type:** List / **Supported operators:** EQUAL\_TO
  - **Field:** send\_at / **Data type:** String / **Supported operators:** N/A
  - **Field:** is\_abtest / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** updated\_at / **Data type:** String / **Supported operators:** N/A
  - **Field:** created\_at / **Data type:** String / **Supported operators:** N/A
  - **Field:** channels / **Data type:** List / **Supported operators:** N/A

- **Marketing Campaign Stats-Automations**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** aggregation / **Data type:** String / **Supported operators:** N/A
  - **Field:** step\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** stats / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** automation\_ids / **Data type:** List / **Supported operators:** EQUAL\_TO

- **Marketing Campaign Stats-Singlesends**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** ab\_variation / **Data type:** String / **Supported operators:** N/A
  - **Field:** ab\_phase / **Data type:** String / **Supported operators:** N/A
  - **Field:** aggregation / **Data type:** String / **Supported operators:** N/A
  - **Field:** stats / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** singlesend\_ids / **Data type:** List / **Supported operators:** EQUAL\_TO

- **Segments**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** query\_version / **Data type:** String / **Supported operators:** N/A
  - **Field:** contacts\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** sample\_updated\_at / **Data type:** String / **Supported operators:** N/A
  - **Field:** next\_sample\_update / **Data type:** String / **Supported operators:** N/A
  - **Field:** created\_at / **Data type:** String / **Supported operators:** N/A
  - **Field:** updated\_at / **Data type:** String / **Supported operators:** N/A
  - **Field:** parent\_list\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** status / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** parent\_list\_ids / **Data type:** String / **Supported operators:** EQUAL\_TO
  - **Field:** no\_parent\_list\_id / **Data type:** Boolean / **Supported operators:** EQUAL\_TO

- **Contacts**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** first\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** last\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** unique\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** email / **Data type:** String / **Supported operators:** N/A
  - **Field:** alternate\_emails / **Data type:** List / **Supported operators:** N/A
  - **Field:** address\_line\_1 / **Data type:** String / **Supported operators:** N/A
  - **Field:** address\_line\_2 / **Data type:** String / **Supported operators:** N/A
  - **Field:** city / **Data type:** String / **Supported operators:** N/A
  - **Field:** state\_province\_region / **Data type:** String / **Supported operators:** N/A
  - **Field:** country / **Data type:** String / **Supported operators:** N/A
  - **Field:** postal\_code / **Data type:** String / **Supported operators:** N/A
  - **Field:** phone\_number / **Data type:** String / **Supported operators:** N/A
  - **Field:** whatsapp / **Data type:** String / **Supported operators:** N/A
  - **Field:** line / **Data type:** String / **Supported operators:** N/A
  - **Field:** facebook / **Data type:** String / **Supported operators:** N/A
  - **Field:** list\_ids / **Data type:** List / **Supported operators:** N/A
  - **Field:** custom\_fields / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** created\_at / **Data type:** String / **Supported operators:** N/A
  - **Field:** updated\_at / **Data type:** String / **Supported operators:** N/A
  - **Field:** \_metadata / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** event\_timestamp / **Data type:** DateTime / **Supported operators:** BETWEEN

- **Category**
  - **Field:** categories
  - **Data type:** List
  - **Supported operators:** N/A

- **Stats**
  - **Field:** date / **Data type:** String / **Supported operators:** N/A
  - **Field:** stats / **Data type:** List / **Supported operators:** N/A
  - **Field:** start\_date / **Data type:** DateTime / **Supported operators:** EQUAL\_TO, BETWEEN
  - **Field:** aggregated\_by / **Data type:** String / **Supported operators:** EQUAL\_TO

- **Unsubscribe Groups**
  - **Field:** id / **Data type:** Integer / **Supported operators:** EQUAL\_TO
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** last\_email\_sent\_at / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** is\_default / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** unsubscribes / **Data type:** Integer / **Supported operators:** N/A



**Note**  
Struct and List data types are converted to String data type, and DateTime data type is converted to Timestamp in the response of the connectors.

## Partitioning queries
<a name="sendgrid-reading-partitioning-queries"></a>

SendGrid doesn't support filter-based partitioning or record-based partitioning.