AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Conversing with your Amazon Bedrock Agent connectors using Amazon Q Developer in chat applications

To start a conversation with your agent, run:

`@Amazon Q ask `connector_name` `your message``. This invokes your configured agent with your message within a new session.
Your agent's response starts a new thread in your chat channel under the initial message.

Any subsequent mention of `@Amazon Q` in this thread sends the provided message directly to the agent and all interactions in this thread share the same agent and session ID. As such, you can
continue to ask questions in this thread without specifying the name of your connector.
