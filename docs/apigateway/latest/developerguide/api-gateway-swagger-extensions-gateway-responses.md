# x-amazon-apigateway-gateway-responses object

Defines the gateway responses for an API as a string-to-[GatewayResponse](../api/API_GatewayResponse.md "../api/API_GatewayResponse.md") map of key-value pairs. The extension applies to the root-level OpenAPI structure.

| Property name  | Type                                                                                                                                                               | Description                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| `responseType` | [x-amazon-apigateway-gateway-responses.gatewayResponse](api-gateway-swagger-extensions-gateway-responses.md "api-gateway-swagger-extensions-gateway-responses.md") | A `GatewayResponse` for the specified `responseType`. |

## x-amazon-apigateway-gateway-responses example

The following API Gateway extension to OpenAPI example defines a [GatewayResponses](../api/API_GetGatewayResponses.md "../api/API_GetGatewayResponses.md") map that
contains two [GatewayResponse](../api/API_GatewayResponse.md "../api/API_GatewayResponse.md") instances—one for the `DEFAULT_4XX`
type and another for the `INVALID_API_KEY` type.

```
{
  "x-amazon-apigateway-gateway-responses": {
    "DEFAULT_4XX": {
      "responseParameters": {
        "gatewayresponse.header.Access-Control-Allow-Origin": "'domain.com'"
      },
      "responseTemplates": {
        "application/json": "{\"message\": test 4xx b }"
      }
    },
    "INVALID_API_KEY": {
      "statusCode": "429",
      "responseTemplates": {
        "application/json": "{\"message\": test forbidden }"
      }
    }
  }
}
```
