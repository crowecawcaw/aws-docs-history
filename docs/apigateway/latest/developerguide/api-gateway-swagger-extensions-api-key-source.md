# x-amazon-apigateway-api-key-source property

Specify the source to receive an API key to throttle API methods that require a key. This API-level property
is a `String` type. For more information about configuring a method to require an API key, see [Configure a method to use API keys with an OpenAPI definition](api-key-usage-plan-oas.md "api-key-usage-plan-oas.md").

Specify the source of the API key for requests. Valid values are:

- `HEADER` for receiving the API key from the `X-API-Key`
  header of a request.
- `AUTHORIZER` for receiving the API key from the
  `UsageIdentifierKey` from a Lambda authorizer (formerly known as a custom authorizer).

## x-amazon-apigateway-api-key-source example

The following example sets the `X-API-Key` header as the API key
source.

OpenAPI 2.0

```
{
  "swagger" : "2.0",
  "info" : {
    "title" : "Test1"
   },
  "schemes" : [ "https" ],
  "basePath" : "/import",
  "x-amazon-apigateway-api-key-source" : "HEADER",
   .
   .
   .
}
```

OpenAPI 3.0.1

```
{
  "openapi" : "3.0.1",
  "info" : {
    "title" : "Test1"
  },
  "servers" : [ {
    "url" : "/{basePath}",
    "variables" : {
      "basePath" : {
        "default" : "import"
      }
    }
  } ],
  "x-amazon-apigateway-api-key-source" : "HEADER",
   .
   .
   .
}
```
