# x-amazon-apigateway-request-validators object

Defines the supported request validators for the containing API as a map between a validator name and the associated request validation rules. This extension applies to a REST API.

| Property name            | Type                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_validator_name` | [x-amazon-apigateway-request-validators.requestValidator object](api-gateway-swagger-extensions-request-validators.md "api-gateway-swagger-extensions-request-validators.md") | Specifies the validation rules consisting of the named validator.<br>For example:<br>`<br>"basic" : {<br>"validateRequestBody" : true,<br>"validateRequestParameters" : true<br>},<br>`<br>To apply this validator to a specific method, reference the validator name (`basic`) as the value of the [x-amazon-apigateway-request-validator property](api-gateway-swagger-extensions-request-validator.md "api-gateway-swagger-extensions-request-validator.md") property. |

## `x-amazon-apigateway-request-validators` example

The following example shows a set of request validators for an API as a map between a validator name and the associated request validation rules.

OpenAPI 2.0

```
{
  "swagger": "2.0",
  ...
  "x-amazon-apigateway-request-validators" : {
    "basic" : {
      "validateRequestBody" : true,
      "validateRequestParameters" : true
    },
    "params-only" : {
      "validateRequestBody" : false,
      "validateRequestParameters" : true
    }
  },
  ...
}
```
