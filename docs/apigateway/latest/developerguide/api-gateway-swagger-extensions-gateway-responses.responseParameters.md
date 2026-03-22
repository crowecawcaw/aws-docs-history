# x-amazon-apigateway-gateway-responses.responseParameters object

Defines a string-to-string map of key-value pairs to generate gateway response parameters from the incoming request parameters or using literal strings. Supported only for REST APIs.

| Property name                                   | Type     | Description                                                                                                                                                                                                  |
| ----------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `gatewayresponse.`param-position`.`param-name`` | `string` | `param-position` can be<br>`header`, `path`, or<br>`querystring`. For more information, see [Parameter mapping for REST APIs in API Gateway](rest-api-parameter-mapping.md "rest-api-parameter-mapping.md"). |

## x-amazon-apigateway-gateway-responses.responseParameters example

The following OpenAPI extensions example shows a
[GatewayResponse](../api/API_GatewayResponse.md "../api/API_GatewayResponse.md") response parameter mapping expression to enable CORS support for resources on the `*.example.domain` domains.

```

      "responseParameters": {
        "gatewayresponse.header.Access-Control-Allow-Origin": '*.example.domain',
        "gatewayresponse.header.from-request-header" : method.request.header.Accept,
        "gatewayresponse.header.from-request-path" : method.request.path.petId,
        "gatewayresponse.header.from-request-query" : method.request.querystring.qname
      }
```
