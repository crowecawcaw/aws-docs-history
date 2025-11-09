# x-amazon-apigateway-integration.response object

Defines a response and specifies parameter mappings or payload mappings from the
integration response to the method response.

| Property name        | Type                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `statusCode`         | `string`                                                                                                                                                                                         | HTTP status code for the method response; for example,<br>`"200"`. This must correspond to a matching response<br>in the [OpenAPI Operation](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#operation-object "https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#operation-object")<br>`responses` field.                                                                                                      |
| `responseTemplates`  | [x-amazon-apigateway-integration.responseTemplates object](api-gateway-swagger-extensions-integration-responseTemplates.md "api-gateway-swagger-extensions-integration-responseTemplates.md")    | Specifies MIME type-specific mapping templates for the response’s<br>payload.                                                                                                                                                                                                                                                                                                                                                                              |
| `responseParameters` | [x-amazon-apigateway-integration.responseParameters object](api-gateway-swagger-extensions-integration-responseParameters.md "api-gateway-swagger-extensions-integration-responseParameters.md") | Specifies parameter mappings for the response. Only the<br>`header` and `body` parameters of the<br>integration response can be mapped to the `header`<br>parameters of the method.                                                                                                                                                                                                                                                                        |
| `contentHandling`    | `string`                                                                                                                                                                                         | Response payload encoding conversion types. Valid values are<br>1)<br>`CONVERT_TO_TEXT`, for converting a<br>binary payload into a base64-encoded string or converting a text payload<br>into a `utf-8`-encoded string or passing<br>through the text payload natively without modification, and 2) `CONVERT_TO_BINARY`, for converting a text<br>payload into a base64-decoded blob or passing through a binary payload<br>natively without modification. |

## `x-amazon-apigateway-integration.response` example

The following example defines a `302` response for the method that
derives a payload of the `application/json` or
`application/xml` MIME type from the backend. The response uses the
supplied mapping templates and returns the redirect URL from the integration
response in the method's `Location` header.

```

{
    "statusCode" : "302",
    "responseTemplates" : {
         "application/json" : "#set ($root=$input.path('$')) { \"stage\": \"$root.name\", \"user-id\": \"$root.key\" }",
         "application/xml" : "#set ($root=$input.path('$')) <stage>$root.name</stage> "
    },
    "responseParameters" : {
        "method.response.header.Location": "integration.response.body.redirect.url"
    }
}


```
