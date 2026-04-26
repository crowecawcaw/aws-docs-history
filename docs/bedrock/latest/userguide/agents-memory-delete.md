# Delete session summaries

To delete session summaries, send a [DeleteAgentMemory](../APIReference/API_agent-runtime_DeleteAgentMemory.md "../APIReference/API_agent-runtime_DeleteAgentMemory.md") request (see link for request and
response formats and field details) with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt").

The following fields are required:

| Field        | Short description                  |
| ------------ | ---------------------------------- |
| agentId      | The identifier of the agent.       |
| agentAliasId | The identifier of the agent alias. |

The following field is optional.

| Field    | Short description                                           |
| -------- | ----------------------------------------------------------- |
| memoryId | The identifier of the memory that has the session summaries |
