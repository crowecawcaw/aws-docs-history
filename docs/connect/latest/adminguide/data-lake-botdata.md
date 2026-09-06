

# Bot analytics data in the Connect Customer analytics data lake
<a name="data-lake-botdata"></a>

This topic details the content in the Connect Customer data lake bot tables. The tables list the column, type, and description of the content.

There are two ways to access the analytics data lake and configure data to be shared: 
+ [Option 1: Use the Connect Customer console](access-datalake.md#option1-configure-data-to-be-shared)
+ [Option 2: Use CLI or CloudShell](access-datalake.md#option2-configure-data-to-be-shared)

If you are unable to access the scheduling tables by using Option 1, try using Option 2.

**Topics**
+ [Bot conversations](#data-lake-bot-conversations)
+ [Bot intents](#data-lake-bot-intents)
+ [Bot slots](#data-lake-bot-slots)

## Bot conversations
<a name="data-lake-bot-conversations"></a>

**Table name:** `bot_conversations`

**Description:** Records bot conversation sessions including conversation outcomes, turn counts, and associated flow and contact context for Lex bot interactions.

**Primary key:** `instance_id, event_id`

**Partition key:** `bot_conversation_start_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record
+ `flow_resource_id` — Joins to Contact Flow Events
+ `bot_originating_request_id`, `bot_session_id` — Joins to bot\_intents


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| event\_id | String |  No  | This is the primary key of the table. This will be a hash of originating request identifier and session identifier. | 
| bot\_originating\_request\_id | String |  Yes  | A unique identifier for a specific bot request. | 
| bot\_session\_id | String |  Yes  | The identifier of the user session that is having the conversation. | 
| aws\_account\_id | String |  Yes  | The identifier of the AWS account that owns the contact. | 
| instance\_arn | String |  Yes  | The ARN of the Connect Customer instance. | 
| instance\_id | String |  No  | The identifier of the Connect Customer instance. | 
| invoking\_resource\_type | String |  Yes  | Can be flow or module. | 
| flow\_resource\_id | String |  Yes  | Flow identifier. | 
| module\_resource\_id | String |  Yes  | Module identifier. | 
| invoking\_resource\_start\_timestamp | Timestamp |  Yes  | Time at which flow started. | 
| parent\_flow\_resource\_id | String |  Yes  | Flow Id from which the module was invoked from. This field will only be populated for modules. | 
| contact\_id | String |  Yes  | The identifier of the contact. | 
| flow\_action\_id | String |  Yes  | Identifier for action that was executed. An Action is a single step of a flow's run. | 
| invoking\_resource\_published\_timestamp | Timestamp |  Yes  | "Creation" or "revision" date of the flow itself. | 
| flow\_type | String |  Yes  | Connect Customer includes a set of nine flow types. For more information, see [Choose a flow type](create-contact-flow.md#contact-flow-types).  | 
| channel | String |  Yes  | The method used to contact your contact center: VOICE, CHAT, TASK. | 
| sub\_type | String |  Yes  | This subtype for the contact. For example, connect:Guide or connect:SMS. | 
| initiation\_method | String |  Yes  | Indicates how the contact was initiated.  | 
| flow\_language\_version | String |  Yes  | Flow language version. | 
| invoking\_resource\_version | String |  Yes  | Version of the contact flow used. | 
| bot\_id | String |  Yes  | The identifier of the bot. | 
| bot\_alias\_id | String |  Yes  | The alias identifier of the bot that the session was held with. | 
| bot\_version | String |  Yes  | The version of the bot that the session was held with. | 
| bot\_locale | String |  Yes  | Language configuration of the bot. | 
| bot\_conversation\_start\_timestamp | Timestamp |  Yes  | The Timestamp marking the start of the conversation with the bot. | 
| bot\_conversation\_end\_timestamp | Timestamp |  Yes  | The Timestamp marking the end of the conversation with the bot. | 
| bot\_conversation\_outcome | String |  Yes  | The final state of the conversation. Values: Success \| Failure \| Dropped | 
| bot\_number\_of\_conversation\_turns | Number |  Yes  | The number of turns that the session took. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot be used to determine reliably data freshness. | 

## Bot intents
<a name="data-lake-bot-intents"></a>

**Table name:** `bot_intents`

**Description:** Records intent-level outcomes for bot conversations, tracking intent names, levels, and resolution status for each bot interaction turn.

**Primary key:** `instance_id, event_id`

**Partition key:** `bot_conversation_start_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `bot_originating_request_id`, `bot_session_id` — Joins to bot\_conversations
+ `bot_originating_request_id`, `bot_session_id`, `bot_intent_name`, `bot_intent_level` — Joins to bot\_slots
+ `contact_id` — Joins to Contact Record


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| event\_id | String |  No  | This is the primary key of the table. This will be a hash of originating request identifier, session identifier, intent name, and intent level. | 
| bot\_originating\_request\_id | String |  Yes  | A unique identifier for a specific bot request. | 
| bot\_session\_id | String |  Yes  | The identifier of the user session that is having the conversation. | 
| aws\_account\_id | String |  Yes  | The identifier of the AWS account that owns the contact. | 
| instance\_arn | String |  Yes  | The ARN of the Connect Customer instance. | 
| instance\_id | String |  No  | The identifier of the Connect Customer instance. | 
| invoking\_resource\_type | String |  Yes  | Can be flow or module. | 
| flow\_resource\_id | String |  Yes  | The flow identifier. | 
| module\_resource\_id | String |  Yes  | The module identifier. | 
| invoking\_resource\_start\_timestamp | Timestamp |  Yes  | The time when the flow started. | 
| parent\_flow\_resource\_id | String |  Yes  | The flow identifier where the module was invoked. This field is only be populated for modules. | 
| contact\_id | String |  Yes  | The identifier of the contact. | 
| flow\_action\_id | String |  Yes  | The identifier of the flow block (action) that invoked the bot, where an action is a single step of a flow's run. | 
| invoking\_resource\_published\_timestamp | Timestamp |  Yes  | The "creation" or "revision" date of the flow itself. | 
| flow\_type | String |  Yes  | The type of flow. Connect Customer includes a set of nine flow types. For more information, see [Choose a flow type](create-contact-flow.md#contact-flow-types).  | 
| channel | String |  Yes  | The method used to contact your contact center: VOICE, CHAT, TASK. | 
| sub\_type | String |  Yes  | The subtype for the contact. For example, connect:Guide or connect:SMS. | 
| initiation\_method | String |  Yes  | How the contact was initiated.  | 
| flow\_language\_version | String |  Yes  | The flow language version. | 
| invoking\_resource\_version | String |  Yes  | Version of the contact flow used. | 
| bot\_id | String |  Yes  | The identifier of the bot. | 
| bot\_alias\_id | String |  Yes  | The alias identifier of the bot that the session was held. with | 
| bot\_version | String |  Yes  | The version of the bot that the session was held with. | 
| bot\_locale | String |  Yes  | The language configuration of the bot. | 
| bot\_conversation\_start\_timestamp | Timestamp |  Yes  | The Timestamp marking the start of the conversation with the bot. | 
| bot\_conversation\_end\_timestamp | Timestamp |  Yes  | The Timestamp marking the end of the conversation with the bot. | 
| bot\_intent\_name | String |  Yes  | The name of the intent. | 
| bot\_intent\_level | Number |  Yes  | The number of intents up to and including the requested path. | 
| bot\_intent\_outcome | String |  Yes  | The end state of the intent. Value of Success, Failed, Switched, or Dropped. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot be used to determine reliably data freshness. | 

## Bot slots
<a name="data-lake-bot-slots"></a>

**Table name:** `bot_slots`

**Description:** Records slot-level outcomes for bot intent fulfillment, tracking slot resolution status and retry counts for each slot within an intent.

**Primary key:** `instance_id, event_id`

**Partition key:** `bot_conversation_start_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `bot_originating_request_id`, `bot_session_id`, `bot_intent_name`, `bot_intent_level` — Joins to bot\_intents
+ `bot_originating_request_id`, `bot_session_id` — Joins to bot\_conversations
+ `contact_id` — Joins to Contact Record


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| event\_id | String |  No  | This is the primary key of the table. This will be a hash of originating request identifier, session identifier, intent name, intent level, slot name, and slot level. | 
| bot\_originating\_request\_id | String |  Yes  | A unique identifier for a specific bot request | 
| bot\_session\_id | String |  Yes  | The identifier of the user session that is having the conversation. | 
| aws\_account\_id | String |  Yes  | The identifier of the AWS account that owns the contact. | 
| instance\_arn | String |  Yes  | The ARN of the Connect Customer instance. | 
| instance\_id | String |  No  | The identifier of the Connect Customer instance. | 
| invoking\_resource\_type | String |  Yes  | Can be flow or module. | 
| flow\_resource\_id | String |  Yes  | Flow identifier. | 
| module\_resource\_id | String |  Yes  | Module identifier. | 
| invoking\_resource\_start\_timestamp | Timestamp |  Yes  | Time at which flow started. | 
| parent\_flow\_resource\_id | String |  Yes  | Flow identifier from which the module was invoked from. This field will only be populated for modules. | 
| contact\_id | String |  Yes  | The identifier of the contact. | 
| flow\_action\_id | String |  Yes  | The identifier of the flow block (action) that invoked the bot, where an action is a single step of a flow's run. | 
| invoking\_resource\_published\_timestamp | Timestamp |  Yes  | "Creation" or "revision" date of the flow itself. | 
| flow\_type | String |  Yes  | Connect Customer includes a set of nine flow types. For more information, see [Choose a flow type](create-contact-flow.md#contact-flow-types).  | 
| channel | String |  Yes  | The method used to contact your contact center: VOICE, CHAT, TASK. | 
| sub\_type | String |  Yes  | This subtype for the contact. For example, connect:Guide or connect:SMS. | 
| initiation\_method | String |  Yes  | Indicates how the contact was initiated.  | 
| flow\_language\_version | String |  Yes  | Flow language version. | 
| invoking\_resource\_version | String |  Yes  | Version of the contact flow used. | 
| bot\_id | String |  Yes  | The identifier of the bot. | 
| bot\_alias\_id | String |  Yes  | The alias identifier of the bot that the session was held with. | 
| bot\_version | String |  Yes  | The version of the bot that the session was held with. | 
| bot\_locale | String |  Yes  | Language configuration of the bot. | 
| bot\_conversation\_start\_timestamp | Timestamp |  Yes  | The Timestamp marking the start of the conversation with the bot. | 
| bot\_conversation\_end\_timestamp | Timestamp |  Yes  | The Timestamp marking the end of the conversation with the bot. | 
| bot\_intent\_name | String |  Yes  | The name of the intent. | 
| bot\_intent\_level | Number |  Yes  | The number of intents up to and including the requested path. | 
| bot\_slot\_name | String |  Yes  | The name of the slot. | 
| bot\_slot\_level | Number |  Yes  | The number of slots up to and including the requested path. | 
| bot\_slot\_outcome | String |  Yes  | The end state of the slot. Values of Success, Failed, Dropped, or Retry. | 
| bot\_slot\_retry\_count | Number |  Yes  | The number of times the bot tried to elicit a response from the user for the slot. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot be used to determine reliably data freshness. | 