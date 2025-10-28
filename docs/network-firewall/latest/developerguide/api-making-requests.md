# Making HTTPS requests to AWS Network Firewall

Network Firewall requests are HTTPS requests, as defined by [RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616 "https://datatracker.ietf.org/doc/html/rfc2616").
Like any HTTP request, a request to Network Firewall contains a request method, a URI, request headers, and a request body.
The response contains an HTTP status code, response headers, and sometimes a response body.

## Request URI

The request URI is always a single forward slash, `/`.

## HTTP headers

Network Firewall requires the following information in the header of an HTTP request.

**Host (Required)**
The endpoint that specifies where your resources are created. You can find the various endpoints in [AWS service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md"). For example, the value of the `Host`
header for Network Firewall for a CloudFront distribution is `network-firewall.amazonaws.com:443`.

**x-amz-date or Date (Required)**
The date used to create the signature that is contained in the `Authorization`
header. Specify the date in ISO 8601 standard format, in UTC time, as
shown in the following example:

```
x-amz-date: 20151007T174952Z
```

You must include either `x-amz-date` or `Date`. (Some HTTP client libraries don't let you set the
`Date` header). When an `x-amz-date` header is present, Network Firewall ignores any `Date` header
when authenticating the request.

The timestamp must be within 15 minutes of the AWS system time when the request is
received. If it isn't, the request fails with the
`RequestExpired` error code to prevent someone else from
replaying your requests.

**Authorization (Required)**
The information required for request authentication. For more information about constructing this header,
see [Authenticating requests](authenticating-requests.md "authenticating-requests.md").

**X-Amz-Target (Required)**
The operation, provided as a concatenation of the following values:

- `NetworkFirewall_`
- `The API version without punctuation`
- `A period (`.`)`
- `The name of the operation`

Example:

`NetworkFirewall_20201112.CreateFirewall`

**Content-Type (Conditional)**
The type and version of the content. Specify the version of JSON, as shown in the following example:

```
Content-Type: application/x-amz-json-1.0
```

Condition: Required for POST requests.

**Content-Length (Conditional)**
The length of the message, without the headers, according to RFC 2616.

Condition: Required if the request body itself contains information. Most toolkits add this header automatically.

The following is an example header for an HTTP request to create a firewall in Network Firewall:

```
POST / HTTP/1.1
Host: network-firewall.amazonaws.com:443
X-Amz-Date: 20151007T174952Z
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAIOSFODNN7EXAMPLE/20151007/us-east-2/network-firewall/aws4_request,
               SignedHeaders=host;x-amz-date;x-amz-target,
               Signature=145b1567ab3c50d929412f28f52c45dbf1e63ec5c66023d232a539a4afd11fd9
X-Amz-Target: NetworkFirewall_20201112.CreateFirewall
Accept: */*
Content-Type: application/x-amz-json-1.0; charset=UTF-8
Content-Length: 231
Connection: Keep-Alive
```

## HTTP request body

Many Network Firewall API actions require you to include JSON-formatted data in the
body of the request.
