

# AgentCore Web Search request and response

This page describes the fields of an `InvokeWebSearch` request, the rules that the API applies to them, and the response.

## Request fields
<a name="web-search-api-request"></a>

You call the API on the Amazon Bedrock AgentCore data plane endpoint, for example `bedrock-agentcore.us-east-1.amazonaws.com`. The AWS SDKs and the AWS Command Line Interface (AWS CLI) sign each request for you with AWS Signature Version 4 (SigV4) for the service name `bedrock-agentcore`.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `webSearchId`  | string | Yes | The identifier of the web search tool to invoke. The AWS managed web search tool is `web-search.v1`. The request sends this value in the URI path. | 
|  `searchQuery`  | string | Yes | The text to search for. The text must be 1–200 characters long. | 
|  `maxResults`  | integer | No | The maximum number of results to return, from 1 to 25. If you don’t specify a value, the API returns up to 25 results. | 
|  `filters`  | object | No | The filters that narrow the results. The object can contain `domainFilter`, `publishedDateFilter`, or both. | 
|  `filters.domainFilter.include`  | array of strings | No | The domains to return results from. The API doesn’t return results from other domains. The list holds 1–100 domain names. | 
|  `filters.domainFilter.exclude`  | array of strings | No | The domains that the API never returns results from. The list holds 1–100 domain names. | 
|  `filters.publishedDateFilter.publishedAfter`  | timestamp | No | The start of the publication time range, inclusive. The API returns only results published at or after this time. For example, `2026-01-01T00:00:00Z`. | 
|  `filters.publishedDateFilter.publishedBefore`  | timestamp | No | The end of the publication time range, inclusive. The API returns only results published at or before this time. For example, `2026-01-31T23:59:59Z`. | 

The API applies the following rules to the request:
+  **Domain names** – Specify a domain name only, such as `example.net`, without a scheme or a path. A root domain also matches its subdomains. For example, `example.net` also matches `docs.example.net`. You can specify `include`, `exclude`, or both. Each domain name can be up to 253 characters long.
+  **Publication times** – Each value is a timestamp. The AWS SDKs and the AWS CLI send it as a date-time in Coordinated Universal Time (UTC), for example `2026-01-01T00:00:00Z`. If you pass a date without a time, such as `2026-01-01` to the AWS CLI, it means midnight UTC at the start of that day. To include a whole day in `publishedBefore`, use the last second of that day, for example `2026-01-31T23:59:59Z`. You can specify `publishedAfter`, `publishedBefore`, or both. If `publishedAfter` is later than `publishedBefore`, the request fails with a `ValidationException`.
+  **Other fields** – The request body can contain only `searchQuery`, `maxResults`, and `filters`. The API rejects a request that contains any other top-level field with a `ValidationException`.
+  **Body size** – The request body can be up to 32 KiB.

## Response
<a name="web-search-api-response"></a>

The response contains a `results` array with the search results, in ranked order. The API doesn’t paginate. It returns up to `maxResults` results in a single response, and it can return fewer.

Each result contains the following fields:


| Field | Type | Always present | Description | 
| --- | --- | --- | --- | 
|  `text`  | string | Yes | A text extract from the page. | 
|  `title`  | string | No | The title of the page. | 
|  `url`  | string | No | The URL of the page. | 
|  `publishedAt`  | timestamp | No | The time the page was published. The API omits this field when the publication time isn’t known. | 

The following example shows a response body with one result:

```json
{
    "results": [
        {
            "title": "Release highlights",
            "url": "https://docs.example.net/releases/highlights",
            "text": "The January release adds support for scheduled reports and improves search performance...",
            "publishedAt": "2026-01-15T17:00:00Z"
        }
    ]
}
```

For the errors that the API returns, see [Troubleshoot AgentCore Web Search](web-search-api-troubleshooting.md#web-search-api-errors).