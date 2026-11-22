

# AWS Marketplace as Connector Target

 [AWS Marketplace](https://aws.amazon.com/marketplace/) is a digital catalog of software, data, and services from third-party sellers, including APIs and agents that other agents can call and pay for.

Amazon Bedrock AgentCore Gateway includes a built-in AWS Marketplace connector for agentic commerce. You add a gateway target that uses the connector, and your agents can then search AWS Marketplace for products they can pay for with the x402 payment protocol, read listing details, and get a product’s callable endpoint and payment details through the Model Context Protocol (MCP). The gateway creates the tool schemas and authenticates to AWS Marketplace with the gateway service role. You don’t write a Lambda function or an MCP server, and you don’t define the tools yourself.

The connector exposes three read-only operations:
+  `SearchListings` — Searches AWS Marketplace and returns ranked x402-enabled listings. Each listing carries a `listingId` and a `productId`.
+  `GetListing` — Returns detail about one listing, such as its description, categories, pricing summaries, reviews, and associated products and offers.
+  `ListFulfillmentOptions` — Returns a product’s fulfillment options, including the callable endpoint URL and its payment protocol details.

The following sections walk through the key capabilities, how the connector works, common use cases, how to set up a target, and the tool schemas and responses.

**Topics**
+ [Key capabilities](#gateway-target-connector-aws-marketplace-key-capabilities)
+ [How it works](#gateway-target-connector-aws-marketplace-how-it-works)
+ [Use cases](#gateway-target-connector-aws-marketplace-use-cases)
+ [Set up an AWS Marketplace target](#gateway-target-connector-aws-marketplace-setup)
+ [Use with a harness](#gateway-target-connector-aws-marketplace-harness)
+ [Configure the Gateway Service Role](#gateway-target-connector-aws-marketplace-service-role)
+ [Invoke the tools](#gateway-target-connector-aws-marketplace-invoke)
+ [Input schemas](#gateway-target-connector-aws-marketplace-input-schema)
+ [Response format](#gateway-target-connector-aws-marketplace-response-format)
+ [Availability](#gateway-target-connector-aws-marketplace-availability)

## Key capabilities
<a name="gateway-target-connector-aws-marketplace-key-capabilities"></a>
+  **x402-only search results** — `SearchListings` returns only x402-enabled AWS Marketplace listings, so every product your agent finds by searching is one it can pay for per request.
+  **Search to endpoint in a few tool calls** — Your agent goes from a plain-language search to a callable endpoint URL and its payment details with `SearchListings` and `ListFulfillmentOptions`, plus an optional `GetListing`.
+  **Zero integration code** — No AWS Marketplace API client, request signing, or response parsing to build. The Gateway exposes the operations as standard MCP tools.
+  **Framework agnostic** — Works with Strands Agents, LangChain, LangGraph, CrewAI, or any MCP-compatible client through the standard Model Context Protocol.
+  **Read-only and scoped by IAM** — All three operations are read-only. The Gateway service role controls which operations the target can call.

## How it works
<a name="gateway-target-connector-aws-marketplace-how-it-works"></a>

The AWS Marketplace connector is a built-in **connector**. The Gateway handles schema management, parameter governance, endpoint resolution, and service authentication. A typical flow works as follows:

1.  **Gateway setup** — Create a Gateway and add an AWS Marketplace target using `connectorId: "aws-marketplace"`. In `configurations`, choose which operations become tools. The Gateway snapshots the tool schemas and provisions the integration.

1.  **Tool discovery** — Your agent calls `tools/list` on the Gateway endpoint and discovers one tool for each configured operation.

1.  **Search** — Your agent calls `SearchListings` with a description of what it needs, for example `"web search API"`. The Gateway authenticates to AWS Marketplace with the Gateway service role and returns ranked x402-enabled listings.

1.  **Optional detail** — To get more detail about a listing before choosing it, your agent calls `GetListing` with a `listingId`.

1.  **Endpoint** — Your agent calls `ListFulfillmentOptions` with the chosen `productId` and gets back the endpoint URL to call and its payment details.

1.  **Pay** — Your agent calls the endpoint, receives the HTTP 402 payment challenge, and pays it with AgentCore payments.

## Use cases
<a name="gateway-target-connector-aws-marketplace-use-cases"></a>
+  **Agentic commerce** — Let an agent find a third-party API or agent for a task, such as web search or data enrichment, get its endpoint and payment details, and pay for and call it per request.
+  **Tool discovery at run time** — Instead of hard-coding every third-party integration, let an agent look up a suitable product in AWS Marketplace when it needs one.
+  **Shopping and research assistants** — Answer questions such as "Which web search APIs can my agent pay for per request?" with current AWS Marketplace listings.

## Set up an AWS Marketplace target
<a name="gateway-target-connector-aws-marketplace-setup"></a>

For setup examples that use Boto3 and the AWS CLI, see [Set up an AWS Marketplace target](gateway-add-target-api-target-config.md#gateway-add-target-api-connector-aws-marketplace-setup).

## Use with a harness
<a name="gateway-target-connector-aws-marketplace-harness"></a>

To give an [AgentCore harness](harness.md) access to AWS Marketplace, attach the gateway that you created in Set up an AWS Marketplace target to the harness as an `agentcore_gateway` tool. The harness execution role requires the `bedrock-agentcore:InvokeGateway` permission on the gateway ARN. For the end-to-end walkthrough, see [Tools](harness-tools.md) in the harness documentation.

## Configure the Gateway Service Role
<a name="gateway-target-connector-aws-marketplace-service-role"></a>

The Gateway needs a service role that allows the AgentCore service to call AWS Marketplace on your behalf. For the required IAM permissions, see [Configure the Gateway Service Role](gateway-add-target-api-target-config.md#gateway-add-target-api-connector-aws-marketplace-service-role) in the target configuration guide.

## Invoke the tools
<a name="gateway-target-connector-aws-marketplace-invoke"></a>

After you create the target, your agent discovers the tools with `tools/list` and calls them with `tools/call`. Each tool name is prefixed with the target name, in the form `<target-name>_<operation>_SearchListings`).

The following JSON-RPC request searches AWS Marketplace:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "marketplace___SearchListings",
    "arguments": {
      "searchText": "web search API",
      "maxResults": 5
    }
  }
}
```

The following JSON-RPC request gets detail about one of the returned listings:

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "marketplace___GetListing",
    "arguments": {
      "listingId": "prodview-EXAMPLE1234567"
    }
  }
}
```

The following JSON-RPC request gets the endpoint and payment details for the product that the agent chose:

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "marketplace___ListFulfillmentOptions",
    "arguments": {
      "productId": "prod-EXAMPLE1234567",
      "maxResults": 10
    }
  }
}
```

## Input schemas
<a name="gateway-target-connector-aws-marketplace-input-schema"></a>

Each tool accepts the following input schema when invoked through `tools/call`.

 `SearchListings`:

```json
{
  "inputSchema": {
    "type": "object",
    "properties": {
      "searchText": {
        "description": "Plain-language description of the product to find, for example \"translation API\" or \"web scraping API\". 1-512 characters.",
        "type": "string"
      },
      "maxResults": {
        "description": "Maximum number of listings to return. Valid range: 1-100. Defaults to 25.",
        "type": "integer"
      },
      "nextToken": {
        "description": "Token from a previous SearchListings response. Pass it to get the next page of results.",
        "type": "string"
      }
    }
  }
}
```

 `GetListing`:

```json
{
  "inputSchema": {
    "type": "object",
    "properties": {
      "listingId": {
        "description": "Listing identifier from a SearchListings result (listingSummaries[].listingId), for example prodview-abc123example.",
        "type": "string"
      }
    },
    "required": [
      "listingId"
    ]
  }
}
```

 `ListFulfillmentOptions`:

```json
{
  "inputSchema": {
    "type": "object",
    "properties": {
      "productId": {
        "description": "Product identifier from a SearchListings result (listingSummaries[].associatedEntities[].product.productId), for example prod-abc123example.",
        "type": "string"
      },
      "maxResults": {
        "description": "Maximum number of fulfillment options to return. Valid range: 1-50.",
        "type": "integer"
      },
      "nextToken": {
        "description": "Token from a previous ListFulfillmentOptions response. Pass it to get the next page of results.",
        "type": "string"
      }
    },
    "required": [
      "productId"
    ]
  }
}
```

The following table applies to connector version `1.0.0`.


| Operation | Default fields | Fields you can expose | Notes | 
| --- | --- | --- | --- | 
|  `SearchListings`  |  `searchText`, `maxResults`, `nextToken`  |  `sortBy`, `sortOrder`  | Returns only x402-enabled listings, ranked. Each listing carries a `listingId` for `GetListing` and a `productId` for `ListFulfillmentOptions`. `searchText` is 1–512 characters. `maxResults` is 1–100 and defaults to 25. | 
|  `GetListing`  |  `listingId` (required) | None | Optional enrichment step before `ListFulfillmentOptions`. | 
|  `ListFulfillmentOptions`  |  `productId` (required), `maxResults`, `nextToken`  | None | Returns the callable endpoint URL and its payment details. `maxResults` is 1–50. | 

The schema returned by `tools/list` for each tool is the set of fields the agent can set. By default, each tool shows only the fields in the **Default fields** column. To let the agent set a field from the **Fields you can expose** column, add it to `parameterOverrides` on that operation’s configuration entry with `visible` set to `true`. The `parameterOverrides` format is the same as for other connectors. For details, see [Control which parameters the agent can set](gateway-add-target-api-target-config.md#gateway-add-target-api-connector-managed-kb-parameters).

## Response format
<a name="gateway-target-connector-aws-marketplace-response-format"></a>

Each tool returns an MCP `tools/call` result. The `text` field contains the serialized AWS Marketplace API response as JSON.

The following example shows a `SearchListings` result, shortened to one listing:

```json
{
  "isError": false,
  "content": [
    {
      "type": "text",
      "text": "{\"totalResults\":42,\"nextToken\":\"eyJ2ZXJzaW9uIjoi...\",\"listingSummaries\":[{\"listingId\":\"prodview-EXAMPLE1234567\",\"listingName\":\"Example Web Search API\",\"shortDescription\":\"Real-time web search results with source URLs and snippets, paid per request with x402.\",\"catalog\":\"AWSMarketplace\",\"publisher\":{\"displayName\":\"Example Seller\",\"sellerProfileId\":\"seller-EXAMPLE12345\"},\"associatedEntities\":[{\"product\":{\"productId\":\"prod-EXAMPLE1234567\",\"productName\":\"Example Web Search API\"}}],\"categories\":[{\"displayName\":\"AI Agents\"}],\"pricingModels\":[{\"pricingModelType\":\"USAGE\",\"displayName\":\"Usage\"}]}]}"
    }
  ]
}
```

The following table describes the `SearchListings` response fields that your agent passes to the next call:


| Field | Type | Description | 
| --- | --- | --- | 
|  `totalResults`  | integer | Number of matching listings. | 
|  `nextToken`  | string | Pass to the next `SearchListings` call to get the next page. Absent on the last page. | 
|  `listingSummaries[].listingId`  | string | Listing identifier. Pass to `GetListing`. | 
|  `listingSummaries[].listingName`  | string | Listing name. | 
|  `listingSummaries[].shortDescription`  | string | One-line description supplied by the seller. | 
|  `listingSummaries[].publisher.displayName`  | string | Seller name. | 
|  `listingSummaries[].associatedEntities[].product.productId`  | string | Product identifier. Pass to `ListFulfillmentOptions`. | 
|  `listingSummaries[].pricingModels`  | list | Pricing models, such as `USAGE`. | 

 `ListFulfillmentOptions` returns `fulfillmentOptions`, a list. Each entry is an `apiFulfillmentOption` with the following fields:


| Field | Type | Description | 
| --- | --- | --- | 
|  `endpoints[].endpointUrl`  | string | URL your agent calls. | 
|  `endpoints[].authorizationTypes`  | list | How the endpoint authorizes calls, for example `PAYMENT_TOKEN`. | 
|  `endpoints[].integrationProtocols`  | list | Protocol the endpoint speaks, such as `MCP` or `A2A`, with the seller’s `usageInstructions`. | 
|  `endpoints[].schemas`  | list | Links to the endpoint’s `OPEN_API` or `SMITHY_AST` schema, when the seller provides one. | 
|  `endpoints[].estimatedCostDescription`  | string | Seller’s description of the cost per call. | 
|  `accessModels[].agenticCommerce.paymentProtocols`  | list | Supported payment protocols. | 
|  `usageInstructions`  | string | Seller’s instructions for calling the product. | 

When the call fails, the result has `isError` set to `true` and the `text` field describes the error.

## Availability
<a name="gateway-target-connector-aws-marketplace-availability"></a>

The AWS Marketplace connector is available in all commercial AWS Regions where Amazon Bedrock AgentCore Gateway is available.

AgentCore payments is available in fewer Regions. To pay for a product that your agent finds, call AgentCore payments in a Region where it’s available and where you created your payment manager, and set that Region explicitly in your agent code. If you don’t set it, the SDK uses your agent’s default Region, for example the AgentCore Runtime Region, and the payment fails if your payment manager isn’t in that Region. For the Regions that each AgentCore service supports, see [Supported AWS Regions](agentcore-regions.md).