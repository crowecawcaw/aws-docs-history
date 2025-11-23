# General helper methods

This page provides additional helper methods inside CloudFront Functions. To use these methods,
create a CloudFront function using JavaScript runtime 2.0.

```
import cf from 'cloudfront';
```

For more information, see [JavaScript runtime 2.0 features for
CloudFront Functions](functions-javascript-runtime-20.md "functions-javascript-runtime-20.md").

## `edgeLocation` metadata

This method requires using the `cloudfront` module.

###### Note

You can only use this method for viewer-request functions. For viewer-response
functions, this method is empty.

Use this JavaScript object to obtain the edge location airport code, expected [Regional Edge Cache](HowCloudFrontWorks.md#CloudFrontRegionaledgecaches "HowCloudFrontWorks.md#CloudFrontRegionaledgecaches") region or the CloudFront
server IP address used to handle the request. This metadata is available only the viewer
request event trigger.

```
cf.edgeLocation = {
    name: SEA
    serverIp: 1.2.3.4
    region: us-west-2
}
```

The `cf.edgeLocation` object can contain the following:

**name**

The three-letter [IATA code](https://en.wikipedia.org/wiki/IATA_airport_code "https://en.wikipedia.org/wiki/IATA_airport_code")
of the edge location that handled the request.

**serverIp**

The IPv4 or IPv6 address of the server that handled the request.

**region**

The CloudFront Regional Edge Cache (REC) that the request is
_expected_ to use if there is a cache miss. This
value is not updated in the event that the expected REC is unavailable and a
backup REC is used for the request. This doesn't include the Origin Shield
location being used, except in cases when the primary REC and the Origin
Shield are the same location.

###### Note

CloudFront Functions isn't invoked a second time when CloudFront is configured to use origin
failover. For more information, see [Optimize high availability with CloudFront
origin failover](high_availability_origin_failover.md "high_availability_origin_failover.md").

## `rawQueryString()` method

This method doesn't require the `cloudFront` module.

Use the `rawQueryString()` method to retrieve the unparsed and unaltered query string as a string.

**Request**

```
function handler(event) {
    var request = event.request;
    const qs = request.rawQueryString();
}
```

**Response**

Returns the full query string of the incoming request as a string value without the
leading `?`.

- If there isn't a query string, but the `?` is present, the
  functions returns an empty string.
- If there isn't a query string and the `?` isn't present, the
  function returns `undefined`.

**Case 1: Full query string returned (without leading `?`)**

Incoming request URL:
`https://example.com/page?name=John&age=25&city=Boston`

`rawQueryString()` returns: `"name=John&age=25&city=Boston"`

**Case 2: Empty string returned (when `?` is present but without
parameters)**

Incoming request URL: `https://example.com/page?`

`rawQueryString()` returns: `""`

**Case 3: `undefined` returned (no query string and no
`?`)**

Incoming request URL: `https://example.com/page`

`rawQueryString()` returns: `undefined`
