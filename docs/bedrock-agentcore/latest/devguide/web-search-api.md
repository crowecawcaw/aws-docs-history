

# Search the web using Amazon Bedrock AgentCore Web Search
<a name="web-search-api"></a>

Amazon Bedrock AgentCore Web Search lets you search the web from your own code with the `InvokeWebSearch` API. The API returns a ranked list of results. Each result includes a text extract from the page and, when they are available, the page title, URL, and publication time. You call the API with the AWS SDKs or the AWS Command Line Interface (AWS CLI), and you authorize calls with AWS Identity and Access Management (IAM). You don’t create or manage any resources to use it.

Use AgentCore Web Search to give an application, an agent loop that you write yourself, or a data pipeline access to current information from the web. For example, you can look up recent announcements about a product, collect sources for a research question, or check a claim against pages from domains that you trust. To narrow the results, you can filter them by domain and by publication time.

**Topics**
+ [Choose between the API and the Gateway connector](#web-search-api-choose)
+ [Regions](#web-search-api-regions)
+ [Quotas](#web-search-api-quotas)
+ [Acceptable use](#web-search-api-acceptable-use)
+ [Get started with AgentCore Web Search](web-search-api-get-started.md)
+ [AgentCore Web Search request and response](web-search-api-reference.md)
+ [Call AgentCore Web Search through AWS PrivateLink](web-search-api-privatelink.md)
+ [Log AgentCore Web Search API calls with AWS CloudTrail](web-search-api-cloudtrail.md)
+ [Troubleshoot AgentCore Web Search](web-search-api-troubleshooting.md)

## Choose between the API and the Gateway connector
<a name="web-search-api-choose"></a>

You can also search the web through the Web Search Tool connector, which you add as a target to an AgentCore gateway. Use the `InvokeWebSearch` API when your code, rather than a Model Context Protocol (MCP) client, consumes the results. Use the connector when your agents discover and call tools over MCP. For more information about the connector, see [Web Search Tool](gateway-target-connector-web-search-tool.md).

The two differ in the following ways:
+  **How you call it** – Your code calls the API on the Amazon Bedrock AgentCore data plane endpoint. Agents call the connector as an MCP tool through a gateway.
+  **Authorization** – The API authorizes callers with IAM only. A gateway can also authorize callers with a JSON Web Token (JWT).
+  **Domain lists** – With the API, each request carries its own domain filter. The connector can also apply target-level domain lists to every request, without the calling agent seeing them.
+  **Search text** – The API takes the search text in `searchQuery`. The MCP tool takes it in `query`.
+  **Default number of results** – If you don’t set `maxResults`, the API returns up to 25 results and the MCP tool returns up to 10.
+  **Publication time range** – The API bounds the range with `publishedAfter` and `publishedBefore`. The MCP tool bounds it with `from` and `to`. Both treat both bounds as inclusive.
+  **Dates without a time** – The MCP tool’s `to` date includes that whole day. The AWS SDKs and the AWS CLI send a `publishedBefore` date as midnight Coordinated Universal Time (UTC) at the start of that day.
+  **Regions** – The connector is also available in AWS GovCloud (US-West). The API isn’t.

## Regions
<a name="web-search-api-regions"></a>

AgentCore Web Search is available in the following AWS Regions:
+ US East (N. Virginia) `us-east-1` 
+ US East (Ohio) `us-east-2` 
+ US West (Oregon) `us-west-2` 
+ Asia Pacific (Sydney) `ap-southeast-2` 
+ Asia Pacific (Tokyo) `ap-northeast-1` 
+ Europe (Ireland) `eu-west-1` 

AgentCore Web Search isn’t available in AWS GovCloud (US-West). In that Region, use the Web Search Tool connector. For the availability of other features, see [Supported AWS Regions](agentcore-regions.md).

## Quotas
<a name="web-search-api-quotas"></a>

By default, each account can send up to 10 `InvokeWebSearch` requests per second in each Region. You can request an increase to this quota for each Region. To request an increase, contact AWS Support. For more information about the quota, see [AgentCore Web Search Service Quotas](bedrock-agentcore-limits.md#web-search-service-limits).

## Acceptable use
<a name="web-search-api-acceptable-use"></a>

If you use Web Search, you are responsible for your use, and any use by your end users, of content retrieved from Web Search ("Search Results"). You must retain and display the source citations and links provided with each Search Result in any output you surface to your end users that uses the Search Result. You may not use Web Search to (a) extract, store, or reproduce content from Search Results in bulk, or (b) build or populate a competing index or database.