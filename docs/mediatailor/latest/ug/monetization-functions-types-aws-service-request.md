

# AWS service request
<a name="monetization-functions-types-aws-service-request"></a>

## When to use
<a name="monetization-functions-types-aws-service-request-when"></a>

With `AWS_SERVICE_REQUEST`, you can call supported AWS service APIs during manifest personalization. You can currently call Elemental Inference GetMetadata for contextual ad targeting.

MediaTailor signs the request with its own service credentials and adds the required authentication and security headers automatically. You do not need to configure IAM roles or manage credentials.

For a guided walkthrough that includes prerequisites, resource policies, and regional considerations, see [Elemental Inference integration](monetization-functions-elemental-inference-integration.md).

## Configuration fields
<a name="monetization-functions-types-aws-service-request-fields"></a>

An `AWS_SERVICE_REQUEST` function has the following fields:
+ **Runtime** (required) — The expression language. Set this to `JSONATA`.
+ **TargetService** (required) — The target AWS service. Currently only `elemental-inference` is supported.
+ **TargetRegion** (required) — The AWS Region for the target service. You can use a static value (for example, `us-west-2`) or a JSONata expression for dynamic resolution (for example, `{%inference.region%}`).
+ **MethodType** (required) — The HTTP method. Supported values are `GET` and `POST`, depending on the target service API.
+ **Url** (required) — The HTTPS endpoint for the AWS service API. Must be a valid AWS endpoint URL. You can use a JSONata expression to build the URL dynamically.
+ **Headers** (optional) — Additional HTTP headers to include in the request. For header restrictions, see [Security model](#monetization-functions-types-aws-service-request-security).
+ **Body** (conditional) — The request body. Required when `MethodType` is `POST`. You can use a JSONata expression to build the body dynamically from session state.
+ **RequestTimeoutMilliseconds** (required) — How long to wait for a response.
+ **Output** (optional) — Defines the values to produce after the call completes. Each entry maps an output key to an expression that can reference the `response` object. Output expressions can reference the same `response` object described in [Response fields](monetization-functions-types-http-request.md#monetization-functions-types-http-request-response).

## Security model
<a name="monetization-functions-types-aws-service-request-security"></a>

MediaTailor signs the outbound request using its own service role. You do not need to create or configure IAM roles for MediaTailor to call the target service.

The target AWS resource must have a resource policy that grants the MediaTailor service principal access with `aws:SourceAccount` and `aws:SourceArn` conditions. These conditions provide cross-service access protection by ensuring that MediaTailor can access the resource only on behalf of your account and specific playback configurations. For complete resource policy examples, see [Grant MediaTailor access to your Elemental Inference feed](monetization-functions-elemental-inference-integration.md#monetization-functions-elemental-inference-integration-access).

**Header restrictions:** All headers with the `X-Amz-` prefix are reserved. MediaTailor overwrites these headers with the required authentication and cross-service access protection values. Do not include `X-Amz-` headers in your configuration.

## How the request is processed
<a name="monetization-functions-types-aws-service-request-phases"></a>

MediaTailor processes an `AWS_SERVICE_REQUEST` function in three steps:

1. **Build the request** — MediaTailor evaluates the `Url`, `Headers`, and `Body` expressions against the current session state. The URL must be a valid endpoint for the specified service.

1. **Sign the request** — MediaTailor authenticates the request using its own service credentials for the specified `TargetService` and `TargetRegion`.

1. **Process the response** — After the call completes, MediaTailor evaluates the expressions in the Output block. These expressions can reference both the original session state and the `response` object returned by the call.

## Response fields
<a name="monetization-functions-types-aws-service-request-response"></a>

After the call completes, you can reference the following fields in your Output expressions:


| Field | Type | Description | 
| --- | --- | --- | 
| response.body | Object or Array | The response body parsed as JSON. Set to null if the body exceeds 20,000 characters or is not valid JSON. | 
| response.statusCode | Integer | The HTTP status code returned by the AWS service. Set to null on network failure. | 
| response.text | String | The raw response body as a string, truncated to 20,000 characters. Set to "Internal Error" on network failure. | 

**Important**  
The maximum response size is 20,000 characters. Responses that exceed this limit result in `response.body` being set to `null`.

## Error handling
<a name="monetization-functions-types-aws-service-request-errors"></a>

The following describes how MediaTailor handles errors for `AWS_SERVICE_REQUEST` functions:
+ If the request times out (exceeds `RequestTimeoutMilliseconds`), `response.statusCode` is `null` and `response.body` is `null`. Your Output expressions still run.
+ If the target service returns a 4xx or 5xx error, `response.statusCode` contains the HTTP status code and `response.body` contains the error response (if valid JSON and under 20,000 characters).
+ If the response body exceeds 20,000 characters, `response.body` is `null` even if the response was successful. Use `response.text` for the raw truncated content.
+ When a function fails or produces empty output, MediaTailor proceeds with ad insertion using the values available without the function's contribution. The ad break is not blocked.

**Tip**  
Always check `response.statusCode` in your Output expressions to handle errors gracefully.

## Example: Elemental Inference GetMetadata
<a name="monetization-functions-types-aws-service-request-example"></a>

The following function calls Elemental Inference `GetMetadata` to retrieve contextual metadata for the content window around the current ad break. The `Body` field uses a JSONata expression to construct the request JSON dynamically from `inference.*` variables. It extracts IAB taxonomy categories and GARM brand safety signals, then stores them as player parameters for use in ADS requests.

```
{
    "FunctionId": "eiContextualMetadata",
    "FunctionType": "AWS_SERVICE_REQUEST",
    "AwsServiceRequestConfiguration": {
        "Runtime": "JSONATA",
        "TargetService": "elemental-inference",
        "TargetRegion": "{%inference.region%}",
        "MethodType": "POST",
        "Url": "{%inference.dataEndpoint & '/v1/feed/' & inference.feedId & '/input/0/metadata'%}",
        "Headers": {
            "Content-Type": "application/json"
        },
        "Body": "{%'{\"outputName\": \"my-contextual-output\", \"timeSpecification\": {\"ptsBased\": {\"startPts\": ' & $string(($exists(inference.previousBreakEndPts) and inference.previousBreakEndPts > inference.pts - 30 * inference.timescale ? inference.previousBreakEndPts : inference.pts - 30 * inference.timescale)) & ', \"endPts\": ' & $string(inference.pts + 1) & ', \"timescale\": ' & $string(inference.timescale) & '}}, \"parameters\": {\"contextualMetadata\": {}}}' %}",
        "RequestTimeoutMilliseconds": 2000,
        "Output": {
            "player_params.iabCategories": "{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.iabTaxonomy.categories.uniqueId), ',') : ''%}",
            "player_params.garmExcluded": "{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.garm.suitability.categories[flagged = true].category), ',') : ''%}"
        }
    }
}
```

At runtime, the `Body` expression produces a JSON payload like the following:

```
{
    "outputName": "my-contextual-output",
    "timeSpecification": {
        "ptsBased": {
            "startPts": 162000000,
            "endPts": 163600001,
            "timescale": 90000
        }
    },
    "parameters": {
        "contextualMetadata": {}
    }
}
```

The `startPts` value is the later of: the end of the previous ad break (`inference.previousBreakEndPts`) or 30 seconds before the current break. The `endPts` value is the current break's PTS plus one.

**Note**  
Replace `my-contextual-output` with the name of your Elemental Inference feed's contextual metadata output.

**Note**  
MediaTailor automatically includes the `x-amzn-elemental-inference-skip-poll` header on requests to Elemental Inference. This ensures low-latency responses suitable for ad break timing.

For a complete setup guide including prerequisites and resource policies, see [Elemental Inference integration](monetization-functions-elemental-inference-integration.md).