

# Provision additional throughput for your agent's model
<a name="agents-pt"></a>

**Amazon Bedrock Agents Classic availability**  
You can no longer sign up for Amazon Bedrock Agents (now Amazon Bedrock Agents Classic). If you already use Agents Classic, you can continue to use it.  
For more information about building code-defined agents with the Strands Agents SDK, see [Get started with Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html). For more information about Agents Classic, see [Amazon Bedrock Agents Classic maintenance mode](agents-classic-maintenance-mode.md).

To increase the rate and number of tokens that the agent can process during model inference, associate a Provisioned Throughput that you've purchased for the model that your agent is using. To learn more about Provisioned Throughput and how to purchase it, see [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](prov-throughput.md).

You can associate a Provisioned Throughput when you [create](agents-deploy.md) or [update](agents-alias-edit.md) an agent alias. In the Amazon Bedrock console, you choose the Provisioned Throughput when setting up the alias or editing it. In the Amazon Bedrock API, you specify the `provisionedThroughput` in the `routingConfiguration` when you send a [CreateAgentAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgentAlias.html) or [UpdateAgentAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentAlias.html); request.