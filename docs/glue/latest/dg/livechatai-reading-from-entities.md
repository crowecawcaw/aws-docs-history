

# Reading from LiveChatAI entities

**Prerequisites**

A LiveChatAI object you want to read from. For the available entities, see the following supported entities table.

The `contacts`, `conversations`, `ai-suggestions`, and `data-sources` entities belong to an agent. Use `{{entity}}/{{agentId}}`, for example `conversations/{{agentId}}`. AWS Glue discovers the available agent IDs for your connection.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| agents | No | Yes | Yes | No | No | 
| ai-suggestions | Yes | Yes | Yes | No | No | 
| contacts | No | Yes | Yes | No | No | 
| conversations | Yes | Yes | Yes | No | No | 
| data-sources | Yes | Yes | Yes | No | No | 

**Example – Reading from a LiveChatAI entity**  
The following example reads from the `agents` entity. Replace {{connectionName}} with the name of your LiveChatAI connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="livechatai",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "agents"
    }
)
```