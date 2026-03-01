# x-amazon-apigateway-minimum-compression-size

Specifies the minimum compression size for a REST API. To enable compression, specify
an integer between 0 and 10485760. To learn more, see [Payload compression for REST APIs in API Gateway](api-gateway-gzip-compression-decompression.md "api-gateway-gzip-compression-decompression.md").

## x-amazon-apigateway-minimum-compression-size example

The following example specifies a minimum compression size of `5242880` bytes for a REST API.

```
"x-amazon-apigateway-minimum-compression-size": 5242880
```
