# Configure an inline agent at runtime

You can configure and invoke an inline Amazon Bedrock agent dynamically at runtime using [InvokeInlineAgent](../APIReference/API_agent-runtime_InvokeInlineAgent.md "../APIReference/API_agent-runtime_InvokeInlineAgent.md") API. Using an inline agent provides you with flexibility
to specify your agent capabilities like foundation models, instructions, action groups,
guardrails, and knowledge bases at the same time you invoke your agent. You do not need
to pre-define agent capabilities before you can use it.

The following are some of the use cases where using inline agents can help by providing you the flexibility to configure your agent at invocation time.

- Conduct rapid experimentation by trying out various agent features with different configurations and dynamically updating tools available
  to your agent without creating separate agents.
- Dynamically invoke an agent to perform specific tasks without creating new agent versions or preparing the agent.
- Run simple queries or use code interpreter for simple tasks by creating and
  invoking the agent at runtime.
- Create multiple agents in a [multi-agent collaboration](agents-multi-agent-collaboration.md "agents-multi-agent-collaboration.md") setup to work together on a task or a conversation.

To use multi-agent collaboration, you can create your agents in the following
combinations using inline agents APIs.

| Agent types | Supervisor  | Collaborator |
| ----------- | ----------- | ------------ |
| Inline      | Inline      |
| Inline      | Traditional |

**Supported models and Regions**

You can use any foundation model supported by Amazon Bedrock Agents to configure your inline agent
and can invoke your inline agent in any of the Regions where Amazon Bedrock Agents are supported.
For more information about the models and Regions supported by Amazon Bedrock Agents, see the
following:

- [Supported Regions for Amazon Bedrock Agents](agents-supported.md "agents-supported.md")
- [Model support by feature](models-features.md "models-features.md")
  With inline agents you can switch between models. We recommend that you switch between
  the models that belong to the same family. Switching between models that belong to
  different families might result in inconsistent behaviors and might cause failures.

Configuring and invoking an inline agent is currently not supported in the Amazon Bedrock console.

## Guidelines for using advanced prompt templates for inline agents

- **Base prompt templates** — By default, Amazon Bedrock will use the default base prompt template for your inline agent and the
  prompts can be changed in the background at any time. This might make the responses
  inconsistent. If you want consistent responses to your queries, customize your inline
  agent's behavior by overriding the logic in the default base prompt template with your
  own configurations. For more information, see [Advanced prompt
  templates](advanced-prompts-templates.md "advanced-prompts-templates.md").
- **Encryption** — Use `customer managed key` to encrypt the session details at rest/storage.
  If a session is started with a customer managed key, it will be required for all future requests made for the same session.
  using a different customer managed key for the same sessions will result in an exception.
- **Session sharing** — Going forward
  all sessions are account level instead of role level. You can isolate
  sessions at the agent level by specifying a unique value for `agentName`.
- **Inline sessions state** — The attributes inside of `InlineSessionState` persists through the session.
  Use the attributes to provide additional context for your model and for [few-shot prompting](what-is-a-prompt.md#few-shot-prompting-vs-zero-shot-prompting "what-is-a-prompt.md#few-shot-prompting-vs-zero-shot-prompting").
