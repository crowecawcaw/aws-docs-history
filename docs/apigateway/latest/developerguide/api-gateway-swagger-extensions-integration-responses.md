# x-amazon-apigateway-integration.responses object

Defines the method's responses and specifies parameter mappings or payload mappings
from integration responses to method responses.

| Property name             | Type                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Response status pattern` | [x-amazon-apigateway-integration.response object](api-gateway-swagger-extensions-integration-response.md "api-gateway-swagger-extensions-integration-response.md") | Either a regular expression used to match the integration<br>response to the method response, or `default` to catch any response that you haven't configured.<br>For HTTP integrations, the regex applies to the integration response status code. For Lambda<br>invocations, the regex applies to the `errorMessage`<br>field of the error information object returned by AWS Lambda as a<br>failure response body when the Lambda function execution throws an exception.<br>NoteThe `Response status pattern` property<br>name refers to a response status code or regular expression<br>describing a group of response status codes. It does not correspond<br>to any identifier of an [IntegrationResponse](../api/API_IntegrationResponse.md "../api/API_IntegrationResponse.md") resource in the API Gateway REST<br>API. |

## `x-amazon-apigateway-integration.responses` example

The following example shows a list of responses from `2xx` and
`302` responses. For the `2xx` response, the method
response is mapped from the integration response's payload of the
`application/json` or `application/xml` MIME type. This
response uses the supplied mapping templates. For the `302` response, the
method response returns a `Location` header whose value is derived from
the `redirect.url` property on the integration response's payload.

```

"responses" : {
    "2\\d{2}" : {
        "statusCode" : "200",
        "responseTemplates" : {
            "application/json" : "#set ($root=$input.path('$')) { \"stage\": \"$root.name\", \"user-id\": \"$root.key\" }",
            "application/xml" : "#set ($root=$input.path('$')) <stage>$root.name</stage> "
        }
    },
    "302" : {
        "statusCode" : "302",
        "responseParameters" : {
            "method.response.header.Location": "integration.response.body.redirect.url"
        }
    }
}


```
