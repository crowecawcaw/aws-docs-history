# HttpApiCorsConfiguration

Manage cross-origin resource sharing (CORS) for your HTTP APIs. Specify the domain to allow as a string or specify a dictionary with additional Cors configuration. NOTE: Cors requires SAM to modify your OpenAPI definition, so it only works with inline OpenApi defined in the `DefinitionBody` property.

For more information about CORS, see [Configuring CORS for an HTTP API](../../../apigateway/latest/developerguide/http-api-cors.md "../../../apigateway/latest/developerguide/http-api-cors.md") in the _API Gateway Developer Guide_.

Note: If HttpApiCorsConfiguration is set both in OpenAPI and at the property level, AWS SAM merges them with the properties taking precedence.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  AllowCredentials: `Boolean`
  AllowHeaders: `List`
  AllowMethods: `List`
  AllowOrigins: `List`
  ExposeHeaders: `List`
  MaxAge: `Integer`

```

## Properties

`AllowCredentials`

Specifies whether credentials are included in the CORS request.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`AllowHeaders`

Represents a collection of allowed headers.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`AllowMethods`

Represents a collection of allowed HTTP methods.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`AllowOrigins`

Represents a collection of allowed origins.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`ExposeHeaders`

Represents a collection of exposed headers.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`MaxAge`

The number of seconds that the browser should cache preflight request results.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### HttpApiCorsConfiguration

HTTP API Cors Configuration example.

#### YAML

```
CorsConfiguration:
  AllowOrigins:
    - "https://example.com"
  AllowHeaders:
    - x-apigateway-header
  AllowMethods:
    - GET
  MaxAge: 600
  AllowCredentials: true

```
