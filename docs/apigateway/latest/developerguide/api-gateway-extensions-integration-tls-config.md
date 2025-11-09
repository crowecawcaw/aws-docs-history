# x-amazon-apigateway-integration.tlsConfig object

Specifies the TLS configuration for an integration.

| Property name              | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `insecureSkipVerification` | `Boolean` | Supported only for REST APIs. Specifies whether or not API Gateway skips verification that the certificate for an integration endpoint is<br>issued by a [supported certificate authority](api-gateway-supported-certificate-authorities-for-http-endpoints.md "api-gateway-supported-certificate-authorities-for-http-endpoints.md"). This isn’t recommended, but it enables you to<br>use certificates that are signed by private certificate authorities, or certificates<br>that are self-signed. If enabled, API Gateway still performs basic certificate<br>validation, which includes checking the certificate's expiration date, hostname, and<br>presence of a root certificate authority. The root certificate belonging to the private authority must satisfy the following constraints:<br>• x509 extension `keyUsage` must have `keyCertSign`.<br>• x509 extension `basicConstraints` must have `CA:TRUE`.<br>Supported only for `HTTP` and<br>`HTTP_PROXY` integrations.<br>WarningEnabling `insecureSkipVerification` isn't recommended, especially for integrations with public<br>HTTPS endpoints. If you enable `insecureSkipVerification`, you increase the risk of man-in-the-middle attacks. |
| `serverNameToVerify`       | `string`  | Supported only for HTTP API private integrations. If you specify a server name,<br>API Gateway uses it to verify the hostname on the integration's<br>certificate. The server name is also included in the TLS handshake<br>to support Server Name Indication (SNI) or virtual hosting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## x-amazon-apigateway-integration.tlsConfig examples

The following OpenAPI 3.0 example enables `insecureSkipVerification` for a REST API HTTP proxy integration.

```
"x-amazon-apigateway-integration": {
  "uri": "http://petstore-demo-endpoint.execute-api.com/petstore/pets",
  "responses": {
     default": {
       "statusCode": "200"
      }
  },
  "passthroughBehavior": "when_no_match",
  "httpMethod": "ANY",
  "tlsConfig" : {
    "insecureSkipVerification" : true
  }
  "type": "http_proxy",
}
```

The following OpenAPI 3.0 example specifies a `serverNameToVerify` for an HTTP API private integration.

```
"x-amazon-apigateway-integration" : {
  "payloadFormatVersion" : "1.0",
  "connectionId" : "abc123",
  "type" : "http_proxy",
  "httpMethod" : "ANY",
  "uri" : "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65",
  "connectionType" : "VPC_LINK",
  "tlsConfig" : {
     "serverNameToVerify" : "example.com"
  }
}
```
