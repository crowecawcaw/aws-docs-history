# x-amazon-apigateway-gateway-responses.responseTemplates object

Defines [GatewayResponse](../api/API_GatewayResponse.md "../api/API_GatewayResponse.md") mapping templates, as a string-to-string map of key-value
pairs, for a given gateway response. For each key-value pair, the key is the content
type. For example, "application/json" and the value is a stringified mapping template
for simple variable substitutions. A `GatewayResponse` mapping template isn't
processed by the [Velocity
Template Language (VTL)](https://velocity.apache.org/engine/devel/vtl-reference.html "https://velocity.apache.org/engine/devel/vtl-reference.html") engine.

| Property name  | Type     | Description                                                                                                                  |
| -------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `content-type` | `string` | A `GatewayResponse` body mapping template supporting only simple variable substitution to customize a gateway response body. |

## x-amazon-apigateway-gateway-responses.responseTemplates example

The following OpenAPI extensions example shows a [GatewayResponse](../api/API_GatewayResponse.md "../api/API_GatewayResponse.md") mapping
template to customize an API Gateway–generated error response into an app-specific
format.

```

      "responseTemplates": {
        "application/json": "{ \"message\": $context.error.messageString, \"type\":$context.error.responseType, \"statusCode\": '488' }"
      }
```

The following OpenAPI extensions example shows a [GatewayResponse](../api/API_GatewayResponse.md "../api/API_GatewayResponse.md") mapping
template to override an API Gateway–generated error response with a static error
message.

```

      "responseTemplates": {
        "application/json": "{ \"message\": 'API-specific errors' }"
      }
```
