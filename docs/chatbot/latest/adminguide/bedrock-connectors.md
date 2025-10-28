AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Connecting Amazon Bedrock to chat channels

To connect an agent to a chat channel, you must set up a connector. Connector commands are used to manage connectors in your chat channel. Amazon Q Developer in chat applications connectors work by assigning a friendly
name to a specific alias of an Amazon Bedrock agent. Once this configuration is defined, you can start conversing with this agent directly in your chat channel.

###### To connect an agent to your chat channel

1. In your chat channel, enter `@Amazon Q connector`. Amazon Q Developer in chat applications responds with a help message, listing the available connector management commands.
2. Add your Amazon Bedrock agent by running `@Amazon Q connector add `connector_name` arn:aws:bedrock:aws-region:111122223333:agent/`AgentID` `AliasID``.
3. (Optional) View all registered connectors by running `@Amazon Q connector list`.
4. (Optional) Remove connectors by running `@Amazon Q connector delete `connector_name``.

###### Important

- Exposing agents to chat channels: By granting a chat channel or user role permission to invoke an agent, they can perform any action that the agent provides. Take careful consideration when exposing agents to chat channels.
- Shared usage of Amazon Bedrock sessions: The threads that connectors start are visible to all members of the the chat channel, and any member can participate in the session (user roles permitting). Consider this when exposing actions that depend on previous session context, as subsequent requests can be from different users.
- Amazon Bedrock session timeouts: Agents have a configurable idle session TTL after which any session data is forgotten. This is true for interactions with agents within a thread and if the idle session TTL is exceeded, previous contents of the conversation are lost. Further interactions with the agent within this thread maintain the same session ID but may lose the previous session context.
- Amazon Bedrock feature coverage: Connectors in Amazon Q Developer in chat applications are currently intended for use in textual conversations with agents. The use of the **Return Control** features in action groups for richer controls is currently not supported. Any trace context, observations, or linked sources are also currently not included in the final message. You can let us know if these features would be desirable by sending us feedback in your chat channel.
