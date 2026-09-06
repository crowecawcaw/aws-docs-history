

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# About the AWS Marketplace MCP server
<a name="marketplace-mcp-server"></a>

AWS Marketplace Model Context Protocol (MCP) provides AI-powered tools for AWS Marketplace discovery, evaluation, research, and proposal generation. MCP is a standardized protocol that enables AI assistants to interact with external systems through the following:
+ **Tools**: Functions that AI models can invoke to perform actions.
+ **Resources**: Data and context that can be shared with AI models.

All tools are stateless — each call is independent with no server-side conversation state.

**Example use cases**

The following are common ways to use the AWS Marketplace MCP server:
+ Find products that address business needs using natural language queries.
+ Evaluate multiple vendors quickly with AI-generated comparison reports.
+ Create comprehensive purchase proposals tailored to business requirements.
+ Get side-by-side analysis of competing solutions.

**Endpoint:** `https://marketplace-mcp.us-east-1.api.aws/mcp`

**Protocol:** MCP over Streamable HTTP (JSON-RPC 2.0). All responses are single JSON payloads.

**Authentication:** None required.

**Topics**
+ [Available tools](#marketplace-mcp-available-tools)
+ [Integration guide](#marketplace-mcp-integration-guide)
+ [Tool details](#marketplace-mcp-tool-details)
+ [Workflows](#marketplace-mcp-workflows)
+ [End-to-end example](#marketplace-mcp-end-to-end-example)
+ [Error handling](#marketplace-mcp-error-handling)

## Available tools
<a name="marketplace-mcp-available-tools"></a>

All 6 tools are stateless and require no conversation context or session management. All tool definitions, including full input/output schemas, are available programmatically through the standard MCP `tools/list` endpoint. The schemas returned by `tools/list` are the canonical, always-current source of truth for parameter names, types, and constraints.

The following table summarizes each tool and whether it is read-only.


| Tool name | Description | Read-only | 
| --- | --- | --- | 
| [`get_aws_marketplace_report_guidelines`](#marketplace-mcp-tool-report-guidelines) | Returns workflow instructions and report format templates for recommendations, comparisons, or evaluations. Call first for any report workflow. | Yes | 
| [`search_aws_marketplace_solutions`](#marketplace-mcp-tool-search-solutions) | Searches the AWS Marketplace catalog by queries. Supports batch queries (up to 10) and cursor-based pagination. | Yes | 
| [`get_aws_marketplace_solution`](#marketplace-mcp-tool-get-solution) | Gets detailed solution metadata by solution IDs (reviews, pricing, sentiments, rankings, CTAs). | Yes | 
| [`get_aws_marketplace_related_solutions`](#marketplace-mcp-tool-related-solutions) | Gets related solutions for given solution IDs, ranked by relation score. | Yes | 
| [`research_aws_marketplace_solution`](#marketplace-mcp-tool-research-solution) | Performs deep web research on solutions (features, reviews, limitations, competitors, pricing, integrations, case studies). Hidden from clients with native web search. | Yes | 
| [`submit_aws_marketplace_feedback`](#marketplace-mcp-tool-submit-feedback) | Submits user feedback (positive/negative) about report quality. | No | 

## Integration guide
<a name="marketplace-mcp-integration-guide"></a>

You can integrate with the AWS Marketplace MCP server in two ways: through a no-code Claude Connector or through a programmatic MCP client.

### Claude Connector (recommended)
<a name="marketplace-mcp-claude-connector"></a>

The fastest way to use AWS Marketplace MCP tools is through the **AWS Marketplace connector for Claude**. This requires no coding or MCP client setup — Claude handles tool discovery and invocation automatically.

**Setup:**

1. Open the [AWS Marketplace connector](https://claude.ai/directory/connectors/2ed43e1e-f547-48a3-85cc-b9baa412d06b) in the Claude Connectors Directory.

1. Choose **Connect** to enable it.

1. In any Claude conversation, choose the **\+** button (lower left) or type **/** to open the menu.

1. Hover over **Connectors** and toggle on **AWS Marketplace**.

1. Ask Claude to find, compare, or evaluate AWS Marketplace products — it automatically uses the MCP tools.

For more details on how connectors work, see [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).

**Example prompts:**
+ "Find the best SIEM solutions on AWS Marketplace for a mid-size company"
+ "Compare Datadog vs New Relic on AWS Marketplace"
+ "Build an evaluation report for Terraform Cloud on AWS Marketplace"

### MCP client integration
<a name="marketplace-mcp-client-integration"></a>

For programmatic integrations or custom agent frameworks, connect directly to the MCP endpoint.

#### Prerequisites
<a name="marketplace-mcp-prerequisites"></a>

You need the following to get started:

1. An MCP-compatible agent framework or client.

1. An HTTP client capable of making JSON-RPC 2.0 requests.

#### Step 1: Set up MCP client
<a name="marketplace-mcp-setup-client"></a>

Use a standard MCP client that supports HTTP transport.

**Endpoint:**

```
https://marketplace-mcp.us-east-1.api.aws/mcp
```

The following methods are supported:
+ `POST` with `method: "initialize"` — Initialize session and obtain `Mcp-Session-Id`.
+ `POST` with `method: "tools/list"` — Discover available tools and their schemas.
+ `POST` with `method: "tools/call"` — Invoke a tool.

**Authentication:** No authentication is required. Omit auth headers in HTTP requests.

#### Step 2: Obtain and register tools (tool discovery)
<a name="marketplace-mcp-setup-obtain-tools"></a>

All tool definitions are available programmatically through the standard MCP `tools/list` method. This is the recommended way to obtain current input/output schemas, as tool schemas may be updated independently of this documentation. Call `tools/list` once during initialization and register the returned tools in your agent's tool manifest or system prompt.

The following example shows a `tools/list` request.

**Request:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

**Response (abbreviated):**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_aws_marketplace_report_guidelines",
        "description": "...",
        "inputSchema": { ... }
      },
      {
        "name": "search_aws_marketplace_solutions",
        "description": "...",
        "inputSchema": { ... }
      },
      {
        "name": "get_aws_marketplace_solution",
        "description": "...",
        "inputSchema": { ... }
      },
      {
        "name": "get_aws_marketplace_related_solutions",
        "description": "...",
        "inputSchema": { ... }
      },
      {
        "name": "research_aws_marketplace_solution",
        "description": "...",
        "inputSchema": { ... }
      },
      {
        "name": "submit_aws_marketplace_feedback",
        "description": "...",
        "inputSchema": { ... }
      }
    ]
  }
}
```

Each tool entry includes the tool `name`, a detailed `description` with usage guidance and examples, and a complete `inputSchema` with parameter types, constraints, and validation rules.

#### Step 3: Configure telemetry
<a name="marketplace-mcp-setup-telemetry"></a>

AWS Marketplace MCP requires a stable identifier on every tool call for request correlation and telemetry. This is not an authentication credential — it is used only for diagnostics and analytics.

Pass the identifier in the custom HTTP header:

```
Mcp-Session-Id: <stable-id>
```
+ **Browser clients:** Derive from an existing session cookie or a frontend-generated UUID. Use the same value across all tool calls.
+ **Programmatic clients:** Use `POST` with `method: "initialize"` to obtain an `Mcp-Session-Id`.

#### HTTP transport
<a name="marketplace-mcp-streamable-http-transport"></a>

AWS Marketplace MCP uses HTTP transport, where the server operates as an independent HTTP service that can handle multiple client connections.

The following are key transport characteristics:
+ **HTTP POST for requests:** Every client message is sent as a new HTTP POST request.
+ **JSON responses:** All tools return JSON responses (`Content-Type: application/json`).
+ **Session management:** Session IDs through the `Mcp-Session-Id` header for request correlation and telemetry.
+ **Protocol version:** Specified through the `MCP-Protocol-Version: 2025-06-18` header.

**Required HTTP headers:**

```
Content-Type: application/json
Mcp-Session-Id: <stable-uuid>
MCP-Protocol-Version: 2025-06-18
```

The following example shows a tool call request and response.

**Example request:**

```
POST /mcp HTTP/1.1
Content-Type: application/json
Mcp-Session-Id: 1868a90c-5b12-4e8a-9f3d-2a1b3c4d5e6f
MCP-Protocol-Version: 2025-06-18

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search_aws_marketplace_solutions",
    "arguments": {
      "queries": ["SIEM solutions"]
    }
  }
}
```

**Example response:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"results\":[...],\"next_cursor\":null}"
      }
    ],
    "isError": false
  }
}
```

## Tool details
<a name="marketplace-mcp-tool-details"></a>

This section describes each tool's input parameters, output format, and usage guidance.

### get\_aws\_marketplace\_report\_guidelines
<a name="marketplace-mcp-tool-report-guidelines"></a>

Returns workflow instructions and output format template for a given report type. **Call this first** for any recommendation, comparison, or evaluation workflow.

This tool returns different prompts depending on client capabilities — clients with native web search get prompts with embedded search queries instead of `research_aws_marketplace_solution` tool references.

**Input:**

```
{
  "workflow_type": "recommendations" | "comparison" | "evaluation"
}
```

The following table describes the input parameters.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| workflow\_type | enum | Yes | "recommendations" for ranked product discovery, "comparison" for side-by-side analysis, "evaluation" for single-product assessment. | 

**Output:**

```
{
  "workflow_type": "recommendations",
  "guidelines": "# AWS Marketplace Recommendations Workflow\n\n..."
}
```

The following table describes the output fields.


| Field | Type | Description | 
| --- | --- | --- | 
| workflow\_type | string | The requested workflow type. | 
| guidelines | string | Combined workflow instructions and markdown format template. | 

**When to use each workflow:**
+ **recommendations** — "find monitoring tools", "I need a CI/CD solution", "SOC2-compliant security scanning under $5k/month".
+ **comparison** — "compare Datadog vs New Relic", "Splunk vs Elastic for log management".
+ **evaluation** — "build evaluation report for Terraform Cloud", "justify purchasing New Relic to my CTO".

### search\_aws\_marketplace\_solutions
<a name="marketplace-mcp-tool-search-solutions"></a>

Performs a direct AWS Marketplace Catalog API search. Returns raw, unranked, unfiltered results without AI processing or relevance scoring. Supports batch queries (up to 10) and cursor-based pagination for single queries.

**Input:**

```
{
  "queries": ["Drata compliance", "Vanta compliance"],
  "max_results": 5,
  "cursor": null
}
```

The following table describes the input parameters.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| queries | string[] | Yes | Array of search queries (1-10). Also accepts legacy query (single string, auto-converted to array). | 
| max\_results | number | No | Maximum results per query (1-100, default: 10). | 
| cursor | string | No | Pagination cursor (only works for single query, ignored for batch). | 

**Output:**

```
{
  "results": [
    {
      "solution_id": "prodview-abc123",
      "solution_name": "Drata",
      "vendor_name": "Drata Inc",
      "vendor_url": "https://aws.amazon.com/marketplace/seller-profile?id=...",
      "solution_description": "Continuous compliance automation...",
      "solution_url": "https://aws.amazon.com/marketplace/pp/prodview-abc123",
      "reviews_summary": {
        "reviews_count": 150,
        "average_rating": 4.7
      }
    }
  ],
  "next_cursor": "eyJvZmZzZXQiOjEwLCJwYWdlU2l6ZSI6MTB9"
}
```

The following table describes the output fields.


| Field | Type | Description | 
| --- | --- | --- | 
| results | MinimalSolutionMetadata[] | Array of matching solutions. | 
| next\_cursor | string \| null | Pagination cursor for next page (single query only). null when no more results. | 

**Batch behavior:** For multiple queries, results are combined and deduplicated by `solution_id`. The pagination cursor is not returned for batch requests.

**Pagination:** If `next_cursor` is returned (single-query requests only), pass it back as the `cursor` parameter to retrieve additional results. When `next_cursor` is `null`, all matching solutions have been retrieved.

### get\_aws\_marketplace\_solution
<a name="marketplace-mcp-tool-get-solution"></a>

Performs a direct AWS Marketplace Catalog API call. Retrieves comprehensive solution metadata by solution ID without AI processing. Supports batch requests (up to 10 IDs).

**Input:**

```
{
  "solution_ids": ["prodview-abc123", "prodview-xyz789"]
}
```

The following table describes the input parameters.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| solution\_ids | string[] | Yes | Array of solution IDs (1-10). IDs start with prodview-. Also accepts legacy solution\_id (single string, auto-converted). | 

**Output:**

```
{
  "solutions": [
    {
      "solution_id": "prodview-abc123",
      "solution_name": "Datadog",
      "solution_description": "Comprehensive monitoring and analytics...",
      "solution_url": "https://aws.amazon.com/marketplace/pp/prodview-abc123?ref_=...",
      "vendor_name": "Datadog, Inc.",
      "vendor_url": "https://aws.amazon.com/marketplace/seller-profile?id=...&ref_=...",
      "highlights": ["Real-time monitoring", "700+ integrations"],
      "reviews_summary": {
        "reviews_count": 245,
        "average_rating": 4.6
      },
      "review_sentiments": [
        {
          "sentiment_category": "functionality",
          "overall_polarity": "positive",
          "positive_score": "85%",
          "negative_score": "5%",
          "mixed_score": "10%",
          "sample_reviews": [
            {
              "review_text": "Excellent monitoring capabilities...",
              "rating": 5,
              "source_name": "G2"
            }
          ]
        }
      ],
      "free_trial_available": true,
      "pricing_options": [
        {
          "name": "Infrastructure Monitoring",
          "description": "$15 per host per month"
        }
      ],
      "fulfillment_options_types": ["SaaS"],
      "categories": ["Monitoring & Observability"],
      "security_certificates": ["SOC 2 Type II", "ISO 27001"],
      "rankings": [{ "category": "Monitoring", "rank": 3 }],
      "has_standard_contract": true,
      "call_to_action": {
        "procurement_url": "https://...",
        "request_for_demo_url": "https://...",
        "request_for_private_offer_url": "https://...",
        "procure_free_trial_url": "https://..."
      }
    }
  ]
}
```

The following table describes the output fields.


| Field | Type | Description | 
| --- | --- | --- | 
| solutions | SolutionOutput[] | Array of solution details (always array, even for single ID). | 

The following table describes the fields in each `SolutionOutput` object.


| Field | Type | Description | 
| --- | --- | --- | 
| solution\_id | string | AWS Marketplace solution ID. | 
| solution\_name | string | Product name. | 
| solution\_description | string | Long or short description. | 
| solution\_url | string | Marketplace URL with ref tags. | 
| vendor\_name | string | Vendor display name. | 
| vendor\_url | string | Vendor profile URL with ref tags. | 
| highlights | string[] | Product highlights. | 
| reviews\_summary | object | { reviews\_count, average\_rating } | 
| review\_sentiments | ReviewSentiment[] | Sentiment by category (functionality, ease\_of\_use, customer\_service, cost\_effectiveness) with polarity scores and sample reviews. | 
| free\_trial\_available | boolean? | Whether a free trial is available. | 
| pricing\_options | PricingOption[] | { name, description } pairs. | 
| fulfillment\_options\_types | string[]? | Fulfillment types such as SaaS, Container, or AMI. | 
| categories | string[]? | Categories such as "Monitoring & Observability". | 
| security\_certificates | string[]? | Certifications such as "SOC 2 Type II" or "ISO 27001". | 
| rankings | Ranking[]? | { category, rank } — rank within category (1-100). | 
| has\_standard\_contract | boolean? | Whether the product supports AWS Standard Contract. | 
| call\_to\_action | CallToAction | { procurement\_url, request\_for\_demo\_url, request\_for\_private\_offer\_url, procure\_free\_trial\_url } | 

### get\_aws\_marketplace\_related\_solutions
<a name="marketplace-mcp-tool-related-solutions"></a>

Performs a direct AWS Marketplace Catalog API call. Returns related solutions for given solution IDs as identified by AWS Marketplace, sorted by relation score (descending), without AI analysis or relevance scoring. Supports batch requests (up to 10 IDs).

**Input:**

```
{
  "solution_ids": ["prodview-abc123"]
}
```

The following table describes the input parameters.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| solution\_ids | string[] | Yes | Array of solution IDs (1-10). Also accepts legacy solution\_id (single string, auto-converted). | 

**Output:**

```
{
  "results": [
    {
      "solution_id": "prodview-abc123",
      "related_solutions": [
        {
          "solution_id": "prodview-xyz789",
          "solution_name": "New Relic",
          "vendor_name": "New Relic, Inc.",
          "vendor_url": "https://aws.amazon.com/marketplace/seller-profile?id=...",
          "solution_description": "Full-stack observability platform...",
          "solution_url": "https://aws.amazon.com/marketplace/pp/prodview-xyz789"
        }
      ]
    }
  ]
}
```

The following table describes the output fields.


| Field | Type | Description | 
| --- | --- | --- | 
| results | SingleRelatedSolutionsResult[] | One entry per input solution ID. | 
| results[].solution\_id | string | The input solution ID. | 
| results[].related\_solutions | MinimalSolutionMetadata[] | Related solutions sorted by relevance. | 

### research\_aws\_marketplace\_solution
<a name="marketplace-mcp-tool-research-solution"></a>

Performs deep web research on AWS Marketplace solutions. Runs web searches for each requested section and returns content with inline citation links. Supports batch requests (up to 5 IDs).

**Visibility:** This tool is hidden from clients with native web search capability (for example, Anthropic/ClaudeAI). Those clients get workflow prompts with embedded search queries instead.

**Input:**

```
{
  "solution_ids": ["prodview-abc123", "prodview-xyz789"],
  "sections": ["features", "integrations"]
}
```

The following table describes the input parameters.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| solution\_ids | string[] | Yes | Array of solution IDs in prodview-\* format (1-5). | 
| sections | ResearchSection[] | No | Sections to research. Default: all 7 sections. | 

The following table describes each available research section.


| Section | What it returns | 
| --- | --- | 
| features | Official documentation, capabilities, specifications | 
| reviews | G2, Gartner, TrustRadius customer feedback | 
| limitations | Known issues, drawbacks, criticisms | 
| competitors | Competitive positioning, alternatives | 
| pricing | Cost information, pricing models, tiers | 
| integrations | AWS ecosystem, APIs, third-party tools | 
| case\_studies | Customer success stories, testimonials, ROI | 

**Output:**

```
{
  "results": [
    {
      "solution_id": "prodview-abc123",
      "solution_name": "Datadog",
      "research": {
        "features": {
          "content": "Datadog provides 700+ integrations...",
          "citations": [
            {
              "index": "1",
              "title": "Datadog Integrations",
              "url": "https://docs.datadoghq.com/integrations/"
            }
          ]
        }
      }
    }
  ]
}
```

The following table describes the output fields.


| Field | Type | Description | 
| --- | --- | --- | 
| results | SingleResearchResult[] | One entry per input solution ID. | 
| results[].solution\_id | string | The researched solution ID. | 
| results[].solution\_name | string | Product name resolved from solution ID. | 
| results[].research | object | Object with keys for each requested section. | 
| results[].research[section].content | string | Research content with inline citation links. | 
| results[].research[section].citations | Citation[] | { index, title, url } for each citation. | 

**Concurrency:** Solutions are researched in parallel. Sections within each solution are sequential to avoid overwhelming downstream services.

### submit\_aws\_marketplace\_feedback
<a name="marketplace-mcp-tool-submit-feedback"></a>

Submits user feedback about an AWS Marketplace report. Call this tool after completing any recommendation, comparison, or evaluation workflow.

**Input:**

```
{
  "sentiment": "negative",
  "categories": ["incomplete", "other"],
  "feedback_text": "Missing pricing details"
}
```

The following table describes the input parameters.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| sentiment | enum | Yes | "positive" or "negative". | 
| categories | string[] | No | For negative feedback: "irrelevant", "incomplete", "inaccurate", "other". | 
| feedback\_text | string | No | Free-form text (max 1000 characters). | 

**Output:**

```
{
  "success": true,
  "message": "Thank you for your feedback. We'll use it to improve."
}
```

## Workflows
<a name="marketplace-mcp-workflows"></a>

The AWS Marketplace MCP server supports three primary workflows for product research and direct catalog lookups.

### Report generation (recommendations, comparisons, evaluations)
<a name="marketplace-mcp-workflow-report-generation"></a>

This is the primary workflow for AI-assisted product research. It uses `get_aws_marketplace_report_guidelines` as the orchestration entry point.

**Flow:**

1. Call `get_aws_marketplace_report_guidelines` with the appropriate `workflow_type`.

1. The tool returns step-by-step workflow instructions and an output format template.

1. The AI assistant follows the returned instructions, which typically involve calling catalog API and research tools to gather data.

1. The assistant generates a formatted report following the output template.

1. After delivering the report, the assistant collects user feedback through `submit_aws_marketplace_feedback`.

**Recommendations workflow:**

1. `get_aws_marketplace_report_guidelines({ workflow_type: "recommendations" })`

1. `search_aws_marketplace_solutions({ queries: ["Product A", "Product B"], max_results: 3 })`

1. Write report following the format template.

1. `submit_aws_marketplace_feedback({ sentiment: "positive" })`

**Comparison workflow:**

1. `get_aws_marketplace_report_guidelines({ workflow_type: "comparison" })`

1. `get_aws_marketplace_solution({ solution_ids: ["prodview-abc", "prodview-xyz"] })`

1. `research_aws_marketplace_solution({ solution_ids: [...], sections: ["features", "integrations"] })`

1. Build comparison matrix and write report following the format template.

1. `submit_aws_marketplace_feedback({ sentiment: "positive" })`

**Evaluation workflow:**

1. `get_aws_marketplace_report_guidelines({ workflow_type: "evaluation" })`

1. `get_aws_marketplace_solution({ solution_ids: ["prodview-target"] })`

1. `research_aws_marketplace_solution({ solution_ids: ["prodview-target"], sections: ["features", "reviews", "limitations", "case_studies"] })`

1. Write evaluation report following the format template.

1. `submit_aws_marketplace_feedback({ sentiment: "positive" })`

### Direct catalog lookup
<a name="marketplace-mcp-workflow-catalog-lookup"></a>

For programmatic integrations or quick lookups that don't require AI analysis, you can call the catalog API tools directly without `get_aws_marketplace_report_guidelines`.

**Search then detail lookup:**

1. Call `search_aws_marketplace_solutions` with one or more keyword queries.

1. Use the returned `solution_id` values to call `get_aws_marketplace_solution` for full details.

1. Optionally call `get_aws_marketplace_related_solutions` to discover related products.

### Feedback collection
<a name="marketplace-mcp-workflow-feedback"></a>

After completing any workflow, the assistant should collect user feedback.

1. Ask the user if the response was helpful.

1. If positive, call `submit_aws_marketplace_feedback` with `sentiment: "positive"`.

1. If negative, ask which categories apply (`irrelevant`, `incomplete`, `inaccurate`, `other`), optionally collect free-text feedback, and submit.

## End-to-end example
<a name="marketplace-mcp-end-to-end-example"></a>

The following example demonstrates a complete recommendations workflow from initial query to feedback submission.

**Step 1 — Get workflow instructions:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_aws_marketplace_report_guidelines",
    "arguments": {
      "workflow_type": "recommendations"
    }
  }
}
```

**Step 2 — Search for candidate solutions:**

```
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "search_aws_marketplace_solutions",
    "arguments": {
      "queries": ["SIEM security monitoring", "log management SIEM"],
      "max_results": 10
    }
  }
}
```

**Step 3 — Retrieve detailed metadata for top candidates:**

```
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "get_aws_marketplace_solution",
    "arguments": {
      "solution_ids": ["prodview-abc123", "prodview-def456", "prodview-ghi789"]
    }
  }
}
```

**Step 4 — Submit user feedback:**

```
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "submit_aws_marketplace_feedback",
    "arguments": {
      "sentiment": "positive",
      "feedback_text": "Recommendations were relevant and well-structured"
    }
  }
}
```

## Error handling
<a name="marketplace-mcp-error-handling"></a>

Errors fall into three categories: protocol errors, tool execution errors, and validation errors.

### Protocol errors
<a name="marketplace-mcp-protocol-errors"></a>

Protocol errors are returned when the request violates the JSON-RPC or MCP specification (for example, malformed JSON, missing required fields, or unknown methods).

```
{
  "jsonrpc": "2.0",
  "id": 10,
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": {
      "details": "Missing required field: queries"
    }
  }
}
```

### Tool execution errors
<a name="marketplace-mcp-tool-execution-errors"></a>

Tool execution errors are returned when a tool invocation fails at runtime (for example, rate limiting, invalid solution IDs, or upstream service errors). Tool errors are reported within the result object, not as MCP protocol-level errors, so the AI assistant can see and handle the error.

```
{
  "jsonrpc": "2.0",
  "id": 11,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Failed to search listings: Rate limit exceeded"
      }
    ],
    "isError": true
  }
}
```

### Validation errors
<a name="marketplace-mcp-validation-errors"></a>

Validation errors are returned when input fails schema validation (for example, invalid solution ID format, exceeding max array length, or missing required fields). These are surfaced as tool execution errors with `isError: true`.