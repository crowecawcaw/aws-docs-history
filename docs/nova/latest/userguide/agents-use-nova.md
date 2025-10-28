# Using Amazon Nova as a foundation model in an AI

agent

To use Amazon Nova models as the foundation model in an AI agent, you can use [Amazon Bedrock Agents](../../../bedrock/latest/userguide/agents-how.md "../../../bedrock/latest/userguide/agents-how.md") or you can [call a tool with the Converse API](../../../bedrock/latest/userguide/tool-use-inference-call.md "../../../bedrock/latest/userguide/tool-use-inference-call.md") or InvokeModel API.
Amazon Bedrock Agents is a fully managed service that you can use to build and
configure autonomous agents in your application. You can also use the converse API and
Invoke model API to connect to other out-of-the-box agent frameworks or build your own
agent framework.

You can use placeholder variables in agent prompt templates. The variables will be populated by pre-existing configurations when the prompt template is called. For information about these placeholder variables, see [Use placeholder variables in Amazon Bedrock agent prompt templates](../../../bedrock/latest/userguide/prompt-placeholders.md "../../../bedrock/latest/userguide/prompt-placeholders.md").

###### Topics

- [Using Amazon Nova with Amazon Bedrock agents](#agents-bedrock "#agents-bedrock")
- [Using Amazon Nova with the Invoke and Converse API](#agents-converse "#agents-converse")

## Using Amazon Nova with Amazon Bedrock agents

Amazon Nova models are enabled in [Bedrock
Agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md") and follow the user instructions of Amazon Bedrock
Agents. Amazon Bedrock Agents is preconfigured with key features and prompts
in order to work effectively with the Amazon Nova models. These configurations enable
you to leverage key features of Amazon Bedrock Agents with minimal
effort:

- **Autonomous Agents**: Amazon Bedrock
  Agents allow for the creation of autonomous agents that can perform tasks
  based on user input and organizational data without requiring extensive
  custom coding. This can save you significant time and effort.
- **Built-in API Invocation**:
  Amazon Bedrock Agents automatically handle API calls to fulfill user
  requests, which simplifies the integration of external services and data
  sources.
- **Memory and Context Management**: Agents can
  maintain context, conversation and memory across interactions, allowing for
  more personalized and coherent conversations over time.
- **Knowledge Base Integration**: You can
  associate a knowledge base with the agent to enhance its performance and
  accuracy, enabling it to provide more relevant responses based on stored
  information.
- **Prompt Engineering and Customization**:
  Amazon Bedrock Agents support advanced prompt engineering, allowing
  developers to customize the agent's behavior and responses to better fit
  specific use cases.
- **Code Interpreter:** The code interpretation
  enables your agent to generate, run, and troubleshoot your application code
  in a secure test environment.
- **Multi-Agent Collaboration:** Build, deploy, and manage multiple AI agents working together on complex multi-step tasks that require specialized skills.

## Using Amazon Nova with the Invoke and Converse API

It's also possible to leverage [Tool use (function calling) with Amazon Nova](tool-use.md "tool-use.md")
with Invoke and Converse APIs to integrate Amazon Nova models with open source or
build custom AI Agent frameworks. This allows for great flexibility but it's
important to note that using the API directly means some aspects are left for your
implementation or library to handle:

1. **Store Conversation/User Data**: The
   Converse API does not retain any user inputs or generated content, which
   means your agent cannot remember past interactions. You need to pass all the
   past messages every time you invoke the model.
2. **Automatic Tool Invocation**: You, as the
   developer, are responsible for implementing the tool based on the model's
   request. This means you need to execute or write the code that executes the
   tool's functionality and processes the input parameters provided by the
   model. After executing the tool, you must send the results back to the model
   in a structured format.
3. **Built-in Memory**: The API lacks built-in
   memory capabilities, meaning your agent cannot remember user preferences or
   past interactions over time, which could limit personalization.
