# x-amazon-apigateway-security-policy

Specifies a security policy for a REST API. If you create a security policy that starts with
`"SecurityPolicy_"`, you must also set the
[endpoint access mode](openapi-extensions-endpoint-access-mode.md "openapi-extensions-endpoint-access-mode.md"). To learn more about security
policies, see [Security policies for REST APIs in API Gateway](apigateway-security-policies.md "apigateway-security-policies.md").

## `x-amazon-apigateway-security-policy` example

The following example specifies
`SecurityPolicy_TLS13_1_3_2025_0` for a REST API.

```
"x-amazon-apigateway-security-policy": "SecurityPolicy_TLS13_1_3_2025_09"
```
