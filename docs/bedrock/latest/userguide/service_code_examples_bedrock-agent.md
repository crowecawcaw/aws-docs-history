# Code examples for Amazon Bedrock Agents using AWS SDKs

The following code examples show how to use Amazon Bedrock Agents with an AWS software development kit (SDK).

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Bedrock with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code example shows how to get started using Amazon Bedrock Agents.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/bedrock-agent#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/bedrock-agent#code-examples").

```

import { fileURLToPath } from "node:url";

import {
  BedrockAgentClient,
  GetAgentCommand,
  paginateListAgents,
} from "@aws-sdk/client-bedrock-agent";

/**
 * @typedef {Object} AgentSummary
 */

/**
 * A simple scenario to demonstrate basic setup and interaction with the Bedrock Agents Client.
 *
 * This function first initializes the Amazon Bedrock Agents client for a specific region.
 * It then retrieves a list of existing agents using the streamlined paginator approach.
 * For each agent found, it retrieves detailed information using a command object.
 *
 * Demonstrates:
 * - Use of the Bedrock Agents client to initialize and communicate with the AWS service.
 * - Listing resources in a paginated response pattern.
 * - Accessing an individual resource using a command object.
 *
 * @returns {Promise<void>} A promise that resolves when the function has completed execution.
 */
export const main = async () => {
  const region = "us-east-1";

  console.log("=".repeat(68));

  console.log(`Initializing Amazon Bedrock Agents client for ${region}...`);
  const client = new BedrockAgentClient({ region });

  console.log("Retrieving the list of existing agents...");
  const paginatorConfig = { client };
  const pages = paginateListAgents(paginatorConfig, {});

  /** @type {AgentSummary[]} */
  const agentSummaries = [];
  for await (const page of pages) {
    agentSummaries.push(...page.agentSummaries);
  }

  console.log(`Found ${agentSummaries.length} agents in ${region}.`);

  if (agentSummaries.length > 0) {
    for (const agentSummary of agentSummaries) {
      const agentId = agentSummary.agentId;
      console.log("=".repeat(68));
      console.log(`Retrieving agent with ID: ${agentId}:`);
      console.log("-".repeat(68));

      const command = new GetAgentCommand({ agentId });
      const response = await client.send(command);
      const agent = response.agent;

      console.log(` Name: ${agent.agentName}`);
      console.log(` Status: ${agent.agentStatus}`);
      console.log(` ARN: ${agent.agentArn}`);
      console.log(` Foundation model: ${agent.foundationModel}`);
    }
  }
  console.log("=".repeat(68));
};

// Invoke main function if this file was run directly.
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  await main();
}


```

- For API details, see the following topics in _AWS SDK for JavaScript API Reference_.
  - [GetAgent](../../../AWSJavaScriptSDK/v3/latest/client/bedrock-agent/command/GetAgentCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/bedrock-agent/command/GetAgentCommand.md")
  - [ListAgents](../../../AWSJavaScriptSDK/v3/latest/client/bedrock-agent/command/ListAgentsCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/bedrock-agent/command/ListAgentsCommand.md")

###### Code examples

- [Basics](service_code_examples_bedrock-agent_basics.md "service_code_examples_bedrock-agent_basics.md")
  - [Hello Amazon Bedrock Agents](bedrock-agent_example_bedrock-agent_Hello_section.md "bedrock-agent_example_bedrock-agent_Hello_section.md")
  - [Actions](service_code_examples_bedrock-agent_actions.md "service_code_examples_bedrock-agent_actions.md")
    - [CreateAgent](bedrock-agent_example_bedrock-agent_CreateAgent_section.md "bedrock-agent_example_bedrock-agent_CreateAgent_section.md")
    - [CreateAgentActionGroup](bedrock-agent_example_bedrock-agent_CreateAgentActionGroup_section.md "bedrock-agent_example_bedrock-agent_CreateAgentActionGroup_section.md")
    - [CreateAgentAlias](bedrock-agent_example_bedrock-agent_CreateAgentAlias_section.md "bedrock-agent_example_bedrock-agent_CreateAgentAlias_section.md")
    - [CreateFlow](bedrock-agent_example_bedrock-agent_CreateFlow_section.md "bedrock-agent_example_bedrock-agent_CreateFlow_section.md")
    - [CreateFlowAlias](bedrock-agent_example_bedrock-agent_CreateFlowAlias_section.md "bedrock-agent_example_bedrock-agent_CreateFlowAlias_section.md")
    - [CreateFlowVersion](bedrock-agent_example_bedrock-agent_CreateFlowVersion_section.md "bedrock-agent_example_bedrock-agent_CreateFlowVersion_section.md")
    - [CreateKnowledgeBase](bedrock-agent_example_bedrock-agent_CreateKnowledgeBase_section.md "bedrock-agent_example_bedrock-agent_CreateKnowledgeBase_section.md")
    - [CreatePrompt](bedrock-agent_example_bedrock-agent_CreatePrompt_section.md "bedrock-agent_example_bedrock-agent_CreatePrompt_section.md")
    - [CreatePromptVersion](bedrock-agent_example_bedrock-agent_CreatePromptVersion_section.md "bedrock-agent_example_bedrock-agent_CreatePromptVersion_section.md")
    - [DeleteAgent](bedrock-agent_example_bedrock-agent_DeleteAgent_section.md "bedrock-agent_example_bedrock-agent_DeleteAgent_section.md")
    - [DeleteAgentAlias](bedrock-agent_example_bedrock-agent_DeleteAgentAlias_section.md "bedrock-agent_example_bedrock-agent_DeleteAgentAlias_section.md")
    - [DeleteFlow](bedrock-agent_example_bedrock-agent_DeleteFlow_section.md "bedrock-agent_example_bedrock-agent_DeleteFlow_section.md")
    - [DeleteFlowAlias](bedrock-agent_example_bedrock-agent_DeleteFlowAlias_section.md "bedrock-agent_example_bedrock-agent_DeleteFlowAlias_section.md")
    - [DeleteFlowVersion](bedrock-agent_example_bedrock-agent_DeleteFlowVersion_section.md "bedrock-agent_example_bedrock-agent_DeleteFlowVersion_section.md")
    - [DeleteKnowledgeBase](bedrock-agent_example_bedrock-agent_DeleteKnowledgeBase_section.md "bedrock-agent_example_bedrock-agent_DeleteKnowledgeBase_section.md")
    - [DeletePrompt](bedrock-agent_example_bedrock-agent_DeletePrompt_section.md "bedrock-agent_example_bedrock-agent_DeletePrompt_section.md")
    - [GetAgent](bedrock-agent_example_bedrock-agent_GetAgent_section.md "bedrock-agent_example_bedrock-agent_GetAgent_section.md")
    - [GetFlow](bedrock-agent_example_bedrock-agent_GetFlow_section.md "bedrock-agent_example_bedrock-agent_GetFlow_section.md")
    - [GetFlowVersion](bedrock-agent_example_bedrock-agent_GetFlowVersion_section.md "bedrock-agent_example_bedrock-agent_GetFlowVersion_section.md")
    - [GetKnowledgeBase](bedrock-agent_example_bedrock-agent_GetKnowledgeBase_section.md "bedrock-agent_example_bedrock-agent_GetKnowledgeBase_section.md")
    - [GetPrompt](bedrock-agent_example_bedrock-agent_GetPrompt_section.md "bedrock-agent_example_bedrock-agent_GetPrompt_section.md")
    - [ListAgentActionGroups](bedrock-agent_example_bedrock-agent_ListAgentActionGroups_section.md "bedrock-agent_example_bedrock-agent_ListAgentActionGroups_section.md")
    - [ListAgentKnowledgeBases](bedrock-agent_example_bedrock-agent_ListAgentKnowledgeBases_section.md "bedrock-agent_example_bedrock-agent_ListAgentKnowledgeBases_section.md")
    - [ListAgents](bedrock-agent_example_bedrock-agent_ListAgents_section.md "bedrock-agent_example_bedrock-agent_ListAgents_section.md")
    - [ListFlowAliases](bedrock-agent_example_bedrock-agent_ListFlowAliases_section.md "bedrock-agent_example_bedrock-agent_ListFlowAliases_section.md")
    - [ListFlowVersions](bedrock-agent_example_bedrock-agent_ListFlowVersions_section.md "bedrock-agent_example_bedrock-agent_ListFlowVersions_section.md")
    - [ListFlows](bedrock-agent_example_bedrock-agent_ListFlows_section.md "bedrock-agent_example_bedrock-agent_ListFlows_section.md")
    - [ListKnowledgeBases](bedrock-agent_example_bedrock-agent_ListKnowledgeBases_section.md "bedrock-agent_example_bedrock-agent_ListKnowledgeBases_section.md")
    - [ListPrompts](bedrock-agent_example_bedrock-agent_ListPrompts_section.md "bedrock-agent_example_bedrock-agent_ListPrompts_section.md")
    - [PrepareAgent](bedrock-agent_example_bedrock-agent_PrepareAgent_section.md "bedrock-agent_example_bedrock-agent_PrepareAgent_section.md")
    - [PrepareFlow](bedrock-agent_example_bedrock-agent_PrepareFlow_section.md "bedrock-agent_example_bedrock-agent_PrepareFlow_section.md")
    - [UpdateFlow](bedrock-agent_example_bedrock-agent_UpdateFlow_section.md "bedrock-agent_example_bedrock-agent_UpdateFlow_section.md")
    - [UpdateFlowAlias](bedrock-agent_example_bedrock-agent_UpdateFlowAlias_section.md "bedrock-agent_example_bedrock-agent_UpdateFlowAlias_section.md")
    - [UpdateKnowledgeBase](bedrock-agent_example_bedrock-agent_UpdateKnowledgeBase_section.md "bedrock-agent_example_bedrock-agent_UpdateKnowledgeBase_section.md")

- [Scenarios](service_code_examples_bedrock-agent_scenarios.md "service_code_examples_bedrock-agent_scenarios.md")
  - [Create and invoke a flow](bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockFlows_section.md "bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockFlows_section.md")
  - [Create and invoke a managed prompt](bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockPrompts_section.md "bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockPrompts_section.md")
  - [Create and invoke an agent](bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockAgents_section.md "bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockAgents_section.md")
  - [Orchestrate generative AI applications with Step Functions](bedrock-agent_example_cross_ServerlessPromptChaining_section.md "bedrock-agent_example_cross_ServerlessPromptChaining_section.md")
