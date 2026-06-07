# Configure Agentic Search on Amazon OpenSearch Serverless

## Agentic search

Agentic search uses agents to accept natural language input, interpret user intent,
and execute complex queries on your behalf. On Amazon OpenSearch Serverless, you can configure agents
to search over indexed data in your collections.

## Configure resources

To use agentic search, complete the following steps. Replace the
`placeholder values` with your specific information.

### Step 1: Configure permissions

Create a data access policy that grants agent and model permissions. The
following example grants all available agent and model permissions to all
agents and models in the collection (using the `*` wildcard). You
can scope down permissions to specific agents or models by replacing the
wildcard with a resource name, such as
`agent/`collection_name`/`agent_name``
 or
 `model/`collection_name`/`model_name``.
At minimum, `aoss:InvokeAgent` and
`aoss:ExecuteMLResource` are required to execute agentic searches
after the resources are available in the collection.

###### Note

When you create a collection using the easy create method in the AWS
console, agent and model permissions are enabled by default.

```

[
    {
        "Description": "Agent and model access policy for `collection_name`",
        "Rules": [
            {
                "ResourceType": "agent",
                "Resource": [
                    "agent/`collection_name`/*"
                ],
                "Permission": [
                    "aoss:CreateAgent",
                    "aoss:DescribeAgent",
                    "aoss:UpdateAgent",
                    "aoss:DeleteAgent",
                    "aoss:InvokeAgent",
                    "aoss:SearchAgents"
                ]
            },
            {
                "ResourceType": "model",
                "Resource": [
                    "model/`collection_name`/*"
                ],
                "Permission": [
                    "aoss:CreateMLResource",
                    "aoss:DescribeMLResource",
                    "aoss:UpdateMLResource",
                    "aoss:DeleteMLResource",
                    "aoss:ExecuteMLResource"
                ]
            }
        ],
        "Principal": [
            "arn:aws:iam::`account_id`:role/`role_name`"
        ]
    }
]

```

For more information about data access policies, see [Data access control for
Amazon OpenSearch Serverless](serverless-data-access.md "serverless-data-access.md").

### Step 2: Create a model

Register a model with an inline connector. The following example creates a
model using Amazon Bedrock Claude Haiku. The `roleArn` must have
permissions to invoke the specified Bedrock model, and its trust policy must
allow `ml.opensearchservice.amazonaws.com` to assume the role. For a list of
other supported Amazon Bedrock models, see [Supported models and features for the Converse API](../../../bedrock/latest/userguide/conversation-inference-supported-models-features.md "../../../bedrock/latest/userguide/conversation-inference-supported-models-features.md").

###### Important

Usage of any Amazon Bedrock model will incur charges. For detailed
pricing information, see the [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

###### Note

When signing requests to Amazon OpenSearch Serverless with cURL, you must include the
`x-amz-content-sha256` header. For more information, see
[Signing HTTP requests with other
clients](serverless-clients.md#serverless-signing "serverless-clients.md#serverless-signing").

```

POST /_plugins/_ml/models/_register?deploy=true
{
    "name": "Bedrock Claude Haiku",
    "function_name": "remote",
    "connector": {
        "name": "Amazon Bedrock Connector",
        "description": "Connector for Amazon Bedrock Claude Haiku",
        "version": 1,
        "protocol": "aws_sigv4",
        "parameters": {
            "region": "`region`",
            "service_name": "bedrock",
            "model": "us.anthropic.claude-haiku-4-5-20251001-v1:0"
        },
        "credential": {
            "roleArn": "arn:aws:iam::`account_id`:role/`role_name`"
        },
        "actions": [
            {
                "action_type": "predict",
                "method": "POST",
                "url": "https://bedrock-runtime.${parameters.region}.amazonaws.com/model/${parameters.model}/converse",
                "headers": {
                    "content-type": "application/json"
                },
                "request_body": "{ \"system\": [{\"text\": \"${parameters.system_prompt}\"}], \"messages\": [${parameters._chat_history:-}{\"role\":\"user\",\"content\":[{\"text\":\"${parameters.user_prompt}\"}]}${parameters._interactions:-}]${parameters.tool_configs:-} }"
            }
        ]
    }
}

```

Note the `model_id` returned in the response.

### Step 3: Create agentic search resources

You can create agentic search resources using OpenSearch UI or the API.

#### Step 3A: Using OpenSearch UI

OpenSearch UI provides a guided experience for creating agents and
executing agentic search. OpenSearch UI applications are available for
each collection, with links available in the AWS console.

###### To configure agentic search using OpenSearch UI

1. In OpenSearch UI, open the menu on the left-hand side. Select
   **OpenSearch Plugins** >
   **AI Search Flows**.
2. On the Workflows page, select the **New workflow**
   tab. Under the **Agentic Search** card, choose
   **Create**.
3. Provide a unique name for the search configuration, then choose
   **Create**.
4. Under **Configure agent**, choose
   **Create new agent**. Under
   **Tools** >
   **Query Planning**, select the model you
   deployed in Step 2, then choose
   **Create agent**.
5. Under **Test flow**, select an index, enter a
   natural language search query, and click
   **Search** to run an agentic search.
6. Choose **Export** to view details on how to
   create the relevant search pipelines and search queries to embed
   in your application.

#### Step 3B: Using the API

Create an agent with the `QueryPlanningTool`. The
`response_filter` value shown below is specific to Amazon
Bedrock models.

###### Note

In Amazon OpenSearch Serverless, agent names serve as unique identifiers. You cannot
create multiple agents with the same name within a collection.

```

POST /_plugins/_ml/agents/_register
{
    "name": "Agentic Search Agent",
    "type": "flow",
    "description": "Agent for agentic search",
    "tools": [
        {
            "type": "QueryPlanningTool",
            "parameters": {
                "model_id": "`model_id`",
                "response_filter": "$.output.message.content[0].text"
            }
        }
    ]
}

```

Note the `agent_id` returned in the response.

Create a search pipeline with an `agentic_query_translator`
search request processor:

```

PUT /_search/pipeline/`pipeline_name`
{
    "request_processors": [
        {
            "agentic_query_translator": {
                "agent_id": "`agent_id`"
            }
        }
    ]
}

```

###### Note

To include the generated DSL query in the search response, add an
`agentic_context` response processor to your search pipeline
with `dsl_query` set to `true`. For more
information, see [Agentic context processor](https://docs.opensearch.org/latest/search-plugins/search-pipelines/agentic-context-processor/ "https://docs.opensearch.org/latest/search-plugins/search-pipelines/agentic-context-processor/") in the OpenSearch
documentation.

To perform agentic search, use an `agentic` query clause and
specify the search pipeline in the URL path:

```

GET `index_name`/_search?search_pipeline=`pipeline_name`
{
    "query": {
        "agentic": {
            "query_text": "`natural language query`"
        }
    }
}

```

For detailed API examples and advanced configurations, see [Using flow agents for agentic search](https://docs.opensearch.org/latest/vector-search/ai-search/agentic-search/flow-agent/ "https://docs.opensearch.org/latest/vector-search/ai-search/agentic-search/flow-agent/") in the OpenSearch
documentation.
