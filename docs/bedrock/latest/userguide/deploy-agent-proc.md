# Create an alias for your agent

The following procedure shows you how to create an alias and a version for your agent. After you
create an alias, you can use the agent in your application by making an [InvokeAgent](../APIReference/API_agent-runtime_InvokeAgent.md "../APIReference/API_agent-runtime_InvokeAgent.md")
request with an [Agents for Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#bra-rt "../../../general/latest/gr/bedrock.md#bra-rt").

###### To create an alias

- Create an alias and version of your agent. Choose the tab for your preferred method, and then follow the steps:

Console

###### To create an alias (and optionally a new version)

    1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
     [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
    2. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.
    3. In the **Aliases** section, choose
     **Create**.
    4. Enter a unique **Alias name** and provide
     an optional **Description**.
    5. Under **Associate a version**, choose one
     of the following options:


    	+ To create a new version, choose **Create a
    	 new version and to associate it to this
    	 alias**.
    	+ To use an existing version, choose **Use
    	 an existing version to associate this
    	 alias**. From the dropdown menu, choose
    	 the version that you want to associate the alias
    	 to.
    6. Under **Select throughput**, select one
     of the following options:


    	+ To let your agent run model inference at the rates
    	 set for your account, select **On-demand
    	 (ODT)**. For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md").
    	+ To let your agent run model inference at an
    	 increased rate using a Provisioned Throughput that you previously
    	 purchased for the model, select **Provisioned Throughput
    	 (PT)** and then select a provisioned
    	 model. For more information, see [Provisioned Throughput](prov-throughput.md "prov-throughput.md").
    7. Select **Create alias**.

API
To create an alias for an agent, send a [CreateAgentAlias](../APIReference/API_agent_CreateAgentAlias.md "../APIReference/API_agent_CreateAgentAlias.md")
request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt").

The following fields are required:

| Field                | Use case                                                                                                                                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| agentId              | To specify the ID of the agent for which to create an alias.                                                                                                                                                |
| agentName            | To specify a name for the alias.                                                                                                                                                                            | The following fields are optional:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Field                | Use case                                                                                                                                                                                                    |
| ---                  | ---                                                                                                                                                                                                         |
| description          | To provide a description of the alias.                                                                                                                                                                      |
| routingConfiguration | To specify a version to associate the alias with (leave blank to create a new version) and a [Provisioned Throughput](prov-throughput.md "prov-throughput.md") to associate with the alias.                 |
| clientToken          | To ensure the API request completes only once. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md"). |
| tags                 | To associate [tags](tagging.md "tagging.md") with the alias.                                                                                                                                                | `def create_agent_alias(self, name, agent_id): """ Creates an alias of an agent that can be used to deploy the agent. :param name: The name of the alias. :param agent_id: The unique identifier of the agent. :return: Details about the alias that was created. """ try: response = self.client.create_agent_alias( agentAliasName=name, agentId=agent_id ) agent_alias = response["agentAlias"] except ClientError as e: logger.error(f"Couldn't create agent alias. {e}") raise else: return agent_alias` For more information, see [Hello Amazon Bedrock Agents](bedrock-agent_example_bedrock-agent_Hello_section.md "bedrock-agent_example_bedrock-agent_Hello_section.md"). |
