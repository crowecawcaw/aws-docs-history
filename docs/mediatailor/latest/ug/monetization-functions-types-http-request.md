

# HTTP request
<a name="monetization-functions-types-http-request"></a>

## When to use
<a name="monetization-functions-types-http-request-when"></a>

Use `HTTP_REQUEST` when your function needs to call an external service. Common use cases include fetching identity data from a resolution provider, retrieving audience segments from a data management platform, and sending session information to a logging endpoint.

## Configuration fields
<a name="monetization-functions-types-http-request-fields"></a>

An `HTTP_REQUEST` function has the following fields:
+ **Runtime** — The expression language. Set this to `JSONATA`.
+ **MethodType** — The HTTP method. Supported values are `GET` and `POST`.
+ **Url** — The URL to send the request to. You can use a static URL or a JSONata expression that builds the URL dynamically.
+ **Headers** — The HTTP headers to include in the request, specified as header name and value pairs. Use `{%...%}` expression syntax for dynamic header values. Static values can be specified directly as strings.
+ **Body** — The request body to send. Used with `POST` requests. You can use a JSONata expression to build the body dynamically.
+ **RequestTimeoutMilliseconds** (required) — How long to wait for a response.
+ **Output** — Defines the values to produce after the HTTP call completes. Each entry maps an output key (such as `player_params.envelope_id`) to an expression that can reference the `response` object.

For size limits and restrictions that apply to these fields, see [Limits](monetization-functions-limits.md).

## How the request is processed
<a name="monetization-functions-types-http-request-phases"></a>

MediaTailor processes an `HTTP_REQUEST` function in two steps:

1. **Build the request** — MediaTailor evaluates the `Url`, `Headers`, and `Body` expressions against the current session state. These evaluated values form the outbound HTTP request.

1. **Process the response** — After the HTTP call completes, MediaTailor evaluates the expressions in the output block. These expressions can reference both the original session state and the `response` object returned by the call.

## Response fields
<a name="monetization-functions-types-http-request-response"></a>

After the HTTP call completes, you can reference the following fields in your Output expressions:


| Field | Type | Description | 
| --- | --- | --- | 
| response.body | Object or Array | The response body parsed as JSON. Set to null if the body exceeds 20,000 characters or is not valid JSON. | 
| response.statusCode | Integer | The HTTP status code returned by the external service. Set to null on network failure. | 
| response.text | String | The raw response body as a string, truncated to 20,000 characters. Set to "Internal Error" on network failure. | 

**Important**  
The `response.body` field is `null` when the response exceeds 20,000 characters, even if the response is valid JSON.

**Note**  
The response object is available only in the Output block of an `HTTP_REQUEST` function. You cannot reference response fields in the Url, Headers, or Body fields. In a `SEQUENTIAL_EXECUTOR`, each `HTTP_REQUEST` function can access only its own response.

A value of `null` means the data is not available. This happens when the HTTP call fails (network error or timeout) or when the response body exceeds 20,000 characters or is not valid JSON.

## Network failure behavior
<a name="monetization-functions-types-http-request-failure"></a>

If the HTTP call fails due to a network error or timeout, `response.statusCode` and `response.body` are set to `null`, and `response.text` is set to `"Internal Error"`. Your Output expressions still run, so always check `response.statusCode` before using response data.

**Tip**  
Use a conditional expression to handle failures gracefully: `{%response.statusCode = 200 ? response.body.value : 'default'%}`

## Example: Fetch identity data
<a name="monetization-functions-types-http-request-example"></a>

The following function calls an identity resolution API at session start and stores the result in player parameters. It is designed for the `PRE_SESSION_INITIALIZATION` lifecycle hook.

```
{
    "FunctionId": "fetchIdentityEnvelope",
    "FunctionType": "HTTP_REQUEST",
    "HttpRequestConfiguration": {
        "Runtime": "JSONATA",
        "MethodType": "GET",
        "Url": "{%'https://identity.example.com/v1/resolve?ip=' & $encodeUrlComponent(session.client_ip)%}",
        "Headers": {
            "Authorization": "{%'Bearer my_api_token'%}",
            "Accept": "application/json"
        },
        "RequestTimeoutMilliseconds": 2000,
        "Output": {
            "player_params.identity_envelope": "{%response.statusCode = 200 ? response.body.envelope : ''%}"
        }
    }
}
```

For a complete walkthrough of a similar example, see [Function examples](monetization-functions-examples.md).