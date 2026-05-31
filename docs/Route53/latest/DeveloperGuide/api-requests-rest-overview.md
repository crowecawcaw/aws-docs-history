# REST Requests

Amazon Route 53 REST requests are HTTPS requests, as defined by [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt "https://www.ietf.org/rfc/rfc2616.txt"). This section describes the structure of an
Route 53 REST request.

A typical REST action consists of sending a single HTTPS request to Route 53, and waiting for the response. Like any HTTP request,
a REST request to Route 53 contains a request method, a URI, request headers, and sometimes a query string or request body.
The response contains an HTTP status code, response headers, and sometimes a response body.

## Request URI

The request URI always starts with a forward slash and then the version of the Route 53 API you use (for example, 2013-04-01).
The remainder of the URI indicates the particular resource you want to act on. For example, following is the URI you use
when creating a new hosted zone. (For more information, see [CreateHostedZone](../APIReference/API_CreateHostedZone.md "../APIReference/API_CreateHostedZone.md").)

```
/2013-04-01/hostedzone
```

## About the Request Time Stamp

You must provide the time stamp in either the HTTP `Date` header or the AWS `x-amz-date` header
(some HTTP client libraries don't let you set the `Date` header). When an `x-amz-date` header is present,
the system ignores any `Date` header when authenticating the request.

The time stamp must be within 5 minutes of the AWS system time when the request is received. If it isn't, the request
fails with the `RequestExpired` error code. This is to prevent replays of your requests by an adversary.

The date must be specified in ISO 8601 format, for example, `2016-03-03T19:20:25.177Z`. For more information
about ISO 8601 format, see the Wikipedia article [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601").

## Request Body

Many of the Route 53 API actions require you to include XML in the body of the request.
The XML conforms to the Route 53 schema.

###### Example Request

The following example request uses a simple XML statement to create a hosted zone named example.com
with the reference identifier, _myUniqueIdentifier_.

The XML elements in your request must appear in the order listed.

```
POST /2013-04-01/hostedzone HTTP/1.1
host:route53.amazonaws.com
x-amz-date:`date and time of the request`
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/`date of the request in yyyymmdd format`/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=`computed signature`
`[Other required headers]`

<?xml version="1.0" encoding="UTF-8"?>
<CreateHostedZoneRequest xmlns="https://route53.amazonaws.com/
doc/2013-04-01/">
   <Name>`example.com.`</Name>
   <CallerReference>`myUniqueIdentifier`</CallerReference>
   <HostedZoneConfig>
      <Comment>`This is my hosted zone.`</Comment>
   </HostedZoneConfig>
</CreateHostedZoneRequest>

```
