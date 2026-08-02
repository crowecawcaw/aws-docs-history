# Provision additional throughput for your agent's model

###### Note

Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore [Amazon Bedrock AgentCore](../../../bedrock-agentcore/latest/devguide/agentcore-get-started-cli.md "../../../bedrock-agentcore/latest/devguide/agentcore-get-started-cli.md"). Existing customers can continue to use the service as normal. For more information, see [Amazon Bedrock Agents Classic maintenance mode](agents-classic-maintenance-mode.md "agents-classic-maintenance-mode.md").

To increase the rate and number of tokens that the agent can process during model inference, associate a Provisioned Throughput that you've purchased for the model that your agent is using. To learn more about Provisioned Throughput and how to purchase it, see [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](prov-throughput.md "prov-throughput.md").

You can associate a Provisioned Throughput when you [create](agents-deploy.md "agents-deploy.md") or [update](agents-alias-edit.md "agents-alias-edit.md") an agent alias. In the Amazon Bedrock console, you choose the Provisioned Throughput when setting up the alias or editing it. In the Amazon Bedrock API, you specify the `provisionedThroughput` in the `routingConfiguration` when you send a [CreateAgentAlias](../APIReference/API_agent_CreateAgentAlias.md "../APIReference/API_agent_CreateAgentAlias.md") or [UpdateAgentAlias](../APIReference/API_agent_UpdateAgentAlias.md "../APIReference/API_agent_UpdateAgentAlias.md"); request.
