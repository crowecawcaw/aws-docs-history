# Configuring Agentic Search with

Bedrock Claude

Agentic search leverages autonomous agents to execute complex searches on your
behalf by understanding user intent, orchestrating the right tools, generating
optimized queries, and providing transparent summaries of their decisions through a
natural language interface. These agents are powered by reasoning models, such as
Bedrock Claude.

Follow the steps below to open and run a CloudFormation template that automatically
configures Bedrock Claude models for agentic search, and how to configure and create
your agents in the AI Search Flows plugin on OpenSearch Dashboards.

## Enabling Bedrock Claude

Access

1. **Prerequisite:** If your domain
   uses fine-grained access control, map
   `arn:aws:iam::`your-account-id`:role/`LambdaInvokeOpenSearchMLCommonsRole``as a backend role to the`ml_full_access` role before
   running the template. This IAM role will be created automatically by
   CloudFormation if it doesn't already exist. For more information on
   how to configure the mapping, see [Map the ML role in OpenSearch Dashboards
   (if using fine-grained access control)](ml-external-connector.md#connector-external-fgac "ml-external-connector.md#connector-external-fgac").
2. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
3. In the left navigation, choose
   **Integrations**.
4. Under **Integration with Bedrock Claude for Agentic
   Search**, choose **Configure
   domain**. Ensure your domain is on version 3.3 or
   greater.
5. In the CloudFormation template, enter your OpenSearch Service domain endpoint and
   select a model. The remaining fields are optional or pre-filled.
   Click **Create Stack** and wait for the
   provisioning to complete.
6. From the Amazon OpenSearch Service console, select **Domains**, and
   select your domain. Click the **OpenSearch Dashboards
   URL** to access OpenSearch Dashboards.

## Building agents and running

Agentic Search

1. From OpenSearch Dashboards, open the menu on the left-hand side. Select
   **OpenSearch Plugins** > **AI Search
   Flows** to access the plugin.
2. On the **Workflows** page, select the **New
   workflow** tab, and under the **Agentic
   Search** card, click **Create**.
3. Provide a unique name for your search configuration, and click
   **Create**.
4. Under **Configure agent**, click **Create new
   agent**. Select your newly-created Bedrock Claude model,
   then click **Create agent**. If the button is
   disabled, check **Advanced Settings** >
   **LLM Interface**, and ensure there is a valid
   interface selected. All models from CloudFormation will be Bedrock Claude
   models, so you can select **Bedrock Claude**, if it
   isn't already, then click **Create agent**.
5. Under **Test flow**, try running agentic searches.
   Provide a natural language search query, and click
   **Search**.

For complete documentation of the AI Search Flows plugin, see [Configuring Agentic Search](https://docs.opensearch.org/latest/vector-search/ai-search/building-agentic-search-flows/ "https://docs.opensearch.org/latest/vector-search/ai-search/building-agentic-search-flows/") in the OpenSearch documentation.

For more information about how Agentic Search works, see [Agentic Search](https://opensearch.org/docs/latest/vector-search/ai-search/agentic-search/ "https://opensearch.org/docs/latest/vector-search/ai-search/agentic-search/") in the OpenSearch documentation.
