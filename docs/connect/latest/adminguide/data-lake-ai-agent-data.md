

# AI agent data in the Connect Customer data lake
<a name="data-lake-ai-agent-data"></a>

The following tables contain ai agent data.

**Topics**
+ [AI Agent](#data-lake-ai-agent)
+ [AI Agent Knowledge Base](#data-lake-ai-agent-knowledge-base)
+ [AI Prompt](#data-lake-ai-prompt)
+ [AI Session](#data-lake-ai-session)
+ [AI Tool](#data-lake-ai-tool)

## AI Agent
<a name="data-lake-ai-agent"></a>

**Table name:** `ai_agent`

**Description:** Tracks AI Agent invocation events, including invocation success, latency, conversation turns, and helpfulness ratings for each AI agent interaction within a contact.

**Primary key:** `ai_agent_event_id, instance_id`

**Partition key:** `creation_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Lens, Contact Evaluation Record, Contact Flow Events
+ `ai_session_id` — Joins to AI Session, AI Prompt, AI Tool, AI Agent Knowledge Base
+ `assistant_id` — Joins to AI Session, AI Prompt, AI Tool


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
| instance\_arn | string |  Yes  | The ARN of the Connect instance. | 
| instance\_id | string |  No  | The ID of the Connect instance. | 
| contact\_id | string |  Yes  | The ID of the contact. | 
| ai\_agent\_id | string |  Yes  | The Id of the requested AI Agent. | 
| ai\_agent\_version | string |  Yes  | The version of the requested AI Agent. | 
| ai\_agent\_event\_id | string |  No  | Id of the event. | 
| aws\_account\_id | string |  Yes  | The ID of the AWS account where AI Assistant is used. | 
| assistant\_id | string |  Yes  | The ID of the AI Assistant. | 
| ai\_session\_id | string |  Yes  | The ID of AI-Agent session. | 
| creation\_timestamp | bigint |  Yes  | The timestamp of the event is created in the data lake. | 
| update\_timestamp | bigint |  Yes  | The timestamp of the event is updated in the data lake. | 
| ai\_use\_case | string |  Yes  | The use case of the AI agent. | 
| ai\_agent\_type | string |  Yes  | The type of the requested AI Agent. | 
| ai\_agent\_name | string |  Yes  | The name of the requested AI Agent. | 
| ai\_agent\_arn | string |  Yes  | The Arn of the requested AI Agent. | 
| invocation\_success | bool |  Yes  | A boolean field which indicates whether the invocation of the AI agent has been successful or not. | 
| invocation\_latency\_ms | float |  Yes  | The invocation latency of the AI Agent in the evaluated contact. | 
| conversation\_turns\_in\_response | bigint |  Yes  | The number of conversation turns responded by the requested AI Agent. | 
| response\_helpful | int |  Yes  | The count of AI suggestions rated as helpful with a thumbs-up. | 
| response\_not\_helpful | int |  Yes  | The count of AI suggestions rated as unhelpful with a thumbs-down. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 

## AI Agent Knowledge Base
<a name="data-lake-ai-agent-knowledge-base"></a>

**Table name:** `ai_agent_knowledge_base`

**Description:** Records knowledge base reference events, tracking which knowledge content was retrieved and used during AI Agent interactions.

**Primary key:** `ai_agent_knowledge_base_event_id, instance_id`

**Partition key:** `creation_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Lens
+ `ai_session_id` — Joins to AI Session, AI Agent, AI Prompt, AI Tool
+ `ai_agent_id` — Joins to AI Agent


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
| instance\_arn | string |  Yes  | The ARN of the Connect instance. | 
| aws\_account\_id | string |  Yes  | The identifer of the AWS account that owns Connect AI Assistant. | 
| instance\_id | string |  No  | The ID of the Connect instance. | 
| contact\_id | string |  Yes  | The ID of the specific contact . | 
| knowledge\_content\_id | string |  Yes  | The ID of the referenced knowledge content. | 
| ai\_agent\_type | string |  Yes  | The type of the requested AI Agent. | 
| ai\_agent\_knowledge\_base\_event\_id | string |  No  | The ID of the knowledge base reference event. | 
| assistant\_id | string |  Yes  | The ID of the Amazon Connect AI Assistant. | 
| ai\_session\_id | string |  Yes  | The ID of AI Agent session. | 
| creation\_timestamp | string |  Yes  | The instant the data lake event was created. | 
| update\_timestamp | string |  Yes  | The instant the data lake event was last modified. | 
| ai\_agent\_id | string |  Yes  | The ID of requested AI Agent. | 
| ai\_agent\_name | string |  Yes  | The name of the requested AI Agent. | 
| ai\_agent\_version | string |  Yes  | The version number of the requested AI Agent. | 
| ai\_agent\_arn | string |  Yes  | The ARN of the requested AI Agent. | 
| knowledge\_base\_id | string |  Yes  | The ID of the referenced knowledge base. | 
| knowledge\_base\_name | string |  Yes  | The name of the referenced knowledge base. | 
| knowledge\_content\_reference | string |  Yes  | The title of the referenced knowledge content. | 
| data\_lake\_last\_processed\_timestamp | timestamp |  Yes  | The timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 

## AI Prompt
<a name="data-lake-ai-prompt"></a>

**Table name:** `ai_prompt`

**Description:** Tracks AI Prompt invocation events, including model usage, token counts, latency, and invocation success for each prompt call within an AI session.

**Primary key:** `ai_prompt_event_id, instance_id`

**Partition key:** `creation_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Lens
+ `ai_session_id` — Joins to AI Session, AI Agent, AI Tool
+ `ai_agent_id` — Joins to AI Agent


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
| instance\_arn | string |  Yes  | The ARN of the Connect Customer instance. | 
| aws\_account\_id | string |  Yes  | The customer AWS account ID. | 
| instance\_id | string |  No  | The ID of the Connect Customer instance. | 
| contact\_id | string |  Yes  | The ID of the contact. | 
| ai\_prompt\_id | string |  Yes  | The ID of the requested AI-prompt. | 
| ai\_prompt\_version | string |  Yes  | The version of the requested AI-prompt. | 
| ai\_prompt\_event\_id | string |  No  | The ID of the event. | 
| assistant\_id | string |  Yes  | The identifier of the AI Assistant. | 
| ai\_session\_id | string |  Yes  | The ID of AI-Agent session. | 
| creation\_timestamp | bigint |  Yes  | The timestamp when the event is created in the data lake. | 
| update\_timestamp | bigint |  Yes  | The timestamp when the event is updated in the data lake. | 
| ai\_agent\_type | string |  Yes  | The type of the requested AI Agent. | 
| ai\_agent\_name | string |  Yes  | The name of the requested AI Agent. | 
| ai\_agent\_id | string |  Yes  | The Id of the requested AI Agent. | 
| ai\_agent\_version | string |  Yes  | The version number of the requested AI Agent. | 
| ai\_agent\_arn | string |  Yes  | The Arn of the requested AI Agent. | 
| ai\_prompt\_type | string |  Yes  | The type of the invoked AI Prompt. | 
| ai\_prompt\_name | string |  Yes  | The name of the invoked AI Prompt. | 
| ai\_prompt\_arn | string |  Yes  | The arn of the invoked AI Prompt. | 
| model\_id | string |  Yes  | The name of the llm model associated to the AI Prompt. | 
| invocation\_success | boolean |  Yes  | A boolean field which indicates whether the invocation of the prompt has been successful or not. | 
| invocation\_latency\_ms | float |  Yes  | The invocation latency of the AI Prompt in the evaluated contact. | 
| input\_token | bigint |  Yes  | The input token of the AI Prompt in the evaluated contact. | 
| output\_token | bigint |  Yes  | The output token of the AI Prompt in the evaluated contact. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 

## AI Session
<a name="data-lake-ai-session"></a>

**Table name:** `ai_session`

**Description:** Contains session-level AI metrics, including proactive intent detection, invocation counts, handoff status, and quality scores (goal success, faithfulness, completeness) for each AI session.

**Primary key:** `ai_session_id, instance_id`

**Partition key:** `creation_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Lens
+ `ai_session_id` — Joins to AI Agent, AI Prompt, AI Tool, AI Agent Knowledge Base


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
| instance\_arn | string |  Yes  | The ARN of the Connect Customer instance. | 
| instance\_id | string |  No  | The ID of the Connect Customer instance. | 
| contact\_id | string |  Yes  | The ID of the contact. | 
| ai\_session\_id | string |  No  | The ID of the AI-Agent session. | 
| aws\_account\_id | string |  Yes  | The customer AWS account ID. | 
| assistant\_id | string |  Yes  | The identifier of the agent assist assistant. | 
| creation\_timestamp | bigint |  Yes  | The timestamp when the event is created in the data lake. | 
| update\_timestamp | bigint |  Yes  | The timestamp when the event is updated in the data lake. | 
| proactive\_intents\_detected | bigint |  Yes  | The number of proactive intents (customer queries) detected during the AI session for an Agent Assistance use case. | 
| proactive\_intents\_engaged | bigint |  Yes  | The number of proactive intents (customer queries) engaged in the AI session for an Agent Assistance use case. | 
| proactive\_intents\_answered | bigint |  Yes  | The number of proactive intents (customer queries) answered in the AI session for an Agent Assistance use case. | 
| ai\_agent\_invocation\_count | bigint |  Yes  | The number of AI Agent invocations in the AI session. | 
| ai\_agent\_invocation\_success\_count | bigint |  Yes  | The number of successful AI Agent invocations in the AI session. | 
| is\_handed\_off | boolean |  Yes  | A boolean field which indicates whether the AI agent has handed off to the human agent during the AI session. | 
| avg\_conversation\_turns\_in\_response | float |  Yes  | The average number of conversation turns in response of AI Agent invocation. | 
| goal\_success\_rate | double |  Yes  | A double between 0 and 1 that evaluates whether the Orchestration AI agent successfully resolved the customer issue. | 
| faithfulness\_score | double |  Yes  | A double between 0 and 1 that evaluates if the Orchestration AI agent's response is faithful to the conversational context, including messages and tool call results. | 
| completeness\_score | double |  Yes  | A double between 0 and 1 that evaluates if the Orchestration AI agent's response fully addresses all parts of customer requests. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 

## AI Tool
<a name="data-lake-ai-tool"></a>

**Table name:** `ai_tool`

**Description:** Tracks AI Tool invocation events, including tool selection accuracy, parameter accuracy, utilization accuracy, and invocation latency for each tool call within an AI session.

**Primary key:** `ai_tool_event_id, instance_id`

**Partition key:** `creation_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Lens
+ `ai_session_id` — Joins to AI Session, AI Agent, AI Prompt
+ `ai_agent_id` — Joins to AI Agent


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
| instance\_arn | string |  Yes  | The ARN of the Connect instance. | 
| aws\_account\_id | string |  Yes  | The identifier of the AWS account that owns Connect AI Assistant. | 
| instance\_id | string |  No  | The ID of the Connect instance. | 
| contact\_id | string |  Yes  | The ID of the contact . | 
| ai\_agent\_id | string |  Yes  | The ID of requested AI Agent. | 
| ai\_tool\_id | string |  Yes  | The ID of requested AI tool. | 
| ai\_tool\_event\_id | string |  No  | The ID of the AI Tool invocation event. | 
| assistant\_id | string |  Yes  | The ID of the Connect Customer AI Assistant. | 
| ai\_session\_id | string |  Yes  | The ID of AI Agent session. | 
| creation\_timestamp | bigint |  Yes  | The instant the data lake event was created. | 
| update\_timestamp | bigint |  Yes  | The instant the data lake event was last modified. | 
| ai\_agent\_type | string |  Yes  | The type of the requested AI Agent. | 
| ai\_agent\_name | string |  Yes  | The name of the requested AI Agent. | 
| ai\_agent\_version | string |  Yes  | The version number of the requested AI Agent. | 
| ai\_agent\_arn | string |  Yes  | The ARN of the requested AI Agent. | 
| ai\_tool\_type | string |  Yes  | The type of the invoked AI tool. | 
| ai\_tool\_name | string |  Yes  | The name of the invoked AI tool. | 
| ai\_tool\_arn | string |  Yes  | The ARN of the invoked AI tool. | 
| invocation\_success | boolean |  Yes  | A boolean field which indicates whether the invocation of the tool has been successful or not. | 
| invocation\_latency\_ms | float |  Yes  | The invocation latency for AI tool calling. | 
| ai\_tool\_parameter\_accuracy | double |  Yes  | A double between 0 and 1 that evaluates whether the AI agent provided the correct tool parameters, where 1 indicates correct tool parameters. | 
| ai\_tool\_selection\_accuracy | double |  Yes  | A double between 0 and 1 that evaluates whether the AI agent selected the correct tool, where 1 indicates correct tool selection. | 
| ai\_tool\_utilization\_accuracy | double |  Yes  | A double between 0 and 1 that evaluates whether the AI agent correctly utilized the tool, where 1 indicates perfect use. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 