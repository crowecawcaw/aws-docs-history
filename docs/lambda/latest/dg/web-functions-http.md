

# HTTP requests and responses
<a name="web-functions-http"></a>

A Web Function endpoint accepts HTTP/1.1 requests and forwards them to your application over HTTP/1.1. Lambda rejects HTTP/1.0 requests with HTTP 505 (HTTP Version Not Supported). Lambda preserves the request method, path, query string, body, and most headers. It removes or changes headers that describe the connection between the client and the endpoint. It also adds headers that provide request context.

## HTTP methods
<a name="web-functions-http-methods"></a>

Web Function endpoints support `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `OPTIONS`, and `DELETE`.

Lambda rejects an unsupported method with an HTTP 400 response before the request reaches your application.

## Request headers
<a name="web-functions-http-request-headers"></a>

Lambda removes the following headers before it forwards a request:
+ `Connection`, `Keep-Alive`, `Upgrade`, `Expect`, `TE`, and `Trailer`
+ `Proxy-Authenticate`, `Proxy-Authorization`, and `Proxy-Connection`
+ `X-Real-IP`
+ `X-HTTP-Method-Override`, `X-HTTP-Method`, and `X-Method-Override`
+ Headers whose names begin with `lambda-web-`, and headers named in the `Connection` header

Lambda validates or changes the following headers.


| Header | Behavior | 
| --- | --- | 
| Host | Must be the Web Function endpoint domain name (for example, bcdfghjklmnpqrst.b7t.lambda-web.us-east-1.on.aws), in lowercase and without a port. Lambda routes on this value and returns HTTP 404 if it doesn't match an endpoint, or HTTP 400 if the header is missing. Your application receives the endpoint domain name. | 
| X-Forwarded-For | Lambda appends the IP address of the connecting client as the last value. Earlier values come from the client and aren't validated. When a Amazon CloudFront distribution is in front of the endpoint, the last value is a CloudFront address. | 

Lambda forwards `X-Forwarded-Host` from the client without validation. Don't use it to build redirects, absolute URLs, or host-based authorization unless a front door that you control sets it.

Lambda adds the following headers.


| Header | Description | 
| --- | --- | 
| lambda-web-request-id | The identifier that Lambda assigns to the request. | 
| lambda-web-endpoint-name | The name of the endpoint that received the request. | 

For endpoints that use IAM authorization, Lambda validates the signed request and removes the `Authorization` header before forwarding it. For more information, see [Using the `IamAuth` authentication type](web-functions-endpoint-access-control.md#web-functions-endpoint-access-control-iam).

## Response headers
<a name="web-functions-http-response-headers"></a>

Lambda removes connection-scoped headers and HTTP trailers from your application's response. Depending on the result of the request, Lambda can add the following headers.


| Header | Description | 
| --- | --- | 
| lambda-web-request-id | The request identifier. Use it to correlate a response with application and system logs. | 
| lambda-web-logstream | The Amazon CloudWatch Logs log stream that contains logs for the execution environment that handled the request. | 
| lambda-web-error-type | The error type, in the format <Prefix>.<ErrorReason> (for example, Platform.EndpointRequestThrottle or Runtime.RequestTimeout). Lambda omits this header for internal service errors and authorization failures. For the list of values, see [Web Function error types](web-functions-troubleshooting.md#web-functions-troubleshooting-error-types). | 

## Header limits
<a name="web-functions-http-header-limits"></a>

The request line, request headers, and terminating blank line can total up to 128 KiB. Lambda rejects a request that exceeds this limit with HTTP 431 (Request Header Fields Too Large) before the request reaches your application. For troubleshooting, see [Request header limits](web-functions-troubleshooting.md#web-functions-troubleshooting-header-limits).