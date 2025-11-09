# Set up data mapping for

WebSocket APIs in API Gateway

_Data mapping_ enables you to map data from a [route request](api-gateway-basic-concept.md#apigateway-definition-route-request "api-gateway-basic-concept.md#apigateway-definition-route-request") to a backend
integration.

###### Note

Data mapping for WebSocket APIs isn't supported in the AWS Management Console. You must use the
AWS CLI, AWS CloudFormation, or an SDK to configure data mapping.

###### Topics

- [Map route request data to integration
  request parameters](#websocket-mapping-request-parameters "#websocket-mapping-request-parameters")
- [Examples](#websocket-data-mapping-examples "#websocket-data-mapping-examples")

## Map route request data to integration

request parameters

Integration request parameters can be mapped from any defined route request
parameters, the request body, [context or](api-gateway-mapping-template-reference.md#context-variable-reference "api-gateway-mapping-template-reference.md#context-variable-reference") [stage](api-gateway-mapping-template-reference.md#stagevariables-template-reference "api-gateway-mapping-template-reference.md#stagevariables-template-reference") variables, and static values.

The following table shows integration request data mapping expressions. In the table, `PARAM_NAME` is the name
of a route request parameter of the given parameter type. It must match the regular
expression `'^[a-zA-Z0-9._$-]+$]'`.
`JSONPath_EXPRESSION` is a JSONPath expression for a JSON field of the request body.

| Mapped data source                                                            | Mapping expression                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Request query string (supported only for the `$connect`<br>route)             | `route.request.querystring.`PARAM_NAME``                                                                                                                                                                                            |
| Request header (supported only for the `$connect`<br>route)                   | `route.request.header.`PARAM_NAME``                                                                                                                                                                                                 |
| Multi-value request query string (supported only for the<br>`$connect` route) | `route.request.multivaluequerystring.`PARAM_NAME``                                                                                                                                                                                  |
| Multi-value request header (supported only for the<br>`$connect` route)       | `route.request.multivalueheader.`PARAM_NAME``                                                                                                                                                                                       |
| Request body                                                                  | `route.request.body.`JSONPath_EXPRESSION``                                                                                                                                                                                          |
| Stage variables                                                               | `stageVariables.`VARIABLE_NAME``                                                                                                                                                                                                    |
| Context variables                                                             | `context.`VARIABLE_NAME`` that<br>must be one of the [supported<br>context variables](api-gateway-mapping-template-reference.md#context-variable-reference "api-gateway-mapping-template-reference.md#context-variable-reference"). |
| Static value                                                                  | `'STATIC_VALUE'`. The<br>`STATIC_VALUE` is a string literal and must<br>be enclosed in single quotes.                                                                                                                               |

When you create a data mapping, using the AWS CLI make sure to follow the correct format for using literals with
strings in the AWS CLI. For more information, see [Using quotation marks and literals with strings in the AWS CLI](../../../cli/latest/userguide/cli-usage-parameters-quoting-strings.md "../../../cli/latest/userguide/cli-usage-parameters-quoting-strings.md") in the _AWS Command Line Interface User Guide_.

## Examples

The following AWS CLI examples configure data mappings. For an example AWS CloudFormation template,
see [`websocket-data-mapping.yaml`](samples/websocket-data-mapping.md "samples/websocket-data-mapping.md").

### Map a client's

connectionId to a header in an integration request

The following [update-integration](../../../cli/latest/reference/apigatewayv2/update-integration.md "../../../cli/latest/reference/apigatewayv2/update-integration.md")
command maps a client's `connectionId` to a `connectionId` header in the request to a
backend integration:

```
aws apigatewayv2 update-integration \
    --integration-id abc123 \
    --api-id a1b2c3d4 \
    --request-parameters 'integration.request.header.connectionId'='context.connectionId'
```

### Map a query string

parameter to a header in an integration request

The following example
maps an `authToken` query string parameter to an `authToken` header in the integration
request.

1. Use the following [update-route](../../../cli/latest/reference/apigatewayv2/update-route.md "../../../cli/latest/reference/apigatewayv2/update-route.md") command
   to add the `authToken` query string parameter to the route's request parameters.

```
aws apigatewayv2 update-route --route-id 0abcdef \
    --api-id a1b2c3d4 \
    --request-parameters '{"route.request.querystring.authToken": {"Required": false}}'
```

2. Use the following [update-integration](../../../cli/latest/reference/apigatewayv2/update-integration.md "../../../cli/latest/reference/apigatewayv2/update-integration.md") command to map the query string parameter to the `authToken` header
   in the request to the backend integration.

```
aws apigatewayv2 update-integration \
    --integration-id abc123 \
    --api-id a1b2c3d4 \
    --request-parameters 'integration.request.header.authToken'='route.request.querystring.authToken'
```

3. (Optional) If necessary, use the following [delete-route-request-parameter](../../../cli/latest/reference/apigatewayv2/delete-route-request-parameter.md "../../../cli/latest/reference/apigatewayv2/delete-route-request-parameter.md")
   to delete the `authToken` query string parameter from the route's request parameters.

```
aws apigatewayv2 delete-route-request-parameter \
    --route-id 0abcdef \
    --api-id a1b2c3d4 \
    --request-parameter-key 'route.request.querystring.authToken'
```
