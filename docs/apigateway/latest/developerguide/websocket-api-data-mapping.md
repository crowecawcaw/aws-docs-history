

# Set up data mapping for WebSocket APIs in API Gateway
<a name="websocket-api-data-mapping"></a>

*Data mapping* enables you to map data from a [route request](api-gateway-basic-concept.md#apigateway-definition-route-request) to a backend integration.

**Note**  
Data mapping for WebSocket APIs isn't supported in the AWS Management Console. You must use the AWS CLI, AWS CloudFormation, or an SDK to configure data mapping.

**Topics**
+ [Map route request data to integration request parameters](#websocket-mapping-request-parameters)
+ [Examples](#websocket-data-mapping-examples)

## Map route request data to integration request parameters
<a name="websocket-mapping-request-parameters"></a>

Integration request parameters can be mapped from any defined route request parameters, the request body, [`context` or ](api-gateway-mapping-template-reference.md#context-variable-reference) [`stage`](api-gateway-mapping-template-reference.md#stagevariables-template-reference) variables, and static values.

The following table shows integration request data mapping expressions. In the table, {{`PARAM_NAME`}} is the name of a route request parameter of the given parameter type. It must match the regular expression `'^[a-zA-Z0-9._$-]+$]'`. {{JSONPath\_EXPRESSION}} is a JSONPath expression for a JSON field of the request body.


| Mapped data source | Mapping expression | 
| --- | --- | 
| Request query string (supported only for the $connect route) | route.request.querystring.{{PARAM\_NAME}} | 
| Request header (supported only for the $connect route) | route.request.header.{{PARAM\_NAME}} | 
| Multi-value request query string (supported only for the $connect route) | route.request.multivaluequerystring.{{PARAM\_NAME}} | 
| Multi-value request header (supported only for the $connect route) | route.request.multivalueheader.{{PARAM\_NAME}} | 
| Request body | route.request.body.{{JSONPath\_EXPRESSION}} | 
| Stage variables | stageVariables.{{VARIABLE\_NAME}} | 
| Context variables | context.{{VARIABLE\_NAME}} that must be one of the [supported context variables](api-gateway-mapping-template-reference.md#context-variable-reference). | 
| Static value | {{'STATIC\_VALUE'}}. The {{STATIC\_VALUE}} is a string literal and must be enclosed in single quotes. | 

When you create a data mapping, using the AWS CLI make sure to follow the correct format for using literals with strings in the AWS CLI. For more information, see [Using quotation marks and literals with strings in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS Command Line Interface User Guide*.

## Examples
<a name="websocket-data-mapping-examples"></a>

The following AWS CLI examples configure data mappings. For an example CloudFormation template, see [`websocket-data-mapping.yaml`](samples/websocket-data-mapping.zip).

### Map a client's connectionId to a header in an integration request
<a name="websocket-data-mapping-examples.connectionId"></a>

The following [update-integration](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/update-integration.html) command maps a client's `connectionId` to a `connectionId` header in the request to a backend integration:

```
aws apigatewayv2 update-integration \
    --integration-id abc123 \
    --api-id a1b2c3d4 \ 
    --request-parameters 'integration.request.header.connectionId'='context.connectionId'
```

### Map a query string parameter to a header in an integration request
<a name="websocket-data-mapping-examples.querystring"></a>

The following example maps an `authToken` query string parameter to an `authToken` header in the integration request.

1. Use the following [update-route](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/update-route.html) command to add the `authToken` query string parameter to the route's request parameters.

   ```
   aws apigatewayv2 update-route --route-id 0abcdef \
       --api-id a1b2c3d4 \
       --request-parameters '{"route.request.querystring.authToken": {"Required": false}}'
   ```

1.  Use the following [update-integration](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/update-integration.html) command to map the query string parameter to the `authToken` header in the request to the backend integration.

   ```
   aws apigatewayv2 update-integration \
       --integration-id abc123 \
       --api-id a1b2c3d4 \
       --request-parameters 'integration.request.header.authToken'='route.request.querystring.authToken'
   ```

1. (Optional) If necessary, use the following [delete-route-request-parameter](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/delete-route-request-parameter.html) to delete the `authToken` query string parameter from the route's request parameters.

   ```
   aws apigatewayv2 delete-route-request-parameter \
       --route-id 0abcdef \
       --api-id a1b2c3d4 \
       --request-parameter-key 'route.request.querystring.authToken'
   ```