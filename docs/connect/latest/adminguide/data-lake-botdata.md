# Bot analytics data in the Amazon Connect analytics data

lake

This topic details the content in the Amazon Connect data lake bot tables. The
tables list the column, type, and description of the content.

There are two ways to access the analytics data lake and configure data to be
shared:

- [Option 1: Use the Amazon Connect
  console](access-datalake.md#option1-configure-data-to-be-shared "access-datalake.md#option1-configure-data-to-be-shared")
- [Option 2: Use CLI or
  CloudShell](access-datalake.md#option2-configure-data-to-be-shared "access-datalake.md#option2-configure-data-to-be-shared")
  If you are unable to access the scheduling tables by using Option 1, try using
  Option 2.

###### Contents

- [Bot conversations](#data-lake-bot-conversations "#data-lake-bot-conversations")
- [Bot intents](#data-lake-bot-intents "#data-lake-bot-intents")
- [Bot slots](#data-lake-bot-slots "#data-lake-bot-slots")

## Bot conversations

Table name: bot_conversations

Composite primary key: {instance_id, event_id}

| Column                                | Type      | Description                                                                                                                                                                                     |
| ------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- |
| event_id                              | String    | This is the primary key of the table. This will be a hash of<br>originating request identifier and session identifier.                                                                          |
| bot_originating_request_id            | String    | A unique identifier for a specific bot request.                                                                                                                                                 |
| bot_session_id                        | String    | The identifier of the user session that is having the<br>conversation.                                                                                                                          |
| aws_account_id                        | String    | The identifier of the AWS account that owns the<br>contact.                                                                                                                                     |
| instance_arn                          | String    | The ARN of the Amazon Connect instance.                                                                                                                                                         |
| instance_id                           | String    | The identifier of the Amazon Connect instance.                                                                                                                                                  |
| invoking_resource_type                | String    | Can be flow or module.                                                                                                                                                                          |
| flow_resource_id                      | String    | Flow identifier.                                                                                                                                                                                |
| module_resource_id                    | String    | Module identifier.                                                                                                                                                                              |
| invoking_resource_start_timestamp     | Timestamp | Time at which flow started.                                                                                                                                                                     |
| parent_flow_resource_id               | String    | Flow Id from which the module was invoked from. This field<br>will only be populated for modules.                                                                                               |
| contact_id                            | String    | The identifier of the contact.                                                                                                                                                                  |
| flow_action_id                        | String    | Identifier for action that was executed. An Action is a<br>single step of a flow's run.                                                                                                         |
| invoking_resource_published_timestamp | Timestamp | "Creation" or "revision" date of the flow itself.                                                                                                                                               |
| flow_type                             | String    | Amazon Connect includes a set of nine flow types. For more<br>information, see [Choose a flow type](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types").     |
| channel                               | String    | The method used to contact your contact center: VOICE, CHAT,<br>TASK.                                                                                                                           |
| sub_type                              | String    | This subtype for the contact. For example, connect:Guide or<br>connect:SMS.                                                                                                                     |
| initiation_method                     | String    | Indicates how the contact was initiated.                                                                                                                                                        |
| flow_language_version                 | String    | Flow language version.                                                                                                                                                                          |
| invoking_resource_version             | String    | Version of the contact flow used.                                                                                                                                                               |
| bot_id                                | String    | The identifier of the bot.                                                                                                                                                                      |
| bot_alias_id                          | String    | The alias identifier of the bot that the session was held<br>with.                                                                                                                              |
| bot_version                           | String    | The version of the bot that the session was held<br>with.                                                                                                                                       |
| bot_locale                            | String    | Language configuration of the bot.                                                                                                                                                              |
| bot_conversation_start_timestamp      | Timestamp | The Timestamp marking the start of the conversation with the<br>bot.                                                                                                                            |
| bot_conversation_end_timestamp        | Timestamp | The Timestamp marking the end of the conversation with the<br>bot.                                                                                                                              |
| bot_conversation_outcome              | String    | The final state of the conversation. Values: Success                                                                                                                                            | <br>Failure | Dropped |
| bot_number_of_conversation_turns      | Number    | The number of turns that the session took.                                                                                                                                                      |
| data_lake_last_processed_timestamp    | Timestamp | Timestamp, which shows the last time the data lake processed<br>the record. This can include transformation and backfill. This<br>field cannot be used to determine reliably data<br>freshness. |

## Bot intents

Table name: bot_intents

Composite primary key: {instance_id, event_id}

| Column                                | Type      | Description                                                                                                                                                                                                   |
| ------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| event_id                              | String    | This is the primary key of the table. This will be a hash of<br>originating request identifier, session identifier, intent name,<br>and intent level.                                                         |
| bot_originating_request_id            | String    | A unique identifier for a specific bot request.                                                                                                                                                               |
| bot_session_id                        | String    | The identifier of the user session that is having the<br>conversation.                                                                                                                                        |
| account_id                            | String    | The identifier of the AWS account that owns the<br>contact.                                                                                                                                                   |
| instance_arn                          | String    | The ARN of the Amazon Connect instance.                                                                                                                                                                       |
| instance_id                           | String    | The identifier of the Amazon Connect instance.                                                                                                                                                                |
| invoking_resource_type                | String    | Can be flow or module.                                                                                                                                                                                        |
| flow_resource_id                      | String    | The flow identifier.                                                                                                                                                                                          |
| module_resource_id                    | String    | The module identifier.                                                                                                                                                                                        |
| invoking_resource_start_timestamp     | Timestamp | The time when the flow started.                                                                                                                                                                               |
| parent_flow_resource_id               | String    | The flow identifier where the module was invoked. This field<br>is only be populated for modules.                                                                                                             |
| contact_id                            | String    | The identifier of the contact.                                                                                                                                                                                |
| action_id                             | String    | The identifier for action that was executed. An Action is a<br>single step of a flow's run.                                                                                                                   |
| invoking_resource_published_timestamp | Timestamp | The "creation" or "revision" date of the flow itself.                                                                                                                                                         |
| flow_type                             | String    | The type of flow. Amazon Connect includes a set of nine flow types.<br>For more information, see [Choose a flow type](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types"). |
| channel                               | String    | The method used to contact your contact center: VOICE, CHAT,<br>TASK.                                                                                                                                         |
| sub_type                              | String    | The subtype for the contact. For example, connect:Guide or<br>connect:SMS.                                                                                                                                    |
| initiation_method                     | String    | How the contact was initiated.                                                                                                                                                                                |
| flow_language_version                 | String    | The flow language version.                                                                                                                                                                                    |
| invoking_resource_version             | String    | Version of the contact flow used.                                                                                                                                                                             |
| bot_id                                | String    | The identifier of the bot.                                                                                                                                                                                    |
| bot_alias_id                          | String    | The alias identifier of the bot that the session was held.<br>with                                                                                                                                            |
| bot_version                           | String    | The version of the bot that the session was held<br>with.                                                                                                                                                     |
| bot_locale                            | String    | The language configuration of the bot.                                                                                                                                                                        |
| bot_conversation_start_timestamp      | Timestamp | The Timestamp marking the start of the conversation with the<br>bot.                                                                                                                                          |
| bot_conversation_end_timestamp        | Timestamp | The Timestamp marking the end of the conversation with the<br>bot.                                                                                                                                            |
| bot_intent_name                       | String    | The name of the intent.                                                                                                                                                                                       |
| bot_intent_level                      | Number    | The number of intents up to and including the requested<br>path.                                                                                                                                              |
| bot_intent_outcome                    | String    | The end state of the intent. Value of Success, Failed,<br>Switched, or Dropped.                                                                                                                               |
| data_lake_last_processed_timestamp    | Timestamp | The Timestamp, which shows the last time the data lake<br>processed the record. This can include transformation and<br>backfill. This field cannot be used to determine reliably data<br>freshness.           |

## Bot slots

Table name: bot_slots

Composite primary key: {instance_id, event_id}

| Column                                | Type      | Description                                                                                                                                                                                     |
| ------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| event_id                              | String    | This is the primary key of the table. This will be a hash of<br>originating request identifier, session identifier, intent name,<br>intent level, slot name, and slot level.                    |
| bot_originating_request_id            | String    | A unique identifier for a specific bot request                                                                                                                                                  |
| bot_session_id                        | String    | The identifier of the user session that is having the<br>conversation.                                                                                                                          |
| account_id                            | String    | The identifier of the AWS account that owns the<br>contact.                                                                                                                                     |
| instance_arn                          | String    | The ARN of the Amazon Connect instance.                                                                                                                                                         |
| instance_id                           | String    | The identifier of the Amazon Connect instance.                                                                                                                                                  |
| invoking_resource_type                | String    | Can be flow or module.                                                                                                                                                                          |
| flow_resource_id                      | String    | Flow identifier.                                                                                                                                                                                |
| module_resource_id                    | String    | Module identifier.                                                                                                                                                                              |
| invoking_resource_start_timestamp     | Timestamp | Time at which flow started.                                                                                                                                                                     |
| parent_flow_resource_id               | String    | Flow identifier from which the module was invoked from. This<br>field will only be populated for modules.                                                                                       |
| contact_id                            | String    | The identifier of the contact.                                                                                                                                                                  |
| action_id                             | String    | Identifier for action that was executed. An Action is a<br>single step of a flow's run.                                                                                                         |
| invoking_resource_published_timestamp | Timestamp | "Creation" or "revision" date of the flow itself.                                                                                                                                               |
| flow_type                             | String    | Amazon Connect includes a set of nine flow types. For more<br>information, see [Choose a flow type](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types").     |
| channel                               | String    | The method used to contact your contact center: VOICE, CHAT,<br>TASK.                                                                                                                           |
| sub_type                              | String    | This subtype for the contact. For example, connect:Guide or<br>connect:SMS.                                                                                                                     |
| initiation_method                     | String    | Indicates how the contact was initiated.                                                                                                                                                        |
| flow_language_version                 | String    | Flow language version.                                                                                                                                                                          |
| invoking_resource_version             | String    | Version of the contact flow used.                                                                                                                                                               |
| bot_id                                | String    | The identifier of the bot.                                                                                                                                                                      |
| bot_alias_id                          | String    | The alias identifier of the bot that the session was held<br>with.                                                                                                                              |
| bot_version                           | String    | The version of the bot that the session was held<br>with.                                                                                                                                       |
| bot_locale                            | String    | Language configuration of the bot.                                                                                                                                                              |
| bot_conversation_start_timestamp      | Timestamp | The Timestamp marking the start of the conversation with the<br>bot.                                                                                                                            |
| bot_conversation_end_timestamp        | Timestamp | The Timestamp marking the end of the conversation with the<br>bot.                                                                                                                              |
| bot_intent_name                       | String    | The name of the intent.                                                                                                                                                                         |
| bot_intent_level                      | Number    | The number of intents up to and including the requested<br>path.                                                                                                                                |
| bot_slot_name                         | String    | The name of the slot.                                                                                                                                                                           |
| bot_slot_level                        | Number    | The number of slots up to and including the requested<br>path.                                                                                                                                  |
| bot_slot_outcome                      | String    | The end state of the slot. Values of Success, Failed,<br>Dropped, or Retry.                                                                                                                     |
| bot_slot_retry_count                  | Number    | The number of times the bot tried to elicit a response from<br>the user for the slot.                                                                                                           |
| data_lake_last_processed_timestamp    | Timestamp | Timestamp, which shows the last time the data lake processed<br>the record. This can include transformation and backfill. This<br>field cannot be used to determine reliably data<br>freshness. |
