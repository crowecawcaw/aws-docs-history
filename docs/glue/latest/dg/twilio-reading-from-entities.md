# Reading from Twilio entities

**Prerequisite**

A Twilio object you would like to read from. You will need the object name such as `SMS-Message` or `SMS-CountryPricing`.

**Supported entities for source**:

| Entity                                | Interface | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ------------------------------------- | --------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| SMS-Message                           | REST      | Yes             | Yes            | No                | Yes                | Yes                   |
| SMS-CountryPricing                    | REST      | No              | No             | No                | Yes                | No                    |
| Voice-Call                            | REST      | Yes             | Yes            | No                | Yes                | No                    |
| Voice-Application                     | REST      | Yes             | Yes            | No                | Yes                | No                    |
| Voice-OutgoingCallerID                | REST      | Yes             | Yes            | No                | Yes                | No                    |
| Voice-Queue                           | REST      | Yes             | Yes            | No                | Yes                | No                    |
| Conversations-Conversation            | REST      | Yes             | Yes            | No                | Yes                | No                    |
| Conversations-User                    | REST      | No              | Yes            | No                | Yes                | No                    |
| Conversations-Role                    | REST      | No              | Yes            | No                | Yes                | No                    |
| Conversations-Configuration           | REST      | No              | No             | No                | Yes                | No                    |
| Conversations-AddressConfiguration    | REST      | Yes             | Yes            | No                | Yes                | No                    |
| Conversations-WebhookConfiguration    | REST      | No              | No             | No                | Yes                | No                    |
| Conversations-ParticipantConversation | REST      | No              | No             | No                | Yes                | No                    |
| Conversations-Credential              | REST      | No              | Yes            | No                | Yes                | No                    |
| Conversations-ConversationService     | REST      | No              | Yes            | No                | Yes                | No                    |

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

| Entity                                | Field         | Data type | Supported operators |
| ------------------------------------- | ------------- | --------- | ------------------- |
| SMS-Message                           | account\_sid  | String    | N/A                 |
| api\_version                          | String        | N/A       |
| body                                  | String        | N/A       |
| date\_created                         | Datetime      | N/A       |
| date\_sent                            | Datetime      | >=, <=, = |
| date\_updated                         | Datetime      | N/A       |
| direction                             | String        | N/A       |
| error\_code                           | Integer       | N/A       |
| error\_message                        | String        | N/A       |
| from                                  | Integer       | =         |
| messaging\_service\_sid               | String        | N/A       |
| num\_media                            | String        | N/A       |
| num\_segments                         | String        | N/A       |
| price                                 | String        | N/A       |
| price\_unit                           | Struct        | N/A       |
| sid                                   | Integer       | N/A       |
| status                                | String        | N/A       |
| subresource\_uris                     | Map           | N/A       |
| to                                    | Integer       | =         |
| uri                                   | Datetime      | N/A       |
| SMS-CountryPricing                    | country       | String    | N/A                 |
| iso\_country                          | String        | N/A       |
| url                                   | String        | N/A       |
| outbound\_sms\_prices                 | List          | N/A       |
| inbound\_sms\_prices                  | List          | N/A       |
| price\_unit                           | String        | N/A       |
| Voice-Call                            | account\_sid  | String    | N/A                 |
| annotation                            | String        | N/A       |
| answered\_by                          | String        | N/A       |
| api\_version                          | String        | N/A       |
| caller\_name                          | String        | N/A       |
| date\_created                         | Datetime      | N/A       |
| date\_updated                         | Datetime      | N/A       |
| direction                             | String        | N/A       |
| duration                              | String        | N/A       |
| end\_time                             | Datetime      | >=, <=, = |
| forwarded\_from                       | String        | N/A       |
| from                                  | String        | =         |
| from\_formatted                       | String        | N/A       |
| group\_sid                            | String        | N/A       |
| parent\_call\_sid                     | String        | N/A       |
| phone\_number\_sid                    | String        | N/A       |
| price                                 | String        | N/A       |
| price\_unit                           | String        | N/A       |
| sid                                   | String        | N/A       |
| start\_time                           | Datetime      | >=, <=, = |
| status                                | String        | =         |
| subresource\_uris                     | String        | N/A       |
| to                                    | String        | =         |
| to\_formatted                         | String        | N/A       |
| trunk\_sid                            | String        | N/A       |
| uri                                   | String        | N/A       |
| queue\_time                           | String        | N/A       |
| Voice-Application                     | account\_sid  | String    | N/A                 |
| api\_version                          | String        | N/A       |
| date\_created                         | Datetime      | N/A       |
| date\_updated                         | Datetime      | N/A       |
| friendly\_name                        | String        | =         |
| message\_status\_callback             | String        | N/A       |
| sid                                   | String        | N/A       |
| sms\_fallback\_method                 | String        | N/A       |
| sms\_fallback\_url                    | String        | N/A       |
| sms\_method                           | String        | N/A       |
| sms\_status\_callback                 | String        | N/A       |
| sms\_url                              | String        | N/A       |
| status\_callback                      | String        | N/A       |
| status\_callback\_method              | String        | N/A       |
| uri                                   | String        | N/A       |
| voice\_caller\_id\_lookup             | Boolean       | N/A       |
| voice\_fallback\_method               | String        | N/A       |
| voice\_fallback\_url                  | String        | N/A       |
| voice\_method                         | String        | N/A       |
| voice\_url                            | String        | N/A       |
| public\_application\_connect\_enabled | Boolean       | N/A       |
| Voice-OutgoingCallerID                | sid           | String    | N/A                 |
| date\_created                         | Datetime      | N/A       |
| date\_updated                         | Datetime      | N/A       |
| account\_sid                          | String        | N/A       |
| friendly\_name                        | String        | =         |
| phone\_number                         | String        | =         |
| uri                                   | String        | N/A       |
| Voice-Queue                           | date\_created | Datetime  | N/A                 |
| date\_updated                         | Datetime      | N/A       |
| current\_size                         | Integer       | N/A       |
| friendly\_name                        | String        | N/A       |
| uri                                   | String        | N/A       |
| account\_sid                          | String        | N/A       |
| average\_wait\_time                   | Integer       | N/A       |
| sid                                   | String        | N/A       |
| max\_size                             | Integer       | N/A       |
| Conversations-Conversation            | account\_sid  | String    | N/A                 |
| chat\_service\_sid                    | String        | N/A       |
| messaging\_service\_sid               | String        | N/A       |
| sid                                   | String        | N/A       |
| friendly\_name                        | String        | N/A       |
| unique\_name                          | String        | N/A       |
| attributes                            | String        | N/A       |
| state                                 | String        | =         |
| date\_created                         | Datetime      | N/A       |
| date\_updated                         | Datetime      | N/A       |
| timers                                | Struct        | N/A       |
| url                                   | String        | N/A       |
| links                                 | Struct        | N/A       |
| bindings                              | Struct        | N/A       |
| start\_date                           | Datetime      | =         |
| end\_date                             | Datetime      | =         |
| Timers.DateInactive                   | String        | N/A       |
| Timers.DateClosed                     | String        | N/A       |
| Conversations-User                    | sid           | String    | N/A                 |
| account\_sid                          | String        | N/A       |
| chat\_service\_sid                    | String        | N/A       |
| role\_sid                             | String        | N/A       |
| identity                              | String        | N/A       |
| friendly\_name                        | String        | N/A       |
| attributes                            | String        | N/A       |
| is\_online                            | Boolean       | N/A       |
| is\_notifiable                        | Boolean       | N/A       |
| date\_created                         | Datetime      | N/A       |
| date\_updated                         | Datetime      | N/A       |
| url                                   | String        | N/A       |
| links                                 | Struct        | N/A       |
| Conversations-Role                    | sid           | String    | N/A                 |
| account\_sid                          | String        | N/A       |
| chat\_service\_sid                    | String        | N/A       |
| friendly\_name                        | String        | N/A       |
| type                                  | String        | N/A       |
| permissions                           | String        | N/A       |
| date\_created                         | Datetime      | N/A       |
| date\_updated                         | Datetime      | N/A       |
| url                                   | String        | N/A       |
| Conversations-Configuration           | account\_sid  | Long      | N/A                 |
| default\_chat\_service\_sid           | String        | N/A       |
| default\_messaging\_service\_sid      | String        | N/A       |
| default\_inactive\_timer              | String        | N/A       |
| default\_closed\_timer                | String        | N/A       |
| url                                   | String        | N/A       |
| links                                 | Map           | N/A       |
| Conversations-AddressConfiguration    | sid           | String    | N/A                 |
| account\_sid                          | String        | N/A       |
| type                                  | String        | N/A       |
| address                               | String        | N/A       |
| friendly\_name                        | String        | N/A       |
| auto\_creation                        | Struct        | N/A       |
| date\_created                         | Datetime      | N/A       |
| date\_updated                         | Datetime      | N/A       |
| url                                   | String        | N/A       |
| address\_country                      | String        | N/A       |
| AutoCreation.Enabled                  | Boolean       | N/A       |
| AutoCreation.Type                     | String        | N/A       |
| AutoCreation.ConversationServiceSid   | String        | N/A       |
| AutoCreation.WebhookUrl               | String        | N/A       |
| AutoCreation.WebhookMethod            | String        | N/A       |
| AutoCreation.WebhookFilters           | List          | N/A       |
| AutoCreation.StudioFlowSid            | String        | N/A       |
| AutoCreation.StudioRetryCount         | Integer       | N/A       |
| Conversations-WebhookConfiguration    | account\_sid  | String    | N/A                 |
| method                                | String        | N/A       |
| filters                               | List          | N/A       |
| pre\_webhook\_url                     | String        | N/A       |
| post\_webhook\_url                    | String        | N/A       |
| target                                | String        | N/A       |
| url                                   | String        | N/A       |
| Converations-ParticipantConversation  | account\_sid  | String    | N/A                 |
| chat\_service\_sid                    | String        | N/A       |
| participant\_sid                      | String        | N/A       |
| participant\_user\_sid                | String        | N/A       |
| participant\_identity                 | String        | N/A       |
| participant\_messaging\_binding       | Struct        | N/A       |
| Conversation\_sid                     | String        | N/A       |
| conversation\_unique\_name            | String        | N/A       |
| conversation\_friendly\_name          | String        | N/A       |
| conversation\_attributes              | String        | N/A       |
| conversation\_date\_created           | Datetime      | N/A       |
| conversation\_date\_updated           | Datetime      | N/A       |
| conversation\_created\_by             | String        | N/A       |
| conversation\_state                   | String        | N/A       |
| conversation\_timers                  | Struct        | N/A       |
| links                                 | Map           | N/A       |
| address                               | String        | =         |
| identity                              | String        | =         |
| Conversation-Credentials              | sid           | String    | N/A                 |
| account\_sid                          | String        | N/A       |
| friendly\_name                        | String        | N/A       |
| type                                  | String        | N/A       |
| sandbox                               | String        | N/A       |
| date\_created                         | Datetime      | N/A       |
| dated\_updated                        | Datetime      | N/A       |
| url                                   | String        | N/A       |
| certificate                           | String        | N/A       |
| private\_key                          | String        | N/A       |
| api\_key                              | String        | N/A       |
| secret                                | String        | N/A       |
| Conversations-ConversationService     | sid           | String    | N/A                 |
| account\_sid                          | String        | N/A       |
| friendly\_name                        | String        | N/A       |
| date\_created                         | Datetime      | N/A       |
| date\_updated                         | Datetime      | N/A       |
| url                                   | String        | N/A       |
| links                                 | Map           | N/A       |

## Partitioning queries

**Fields supporting partitioning**:

In Twilio, the DateTime datatype fields support field-based partitioning.

You can provide the additional Spark options `PARTITION_FIELD`,
`LOWER_BOUND`, `UPPER_BOUND`, and
`NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
these parameters, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks
concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the Datetime field, we accept the Spark timestamp format used in Spark SQL queries.

Examples of valid value:

```
"2024-05-01T20:55:02.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

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
