

# Web Answer
<a name="gateway-target-connector-web-answer-tool"></a>

Web Answer on Amazon Bedrock AgentCore takes a natural-language question and returns a synthesized answer with citations to current web sources. It is a managed connector that you add as a target to your AgentCore Gateway. Agents discover it with a standard `tools/list` call and invoke it like any other Model Context Protocol (MCP) tool.

Web Answer runs an agentic search for each question. It searches the web, reads relevant pages to ground its answer, and includes citations so you can verify claims. Your agent makes one tool call and gets back a finished, cited answer. You don’t need to build or maintain a search, page-fetch, and synthesis pipeline, and your agent’s model doesn’t need to process raw search results.

Web Answer and [Web Search Tool](gateway-target-connector-web-search-tool.md) complement each other:
+ Use **Web Search Tool** when your agent’s own model should reason over ranked results (titles, URLs, snippets, and publication dates).
+ Use **Web Answer** when your agent needs a finished answer with citations, for example for a factual sub-question inside a larger task.

**Topics**
+ [Key capabilities](#gateway-target-connector-web-answer-tool-key-capabilities)
+ [Private by design](#gateway-target-connector-web-answer-tool-privacy)
+ [How it works](#gateway-target-connector-web-answer-tool-how-it-works)
+ [Use cases](#gateway-target-connector-web-answer-tool-use-cases)
+ [Set up Web Answer](#gateway-target-connector-web-answer-tool-setup)
+ [Use with a harness](#gateway-target-connector-web-answer-tool-harness)
+ [Configure domain filtering](#gateway-target-connector-web-answer-tool-domain-filtering)
+ [Configure the Gateway Service Role](#gateway-target-connector-web-answer-tool-service-role)
+ [Input schema](#gateway-target-connector-web-answer-tool-input-schema)
+ [Response format](#gateway-target-connector-web-answer-tool-response-format)
+ [Availability](#gateway-target-connector-web-answer-tool-availability)
+ [Acceptable use](#gateway-target-connector-web-answer-tool-acceptable-use)

## Key capabilities
<a name="gateway-target-connector-web-answer-tool-key-capabilities"></a>

Web Answer provides the following key capabilities:
+  **Built-in agentic web search** – Runs several searches in parallel to cover the question, and reads relevant pages to ground its answer, all from one tool call.
+  **Answers with citations** – Returns markdown text with inline citation markers, plus a structured list of the cited source URLs.
+  **Current sources** – Runs new searches for every question.
+  **Zero infrastructure management** – You don’t provision search APIs, model endpoints, or outbound credentials. The Gateway exposes Web Answer as a standard MCP tool.
+  **Framework agnostic** – Works with Strands Agents, LangChain, LangGraph, CrewAI, or any MCP-compatible client.
+  **Domain, date, and location controls** – In connector version `1.1.0` and later, you can set a target-level domain include list and exclude list, and your agent can pass per-request domain filters, a published-date range, and a country.

## Private by design
<a name="gateway-target-connector-web-answer-tool-privacy"></a>

Before you let an agent send questions to the web, you need to know where those questions go. Web Answer keeps that answer simple.

 **Questions stay in AWS **   
When your agent calls Web Answer, the question is served entirely within AWS infrastructure. Web Answer searches a web index that Amazon builds and operates, and writes the answer with a model on Amazon Bedrock. It doesn’t send your questions to a third-party search engine. The Gateway authenticates to the AWS-owned connector and routes the request internally, so the data path stays inside AWS end to end.

 **Processing stays in your geography**   
Web Answer uses geographic cross-Region inference, so data processing remains in supported commercial AWS Regions within the geographic boundary. For more information, see [Availability](#gateway-target-connector-web-answer-tool-availability).

## How it works
<a name="gateway-target-connector-web-answer-tool-how-it-works"></a>

Web Answer is a built-in **connector**. The Gateway handles schema management, parameter governance, endpoint resolution, and service authentication.

1.  **Gateway setup** – You create a Gateway and add a Web Answer target with `connectorId: "web-answer"`. The Gateway snapshots the tool schema and provisions the integration.

1.  **Tool discovery** – Your agent calls `tools/list` on the Gateway endpoint and discovers the `<target-name>___WebAnswer` tool with its input schema.
**Note**  
If your gateway uses semantic search (`searchType: "SEMANTIC"`), `tools/list` also returns the gateway’s `x_amz_bedrock_agentcore_search` tool, and that tool can come first in the list. If your code selects the Web Answer tool itself, match the tool name that ends with `___WebAnswer`. Don’t rely on its position in the list.

1.  **Question** – Your agent calls `tools/call` with a natural-language question and, in connector version `1.1.0` and later, optional request-level filters and a country. The Gateway authenticates to the backend with its service role and passes on the target’s settings.

1.  **Agentic search** – Web Answer searches the web, reads the most relevant pages, and writes an answer from the evidence that it collected.

1.  **Cited answer** – Your agent gets the answer as markdown text with inline citations, and as structured content with a list of the cited URLs.

## Use cases
<a name="gateway-target-connector-web-answer-tool-use-cases"></a>

You can use Web Answer for the following use cases:
+  **Factual sub-questions** – Answer a specific question inside a larger agent workflow without adding a retrieval pipeline to the agent.
+  **Regulatory and policy Q&A** – Answer questions about regulations, standards, or policy changes, with citations so you can verify claims.
+  **Customer support** – Answer product and policy questions from current public information, with sources that your support agent can show to the customer.
+  **Research assistants** – Give knowledge workers current, cited answers that they can audit.

Web Answer is not a substitute for professional advice. Review outputs before you rely on them in regulated contexts.

## Set up Web Answer
<a name="gateway-target-connector-web-answer-tool-setup"></a>

For instructions on creating a Gateway Target with the Web Answer connector configuration, including setup examples that use the Python SDK and the AWS CLI, see [Set up Web Answer](gateway-add-target-api-target-config.md#gateway-add-target-api-connector-web-answer-setup) in the target configuration guide.

## Use with a harness
<a name="gateway-target-connector-web-answer-tool-harness"></a>

To give an [AgentCore harness](harness.md) access to Web Answer, attach the gateway that you created in Set up Web Answer to the harness as an `agentcore_gateway` tool. Grant the harness execution role the `bedrock-agentcore:InvokeGateway` permission on the gateway ARN. For the end-to-end walkthrough, see [Tools](harness-tools.md) in the harness documentation.

## Configure domain filtering
<a name="gateway-target-connector-web-answer-tool-domain-filtering"></a>

In connector version `1.1.0` and later, Web Answer supports 2 layers of filtering that compose on every request:
+  **Target-level domain include list and exclude list.** When you set up the target, you configure `parameterValues.domainFilter.include` and `parameterValues.domainFilter.exclude`, up to 50 domains per list. Your agent can’t see these lists, and Web Answer applies them to every request that flows through the target.
+  **Request-level filters.** Your agent can pass an optional `filters` object with each `tools/call` request:
  +  `domainFilter` – `include` and `exclude` lists, up to 50 domains per list.
  +  `publishedDateFilter` – `from` and `to` bounds, inclusive, ISO-8601 date or date-time, interpreted in UTC. A date-only `to` covers the whole day.

Request-level filters compose with the target-level lists:
+ A domain is excluded if it appears on either the target-level exclude list or the request-level exclude list. A root domain also matches its subdomains.
+ If both the target-level and request-level include lists are set, only domains present in both are used. If the two lists share no domains, the request fails with a validation error.
+ If `publishedDateFilter.from` is later than `publishedDateFilter.to`, the request fails with a validation error.

Request-level filters cannot override the target-level exclude list or expand beyond the target-level include list.

For configuration examples, see [Configure domain filtering](gateway-add-target-api-target-config.md#gateway-add-target-api-connector-web-answer-domain-filtering) in the target configuration guide.

## Configure the Gateway Service Role
<a name="gateway-target-connector-web-answer-tool-service-role"></a>

The Gateway needs a service role that allows the AgentCore service to perform actions on your behalf. For the required IAM permissions and policy configuration, see [Configure the Gateway Service Role](gateway-add-target-api-target-config.md#gateway-add-target-api-connector-web-answer-service-role) in the target configuration guide.

## Input schema
<a name="gateway-target-connector-web-answer-tool-input-schema"></a>

Web Answer accepts the following input schema when invoked through `tools/call`. The `filters` and `userLocation` fields are available in connector version `1.1.0` and later. On version `1.0.0`, the schema exposes only `query`.

```
{
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "description": "The question or search query to answer.",
        "type": "string"
      },
      "filters": {
        "description": "Per-call runtime filters set by the caller for this specific request. Contains an optional runtime domainFilter (merged with the admin-level domainFilter) and an optional publishedDateFilter.",
        "type": "object",
        "properties": {
          "domainFilter": {
            "description": "Per-call domain filter. Include and exclude lists each hold up to 50 domains. Merged with the admin-level domainFilter; the merged exclude list holds up to 100 domains.",
            "type": "object",
            "properties": {
              "include": {
                "description": "Domains to include in search results. When set, results are restricted to these domains (subject to merge rules with the peer filter).",
                "type": "array",
                "items": {"type": "string"}
              },
              "exclude": {
                "description": "Domains to exclude from search results. Root domain matches subdomains (for example, example.com matches blog.example.com).",
                "type": "array",
                "items": {"type": "string"}
              }
            }
          },
          "publishedDateFilter": {
            "description": "Per-call published-date filter. Both bounds inclusive, UTC, ISO-8601. Applies to web results only.",
            "type": "object",
            "properties": {
              "from": {
                "description": "Earliest publication date to include (inclusive).",
                "type": "string"
              },
              "to": {
                "description": "Latest publication date to include (inclusive).",
                "type": "string"
              }
            }
          }
        }
      },
      "userLocation": {
        "description": "Optional. Per-call caller location that may allow web results to be refined for that location. Only country is supported.",
        "type": "object",
        "properties": {
          "country": {
            "description": "Optional. ISO 3166-1 alpha-2 country code, for example \"DE\". Case-insensitive.",
            "type": "string"
          }
        }
      }
    },
    "required": ["query"]
  }
}
```


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `query`  | string | Yes | The question or search query to answer. 1 to 30,000 characters. | 
|  `filters`  | object | No | Optional request-level filters. Available in connector version `1.1.0` and later. | 
|  `filters.domainFilter.include`  | array of strings | No | Domains to include. 1 to 50 entries. | 
|  `filters.domainFilter.exclude`  | array of strings | No | Domains to exclude. A root domain also matches its subdomains. 1 to 50 entries. | 
|  `filters.publishedDateFilter.from`  | string | No | Earliest publication date, inclusive. ISO-8601 date (`YYYY-MM-DD`) or date-time (`YYYY-MM-DDTHH:mm:ss` with optional `Z` or `+HH:mm` offset). | 
|  `filters.publishedDateFilter.to`  | string | No | Latest publication date, inclusive. ISO-8601 date (`YYYY-MM-DD`) or date-time (`YYYY-MM-DDTHH:mm:ss` with optional `Z` or `+HH:mm` offset). | 
|  `userLocation`  | object | No | Optional caller location to refine web results. Available in connector version `1.1.0` and later. | 
|  `userLocation.country`  | string | No | ISO 3166-1 alpha-2 country code, for example `DE`. Exactly 2 letters, case-insensitive. | 

## Response format
<a name="gateway-target-connector-web-answer-tool-response-format"></a>

Web Answer returns an MCP tool result with `content`, `structuredContent`, `isError`, and `_meta` fields:

```
{
  "isError": false,
  "content": [
    {
      "type": "text",
      "text": "Under Basel III, banks must hold Common Equity Tier 1 capital of at least 4.5% of risk-weighted assets [[1](https://example.com/basel-iii)]..."
    }
  ],
  "structuredContent": {
    "answer": [
      {
        "text": "Under Basel III, banks must hold Common Equity Tier 1 capital of at least 4.5% of risk-weighted assets [[1](https://example.com/basel-iii)]...",
        "citations": [
          {"domain": "example.com", "url": "https://example.com/basel-iii"}
        ]
      }
    ]
  },
  "_meta": {
    "latencyMs": 5210
  }
}
```
+  `content[0].text` is markdown text, not JSON. Inline citation markers use the form `[[N](url)]`. `N` starts at 1, and a marker can repeat when several sentences cite the same source.
+  `structuredContent.answer` is a list of answer blocks. Each block has `text` and an optional `citations` list. The marker ` ` in a block’s text refers to `citations[N-1]` of that block. Read every block in the list.
+ Each citation has a `url` and, when available, a `domain`.
+  `_meta.latencyMs` reports the server-side latency.
+ When the tool can’t answer, `isError` is `true` and `content[0].text` describes the problem.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `content[].text`  | string | Yes | The answer as markdown text with inline citation markers. | 
|  `structuredContent.answer[].text`  | string | Yes | The text of an answer block. | 
|  `structuredContent.answer[].citations[].url`  | string | Yes | URL of a cited source. | 
|  `structuredContent.answer[].citations[].domain`  | string | No | Domain of a cited source. | 
|  `isError`  | boolean | Yes |  `true` when the result describes an error instead of an answer. | 

## Availability
<a name="gateway-target-connector-web-answer-tool-availability"></a>

The Web Answer connector is available in the following AWS Region:
+ US East (N. Virginia) `us-east-1` 

Web Answer uses geographic cross-Region inference. Data processing remains in supported commercial AWS Regions within specified geographic boundaries, such as the US, EU, and APAC. For more information, see [Geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html) in the *Amazon Bedrock User Guide*.

Because Amazon operates the full Web Answer stack, improvements to search, reading, and answer quality reach your agents through the same managed connector. You don’t need to upgrade or migrate anything.

## Acceptable use
<a name="gateway-target-connector-web-answer-tool-acceptable-use"></a>

If you use Web Answer, you are responsible for your use, and any use by your end users, of Web Answer results ("Web Answer Results"). You must retain and display the source citations and links provided with each Web Answer Result in any output you surface to your end users that uses the Web Answer Result. You may not use Web Answer to (a) extract, store, or reproduce content from Web Answer Results in bulk, or (b) build or populate a competing index or database.