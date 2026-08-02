# Configure agent to request information from user to increase accuracy of function prediction

###### Note

Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore [Amazon Bedrock AgentCore](../../../bedrock-agentcore/latest/devguide/agentcore-get-started-cli.md "../../../bedrock-agentcore/latest/devguide/agentcore-get-started-cli.md"). Existing customers can continue to use the service as normal. For more information, see [Amazon Bedrock Agents Classic maintenance mode](agents-classic-maintenance-mode.md "agents-classic-maintenance-mode.md").

You can configure your agent to request more information from the user if it doesn't have enough information to accomplish a task. If your agent has action groups or
APIs with some parameters, by default, the agent will use the default values for those parameters or Foundation Model hallucinates to assume the values of the parameter
to complete the API request if it is not provided by the user. This might lead to agent inaccurately predicting the next function or the method to invoke based on the current interaction and causing
hallucination.

To increase you agent’s accuracy, configure your agent to ask user to provide more information by enabling `User input` field in the Amazon Bedrock console,
using the API, or using the AWS SDKs. Amazon Bedrock Agent model user input is a builtin ActionGroup that you'll need to add as an action group to your agent.
