

# Reading from Twilio entities
<a name="twilio-reading-from-entities"></a>

**Prerequisite**

A Twilio object you would like to read from. You will need the object name such as `SMS-Message` or `SMS-CountryPricing`.

**Supported entities for source**:


| Entity | Interface | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | --- | 
| SMS-Message | REST | Yes | Yes | No | Yes | Yes | 
| SMS-CountryPricing | REST | No | No | No | Yes | No | 
| Voice-Call | REST | Yes | Yes | No | Yes | No | 
| Voice-Application | REST | Yes | Yes | No | Yes | No | 
| Voice-OutgoingCallerID | REST | Yes | Yes | No | Yes | No | 
| Voice-Queue | REST | Yes | Yes | No | Yes | No | 
| Conversations-Conversation | REST | Yes | Yes | No | Yes | No | 
| Conversations-User | REST | No | Yes | No | Yes | No | 
| Conversations-Role | REST | No | Yes | No | Yes | No | 
| Conversations-Configuration | REST | No | No | No | Yes | No | 
| Conversations-AddressConfiguration | REST | Yes | Yes | No | Yes | No | 
| Conversations-WebhookConfiguration | REST | No | No | No | Yes | No | 
| Conversations-ParticipantConversation | REST | No | No | No | Yes | No | 
| Conversations-Credential | REST | No | Yes | No | Yes | No | 
| Conversations-ConversationService | REST | No | Yes | No | Yes | No | 

**Example**:

```
twilio_read = glueContext.create_dynamic_frame.from_options(
    connection_type="twilio",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "sms-message",
        "API_VERSION": "2010-04-01",
        "Edge_Location": "sydney.us1"
    }
```

**Twilio entity and field details**:



- **SMS-Message**
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** api\_version / **Data type:** String / **Supported operators:** N/A
  - **Field:** body / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_sent / **Data type:** Datetime / **Supported operators:** >=, <=, =
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** direction / **Data type:** String / **Supported operators:** N/A
  - **Field:** error\_code / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** error\_message / **Data type:** String / **Supported operators:** N/A
  - **Field:** from / **Data type:** Integer / **Supported operators:** =
  - **Field:** messaging\_service\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** num\_media / **Data type:** String / **Supported operators:** N/A
  - **Field:** num\_segments / **Data type:** String / **Supported operators:** N/A
  - **Field:** price / **Data type:** String / **Supported operators:** N/A
  - **Field:** price\_unit / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** sid / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:** N/A
  - **Field:** subresource\_uris / **Data type:** Map / **Supported operators:** N/A
  - **Field:** to / **Data type:** Integer / **Supported operators:** =
  - **Field:** uri / **Data type:** Datetime / **Supported operators:** N/A

- **SMS-CountryPricing**
  - **Field:** country / **Data type:** String / **Supported operators:** N/A
  - **Field:** iso\_country / **Data type:** String / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** outbound\_sms\_prices / **Data type:** List / **Supported operators:** N/A
  - **Field:** inbound\_sms\_prices / **Data type:** List / **Supported operators:** N/A
  - **Field:** price\_unit / **Data type:** String / **Supported operators:** N/A

- **Voice-Call**
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** annotation / **Data type:** String / **Supported operators:** N/A
  - **Field:** answered\_by / **Data type:** String / **Supported operators:** N/A
  - **Field:** api\_version / **Data type:** String / **Supported operators:** N/A
  - **Field:** caller\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** direction / **Data type:** String / **Supported operators:** N/A
  - **Field:** duration / **Data type:** String / **Supported operators:** N/A
  - **Field:** end\_time / **Data type:** Datetime / **Supported operators:** >=, <=, =
  - **Field:** forwarded\_from / **Data type:** String / **Supported operators:** N/A
  - **Field:** from / **Data type:** String / **Supported operators:** =
  - **Field:** from\_formatted / **Data type:** String / **Supported operators:** N/A
  - **Field:** group\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** parent\_call\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** phone\_number\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** price / **Data type:** String / **Supported operators:** N/A
  - **Field:** price\_unit / **Data type:** String / **Supported operators:** N/A
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** start\_time / **Data type:** Datetime / **Supported operators:** >=, <=, =
  - **Field:** status / **Data type:** String / **Supported operators:** =
  - **Field:** subresource\_uris / **Data type:** String / **Supported operators:** N/A
  - **Field:** to / **Data type:** String / **Supported operators:** =
  - **Field:** to\_formatted / **Data type:** String / **Supported operators:** N/A
  - **Field:** trunk\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** uri / **Data type:** String / **Supported operators:** N/A
  - **Field:** queue\_time / **Data type:** String / **Supported operators:** N/A

- **Voice-Application**
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** api\_version / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** =
  - **Field:** message\_status\_callback / **Data type:** String / **Supported operators:** N/A
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** sms\_fallback\_method / **Data type:** String / **Supported operators:** N/A
  - **Field:** sms\_fallback\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** sms\_method / **Data type:** String / **Supported operators:** N/A
  - **Field:** sms\_status\_callback / **Data type:** String / **Supported operators:** N/A
  - **Field:** sms\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** status\_callback / **Data type:** String / **Supported operators:** N/A
  - **Field:** status\_callback\_method / **Data type:** String / **Supported operators:** N/A
  - **Field:** uri / **Data type:** String / **Supported operators:** N/A
  - **Field:** voice\_caller\_id\_lookup / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** voice\_fallback\_method / **Data type:** String / **Supported operators:** N/A
  - **Field:** voice\_fallback\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** voice\_method / **Data type:** String / **Supported operators:** N/A
  - **Field:** voice\_url / **Data type:** String / **Supported operators:** N/A

- **public\_application\_connect\_enabled**
  - **Field:** Boolean
  - **Data type:** N/A

- **Voice-OutgoingCallerID**
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** =
  - **Field:** phone\_number / **Data type:** String / **Supported operators:** =
  - **Field:** uri / **Data type:** String / **Supported operators:** N/A

- **Voice-Queue**
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** current\_size / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** uri / **Data type:** String / **Supported operators:** N/A
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** average\_wait\_time / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** max\_size / **Data type:** Integer / **Supported operators:** N/A

- **Conversations-Conversation**
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** chat\_service\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** messaging\_service\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** unique\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** attributes / **Data type:** String / **Supported operators:** N/A
  - **Field:** state / **Data type:** String / **Supported operators:** =
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** timers / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** links / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** bindings / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** start\_date / **Data type:** Datetime / **Supported operators:** =
  - **Field:** end\_date / **Data type:** Datetime / **Supported operators:** =
  - **Field:** Timers.DateInactive / **Data type:** String / **Supported operators:** N/A
  - **Field:** Timers.DateClosed / **Data type:** String / **Supported operators:** N/A

- **Conversations-User**
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** chat\_service\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** role\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** identity / **Data type:** String / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** attributes / **Data type:** String / **Supported operators:** N/A
  - **Field:** is\_online / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_notifiable / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** links / **Data type:** Struct / **Supported operators:** N/A

- **Conversations-Role**
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** chat\_service\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** N/A
  - **Field:** permissions / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A

- **Conversations-Configuration**
  - **Field:** account\_sid / **Data type:** Long / **Supported operators:** N/A
  - **Field:** default\_chat\_service\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** default\_messaging\_service\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** default\_inactive\_timer / **Data type:** String / **Supported operators:** N/A
  - **Field:** default\_closed\_timer / **Data type:** String / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** links / **Data type:** Map / **Supported operators:** N/A

- **Conversations-AddressConfiguration**
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** N/A
  - **Field:** address / **Data type:** String / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** auto\_creation / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** address\_country / **Data type:** String / **Supported operators:** N/A
  - **Field:** AutoCreation.Enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** AutoCreation.Type / **Data type:** String / **Supported operators:** N/A
  - **Field:** AutoCreation.ConversationServiceSid / **Data type:** String / **Supported operators:** N/A
  - **Field:** AutoCreation.WebhookUrl / **Data type:** String / **Supported operators:** N/A
  - **Field:** AutoCreation.WebhookMethod / **Data type:** String / **Supported operators:** N/A
  - **Field:** AutoCreation.WebhookFilters / **Data type:** List / **Supported operators:** N/A
  - **Field:** AutoCreation.StudioFlowSid / **Data type:** String / **Supported operators:** N/A
  - **Field:** AutoCreation.StudioRetryCount / **Data type:** Integer / **Supported operators:** N/A

- **Conversations-WebhookConfiguration**
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** method / **Data type:** String / **Supported operators:** N/A
  - **Field:** filters / **Data type:** List / **Supported operators:** N/A
  - **Field:** pre\_webhook\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** post\_webhook\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** target / **Data type:** String / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A

- **Converations-ParticipantConversation**
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** chat\_service\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** participant\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** participant\_user\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** participant\_identity / **Data type:** String / **Supported operators:** N/A
  - **Field:** participant\_messaging\_binding / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** Conversation\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** conversation\_unique\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** conversation\_friendly\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** conversation\_attributes / **Data type:** String / **Supported operators:** N/A
  - **Field:** conversation\_date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** conversation\_date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** conversation\_created\_by / **Data type:** String / **Supported operators:** N/A
  - **Field:** conversation\_state / **Data type:** String / **Supported operators:** N/A
  - **Field:** conversation\_timers / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** links / **Data type:** Map / **Supported operators:** N/A
  - **Field:** address / **Data type:** String / **Supported operators:** =
  - **Field:** identity / **Data type:** String / **Supported operators:** =

- **Conversation-Credentials**
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** N/A
  - **Field:** sandbox / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** dated\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** certificate / **Data type:** String / **Supported operators:** N/A
  - **Field:** private\_key / **Data type:** String / **Supported operators:** N/A
  - **Field:** api\_key / **Data type:** String / **Supported operators:** N/A
  - **Field:** secret / **Data type:** String / **Supported operators:** N/A

- **Conversations-ConversationService**
  - **Field:** sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** account\_sid / **Data type:** String / **Supported operators:** N/A
  - **Field:** friendly\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** date\_created / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** date\_updated / **Data type:** Datetime / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** links / **Data type:** Map / **Supported operators:** N/A



## Partitioning queries
<a name="twilio-reading-partitioning-queries"></a>

**Fields supporting partitioning**:

In Twilio, the DateTime datatype fields support field-based partitioning.

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `PARTITION_FIELD`: the name of the field to be used to partition the query.
+ `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

  For the Datetime field, we accept the Spark timestamp format used in Spark SQL queries.

  Examples of valid value:

  ```
  "2024-05-01T20:55:02.000Z"
  ```
+ `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
+ `NUM_PARTITIONS`: the number of partitions.

Example:

```
twilio_read = glueContext.create_dynamic_frame.from_options(
    connection_type="twilio",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "sms-message",
        "API_VERSION": "2010-04-01",
        "PARTITION_FIELD": "date_sent"
        "LOWER_BOUND": "2024-05-01T20:55:02.000Z"
        "UPPER_BOUND": "2024-06-01T20:55:02.000Z"
        "NUM_PARTITIONS": "10"
    }
```