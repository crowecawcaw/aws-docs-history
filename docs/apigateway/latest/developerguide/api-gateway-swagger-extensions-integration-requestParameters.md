# x-amazon-apigateway-integration.requestParameters object

For REST APIs, specifies mappings from named method request parameters to integration request
parameters. The method request parameters must be defined before being referenced.

For HTTP APIs, specifies parameters that are passed to `AWS_PROXY`
integrations with a specified `integrationSubtype`.

| Property name                                       | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `integration.request.`<param-type>`.`<param-name>`` | `string` | For REST APIs, the value is typically a predefined<br>method request parameter of the<br>`method.request.`<param-type>`.`<param-name>``<br>format, where `<param-type>` can be<br>`querystring`, `path`,<br>`header`, or `body`. However,<br>`$context.`VARIABLE_NAME``,<br>`$stageVariables.`VARIABLE_NAME`,<br>and `STATIC_VALUE``are also<br>valid. For the`body` parameter, the<br>`<param-name>`is a JSON path expression<br>without the`$.` prefix.                             |
| `parameter`                                         | `string` | For HTTP APIs, request parameters are a key-value map<br>specifying parameters that are passed to `AWS_PROXY` integrations with a<br>specified `integrationSubtype`. You can provide static values, or map request<br>data, stage variables, or context variables that are evaluated at runtime. To learn<br>more, see [Create AWS service integrations for HTTP APIs in API Gateway](http-api-develop-integrations-aws-services.md "http-api-develop-integrations-aws-services.md"). |

## `x-amazon-apigateway-integration.requestParameters` example

The following request parameter mappings example translates a method request's
query (`version`), header (`x-user-id`), and path
(`service`) parameters to the integration request's query
(`stage`), header (`x-userid`), and path parameters
(`op`), respectively.

###### Note

If you're creating resources through OpenAPI or CloudFormation, static values should be
enclosed in single quotes.

To add this value from the console, enter `application/json` in the box, without quotation marks.

```

"requestParameters" : {
    "integration.request.querystring.stage" : "method.request.querystring.version",
    "integration.request.header.x-userid" : "method.request.header.x-user-id",
    "integration.request.path.op" : "method.request.path.service"
},


```
