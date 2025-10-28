# Choose an API key source in API Gateway

When you associate a usage plan with an API and enable API keys on API methods, every
incoming request to the API must contain an [API key](api-gateway-basic-concept.md#apigateway-definition-api-key "api-gateway-basic-concept.md#apigateway-definition-api-key"). API Gateway reads the key and
compares it against the keys in the usage plan. If there is a match, API Gateway throttles the
requests based on the plan's request limit and quota. Otherwise, it throws an
`InvalidKeyParameter` exception. As a result, the caller receives a
`403 Forbidden` response.

Your API Gateway API can receive API keys from one of two sources:

**`HEADER`**

You distribute API keys to your customers and require them to pass the API
key as the `X-API-Key` header of each incoming request.

**`AUTHORIZER`**

You have a Lambda authorizer return the API key as part of the
authorization response. For more information on the authorization response,
see [Output from an API Gateway Lambda authorizer](api-gateway-lambda-authorizer-output.md "api-gateway-lambda-authorizer-output.md").

###### Note

For best practices to consider, see [Best practices for API keys and usage plans](api-gateway-api-usage-plans.md#apigateway-usage-plans-best-practices "api-gateway-api-usage-plans.md#apigateway-usage-plans-best-practices").

The following procedure shows how to choose an API key source for an API.

AWS Management Console###### To choose an API key source for an API

1. Sign in to the API Gateway console.
2. Choose an existing API or create a new one.
3. In the main navigation pane, choose **API settings**.
4. In the **API details** section, choose **Edit**.
5. Under
   **API key source**, select `Header` or
   `Authorizer` from the dropdown list.
6. Choose **Save changes**.

AWS CLIThe following [update-rest-api](../../../cli/latest/reference/apigateway/update-rest-api.md "../../../cli/latest/reference/apigateway/update-rest-api.md") command
updates an API to set the API key source to `AUTHORIZER`:

```
aws apigateway update-rest-api --rest-api-id 1234123412 --patch-operations op=replace,path=/apiKeySource,value=AUTHORIZER
```

To have the client submit an API key, set the `value` to
`HEADER` in the previous command.

REST APITo choose an API key source for an API by using the API Gateway REST API, call [`restapi:update`](../api/API_UpdateRestApi.md "../api/API_UpdateRestApi.md")
as follows:

```
PATCH /restapis/fugvjdxtri/ HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160603T205348Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160603/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "patchOperations" : [
    {
        "op" : "replace",
        "path" : "/apiKeySource",
        "value" : "HEADER"
    }
  ]
}
```

To have an authorizer return an API key, set the `value` to
`AUTHORIZER` in the previous `patchOperations` input.
