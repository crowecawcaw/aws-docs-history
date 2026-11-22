

# Pass JWT claims to your integration

After a JWT authorizer validates a token, API Gateway makes the token's claims available to the integration. You reference a claim with `$context.authorizer.claims.{{property}}`, where {{property}} is the claim name. For more information about context variables, see [Variables for data transformations for API Gateway](api-gateway-mapping-template-reference.md).

Each claim value is JSON, so the string `"42"` and the number `42` stay distinct. A Lambda proxy integration receives each claim with its JSON type. Parameter mappings, mapping templates, and access logs receive each claim as JSON text.

API Gateway writes each non-ASCII character as a Unicode escape sequence. For example, `é` becomes `\u00E9`. A JSON parser converts the sequence back to the original character.

You can reference top-level claims only. For example, `$context.authorizer.claims.address.city` isn't a valid context variable. To read `city`, reference `address` and parse the value.

## Example claim values
<a name="rest-api-jwt-authorizer-claims.example"></a>

The examples on this page use a token with the following claims:

```json
{
  "name": "Doe, \"Jane\"",
  "iat": 1516239022,
  "version": "42",
  "roles": ["user", "editor"],
  "address": {"city": "Seattle"}
}
```

The token produces the following values.


| Context variable | Value | 
| --- | --- | 
| $context.authorizer.claims.name | "Doe, \\"Jane\\"" | 
| $context.authorizer.claims.iat | 1516239022 | 
| $context.authorizer.claims.version | "42" | 
| $context.authorizer.claims.roles | ["user","editor"] | 
| $context.authorizer.claims.address | {"city":"Seattle"} | 

## Lambda proxy integrations
<a name="rest-api-jwt-authorizer-claims.lambda"></a>

A Lambda proxy integration receives the claims in the `requestContext.authorizer.claims` object of the input event. Each claim keeps its JSON type. The event omits other fields. For the example token, the event contains the following:

```json
{
  "requestContext": {
    "authorizer": {
      "claims": {
        "name": "Doe, \"Jane\"",
        "iat": 1516239022,
        "version": "42",
        "roles": ["user","editor"],
        "address": {"city": "Seattle"}
      }
    }
  }
}
```

## Mapping templates
<a name="rest-api-jwt-authorizer-claims.mapping"></a>

A mapping template can reference a claim directly. Because each value is already JSON text, don't put quotation marks around the variable and don't apply `$util.escapeJavaScript()` to it. The following request mapping template sends two claims in the request body.

```
{
  "version": $context.authorizer.claims.version,
  "roles": $context.authorizer.claims.roles
}
```

For the example token, the integration receives the following body:

```json
{
  "version": "42",
  "roles": ["user","editor"]
}
```

## HTTP proxy integrations
<a name="rest-api-jwt-authorizer-claims.http"></a>

An HTTP proxy integration does not forward authorizer context on its own. To pass a claim to an HTTP backend, map the claim to a request header in the integration request. For example, map `integration.request.header.x-roles` to `context.authorizer.claims.roles`. For the example token, the backend receives the following header:

```
x-roles: ["user","editor"]
```

The header contains the claim's JSON text. To get the original value, parse the header value as JSON. For more information about mapping request parameters, see [Parameter mapping for REST APIs in API Gateway](rest-api-parameter-mapping.md).