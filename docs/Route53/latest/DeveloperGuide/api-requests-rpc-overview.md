

# RPC Requests
<a name="api-requests-rpc-overview"></a>

Amazon Route 53 RPC requests are HTTPS requests, as defined by [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt). This section describes the structure of an Route 53 RPC request. 

For an RPC action, you send an HTTPS request to Route 53 and wait for the response. An RPC request to Route 53 contains request headers and sometimes a query string or request body. The response contains an HTTP status code, response headers, and sometimes a response body.

## About the Request Time Stamp
<a name="api-requests-rpc-time-stamp"></a>

You must provide the time stamp in either the HTTP `Date` header or the AWS `x-amz-date` header (some HTTP client libraries don't let you set the `Date` header). When an `x-amz-date` header is present, the system ignores any `Date` header when authenticating the request.

The time stamp must be within 5 minutes of the AWS system time when the request is received. If it isn't, the request fails with the `RequestExpired` error code. This helps prevent someone else from resubmitting a request.

The date must be specified in ISO 8601 format, for example, `2016-03-03T19:20:25.177Z`. For more information, see the Wikipedia article [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

## Request Body
<a name="api-requests-rpc-body"></a>

Many Route 53 API actions require you to include JSON in the body of the request. The JSON conforms to the Route 53 schema for either domain registration or Route 53 Resolver. 

**Example Request**  
The following example request uses a simple JSON statement to determine whether the domain name `example.com` is available.  
The JSON elements in your request must appear in the order listed.  

```
 1. POST / HTTP/1.1  
 2. host:route53domains.us-east-1.amazonaws.com
 3. x-amz-date:{{date and time of the request}}
 4. authorization:AWS4-HMAC-SHA256
 5.               Credential=AKIAIOSFODNN7EXAMPLE/{{date of the request in yyyymmdd format}}/us-east-1/route53domains/aws4_request,
 6.               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
 7.               Signature={{computed signature}}
 8. x-amz-target:Route53Domains_v20140515.CheckDomainAvailability 
 9. user-agent:{{information about the source of the request}} 
10. content-type:application/x-amz-json- 1.1
11. content-length:{{length}}
12. connections:Keep-Alive
13. {
14.    "DomainName":"example.com"
15. }
```